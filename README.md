# Awesome Grok Bot Playbooks

> 中文向 Grok Bot / 多 Agent 玩法清单。每条 = 短评 + 链接 + 标签。

本仓**不是** Grok Bot 客户端，也**不是** xAI 官方项目，只做整理与点评。

## 与 awesome-grok-bot 的差异

[ZeroPointRepo/awesome-grok-bot](https://github.com/ZeroPointRepo/awesome-grok-bot) 是英文生态导航，覆盖面广。本仓侧重：

- **中文出海一人公司**：一个人怎么用 bot 撑起调研、内容、客服
- **作战室**：多 bot 分工协作的编排方式
- **雷达 routine**：定时抓取、摘要、推送的固定流程
- **脱敏配方**：可直接抄的 prompt / 配置，已去掉 key 与隐私

不拼条目数量，宁缺毋滥。

## 目录

- [Official & SDK](#official--sdk)
- [Self-hosted bots](#self-hosted-bots)
- [Skills & Playbooks](#skills--playbooks)
- [Multi-bot teams](#multi-bot-teams)
- [Routines & Digests](#routines--digests)
- [Chinese solo-founder](#chinese-solo-founder)
- [Learning](#learning)

## 条目格式

```
- [名称](链接) - 一句话短评。标签：`tag1` `tag2`
```

---

## Official & SDK

- [xAI API Docs](https://docs.x.ai) - 官方 API 文档，模型列表、计费、工具调用都以这里为准。标签：`official` `api` `docs`
- [xai-org on GitHub](https://github.com/xai-org) - 官方开源组织，SDK 与开源模型权重入口。标签：`official` `sdk`

## Self-hosted bots

- [XinyunOpenBot](https://github.com/dongpen-max/XinyunOpenBot) - 中文优先的开源替代，默认简中，支持 OpenAI 兼容接口与 API 中转站，国内网络环境先看它。标签：`self-hosted` `chinese` `desktop`
- [OpenGrokBot](https://github.com/wolfqing/OpenGrokBot) - 基于 OpenClaw 的自托管方案，每个 bot 一台自己的机器、模型自带，想把数据留在本地时的首选参考。标签：`self-hosted` `openclaw` `byo-model`
- [open-grok-bot](https://github.com/Anil-matcha/open-grok-bot) - FastAPI + Next.js 的本地优先工作台，动作默认拒绝、需审批并留审计记录，适合对权限敏感的场景。标签：`self-hosted` `governance` `audit`

## Skills & Playbooks

- [grok-bot-templates](https://github.com/cobusgreyling/grok-bot-templates) - 模板工程化：规范 + Bot Ready 打分 + team / skill / routine 目录，写自己的配方前先对照它的结构。标签：`templates` `spec` `routine`
- [botskills](https://github.com/PramodDutta/botskills) - 可直接粘贴的 bot 设定，每条都声明「哪个动作必须先问你」，护栏写法值得抄。标签：`skills` `guardrails`
- [grokbot-for-gtm](https://github.com/bcharleson/grokbot-for-gtm) - 完整外呼 GTM 流程：建名单、补全、发信到处理回复，出海冷启动获客可参考。标签：`playbook` `gtm` `outbound`

## Multi-bot teams

- [botteams](https://github.com/ellelion/botteams) - 一个 markdown 文件装一整支团队（bot + 群聊 + routine），看作战室怎么一次性编排的好样例。标签：`multi-bot` `team` `routine`
- [grok-bot-profiles](https://github.com/HAEGONG/grok-bot-profiles) - 需求 / 复现 / 出 PR / 验 PR 四角色拆开，每个 bot 有明确审批边界，研发分工可直接套。标签：`multi-bot` `dev` `guardrails`
- [overnight](https://github.com/Archive228/overnight) - 六 bot 短视频生产线，素材带出处，发布前必须人审，内容号可参考它的人工闸门设计。标签：`multi-bot` `content` `human-in-loop`

## Routines & Digests

- [配方：竞品雷达 routine](examples/competitor-radar.md) - 定时抓竞品公开页面，只推送有实质变化的部分；重点在先过滤时间戳等噪音。标签：`example` `routine` `radar`

## Chinese solo-founder

- [配方：一人三岗](examples/one-person-three-roles.md) - 客服 + 内容 + 调研三个 bot 用文件交接，人每天只审 30 分钟；虚构示例，可直接改。标签：`example` `solo-founder` `multi-bot`
- [hiapi.ai](https://hiapi.ai) - 面向开发者与 Agent 的图片/视频/音频生成 API 聚合网关，用途型参考（作者相关）。标签：`api` `media` `solo-founder`

## Learning

- [awesome-grok-bot](https://github.com/ZeroPointRepo/awesome-grok-bot) - 英文生态导航，找现成 skill 和工具先翻这里，别自己造轮子。标签：`awesome` `learning`
- [配方模板](examples/_template.md) - 投稿配方前先照这个格式写：场景 / 输入 / 步骤 / prompt / 产出 / 坑。标签：`template` `learning`

---

## 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## License

[MIT](LICENSE)
