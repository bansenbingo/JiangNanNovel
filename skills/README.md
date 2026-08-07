# 可发布技能包

本目录包含可独立复制到 Claude Code、OpenCode 或其他支持 `SKILL.md` 的 Agent 技能目录中的技能包。

## 技能包

### `author-jiang-nan-longzu`

面向原创化龙族同人和青春幻想创作。包含世界观约束、人物工程、双线结构、场景镜头链、伏笔审计、写作流程、作家配置、自测用例，以及龙族 1—4 蒸馏报告和龙族 V 滚动留出验证报告/工作日志。

### `novel-author-persona-distiller`

通用小说人格蒸馏与审计流程。包含证据分层、十二维蒸馏矩阵、跨卷留出验证、原创化边界、人格包模板和质量门。

## 安装

将任一技能目录复制到目标 Agent 的技能目录。例如 OpenCode 项目级目录：

```bash
cp -R skills/author-jiang-nan-longzu .claude/skills/
cp -R skills/novel-author-persona-distiller .claude/skills/
```

项目根目录的 `tools/install_jiangnan_skills.py` 会安装两个技能到用户级 OpenCode 或 Claude Code 目录：

```bash
python3 tools/install_jiangnan_skills.py --opencode
python3 tools/install_jiangnan_skills.py --user
```

## 研究与版权边界

技能只发布由研究材料提炼出的高层、可解释、可审计机制，不发布原著或论文正文，不复制原文、连续情节、独特台词、可识别口吻，也不把现实作者作为可扮演身份。原著和论文仅作为本地研究材料，不属于技能包。
