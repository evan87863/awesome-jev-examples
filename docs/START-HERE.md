# Getting started

**English** · [简体中文](START-HERE.zh-CN.md) · [日本語](START-HERE.ja.md) · [Español](START-HERE.es.md)

[Back to index](../README.md)

1. Read the official quick start and understand `state` and `questions`.
2. Pick one project close to your use case. Read what Jev receives and what it decides.
3. Check fallbacks, uncertainty, external models, and independent outcome verification.
4. Before automating actions, evaluate a small labeled sample from your own task.

## Suggested reading

- [Quick start](https://docs.typesafe.ai/introduction/quickstart) — Make a first typed request in the Playground or SDK.
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) — Choose a browser operation and target together from a dynamic table of page elements.
- [Jev Review (devagrawal09)](https://github.com/devagrawal09/jev-review) — Review diffs or repositories through staged risk screening, evidence selection, and severity scoring.
- [Kill My Idea](https://github.com/monteduro/killmyidea) — Ask parallel questions about a startup idea and combine scores into a fixed verdict.
- [neo4jev](https://github.com/jexp/neo4jev) — Choose the next graph relationship and check whether the goal is reached in the same call.
- [Janus](https://github.com/FirasSX914/Janus) — Measure when to route between small and large models, including when routing should be rejected.
- [Jev Chess Lab](https://github.com/denikuchero/jev-chess-lab) — Recorded chess experiments compare Jev alone, tactical filters, and Stockfish assistance.

A useful pattern across these examples: code builds the candidate actions, Jev chooses or scores, and code checks the outcome. Free-text generation or complex reasoning may still use another model.
