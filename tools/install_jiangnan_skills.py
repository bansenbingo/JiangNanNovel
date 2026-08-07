#!/usr/bin/env python3
"""Install or validate the local JiangNanNovel skills."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SKILLS_DIR = Path(".claude/skills")
INSTALLABLE = (
    "author-jiang-nan-longzu",
    "novel-author-persona-distiller",
)
REQUIRED = {
    "author-jiang-nan-longzu": (
        "SKILL.md",
        "meta.json",
        "author_persona.md",
        "writing.md",
        "writer_profile.md",
        "distillation_report.md",
        "research_archive.md",
        "self_test.md",
    ),
    "novel-author-persona-distiller": ("SKILL.md",),
}


def check(root: Path) -> int:
    missing = [
        f"{skill}/{name}"
        for skill, files in REQUIRED.items()
        for name in files
        if not (root / SKILLS_DIR / skill / name).is_file()
    ]
    if missing:
        print("missing: " + ", ".join(missing))
        return 1
    print(f"skills are valid: {root / SKILLS_DIR}")
    return 0


def install(root: Path, destination: Path) -> int:
    if check(root):
        return 1
    destination.mkdir(parents=True, exist_ok=True)
    for skill in INSTALLABLE:
        source = root / SKILLS_DIR / skill
        target = destination / skill
        if target.is_symlink():
            target.unlink()
        elif target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target)
        print(f"installed: {target}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--user", action="store_true", help="install into ~/.claude/skills")
    parser.add_argument("--opencode", action="store_true", help="install into ~/.config/opencode/skills")
    args = parser.parse_args()

    root = args.root.resolve()
    if args.check or not (args.user or args.opencode):
        raise SystemExit(check(root))
    destination = Path.home() / (".config/opencode/skills" if args.opencode else ".claude/skills")
    raise SystemExit(install(root, destination))


if __name__ == "__main__":
    main()
