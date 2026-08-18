# 维度 3：语言指纹

## Collection Metadata
- Dimension: 3 Expression DNA / 语言指纹
- Collection strategy: local-first
- Sources searched: 三个主系列、补充小说、散文/文论/序跋、访谈和设定集的清洗分卷
- Sources used: 10
- Primary vs secondary ratio: 10:0
- Safety note: 本轨只记录统计、节奏功能和声部切换，不保存标志性句式、口癖清单或可拼贴原句

## Source Metadata
- ID: E1
- URL: local://original-materials/reference-series/dragon
- Source type: book corpus / fiction samples
- Grounding level: primary（一手）
- Access note: 龙族 I-V 共 62 个分卷样本，约 2,885,794 字符；留出分卷 08、21、35 单独判定
- Source weight: 1
- Date: local access 2026-08-17

## Source Metadata
- ID: E2
- URL: local://original-materials/reference-series/novolume
- Source type: book corpus / fiction samples
- Grounding level: primary（一手）
- Access note: 九州缥缈录 67 个分卷样本，约 1,165,358 字符；留出分卷 08、33、58 单独判定
- Source weight: 1
- Date: local access 2026-08-17

## Source Metadata
- ID: E3
- URL: local://original-materials/reference-series/blazing-sky
- Source type: book corpus / fiction samples
- Grounding level: primary（一手）
- Access note: 天之炽 37 个分卷样本，约 639,987 字符；留出分卷 06、19、31 单独判定
- Source weight: 1
- Date: local access 2026-08-17

## Source Metadata
- ID: E4
- URL: local://original-materials/jiangnan-cleaned/supplemental-fiction
- Source type: multi-work fiction corpus
- Grounding level: primary（一手）
- Access note: 去重后的补充长短篇、九州故事、武侠和其他小说，共 355 个分卷样本，约 3,563,788 字符
- Source weight: 1
- Date: local access 2026-08-17

## Source Metadata
- ID: E5
- URL: local://original-materials/jiangnan-cleaned/essays-criticism-interviews
- Source type: essay / criticism / interview corpus
- Grounding level: primary（一手）
- Access note: 散文、杂文、文论、影评、序跋、刊首语和访谈共 88 个分卷样本，约 859,542 字符
- Source weight: 1
- Date: local access 2026-08-17

## Source Metadata
- ID: E6
- URL: local://original-materials/essays/retrospectives
- Source type: essay series
- Grounding level: primary（一手）
- Access note: 温故 2005、2008、2009、2015 及相关年度自述，用于跨期语域比较
- Source weight: 1
- Date: 2005-2015; accessed 2026-08-17

## Source Metadata
- ID: E7
- URL: local://original-materials/craft/dragon-volume-three
- Source type: craft essay
- Grounding level: primary（一手）
- Access note: 龙族 III 创作手记，已用清洗版本排除嵌入的重复小说段落
- Source weight: 1
- Date: archive date uncertain; accessed 2026-08-17

## Source Metadata
- ID: E8
- URL: local://original-materials/craft/author-anti-patterns
- Source type: craft essay
- Grounding level: primary（一手）
- Access note: 作者工艺自评与失败模式文本组
- Source weight: 1
- Date: archive date uncertain; accessed 2026-08-17

## Source Metadata
- ID: E9
- URL: local://original-materials/interviews/literature-business-self-positioning
- Source type: chat interview
- Grounding level: primary（一手）
- Access note: 本地完整文字对话，用于非正式语域对照
- Source weight: 1
- Date: archive date uncertain; accessed 2026-08-17

## Source Metadata
- ID: E10
- URL: https://www.chinawriter.com.cn/n1/2020/1025/c405057-31905087.html
- Source type: long-form interview
- Grounding level: primary（一手访谈）
- Access note: 中国作家网具体文章页已检查，用于正式访谈语域对照
- Source weight: 3
- Date: 2020-10-25; accessed 2026-08-17

