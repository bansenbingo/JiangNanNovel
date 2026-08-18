# Outline Schema

本文件是交接协议，不是要求每次输出都机械填满的表单。用户要小样时只输出前四段；用户要完整大纲时展开到章节卡和账本。

## A. 版本头

```yaml
outline_state:
  version: "v0.1"
  mode: "idea-to-outline | continue | branch-rewrite | deep-rewrite | repair-expand | hybrid"
  source_scope: "读取了哪些文件、章节或用户段落"
  canon_policy: "原创 | 原作事实+用户分歧 | 非官方同人 | 待确认"
  confidence: "high | medium | low"
  source_input: "若来自 source_outline_state，保留其路由元数据"
```

正文中另外列出：

- `locked_facts`：材料或用户明确锁定，除非用户改口不改。
- `user_changes`：与原材料不同的主动要求。
- `inferences`：为接通因果而提出的推演。
- `assumptions`：暂代缺失信息的默认值，必须可回滚。
- `open_questions`：仍可能改变主线的问题，按影响排序。
- `vision_capture`：用户用开放回答提供的原话、画面、情绪、关系愿景、硬边界，以及它们对结构的影响；不要把解释伪装成用户原话。

### vision_capture

```yaml
vision_capture:
  user_phrases: ["用户原话或关键比喻"]
  desired_images: ["想保留的瞬间、空间、动作"]
  emotional_truth: ["用户希望读者带走的感觉"]
  relationship_wish: ["关系最终希望变成什么样"]
  non_negotiables: ["不能静默改动的事实、人物或结局边界"]
  interpreted_impacts: ["这些回答影响了哪些冲突、结构和回收"]
  unresolved_meanings: ["仍需确认的隐喻或矛盾愿望"]
```

## B. 故事核心

```yaml
story_engine:
  logline: "主角 + 欲望/问题 + 阻力 + 必须支付的代价"
  reality_gap: "奇观出现前，人物在日常中解决不了什么"
  desired_normal: "什么共同生活、承诺或未来值得被保护"
  central_choice: "最终不能同时保住的两件事"
  public_result: "外部世界获得或失去什么"
  private_result: "人物关系、记忆或身份发生什么不可逆变化"
  ending_pressure: "结局要偿还的承诺"
```

## C. 人物和关系

每位主要人物一行，必要时再展开：

| 字段 | 内容 |
| --- | --- |
| current_state | 故事开始时的可观察状态 |
| wants / needs | 表层目标与真正需要 |
| false_belief | 他如何误读自己或他人 |
| boundary | 不愿做什么，什么会迫使他越界 |
| resources | 人脉、知识、权力、物件、时间等 |
| pressure_response | 受压时会隐瞒、交易、逃跑、保护还是攻击 |
| forcing_event | 让改变有因有果的事件 |
| final_choice | 他在高潮主动选择什么 |
| cost | 选择后不能恢复的代价 |

关系表至少记录：`before -> pressure -> choice -> after`。不要写“关系变好/变坏”，写谁对谁多知道了什么、交付了什么、撤回了什么。

## D. 宏观结构

```yaml
segments:
  - id: "V1-A1"
    purpose: "本段必须完成的故事功能"
    entry_state: "进入时人物和局势"
    milestones: ["事件/选择/转折"]
    midpoint_or_lowpoint: "若有"
    exit_state: "离开时的新局面"
    relationship_delta: "哪段关系改变"
    promises_created: ["新增承诺或问题"]
    promises_closed: ["本段回收"]
```

每卷/幕/阶段都要有入口、压力升级、选择、出口。若没有新状态，只是事件清单，应合并或删去。

## E. 章节/场景卡

```yaml
scene:
  id: "C03-S02"
  title: "工作标题，不要假装是成稿标题"
  pov: "视角人物"
  time_place: "时间与地点"
  entry_state: "上一节点留下的状态"
  scene_goal: "本场谁想得到什么"
  obstacle: "外部阻力与内部阻力"
  information_delta: "谁知道了什么，谁误会了什么"
  action_or_dialogue_turn: "把信息变成行动，而非说明书"
  irreversible_turn: "本场不可逆变化"
  exit_state: "下一场必须承接的压力"
  relationship_delta: "关系如何具体变化"
  cost: "为成功或失败付出的代价"
  setup_payoff: "建立/施压/回收的伏笔"
  continuity_checks: ["时间、伤势、物件、能力、承诺"]
```

## F. 账本与风险

完整版本附上：

- 时间线锚点和场景顺序
- 人物状态、伤势、秘密、资源和物件去向
- `open_threads`、`promises`、`payoffs` 的状态：`open | pressured | paid | intentionally-abandoned`
- 结构风险：支线抢戏、规则万能、高潮无代价、角色突然变形、结尾漂浮
- 本轮 `change_log`：接受、拒绝、暂缓，以及连锁影响

## G. 交接尾部

```yaml
next_scene_candidates:
  - option: "从哪个出口状态继续"
    benefit: "会优先解决什么"
    tradeoff: "会延后或牺牲什么"
```

给出至少两个下一步候选；用户选定后，后续技能可以直接从该节点开始，而不重新总结整本书。

## H. 从原文压缩状态接入

上游 `novel-source-compressor` 的 `source_outline_state` 可以直接作为输入。接入时保留来源和不确定性：

```yaml
source_input:
  version: "source-v0.1"
  source_scope: "压缩器已覆盖的文件/章节"
  source_status: "complete | unfinished | partial | conflicting"
  traceability: ["高风险结论与原文位置"]
  compression_risks: ["可能漏失或冲突的位置"]
  mode: "handoff-compress | incremental-merge"
  compression_depth: "quick | standard | deep"
  confidence: "high | medium | low"
```

旧版压缩状态若使用 `state_version` 或 `compression_mode`，分别映射为 `version` 和 `mode`；新版本不要继续输出别名。不要把 `inferred_items` 升格为 `locked_facts`，也不要因为压缩状态里有一个故事核心，就跳过用户对续写分歧点、结局和规模的选择。除非风险要求回读，续写规划从 `ending_or_last_stable_point` 之后开始。
