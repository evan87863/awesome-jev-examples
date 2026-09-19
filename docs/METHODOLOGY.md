# Scope and review methodology

[Back to index](../README.md) · [简体中文](METHODOLOGY.zh-CN.md)

## Scope

Public projects that use TypeSafe Jev, official practical guides, and first-party integration reports. Applications, SDKs, guides, and evaluations are labeled separately. Jev-inspired alternative models are outside this initial collection, so “uses Jev” and “inspired by Jev” are not confused.

## Evidence levels

| Value | What was checked | What it does not establish |
| --- | --- | --- |
| `readme-reviewed` | The original repository README explicitly describes Jev use | Code audit, execution, or effectiveness |
| `doc-reviewed` | The official guide and example description | Reproduction of the reported result |
| `doc-excerpt-reviewed` | Official title, introduction, and index; incomplete body retrieval | Complete review of the guide |
| `article-reviewed` | A first-party author or development-team report | Independent measurement |
| `discovery-only` | A specific original link located through search or a directory | Review of the original post or full video |

Every current resource has `reproduction: not-run`. To upgrade this status, record the version or commit, environment, method, input, observed output, and failures, and update the schema checks and all language renderers. Reading a README is not successful reproduction.

`checked_at` is our source-review date, not a release or translation date. `evidence_sha256` fingerprints the source bytes received; it is not a Git commit or proof of reproduction. For partial downloads, it covers only the received portion.

## Editorial rules

1. Credit the author, retain the original URL, and write an independent concise summary.
2. Keep one entry per project. Attach tweets, videos, and hosted demos as related links.
3. Do not infer actual Jev use from a repository name or another directory's description alone.
4. Confidence is not a correctness guarantee; a constrained output type can still contain a wrong decision.
5. Mark reported costs, latency, accuracy, and wins as author claims unless independently reproduced.
6. Preserve useful failures and disclosures about other models, simulators, or heuristic fallbacks.
7. Keep inaccessible original social posts and videos in the discovery queue; do not expand secondary titles into technical conclusions.
8. Distinguish timeouts, login walls, blocking, migration, and deletion.

## Languages and maintenance

English is the canonical edition. Simplified Chinese, Japanese, and Spanish contain the same resource IDs, URLs, review metadata, and limitations. Only display text is translated; no translation changes a resource's evidence level.

The generator uses `data/resources.json`, `data/candidates.json`, and `data/locales/*.json`. Checks require complete resource translations and resolve local links and stable anchors. They do not evaluate translation quality or remote availability. The workflow runs on push and pull requests; it does not schedule scraping or make model calls.

We link to original material rather than copying full documents, videos, screenshots, or external code. Original annotations and scripts use MIT; external resources retain their licenses.
