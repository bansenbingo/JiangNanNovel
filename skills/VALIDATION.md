# Workspace Validation Report

Validation date: 2026-08-18

## Build Result

- Character persona units: 19
- Character Skills generated through `dot-skill/tools/skill_writer.py`: 19
- Research profile: `budget-unfriendly`
- Raw research notes: 114（19 x 6）
- Local primary scene anchors: 228（19 x 12）
- Research audits with `Status: PASS`: 19/19
- Synthesis reviews present: 19/19
- Validation reviews with `Status: PASS`: 19/19
- Workspace files: 370
- Workspace size: approximately 3.2 MB

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

- The installable bundle now lives under top-level `skills/`; the `v1.2.0` `skill/` layout was renamed without changing internal author-to-character relative routes. The earlier source merge preserved eight newer research files, the unique holdout and the Phase 2.5 correction validations.
- All 19 expected combined `SKILL.md` files exist.
- All 228 recorded `Local source` paths resolve to existing files under `原著素材/龙族/分卷/`.
- All 19 character paths referenced by `JiangNanNovel/SKILL.md` resolve inside this workspace.
- `JiangNanNovel/knowledge/character-routing.md` records all 19 links to `SKILL.md`, `persona.md` and `work.md`, together with core extraction, state selection and hard boundaries.
- The archived generator compiles successfully.
- The installed `/Users/teddyjiang/.codex/skills/JiangNanNovel` aggregate SHA-256 remained `091381c60f7eb02b558ba7827468bba69d33f91cccc242f46a66e2f8aa5d09f2` before and after generation.
- Every writer invocation used `--no-install-claude-skill`; no Codex, Claude, or OpenClaw installation flag was used.

## Outline Planning Module Addendum

Validation date: 2026-08-18

- `novel-continuation-outline/SKILL.md` is the planning entry for idea-to-outline, continuation, branch rewrite, deep rewrite and unfinished-draft repair tasks.
- The module keeps its required `SKILL.md` under 500 lines and moves the output schema, question bank and continuity ledger into on-demand references.
- Its interaction protocol asks for the user's own image, relationship, emotional residue, cost or hard boundary before offering optional A/B/C scaffolding; free-form answers remain traceable in `vision_capture` instead of being reduced to a choice label.
- `evals/evals.json` covers nonofficial fan-fiction planning, an unfinished original draft, a structural rewrite under a fixed word-count budget and an upstream routing case with open-ended vision capture.
- The package entry routes planning tasks through the module before author and character execution Skills.
- Both installers verify the planning module before replacing an installed bundle.

## Source Compression Module Addendum

Validation date: 2026-08-18

- `novel-source-compressor/SKILL.md` compresses original text into a traceable outline while preserving causal, character, knowledge, continuity and promise state.
- The module supports `handoff-compress`, `standalone-outline`, `incremental-merge` and `archive-dossier` modes.
- `source_outline_state` maps directly into `novel-continuation-outline` through the documented field mapping; the canonical routing envelope is `version`, `source_scope`, `source_status`, `mode`, `compression_depth`, `confidence`, `traceability` and `compression_risks`.
- Readers accept legacy `state_version` and `compression_mode` aliases, while all newly generated states normalize them to `version` and `mode`; inference and compression risks remain visible and are never promoted to locked facts.
- Continuation begins after `ending_or_last_stable_point` and does not re-summarize chapters already covered by the compressor unless a traceability or compression risk requires a targeted source reread.
- Evals cover handoff compression, standalone detailed outline and incremental merging of a new chapter.
- Both installers verify the source compressor before replacing an installed bundle.

## Release Boundaries

- Nonofficial, noncommercial, AIGC labeling is mandatory.
- The generated Skills are research and writing controls, not claims about canonical hidden motives.
- Volume V identity and end-state conclusions remain provisional.
- The author Skill handles narrative construction; character Skills handle character-specific perception, knowledge, voice, choice and relationship behavior.
