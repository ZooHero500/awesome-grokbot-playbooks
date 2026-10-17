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

## Self-hosted bots

- [XinyunOpenBot](https://github.com/dongpen-max/XinyunOpenBot) - Chinese-first open alternative, Simplified Chinese by default, supports OpenAI-compatible endpoints and API relays. Tags: `self-hosted` `chinese` `desktop`
- [OpenGrokBot](https://github.com/wolfqing/OpenGrokBot) - Self-hosted on OpenClaw, one machine per bot, bring your own model; the reference if you want data to stay local. Tags: `self-hosted` `openclaw` `byo-model`
- [open-grok-bot](https://github.com/Anil-matcha/open-grok-bot) - Local-first FastAPI + Next.js workspace; actions are deny-by-default with approvals and an audit trail. Tags: `self-hosted` `governance` `audit`
- [xiryn](https://github.com/SouravBeraAkaSpeed/xiryn) - Each agent gets its own Linux desktop in Docker, bring-your-own keys, encrypted vault, Telegram control; closest to owning your own Grok Bot. Tags: `self-hosted` `docker` `telegram`
- [DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Open alternative on DeepSeek Harness: multi-bot, long-term memory, permissions, bilingual README. Tags: `self-hosted` `chinese` `deepseek`
- [lorca](https://github.com/egoist/lorca) - "Telegram for one person": end-to-end encrypted messaging with agents, more personal comms than task orchestration. GPL-3.0. Tags: `self-hosted` `messaging` `e2ee`
- [guilds](https://github.com/CigaleAI/guilds) - Team/guild-style open alternative; early project, watch before production use. AGPL-3.0. Tags: `self-hosted` `multi-bot`

## Skills & Playbooks

- [grok-bot-templates](https://github.com/cobusgreyling/grok-bot-templates) - Engineering kit for templates: spec, Bot Ready score, team / skill / routine catalog. Check its structure before writing your own. Tags: `templates` `spec` `routine`
- [botskills](https://github.com/PramodDutta/botskills) - Paste-ready bot setups; each declares the one action it never takes without you. Good guardrail pattern. Tags: `skills` `guardrails`
- [grokbot-for-gtm](https://github.com/bcharleson/grokbot-for-gtm) - Full outbound GTM motion from list building and enrichment to reply handling. Tags: `playbook` `gtm` `outbound`
- [Recipe: Teach-a-Task](examples/teach-a-task.md) - Pairs with Grok Bot's built-in Teach a Task: set boundaries before the demo, turn it into a reviewable skill card after, dry-run before letting go. (Chinese) Tags: `example` `skill` `teach-a-task`
- [grokbot-field-notes](https://github.com/unicodef1wn/grokbot-field-notes) - Unofficial notes from the xAI team's 72-hour live build: rules, 69 roles, 9 role playbooks and 40 failures; `AGENTS.md` is drop-in. Tags: `playbook` `field-notes` `agents-md`
- [grok-bot-jev](https://github.com/Bodila51/grok-bot-jev) - A cheap classification step before expensive research or retries; worth copying the idea. Depends on the third-party TypeSafe service. Tags: `skill` `cost` `decision-layer`
- [agent-cookie-sync](https://github.com/markfulton/agent-cookie-sync) - Hands your signed-in Chrome sessions to a cloud bot without pasting passwords; that still hands over account access, so use low-sensitivity accounts only. Tags: `chrome` `session` `security`
- [templatesgrokbot.com](https://github.com/templatesgrokbot/templatesgrokbot.com) - 3,000+ templates searchable by job title, MCP-accessible; uneven quality, use as an idea library. Tags: `templates` `catalog` `mcp`

## Multi-bot teams

- [botteams](https://github.com/ellelion/botteams) 🔍 - A whole team (bots + group chat + routines) in one markdown file; a good war-room orchestration example. Note `connector_modes` is prompt wording, not a permission. Tags: `multi-bot` `team` `routine`
- [grok-bot-profiles](https://github.com/HAEGONG/grok-bot-profiles) 🔍 - Spec / repro / PR / verify as four separate bots; hand-off is not approval, and the verifier must run in its own conversation. CC BY 4.0, attribute when adapting. Tags: `multi-bot` `dev` `guardrails`
- [overnight](https://github.com/Archive228/overnight) - Six-bot short-video crew with sourced material and a mandatory human review before publishing. Tags: `multi-bot` `content` `human-in-loop`
- [Recipe: war room](examples/war-room.md) - 3–6 bots hand off via files only, with a human gate before publishing; this repo's own Claude ⇄ Grok workflow. (Chinese) Tags: `example` `multi-bot` `war-room`
- [Recipe: four dev roles](examples/dev-four-roles.md) - Spec / repro / PR / verify split across four bots so producing and judging stay separate; the human only approves the spec and merges. (Chinese) Tags: `example` `dev` `guardrails`
- [grokbot-gtm-team](https://github.com/timscheuerai/grokbot-gtm-team) - 13 GTM bots, their rules, and a one-chat setup prompt; Grok Bot orchestrates, Claude Code / Codex do the work. Tags: `multi-bot` `gtm` `claude-code`
- [AgentPeerChat](https://github.com/AgenticsWorks/AgentPeerChat) - Self-hosted agent-to-agent messaging, one-click Cloudflare deploy; puts Grok Bot and other agents in one channel. Tags: `multi-bot` `messaging` `cloudflare`
- [noodle](https://github.com/pdparchitect/noodle) - Mac / iOS multi-agent group chat reusing your existing subscriptions (Codex, Claude Code, Grok Build, ...). Tags: `multi-bot` `macos` `desktop`

## Routines & Digests

- [Recipe: competitor radar routine](examples/competitor-radar.md) - Scheduled scraping of competitor pages that only notifies on real changes; filter timestamp noise first. (Chinese) Tags: `example` `routine` `radar`
- [Recipe: weekly review routine](examples/weekly-review.md) - Every Friday, collect the week's traces from GitHub, docs and calendar into a draft checked against last week's plan; every item needs a link. (Chinese) Tags: `example` `routine` `weekly`
- [Recipe: X radar](examples/x-radar.md) - A daily pass over public X posts that only pushes a digest when there is real signal; all engagement stays human. (Chinese) Tags: `example` `routine` `x`

## Chinese solo-founder

- [Recipe: one person, three roles](examples/one-person-three-roles.md) - Support + content + research bots hand off via files; the human reviews 30 minutes a day. Fictional example. (Chinese) Tags: `example` `solo-founder` `multi-bot`
- [Recipe: global support triage](examples/outbound-support.md) - Sanitize multilingual tickets, triage, draft only; payment, security and legal go to a human, the bot never sends. (Chinese) Tags: `example` `support` `i18n`
- [eze-grokbot](https://github.com/eze-is/eze-grokbot) - A Chinese author's public multi-bot config, one folder per bot; see how a real person splits roles. No license declared, reference structure only. Tags: `chinese` `profiles` `config`
- [hiapi.ai](https://hiapi.ai) - Image / video / audio generation API gateway for developers and agents (author-related). Tags: `api` `media` `solo-founder`

## Hardware

- [groki-bot](https://github.com/JosssphZhou/groki-bot) - M5Stack CoreS3 desktop robot: firmware plus a voice / MCP gateway on your computer, with hand-off to Grok Bot; a reference for giving a bot a physical front end. Tags: `hardware` `mcp` `voice`
- [grok-gadgets](https://github.com/adidshaft/grok-gadgets) - SDKs and tools to connect hardware to Grok Bot; start with the simulator, then the ESP32-S3 OLED kit. The author labels it alpha. Tags: `hardware` `esp32` `sdk`

## Learning

- [awesome-grok-bot](https://github.com/ZeroPointRepo/awesome-grok-bot) - The English ecosystem index; check here for existing skills and tools before building your own. Tags: `awesome` `learning`
- [Recipe template](examples/_template.md) - Format to follow before submitting a recipe: scenario / input / steps / prompt / output / pitfalls. (Chinese) Tags: `template` `learning`

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) (Chinese). English issues and PRs are welcome.

## License

[MIT](LICENSE)
