# Workspace Validation Report

Validation date: 2026-08-17

## Build Result

- Character persona units: 19
- Character Skills generated through `dot-skill/tools/skill_writer.py`: 19
- Research profile: `budget-unfriendly`
- Raw research notes: 114（19 x 6）
- Local primary scene anchors: 228（19 x 12）
- Research audits with `Status: PASS`: 19/19
- Synthesis reviews present: 19/19
- Validation reviews with `Status: PASS`: 19/19
- Workspace files: 356
- Workspace size: approximately 3.0 MB

## Metadata Result

All 19 generated `meta.json` files agree on:

- `character=celebrity`，用于复用 dot-skill 的 budget-unfriendly 管线
- `research_profile=budget-unfriendly`
- `classification.language=zh-CN`
- `source_context.is_real_person=false`
- `source_context.is_public_figure=false`
- `source_context.is_fictional=true`

## Strict Quality Check

The stock budget-unfriendly checker passed these checks for all 19 Skills:

- mental models
- limitations and honest boundaries
- Expression DNA
- internal tensions
- intellectual genealogy
- Agentic Protocol
- copyright safety
- source hierarchy
- audit / synthesis / validation review chain
- known-answer and edge-case validation depth

The stock checker reports the same two expected failures for all 19 Skills:

- `source_grounding`: the checker only counts HTTP(S) URLs
- `research_depth`: its aggregate rule includes `Unique URLs >= 8`

This is an intentional fictional-character local-source adaptation. Each character has 12 inspected primary-text scene anchors, 6 independent tracks, 12 source metadata blocks, 6 contradiction records, 6 inference records, 100% weight 1 primary material and 0 potential long-quote lines. `Unique URLs` remains 0; no URL was fabricated to satisfy a reality-person benchmark.

## Structural and Source Checks

- The former top-level `skills/` tree was merged into `skill/`; eight newer research files replaced their older counterparts, and the unique holdout plus Phase 2.5 correction validations were preserved.
- All 19 expected combined `SKILL.md` files exist.
- All 228 recorded `Local source` paths resolve to existing files under `原著素材/龙族/分卷/`.
- All 19 character paths referenced by `JiangNanNovel/SKILL.md` resolve inside this workspace.
- `JiangNanNovel/knowledge/character-routing.md` records all 19 links to `SKILL.md`, `persona.md` and `work.md`, together with core extraction, state selection and hard boundaries.
- The archived generator compiles successfully.
- The installed `/Users/teddyjiang/.codex/skills/JiangNanNovel` aggregate SHA-256 remained `091381c60f7eb02b558ba7827468bba69d33f91cccc242f46a66e2f8aa5d09f2` before and after generation.
- Every writer invocation used `--no-install-claude-skill`; no Codex, Claude, or OpenClaw installation flag was used.

## Release Boundaries

- Nonofficial, noncommercial, AIGC labeling is mandatory.
- The generated Skills are research and writing controls, not claims about canonical hidden motives.
- Volume V identity and end-state conclusions remain provisional.
- The author Skill handles narrative construction; character Skills handle character-specific perception, knowledge, voice, choice and relationship behavior.
