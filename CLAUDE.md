# CLAUDE.md — Claude Code 项目说明

本项目为江南小说 AI 续写仓库。完整项目规则见 AGENTS.md（opencode/codex/claude code 通用），此处引入以避免重复维护。

@AGENTS.md

## 可用斜杠命令（人格技能）

- `/author-jiang-nan-master` — 江南总人格（自动识别世界观，首选）
- `/author-jiang-nan` — 九州缥缈录人格
- `/author-jiang-nan-longzu` — 龙族人格
- `/author-jiang-nan-tianzhichi` — 天之炽人格

技能定义位于 `.claude/skills/`（与 opencode 共用），源文件见根目录 `00_江南总人格-master/` 等目录。创作前确保已加载对应人格的完整写作规则。
