# 《龙族》主要人物人格路由记录

本文件是工作区 `JiangNanNovel` 的人物依赖清单。路径均以 `skill/JiangNanNovel/` 为解析根目录。快速别名触发保存在主 `SKILL.md`；本文件记录触发后实际加载哪些人格提取内容。

## Loading Contract

人物在场景中只有背景点名时，可只读取其 `SKILL.md` 的边界。人物拥有对白、动作、心理、关键观察或决定时，必须读取三项：

1. `SKILL.md`：完整入口、免责声明和运行优先级。
2. `persona.md`：Expression DNA、通过三重门的 mental models、heuristics、关系与信息边界。
3. `work.md`：把人格转换成场景行动、对话、关系路由和失败检查的步骤。

每次使用还要锁定卷次、身份、阵营、记忆和压力状态。下列“核心提取”是检索摘要，不可替代对应文件正文。

## 01 路明非

- Trigger aliases: 路明非、明明、路主席。
- Combined route: `../characters/lu_mingfei/SKILL.md`
- Persona extraction: `../characters/lu_mingfei/persona.md`
- Scene protocol: `../characters/lu_mingfei/work.md`
- Core extraction: 被遗弃雷达；笑话减压阀；具体之人优先于公共荣誉。
- State selector: 安全态以自嘲、网络和日常比喻绕行；具体的人失去退路时，语言骤短并转入行动。
- Hard boundary: 不把牺牲写成索爱资格；堂弟路鸣泽和小魔鬼路鸣泽必须消歧；第五卷身份终局为阶段性。

## 02 楚子航

- Trigger aliases: 楚子航、楚师兄、会长。
- Combined route: `../characters/chu_zihang/SKILL.md`
- Persona extraction: `../characters/chu_zihang/persona.md`
- Scene protocol: `../characters/chu_zihang/work.md`
- Core extraction: 程序化关怀；缺席反证存在；“行动替代表白”只作为 heuristic。
- State selector: 成人常态、幼年化、被因果抹除、异化和归来状态分别路由；短答必须由观察、准备或承担支撑。
- Hard boundary: 不用“面瘫”“机器人”代替人格；后卷记忆不能倒灌雨夜前后的不同状态。

## 03 恺撒·加图索

- Trigger aliases: 恺撒、凯撒、恺撒·加图索。
- Combined route: `../characters/caesar_gattuso/SKILL.md`
- Persona extraction: `../characters/caesar_gattuso/persona.md`
- Scene protocol: `../characters/caesar_gattuso/work.md`
- Core extraction: 公开下注伦理；资源必须兑现承诺；“值得的对手也是潜在盟友”只作为 heuristic。
- State selector: 领袖态先公开标准、筹码与代价；关系受挫时仍保持体面，但允许事实推翻资源优势。
- Hard boundary: 不写空洞霸总，不让财富自动解决爱情，不把家族资本等同其全部人格。

## 04 陈墨瞳 / 诺诺

- Trigger aliases: 陈墨瞳、诺诺、红发巫女。
- Combined route: `../characters/nono/SKILL.md`
- Persona extraction: `../characters/nono/persona.md`
- Scene protocol: `../characters/nono/work.md`
- Core extraction: 破坏预定悲剧；痕迹侧写；选择权高于完美方案。
- State selector: 日常以短句、反问和突然行动破局；侧写时切换为证据链；受伤或被控制时反而减少解释。
- Hard boundary: 侧写必须依赖痕迹，不得写成读心；婚姻和第五卷记忆状态必须按时间点锁定。

## 05 小魔鬼·路鸣泽

- Trigger aliases: 小魔鬼、小魔鬼路鸣泽、交易者路鸣泽；仅有“路鸣泽”时先消歧。
- Combined route: `../characters/lu_mingze_devil/SKILL.md`
- Persona extraction: `../characters/lu_mingze_devil/persona.md`
- Scene protocol: `../characters/lu_mingze_devil/work.md`
- Core extraction: 绝境定价；亲密包装条款；操控舞台而保留形式同意。
- State selector: 先以“哥哥”建立亲密，再命名欲望、列出价格并用短句落槌；身份和终局问题保持回避。
- Hard boundary: 永不加载到普通堂弟语境；不得无条件赠予、含混报价或把幕后能力写成无边界全知。

## 06 芬格尔·冯·弗林斯

- Trigger aliases: 芬格尔、芬狗、废柴师兄。
- Combined route: `../characters/fingel/SKILL.md`
- Persona extraction: `../characters/fingel/persona.md`
- Scene protocol: `../characters/fingel/work.md`
- Core extraction: 废柴烟幕；噪声中的关键情报；不宣誓的在场。
- State selector: 安全态用抱怨、歪理和夸张制造噪声；工作态突然压缩为精确位置、权限、时间和风险。
- Hard boundary: 不写纯丑角或持续无能；真人与第五卷手机人格的语言证据分开使用。

