# Awesome Grok Bot Playbooks

[![Stars](https://img.shields.io/github/stars/sit-in/awesome-grokbot-playbooks?style=flat)](https://github.com/sit-in/awesome-grokbot-playbooks/stargazers)
[![link-check](https://github.com/sit-in/awesome-grokbot-playbooks/actions/workflows/link-check.yml/badge.svg)](https://github.com/sit-in/awesome-grokbot-playbooks/actions/workflows/link-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**中文** | [English](README.en.md) | [Roadmap](ROADMAP.md)

> 中文向 Grok Bot / 多 Agent 玩法清单。每条 = 短评 + 链接 + 标签；配方可直接抄。

**验证标记**：✅ 实测 = 在 Grok Bot 里真机跑通　🔍 已审 = 读过文档与配置、未真机跑　无标记 = 仅核实仓库存在且在维护

本仓**不是** Grok Bot 客户端，也**不是** xAI 官方项目，只做整理与点评。

## 3 分钟上手

1. **先补课**：读 [grokbot-field-notes](https://github.com/unicodef1wn/grokbot-field-notes) 的 `AGENTS.md` 和翻车记录，少走弯路
2. **要现成团队**：去 [botteams](https://github.com/ellelion/botteams) 挑一个 `installable` 团队，复制 installer prompt 粘进 Grok Bot
3. **要自己编排**：照 [作战室配方](examples/war-room.md) 拆角色、用文件交接、发布前加人工闸门
4. **不想上云**：看 [Self-hosted bots](#self-hosted-bots)

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
- [Hardware](#hardware)
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
- [xiryn](https://github.com/SouravBeraAkaSpeed/xiryn) - 每个 agent 一台 Docker 里的 Linux 桌面，模型自带 key、加密 vault、Telegram 遥控，最接近「自己的 Grok Bot」。标签：`self-hosted` `docker` `telegram`
- [DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - 基于 DeepSeek Harness 的开源平替，多 bot + 长期记忆 + 权限，中英双语 README，国内模型首选参考。标签：`self-hosted` `chinese` `deepseek`
- [lorca](https://github.com/egoist/lorca) - 「一个人的 Telegram」：端到端加密的 agent 消息面，偏个人通讯而非任务编排。GPL-3.0。标签：`self-hosted` `messaging` `e2ee`
- [guilds](https://github.com/CigaleAI/guilds) - 团队/公会形态的开源替代，早期项目，适合关注而非直接上生产。AGPL-3.0。标签：`self-hosted` `multi-bot`

## Skills & Playbooks

- [grok-bot-templates](https://github.com/cobusgreyling/grok-bot-templates) - 模板工程化：规范 + Bot Ready 打分 + team / skill / routine 目录，写自己的配方前先对照它的结构。标签：`templates` `spec` `routine`
- [botskills](https://github.com/PramodDutta/botskills) - 可直接粘贴的 bot 设定，每条都声明「哪个动作必须先问你」，护栏写法值得抄。标签：`skills` `guardrails`
- [grokbot-for-gtm](https://github.com/bcharleson/grokbot-for-gtm) - 完整外呼 GTM 流程：建名单、补全、发信到处理回复，出海冷启动获客可参考。标签：`playbook` `gtm` `outbound`
- [配方：Teach-a-Task](examples/teach-a-task.md) - 配合 Grok Bot 自带的 Teach a Task：演示前定边界，演示后整理成可审的技能卡，先干跑再放手。标签：`example` `skill` `teach-a-task`
- [grokbot-field-notes](https://github.com/unicodef1wn/grokbot-field-notes) - 非官方整理：xAI 团队 72 小时直播搭产品的规则、69 个角色、9 套岗位 playbook 和 40 条翻车记录，`AGENTS.md` 可直接拷。标签：`playbook` `field-notes` `agents-md`
- [grok-bot-jev](https://github.com/Bodila51/grok-bot-jev) - 在昂贵的调研/重试前加一层低成本分类决策，省调用量的思路值得抄；依赖第三方 TypeSafe 服务。标签：`skill` `cost` `decision-layer`
- [agent-cookie-sync](https://github.com/markfulton/agent-cookie-sync) - 把本机 Chrome 已登录站点交给云端 bot，不贴密码；等于把账号权限交出去，只给低敏账号用。标签：`chrome` `session` `security`
- [templatesgrokbot.com](https://github.com/templatesgrokbot/templatesgrokbot.com) - 3000+ 模板按岗位检索，可经 MCP 接入；量大质量参差，当灵感库用。标签：`templates` `catalog` `mcp`
- [devspace](https://github.com/Waishnav/devspace) - 极简的 MCP 编码 harness，让 Grok Bot、Claude、ChatGPT 等通过 MCP 拿到读写代码的能力。标签：`mcp` `coding` `harness`
- [Bland 电话 MCP](https://docs.bland.ai/integrations/mcp/grok-bot) - 第三方官方文档：给 Grok Bot 接上 Bland 的 MCP，用专属号码打电话、发短信，出海外呼可用；bot 能在对话里自己付费开户，务必先设人工闸门。标签：`mcp` `voice` `outbound`

## Multi-bot teams

- [botteams](https://github.com/ellelion/botteams) 🔍 - 一个 markdown 文件装一整支团队（bot + 群聊 + routine），看作战室怎么一次性编排的好样例；注意 `connector_modes` 只是 prompt 约束，不是权限。标签：`multi-bot` `team` `routine`
- [grok-bot-profiles](https://github.com/HAEGONG/grok-bot-profiles) 🔍 - 需求 / 复现 / 出 PR / 验 PR 四角色拆开，交接 ≠ 批准，验 PR 的 bot 必须单独会话；改编需按 CC BY 4.0 署名。标签：`multi-bot` `dev` `guardrails`
- [overnight](https://github.com/Archive228/overnight) - 六 bot 短视频生产线，素材带出处，发布前必须人审，内容号可参考它的人工闸门设计。标签：`multi-bot` `content` `human-in-loop`
- [配方：作战室](examples/war-room.md) - 3–6 个 bot 只靠文件交接、不串聊，发布前过人工闸门；本仓 Claude ⇄ Grok 协作就是这套。标签：`example` `multi-bot` `war-room`
- [配方：研发四角色](examples/dev-four-roles.md) - 需求 / 复现 / 出 PR / 验 PR 拆给四个 bot，产出和裁决分开，人只在批准 spec 和合并两处点头。标签：`example` `dev` `guardrails`
- [grokbot-gtm-team](https://github.com/timscheuerai/grokbot-gtm-team) - 13 个 GTM bot + 规则 + 一句话建队 prompt，Grok Bot 编排、Claude Code/Codex 干活。标签：`multi-bot` `gtm` `claude-code`
- [AgentPeerChat](https://github.com/AgenticsWorks/AgentPeerChat) - 自托管的 agent 间消息通道，一键部署到 Cloudflare，可把 Grok Bot 和其他 agent 拉进同一频道。标签：`multi-bot` `messaging` `cloudflare`
- [noodle](https://github.com/pdparchitect/noodle) - Mac / iOS 多 agent 群聊客户端，复用已有订阅（Codex、Claude Code、Grok Build 等），本地组队的轻量方案。标签：`multi-bot` `macos` `desktop`
- [orca](https://github.com/stablyai/orca) - 管一整队 agent（Grok Bot、Codex 等）的工作台，桌面 / 手机 / 远程都能用，跑在你自己的订阅上；生态里体量最大的项目。标签：`multi-bot` `fleet` `desktop`
- [agentrove](https://github.com/Mng-dev-ai/agentrove) - 自托管编码工作区，把 Claude Code、Codex、Cursor、Grok 等 agent 放在一起编排，带 persona 和多 agent 工作流。标签：`multi-bot` `self-hosted` `coding`

## Routines & Digests

- [配方：竞品雷达 routine](examples/competitor-radar.md) - 定时抓竞品公开页面，只推送有实质变化的部分；重点在先过滤时间戳等噪音。标签：`example` `routine` `radar`
- [配方：周报 routine](examples/weekly-review.md) - 每周五从 GitHub、文档、日历收痕迹出初稿，对照上周计划，每条必须带链接，人改 10 分钟就发。标签：`example` `routine` `weekly`
- [配方：X 雷达](examples/x-radar.md) - 每天扫一轮 X 公开帖，只推有实质信号的摘要，没信号就不打扰；互动一律人来。标签：`example` `routine` `x`

## Chinese solo-founder

- [配方：一人三岗](examples/one-person-three-roles.md) - 客服 + 内容 + 调研三个 bot 用文件交接，人每天只审 30 分钟；虚构示例，可直接改。标签：`example` `solo-founder` `multi-bot`
- [配方：出海客服](examples/outbound-support.md) - 多语言工单先脱敏、再分流、只出草稿；付款、安全、法律类一律转人工，bot 不直接发信。标签：`example` `support` `i18n`
- [eze-grokbot](https://github.com/eze-is/eze-grokbot) - 中文作者公开的多 bot 配置，每个 bot 一个文件夹，看真人怎么拆角色。未声明 License，只参考结构。标签：`chinese` `profiles` `config`
- [grok-bot-wechat](https://github.com/bogao6769-netizen/grok-bot-wechat) - 微信消息触发 Grok Bot 的 webhook Routine，本地转发器把回复送回微信；只是配方不含服务，项目很新，想让国内用户在微信里找 bot 的可参考。标签：`chinese` `wechat` `routine`
- [hiapi.ai](https://hiapi.ai) - 面向开发者与 Agent 的图片/视频/音频生成 API 聚合网关，用途型参考（作者相关）。标签：`api` `media` `solo-founder`

## Hardware

- [groki-bot](https://github.com/JosssphZhou/groki-bot) - M5Stack CoreS3 桌面机器人：固件 + 电脑端语音/MCP 网关，能把任务交接给 Grok Bot，想让 bot 有个实体入口时参考。标签：`hardware` `mcp` `voice`
- [grok-gadgets](https://github.com/adidshaft/grok-gadgets) - 把硬件接到 Grok Bot 的 SDK 和工具，可先用模拟器，再上 ESP32-S3 OLED 套件；作者标注 alpha，玩票为主。标签：`hardware` `esp32` `sdk`

## Learning

- [awesome-grok-bot](https://github.com/ZeroPointRepo/awesome-grok-bot) - 英文生态导航，找现成 skill 和工具先翻这里，别自己造轮子。标签：`awesome` `learning`
- [CNR Grok Bot 指南](https://cnrcode.com/guides/) - 英文入门四篇：功能与套餐、Routine 和 Skill 设置、额度怎么省、5 套免费模板；咨询公司官网，带营销成分。标签：`guide` `routine` `usage`
- [配方模板](examples/_template.md) - 投稿配方前先照这个格式写：场景 / 输入 / 步骤 / prompt / 产出 / 坑。标签：`template` `learning`

---

## 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## License

[MIT](LICENSE)
