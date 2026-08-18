---
name: JiangNanNovel
description: 江南小说创作方法、《龙族》主要人物人格路由与续写/改写大纲规划的完整工作区 Skill 包。用于原创长篇设计、场景改写、人物对白、关系推进、悲剧结构、未完稿重构和文本自检。
---

# JiangNanNovel Bundle Entry

本目录是可安装入口。它把作者级创作方法与 19 个《龙族》人物 Skill 保存在同一个相对路径稳定的包内。

## Required Loading Order

1. 接到需要从长篇原文、章节文件或旧稿中提取续写依据的任务时，先完整读取 `novel-source-compressor/SKILL.md`，生成或读取 `source_outline_state`。
2. 接到需要先规划的续写、改写、分支、未完稿修复或大纲任务时，再完整读取 `novel-continuation-outline/SKILL.md`；它负责交互、版本和 `outline_state` 交接协议。
3. 接到小说创作、场景改写、人物对白或人物分析任务时，再完整读取 `JiangNanNovel/SKILL.md`。
4. 按 `JiangNanNovel/knowledge/character-routing.md` 识别人名、别名、复合身份和版本边界。
5. 任务中出现已收录人物时，在动笔前完整读取对应的 `characters/<slug>/SKILL.md`；出现多个人物就分别读取，不能只加载视角人物。
6. 作者层负责结构、镜头、节奏和悲剧代价；人物层负责角色的知识、欲望、底线、关系状态、说话方式与选择。两层约束同时生效。
7. 执行作者 Skill 规定的证据边界、版权检查、事实连续性检查和交付前自检。

不得绕过人物路由直接用通用标签代替具体人物，也不得把未收录人物强行映射到性格相似者。

## Boundary

`novel-continuation-outline/` 可用于原创小说的构思、续写规划与未完稿修复；其中涉及既有 IP 时仍需区分原作事实、用户改动和推演。`JiangNanNovel/` 及 `characters/` 作者/人物模块仅用于非官方、非商用、明确标注 AIGC 的《龙族》衍生创作与文本研究，不代表江南本人、江南工作室或《龙族》官方。不得冒充作者本人，不得用于商业出版、署名混淆或规避版权责任。
