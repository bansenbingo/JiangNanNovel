# 江南原创小说创作 Skill

## 安装

### 命令行安装与更新（推荐）

安装器会扫描 `PATH` 中的 agent CLI，让你选择把 Skill 安装到哪个 agent。当前支持 Codex、Claude Code、Gemini CLI、OpenCode、Cursor Agent 和 GitHub Copilot CLI。

macOS：

```bash
curl -fsSL https://github.com/bansenbingo/JiangNanNovel/releases/latest/download/install.sh | bash
```

Windows PowerShell：

```powershell
irm https://github.com/bansenbingo/JiangNanNovel/releases/latest/download/install.ps1 | iex
```

再次运行同一脚本会比较 GitHub 上的最新 Skill：内容没有变化时报告已是最新版本，有变化时自动更新。也可以下载脚本后指定 agent，跳过交互选择：

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
   使用 $skill-installer 从 https://github.com/bansenbingo/JiangNanNovel/tree/main/skills/celebrity/JiangNanNovel 安装 JiangNanNovel。
   ```

3. 安装完成后，在 Codex 中运行 `/skills`，或输入 `$JiangNanNovel`，确认 Skill 已出现。
4. 如果没有立即出现，重启 Codex 后再次检查。

开始使用时，可以直接输入：

```text
使用 $JiangNanNovel，帮我设计一部长篇原创小说。
```

Skill 在 `SKILL.md` 中声明的名称是 `JiangNanNovel`。安装目标只是仓库中的 `skills/celebrity/JiangNanNovel/` 目录，`原著素材/` 不会被复制到 Skill 安装目录；安装器如何临时获取 GitHub 仓库内容由其实现决定。

### 手动安装（备用）

需要预先安装 [Git 2.25 或更高版本](https://git-scm.com/downloads)。以下命令用于首次安装，请在不含 `JiangNanNovel-repo` 子目录的位置执行。命令使用部分克隆和稀疏检出，只检出 Skill，并避免获取未检出的原著文件内容。

macOS 或 Linux：

```bash
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/bansenbingo/JiangNanNovel.git JiangNanNovel-repo
git -C JiangNanNovel-repo sparse-checkout set skills/celebrity/JiangNanNovel
mkdir -p "$HOME/.agents/skills"
cp -R JiangNanNovel-repo/skills/celebrity/JiangNanNovel "$HOME/.agents/skills/JiangNanNovel"
test -f "$HOME/.agents/skills/JiangNanNovel/SKILL.md" && echo "JiangNanNovel 安装成功"
```

Windows PowerShell：

```powershell
git clone --depth 1 --filter=blob:none --sparse `
  https://github.com/bansenbingo/JiangNanNovel.git JiangNanNovel-repo
git -C JiangNanNovel-repo sparse-checkout set skills/celebrity/JiangNanNovel
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse JiangNanNovel-repo\skills\celebrity\JiangNanNovel `
  "$HOME\.agents\skills\JiangNanNovel"
Test-Path "$HOME\.agents\skills\JiangNanNovel\SKILL.md"
```

手动安装后，在 Codex 中运行 `/skills` 或输入 `$JiangNanNovel` 进行验证；若未显示，请重启 Codex。Codex 会从 `$HOME/.agents/skills/JiangNanNovel/SKILL.md` 发现该 Skill。

安装位置与发现规则参见 [OpenAI 官方 Codex Skills 文档](https://developers.openai.com/codex/skills/)。

## 训练与蒸馏方式

本 Skill 使用 `dot-skill` 完成的证据驱动人格与创作方法蒸馏：

- Character family：`celebrity`
- Research profile：`budget-unfriendly`
- Collection strategy：`local-first`
- Research cutoff：`2026-08-15`

语料预处理流程：

1. 读取 UTF-8、UTF-16、GB18030、Big5 等编码的 TXT。
2. 以《龙族》《九州缥缈录》《天之炽》既有文本为参考基线，执行文件级、段落级和近似重复检测。
3. 保留访谈、文论、序跋中独有的作者论述，只删除其中复制的小说正文。
4. 将清洗语料按约 10,000 个非空白字符分卷，不跨作品分类强行拼接。

处理结果：493 个输入 TXT，保留 447 个独有文本，生成 702 个分卷，共 7,044,907 个去重后非空白字符；分卷中位数 10,044，最大 11,564。

蒸馏研究分为六个独立轨道：著作与系统思考、即兴对话与压力应对、语言指纹、行为与选择、他者视角与批评、认知时间线。每条证据标注 1-7 级信源权重，并经过以下关卡：

- Phase 1.5：六轨覆盖、来源与矛盾门槛确认。
- Research audit：`PASS`；保守口径下一手来源 48/59（81%），权重 1-3 来源占 83%。
- Phase 2.5：确认六个核心心智模型；“跨类型翻译”降为启发式，“从雄心到守诺”作为时间校准器。
- Validation：3 个 known-answer 检查、1 个 edge-case 检查、约 100 字声纹盲测、版权检查和 Agentic Protocol 检查全部通过。
- 最终 `budget-unfriendly` 质量检查：13/13 `PASS`。

Skill 提炼的是现实缺口、制度化奇观、关系代价、结构与人物的相互修正、修订方法，以及作者/读者/商业之间的决策张力。它不复制原著段落、角色、专有设定或标志性句式，也不代表江南本人。

## 蒸馏素材来源

### 本地文件

主要原著与参考基线：

- `原著素材/江南/`：江南文字作品 TXT 全集，清洗前输入目录。
- `原著素材/龙族/《龙族》（实体版1-4部全本）.txt`
- `原著素材/龙族/龙族Ⅴ·悼亡者归来.txt`
- `原著素材/九州缥缈录/九州缥缈录.txt`
- `原著素材/天之炽/天之炽（三册全）.txt`
- `原著素材/江南_清洗分卷/`：清洗文本、约万字分卷、manifest 和去重报告。

重点作品样本：

- `原著素材/江南_清洗分卷/cleaned/上海堡垒.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[04]其它长篇小说/《此间的少年》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[04]其它长篇小说/《蝴蝶风暴Ⅰ：猎犬狐》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[01]九州长篇小说/《九州飘零书·商博良》.txt`

重点访谈、文论与序跋：

- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[12]访谈录/《文学、创业和自我定位》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[12]访谈录/《我的写作天赋并不比别人高——〈宁波晚报〉访谈》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[12]访谈录/《中国作家富豪榜采访提纲》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[08]文论/《一个优秀作者所不应具备的七种特征》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[08]文论/《〈龙族Ⅲ〉创作手记》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[10]序跋/《写一场修行——人民文学版〈九州缥缈录〉自序》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[10]序跋/《〈上海堡垒〉——2016再版后记》.txt`
- `原著素材/江南_清洗分卷/cleaned/江南作品合集/[06]散文随笔/《温故2015》.txt`

外部批评文件（蒸馏时读取，精简仓库后不随 Skill 安装）：

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

研究笔记、来源权重、审计、综合与验证记录保存在 `skills/celebrity/JiangNanNovel/knowledge/research/`。