## 07 零

- Trigger aliases: 零、零号、雷娜塔；后两项只触发关联审查。
- Combined route: `../characters/zero/SKILL.md`
- Persona extraction: `../characters/zero/persona.md`
- Scene protocol: `../characters/zero/work.md`
- Core extraction: 尊严定价；秘密即边界；“默契先于言语”只作为 heuristic。
- State selector: 默认以短句、正式条件和位置变化表达；触及过去时不被强迫坦白，先保护秘密关联者。
- Hard boundary: 零 / 零号 / 雷娜塔可关联但不自动断言同一；不写娃娃式天真或“等待被解冻”。

## 08 希尔伯特·让·昂热

- Trigger aliases: 昂热、希尔伯特·让·昂热、校长。
- Combined route: `../characters/ange/SKILL.md`
- Persona extraction: `../characters/ange/persona.md`
- Scene protocol: `../characters/ange/work.md`
- Core extraction: 礼仪包裹战争；授权式武器化教育；私人复仇制度化。
- State selector: 越危险越从容，先安顿场面和年轻人，再给出明确猎杀方向；未知情报交给最有能力者验证。
- Hard boundary: 学生关爱与工具化必须并存，不写单面慈父或无计算的冒险校长。

## 09 夏弥 / 耶梦加得

- Trigger aliases: 夏弥、耶梦加得、师妹。
- Combined route: `../characters/xia_mi/SKILL.md`
- Persona extraction: `../characters/xia_mi/persona.md`
- Scene protocol: `../characters/xia_mi/work.md`
- Core extraction: 骗局中的真实日常；照料弱者优先；玩笑式情感测压。
- State selector: 师妹态用校园、吃饭和恋爱想象逼出情感回应；龙王态句子变稳，但真实日常愿望不因此作废。
- Hard boundary: 不把所有轻快判成伪装，不写全程古老龙王腔；身份揭示不得提前泄露给未知情人物。

## 10 上杉绘梨衣

- Trigger aliases: 上杉绘梨衣、绘梨衣、Erii。
- Combined route: `../characters/uesugi_erii/SKILL.md`
- Persona extraction: `../characters/uesugi_erii/persona.md`
- Scene protocol: `../characters/uesugi_erii/work.md`
- Core extraction: 物件式世界学习；有限语言中的明确选择；武器身体与普通愿望错位。
- State selector: 先用游戏、衣服、食物和城市物件理解世界；复杂意图拆成短句、书写、指认和“试探 -> 反应 -> 保护”动作链。
- Hard boundary: 语言有限不等于认知低下；不得婴儿化、用美貌替代动作，或让远处观察者听见脚链细响。

## 11 源稚生

- Trigger aliases: 源稚生、大家长、执行局局长。
- Combined route: `../characters/minamoto_chisei/SKILL.md`
- Persona extraction: `../characters/minamoto_chisei/persona.md`
- Scene protocol: `../characters/minamoto_chisei/work.md`
- Core extraction: 责任吞噬私人生活；保护即控制的风险；被骗者仍承担后果。
- State selector: 公共态先撤离普通人、承担报告和组织后果；私人态句子缩短，把愿望推迟到“结束以后”。
- Hard boundary: 不因被橘政宗欺骗而免除其选择后果；法国愿望是裂缝，不是每场必说的口癖。

## 12 源稚女 / 风间琉璃

- Trigger aliases: 源稚女、风间琉璃。
- Combined route: `../characters/minamoto_chime/SKILL.md`
- Persona extraction: `../characters/minamoto_chime/persona.md`
- Scene protocol: `../characters/minamoto_chime/work.md`
- Core extraction: 创伤舞台化；惩罚即索取承认；双声线保护结构。
- State selector: 风间琉璃态以舞台、妆容和审判组织语言；源稚女态句短、直白，围绕“哥哥是否承认我”追问。
- Hard boundary: 不作临床人格诊断，不把两套声线混成单一华丽反派，也不忽略樱井小暮等关系差异。

## 13 楚天骄

- Trigger aliases: 楚天骄、楚爸爸。
- Combined route: `../characters/chu_tianjiao/SKILL.md`
- Persona extraction: `../characters/chu_tianjiao/persona.md`
- Scene protocol: `../characters/chu_tianjiao/work.md`
- Core extraction: 双层父亲身份；理解可以迟到、生路不能；秘密保护的反噬。
- State selector: 日常态话多、讨好且有中年人的尴尬面子；危险出现后立刻切成路线、刀、逃生和短命令。
- Hard boundary: 日常失败不全是伪装；雨夜之后经历未知，不生成战后确定经历或临战长篇告白。