## Evidence
- [E1] 龙族样本平均句长 29.52 字，中位数 25 字，P90 为 59 字；对话和动作形成快速底盘，解释或情绪句在关键节点显著拉长。
- [E2] 九州样本平均句长 26.84 字，中位数 23 字，P90 为 52 字；战术、礼法和环境说明多嵌入人物位置变化，而不是连续百科段。
- [E3] 天之炽样本平均句长 31.43 字，中位数 27 字，P90 为 62 字；短命令、机械动作与较长视觉/身体感受交替，镜头式加速和骤停最明显。
- [E4] 补充小说平均句长 27.79 字，中位数 24 字，P90 为 54 字，说明主系列之外仍保留“短推进 + 长解释/情绪”的双速度，而非某一世界观偶然。
- [E5] 散文、文论和访谈平均句长 39.87 字，中位数 33 字，P90 为 78 字；进入论述语域后增加因果、转折、补充条件和自我修正。
- [E1-E5] 小说高对话密度与非虚构长句链形成稳定语域差：叙事先把读者带进行动，论述再把因果说开。
- [E1-E4 + holdout] 九个留出分卷的声部切换全部命中：快速动作/对白之后出现较慢的因果、记忆、制度解释、身体感觉或情绪停顿。
- [E1-E4] 角色语言按社会位置分工：处于弱势的人常用回避、玩笑或自我贬低保护自尊；掌握资源的人常用短命令、精确信息或沉默维持控制。
- [E5-E9] 严肃议题常由生活琐事、自嘲或夸张类比打开，中段转入较长论证，结尾落回行动承诺或具体生活图景。
- [E6/E7] 抽象判断经常需要空间、天气、身体负重、道路、物件功能或时间痕迹承载；意象的任务是改变意义，不是装饰性堆叠。
- [E9/E10] 正式访谈会减少粗粝和戏谑，但仍保留反问、类比、自我拆台和强断言后的限定；变的是表面温度，底层推理骨架较稳定。
- [E1-E4 + phase 2.5 correction validation] 轻快声部不仅负责降低阅读门槛，也负责把短暂同行、日常、友情、亲密或可能未来安装为“值得保留的价值”；后续胜利无法阻止这段未来被取消，相同的物件、玩笑、场所或生活愿望遂成为现实空缺的证据。

## Patterns and Repeated Themes
- 双速度句群：短动作/对白推进，长因果/感受句重估刚发生的事。
- 先具体后抽象：先写空间、动作、身体或物件功能，再允许情绪和判断浮现。
- 幽默是转场装置：承担降压、保护自尊或延迟直面悲伤的功能，不能只做段子。
- 强断言后自我校准：通过补条件、转折或承认例外防止论证绝对化。
- 角色声部分权：谁能下命令、谁必须解释、谁用笑话回避，本身就是关系状态。
- 意象必须变义：同一原创物件至少经历日常功能、冲突证据、情绪回响中的两次功能变化。
- 以乐写哀：先让欢乐场景完成关系建档和未来许诺，再让公共任务胜利与私人关系失去同时成立；余波返回日常声部，但旧日常已经带着缺席、债务或无法兑现的含义。

## Contradictions
- 表面语言常显得随意、口语甚至粗粝，工艺层面却高度追求戏剧结构、节奏和镜头调度。
- 反复书写英雄、战争与宏大秩序，最稳定的情感触点却是普通人的自卑、错过、孤独和无力。
- 自述不愿过度解释，非虚构文本实际压缩度偏低，常用长句把前因后果和限定交代充分。
- 快慢切换能制造强烈情绪，但高频死亡、牺牲和骤停式抒情也可能造成情绪通胀。
- 乐声部能够抬高损失价值，但若每次欢乐都机械预告死亡，读者会提前识别操纵意图，反而削弱人物的真实生活感。

## Inferences (clearly marked)
- 推断：可识别度来自“口语缓冲 + 因果长句 + 具体俗物 + 宏观压力”同场协作，而不是任何单一固定句式。
- 推断：原创化生成只能迁移句群速度、信息功能和角色权力差，必须替换词汇组合、意象、人物、场景和结局。
- 推断：沉重场景之前可放置轻声部入口，但入口必须改变关系、信息或防御状态，否则只会稀释情绪。
- 推断：盲测不应以“像不像江南”为验收，而应检查双速度、角色声部分权、意象变义和行动后重估是否同时成立。
- 推断：原创场景应先给出至少一个读者希望保留下来的关系动作或生活状态；损失发生后，必须让路线、称谓、物件功能、身体或制度记录至少一项永久改变，而不是只靠抒情宣告悲伤。

## Gaps and Missing Information
- 句长统计是自动切句后的语料级指标，未做完整人工句法标注；标点清洗和版本差异会影响绝对数值。
- 缺少原始音视频，无法可靠建模真实口语中的语速、停顿、音高和非语言反应。
- 跨二十余年的作品存在编辑与修订变量，不能把所有语言变化都解释为作者认知变化。
- 为避免可冒充模仿，本轨有意不输出高频口癖、固定比喻模板或可直接复制的句式配方。
