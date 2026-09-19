#!/usr/bin/env python3
"""Build and check complete English, Chinese, Japanese and Spanish catalogs."""
import argparse
from collections import Counter
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

from locales import UI, LANGUAGES

ROOT = Path(__file__).resolve().parents[1]
STATUSES = ['readme-reviewed', 'doc-reviewed', 'doc-excerpt-reviewed', 'article-reviewed']
FEATURED = ['official-quickstart', 'browser-use--jev-ultrafast', 'devagrawal09--jev-review',
            'monteduro--killmyidea', 'jexp--neo4jev', 'firassx914--janus', 'denikuchero--jev-chess-lab']
TEXT_FIELDS = ('title', 'summary', 'limitations')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def url_ok(url):
    p = urlparse(url)
    return p.scheme == 'https' and bool(p.netloc) and not any(c.isspace() for c in url)


def read_json(path):
    def unique_pairs(pairs):
        result = {}
        for k, v in pairs:
            require(k not in result, f'Duplicate JSON key: {k} in {path}')
            result[k] = v
        return result
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_pairs)


def load():
    records = read_json(ROOT / 'data/resources.json')
    candidates = read_json(ROOT / 'data/candidates.json')
    seen_ids, seen_urls = set(), set()
    for r in records + candidates:
        require(bool(re.fullmatch(r'[a-zA-Z0-9_-]+', r['id'])), f"Invalid id: {r['id']}")
        require(r['id'] not in seen_ids, f"Duplicate id: {r['id']}")
        require(r['url'].rstrip('/') not in seen_urls, f"Duplicate URL: {r['url']}")
        seen_ids.add(r['id']); seen_urls.add(r['url'].rstrip('/'))
        require(url_ok(r['url']), f"Invalid URL: {r['url']}")
        date.fromisoformat(r['checked_at'])
        require(bool(r['title'].strip()), f"Missing title: {r['id']}")
        require(r['discovered_via'] == 'web-search' or url_ok(r['discovered_via']), 'Invalid discovery URL')
    for r in records:
        for key in (*TEXT_FIELDS, 'author', 'language', 'evidence_url'):
            require(isinstance(r[key], str) and bool(r[key].strip()), f"Missing {key}: {r['id']}")
        require(r['category'] in UI['en']['categories'], f"Unknown category: {r['category']}")
        require(r['kind'] in {'project', 'sdk', 'guide', 'article'}, 'Invalid kind')
        require(r['verification'] in STATUSES, 'Invalid review status')
        require(r['reproduction'] == 'not-run', 'Add reproducibility evidence and renderer before changing this status')
        require(url_ok(r['evidence_url']), 'Invalid evidence URL')
        if 'evidence_sha256' in r:
            require(bool(re.fullmatch('[0-9a-f]{64}', r['evidence_sha256'])), 'Invalid source hash')
        for link in r['related']:
            require(bool(link['label']) and url_ok(link['url']), 'Invalid related link')
    for r in candidates:
        require(r['verification'] == 'discovery-only', 'Candidate cannot claim review')
        require(r['platform'] in {'x', 'youtube'} and bool(r['note'].strip()), 'Invalid candidate')
    editions = {'en': records}
    ids = {r['id'] for r in records}
    for lang in LANGUAGES:
        if lang == 'en':
            continue
        translated = read_json(ROOT / f'data/locales/{lang}.json')
        require(set(translated) == ids, f'{lang}: missing or unknown translation IDs: {set(translated) ^ ids}')
        for rid, entry in translated.items():
            for key in TEXT_FIELDS:
                require(isinstance(entry.get(key), str) and bool(entry[key].strip()), f'{lang}/{rid}: missing {key}')
        editions[lang] = [{**r, **{k: translated[r['id']][k] for k in TEXT_FIELDS}} for r in records]
    return records, candidates, editions


def filename(stem, lang):
    return f'{stem}{"" if lang == "en" else "." + lang}.md'


def language_nav(stem, current, prefix=''):
    return ' · '.join(f'**{name}**' if lang == current else f'[{name}]({prefix}{filename(stem, lang)})'
                      for lang, name in LANGUAGES.items())


def cell(s):
    return s.replace('|', '\\|').replace('\n', ' ')


