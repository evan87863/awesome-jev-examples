# Awesome Jev Examples

[English](README.md) · [简体中文](README.zh-CN.md) · **日本語** · [Español](README.es.md)

> Jev の活用例を見つけ、仕組みを理解し、元の資料へ進む。

**[TypeSafe AI の Jev](https://docs.typesafe.ai/introduction)** を使った事例の厳選リストです。Jev は与えられた状態について Choice、Score、Noul 形式の質問に答える判断モデルです。TypeSafe AI とは独立したコミュニティプロジェクトです。

[はじめに](docs/START-HERE.ja.md) · [すべての詳細](catalog/DETAILS.ja.md) · [X / YouTube](catalog/MEDIA.ja.md) · [貢献ガイド（英語）](CONTRIBUTING.md)

**72 件のリソース：**ソースコードのあるプロジェクト・SDK が 46 件、公式ガイド・パターン・参考資料が 25 件、開発チームによる実測記事が 1 件。別に **X / YouTube の未確認リンク 28 件**を掲載。初回確認日：2026-09-19。

確認済みとは、記載の資料を読んだという意味です。実行、監査、効果の保証ではありません。本リポジトリで追試した事例はありません。公式ページ二件は本文を一部しか取得できず、その旨を明記しています。作者の性能報告は独立に検証していません。

## まず見たい事例

- **[クイックスタート](https://docs.typesafe.ai/introduction/quickstart)** — Playground や SDK で、最初の型付きリクエストを作ります。 [詳細を見る](catalog/DETAILS.ja.md#official-quickstart)
- **[Jev Ultrafast](https://github.com/browser-use/jev-ultrafast)** — 動的なページ要素一覧から、操作と対象要素をまとめて選びます。 [詳細を見る](catalog/DETAILS.ja.md#browser-use--jev-ultrafast)
- **[Jev Review (devagrawal09)](https://github.com/devagrawal09/jev-review)** — 差分やリポジトリを、リスク判定、根拠選択、重大度評価の段階に分けてレビューします。 [詳細を見る](catalog/DETAILS.ja.md#devagrawal09--jev-review)
- **[Kill My Idea](https://github.com/monteduro/killmyidea)** — 起業アイデアに複数の質問を並列で行い、スコアを組み合わせて定型の判定を出します。 [詳細を見る](catalog/DETAILS.ja.md#monteduro--killmyidea)
- **[neo4jev](https://github.com/jexp/neo4jev)** — 同じ呼び出しで、グラフの次の関係を選び、目標に到達したかも判定します。 [詳細を見る](catalog/DETAILS.ja.md#jexp--neo4jev)
- **[Janus](https://github.com/FirasSX914/Janus)** — 小型・大型モデルの振り分け条件を測定し、振り分けを採用しない選択もできます。 [詳細を見る](catalog/DETAILS.ja.md#firassx914--janus)
- **[Jev Chess Lab](https://github.com/denikuchero/jev-chess-lab)** — Jev 単独、戦術フィルター、Stockfish 支援を分けて記録したチェス実験です。 [詳細を見る](catalog/DETAILS.ja.md#denikuchero--jev-chess-lab)

## 用途別に探す

- [公式ガイドと SDK](#official) (26)
- [ブラウザ・デスクトップ・モバイル](#browser) (8)
- [コーディングエージェントと MCP](#agents) (8)
- [モデルの振り分け](#routing) (2)
- [モデレーション・ルール・安全性チェック](#safety) (5)
- [検索と知識グラフ](#retrieval) (1)
- [データ処理と可観測性](#data) (4)
- [日常の自動化とスマートホーム](#automation) (2)
- [アプリとコンテンツツール](#applications) (4)
- [ゲームとシミュレーション](#games) (6)
- [評価と校正](#evaluation) (5)
- [限界を探る実験](#experiments) (1)

<a id="official"></a>

## 公式ガイドと SDK

| リソース | 概要と詳細 |
| --- | --- |
| [公式 Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) | 公式 Python クライアント。問い合わせ分類の最小例から始められます。 [詳細を見る](catalog/DETAILS.ja.md#typesafe-ai--typesafe-sdk-python) |
| [クイックスタート](https://docs.typesafe.ai/introduction/quickstart) | Playground や SDK で、最初の型付きリクエストを作ります。 [詳細を見る](catalog/DETAILS.ja.md#official-quickstart) |
| [分岐候補の並列評価](https://docs.typesafe.ai/patterns/fan-out) | 考えられる分岐をまとめて質問し、必要な回答をコードで選びます。 [詳細を見る](catalog/DETAILS.ja.md#official-fan-out) |
| [信頼度に応じた振り分け](https://docs.typesafe.ai/patterns/confidence-routing) | 回答と実行判断を分け、自分のデータで確認を求める閾値を測ります。 [詳細を見る](catalog/DETAILS.ja.md#official-confidence-routing) |
| [スコアの組み合わせ](https://docs.typesafe.ai/patterns/composite-scoring) | 複数の観点を別々に評価し、コードで明示した重みを使って組み合わせます。 [詳細を見る](catalog/DETAILS.ja.md#official-composite-scoring) |
| [意図の振り分け](https://docs.typesafe.ai/patterns/intent-routing) | 入力を分類し、ルール、専門モデル、人の担当へ振り分けます。 [詳細を見る](catalog/DETAILS.ja.md#official-intent-routing) |
| [スマートホーム助手](https://docs.typesafe.ai/demos/smart-home) | 家庭の操作依頼を、一回の呼び出しにまとめた複数の質問で評価します。 [詳細を見る](catalog/DETAILS.ja.md#official-smart-home) |
| [Jev 1.13 の既知の限界](https://docs.typesafe.ai/model-jaggedness/jev-1.13) | このモデルバージョンについて公開された弱点と失敗例を確認できます。 [詳細を見る](catalog/DETAILS.ja.md#official-jev-1-13) |
| [Noul の一貫性](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook) | 保険請求の判断を繰り返し、不確実性と安定性を確認します。一貫性は正しさとは別です。 [詳細を見る](catalog/DETAILS.ja.md#official-consistency-noul-cookbook) |
| [Choice の一貫性](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook) | モデレーションに保留の選択肢を加え、一致率と自動処理率を比較します。 [詳細を見る](catalog/DETAILS.ja.md#official-consistency-choice-cookbook) |
| [質問の一括処理](https://docs.typesafe.ai/cookbooks/parallel_questions) | 一つの文書への複数の質問を、まとめて送る場合と分ける場合で比較します。 [詳細を見る](catalog/DETAILS.ja.md#official-parallel-questions) |
| [検索結果の再ランキング](https://docs.typesafe.ai/cookbooks/rerank_typesafe) | BM25 で候補を絞り、質問と段落の関連を評価します。例は法律文書の検索です。 [詳細を見る](catalog/DETAILS.ja.md#official-rerank-typesafe) |
| [行単位の意味検索](https://docs.typesafe.ai/cookbooks/semantic_find) | 関連する行番号を選び、答えが文書に存在するかも別に確認します。 [詳細を見る](catalog/DETAILS.ja.md#official-semantic-find) |
| [文書構造の復元](https://docs.typesafe.ai/cookbooks/autoformat) | 改行、見出し、リスト、コードブロックを分類し、コードで Markdown を再構成します。 [詳細を見る](catalog/DETAILS.ja.md#official-autoformat) |
| [選択肢を限定した関数呼び出し](https://docs.typesafe.ai/cookbooks/function_calling) | 関数名と有限の引数候補を、型付きの判断に変換します。 [詳細を見る](catalog/DETAILS.ja.md#official-function-calling) |
| [エージェントのスキル選択](https://docs.typesafe.ai/cookbooks/skill_suggestion) | スキル候補を順位付けして少数の詳細を読み、すべて不適合と判断することもできます。 [詳細を見る](catalog/DETAILS.ja.md#official-skill-suggestion) |
| [知識グラフのエンティティ照合](https://docs.typesafe.ai/cookbooks/entity_alignment) | 候補同士を統合するか、別々に残すか、人が確認するかを判断します。 [詳細を見る](catalog/DETAILS.ja.md#official-entity-alignment) |
| [RAG 段落の分類](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) | 検索から文章生成までの間に、関連性、矛盾、埋め込まれた指示を確認します。 [詳細を見る](catalog/DETAILS.ja.md#official-classifying-rag-passages) |
| [引用の確認](https://docs.typesafe.ai/cookbooks/citation_check) | 引用文が実在するかを確認してから、文脈が主張を裏付けているかを判断します。 [詳細を見る](catalog/DETAILS.ja.md#official-citation-check) |
| [LLM の入力・出力チェック](https://docs.typesafe.ai/cookbooks/llm_guardrails) | リスクの質問と重大度スコアで、通過、確認、ブロックを選びます。 [詳細を見る](catalog/DETAILS.ja.md#official-llm-guardrails) |
| [構造化抽出の段階処理](https://docs.typesafe.ai/cookbooks/sde_cascade) | 小型モデルで抽出し、Jev で各項目を検証して、必要な場合に上位モデルへ回します。 [詳細を見る](catalog/DETAILS.ja.md#official-sde-cascade) |
| [日付の抽出](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook) | 文中の日付の各要素を選び、暦の計算と検証はコードが担当します。 [詳細を見る](catalog/DETAILS.ja.md#official-date-extraction-cookbook) |
| [事前抽出した値の選択](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) | 正規表現で候補を見つけ、Jev で選び、元の文字列をコピーします。 [詳細を見る](catalog/DETAILS.ja.md#official-pre-parsed-value-extraction-cookbook) |
| [階層分類](https://docs.typesafe.ai/cookbooks/hierarchical_classification) | 確率を使ってラベルの木を探索し、分岐と最終ラベル両方の誤りを追跡します。 [詳細を見る](catalog/DETAILS.ja.md#official-hierarchical-classification) |
| [特徴量の自動発見](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery) | LLM が質問を提案し、Jev が数値化し、CatBoost の誤りを次の改善に使います。 [詳細を見る](catalog/DETAILS.ja.md#official-autoresearch-feature-discovery) |
| [粗いラベルへの切り替え付き分類](https://docs.typesafe.ai/cookbooks/classification_using_confidence) | 年次報告書を業種分類し、信頼度が低い場合はより広い分類に戻します。 [詳細を見る](catalog/DETAILS.ja.md#official-classification-using-confidence) |

<a id="browser"></a>

## ブラウザ・デスクトップ・モバイル

| リソース | 概要と詳細 |
| --- | --- |
| [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) | 動的なページ要素一覧から、操作と対象要素をまとめて選びます。 [詳細を見る](catalog/DETAILS.ja.md#browser-use--jev-ultrafast) |
| [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) | OCR とアクセシビリティ API で Mac の画面を読み、Jev が次の操作を選びます。 [詳細を見る](catalog/DETAILS.ja.md#awlevin--typesafe-computer-use) |
| [Jev Browser](https://github.com/jkudish/jev-browser) | ライブラリ、CLI、MCP からブラウザを操作し、予算、復旧、判断履歴を管理します。 [詳細を見る](catalog/DETAILS.ja.md#jkudish--jev-browser) |
| [Mobile Jev](https://github.com/droidrun/mobile-jev) | Mobilerun の Android 端末で、現在の画面状態から操作を選択します。 [詳細を見る](catalog/DETAILS.ja.md#droidrun--mobile-jev) |
| [Unclutter](https://github.com/kitze/unclutter) | Jev でページの不要な要素を判定し、テンプレートのルールとして再利用する拡張です。 [詳細を見る](catalog/DETAILS.ja.md#kitze--unclutter) |
| [TypeSafe Fun AdBlocker](https://github.com/realZachi/typesafe-adblock) | DOM 要素が広告かどうかを判定し、ブラウザ側のコードで取り除きます。 [詳細を見る](catalog/DETAILS.ja.md#realzachi--typesafe-adblock) |
| [Jev for Social Media](https://github.com/socai-io/jev-social) | Jev が SNS の操作を選び、socai がブラウザで実行します。 [詳細を見る](catalog/DETAILS.ja.md#socai-io--jev-social) |
| [Retriever AI：ブラウザエージェントの実測](https://rtrvr.ai/blog/jev-browser-agent-benchmark) | GLM の計画と Jev の操作選択を組み合わせ、速度改善と総費用増加を報告した開発者記事です。 [詳細を見る](catalog/DETAILS.ja.md#rtrvr-browser-benchmark) |

<a id="agents"></a>

## コーディングエージェントと MCP

| リソース | 概要と詳細 |
| --- | --- |
| [Typesafe MCP](https://github.com/itsmostafa/typesafe-mcp) | MCP サーバーを通じて、型付きの判断をコーディング支援ツールに提供します。 [詳細を見る](catalog/DETAILS.ja.md#itsmostafa--typesafe-mcp) |
| [Jev MCP (jkudish)](https://github.com/jkudish/jev-mcp) | 検証、フィルタリング、再ランキング、分類、コードレビューを行う MCP ツール群です。 [詳細を見る](catalog/DETAILS.ja.md#jkudish--jev-mcp) |
| [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | ツール呼び出しと結果を評価し、古い内容を削減して、残す部分は原文のまま保持します。 [詳細を見る](catalog/DETAILS.ja.md#tamaratran--fast-jev-compaction) |
| [Foreman](https://github.com/thruwire/foreman) | 実装が完了したか、テストが十分か、人の入力が必要かを判断します。 [詳細を見る](catalog/DETAILS.ja.md#thruwire--foreman) |
| [Winnow](https://github.com/GhalebDweikat/winnow) | 大きなツール出力をコンテキスト投入前に絞り込み、隠した原文を復元できるようにします。 [詳細を見る](catalog/DETAILS.ja.md#ghalebdweikat--winnow) |
| [Jev Review (devagrawal09)](https://github.com/devagrawal09/jev-review) | 差分やリポジトリを、リスク判定、根拠選択、重大度評価の段階に分けてレビューします。 [詳細を見る](catalog/DETAILS.ja.md#devagrawal09--jev-review) |
| [Jev Review MCP](https://github.com/NiazMorshed2007/jev-review) | ローカル MCP サーバーが、作業中のコーディングエージェントに品質スコアを返します。 [詳細を見る](catalog/DETAILS.ja.md#niazmorshed2007--jev-review) |
| [Jev MCP (blakestone-x)](https://github.com/blakestone-x/jev-mcp) | 分類、評価、照合、フィルタリング向けの MCP ツールとリクエスト例です。 [詳細を見る](catalog/DETAILS.ja.md#blakestone-x--jev-mcp) |

<a id="routing"></a>

## モデルの振り分け

| リソース | 概要と詳細 |
| --- | --- |
| [Jev Codex Router](https://github.com/0xNatoshi/jev-codex-router) | 会話の各ターンで、Jev がモデルと推論の深さを選びます。 [詳細を見る](catalog/DETAILS.ja.md#0xnatoshi--jev-codex-router) |
| [jev-router](https://github.com/gargpratyush/jev-router) | Claude Code や Codex の新しいターンを、適切なモデル階層に振り分けます。 [詳細を見る](catalog/DETAILS.ja.md#gargpratyush--jev-router) |

<a id="safety"></a>

## モデレーション・ルール・安全性チェック

| リソース | 概要と詳細 |
| --- | --- |
| [Tripwire](https://github.com/noelzappy/tripwire) | 応答がユーザーに届く前に、ミドルウェアやプロキシで内容を検査します。 [詳細を見る](catalog/DETAILS.ja.md#noelzappy--tripwire) |
| [jev-gates](https://github.com/rashedInt32/jev-gates) | コーディング中のルール、作業範囲、完了宣言を確認し、必要なときに確認を求めます。 [詳細を見る](catalog/DETAILS.ja.md#rashedint32--jev-gates) |
| [pi-warden](https://github.com/DevMortimer/pi-warden) | 編集やツール利用を監視し、ルール違反、再試行ループ、完了根拠を確認します。 [詳細を見る](catalog/DETAILS.ja.md#devmortimer--pi-warden) |
| [Safer with Jev](https://github.com/andrelandgraf/safer-with-jev) | 内容の判定と、任意の HTTPS 転送を組み合わせた公開デモです。 [詳細を見る](catalog/DETAILS.ja.md#andrelandgraf--safer-with-jev) |
| [Triagedy](https://github.com/m0rphtail/triagedy) | JSONL 形式のセキュリティ通知を、Unix パイプラインで扱える判断結果に変換します。 [詳細を見る](catalog/DETAILS.ja.md#m0rphtail--triagedy) |

<a id="retrieval"></a>

## 検索と知識グラフ

| リソース | 概要と詳細 |
| --- | --- |
| [neo4jev](https://github.com/jexp/neo4jev) | 同じ呼び出しで、グラフの次の関係を選び、目標に到達したかも判定します。 [詳細を見る](catalog/DETAILS.ja.md#jexp--neo4jev) |

<a id="data"></a>

## データ処理と可観測性

| リソース | 概要と詳細 |
| --- | --- |
| [pg-jev](https://github.com/realZachi/pg-jev) | 自然言語の条件で行を絞り込み、順位付け、分類する PostgreSQL 拡張です。 [詳細を見る](catalog/DETAILS.ja.md#realzachi--pg-jev) |
| [jevQL](https://github.com/kylemclaren/jevql) | 通常の PostgreSQL クエリに、クライアント側で Jev の判断を追加します。 [詳細を見る](catalog/DETAILS.ja.md#kylemclaren--jevql) |
| [duckdb-jev](https://github.com/colliber/duckdb-jev) | DuckDB のクエリから、テーブルや Parquet データの型付き判断を返します。 [詳細を見る](catalog/DETAILS.ja.md#colliber--duckdb-jev) |
| [Jev Logs](https://github.com/reachjalil/jevlogs) | OpenTelemetry ログを評価し、必要なレコードを高コストの分析へ振り分けます。 [詳細を見る](catalog/DETAILS.ja.md#reachjalil--jevlogs) |

<a id="automation"></a>

## 日常の自動化とスマートホーム

| リソース | 概要と詳細 |
| --- | --- |
| [Jev for Home Assistant](https://github.com/AboveColin/HA-Jev) | 家庭の状態について質問し、Home Assistant の自動化に使える値を返します。 [詳細を見る](catalog/DETAILS.ja.md#abovecolin--ha-jev) |
| [jev-shell-history](https://github.com/mrnugget/jev-shell-history) | 入力中の内容に合わせて、既存の zsh コマンド履歴を順位付けします。 [詳細を見る](catalog/DETAILS.ja.md#mrnugget--jev-shell-history) |

<a id="applications"></a>

## アプリとコンテンツツール

| リソース | 概要と詳細 |
| --- | --- |
| [TypeSafe AI Playground (Rust CLI)](https://github.com/markjaquith/typesafe-ai-playground) | 機微情報検出、コメントレビュー、語調分析、業種分類を試す Rust CLI です。 [詳細を見る](catalog/DETAILS.ja.md#markjaquith--typesafe-ai-playground) |
| [Jev Moderation Bot](https://github.com/brainstormity/Jev-Moderation-Bot) | Discord のスパムや詐欺リンクを判定し、段階的なモデレーションを行います。 [詳細を見る](catalog/DETAILS.ja.md#brainstormity--jev-moderation-bot) |
| [JEVMETER](https://github.com/ChetasLua/jevmeter) | 動画の文字起こしを文ごとに評価し、結果をメーターとして映像に表示します。 [詳細を見る](catalog/DETAILS.ja.md#chetaslua--jevmeter) |
| [Kill My Idea](https://github.com/monteduro/killmyidea) | 起業アイデアに複数の質問を並列で行い、スコアを組み合わせて定型の判定を出します。 [詳細を見る](catalog/DETAILS.ja.md#monteduro--killmyidea) |

<a id="games"></a>

## ゲームとシミュレーション

| リソース | 概要と詳細 |
| --- | --- |
| [1v1 Jev](https://github.com/emrickgarrett/OneVOneJev) | ブラウザ上の対戦ゲームで、Jev がキャラクターの行動を選びます。 [詳細を見る](catalog/DETAILS.ja.md#emrickgarrett--onevonejev) |
| [TypeSafe Mario](https://github.com/fhshaik/typesafe-mario) | エミュレーターの RAM と計測値を状態に変換し、Jev が NES の操作を選びます。 [詳細を見る](catalog/DETAILS.ja.md#fhshaik--typesafe-mario) |
| [Jev Plays StarCraft](https://github.com/phyous/tsai-sc) | 構造化状態から StarCraft 体験版のミッションを操作し、行動確率を記録します。 [詳細を見る](catalog/DETAILS.ja.md#phyous--tsai-sc) |
| [Jev Pong](https://github.com/ably-labs/jev-pong) | モデルの判断ごとに Pong の球を一歩進め、応答待ち時間を可視化します。 [詳細を見る](catalog/DETAILS.ja.md#ably-labs--jev-pong) |
| [jev-drone](https://github.com/RomanSlack/jev-drone) | MuJoCo のドローン仮想環境で Jev が状況を判断し、高速制御はコードが担当します。 [詳細を見る](catalog/DETAILS.ja.md#romanslack--jev-drone) |
| [Jev Chess Lab](https://github.com/denikuchero/jev-chess-lab) | Jev 単独、戦術フィルター、Stockfish 支援を分けて記録したチェス実験です。 [詳細を見る](catalog/DETAILS.ja.md#denikuchero--jev-chess-lab) |

<a id="evaluation"></a>

## 評価と校正

| リソース | 概要と詳細 |
| --- | --- |
| [jevcal](https://github.com/abhixhek/jevcal) | 自分のデータで信頼度の閾値を選び、モデル更新による変化を検出します。 [詳細を見る](catalog/DETAILS.ja.md#abhixhek--jevcal) |
| [Janus](https://github.com/FirasSX914/Janus) | 小型・大型モデルの振り分け条件を測定し、振り分けを採用しない選択もできます。 [詳細を見る](catalog/DETAILS.ja.md#firassx914--janus) |
| [jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) | 確率の校正、自動処理率、遅延、リソース消費を評価します。 [詳細を見る](catalog/DETAILS.ja.md#abdelstark--jev-benchmarks) |
| [typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) | 同じアプリケーション課題で、LLM の構造化出力と Jev を比較します。 [詳細を見る](catalog/DETAILS.ja.md#iammrduncan--typesafe-ai-benchmark) |
| [jev-secret-detection](https://github.com/teyhouse/jev-secret-detection) | コード片に利用可能な秘密情報が含まれるか、Noul の質問で評価します。 [詳細を見る](catalog/DETAILS.ja.md#teyhouse--jev-secret-detection) |

<a id="experiments"></a>

## 限界を探る実験

| リソース | 概要と詳細 |
| --- | --- |
| [jev-llm](https://github.com/Code-Forge-AU/jev-llm) | 候補から次の単語を繰り返し選ぶことで、文章生成を構成する実験です。 [詳細を見る](catalog/DETAILS.ja.md#code-forge-au--jev-llm) |

## リストの更新

英語版を基準に管理します。`data/resources.json` と `data/locales/` の三つの翻訳を更新し、全言語をまとめて生成します。Python 3.10+ のみ必要で、追加パッケージや API キーは不要です。

```sh
python3 scripts/catalog.py
python3 scripts/catalog.py --check
python3 scripts/catalog.py --search browser --lang en
```

データ、翻訳の欠落、重複、生成ファイル、ローカルリンクを検査します。外部サイトの可用性確認やモデル呼び出しは行いません。

[確認方法](docs/METHODOLOGY.md)、[調査記録](docs/RESEARCH.md)、[貢献ガイド](CONTRIBUTING.md)は英語です。独自の説明とスクリプトは [MIT ライセンス](LICENSE)、リンク先の資料は元のライセンスに従います。
