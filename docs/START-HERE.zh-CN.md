# 入门路线

[English](START-HERE.md) · **简体中文** · [日本語](START-HERE.ja.md) · [Español](START-HERE.es.md)

[返回索引](../README.zh-CN.md)

1. 先读官方快速开始，理解 `state` 与 `questions`。
2. 选择接近自己需求的项目，确认 Jev 收到了什么、负责什么判断。
3. 查看兜底、不确定性、其他模型参与和独立结果验证。
4. 在自动执行之前，先用自己任务的一小组有标签样本评估。

## 建议阅读

- [快速开始](https://docs.typesafe.ai/introduction/quickstart) — 在 Playground 和 SDK 中构建第一个类型化判断。
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) — 从动态页面元素表中同时选择操作和目标元素。
- [Jev Review（devagrawal09）](https://github.com/devagrawal09/jev-review) — 分阶段评估 diff 或代码库，选择证据、归类问题并评分。
- [Kill My Idea](https://github.com/monteduro/killmyidea) — 并行提出多个问题，将创业点子评分组合成固定结论。
- [neo4jev](https://github.com/jexp/neo4jev) — 对图中相邻关系做 Choice 判断，同时检查是否到达目标。
- [Janus](https://github.com/FirasSX914/Janus) — 测量小模型与大模型的分流阈值，允许得出不应分流的结论。
- [Jev Chess Lab](https://github.com/denikuchero/jev-chess-lab) — 记录独立下棋、战术筛选及 Stockfish 辅助等不同实验。

这些案例中常见的结构是：代码构建候选动作，Jev 选择或评分，代码再核对结果。自由文本和复杂推理可能仍由其他模型完成。
