# リソースの詳細

[English](DETAILS.md) · [简体中文](DETAILS.zh-CN.md) · **日本語** · [Español](DETAILS.es.md)

[索引に戻る](../README.ja.md)

原資料へのリンク、概要、制約をまとめています。本リポジトリでは実行による追試を行っていません。

## 公式ガイドと SDK

<a id="typesafe-ai--typesafe-sdk-python"></a>

### 公式 Python SDK

公式 Python クライアント。問い合わせ分類の最小例から始められます。

- **原資料:** [公式 Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python)
- **作者・組織:** typesafe-ai (en)
- **制約:** 単独のアプリではなく、API 接続用のリソースです。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/typesafe-ai/typesafe-sdk-python/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="official-quickstart"></a>

### クイックスタート

Playground や SDK で、最初の型付きリクエストを作ります。

- **原資料:** [クイックスタート](https://docs.typesafe.ai/introduction/quickstart)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/introduction/quickstart.md) · 2026-09-19 · 未追試.

<a id="official-fan-out"></a>

### 分岐候補の並列評価

考えられる分岐をまとめて質問し、必要な回答をコードで選びます。

- **原資料:** [分岐候補の並列評価](https://docs.typesafe.ai/patterns/fan-out)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/patterns/fan-out.md) · 2026-09-19 · 未追試.

<a id="official-confidence-routing"></a>

### 信頼度に応じた振り分け

回答と実行判断を分け、自分のデータで確認を求める閾値を測ります。

- **原資料:** [信頼度に応じた振り分け](https://docs.typesafe.ai/patterns/confidence-routing)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/patterns/confidence-routing.md) · 2026-09-19 · 未追試.

<a id="official-composite-scoring"></a>

### スコアの組み合わせ

複数の観点を別々に評価し、コードで明示した重みを使って組み合わせます。

- **原資料:** [スコアの組み合わせ](https://docs.typesafe.ai/patterns/composite-scoring)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/patterns/composite-scoring.md) · 2026-09-19 · 未追試.

<a id="official-intent-routing"></a>

### 意図の振り分け

入力を分類し、ルール、専門モデル、人の担当へ振り分けます。

- **原資料:** [意図の振り分け](https://docs.typesafe.ai/patterns/intent-routing)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。 本文の取得は不完全で、タイトル、導入文、公式目次のみ確認しました。
- **確認状況:** 公式のタイトル・導入文・目次を確認、本文は不完全. [確認した資料](https://docs.typesafe.ai/patterns/intent-routing.md) · 2026-09-19 · 未追試.

<a id="official-smart-home"></a>

### スマートホーム助手

家庭の操作依頼を、一回の呼び出しにまとめた複数の質問で評価します。

- **原資料:** [スマートホーム助手](https://docs.typesafe.ai/demos/smart-home)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/demos/smart-home.md) · 2026-09-19 · 未追試.

<a id="official-jev-1-13"></a>

### Jev 1.13 の既知の限界

このモデルバージョンについて公開された弱点と失敗例を確認できます。

- **原資料:** [Jev 1.13 の既知の限界](https://docs.typesafe.ai/model-jaggedness/jev-1.13)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。 特定バージョンの限界です。更新後は再評価が必要です。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md) · 2026-09-19 · 未追試.

<a id="official-consistency-noul-cookbook"></a>

### Noul の一貫性

保険請求の判断を繰り返し、不確実性と安定性を確認します。一貫性は正しさとは別です。

- **原資料:** [Noul の一貫性](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。 本文の取得は不完全で、タイトル、導入文、公式目次のみ確認しました。
- **確認状況:** 公式のタイトル・導入文・目次を確認、本文は不完全. [確認した資料](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook.md) · 2026-09-19 · 未追試.

<a id="official-consistency-choice-cookbook"></a>

### Choice の一貫性

モデレーションに保留の選択肢を加え、一致率と自動処理率を比較します。

- **原資料:** [Choice の一貫性](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook.md) · 2026-09-19 · 未追試.

<a id="official-parallel-questions"></a>

### 質問の一括処理

一つの文書への複数の質問を、まとめて送る場合と分ける場合で比較します。

- **原資料:** [質問の一括処理](https://docs.typesafe.ai/cookbooks/parallel_questions)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/parallel_questions.md) · 2026-09-19 · 未追試.

<a id="official-rerank-typesafe"></a>

### 検索結果の再ランキング

BM25 で候補を絞り、質問と段落の関連を評価します。例は法律文書の検索です。

- **原資料:** [検索結果の再ランキング](https://docs.typesafe.ai/cookbooks/rerank_typesafe)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。 法律文書での結果は、他のすべての文書での性能を保証しません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/rerank_typesafe.md) · 2026-09-19 · 未追試.

<a id="official-semantic-find"></a>

### 行単位の意味検索

関連する行番号を選び、答えが文書に存在するかも別に確認します。

- **原資料:** [行単位の意味検索](https://docs.typesafe.ai/cookbooks/semantic_find)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/semantic_find.md) · 2026-09-19 · 未追試.

<a id="official-autoformat"></a>

### 文書構造の復元

改行、見出し、リスト、コードブロックを分類し、コードで Markdown を再構成します。

- **原資料:** [文書構造の復元](https://docs.typesafe.ai/cookbooks/autoformat)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/autoformat.md) · 2026-09-19 · 未追試.

<a id="official-function-calling"></a>

### 選択肢を限定した関数呼び出し

関数名と有限の引数候補を、型付きの判断に変換します。

- **原資料:** [選択肢を限定した関数呼び出し](https://docs.typesafe.ai/cookbooks/function_calling)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/function_calling.md) · 2026-09-19 · 未追試.

<a id="official-skill-suggestion"></a>

### エージェントのスキル選択

スキル候補を順位付けして少数の詳細を読み、すべて不適合と判断することもできます。

- **原資料:** [エージェントのスキル選択](https://docs.typesafe.ai/cookbooks/skill_suggestion)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/skill_suggestion.md) · 2026-09-19 · 未追試.

<a id="official-entity-alignment"></a>

### 知識グラフのエンティティ照合

候補同士を統合するか、別々に残すか、人が確認するかを判断します。

- **原資料:** [知識グラフのエンティティ照合](https://docs.typesafe.ai/cookbooks/entity_alignment)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/entity_alignment.md) · 2026-09-19 · 未追試.

<a id="official-classifying-rag-passages"></a>

### RAG 段落の分類

検索から文章生成までの間に、関連性、矛盾、埋め込まれた指示を確認します。

- **原資料:** [RAG 段落の分類](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/classifying_rag_passages.md) · 2026-09-19 · 未追試.

<a id="official-citation-check"></a>

### 引用の確認

引用文が実在するかを確認してから、文脈が主張を裏付けているかを判断します。

- **原資料:** [引用の確認](https://docs.typesafe.ai/cookbooks/citation_check)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/citation_check.md) · 2026-09-19 · 未追試.

<a id="official-llm-guardrails"></a>

### LLM の入力・出力チェック

リスクの質問と重大度スコアで、通過、確認、ブロックを選びます。

- **原資料:** [LLM の入力・出力チェック](https://docs.typesafe.ai/cookbooks/llm_guardrails)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。 モデルによる検査は、回避不可能なセキュリティ境界ではありません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/llm_guardrails.md) · 2026-09-19 · 未追試.

<a id="official-sde-cascade"></a>

### 構造化抽出の段階処理

小型モデルで抽出し、Jev で各項目を検証して、必要な場合に上位モデルへ回します。

- **原資料:** [構造化抽出の段階処理](https://docs.typesafe.ai/cookbooks/sde_cascade)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/sde_cascade.md) · 2026-09-19 · 未追試.

<a id="official-date-extraction-cookbook"></a>

### 日付の抽出

文中の日付の各要素を選び、暦の計算と検証はコードが担当します。

- **原資料:** [日付の抽出](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook.md) · 2026-09-19 · 未追試.

<a id="official-pre-parsed-value-extraction-cookbook"></a>

### 事前抽出した値の選択

正規表現で候補を見つけ、Jev で選び、元の文字列をコピーします。

- **原資料:** [事前抽出した値の選択](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。 原文をコピーしても、候補を間違えて選ぶ可能性は残ります。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook.md) · 2026-09-19 · 未追試.

<a id="official-hierarchical-classification"></a>

### 階層分類

確率を使ってラベルの木を探索し、分岐と最終ラベル両方の誤りを追跡します。

- **原資料:** [階層分類](https://docs.typesafe.ai/cookbooks/hierarchical_classification)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/hierarchical_classification.md) · 2026-09-19 · 未追試.

<a id="official-autoresearch-feature-discovery"></a>

### 特徴量の自動発見

LLM が質問を提案し、Jev が数値化し、CatBoost の誤りを次の改善に使います。

- **原資料:** [特徴量の自動発見](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。 ラベル付きデータを使い、学習と評価を分けてください。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery.md) · 2026-09-19 · 未追試.

<a id="official-classification-using-confidence"></a>

### 粗いラベルへの切り替え付き分類

年次報告書を業種分類し、信頼度が低い場合はより広い分類に戻します。

- **原資料:** [粗いラベルへの切り替え付き分類](https://docs.typesafe.ai/cookbooks/classification_using_confidence)
- **作者・組織:** TypeSafe AI (en)
- **制約:** 公式の例または作者の報告です。本リポジトリでは API を使った追試はしていません。
- **確認状況:** 公式文書を確認. [確認した資料](https://docs.typesafe.ai/cookbooks/classification_using_confidence.md) · 2026-09-19 · 未追試.

## ブラウザ・デスクトップ・モバイル

<a id="browser-use--jev-ultrafast"></a>

### Jev Ultrafast

動的なページ要素一覧から、操作と対象要素をまとめて選びます。

- **原資料:** [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast)
- **作者・組織:** browser-use (en)
- **制約:** 自由文は小型 LLM が生成します。航空券デモは検索のみで予約はしません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/browser-use/jev-ultrafast/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="awlevin--typesafe-computer-use"></a>

### typesafe-computer-use

OCR とアクセシビリティ API で Mac の画面を読み、Jev が次の操作を選びます。

- **原資料:** [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
- **作者・組織:** awlevin (en)
- **制約:** システム権限が必要です。一部の自由文には別の生成モデルを使います。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/awlevin/typesafe-computer-use/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="jkudish--jev-browser"></a>

### Jev Browser

ライブラリ、CLI、MCP からブラウザを操作し、予算、復旧、判断履歴を管理します。

- **原資料:** [Jev Browser](https://github.com/jkudish/jev-browser)
- **作者・組織:** jkudish (en)
- **制約:** 実際のブラウザを操作します。本リポジトリでは説明資料のみ確認しました。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/jkudish/jev-browser/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="droidrun--mobile-jev"></a>

### Mobile Jev

Mobilerun の Android 端末で、現在の画面状態から操作を選択します。

- **原資料:** [Mobile Jev](https://github.com/droidrun/mobile-jev)
- **作者・組織:** droidrun (en)
- **制約:** Uber デモは支払い選択までです。予約完了は示されていません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/droidrun/mobile-jev/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="kitze--unclutter"></a>

### Unclutter

Jev でページの不要な要素を判定し、テンプレートのルールとして再利用する拡張です。

- **原資料:** [Unclutter](https://github.com/kitze/unclutter)
- **作者・組織:** kitze (en)
- **制約:** 必要な内容を隠す可能性があります。拡張は未インストールです。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/kitze/unclutter/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="realzachi--typesafe-adblock"></a>

### TypeSafe Fun AdBlocker

DOM 要素が広告かどうかを判定し、ブラウザ側のコードで取り除きます。

- **原資料:** [TypeSafe Fun AdBlocker](https://github.com/realZachi/typesafe-adblock)
- **作者・組織:** realZachi (en)
- **制約:** 作者は趣味のデモと明記しています。完全な広告・追跡対策ではありません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/realZachi/typesafe-adblock/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="socai-io--jev-social"></a>

### Jev for Social Media

Jev が SNS の操作を選び、socai がブラウザで実行します。

- **原資料:** [Jev for Social Media](https://github.com/socai-io/jev-social)
- **作者・組織:** socai-io (en)
- **制約:** 古い動画は初期の振り分け版です。現在の全ワークフローを示すものではありません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/socai-io/jev-social/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="rtrvr-browser-benchmark"></a>

### Retriever AI：ブラウザエージェントの実測

GLM の計画と Jev の操作選択を組み合わせ、速度改善と総費用増加を報告した開発者記事です。

- **原資料:** [Retriever AI：ブラウザエージェントの実測](https://rtrvr.ai/blog/jev-browser-agent-benchmark)
- **作者・組織:** Bhavani Kalisetty / Retriever AI (en)
- **制約:** 各課題・構成につき一回の実行で、ページや計画も異なります。独立した追試はしていません。
- **確認状況:** 作者の記事を確認. [確認した資料](https://rtrvr.ai/blog/jev-browser-agent-benchmark) · 2026-09-19 · 未追試.

## コーディングエージェントと MCP

<a id="itsmostafa--typesafe-mcp"></a>

### Typesafe MCP

MCP サーバーを通じて、型付きの判断をコーディング支援ツールに提供します。

- **原資料:** [Typesafe MCP](https://github.com/itsmostafa/typesafe-mcp)
- **作者・組織:** itsmostafa (en)
- **制約:** クライアント設定と API キーが必要です。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/itsmostafa/typesafe-mcp/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="jkudish--jev-mcp"></a>

### Jev MCP (jkudish)

検証、フィルタリング、再ランキング、分類、コードレビューを行う MCP ツール群です。

- **原資料:** [Jev MCP (jkudish)](https://github.com/jkudish/jev-mcp)
- **作者・組織:** jkudish (en)
- **制約:** ツール数やインターフェースはバージョンによって変わります。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/jkudish/jev-mcp/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="tamaratran--fast-jev-compaction"></a>

### fast-jev-compaction

ツール呼び出しと結果を評価し、古い内容を削減して、残す部分は原文のまま保持します。

- **原資料:** [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)
- **作者・組織:** tamaratran (en)
- **制約:** 削除した情報が後で必要になる可能性があります。後続タスクへの影響を評価してください。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/tamaratran/fast-jev-compaction/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="thruwire--foreman"></a>

### Foreman

実装が完了したか、テストが十分か、人の入力が必要かを判断します。

- **原資料:** [Foreman](https://github.com/thruwire/foreman)
- **作者・組織:** thruwire (en)
- **制約:** 完了の判断は、コードの正しさを独立に検証するものではありません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/thruwire/foreman/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="ghalebdweikat--winnow"></a>

### Winnow

大きなツール出力をコンテキスト投入前に絞り込み、隠した原文を復元できるようにします。

- **原資料:** [Winnow](https://github.com/GhalebDweikat/winnow)
- **作者・組織:** GhalebDweikat (en)
- **制約:** 関連性の判断は Jev、要約には別のモデルも使います。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/GhalebDweikat/winnow/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="devagrawal09--jev-review"></a>

### Jev Review (devagrawal09)

差分やリポジトリを、リスク判定、根拠選択、重大度評価の段階に分けてレビューします。

- **原資料:** [Jev Review (devagrawal09)](https://github.com/devagrawal09/jev-review)
- **作者・組織:** devagrawal09 (en)
- **制約:** 構造化された評価もテストの代わりにはなりません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/devagrawal09/jev-review/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="niazmorshed2007--jev-review"></a>

### Jev Review MCP

ローカル MCP サーバーが、作業中のコーディングエージェントに品質スコアを返します。

- **原資料:** [Jev Review MCP](https://github.com/NiazMorshed2007/jev-review)
- **作者・組織:** NiazMorshed2007 (en)
- **制約:** 修正はエージェントが担当します。スコアは正しさの証明ではありません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/NiazMorshed2007/jev-review/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="blakestone-x--jev-mcp"></a>

### Jev MCP (blakestone-x)

分類、評価、照合、フィルタリング向けの MCP ツールとリクエスト例です。

- **原資料:** [Jev MCP (blakestone-x)](https://github.com/blakestone-x/jev-mcp)
- **作者・組織:** blakestone-x (en)
- **制約:** 複数の入力を一つの状態に入れても、それぞれ個別に分類されるとは限りません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/blakestone-x/jev-mcp/HEAD/README.md) · 2026-09-19 · 未追試.

## モデルの振り分け

<a id="0xnatoshi--jev-codex-router"></a>

### Jev Codex Router

会話の各ターンで、Jev がモデルと推論の深さを選びます。

- **原資料:** [Jev Codex Router](https://github.com/0xNatoshi/jev-codex-router)
- **作者・組織:** 0xNatoshi (en)
- **制約:** 既存の Codex Router が必要です。作者のコスト削減結果は未追試です。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/0xNatoshi/jev-codex-router/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="gargpratyush--jev-router"></a>

### jev-router

Claude Code や Codex の新しいターンを、適切なモデル階層に振り分けます。

- **原資料:** [jev-router](https://github.com/gargpratyush/jev-router)
- **作者・組織:** gargpratyush (en)
- **制約:** 元の CLI とその認証環境が必要です。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/gargpratyush/jev-router/HEAD/README.md) · 2026-09-19 · 未追試.

## モデレーション・ルール・安全性チェック

<a id="noelzappy--tripwire"></a>

### Tripwire

応答がユーザーに届く前に、ミドルウェアやプロキシで内容を検査します。

- **原資料:** [Tripwire](https://github.com/noelzappy/tripwire)
- **作者・組織:** noelzappy (en)
- **制約:** 遅延の数値は未追試です。誤検出と見逃しを評価する必要があります。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/noelzappy/tripwire/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="rashedint32--jev-gates"></a>

### jev-gates

コーディング中のルール、作業範囲、完了宣言を確認し、必要なときに確認を求めます。

- **原資料:** [jev-gates](https://github.com/rashedInt32/jev-gates)
- **作者・組織:** rashedInt32 (en)
- **制約:** 承認は行わず、確認要求のみを出します。権限管理システムではありません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/rashedInt32/jev-gates/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="devmortimer--pi-warden"></a>

### pi-warden

編集やツール利用を監視し、ルール違反、再試行ループ、完了根拠を確認します。

- **原資料:** [pi-warden](https://github.com/DevMortimer/pi-warden)
- **作者・組織:** DevMortimer (en)
- **制約:** 特定エージェント向けの実装です。作者の測定値は一般的な性能を保証しません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/DevMortimer/pi-warden/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="andrelandgraf--safer-with-jev"></a>

### Safer with Jev

内容の判定と、任意の HTTPS 転送を組み合わせた公開デモです。

- **原資料:** [Safer with Jev](https://github.com/andrelandgraf/safer-with-jev)
- **作者・組織:** andrelandgraf (en)
- **制約:** サービスとソースは別々に更新されます。転送動作は未検証です。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/andrelandgraf/safer-with-jev/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="m0rphtail--triagedy"></a>

### Triagedy

JSONL 形式のセキュリティ通知を、Unix パイプラインで扱える判断結果に変換します。

- **原資料:** [Triagedy](https://github.com/m0rphtail/triagedy)
- **作者・組織:** m0rphtail (en)
- **制約:** 自分のラベル付きデータで振り分け性能を評価する必要があります。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/m0rphtail/triagedy/HEAD/README.md) · 2026-09-19 · 未追試.

## 検索と知識グラフ

<a id="jexp--neo4jev"></a>

### neo4jev

同じ呼び出しで、グラフの次の関係を選び、目標に到達したかも判定します。

- **原資料:** [neo4jev](https://github.com/jexp/neo4jev)
- **作者・組織:** jexp (en)
- **制約:** Neo4j が必要です。経路スコアは回答の正解率ではありません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/jexp/neo4jev/HEAD/README.md) · 2026-09-19 · 未追試.

## データ処理と可観測性

<a id="realzachi--pg-jev"></a>

### pg-jev

自然言語の条件で行を絞り込み、順位付け、分類する PostgreSQL 拡張です。

- **原資料:** [pg-jev](https://github.com/realZachi/pg-jev)
- **作者・組織:** realZachi (en)
- **制約:** 拡張と API 呼び出しが必要です。ローカル DB への導入は行っていません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/realZachi/pg-jev/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="kylemclaren--jevql"></a>

### jevQL

通常の PostgreSQL クエリに、クライアント側で Jev の判断を追加します。

- **原資料:** [jevQL](https://github.com/kylemclaren/jevql)
- **作者・組織:** kylemclaren (en)
- **制約:** DB は通常のクエリを実行し、意味の評価は外部で行います。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/kylemclaren/jevql/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="colliber--duckdb-jev"></a>

### duckdb-jev

DuckDB のクエリから、テーブルや Parquet データの型付き判断を返します。

- **原資料:** [duckdb-jev](https://github.com/colliber/duckdb-jev)
- **作者・組織:** colliber (en)
- **制約:** 拡張と認証情報が必要です。サンプルクエリは未実行です。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/colliber/duckdb-jev/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="reachjalil--jevlogs"></a>

### Jev Logs

OpenTelemetry ログを評価し、必要なレコードを高コストの分析へ振り分けます。

- **原資料:** [Jev Logs](https://github.com/reachjalil/jevlogs)
- **作者・組織:** reachjalil (en)
- **制約:** プレビュー版です。不確実な記録や API 障害時の記録も分析対象に残す設計です。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/reachjalil/jevlogs/HEAD/README.md) · 2026-09-19 · 未追試.

## 日常の自動化とスマートホーム

<a id="abovecolin--ha-jev"></a>

### Jev for Home Assistant

家庭の状態について質問し、Home Assistant の自動化に使える値を返します。

- **原資料:** [Jev for Home Assistant](https://github.com/AboveColin/HA-Jev)
- **作者・組織:** AboveColin (en)
- **制約:** Home Assistant が必要です。本リポジトリでは実機を試していません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/AboveColin/HA-Jev/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="mrnugget--jev-shell-history"></a>

### jev-shell-history

入力中の内容に合わせて、既存の zsh コマンド履歴を順位付けします。

- **原資料:** [jev-shell-history](https://github.com/mrnugget/jev-shell-history)
- **作者・組織:** mrnugget (en)
- **制約:** 履歴をモデルに渡します。デモでは架空の履歴を使っています。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/mrnugget/jev-shell-history/HEAD/README.md) · 2026-09-19 · 未追試.

## アプリとコンテンツツール

<a id="markjaquith--typesafe-ai-playground"></a>

### TypeSafe AI Playground (Rust CLI)

機微情報検出、コメントレビュー、語調分析、業種分類を試す Rust CLI です。

- **原資料:** [TypeSafe AI Playground (Rust CLI)](https://github.com/markjaquith/typesafe-ai-playground)
- **作者・組織:** markjaquith (en)
- **制約:** 機微情報検出は実験であり、コンプライアンス認証ではありません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/markjaquith/typesafe-ai-playground/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="brainstormity--jev-moderation-bot"></a>

### Jev Moderation Bot

Discord のスパムや詐欺リンクを判定し、段階的なモデレーションを行います。

- **原資料:** [Jev Moderation Bot](https://github.com/brainstormity/Jev-Moderation-Bot)
- **作者・組織:** brainstormity (en)
- **制約:** 削除やユーザーへの処分を伴います。接続や誤判定率の検証は未実施です。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/brainstormity/Jev-Moderation-Bot/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="chetaslua--jevmeter"></a>

### JEVMETER

動画の文字起こしを文ごとに評価し、結果をメーターとして映像に表示します。

- **原資料:** [JEVMETER](https://github.com/ChetasLua/jevmeter)
- **作者・組織:** ChetasLua (en)
- **制約:** 作者は、これらのスコアはファクトチェックではないと明記しています。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/ChetasLua/jevmeter/HEAD/README.md) · 2026-09-19 · 未追試.
- **関連リンク:** [X](https://x.com/chetaslua/status/2100473581251748216) — 元投稿または動画全編は独立に未確認。

<a id="monteduro--killmyidea"></a>

### Kill My Idea

起業アイデアに複数の質問を並列で行い、スコアを組み合わせて定型の判定を出します。

- **原資料:** [Kill My Idea](https://github.com/monteduro/killmyidea)
- **作者・組織:** monteduro (en)
- **制約:** 事業の成功予測ではありません。作者の実装は評価結果を既定で保存します。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/monteduro/killmyidea/HEAD/README.md) · 2026-09-19 · 未追試.

## ゲームとシミュレーション

<a id="emrickgarrett--onevonejev"></a>

### 1v1 Jev

ブラウザ上の対戦ゲームで、Jev がキャラクターの行動を選びます。

- **原資料:** [1v1 Jev](https://github.com/emrickgarrett/OneVOneJev)
- **作者・組織:** emrickgarrett (en)
- **制約:** ヒューリスティックな代替処理もあり、すべての動作が Jev によるものではありません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/emrickgarrett/OneVOneJev/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="fhshaik--typesafe-mario"></a>

### TypeSafe Mario

エミュレーターの RAM と計測値を状態に変換し、Jev が NES の操作を選びます。

- **原資料:** [TypeSafe Mario](https://github.com/fhshaik/typesafe-mario)
- **作者・組織:** fhshaik (en)
- **制約:** 実験的なコントローラーです。Jev にスクリーンショットは送りません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/fhshaik/typesafe-mario/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="phyous--tsai-sc"></a>

### Jev Plays StarCraft

構造化状態から StarCraft 体験版のミッションを操作し、行動確率を記録します。

- **原資料:** [Jev Plays StarCraft](https://github.com/phyous/tsai-sc)
- **作者・組織:** phyous (en)
- **制約:** 特定ミッションの成功報告であり、一般的なゲーム能力を示すものではありません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/phyous/tsai-sc/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="ably-labs--jev-pong"></a>

### Jev Pong

モデルの判断ごとに Pong の球を一歩進め、応答待ち時間を可視化します。

- **原資料:** [Jev Pong](https://github.com/ably-labs/jev-pong)
- **作者・組織:** ably-labs (en)
- **制約:** 球速は呼び出し時間に依存します。同じ時計での競技能力比較ではありません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/ably-labs/jev-pong/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="romanslack--jev-drone"></a>

### jev-drone

MuJoCo のドローン仮想環境で Jev が状況を判断し、高速制御はコードが担当します。

- **原資料:** [jev-drone](https://github.com/RomanSlack/jev-drone)
- **作者・組織:** RomanSlack (en)
- **制約:** Jev は画像を直接見ません。知覚結果を構造化してから入力します。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/RomanSlack/jev-drone/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="denikuchero--jev-chess-lab"></a>

### Jev Chess Lab

Jev 単独、戦術フィルター、Stockfish 支援を分けて記録したチェス実験です。

- **原資料:** [Jev Chess Lab](https://github.com/denikuchero/jev-chess-lab)
- **作者・組織:** denikuchero (en)
- **制約:** 作者によると単独の Jev は駒を失うミスが残ります。再生映像は実時間の録画ではありません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/denikuchero/jev-chess-lab/HEAD/README.md) · 2026-09-19 · 未追試.

## 評価と校正

<a id="abhixhek--jevcal"></a>

### jevcal

自分のデータで信頼度の閾値を選び、モデル更新による変化を検出します。

- **原資料:** [jevcal](https://github.com/abhixhek/jevcal)
- **作者・組織:** abhixhek (en)
- **制約:** 付属デモはシミュレーターで、実 API の測定結果ではありません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/abhixhek/jevcal/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="firassx914--janus"></a>

### Janus

小型・大型モデルの振り分け条件を測定し、振り分けを採用しない選択もできます。

- **原資料:** [Janus](https://github.com/FirasSX914/Janus)
- **作者・組織:** FirasSX914 (en)
- **制約:** 正解ラベルのないログで測れるのは一致率であり、正解率ではありません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/FirasSX914/Janus/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="abdelstark--jev-benchmarks"></a>

### jev-benchmarks

確率の校正、自動処理率、遅延、リソース消費を評価します。

- **原資料:** [jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)
- **作者・組織:** AbdelStark (en)
- **制約:** 結果はデータ、モデルの版、評価設計に依存します。本リポジトリでは未追試です。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/AbdelStark/jev-benchmarks/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="iammrduncan--typesafe-ai-benchmark"></a>

### typesafe-ai-benchmark

同じアプリケーション課題で、LLM の構造化出力と Jev を比較します。

- **原資料:** [typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark)
- **作者・組織:** iammrduncan (en)
- **制約:** 合成データの課題を含み、そのまま本番に一般化はできません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/iammrduncan/typesafe-ai-benchmark/HEAD/README.md) · 2026-09-19 · 未追試.

<a id="teyhouse--jev-secret-detection"></a>

### jev-secret-detection

コード片に利用可能な秘密情報が含まれるか、Noul の質問で評価します。

- **原資料:** [jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)
- **作者・組織:** teyhouse (en)
- **制約:** 正規表現や発行元での検証をあえて省いています。完全な秘密情報スキャナーではありません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/teyhouse/jev-secret-detection/HEAD/README.md) · 2026-09-19 · 未追試.

## 限界を探る実験

<a id="code-forge-au--jev-llm"></a>

### jev-llm

候補から次の単語を繰り返し選ぶことで、文章生成を構成する実験です。

- **原資料:** [jev-llm](https://github.com/Code-Forge-AU/jev-llm)
- **作者・組織:** Code-Forge-AU (en)
- **制約:** 各段階は候補選択です。Jev 自体が自由文を生成する機能ではありません。
- **確認状況:** プロジェクトの README を確認. [確認した資料](https://raw.githubusercontent.com/Code-Forge-AU/jev-llm/HEAD/README.md) · 2026-09-19 · 未追試.

