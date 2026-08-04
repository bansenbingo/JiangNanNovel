# JiangNanNovel

江南小说 AI 续写内容仓库：收录江南（起点中文网白金大神，代表作《龙族》《九州缥缈录》《天之炽》）的完整 AI 写作人格，以及基于这些人格创作的 AI 续写作品。

## 仓库结构

```
JiangNanNovel/
├── README.md                       ← 本说明文档
├── AGENTS.md                       ← Agent 通用规则（opencode/codex/claude code 启动即加载）
├── CLAUDE.md                       ← Claude Code 入口
├── opencode.json                   ← opencode 配置
├── .claude/skills/                 ← 4 个人格的技能注册（opencode 与 Claude Code 共用）
├── 00_江南总人格-master/           ← ★总人格（自动识别世界观：龙族/九州/天之炽）
├── 01_江南-九州人格/               ← 九州专项（蒙太奇/空间构建/留白/断言叙事）
├── 02_江南-龙族人格/               ← 龙族专项（路明非白烂/绘梨衣Sakura/情节架构）
├── 03_江南-天之炽人格/             ← 天之炽专项（西泽尔深渊/蒸汽朋克/甲胄战斗）
└── LICENSE
```

> **★ 推荐使用 `00_江南总人格-master`**：它会自动识别你输入内容所属的世界观（龙族/九州/天之炽），并调用对应人格创作。`references/` 内含三个子人格的完整写作规则。

## 世界观识别示例

| 输入提及 | 自动识别 |
|---------|---------|
| 卡塞尔学院、言灵、路明非、绘梨衣 | 龙族 |
| 殇阳关、天驱、姬野、吕归尘 | 九州 |
| 炽天使、机动甲胄、西泽尔、翡冷翠 | 天之炽 |

## 每个人格的组成

| 文件 | 内容 |
|------|------|
| `SKILL.md` | 技能入口，训练要点与禁令 |
| `writing.md` | 写作能力（文风/人物/情节/标题/大纲） |
| `author_persona.md` | 作者人格（5层结构） |
| `meta.json` | 元数据（版本/训练状态/标签） |
| `knowledge/` | 九州人格的素材库（书评/原著/社交信息） |

## 人格版本状态

| 人格 | 版本 | 状态 |
|------|------|------|
| 总人格（master） | v1 | 自动识别世界观（龙族/九州/天之炽） |
| 九州 | v7 | 已收敛（蒙太奇/空间构建/留白/断言叙事） |
| 龙族 | v9 | 已收敛（图灵测试通过，含情节架构模块） |
| 天之炽 | v5 | 已收敛（含标题风格总论与大纲设计） |

## 在 Agent 中使用（已预加载配置）

仓库已配置三个主流 Agent 的预加载机制，克隆后无需额外安装：

| Agent | 预加载机制 | 说明 |
|-------|-----------|------|
| **opencode** | `AGENTS.md` + `.claude/skills/` | 启动即加载项目规则；4 个人格以 skill 形式注册，创作时自动调用 |
| **Claude Code** | `CLAUDE.md` + `.claude/skills/` | 启动即加载项目规则；可用 `/author-jiang-nan-master` 等斜杠命令 |
| **codex** | `AGENTS.md` | 启动即加载项目规则；按规则阅读 `.claude/skills/` 中的人格完整定义 |

- `AGENTS.md`：通用项目规则（必读章节为"创作时必须加载江南人格"）
- `CLAUDE.md`：Claude Code 入口（引入 AGENTS.md）
- `.claude/skills/`：4 个人格的技能注册（`author-jiang-nan-master` / `author-jiang-nan` / `author-jiang-nan-longzu` / `author-jiang-nan-tianzhichi`），为 `00_`~`03_` 源文件的镜像，修改源文件后需同步

在 Claude Code 中调用：
- **★ 江南总人格（自动识别世界观）**：`/author-jiang-nan-master`
- 九州人格：`/author-jiang-nan`
- 龙族人格：`/author-jiang-nan-longzu`
- 天之炽人格：`/author-jiang-nan-tianzhichi`

## 训练方法

如需重新训练或训练其他作者，可参考蒸馏作者 skill（`Skills-for-Long-Online-Novel-Authors-main`）中的"自主深度训练方法论"，包含八步流程：文本解析→文风提炼→人物情节分析→网络书评→写入注册→图灵测试→章节标题→用户反馈迭代。
