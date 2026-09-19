# 贡献指南

[English](CONTRIBUTING.md) · **简体中文**

欢迎提交使用 **TypeSafe Jev** 的项目、实践教程、作者演示和评测。一个项目只保留一条，视频和帖子作为相关链接补充。

## 提交方式

可以使用 Issue 表单提交原始链接、作者、Jev 实际负责的判断、源码或演示、限制及核验方法。不要求事先调用付费 API；未读原文的线索请标注待核验。

提交 PR 时：

1. 在 `data/resources.json` 更新**英文**资料；待核验的 X / YouTube 线索放在 `data/candidates.json`。
2. 同步更新 `data/locales/zh-CN.json`、`data/locales/ja.json`、`data/locales/es.json` 中相同 ID 的 `title`、`summary`、`limitations`。
3. 保留项目名称、原始地址、其他模型参与、失败情况和未复现说明。不把来源核对日期改成翻译日期。
4. 运行 `python3 scripts/catalog.py` 和 `python3 scripts/catalog.py --check`。
5. 在 PR 中说明来源、核验方法及未验证部分。

字段列表与规范见[英文贡献指南](CONTRIBUTING.md)。不要手工修改生成的 `README*.md`、`catalog/*.md`、`docs/START-HERE*.md`。

`README.md` 为默认英文首页；`README.en.md` 为兼容旧链接的生成副本。其他语言均有完整索引、详情页、入门页与候选列表。媒体候选中的原始标题保留原文。检查脚本会检测漏译的条目和字段，但不能判断翻译准确性；英文有变动时应人工复核三个译本。

## 内容标准

- 只收录与 TypeSafe Jev 有明确关系的资源，不混入同名项目。
- 不把受 Jev 启发的替代模型描述成调用官方 Jev。
- 不用无依据的“零错误”“绝对安全”或性能排名。
- 不提交 API key、私人数据、完整转载或未授权媒体。
- 核验等级见[方法说明](docs/METHODOLOGY.zh-CN.md)。当前 `reproduction` 只接受 `not-run`；更改前须补充复现证据结构及多语言展示。

Python 3.10+，无第三方依赖。检查仅离线执行，不访问外部服务或调用模型。原创整理和脚本使用本仓库许可证，外链内容保留原许可证。
