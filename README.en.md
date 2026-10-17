# Awesome Grok Bot Playbooks

[![Stars](https://img.shields.io/github/stars/sit-in/awesome-grokbot-playbooks?style=flat)](https://github.com/sit-in/awesome-grokbot-playbooks/stargazers)
[![link-check](https://github.com/sit-in/awesome-grokbot-playbooks/actions/workflows/link-check.yml/badge.svg)](https://github.com/sit-in/awesome-grokbot-playbooks/actions/workflows/link-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

[中文](README.md) | **English** | [Roadmap](ROADMAP.md)

> Curated Grok Bot / multi-agent playbooks. Each entry = short review + link + tags. Recipes are copy-paste ready; ✅ means field-tested.

This repo is **not** a Grok Bot client and **not** affiliated with xAI. It only curates and reviews.

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
- [Learning](#learning)

---

## Official & SDK

- [xAI API Docs](https://docs.x.ai) - Official API docs; source of truth for models, pricing and tool calling. Tags: `official` `api` `docs`
- [xai-org on GitHub](https://github.com/xai-org) - Official open-source org: SDKs and open model weights. Tags: `official` `sdk`

## Self-hosted bots

- [XinyunOpenBot](https://github.com/dongpen-max/XinyunOpenBot) - Chinese-first open alternative, Simplified Chinese by default, supports OpenAI-compatible endpoints and API relays. Tags: `self-hosted` `chinese` `desktop`
- [OpenGrokBot](https://github.com/wolfqing/OpenGrokBot) - Self-hosted on OpenClaw, one machine per bot, bring your own model; the reference if you want data to stay local. Tags: `self-hosted` `openclaw` `byo-model`
- [open-grok-bot](https://github.com/Anil-matcha/open-grok-bot) - Local-first FastAPI + Next.js workspace; actions are deny-by-default with approvals and an audit trail. Tags: `self-hosted` `governance` `audit`

## Skills & Playbooks

- [grok-bot-templates](https://github.com/cobusgreyling/grok-bot-templates) - Engineering kit for templates: spec, Bot Ready score, team / skill / routine catalog. Check its structure before writing your own. Tags: `templates` `spec` `routine`
- [botskills](https://github.com/PramodDutta/botskills) - Paste-ready bot setups; each declares the one action it never takes without you. Good guardrail pattern. Tags: `skills` `guardrails`
- [grokbot-for-gtm](https://github.com/bcharleson/grokbot-for-gtm) - Full outbound GTM motion from list building and enrichment to reply handling. Tags: `playbook` `gtm` `outbound`

## Multi-bot teams

- [botteams](https://github.com/ellelion/botteams) - A whole team (bots + group chat + routines) in one markdown file; a good war-room orchestration example. Tags: `multi-bot` `team` `routine`
- [grok-bot-profiles](https://github.com/HAEGONG/grok-bot-profiles) - Spec / repro / PR / verify as four separate bots with explicit approval boundaries. Tags: `multi-bot` `dev` `guardrails`
- [overnight](https://github.com/Archive228/overnight) - Six-bot short-video crew with sourced material and a mandatory human review before publishing. Tags: `multi-bot` `content` `human-in-loop`

## Routines & Digests

- [Recipe: competitor radar routine](examples/competitor-radar.md) - Scheduled scraping of competitor pages that only notifies on real changes; filter timestamp noise first. (Chinese) Tags: `example` `routine` `radar`

## Chinese solo-founder

- [Recipe: one person, three roles](examples/one-person-three-roles.md) - Support + content + research bots hand off via files; the human reviews 30 minutes a day. Fictional example. (Chinese) Tags: `example` `solo-founder` `multi-bot`
- [hiapi.ai](https://hiapi.ai) - Image / video / audio generation API gateway for developers and agents (author-related). Tags: `api` `media` `solo-founder`

## Learning

- [awesome-grok-bot](https://github.com/ZeroPointRepo/awesome-grok-bot) - The English ecosystem index; check here for existing skills and tools before building your own. Tags: `awesome` `learning`
- [Recipe template](examples/_template.md) - Format to follow before submitting a recipe: scenario / input / steps / prompt / output / pitfalls. (Chinese) Tags: `template` `learning`

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) (Chinese). English issues and PRs are welcome.

## License

[MIT](LICENSE)
