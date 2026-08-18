# JiangNanNovel Workspace Skills

本目录是仓库中的完整可安装 Skill 包。大纲规划模块可服务原创或既有 IP 的续写/改写；江南作者与《龙族》人物模块定位为非官方、非商用、AIGC 衍生创作与文本研究，不代表江南本人、江南工作室或《龙族》官方。

## Contents

- `novel-continuation-outline/`：续写、改写、分支和未完稿修复的大纲规划模块，输出可交接的 `outline_state`，不在用户只要大纲时擅自写正文。
- `novel-source-compressor/`：把长篇原文、章节文件或草稿压缩为带来源锚点的 `source_outline_state`；可单独生成完整大纲，也可供上一个模块接续。
- `JiangNanNovel/`：江南创作方法与作者人格入口，并已接入人物强制路由。
- `characters/`：19 个《龙族》人物的 budget-unfriendly 人格 Skill。每个人物目录包含 `SKILL.md`、`work.md`、`persona.md`、独立能力/人格入口、元数据和完整六轨研究链。
- `characters/_research/`：总名单、Phase 1.5 采集检查点、Phase 2.5 三重门结果、语料清单和可复现生成器。
- `VALIDATION.md`：工作区结构、来源适配、严格检查结果和安装隔离证明。

## Runtime Order

1. 需要从长篇原文提取续写依据时，先加载 `novel-source-compressor/SKILL.md`，生成 `source_outline_state`。
2. 需要先定路线时，再加载 `novel-continuation-outline/SKILL.md`，把压缩状态映射为 `outline_state`。
3. 创作或改写再加载 `JiangNanNovel/SKILL.md`。
4. 场景出现 19 人中的任何一人，再按其中的 alias index 加载对应 `characters/<slug>/SKILL.md`。
5. 多人物场景分别计算信息、目标、底线和代价，再由场景事实仲裁，不生成团队统一声线。
6. 未收录人物回查 `../原著素材/龙族/分卷/`，不得拿性格相近的已收录人物代替。

## Source Policy

人物蒸馏以用户提供的本地分卷正文为最高权重一手证据。现实公众人物流程要求的 8 个外部 URL 在此替换为每人 12 个可验证本地场景锚点；仓库不为通过自动检查而伪造 URL。
