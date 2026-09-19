# Awesome Jev Examples

[English](README.md) · **简体中文** · [日本語](README.ja.md) · [Español](README.es.md)

> 发现 Jev 的实际用法，了解实现思路，找到原始资料。

面向 **[TypeSafe AI Jev](https://docs.typesafe.ai/introduction)** 的精选索引。Jev 根据给定状态回答 Choice、Score、Noul 类型的问题。本仓库为独立社区项目，与 TypeSafe AI 无隶属关系。

[入门路线](docs/START-HERE.zh-CN.md) · [全部详情](catalog/DETAILS.zh-CN.md) · [X / YouTube](catalog/MEDIA.zh-CN.md) · [贡献指南（英文）](CONTRIBUTING.md)

**72 条资源：**46 个源码项目/SDK、25 篇官方教程/模式/参考、1 篇开发团队实测。另有 **28 条 X / YouTube 线索**待核验。首批核对日期：2026-09-19。

核对表示阅读所标明的来源，不代表运行、审计或效果背书。本仓库尚未复现任何案例。两篇官方页面仅获取了部分正文，已单独标明。作者报告的性能数据未经独立复测。

## 从这些案例开始

- **[快速开始](https://docs.typesafe.ai/introduction/quickstart)** — 在 Playground 和 SDK 中构建第一个类型化判断。 [查看详情](catalog/DETAILS.zh-CN.md#official-quickstart)
- **[Jev Ultrafast](https://github.com/browser-use/jev-ultrafast)** — 从动态页面元素表中同时选择操作和目标元素。 [查看详情](catalog/DETAILS.zh-CN.md#browser-use--jev-ultrafast)
- **[Jev Review（devagrawal09）](https://github.com/devagrawal09/jev-review)** — 分阶段评估 diff 或代码库，选择证据、归类问题并评分。 [查看详情](catalog/DETAILS.zh-CN.md#devagrawal09--jev-review)
- **[Kill My Idea](https://github.com/monteduro/killmyidea)** — 并行提出多个问题，将创业点子评分组合成固定结论。 [查看详情](catalog/DETAILS.zh-CN.md#monteduro--killmyidea)
- **[neo4jev](https://github.com/jexp/neo4jev)** — 对图中相邻关系做 Choice 判断，同时检查是否到达目标。 [查看详情](catalog/DETAILS.zh-CN.md#jexp--neo4jev)
- **[Janus](https://github.com/FirasSX914/Janus)** — 测量小模型与大模型的分流阈值，允许得出不应分流的结论。 [查看详情](catalog/DETAILS.zh-CN.md#firassx914--janus)
- **[Jev Chess Lab](https://github.com/denikuchero/jev-chess-lab)** — 记录独立下棋、战术筛选及 Stockfish 辅助等不同实验。 [查看详情](catalog/DETAILS.zh-CN.md#denikuchero--jev-chess-lab)

## 按用途浏览

- [官方教程与 SDK](#official) (26)
- [浏览器、桌面与手机](#browser) (8)
- [编码 Agent 与 MCP](#agents) (8)
- [模型路由](#routing) (2)
- [审核、规则与安全检查](#safety) (5)
- [检索与知识图谱](#retrieval) (1)
- [数据处理与可观测性](#data) (4)
- [日常自动化与智能家居](#automation) (2)
- [产品与内容工具](#applications) (4)
- [游戏与仿真](#games) (6)
- [评测与置信度校准](#evaluation) (5)
- [边界实验](#experiments) (1)

<a id="official"></a>

## 官方教程与 SDK

| 资源 | 摘要与详情 |
| --- | --- |
| [官方 Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) | 用官方客户端完成工单分类等最小调用。 [查看详情](catalog/DETAILS.zh-CN.md#typesafe-ai--typesafe-sdk-python) |
| [快速开始](https://docs.typesafe.ai/introduction/quickstart) | 在 Playground 和 SDK 中构建第一个类型化判断。 [查看详情](catalog/DETAILS.zh-CN.md#official-quickstart) |
| [并行预测多个分支](https://docs.typesafe.ai/patterns/fan-out) | 把同一状态下可能需要的问题一次发送，再由代码选择适用答案。 [查看详情](catalog/DETAILS.zh-CN.md#official-fan-out) |
| [基于置信度分流](https://docs.typesafe.ai/patterns/confidence-routing) | 把决策结果和是否自动执行分开，低把握时升级处理。 [查看详情](catalog/DETAILS.zh-CN.md#official-confidence-routing) |
| [组合评分](https://docs.typesafe.ai/patterns/composite-scoring) | 拆开复杂评估的不同维度，再用代码组合。 [查看详情](catalog/DETAILS.zh-CN.md#official-composite-scoring) |
| [意图路由](https://docs.typesafe.ai/patterns/intent-routing) | 将输入分类后转给规则、专用模型或人工。 [查看详情](catalog/DETAILS.zh-CN.md#official-intent-routing) |
| [智能家居助手](https://docs.typesafe.ai/demos/smart-home) | 用同一请求评估用户的家庭控制意图。 [查看详情](catalog/DETAILS.zh-CN.md#official-smart-home) |
| [Jev 1.13 已知局限](https://docs.typesafe.ai/model-jaggedness/jev-1.13) | 查看官方公开的模型弱项和失败模式。 [查看详情](catalog/DETAILS.zh-CN.md#official-jev-1-13) |
| [Noul 一致性](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook) | 重复评估保险理赔相关判断，观察不确定答案的稳定性。 [查看详情](catalog/DETAILS.zh-CN.md#official-consistency-noul-cookbook) |
| [Choice 一致性](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook) | 为内容审核加入不确定结果，比较标签稳定性和自动处理比例。 [查看详情](catalog/DETAILS.zh-CN.md#official-consistency-choice-cookbook) |
| [并行问题批处理](https://docs.typesafe.ai/cookbooks/parallel_questions) | 对同一文档的多个问题比较合并与分开请求。 [查看详情](catalog/DETAILS.zh-CN.md#official-parallel-questions) |
| [检索重排](https://docs.typesafe.ai/cookbooks/rerank_typesafe) | 先用 BM25 缩小候选，再对查询与段落关系打分。 [查看详情](catalog/DETAILS.zh-CN.md#official-rerank-typesafe) |
| [逐行语义搜索](https://docs.typesafe.ai/cookbooks/semantic_find) | 在文档行号候选中选择相关位置，并检查是否存在答案。 [查看详情](catalog/DETAILS.zh-CN.md#official-semantic-find) |
| [恢复文档结构](https://docs.typesafe.ai/cookbooks/autoformat) | 判断换行、标题、列表及代码块，重建丢失的 Markdown 结构。 [查看详情](catalog/DETAILS.zh-CN.md#official-autoformat) |
| [受限函数调用](https://docs.typesafe.ai/cookbooks/function_calling) | 把函数名和有限参数选项变成结构化决策。 [查看详情](catalog/DETAILS.zh-CN.md#official-function-calling) |
| [Agent 技能选择](https://docs.typesafe.ai/cookbooks/skill_suggestion) | 先筛选技能候选，再读取少量技能细节并允许全部拒绝。 [查看详情](catalog/DETAILS.zh-CN.md#official-skill-suggestion) |
| [知识图谱实体对齐](https://docs.typesafe.ai/cookbooks/entity_alignment) | 比较两份目录里的候选实体，决定合并、不关联或交由人工。 [查看详情](catalog/DETAILS.zh-CN.md#official-entity-alignment) |
| [RAG 段落分类](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) | 在检索与生成之间检查相关性、冲突和指令注入。 [查看详情](catalog/DETAILS.zh-CN.md#official-classifying-rag-passages) |
| [引用核对](https://docs.typesafe.ai/cookbooks/citation_check) | 先确定引用原句存在，再判断上下文是否支持声明。 [查看详情](catalog/DETAILS.zh-CN.md#official-citation-check) |
| [LLM 输入输出检查](https://docs.typesafe.ai/cookbooks/llm_guardrails) | 以多个风险问题和严重度评分决定通过、审核或拦截。 [查看详情](catalog/DETAILS.zh-CN.md#official-llm-guardrails) |
| [结构化抽取级联](https://docs.typesafe.ai/cookbooks/sde_cascade) | 小模型先抽取，Jev 验证字段，必要时升级推理模型。 [查看详情](catalog/DETAILS.zh-CN.md#official-sde-cascade) |
| [日期抽取](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook) | 选择文中日期的组成部分，由代码解析相对日期并验证。 [查看详情](catalog/DETAILS.zh-CN.md#official-date-extraction-cookbook) |
| [候选值抽取](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) | 正则先找到邮箱、电话和金额候选，Jev 选择所需片段。 [查看详情](catalog/DETAILS.zh-CN.md#official-pre-parsed-value-extraction-cookbook) |
| [分层分类](https://docs.typesafe.ai/cookbooks/hierarchical_classification) | 在专利、商品等层级标签中使用概率驱动的搜索。 [查看详情](catalog/DETAILS.zh-CN.md#official-hierarchical-classification) |
| [自动发现文本特征](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery) | 让 LLM 提问题，Jev 转成数值特征，再训练 CatBoost 并迭代。 [查看详情](catalog/DETAILS.zh-CN.md#official-autoresearch-feature-discovery) |
| [带退让策略的分类](https://docs.typesafe.ai/cookbooks/classification_using_confidence) | 给年报选择行业类别，低置信度时退回更宽泛类别。 [查看详情](catalog/DETAILS.zh-CN.md#official-classification-using-confidence) |

<a id="browser"></a>

## 浏览器、桌面与手机

| 资源 | 摘要与详情 |
| --- | --- |
| [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) | 从动态页面元素表中同时选择操作和目标元素。 [查看详情](catalog/DETAILS.zh-CN.md#browser-use--jev-ultrafast) |
| [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) | 用 OCR 与辅助功能提取 Mac 界面状态，再由 Jev 选择动作。 [查看详情](catalog/DETAILS.zh-CN.md#awlevin--typesafe-computer-use) |
| [Jev Browser](https://github.com/jkudish/jev-browser) | 通过库、CLI 或 MCP 控制浏览器，并记录逐步决策。 [查看详情](catalog/DETAILS.zh-CN.md#jkudish--jev-browser) |
| [Mobile Jev](https://github.com/droidrun/mobile-jev) | 在 Mobilerun Android 设备上依据界面状态选择动作。 [查看详情](catalog/DETAILS.zh-CN.md#droidrun--mobile-jev) |
| [Unclutter](https://github.com/kitze/unclutter) | 浏览器扩展使用 Jev 识别页面杂乱内容并复用模板规则。 [查看详情](catalog/DETAILS.zh-CN.md#kitze--unclutter) |
| [TypeSafe Fun AdBlocker](https://github.com/realZachi/typesafe-adblock) | 判断 DOM 元素是否像广告，并由浏览器代码移除。 [查看详情](catalog/DETAILS.zh-CN.md#realzachi--typesafe-adblock) |
| [Jev for Social Media](https://github.com/socai-io/jev-social) | 由 Jev 选择搜索、打开帖子等操作，socai 在浏览器执行。 [查看详情](catalog/DETAILS.zh-CN.md#socai-io--jev-social) |
| [Retriever AI：浏览器动作选择实测](https://rtrvr.ai/blog/jev-browser-agent-benchmark) | 开发团队记录如何用 Jev 选择浏览器动作、用 GLM 处理计划和生成。 [查看详情](catalog/DETAILS.zh-CN.md#rtrvr-browser-benchmark) |

<a id="agents"></a>

## 编码 Agent 与 MCP

| 资源 | 摘要与详情 |
| --- | --- |
| [Typesafe MCP](https://github.com/itsmostafa/typesafe-mcp) | 通过 MCP 把 Jev 的结构化判断提供给编码助手。 [查看详情](catalog/DETAILS.zh-CN.md#itsmostafa--typesafe-mcp) |
| [Jev MCP（jkudish）](https://github.com/jkudish/jev-mcp) | 提供验证、筛选、重排、分类、审查等判断工具。 [查看详情](catalog/DETAILS.zh-CN.md#jkudish--jev-mcp) |
| [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 对工具调用和结果评分，删除或截短过时内容，保留其余原文。 [查看详情](catalog/DETAILS.zh-CN.md#tamaratran--fast-jev-compaction) |
| [Foreman](https://github.com/thruwire/foreman) | 使用 Jev 评估编码工作是否完成、测试是否充分及是否需要人工输入。 [查看详情](catalog/DETAILS.zh-CN.md#thruwire--foreman) |
| [Winnow](https://github.com/GhalebDweikat/winnow) | 在大块工具结果进入上下文前筛选内容，保留恢复原文的入口。 [查看详情](catalog/DETAILS.zh-CN.md#ghalebdweikat--winnow) |
| [Jev Review（devagrawal09）](https://github.com/devagrawal09/jev-review) | 分阶段评估 diff 或代码库，选择证据、归类问题并评分。 [查看详情](catalog/DETAILS.zh-CN.md#devagrawal09--jev-review) |
| [Jev Review MCP](https://github.com/NiazMorshed2007/jev-review) | 本地 MCP 服务为编码助手提供持续的软件质量评分。 [查看详情](catalog/DETAILS.zh-CN.md#niazmorshed2007--jev-review) |
| [Jev MCP（blakestone-x）](https://github.com/blakestone-x/jev-mcp) | 为 agent 提供分类、评分、匹配和筛选工具及请求模板。 [查看详情](catalog/DETAILS.zh-CN.md#blakestone-x--jev-mcp) |

<a id="routing"></a>

## 模型路由

| 资源 | 摘要与详情 |
| --- | --- |
| [Jev Codex Router](https://github.com/0xNatoshi/jev-codex-router) | 按对话轮次判断任务需求并选择模型与思考深度。 [查看详情](catalog/DETAILS.zh-CN.md#0xnatoshi--jev-codex-router) |
| [jev-router](https://github.com/gargpratyush/jev-router) | 为 Claude Code 与 Codex 的新一轮任务选择执行模型。 [查看详情](catalog/DETAILS.zh-CN.md#gargpratyush--jev-router) |

<a id="safety"></a>

## 审核、规则与安全检查

| 资源 | 摘要与详情 |
| --- | --- |
| [Tripwire](https://github.com/noelzappy/tripwire) | 在模型响应到达用户前检查内容，支持中间件与代理。 [查看详情](catalog/DETAILS.zh-CN.md#noelzappy--tripwire) |
| [jev-gates](https://github.com/rashedInt32/jev-gates) | 为编码流程检查规则、范围、完成声明等条件。 [查看详情](catalog/DETAILS.zh-CN.md#rashedint32--jev-gates) |
| [pi-warden](https://github.com/DevMortimer/pi-warden) | 在编辑和工具调用过程中检查规则、重试循环及完成声明。 [查看详情](catalog/DETAILS.zh-CN.md#devmortimer--pi-warden) |
| [Safer with Jev](https://github.com/andrelandgraf/safer-with-jev) | 展示内容判断与可选请求转发的组合。 [查看详情](catalog/DETAILS.zh-CN.md#andrelandgraf--safer-with-jev) |
| [Triagedy](https://github.com/m0rphtail/triagedy) | 把 JSONL 安全告警转成结构化分诊结果。 [查看详情](catalog/DETAILS.zh-CN.md#m0rphtail--triagedy) |

<a id="retrieval"></a>

## 检索与知识图谱

| 资源 | 摘要与详情 |
| --- | --- |
| [neo4jev](https://github.com/jexp/neo4jev) | 对图中相邻关系做 Choice 判断，同时检查是否到达目标。 [查看详情](catalog/DETAILS.zh-CN.md#jexp--neo4jev) |

<a id="data"></a>

## 数据处理与可观测性

| 资源 | 摘要与详情 |
| --- | --- |
| [pg-jev](https://github.com/realZachi/pg-jev) | PostgreSQL 扩展以自然语言条件筛选、排序和分类行。 [查看详情](catalog/DETAILS.zh-CN.md#realzachi--pg-jev) |
| [jevQL](https://github.com/kylemclaren/jevql) | 在客户端为普通 PostgreSQL 查询补充 Jev 判断。 [查看详情](catalog/DETAILS.zh-CN.md#kylemclaren--jevql) |
| [duckdb-jev](https://github.com/colliber/duckdb-jev) | 在 DuckDB 查询中为表或 Parquet 数据返回类型化判断。 [查看详情](catalog/DETAILS.zh-CN.md#colliber--duckdb-jev) |
| [Jev Logs](https://github.com/reachjalil/jevlogs) | 给 OpenTelemetry 日志评分，再决定是否进入昂贵分析分支。 [查看详情](catalog/DETAILS.zh-CN.md#reachjalil--jevlogs) |

<a id="automation"></a>

## 日常自动化与智能家居

| 资源 | 摘要与详情 |
| --- | --- |
| [Jev for Home Assistant](https://github.com/AboveColin/HA-Jev) | 把家庭状态交给 Jev 判断，返回可用于自动化的数值结果。 [查看详情](catalog/DETAILS.zh-CN.md#abovecolin--ha-jev) |
| [jev-shell-history](https://github.com/mrnugget/jev-shell-history) | 根据正在输入的内容为 zsh 历史命令排序。 [查看详情](catalog/DETAILS.zh-CN.md#mrnugget--jev-shell-history) |

<a id="applications"></a>

## 产品与内容工具

| 资源 | 摘要与详情 |
| --- | --- |
| [TypeSafe AI Playground（Rust CLI）](https://github.com/markjaquith/typesafe-ai-playground) | 集合隐私信息检测、注释审查、语气及业务分类实验。 [查看详情](catalog/DETAILS.zh-CN.md#markjaquith--typesafe-ai-playground) |
| [Jev Moderation Bot](https://github.com/brainstormity/Jev-Moderation-Bot) | Discord 机器人判断垃圾信息与诈骗链接并执行分级处理。 [查看详情](catalog/DETAILS.zh-CN.md#brainstormity--jev-moderation-bot) |
| [JEVMETER](https://github.com/ChetasLua/jevmeter) | 对视频转录逐句提问，再把结果渲染成视频仪表。 [查看详情](catalog/DETAILS.zh-CN.md#chetaslua--jevmeter) |
| [Kill My Idea](https://github.com/monteduro/killmyidea) | 并行提出多个问题，将创业点子评分组合成固定结论。 [查看详情](catalog/DETAILS.zh-CN.md#monteduro--killmyidea) |

<a id="games"></a>

## 游戏与仿真

| 资源 | 摘要与详情 |
| --- | --- |
| [1v1 Jev](https://github.com/emrickgarrett/OneVOneJev) | 浏览器对战游戏以 Jev 决定角色行动。 [查看详情](catalog/DETAILS.zh-CN.md#emrickgarrett--onevonejev) |
| [TypeSafe Mario](https://github.com/fhshaik/typesafe-mario) | 把模拟器 RAM 与遥测转成结构化状态，由 Jev 选择手柄输入。 [查看详情](catalog/DETAILS.zh-CN.md#fhshaik--typesafe-mario) |
| [Jev Plays StarCraft](https://github.com/phyous/tsai-sc) | 用结构化游戏状态驱动星际争霸试玩任务，保存动作概率。 [查看详情](catalog/DETAILS.zh-CN.md#phyous--tsai-sc) |
| [Jev Pong](https://github.com/ably-labs/jev-pong) | Pong 球每得到一次模型决策前进一步，以可视化模型等待。 [查看详情](catalog/DETAILS.zh-CN.md#ably-labs--jev-pong) |
| [jev-drone](https://github.com/RomanSlack/jev-drone) | MuJoCo 无人机仿真中让 Jev 判断局面，普通代码执行实时控制。 [查看详情](catalog/DETAILS.zh-CN.md#romanslack--jev-drone) |
| [Jev Chess Lab](https://github.com/denikuchero/jev-chess-lab) | 记录独立下棋、战术筛选及 Stockfish 辅助等不同实验。 [查看详情](catalog/DETAILS.zh-CN.md#denikuchero--jev-chess-lab) |

<a id="evaluation"></a>

## 评测与置信度校准

| 资源 | 摘要与详情 |
| --- | --- |
| [jevcal](https://github.com/abhixhek/jevcal) | 用自己的数据选择置信度阈值并检测模型变化。 [查看详情](catalog/DETAILS.zh-CN.md#abhixhek--jevcal) |
| [Janus](https://github.com/FirasSX914/Janus) | 测量小模型与大模型的分流阈值，允许得出不应分流的结论。 [查看详情](catalog/DETAILS.zh-CN.md#firassx914--janus) |
| [jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) | 评估结构化模型的概率校准、自动化覆盖率和资源消耗。 [查看详情](catalog/DETAILS.zh-CN.md#abdelstark--jev-benchmarks) |
| [typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) | 在相同应用任务上比较 LLM 结构化输出与 Jev。 [查看详情](catalog/DETAILS.zh-CN.md#iammrduncan--typesafe-ai-benchmark) |
| [jev-secret-detection](https://github.com/teyhouse/jev-secret-detection) | 对代码片段提出 Noul 问题，评估是否含真实凭据。 [查看详情](catalog/DETAILS.zh-CN.md#teyhouse--jev-secret-detection) |

<a id="experiments"></a>

## 边界实验

| 资源 | 摘要与详情 |
| --- | --- |
| [jev-llm](https://github.com/Code-Forge-AU/jev-llm) | 循环从词表选择下一个词，把决策模型组成文字生成实验。 [查看详情](catalog/DETAILS.zh-CN.md#code-forge-au--jev-llm) |

## 维护索引

英文为主版本。修改 `data/resources.json`，同步更新 `data/locales/` 下的三个译本，再统一生成所有语言版本。需要 Python 3.10+，无需安装依赖或提供 API key。

```sh
python3 scripts/catalog.py
python3 scripts/catalog.py --check
python3 scripts/catalog.py --search browser --lang en
```

检查涵盖数据、翻译完整性、重复条目、生成文件和本地链接，不检测远程服务可用性，也不调用模型。

参阅[核验方法](docs/METHODOLOGY.zh-CN.md)、[研究记录](docs/RESEARCH.zh-CN.md)和[贡献指南](CONTRIBUTING.zh-CN.md)。原创摘要与脚本采用 [MIT 许可证](LICENSE)，外链资源保留原许可证。
