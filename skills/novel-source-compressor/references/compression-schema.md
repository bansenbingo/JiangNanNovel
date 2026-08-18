# Compression Schema

本文件定义压缩结果的最小交接协议。用户只要摘要时可省略章节卡；用户要续写或完整大纲时保留全部高风险字段。

## 1. 版本头

```yaml
source_outline_state:
  version: "source-v0.1"
  mode: "handoff-compress | standalone-outline | incremental-merge | archive-dossier"
  source_scope: "读取的文件、章节、分卷、范围和抽样方式"
  source_status: "complete | unfinished | partial | conflicting"
  compression_depth: "quick | standard | deep"
  confidence: "high | medium | low"
  traceability: []
  compression_risks: []
```

`version` 和 `mode` 是规范路由字段。读取旧状态时可将 `state_version` 映射为 `version`、将 `compression_mode` 映射为 `mode`；新输出不要继续写旧别名。`traceability` 保存高风险结论与来源位置，`compression_risks` 保存可能漏失、冲突或值得回读的原文窗口，二者都必须随交接状态传递。

随后分别列出：

- `locked_facts`：原文直接确认，附来源位置。
- `user_constraints`：用户要求保留、改动、删除或用途限制。
- `inferred_items`：压缩者为连接因果提出的推演。
- `unknowns_and_conflicts`：未读、未决或版本冲突。

## 2. 故事核心

```yaml
story_engine:
  logline: "主角 + 欲望/问题 + 主要阻力 + 代价"
  reality_gap: "奇观之前的现实困境；无证据时写 unknown"
  desired_normal: "人物试图保住的日常、关系或承诺"
  central_choice: "最终不能同时保住的两件事"
  public_result: "对外部世界的结果"
  private_result: "对人物关系/身份/记忆的结果"
  ending_state: "原文结尾或当前末尾状态"
```

## 3. 段落、章节和场景卡

### 段落/卷卡

| 字段 | 含义 |
| --- | --- |
| id / source_range | 稳定 ID 与来源范围 |
| purpose | 本段在全局结构中的功能 |
| entry_state | 人物、局势和信息的进入状态 |
| pressure | 迫使人物行动的外部/内部压力 |
| milestones | 关键事件和主动选择 |
| lowpoint_or_cost | 付出的不可逆代价 |
| exit_state | 离开时的新局面 |
| promises_created/closed | 创建、施压、回收或放弃的承诺 |

### 章节卡

```yaml
chapter:
  id: "C03"
  source_range: "卷/文件/章节"
  title: "原文标题或工作标题"
  pov: "视角人物；不确定则 unknown"
  entry_state: "进入时状态"
  goal_and_obstacle: "谁想得到什么，什么阻止他"
  events: ["只列改变状态的事件"]
  choice: "谁主动选择了什么；若无主动选择，标注"
  information_delta: "谁知道了什么/误会了什么"
  relationship_delta: "关系具体如何变化"
  cost: "选择或失败的代价"
  exit_state: "下一章承接的状态"
  setup_payoff: ["建立/施压/回收的承诺或伏笔"]
  evidence: ["文件和章节定位"]
```

## 4. 人物与连续性

人物记录：`current_state`、`wants`、`needs`、`knowledge`、`misbelief`、`boundary`、`resources`、`pressure_response`、`relationship_changes`、`next_pressure`、`evidence`。

连续性账本记录：

- 时间、地点、场景顺序、旅行耗时和同场可行性
- 伤势、能力条件、秘密、组织状态、资源和物件去向
- 关系的 `before -> pressure -> choice -> after`
- 线程和承诺的 `open | pressured | paid | abandoned | conflicting`

## 5. 续写交接

```yaml
ending_or_last_stable_point:
  source_location: "末尾章节或文件位置"
  state: "明确发生了什么"
  characters: ["每个关键人物的状态/信息/资源/关系"]
  unresolved_pressure: ["下一步必须处理的压力"]
  forbidden_rewrites: ["除非用户改口，不应静默改变的事实"]

next_scene_candidates:
  - option: "从哪个出口状态开始"
    solves: "优先解决什么"
    delays_or_costs: "会延后或牺牲什么"

traceability:
  - claim: "高风险结论"
    evidence: "来源位置"
    confidence: "high | medium | low"

compression_risks:
  - risk: "可能漏失、合并失真、推演越界、版本冲突或末尾不稳定"
    source_window: "建议回读的最小原文范围"
    action: "交给下游前的核验动作"
```
