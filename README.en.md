# Awesome Grok Bot Playbooks

[![Stars](https://img.shields.io/github/stars/sit-in/awesome-grokbot-playbooks?style=flat)](https://github.com/sit-in/awesome-grokbot-playbooks/stargazers)
[![link-check](https://github.com/sit-in/awesome-grokbot-playbooks/actions/workflows/link-check.yml/badge.svg)](https://github.com/sit-in/awesome-grokbot-playbooks/actions/workflows/link-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

[中文](README.md) | **English** | [Roadmap](ROADMAP.md)

> Curated Grok Bot / multi-agent playbooks. Each entry = short review + link + tags. Recipes are copy-paste ready.

**Verification marks**: ✅ tested = run end-to-end in Grok Bot　🔍 reviewed = docs and config read, not run　no mark = repo confirmed to exist and be maintained

This repo is **not** a Grok Bot client and **not** affiliated with xAI. It only curates and reviews.

## 3-minute start

1. **Learn first**: read `AGENTS.md` and the failure log in [grokbot-field-notes](https://github.com/unicodef1wn/grokbot-field-notes)
2. **Want a ready-made team**: pick an `installable` team on [botteams](https://github.com/ellelion/botteams) and paste its installer prompt into Grok Bot
3. **Want to orchestrate yourself**: follow the [war room recipe](examples/war-room.md): split roles, hand off via files, add a human gate before publishing
4. **Don't want the cloud**: see [Self-hosted bots](#self-hosted-bots)

## How it differs from awesome-grok-bot

[ZeroPointRepo/awesome-grok-bot](https://github.com/ZeroPointRepo/awesome-grok-bot) is a broad ecosystem index. This repo focuses on:

- **Solo founders going global**: one person running research, content and support with bots
- **War rooms**: orchestrating multiple bots that split work
- **Radar routines**: scheduled fetch → summarize → notify pipelines
- **Sanitized recipes**: prompts and configs you can copy, with keys and private data removed

Quality over quantity.

## Contents

- [Official & SDK](#official--sdk)
- [Self-hosted bots](#self-hosted-bots)
- [Skills & Playbooks](#skills--playbooks)
- [Multi-bot teams](#multi-bot-teams)
- [Routines & Digests](#routines--digests)
- [Chinese solo-founder](#chinese-solo-founder)
- [Hardware](#hardware)
- [Learning](#learning)

---

## Official & SDK

- [xAI API Docs](https://docs.x.ai) - Official API docs; source of truth for models, pricing and tool calling. Tags: `official` `api` `docs`
- [xai-org on GitHub](https://github.com/xai-org) - Official open-source org: SDKs and open model weights. Tags: `official` `sdk`
- [grokbot-sdk](https://github.com/adam91holt/grokbot-sdk) - Unofficial TypeScript SDK: talks to a running Grok Bot host's local gateway for roster, memories and transcripts, and reads the local data directory when the host is down. Needs the gateway token; keep it on your own machine. Tags: `sdk` `typescript` `unofficial`
- [Grok Bot Marketplace](https://x.ai/bot/marketplace) - Official template catalog grouped by sales, engineering, marketing, design, operations and personal; click Add to import into your Grok Bot. Most single templates listed here can be found there. Tags: `official` `templates` `marketplace`

## Self-hosted bots

- [XinyunOpenBot](https://github.com/dongpen-max/XinyunOpenBot) - Chinese-first open alternative, Simplified Chinese by default, supports OpenAI-compatible endpoints and API relays. Tags: `self-hosted` `chinese` `desktop`
- [OpenGrokBot](https://github.com/wolfqing/OpenGrokBot) - Self-hosted on OpenClaw, one machine per bot, bring your own model; the reference if you want data to stay local. Tags: `self-hosted` `openclaw` `byo-model`
- [open-grok-bot](https://github.com/Anil-matcha/open-grok-bot) - Local-first FastAPI + Next.js workspace; actions are deny-by-default with approvals and an audit trail. Tags: `self-hosted` `governance` `audit`
- [xiryn](https://github.com/SouravBeraAkaSpeed/xiryn) - Each agent gets its own Linux desktop in Docker, bring-your-own keys, encrypted vault, Telegram control; closest to owning your own Grok Bot. Tags: `self-hosted` `docker` `telegram`
- [DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Open alternative on DeepSeek Harness: multi-bot, long-term memory, permissions, bilingual README. Tags: `self-hosted` `chinese` `deepseek`
- [lorca](https://github.com/egoist/lorca) - "Telegram for one person": end-to-end encrypted messaging with agents, more personal comms than task orchestration. GPL-3.0. Tags: `self-hosted` `messaging` `e2ee`
- [guilds](https://github.com/CigaleAI/guilds) - Team/guild-style open alternative; early project, watch before production use. AGPL-3.0. Tags: `self-hosted` `multi-bot`
- [rakazo](https://github.com/elie222/rakazo) - Open-source, self-hosted Grok Bot alternative: pick your own model and sandbox, then chat with and manage bots the way you would in Grok Bot. Most-starred in its class. Tags: `self-hosted` `byo-model` `alternative`
- [Codync](https://github.com/leepokai/Codync) - Open-source alternative that turns local coding agents (Claude Code, Codex, Cursor, Grok Build and ~40 more) into bots you can message from phone or desktop. Tags: `self-hosted` `multi-agent` `acp`
- [openbot (nightly-labs)](https://github.com/nightly-labs/openbot) - Local-first desktop workspace with per-agent workspaces and task queues for Codex, Claude and Grok; can import agents exported from Grok Bot. Not the same project as CopilotKit/OpenBot. Licensed PolyForm Noncommercial; commercial use needs a separate license. Tags: `self-hosted` `desktop` `noncommercial`

## Skills & Playbooks

- [grok-bot-templates](https://github.com/cobusgreyling/grok-bot-templates) - Engineering kit for templates: spec, Bot Ready score, team / skill / routine catalog. Check its structure before writing your own. Tags: `templates` `spec` `routine`
- [botskills](https://github.com/PramodDutta/botskills) - Paste-ready bot setups; each declares the one action it never takes without you. Good guardrail pattern. Tags: `skills` `guardrails`
- [grokbot-for-gtm](https://github.com/bcharleson/grokbot-for-gtm) - Full outbound GTM motion from list building and enrichment to reply handling. Tags: `playbook` `gtm` `outbound`
- [Recipe: Teach-a-Task](examples/teach-a-task.md) - Pairs with Grok Bot's built-in Teach a Task: set boundaries before the demo, turn it into a reviewable skill card after, dry-run before letting go. (Chinese) Tags: `example` `skill` `teach-a-task`
- [grokbot-field-notes](https://github.com/unicodef1wn/grokbot-field-notes) - Unofficial notes from the xAI team's 72-hour live build: rules, 69 roles, 9 role playbooks and 40 failures; `AGENTS.md` is drop-in. Tags: `playbook` `field-notes` `agents-md`
- [grok-bot-jev](https://github.com/Bodila51/grok-bot-jev) - A cheap classification step before expensive research or retries; worth copying the idea. Depends on the third-party TypeSafe service. Tags: `skill` `cost` `decision-layer`
- [agent-cookie-sync](https://github.com/markfulton/agent-cookie-sync) - Hands your signed-in Chrome sessions to a cloud bot without pasting passwords; that still hands over account access, so use low-sensitivity accounts only. Tags: `chrome` `session` `security`
- [templatesgrokbot.com](https://github.com/templatesgrokbot/templatesgrokbot.com) - 3,000+ templates searchable by job title, MCP-accessible; uneven quality, use as an idea library. Tags: `templates` `catalog` `mcp`
- [devspace](https://github.com/Waishnav/devspace) - Minimal coding-agent harness over MCP, giving Grok Bot, Claude, ChatGPT and others the ability to read and edit code. Tags: `mcp` `coding` `harness`
- [Bland phone MCP](https://docs.bland.ai/integrations/mcp/grok-bot) - Third-party official docs: connect Bland's MCP so Grok Bot can call and text from a dedicated number; the bot can pay for and open the account inside a conversation, so put a human gate in front of it. Tags: `mcp` `voice` `outbound`
- [grokbot-imessage-skill](https://github.com/jeffhuber/grokbot-imessage-skill) - Lets Grok Bot read, search and triage iMessage on macOS, with preview-and-confirm before sending. Requires Full Disk Access, which hands your whole message history to the bot; use with care. Tags: `skill` `imessage` `macos`
- [grok-bot-skill](https://github.com/adamanz/grok-bot-skill) - A skill for Claude Code, Cursor or Codex to message Grok Bot teammates and create new bots from the terminal, through your signed-in Grok Bot desktop app. Tags: `skill` `cli` `claude-code`
- [lauren-poteto-rules](https://github.com/unicodef1wn/lauren-poteto-rules) - Engineering principles as a private Grok Bot skill: evidence before diagnosis, verify in the running product, turn repeated corrections into durable constraints. Same author as grokbot-field-notes. Tags: `skill` `engineering` `rules`
- [web-access](https://github.com/eze-is/web-access) - Gives local agents (Claude Code, Grok Bot and others) full web access: three-tier channel routing, browser CDP, parallel fetching, and per-site experience that builds up over time. Same author as eze-grokbot. README declares MIT but the repo has no LICENSE file. (Chinese) Tags: `skill` `browser` `cdp`
- [botdirectory.ai](https://github.com/elie222/botdirectory.ai) - Open-source directory of bot prompts usable in Grok Bot, Rakazo and others; browse it for ideas. Tags: `templates` `directory` `prompts`
- [Template: Motion Director](https://x.ai/bot/MdpeJPD6eiY7YWUa9bfes) - Third-party template, one-click import: one line (a product URL, topic or song) becomes a finished film with shot-by-shot animation, lip sync from the vocals and local GPU upscaling, plus a contact sheet and quality-check results. No price listed; importing accepts the bot-sharing terms. Tags: `template` `video` `creative`

## Multi-bot teams

- [botteams](https://github.com/ellelion/botteams) 🔍 - A whole team (bots + group chat + routines) in one markdown file; a good war-room orchestration example. Note `connector_modes` is prompt wording, not a permission. Tags: `multi-bot` `team` `routine`
- [grok-bot-profiles](https://github.com/HAEGONG/grok-bot-profiles) 🔍 - Spec / repro / PR / verify as four separate bots; hand-off is not approval, and the verifier must run in its own conversation. CC BY 4.0, attribute when adapting. Tags: `multi-bot` `dev` `guardrails`
- [overnight](https://github.com/Archive228/overnight) - Six-bot short-video crew with sourced material and a mandatory human review before publishing. Tags: `multi-bot` `content` `human-in-loop`
- [Recipe: war room](examples/war-room.md) - 3–6 bots hand off via files only, with a human gate before publishing; this repo's own Claude ⇄ Grok workflow. (Chinese) Tags: `example` `multi-bot` `war-room`
- [Recipe: four dev roles](examples/dev-four-roles.md) - Spec / repro / PR / verify split across four bots so producing and judging stay separate; the human only approves the spec and merges. (Chinese) Tags: `example` `dev` `guardrails`
- [grokbot-gtm-team](https://github.com/timscheuerai/grokbot-gtm-team) - 13 GTM bots, their rules, and a one-chat setup prompt; Grok Bot orchestrates, Claude Code / Codex do the work. Tags: `multi-bot` `gtm` `claude-code`
- [AgentPeerChat](https://github.com/AgenticsWorks/AgentPeerChat) - Self-hosted agent-to-agent messaging, one-click Cloudflare deploy; puts Grok Bot and other agents in one channel. Tags: `multi-bot` `messaging` `cloudflare`
- [noodle](https://github.com/pdparchitect/noodle) - Mac / iOS multi-agent group chat reusing your existing subscriptions (Codex, Claude Code, Grok Build, ...). Tags: `multi-bot` `macos` `desktop`
- [orca](https://github.com/stablyai/orca) - A workspace for a fleet of agents (Grok Bot, Codex, ...) on desktop, mobile or remote, running on your own subscriptions; the largest project in this ecosystem. Tags: `multi-bot` `fleet` `desktop`
- [agentrove](https://github.com/Mng-dev-ai/agentrove) - Self-hosted coding workspace orchestrating Claude Code, Codex, Cursor, Grok and more, with personas and multi-agent workflows. Tags: `multi-bot` `self-hosted` `coding`
- [reason-network](https://github.com/reason-machines/reason-network) - One small daemon per computer, peer to peer, so coding agents (Claude Code, Codex, Cursor, ...) can message and hand work to each other, falling back to an encrypted relay when a direct link fails. Grok Bot is not wired in automatically: install the CLI on its cloud computer and use `listen` / `send`. The Reason plugin of the same name hands tasks to Reason's cloud agents, which is a separate thing from this network. Our 2026-10-18 attempt to link a Grok Bot cloud computer with a local Mac did not connect; cause unknown. Engine is dual-licensed MIT or Apache-2.0; the Reason CLI is not open source. Tags: `multi-bot` `p2p` `claude-code`
- [Template: Chief of Operations](https://x.ai/bot/HQh9l4duDHNmhCuSW_pn-) - Third-party, one-click import: keeps shared team rules, a register of every bot and routine, regular security audits and an incident plan; you approve every change. Pairs with the [Routine budget check recipe](examples/routine-budget.md). Tags: `template` `governance` `audit`
- [Template: T3 Code Bridge](https://x.ai/bot/_5NG_WsrOdQs2jtUhZeQH) - Third-party, one-click import: Grok Bot launches, directs and monitors T3 Code coding threads, and pings you when one finishes, fails or needs input. Tags: `template` `coding` `t3-code`

## Routines & Digests

- [Recipe: competitor radar routine](examples/competitor-radar.md) - Scheduled scraping of competitor pages that only notifies on real changes; filter timestamp noise first. (Chinese) Tags: `example` `routine` `radar`
- [Recipe: weekly review routine](examples/weekly-review.md) - Every Friday, collect the week's traces from GitHub, docs and calendar into a draft checked against last week's plan; every item needs a link. (Chinese) Tags: `example` `routine` `weekly`
- [Recipe: X radar](examples/x-radar.md) - A daily pass over public X posts that only pushes a digest when there is real signal; all engagement stays human. (Chinese) Tags: `example` `routine` `x`
- [Recipe: Routine budget check](examples/routine-budget.md) - When quota is nearly gone, pause everything, have a lead bot grade each Routine, then re-enable one by one after human sign-off; high-frequency Routines stay silent when nothing changed. (Chinese) Tags: `example` `routine` `budget`

## Chinese solo-founder

- [Recipe: one person, three roles](examples/one-person-three-roles.md) - Support + content + research bots hand off via files; the human reviews 30 minutes a day. Fictional example. (Chinese) Tags: `example` `solo-founder` `multi-bot`
- [Recipe: global support triage](examples/outbound-support.md) - Sanitize multilingual tickets, triage, draft only; payment, security and legal go to a human, the bot never sends. (Chinese) Tags: `example` `support` `i18n`
- [eze-grokbot](https://github.com/eze-is/eze-grokbot) - A Chinese author's public multi-bot config, one folder per bot; see how a real person splits roles. No license declared, reference structure only. Tags: `chinese` `profiles` `config`
- [grok-bot-wechat](https://github.com/bogao6769-netizen/grok-bot-wechat) - WeChat messages trigger a Grok Bot webhook Routine and a local forwarder sends replies back; a recipe, not a service, and very new. Tags: `chinese` `wechat` `routine`
- [hiapi.ai](https://hiapi.ai) - Image / video / audio generation API gateway for developers and agents (author-related). Tags: `api` `media` `solo-founder`

## Hardware

- [groki-bot](https://github.com/JosssphZhou/groki-bot) - M5Stack CoreS3 desktop robot: firmware plus a voice / MCP gateway on your computer, with hand-off to Grok Bot; a reference for giving a bot a physical front end. Tags: `hardware` `mcp` `voice`
- [grok-gadgets](https://github.com/adidshaft/grok-gadgets) - SDKs and tools to connect hardware to Grok Bot; start with the simulator, then the ESP32-S3 OLED kit. The author labels it alpha. Tags: `hardware` `esp32` `sdk`

## Learning

- [awesome-grok-bot](https://github.com/ZeroPointRepo/awesome-grok-bot) - The English ecosystem index; check here for existing skills and tools before building your own. Tags: `awesome` `learning`
- [CNR Grok Bot guides](https://cnrcode.com/guides/) - Four intro guides: features and plans, Routines and Skills setup, making usage limits last, five free templates; a consulting firm's site, so expect some marketing. Tags: `guide` `routine` `usage`
- [Tiezhu Grok Bot learning site](https://bot.tiezhu.si/) - Unofficial Chinese learning site in four parts: setup, dispatching tasks, Routines, then multi-bot teamwork and enterprise deployment, with case studies such as a social-media team and an always-on repo ops desk. Links out to the author's WeChat account and group. (Chinese) Tags: `chinese` `guide` `learning`
- [Grok Bot Orange Book](https://github.com/KinGao294/grok-bot-orange-book) - A ~16k-character beginner-to-advanced handbook: multi-bot teamwork, Routines, saving usage and automation, in PDF and Markdown; the author suggests feeding the whole book to your bot as context. Written in the first two weeks after launch, so check official docs before acting. README declares CC BY-NC-SA 4.0 (non-commercial). (Chinese) Tags: `chinese` `guide` `book`
- [UseGrokBot](https://usegrokbot.com/) - Third-party discovery site: templates grouped by role, real use cases, bot-team setups and ranked articles, in English, Chinese and Japanese. Browse it for ideas. Tags: `directory` `use-cases` `templates`
- [sitin's Grok Bot tutorials](docs/sitin-tutorials.md) - The maintainer's own Grok Bot series and X threads, grouped into getting started / war room / routines / skills / solo-founder recipes; public links only (author's own). (Chinese) Tags: `chinese` `tutorials` `author`
- [Community Grok Bot tutorials](docs/community-tutorials.md) - 25 X threads and articles by other creators, Chinese and English, grouped into getting started, war room, routines and usage, skills, solo-founder and indexes; each checked for liveness and date. (Chinese) Tags: `chinese` `tutorials` `community`
- [Recipe template](examples/_template.md) - Format to follow before submitting a recipe: scenario / input / steps / prompt / output / pitfalls. (Chinese) Tags: `template` `learning`

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) (Chinese). English issues and PRs are welcome.

## License

[MIT](LICENSE)