def output_edition(records, candidates, lang):
    t = UI[lang]
    counts = Counter(r['kind'] for r in records)
    index = filename('README', lang)
    details_name = filename('catalog/DETAILS', lang)
    media_name = filename('catalog/MEDIA', lang)
    start_name = filename('docs/START-HERE', lang)
    stats = t['counts'].format(total=len(records), projects=counts['project']+counts['sdk'],
                               guides=counts['guide'], articles=counts['article'], candidates=len(candidates))
    nav = ' · '.join(f'[{label}]({path})' for label, path in zip(t['nav'], [start_name, details_name, media_name, 'CONTRIBUTING.md']))
    text = f"# Awesome Jev Examples\n\n{language_nav('README', lang)}\n\n> {t['tagline']}\n\n{t['intro']}\n\n{nav}\n\n{stats}\n\n{t['notice']}\n\n## {t['featured']}\n\n"
    lookup = {r['id']: r for r in records}
    for rid in FEATURED:
        r = lookup[rid]
        text += f"- **[{r['title']}]({r['url']})** — {r['summary']} [{t['details']}]({details_name}#{rid})\n"
    text += f"\n## {t['browse']}\n\n"
    for cat, title in t['categories'].items():
        n = sum(r['category'] == cat for r in records)
        text += f'- [{title}](#{cat}) ({n})\n'
    detail = f"# {t['cardtitle']}\n\n{language_nav('DETAILS', lang)}\n\n[{t['back']}](../{index})\n\n{t['cardintro']}\n\n"
    for cat, title in t['categories'].items():
        text += f'\n<a id="{cat}"></a>\n\n## {title}\n\n| {t["resource"]} | {t["description"]} |\n| --- | --- |\n'
        detail += f'## {title}\n\n'
        for r in [r for r in records if r['category'] == cat]:
            text += f"| [{cell(r['title'])}]({r['url']}) | {cell(r['summary'])} [{t['details']}]({details_name}#{r['id']}) |\n"
            detail += f'''<a id="{r['id']}"></a>

### {r['title']}

{r['summary']}

- **{t['source']}:** [{r['title']}]({r['url']})
- **{t['author']}:** {r['author']} ({r['language']})
- **{t['limits']}:** {r['limitations']}
- **{t['review']}:** {t['statuses'][STATUSES.index(r['verification'])]}. [{t['evidence']}]({r['evidence_url']}) · {r['checked_at']} · {t['notrun']}.
'''
            for link in r['related']:
                # This collection has one author video link; label remains explicit about its status.
                detail += f"- **{t['related']}:** [X]({link['url']}) — {t['pending']}\n"
            detail += '\n'
    text += f'''\n## {t['maintain']}

{t['maintenance']}

```sh
python3 scripts/catalog.py
python3 scripts/catalog.py --check
python3 scripts/catalog.py --search browser --lang en
```

{t['checknote']}

{t['policy']}
'''
    media = f"# {t['mediatitle']}\n\n{language_nav('MEDIA', lang)}\n\n[{t['back']}](../{index})\n\n{t['mediaintro']}\n\n"
    for platform, name in [('youtube', 'YouTube'), ('x', 'X / Twitter')]:
        media += f"## {name}\n\n| {t['lead']} | {t['discovery']} | {t['state']} |\n| --- | --- | --- |\n"
        for r in candidates:
            if r['platform'] == platform:
                status = t['partialmedia'] if r['id'] == 'x-2100715237267660873' else t['pending']
                media += f"| [{cell(r['title'])}]({r['url']}) | [{t['source']}]({r['discovered_via']}) | {status} |\n"
        media += '\n'
    start = f"# {t['tutorial']}\n\n{language_nav('START-HERE', lang)}\n\n[{t['back']}](../{index})\n\n"
    start += '\n'.join(f'{i}. {step}' for i, step in enumerate(t['steps'], 1))
    start += f"\n\n## {t['reading']}\n\n"
    for rid in FEATURED:
        r = lookup[rid]
        start += f"- [{r['title']}]({r['url']}) — {r['summary']}\n"
    start += f"\n{t['readingnote']}\n"
    return {index: text, details_name: detail, media_name: media, start_name: start}


def outputs(candidates, editions):
    result = {}
    for lang, records in editions.items():
        result.update(output_edition(records, candidates, lang))
    # Preserve the previous English URL, generated from the same source as README.md.
    result['README.en.md'] = result['README.md']
    return result


def check_local_links():
    cache = {}
    for path in ROOT.rglob('*.md'):
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if re.match(r'[a-zA-Z]+:', target):
                continue
            filepart, _, anchor = target.partition('#')
            dest = (path.parent / filepart).resolve() if filepart else path.resolve()
            require(dest.is_relative_to(ROOT), f'Link outside repository: {target}')
            require(dest.is_file(), f'{path.relative_to(ROOT)}: missing {target}')
            if anchor:
                body = cache.setdefault(dest, dest.read_text(encoding='utf-8'))
                # Generated links use explicit stable anchors, independent of translated headings.
                require(f'id="{anchor}"' in body, f'{path.relative_to(ROOT)}: missing anchor {target}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--search', metavar='QUERY')
    parser.add_argument('--lang', choices=LANGUAGES, default='en')
    args = parser.parse_args()
    records, candidates, editions = load()
    if args.search:
        query = args.search.casefold()
        for r in editions[args.lang]:
            content = json.dumps(r, ensure_ascii=False) + UI[args.lang]['categories'][r['category']]
            if query in content.casefold():
                print(f"{r['title']} — {r['summary']}\n{r['url']}\n")
        return
    generated = outputs(candidates, editions)
    for name, body in generated.items():
        path = ROOT / name
        if args.check:
            require(path.exists() and path.read_text(encoding='utf-8') == body, f'Stale generated file: {name}')
        else:
            path.write_text(body, encoding='utf-8')
    check_local_links()
    print(f'OK: {len(records)} resources × {len(editions)} languages, {len(candidates)} candidates, {len(generated)} generated files; data and local links checked')


if __name__ == '__main__':
    try:
        main()
    except (KeyError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        sys.exit(1)
