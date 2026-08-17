# 江南原创小说创作 Skill

JiangNanNovel 是一个基于江南公开作品、访谈、文论、外部批评与《龙族》本地分卷语料蒸馏的小说创作 Skill 包。`v1.2.0` 同时包含作者级创作方法和 19 个主要人物的人格/场景 Skill；创作时先加载作者层，再按人物别名自动路由到对应人物层。

> **使用声明**
>
> 本项目是非官方、非商用、AIGC 同人创作与文本研究工具，不代表江南本人、江南工作室或《龙族》官方。依项目维护者说明，本项目所涉及的非商用声纹复刻用途已与江南工作室书面联系并获得许可；该说明不构成官方出品、推荐或背书。使用者仍应标注 AIGC，不得冒充作者本人，不得用于商业出版、署名混淆或规避版权责任。

## 安装

### 命令行安装与更新（推荐）

安装器会扫描 `PATH` 中的 agent CLI，让你选择把完整 Skill 包安装到哪个 agent。当前支持 Codex、Claude Code、Gemini CLI、OpenCode、Cursor Agent 和 GitHub Copilot CLI。

macOS 或 Linux：

```bash
curl -fsSL https://github.com/bansenbingo/JiangNanNovel/releases/latest/download/install.sh | bash
```

Windows PowerShell：

```powershell
irm https://github.com/bansenbingo/JiangNanNovel/releases/latest/download/install.ps1 | iex
```

再次运行同一脚本会比较 GitHub 上的最新 Skill 包：内容没有变化时报告已是最新版本，有变化时自动更新。也可以下载脚本后指定 agent，跳过交互选择：

```bash
bash install.sh --agent codex
```

```powershell
.\install.ps1 -Agent codex
```

使用 `--list`（PowerShell 为 `-List`）可以查看扫描结果和安装目录。

### 使用 Codex 内置安装器

1. 打开 Codex，新建一个任务。
2. 把下面这句话发送给 Codex：

   ```text
   使用 $skill-installer 从 https://github.com/bansenbingo/JiangNanNovel/tree/main/skill 安装 JiangNanNovel。
   ```

3. 安装完成后，在 Codex 中运行 `/skills`，或输入 `$JiangNanNovel`，确认 Skill 已出现。
4. 如果没有立即出现，重启 Codex 后再次检查。

开始使用时，可以直接输入：

```text
使用 $JiangNanNovel，帮我设计一部长篇原创小说。
```

从 `v1.2.0` 起，安装目标是仓库中的完整 `skill/` 包，而不是旧版的 `skills/celebrity/JiangNanNovel/` 单目录。完整包包含作者层、人物层及二者之间的相对路由；只复制 `skill/JiangNanNovel/` 会导致人物依赖缺失。`原著素材/` 不会被复制到 agent 的 Skill 安装目录。

### 手动安装（备用）

