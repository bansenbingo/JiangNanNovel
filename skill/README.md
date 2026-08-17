# JiangNanNovel Workspace Skills

本目录保存本轮对话生成的未安装工作区副本。所有内容均定位为非官方、非商用、AIGC 同人创作与文本研究材料，不代表江南本人、江南工作室或《龙族》官方。

## Contents

- `JiangNanNovel/`：本轮对话持续修订的江南创作方法与作者人格临时副本。它没有写入 Codex 已安装技能，并已接入人物强制路由。
- `characters/`：19 个《龙族》人物的 budget-unfriendly 人格 Skill。每个人物目录包含 `SKILL.md`、`work.md`、`persona.md`、独立能力/人格入口、元数据和完整六轨研究链。
- `characters/_research/`：总名单、Phase 1.5 采集检查点、Phase 2.5 三重门结果、语料清单和可复现生成器。
- `VALIDATION.md`：工作区结构、来源适配、严格检查结果和安装隔离证明。

## Runtime Order

1. 创作或改写先加载 `JiangNanNovel/SKILL.md`。
2. 场景出现 19 人中的任何一人，再按其中的 alias index 加载对应 `characters/<slug>/SKILL.md`。
3. 多人物场景分别计算信息、目标、底线和代价，再由场景事实仲裁，不生成团队统一声线。
4. 未收录人物回查 `../原著素材/龙族/分卷/`，不得拿性格相近的已收录人物代替。

## Source Policy

人物蒸馏以用户提供的本地分卷正文为最高权重一手证据。现实公众人物流程要求的 8 个外部 URL 在此替换为每人 12 个可验证本地场景锚点；仓库不为通过自动检查而伪造 URL。
