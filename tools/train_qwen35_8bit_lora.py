"""Continue pretraining Qwen3.5 with an 8-bit base and LoRA adapters."""

from __future__ import annotations

import argparse
import json
import math
import random
from pathlib import Path

import numpy as np
import torch
from peft import LoraConfig, PeftModel, get_peft_model, prepare_model_for_kbit_training
from torch import nn
from torch.utils.data import DataLoader, Dataset
from transformers import AutoModelForImageTextToText, AutoTokenizer, BitsAndBytesConfig


def install_torch24_compatibility() -> None:
    if hasattr(nn.Module, "set_submodule"):
        return

    def set_submodule(self: nn.Module, target: str, module: nn.Module) -> None:
        atoms = target.split(".")
        parent = self.get_submodule(".".join(atoms[:-1])) if len(atoms) > 1 else self
        setattr(parent, atoms[-1], module)

    nn.Module.set_submodule = set_submodule  # type: ignore[attr-defined]


class TokenBlocks(Dataset):
    def __init__(self, path: Path, max_samples: int | None = None):
        self.blocks = np.load(path, mmap_mode="r")
        self.length = min(len(self.blocks), max_samples) if max_samples else len(self.blocks)

    def __len__(self) -> int:
        return self.length

    def __getitem__(self, index: int) -> dict[str, torch.Tensor]:
        input_ids = torch.from_numpy(np.array(self.blocks[index], dtype=np.int64, copy=True))
        return {"input_ids": input_ids, "labels": input_ids.clone()}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=Path, default=Path("model"))
    parser.add_argument("--data", type=Path, default=Path("training/tokenized-qwen35/input_ids.npy"))
    parser.add_argument("--output", type=Path, default=Path("training/qwen35-9b-8bit-lora"))
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--learning-rate", type=float, default=2e-4)
    parser.add_argument("--gradient-accumulation", type=int, default=8)
    parser.add_argument("--save-steps", type=int, default=100)
    parser.add_argument("--max-steps", type=int)
    parser.add_argument("--max-samples", type=int)
    parser.add_argument("--resume", type=Path)
    parser.add_argument("--seed", type=int, default=3407)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not torch.cuda.is_available():
        raise SystemExit("CUDA is required")
    install_torch24_compatibility()
    torch.manual_seed(args.seed)
    random.seed(args.seed)

    quantization = BitsAndBytesConfig(load_in_8bit=True)
    model = AutoModelForImageTextToText.from_pretrained(
        args.model,
        local_files_only=True,
        quantization_config=quantization,
        device_map={"": 0},
        dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
    )
    model.config.use_cache = False
    model = prepare_model_for_kbit_training(model, use_gradient_checkpointing=True)
    target_pattern = (
        r"model\.language_model\.layers\.\d+\."
        r"(?:self_attn\.(?:q_proj|k_proj|v_proj|o_proj|in_proj_qkv|in_proj_z|in_proj_b|in_proj_a|out_proj)"
        r"|mlp\.(?:gate_proj|up_proj|down_proj))"
    )
    if args.resume:
        model = PeftModel.from_pretrained(model, args.resume, local_files_only=True, is_trainable=True)
    else:
        lora_config = LoraConfig(
            r=16,
            lora_alpha=32,
            lora_dropout=0.05,
            bias="none",
            task_type="CAUSAL_LM",
            target_modules=target_pattern,
        )
        model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    dataset = TokenBlocks(args.data, args.max_samples)
    generator = torch.Generator().manual_seed(args.seed)
    loader = DataLoader(dataset, batch_size=1, shuffle=True, generator=generator, pin_memory=True)
    updates_per_epoch = math.ceil(len(loader) / args.gradient_accumulation)
    total_steps = args.max_steps or updates_per_epoch * args.epochs
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.learning_rate, betas=(0.9, 0.95), weight_decay=0.01)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=max(total_steps, 1), eta_min=2e-5)
    global_step = 0
    consumed_micro_steps = 0
    if args.resume:
        state = torch.load(args.resume / "trainer_state.pt", map_location="cpu", weights_only=False)
        optimizer.load_state_dict(state["optimizer"])
        scheduler.load_state_dict(state["scheduler"])
        global_step = int(state["global_step"])
        consumed_micro_steps = global_step * args.gradient_accumulation

    args.output.mkdir(parents=True, exist_ok=True)
    metadata = {
        "base_model": str(args.model),
        "quantization": "bitsandbytes int8",
        "samples": len(dataset),
        "epochs": args.epochs,
        "gradient_accumulation": args.gradient_accumulation,
        "total_steps": total_steps,
        "seed": args.seed,
    }
    (args.output / "training_config.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    model.train()
    optimizer.zero_grad(set_to_none=True)
    micro_step = 0
    running_loss = 0.0
    stop = False
    for epoch in range(args.epochs):
        for batch_index, batch in enumerate(loader):
            if epoch == 0 and batch_index < consumed_micro_steps:
                continue
            batch = {key: value.cuda(non_blocking=True) for key, value in batch.items()}
            accumulation_size = min(args.gradient_accumulation, len(loader) - batch_index)
            with torch.autocast(device_type="cuda", dtype=torch.bfloat16):
                loss = model(**batch, use_cache=False).loss / accumulation_size
            loss.backward()
            running_loss += loss.item() * accumulation_size
            micro_step += 1
            if micro_step % args.gradient_accumulation and batch_index + 1 < len(loader):
                continue

            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            scheduler.step()
            optimizer.zero_grad(set_to_none=True)
            global_step += 1
            average_loss = running_loss / accumulation_size
            running_loss = 0.0
            print(
                f"step={global_step}/{total_steps} epoch={epoch + 1} "
                f"loss={average_loss:.6f} lr={scheduler.get_last_lr()[0]:.8f} "
                f"vram={torch.cuda.max_memory_allocated() / 1024**3:.2f}GiB",
                flush=True,
            )
            if global_step % args.save_steps == 0:
                checkpoint = args.output / f"checkpoint-{global_step}"
                model.save_pretrained(checkpoint, safe_serialization=True)
                torch.save(
                    {"global_step": global_step, "optimizer": optimizer.state_dict(), "scheduler": scheduler.state_dict()},
                    checkpoint / "trainer_state.pt",
                )
            if global_step >= total_steps:
                stop = True
                break
        if stop:
            break

    final_output = args.output / "final"
    model.save_pretrained(final_output, safe_serialization=True)
    AutoTokenizer.from_pretrained(args.model, local_files_only=True).save_pretrained(final_output)
    print(f"adapter saved to {final_output}")


if __name__ == "__main__":
    main()
