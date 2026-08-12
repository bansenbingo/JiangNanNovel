"""Tokenize the three novel corpora into fixed-length causal-LM blocks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from transformers import AutoTokenizer


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=Path, default=Path("model"))
    parser.add_argument("--source", type=Path, default=Path("原著素材"))
    parser.add_argument("--output", type=Path, default=Path("training/tokenized-qwen35"))
    parser.add_argument("--sequence-length", type=int, default=2048)
    return parser.parse_args()


def read_text(path: Path) -> str:
    for encoding in ("utf-8-sig", "gb18030"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            pass
    raise UnicodeError(f"unable to decode {path}")


def main() -> None:
    args = parse_args()
    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=True)
    eos_id = tokenizer.eos_token_id
    if eos_id is None:
        raise SystemExit("tokenizer does not define eos_token_id")

    book_dirs = sorted(path for path in args.source.iterdir() if (path / "分卷").is_dir())
    if len(book_dirs) != 3:
        raise SystemExit(f"expected exactly three books under {args.source}, found {len(book_dirs)}")

    all_tokens: list[int] = []
    books: list[dict[str, int | str]] = []
    for book_dir in book_dirs:
        files = sorted((book_dir / "分卷").glob("*.txt"))
        start = len(all_tokens)
        characters = 0
        for path in files:
            text = read_text(path).replace("\r\n", "\n").replace("\r", "\n").strip()
            if not text:
                continue
            characters += len(text)
            all_tokens.extend(tokenizer.encode(text, add_special_tokens=False))
            all_tokens.append(eos_id)
        books.append(
            {
                "book": book_dir.name,
                "files": len(files),
                "characters": characters,
                "tokens": len(all_tokens) - start,
            }
        )

    usable_tokens = len(all_tokens) // args.sequence_length * args.sequence_length
    if usable_tokens == 0:
        raise SystemExit("corpus is too small for one training block")
    blocks = np.asarray(all_tokens[:usable_tokens], dtype=np.int32).reshape(-1, args.sequence_length)

    args.output.mkdir(parents=True, exist_ok=True)
    np.save(args.output / "input_ids.npy", blocks)
    manifest = {
        "model": str(args.model),
        "source": str(args.source),
        "sequence_length": args.sequence_length,
        "samples": int(blocks.shape[0]),
        "total_tokens": len(all_tokens),
        "training_tokens": usable_tokens,
        "discarded_tail_tokens": len(all_tokens) - usable_tokens,
        "books": books,
    }
    (args.output / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
