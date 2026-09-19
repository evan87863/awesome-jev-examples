# Contributing

[English](CONTRIBUTING.md) · [简体中文](CONTRIBUTING.zh-CN.md)

Suggest projects that use **TypeSafe Jev**, practical tutorials, author demonstrations, or evaluations. Search existing entries first: one project gets one entry, with additional channels attached as related links.

## Suggest a resource

Use the resource issue form. Include the original URL, author, what Jev actually decides, source code or a demonstration, limitations, and your review method. You do not need to make paid API calls. Unreviewed leads are welcome when clearly labeled.

## Update the catalog

1. Edit the English source data in `data/resources.json`. Unreviewed X / YouTube links belong in `data/candidates.json`.
2. Use a stable ID containing letters, digits, hyphens, or underscores. For GitHub projects, prefer `owner--repo`.
3. Required resource fields: `id`, `title`, `category`, `kind`, `author`, `url`, `language`, `summary`, `limitations`, `verification`, `reproduction`, `checked_at`, `evidence_url`, `discovered_via`, and `related`. An optional `evidence_sha256` must describe the bytes actually retrieved.
4. Add or update the same ID in **all three** files: `data/locales/zh-CN.json`, `data/locales/ja.json`, and `data/locales/es.json`. Translate `title`, `summary`, and `limitations`. Keep project names recognizable. Preserve uncertainties, fallback models, partial-source warnings, and reproduction status.
5. Run `python3 scripts/catalog.py` to generate every edition, then `python3 scripts/catalog.py --check`.
6. Explain the source, review method, and remaining limitations in the PR.

Do not directly edit generated `README*.md`, `catalog/*.md`, or `docs/START-HERE*.md` files. `README.md` is the default English edition; `README.en.md` is a generated compatibility copy. Each localized index points to its own localized details and discovery queue. Review dates describe source checks, not translation dates. Original source titles in the media queue remain untranslated.

The UI labels and category names live in `scripts/locales.py`. The validator requires every resource ID in every maintained locale, and checks that generated files and local anchors agree. It cannot judge translation accuracy or detect a semantically stale translation, so review the three translations whenever the English text changes.

## Evidence and scope

- `kind`: `project`, `sdk`, `guide`, or `article`.
- Review statuses: see [methodology](docs/METHODOLOGY.md).
- `reproduction` currently accepts only `not-run`. To claim reproduction, first add evidence fields and update the validator and all renderers.
- Avoid unrelated projects called Jev and do not present a Jev-inspired model as a user of the official model.
- Do not claim zero errors, absolute security, or independently measured performance without evidence.
- Do not submit keys, private data, copied full transcripts, or unlicensed media.
- Original summaries and scripts use this repository's MIT license; linked materials keep their original licenses.

## Local checks

Python 3.10+, standard library only:

```sh
python3 scripts/catalog.py
python3 scripts/catalog.py --check
python3 scripts/catalog.py --search browser --lang en
python3 scripts/catalog.py --search ブラウザ --lang ja
python3 scripts/catalog.py --search navegador --lang es
python3 scripts/catalog.py --search 浏览器 --lang zh-CN
```

Checks are offline. They do not verify remote availability, install external projects, or call models. Before adding a reviewed resource, open the original source separately.
