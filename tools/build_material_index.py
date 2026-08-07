#!/usr/bin/env python3
"""Build a metadata-only index for the local writing research corpus.

The index records paths, sizes, hashes, and rough source categories. It does
not copy or quote copyrighted source text into the generated artifact.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def classify(path: Path) -> str:
    parts = path.parts
    if "参考资料" in parts:
        return "research-paper"
    if "分卷" in parts:
        return "novel-volume"
    if "龙族" in parts:
        return "novel-other"
    return "other"


def build_index(root: Path) -> dict:
    files = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.name.startswith("."):
            continue
        relative = path.relative_to(root).as_posix()
        files.append(
            {
                "path": relative,
                "category": classify(path),
                "suffix": path.suffix.lower(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    return {
        "schema_version": 1,
        "purpose": "metadata-only local research corpus index",
        "copyright_note": "Source text is not copied into this index or generated prompts.",
        "files": files,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("素材索引.json"))
    args = parser.parse_args()

    index = build_index(args.root)
    args.output.write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"indexed {len(index['files'])} files -> {args.output}")


if __name__ == "__main__":
    main()
