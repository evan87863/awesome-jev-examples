# Initial research log

[Back to index](../README.md) · [简体中文](RESEARCH.zh-CN.md)

Source-review date: September 19, 2026. Goal: a use-case-oriented Jev collection with traceable primary sources.

## Discovery sources

- [TypeSafe documentation index](https://docs.typesafe.ai/llms.txt): official cookbooks, patterns, and SDK material.
- [MrJev / awesome-jev](https://github.com/MrJev/awesome-jev): community repositories. We then read each included author's README and wrote our own summaries rather than adopting the directory's review claims.
- [hellogumbo / awesome-jev](https://github.com/hellogumbo/awesome-jev): additional ecosystem discovery.
- [Made with Jev](https://madewithjev.com/): specific X posts and YouTube URLs retained as pending leads.
- Web search: social automation, startup-idea scoring, secret detection, bounded text-generation experiments, and first-party integration reports.

Representative queries: `"jev" AI examples github`, `"jev" "noul"`, `Jev TypeSafe YouTube demo`, and `Jev typesafe site:x.com`. Search results located sources; primary text supported the technical summaries.

## Completed review

- Read README material from 46 source-code projects/SDKs, recording source URLs and hashes.
- Retrieved 25 official pages: 23 complete transfers, plus partial introductions for intent routing and Noul consistency checked against the official index. Both are explicitly marked.
- Read Retriever AI's own browser-integration report, preserving its limited experimental scope and cost tradeoff.
- Collected 28 specific video/social leads in a separate queue.
- Did not clone, install, or execute third-party projects, or use API credentials from the surrounding workspace.

## Access limits and excluded leads

Direct YouTube pages and oEmbed requests timed out; search did not return reviewable original video content. An X sample returned 403 through search. A later browser read exposed Moritz Kremb's original title and chapters, but not a full video review, so the entry remains pending.

Several GitHub HEAD/raw README paths returned 404. This does not prove repository deletion: filenames or branches may differ. The following were excluded from the reviewed collection: `typesafe-ai/typesafe-sdk-js`, `AntonioCoppe/jev-harness`, `jomatsu/zod-jev`, `kieranklaassen/ruby_llm-typesafe`, `yusukebe/hono-jev-router`, `reachjalil/jev-tree`, `zampierid4p/n8n-nodes-typesafe-ai`, and `ellipsis-dev/blink`. The retrieved body for `standardagents/jevpilot` was empty and was also excluded.

External directory totals were not counted as our reviewed resources. Alternative models and projects that merely mention Jev were not automatically included.

## Useful follow-up research

- Watch candidate videos, confirm authors and official titles, and add timestamps and code links.
- Attach original release posts to existing GitHub entries rather than duplicating projects.
- Reproduce one project per category in an isolated environment with inputs, outputs, and failures recorded.
- Add more first-hand work from non-English creators.
- Recheck missing README paths before declaring projects unavailable.

Translations reorganize this research for readers; they do not represent additional source checks or independent reproductions.
