# はじめに

[English](START-HERE.md) · [简体中文](START-HERE.zh-CN.md) · **日本語** · [Español](START-HERE.es.md)

[索引に戻る](../README.ja.md)

1. 公式クイックスタートで `state` と `questions` を理解します。
2. 目的に近い事例を選び、Jev への入力と判断対象を確認します。
3. 代替処理、不確実性、他モデルの関与、独立した結果確認を調べます。
4. 自動実行を始める前に、自分の課題のラベル付きサンプルで評価します。

## おすすめの資料

- [クイックスタート](https://docs.typesafe.ai/introduction/quickstart) — Playground や SDK で、最初の型付きリクエストを作ります。
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) — 動的なページ要素一覧から、操作と対象要素をまとめて選びます。
- [Jev Review (devagrawal09)](https://github.com/devagrawal09/jev-review) — 差分やリポジトリを、リスク判定、根拠選択、重大度評価の段階に分けてレビューします。
- [Kill My Idea](https://github.com/monteduro/killmyidea) — 起業アイデアに複数の質問を並列で行い、スコアを組み合わせて定型の判定を出します。
- [neo4jev](https://github.com/jexp/neo4jev) — 同じ呼び出しで、グラフの次の関係を選び、目標に到達したかも判定します。
- [Janus](https://github.com/FirasSX914/Janus) — 小型・大型モデルの振り分け条件を測定し、振り分けを採用しない選択もできます。
- [Jev Chess Lab](https://github.com/denikuchero/jev-chess-lab) — Jev 単独、戦術フィルター、Stockfish 支援を分けて記録したチェス実験です。

多くの事例に共通する構造は、コードが候補を作り、Jev が選択・評価し、コードが結果を確認するというものです。自由文や複雑な推論には別のモデルを使う場合があります。
