# 首批研究记录

[返回首页](../README.zh-CN.md)

核对日期：2026-09-19。目标：为 TypeSafe Jev 建立按用途浏览、可追溯到一手资料的案例索引。

## 发现渠道

- [TypeSafe 官方文档索引](https://docs.typesafe.ai/llms.txt)：发现官方 cookbook、模式与 SDK。
- [MrJev / awesome-jev](https://github.com/MrJev/awesome-jev)：发现多个社区仓库；逐个读取原作者 README 后重新编写摘要，不沿用其验证结论。
- [hellogumbo / awesome-jev](https://github.com/hellogumbo/awesome-jev)：交叉发现社区方向。
- [Made with Jev](https://madewithjev.com/)：发现具体 X 帖子及 YouTube 视频链接，保留为待核验线索。
- Web 搜索：补充社交自动化、创业点子评分、凭据检测、受限文字生成实验和开发团队实测。

代表搜索词：`"jev" AI examples github`、`"jev" "noul"`、`Jev TypeSafe YouTube demo`、`Jev typesafe site:x.com`。搜索结果仅用于定位，一手正文才用于写正式技术摘要。

## 本次检查完成了什么

- 获取并阅读 46 个源码项目/SDK 的 README，记录原始地址与正文散列。
- 获取 25 篇官方文档：23 篇正文传输完整，意图路由与 Noul 一致性两篇只核对已收到的导语及官方目录，详情明确标记。
- 阅读 Retriever AI 自己撰写的浏览器集成报告，保留实验规模和成本边界。
- 收集 28 个具体视频/社交链接，单独入候选区。
- 没有克隆、安装、执行第三方项目，也没有使用当前工作区的 API 凭据。

## 访问限制及未收录项

YouTube 直接页面及 oEmbed 请求出现超时，搜索工具也未返回可核验的原视频内容。X 样本原帖在搜索工具中返回 403。浏览器后续读到了 Moritz Kremb 原帖标题与章节，但未观看其视频，仍保留待核验。未将目录摘要伪装成已观看视频或已读完整原帖。

若干 GitHub README 的 HEAD/raw 路径返回 404：这不足以认定仓库被删除，也可能是文件名或默认分支问题。以下线索未进入正式清单：`typesafe-ai/typesafe-sdk-js`、`AntonioCoppe/jev-harness`、`jomatsu/zod-jev`、`kieranklaassen/ruby_llm-typesafe`、`yusukebe/hono-jev-router`、`reachjalil/jev-tree`、`zampierid4p/n8n-nodes-typesafe-ai`、`ellipsis-dev/blink`。`standardagents/jevpilot` 读取结果为空，同样未收录。

没有沿用外部目录的“数百项目”数量作为本仓库成果，也没有把替代模型或单纯提到 Jev 的项目自动收录。

## 下一批值得补充

- 人工查看候选视频，确认作者、正式标题、章节时间、源码链接。
- 为现有 GitHub 条目关联作者原始发布帖，补充具体发布日期。
- 每个用途挑选一个项目，在独立环境记录可复现步骤与失败案例。
- 增加中文作者的一手实践，避免只收录二手解读。
- 再检查未找到 README 的候选仓库，而不是把临时访问失败写成永久失效。
