#!/usr/bin/env python3
"""Validate the published skill package layout and required front matter."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "skills"
REQUIRED = {
    "author-jiang-nan-longzu": (
        "SKILL.md", "meta.json", "author_persona.md", "writing.md",
        "writer_profile.md", "distillation_report.md", "research_archive.md",
        "self_test.md", "holdout_audit.md", "rolling_worklog.md",
    ),
    "novel-author-persona-distiller": ("SKILL.md", "meta.json"),
}


def main() -> int:
    errors: list[str] = []
    for skill, files in REQUIRED.items():
        directory = ROOT / skill
        for filename in files:
            path = directory / filename
            if not path.is_file():
                errors.append(f"missing: {skill}/{filename}")
        metadata = directory / "meta.json"
        if metadata.is_file():
            try:
                data = json.loads(metadata.read_text(encoding="utf-8"))
                if data.get("slug") != skill:
                    errors.append(f"wrong slug: {skill}/meta.json")
            except json.JSONDecodeError as error:
                errors.append(f"invalid JSON: {metadata}: {error}")
        skill_file = directory / "SKILL.md"
        if skill_file.is_file():
            front_matter = skill_file.read_text(encoding="utf-8").split("---", 2)
            if len(front_matter) < 3:
                errors.append(f"missing front matter: {skill}/SKILL.md")
            elif f"name: {skill}" not in front_matter[1]:
                errors.append(f"wrong skill name: {skill}/SKILL.md")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"validated {len(REQUIRED)} skill packages in {ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
