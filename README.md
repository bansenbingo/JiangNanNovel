# JiangNanNovel

这是一个面向原创化龙族同人创作的 OpenCode 项目级技能。它使用 `原著素材/龙族/分卷` 中的龙族 1-4 分卷、`参考资料` 中的研究论文，以及桌面 `JiangNan` 文件夹中的龙族专项人格存档作为内部研究材料，提炼世界观约束、叙事结构、人物动力和场景方法，不复制原著句子、段落或连续情节。

## 使用

将项目作为工作目录启动 OpenCode，然后直接提出创作任务，例如：

```text
基于龙族世界观写一个原创支线：地点是冬季海港，主角是第一次接触混血种社会的普通大学生。先给出卷纲，再写第一章，不复用原著事件和台词。
```

可发布技能包位于 `skills/`：`author-jiang-nan-longzu` 是龙族原创化写作包，包含 1—4 分卷蒸馏和 V 卷滚动留出审计；`novel-author-persona-distiller` 是通用蒸馏审计器。项目级聚合副本位于 `.claude/skills/`，可直接调用的作家配置位于龙族技能目录的 `writer_profile.md`，蒸馏审计位于 `distillation_report.md` 和 `holdout_audit.md`。安装脚本会把两个技能复制到用户级目录，适用于需要在其他项目中调用的场景：

```bash
python3 tools/install_jiangnan_skills.py --user
```

OpenCode 用户级安装：

```bash
python3 tools/install_jiangnan_skills.py --opencode
```

## 研究边界

- 原著用于提炼可迁移的叙事机制和设定逻辑，不用于逐字仿写。
- 论文用于理解类型特征、东方化处理和研究视角，不把论文结论当作原著事实。
- 生成内容应使用原创事件、原创配角、原创冲突和原创意象；使用既有角色时只保留必要的世界观锚点。
- 用户要求“完全像原文”时，技能会转译为青春幻想、都市神话、黑色幽默、悬疑推进和关系驱动等高层特征。

## 检查

```bash
python3 tools/install_jiangnan_skills.py --check
```

生成不包含正文的素材元数据索引：

```bash
python3 tools/build_material_index.py
```

索引只记录文件路径、类别、大小和 SHA-256，用于确认素材版本和定位来源；它不会把小说或论文正文复制进提示词、技能文件或索引。

验证发布技能包：

```bash
python3 tools/validate_skill_packages.py
```
