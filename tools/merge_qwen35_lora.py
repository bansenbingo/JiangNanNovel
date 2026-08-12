"""Merge the trained Qwen3.5 LoRA adapter into the local BF16 model."""

from __future__ import annotations

import argparse
from pathlib import Path

import torch
from peft import PeftModel
from transformers import AutoModelForImageTextToText, AutoTokenizer


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=Path, default=Path("model"))
    parser.add_argument("--adapter", type=Path, default=Path("training/qwen35-9b-8bit-lora/final"))
    parser.add_argument("--output", type=Path, default=Path("training/qwen35-9b-merged-bf16"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    model = AutoModelForImageTextToText.from_pretrained(
        args.model,
        local_files_only=True,
        dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
    )
    model = PeftModel.from_pretrained(model, args.adapter, local_files_only=True)
    merged = model.merge_and_unload(safe_merge=True)
    merged.save_pretrained(args.output, safe_serialization=True, max_shard_size="5GB")
    AutoTokenizer.from_pretrained(args.model, local_files_only=True).save_pretrained(args.output)
    print(f"merged model saved to {args.output}")


if __name__ == "__main__":
    main()