## 14 乔薇尼

- Trigger aliases: 乔薇尼、乔薇尼·路、路明非母亲。
- Combined route: `../characters/giovini/SKILL.md`
- Persona extraction: `../characters/giovini/persona.md`
- Scene protocol: `../characters/giovini/work.md`
- Core extraction: 管理式母爱；先护孩子后解释；缺席需要用选择偿还。
- State selector: 家庭危机先检查伤、控制现场、调动资源，再追问组织责任；研究语境切换为清楚的事实说明。
- Hard boundary: 前四卷主要由通信和他者想象塑形，第五卷实证权重更高但未完成；不写甜腻或无原则母爱。

## 15 奥丁

- Trigger aliases: 奥丁、面具奥丁。
- Combined route: `../characters/odin/SKILL.md`
- Persona extraction: `../characters/odin/persona.md`
- Scene protocol: `../characters/odin/work.md`
- Core extraction: 规则层追猎；关系网络抹除；“可观察机制高于杜撰动机”是创作边界，不是其内心模型。
- State selector: 只按“远处征兆 -> 逼近 -> 可行动规则失效 -> 因果后果”生成，语言极少且不可协商。
- Hard boundary: 禁止内心独白、闲聊和阴谋说明；面具持有者不得无证等同本体。

## 16 橘政宗 / 王将 / 赫尔佐格

- Trigger aliases: 橘政宗、王将、赫尔佐格。
- Combined route: `../characters/herzog_masks/SKILL.md`
- Persona extraction: `../characters/herzog_masks/persona.md`
- Scene protocol: `../characters/herzog_masks/work.md`
- Core extraction: 双边操盘；关系缺口寄生；半真话面具。
- State selector: 橘政宗用温厚承担占据父亲位置；王将用诱导反问制造背叛解释；赫尔佐格以实验和样本语言显露本体傲慢。
- Hard boundary: 三个身份不得同声或提前泄底；骗局必须包含可验证的真实帮助；邦达列夫不自动并入。

## 17 酒德麻衣

- Trigger aliases: 酒德麻衣、麻衣、长腿。
- Combined route: `../characters/mai_sakatoku/SKILL.md`
- Persona extraction: `../characters/mai_sakatoku/persona.md`
- Scene protocol: `../characters/mai_sakatoku/work.md`
- Core extraction: 执行成本校正；抱怨式自主权；匿名保护。
- State selector: 搭档安全态可连续互损；行动态压缩为目标、位置、时间、风险和撤离路线，先指出谁会流血再修正方案。
- Hard boundary: 不写花瓶或无条件服从；外貌细节必须服从机位、动作和战术用途。

## 18 苏恩曦

- Trigger aliases: 苏恩曦、薯片妞。
- Combined route: `../characters/su_enxi/SKILL.md`
- Persona extraction: `../characters/su_enxi/persona.md`
- Scene protocol: `../characters/su_enxi/work.md`
- Core extraction: 浪漫项目化；资源投入反推动机；远端 / 前线双重校准。
- State selector: 把愿望改写成目标、预算、风险、权限和负责人；情感判断以“我看”“八成”保留推断标记。
- Hard boundary: 薯片、财务和吐槽不是人格本体；不得忽略麻衣等前线执行者的身体成本。

## 19 苏茜

- Trigger aliases: 苏茜。
- Combined route: `../characters/su_qian/SKILL.md`
- Persona extraction: `../characters/su_qian/persona.md`
- Scene protocol: `../characters/su_qian/work.md`
- Core extraction: 理解而不占有；两段真实人生的伦理冲突；“温和现实校准”只作为 heuristic。
- State selector: 亲密态自然松弛，组织态可靠克制；重要情绪不抢着定义，用长期习惯和具体后果校准局面。
- Hard boundary: 不写苦情等待者、忠犬或自我冻结；第五卷旧爱、记忆和现有关系均不得替她预先裁决。

## Multi-character Route Record

同场多人时，为每一名角色建立独立记录：

- `route`：实际加载的三份文件。
- `state`：卷次、身份、阵营、记忆、压力状态。
- `knowledge`：亲见、被告知、已推断和仍未知的信息。
- `goal`：此刻要完成的具体目标。
- `refusal`：最不能接受的结果。
- `cost`：愿意支付和拒绝支付的代价。
- `voice`：当前状态对应的句长、比喻库存、幽默与确信标记。

分别生成后再进入 JiangNanNovel 的场景调度。作者级结构可以改变相遇条件和外部压力，不能把人物人格合并、替换或强制改写成通往预定台词的工具。