需要预先安装 [Git 2.25 或更高版本](https://git-scm.com/downloads)。以下命令用于首次安装，请在不含 `JiangNanNovel-repo` 子目录的位置执行。命令使用部分克隆和稀疏检出，只检出可安装的 `skill/` 包。

macOS 或 Linux：

```bash
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/bansenbingo/JiangNanNovel.git JiangNanNovel-repo
git -C JiangNanNovel-repo sparse-checkout set skill
mkdir -p "$HOME/.agents/skills"
cp -R JiangNanNovel-repo/skill "$HOME/.agents/skills/JiangNanNovel"
test -f "$HOME/.agents/skills/JiangNanNovel/SKILL.md" && echo "JiangNanNovel 安装成功"
```

Windows PowerShell：

```powershell
git clone --depth 1 --filter=blob:none --sparse `
  https://github.com/bansenbingo/JiangNanNovel.git JiangNanNovel-repo
git -C JiangNanNovel-repo sparse-checkout set skill
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse JiangNanNovel-repo\skill `
  "$HOME\.agents\skills\JiangNanNovel"
Test-Path "$HOME\.agents\skills\JiangNanNovel\SKILL.md"
```

手动安装后，在 Codex 中运行 `/skills` 或输入 `$JiangNanNovel` 进行验证；若未显示，请重启 Codex。安装位置与发现规则参见 [OpenAI 官方 Codex Skills 文档](https://developers.openai.com/codex/skills/)。

## Skill 包结构

```text
skill/
├── SKILL.md                  # 可安装入口
├── JiangNanNovel/            # 作者人格与小说创作方法
│   ├── SKILL.md
│   └── knowledge/
│       ├── character-routing.md
│       └── research/
├── characters/              # 19 个主要人物 Skill
│   ├── lu_mingfei/
│   ├── chu_zihang/
│   ├── caesar_gattuso/
│   └── ...
└── VALIDATION.md            # 工作区验证报告
```

运行顺序：

1. 包级入口读取 `JiangNanNovel/SKILL.md`，加载作者级结构、镜头、节奏、以乐写哀和“公共胜利 / 私人空缺”方法。
2. 场景出现收录人物时，根据 `JiangNanNovel/knowledge/character-routing.md` 读取对应 `characters/<slug>/SKILL.md`。
3. 多人物场景分别计算每个人的信息、目标、底线、关系状态与代价，再由场景事实仲裁，不生成统一声线。
4. 未收录人物回查一手正文，不使用性格相近人物代替。

当前人物层覆盖：路明非、楚子航、恺撒、诺诺、小魔鬼路鸣泽、芬格尔、零、昂热、夏弥、上杉绘梨衣、源稚生、源稚女、楚天骄、乔薇尼、奥丁、橘政宗/王将/赫尔佐格、酒德麻衣、苏恩曦和苏茜。

## 训练与蒸馏方式

本 Skill 使用 `dot-skill` 完成证据驱动的人格与创作方法蒸馏：

- Character family：`celebrity`（人物层复用同一研究管线，但元数据明确标记为虚构人物）
- Research profile：`budget-unfriendly`
- Collection strategy：`local-first`
- Research cutoff：`2026-08-17`

### 作者层

语料预处理流程：

1. 读取 UTF-8、UTF-16、GB18030、Big5 等编码的 TXT。
2. 以《龙族》《九州缥缈录》《天之炽》既有文本为参考基线，执行文件级、段落级和近似重复检测。
3. 保留访谈、文论、序跋中独有的作者论述，只删除其中复制的小说正文。
4. 将清洗语料按约 10,000 个非空白字符分卷，不跨作品分类强行拼接。

处理结果：493 个输入 TXT，保留 447 个独有文本，生成 702 个分卷，共 7,044,907 个去重后非空白字符；分卷中位数 10,044，最大 11,564。

作者研究分为六个独立轨道：著作与系统思考、即兴对话与压力应对、语言指纹、行为与选择、他者视角与批评、认知时间线。每条证据标注 1-7 级信源权重，并通过 Phase 1.5、Research audit、Phase 2.5、holdout、known-answer、edge-case、版权和 Agentic Protocol 检查。最终 `budget-unfriendly` 质量检查为 13/13 `PASS`。

作者层提炼现实缺口、制度化奇观、关系代价、结构与人物的相互修正、修订方法，以及作者/读者/商业之间的决策张力。它把“先建立值得失去的美好，再让胜利无法恢复原状”作为悲剧结构控制，不把现实中的商业人格直接等同于作品中未长大的少年叙述者。

### 人物层

19 个人物均使用六轨独立研究链，每人包含组合 `SKILL.md`、人格提取、场景协议、元数据、审计、综合与验证记录：

- 19/19 research audit：`PASS`
- 19/19 synthesis review：已生成
- 19/19 validation review：`PASS`
- 114 份原始人物研究文件（19 × 6）
- 228 个一手正文场景锚点（19 × 12）
- 57 条作者到人物的组合 Skill、人格与场景协议路由

通用质量检查中的 `source_grounding` 和 `research_depth` 只统计 HTTP(S) URL，因此人物层没有用伪造网页链接换取形式通过。虚构人物以本地一手正文替代现实公众人物的外部 URL：每人 12 个可定位场景锚点、6 条矛盾记录、6 条推断记录，来源权重均为一级文本。

完整验证口径见 [`skill/VALIDATION.md`](skill/VALIDATION.md)。

## 蒸馏素材来源

### 本地文件

主要原著与参考基线：

- `原著素材/江南/`：江南文字作品 TXT 全集，清洗前输入目录。
- `原著素材/龙族/《龙族》（实体版1-4部全本）.txt`
- `原著素材/龙族/龙族Ⅴ·悼亡者归来.txt`
- `原著素材/龙族/分卷/`：人物蒸馏使用的可定位正文分卷。
- `原著素材/九州缥缈录/九州缥缈录.txt`
- `原著素材/天之炽/天之炽（三册全）.txt`
- `原著素材/江南_清洗分卷/`：清洗文本、约万字分卷、manifest 和去重报告。

重点访谈、文论与序跋：

- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[12]访谈录/《文学、创业和自我定位》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[12]访谈录/《我的写作天赋并不比别人高——〈宁波晚报〉访谈》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[12]访谈录/《中国作家富豪榜采访提纲》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[08]文论/《一个优秀作者所不应具备的七种特征》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[08]文论/《〈龙族Ⅲ〉创作手记》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[10]序跋/《写一场修行——人民文学版〈九州缥缈录〉自序》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[10]序跋/《〈上海堡垒〉——2016再版后记》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[06]散文随笔/《温故2015》.txt`

外部批评文件：

- `参考资料/奇幻小说的东方化——以江南的《龙族》为例-张猛.pdf`
- `参考资料/玄幻小说的特征及发展现状初探——以江南的《龙族》为例-陈妍锦.pdf`

### 已核验网页

书目与版本锚点：

- https://book.douban.com/subject/1321017/
- https://book.douban.com/subject/4737329/
- https://book.douban.com/subject/6434543/
- https://book.douban.com/subject/25825717/
- https://book.douban.com/subject/25997575/
- https://book.douban.com/subject/26647621/

长访谈与外部批评：

- https://www.chinawriter.com.cn/n1/2018/0523/c405057-30006739.html
- https://www.chinawriter.com.cn/n1/2020/1025/c405057-31905087.html
- https://www.chinawriter.com.cn/n1/2020/1108/c405057-31923053.html
- https://www.chinawriter.com.cn/n1/2025/1030/c404027-40592897.html

作者研究笔记、来源权重、审计、综合与验证记录保存在 `skill/JiangNanNovel/knowledge/research/`；人物名单、语料矩阵和阶段检查点保存在 `skill/characters/_research/`。
