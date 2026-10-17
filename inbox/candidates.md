# T1 X 雷达候选（待 Claude T5 核实）

- **日期**：2026-10-17（Asia/Shanghai）
- **窗口**：约近 30 天（2026-09-17 → 2026-10-17）
- **负责**：Grok
- **方法**：X `search_posts_all`（多查询）+ `gh search repos` / Web 交叉核验
- **红线**：无 API key / 营收 / 内部路径 / 隐私；未 star / fork
- **已在 README、不重复列为「新」**：ZeroPointRepo/awesome-grok-bot、XinyunOpenBot、OpenGrokBot、open-grok-bot、grok-bot-templates（cobusgreyling）、botskills、grokbot-for-gtm（bcharleson）、botteams、grok-bot-profiles、overnight、hiapi.ai

---

## 推荐入清单（优先）

| 名称 | 链接 | 一句理由 | 建议 README 节 | 标签 | 来源 |
|------|------|----------|----------------|------|------|
| grokbot-field-notes | https://github.com/unicodef1wn/grokbot-field-notes | xAI 团队 72h 直播里的规则 / playbook / 角色 / 失败日志；可直接丢 AGENTS.md。~603★，2026-09-18 | Skills & Playbooks | `playbook` `field-notes` `agents-md` | GitHub（星标交叉）；X 上同类「官方方法」帖多但多无仓 |
| lorca | https://github.com/egoist/lorca | 单人端到端加密 + agent 消息面，对标 Grok Bot / Muse / Dots。~310★，2026-09-18 | Self-hosted bots | `self-hosted` `messaging` `e2ee` | GitHub |
| xiryn | https://github.com/SouravBeraAkaSpeed/xiryn | 自托管个人 agent：每 agent 一台 Docker Linux 桌面，任意模型 + 加密 vault + Telegram。~185★，2026-10-11 | Self-hosted bots | `self-hosted` `docker` `telegram` | GitHub |
| noodle | https://github.com/pdparchitect/noodle | macOS 多 agent 桌面（Swift），topic 含 grokbot / hermes / muse。~175★，2026-09-04 | Multi-bot teams | `multi-bot` `macos` `desktop` | GitHub |
| DeepSeekBot | https://github.com/BotHarness/DeepSeekBot | 基于 DeepSeek Harness 的开源 GrokBot 平替：多 bot、记忆、权限、插件；中文 README。~127★，2026-09-16 | Self-hosted bots / Chinese solo-founder | `self-hosted` `chinese` `multi-bot` `deepseek` | GitHub + X 讨论（DeepSeekBot vs Rakazo） |
| AgentPeerChat | https://github.com/AgenticsWorks/AgentPeerChat | 免费自托管 agent 间消息，可连 Grok Bot / Muse / Dots。~124★，2026-10-02 | Multi-bot teams | `multi-bot` `messaging` `self-hosted` | GitHub |
| grok-bot-jev | https://github.com/Bodila51/grok-bot-jev | 把 TypeSafe Jev 接到 Grok Bot 作便宜决策层（usage gate + skill 模板）。~112★，2026-09-19 | Skills & Playbooks | `skill` `decision-layer` `cost` | GitHub |
| agent-cookie-sync | https://github.com/markfulton/agent-cookie-sync | Chrome MV3 + native host，把已登录站点会话给 Grok Bot / Muse，不贴密码。~88★，2026-09-23 | Skills & Playbooks | `chrome` `session` `playbook` | GitHub；与 X 上「本机 Chrome 驱动云端 Bot」玩法同向（@fankaishuoai 2026-10-17） |
| groki-bot | https://github.com/JosssphZhou/groki-bot | M5Stack 桌面机器人：固件 + 语音/MCP 网关，可交接给 Grok Bot。~65★，2026-09-23 | Learning / Official-adjacent hardware | `hardware` `mcp` `iot` | GitHub |
| guilds | https://github.com/CigaleAI/guilds | 开源 Grok bots 替代（团队/公会形态）。~61★，2026-10-09 | Self-hosted bots | `self-hosted` `multi-bot` | GitHub |
| templatesgrokbot.com | https://github.com/templatesgrokbot/templatesgrokbot.com | 3000+ 模板库 + MCP 接 catalog；按岗位搜。~34★，2026-09-17 | Skills & Playbooks | `templates` `marketplace` `mcp` | GitHub |
| grok-bots-for-deepseek-harness | https://github.com/brokep/grok-bots-for-deepseek-harness | 把 90 个 Grok Bot marketplace agent 打成 DeepSeek Harness 插件包。~29★，2026-10-15 | Skills & Playbooks | `templates` `deepseek` `port` | GitHub |
| grokbot-gtm-team | https://github.com/timscheuerai/grokbot-gtm-team | 13 个 GTM bot + 规则 + 一键建队 prompt；Grok 编排、Claude Code/Codex 干活。~29★，2026-10-14 | Multi-bot teams / Chinese solo-founder 可对照 | `gtm` `multi-bot` `claude-code` | GitHub；X 上大量「Claude Code 指挥 Grok Bot」玩法互相印证 |
| smfworks/grok-bot-templates | https://github.com/smfworks/grok-bot-templates | Michael Gannotti 合集：Video Studio / Builder Prime 等，官方 Add to Grok Bot 链。~3★，2026-10-09 | Skills & Playbooks | `templates` `marketplace` | **X**（@MichaelGannotti 2026-10-17）+ GitHub |
| grok-gadgets | https://github.com/adidshaft/grok-gadgets | 硬件 ↔ Grok Bot SDK/模拟器（ESP32-S3 OLED），MCP 网关。~2★，2026-10-05 | Learning | `hardware` `mcp` `esp32` | **X**（作者 @adidshaft + @grok 回复）+ GitHub |
| awesome-grok-bot-plugins | https://github.com/rdmgator12/awesome-grok-bot-plugins | 219 条 in-app Plugins 目录快照（2026-08-12），按类整理。 | Learning | `awesome` `plugins` `catalog` | **X** 提及（旧链）+ GitHub 核验 |
| eze-grokbot | https://github.com/eze-is/eze-grokbot | 公开的多 Bot 配置（每 Bot 一文件夹），中文向可抄结构。~15★，2026-10-10 | Chinese solo-founder / Multi-bot teams | `chinese` `profiles` `config` | GitHub |

---

## 玩法 / 文章向（无独立仓或仓弱，可作 Learning 短链）

| 名称 | 链接 | 一句理由 | 建议节 | 来源 |
|------|------|----------|--------|------|
| Claude Code ↔ Grok Bot 协作 | 例：https://x.com/heyrobinai/status/2111440703784169885 ；中文：https://x.com/LawrenceW_Zen/status/2110993612838441143 | 云端 Bot 装 Claude Code / 本机 Claude 编排 Bot；与本仓「Grok↔Claude」协作同构，值得 Learning 一条。 | Learning | **X**（多帖，2026-10-16–17） |
| 本机 Chrome 驱动云端 Grok Bot | https://x.com/fankaishuoai/status/2111484271198343195 | 本地 Agent 打开已登录 Chrome，用 Bot URL 对话/操控云端 Bot。 | Learning / Skills | **X**（2026-10-17） |
| How to Build Anything with Grok Bot | https://x.com/Av1dlive/status/2111125320590074017 | 高曝光「全课」文章卡（~62k 展示），可作入门 Learning，需 Claude 抽可复用步骤、去营销水。 | Learning | **X**（2026-10-16） |
| 爆款监控 Skill | https://x.com/aehyok/status/2109817788198158347 | 中文向：用 Grok Bot 从零做监控 Skill（高互动）。核实后或可摘要进 Routines。 | Routines & Digests | **X**（2026-10-13） |
| Plugin marketplace 开放提交 | https://x.com/AGTPinsights/status/2111456279545917951 | 开发者可提交 plugin/MCP 进 Grok Bot 市场——生态信号，不必单列仓。 | Official & SDK（备注） | **X**（2026-10-17） |

---

## 已有条目的更新信号（勿当新条目，供 T5 决定是否加一句）

| 条目 | 信号 | 来源 |
|------|------|------|
| OpenGrokBot | X 称 2.4：网页/Feed/邮件/日历触发自启；PDF/Excel 读写 | **X** @BuilderGuest 2026-10-17 |
| grok-bot-templates / botskills 等 | X 上「20 templates / SpaceXAI templates」营销帖极多，多数指向已有或 marketplace，勿重复堆 | **X** |

---

## Maybe / Skip（弱、空仓、归档、或偏题）

| 名称 | 链接 | 原因 | 来源 |
|------|------|------|------|
| b-nnett/grok-bot-0.18-reconstructed | https://github.com/b-nnett/grok-bot-0.18-reconstructed | ~3.5k★ 但 **已归档**；逆向研究向，合规/伦理需 Claude 把关，不宜当 playbook 主推 | GitHub / Web |
| tyonger-stack/GrokNode | https://github.com/tyonger-stack/GrokNode | 0.18 中文重建，研究向、星少；同归档仓风险 | GitHub |
| CogineBot | https://github.com/cogine-ai/CogineBot | WIP、8★；可观察 | GitHub + X 对比讨论 |
| milo / ngai-platform / OpenEveryAgentIDE / fakkelbot / liquid-gold-grok-bot | 各 GitHub | 描述对口但 0★、过新或空，先观察 | GitHub |
| AgwaB/grok-bot-audit | https://github.com/AgwaB/grok-bot-audit | 当日新建 fleet audit plugin，可跟 | GitHub |
| FreeToken-Bots 类 | X 文章 | 额度/免费模型接入，易踩 ToS；跳过 | **X** |
| 营收/agency「$1M MRR」类长文 | 多 X article | 营销向，不符合本仓宁缺毋滥 | **X** |
| yetone 相关 | — | 用户明确：仅自用参考，**不进 README / 不写本候选主表** | 约束 |

---

## 搜索备注 / 限制

1. X API：`since:` 运算符会被剥掉，已用 `start_time`/`end_time`；单次 `max_results` 上限 25，多查询分页未穷尽全部帖。
2. 大量高互动帖是 **X Article**（t.co → x.com/i/article/…），无 GitHub 链；只挑可复用玩法进「文章向」。
3. `gh search` 按 created≥2026-09-01 / stars 排序补漏；未对每个仓做 clone 实测（留给 T2/T5）。
4. 配额：本日 X reads 仍充足；无 fatal 错误。部分 WebFetch 对 X article 会 404，以搜索摘要 + `gh repo view` 为准。

---

## 给 Claude（T5）的合并建议

1. 优先核实 **field-notes / lorca / xiryn / noodle / DeepSeekBot / agent-cookie-sync / grokbot-gtm-team / smfworks templates**。
2. Learning 节可加一条「Claude Code ↔ Grok Bot」并链 1–2 篇高质量 X 帖（去营销话）。
3. OpenGrokBot 只更新短评一句（2.4 触发），不要新开条目。
4. 勿把 yetone、归档逆向仓、营收文写进 README。

---

## 夜班 2026-10-18 ~00:15（Asia/Shanghai）

- **窗口**：约 2026-10-14 → 10-17（UTC）近几日 X + `gh search`
- **负责**：Grok 夜班半小时雷达 #1
- **方法**：X `search_posts_all`（playbook/skill/routine/multi-bot + `url:github.com`）+ `gh api`/`gh search repos`
- **红线**：无 key / 营收 / 内部路径 / 隐私；未 star / fork；未改 README
- **去重**：相对当前 README + 上文 T1 表；个人参考仓不点名、不进公开主表

### 推荐入清单（夜班新）

| 名称 | 链接 | 一句理由 | 建议 README 节 | 标签 | ★/License | 来源 |
|------|------|----------|----------------|------|-----------|------|
| orca | https://github.com/stablyai/orca | fleet of agents（Grok Bot / Codex 等），桌面+手机+远程 runtime，用自有订阅跑编码 agent。群雷达【适合 Awesome】 | Multi-bot teams | `multi-bot` `fleet` `desktop` | ~95k / MIT | GitHub 雷达交叉 + gh |
| devspace | https://github.com/Waishnav/devspace | 轻量 MCP harness，描述点名 Grok Bot / Hermes / OpenClaw。群雷达【适合 Awesome】 | Self-hosted bots / Skills | `mcp` `harness` `self-hosted` | ~5.3k / MIT | GitHub 雷达交叉 + gh |
| agentrove | https://github.com/Mng-dev-ai/agentrove | 自托管多 agent 工作区，点名 Grok + Claude Code/Codex；星少但方向贴。群雷达【适合 Awesome】 | Multi-bot teams | `multi-bot` `workspace` `self-hosted` | ~338 / Apache-2.0 | GitHub 雷达交叉 + gh |
| last30days-skill | https://github.com/mvanhorn/last30days-skill | 跨 Reddit/X/YouTube/HN 的研究 skill；X 上被当成 Grok Bot「工程队」组件之一 | Skills & Playbooks | `skill` `research` `digest` | ~64k / MIT | **X** @0xCarnagee + gh |
| browserpaw | https://github.com/GoldenLoaf24h/browserpaw | 本机 Chrome 给 agent 用、不丢登录态；作者用 Cursor+Grok Bot 推进。与 cookie-sync 同向，可对照 | Skills & Playbooks | `chrome` `browser` `security` | ~35 / AGPL-3.0 | **X** + gh |
| iwork_mcp | https://github.com/reichenbach/iwork_mcp | 117 个 Numbers/Pages/Keynote 工具，已做成 Grok Bot plugin 提市场 | Skills & Playbooks | `mcp` `macos` `iwork` | ~37 / 无 License | **X** @realcoachmatt23 + gh |
| grokbot-notch | https://github.com/robzilla1738/grokbot-notch | macOS Notch 伴侣：桌面 Grok Bot + 实时语音；硬件/桌面入口向 | Hardware | `macos` `voice` `desktop` | ~7 / MIT | gh search（created≥10-16） |
| grokbot-hermes-bridge | https://github.com/jamesonedge/grokbot-hermes-bridge | Tailscale + webhook：Grok Bot ↔ 自托管 Hermes，额度耗尽时的备份编排 | Skills / Multi-bot | `bridge` `hermes` `webhook` | ~3 / 无 License | **X** @JamesOnEdge |
| twilio-grok-voice-bridge | https://github.com/jeffhuber/twilio-grok-voice-bridge | Twilio Media Streams ↔ Grok Voice，给 Bot 外呼能力 | Skills & Playbooks | `voice` `twilio` `outbound` | ~2 / MIT | **X** @jhuber |
| Claude2GrokBot | https://github.com/Parsiffall1/Claude2GrokBot | Claude 把任务交给 Grok Bot（可唤醒）并回传；CF Workers + Durable Objects MCP | Skills / Multi-bot | `claude` `bridge` `mcp` | ~1 / MIT | gh search（当日新建） |
| grok-bot-wechat | https://github.com/bogao6769-netizen/grok-bot-wechat | 中文：微信 ClawBot → Grok Bot（webhook Routine + 本地转发）Cursor 配方 | Chinese solo-founder | `chinese` `wechat` `routine` | ~1 / MIT | gh search |
| grok-cc | https://github.com/codebyelvis/grok-cc | 经 Orca 把本机 Mac 开发任务委派给 Grok Bot 上的 Claude Code | Skills / Multi-bot | `claude-code` `orca` `mac` | ~2 / 未明确 | gh search |

### 玩法 / 产品信号（无强仓或仓弱，Learning / Routines 短链）

| 名称 | 链接 | 一句理由 | 建议节 | 来源 |
|------|------|----------|--------|------|
| 邮箱 +别名分流 Routine | https://x.com/JJKKKK92/status/2111435631981195618 ；英文说明例 https://x.com/grokbotusecases/status/2110514228193079634 | `+invoice` / `+alerts` / `+reading` 各触发一条流水线；产品新能力，值得 Routines 一条短评 | Routines & Digests | **X**（多帖，2026-10-14–17） |
| Bot Library 找旧文件 | https://x.com/SuddenlyJon/status/2111490547017744886 | 信息栏 Library：Today / This week / Older 分组找回几天前文件——实用小技巧 | Learning | **X** 2026-10-17 |
| pstack / poteto-mode | Cursor/Grok Bot 插件生态；移植例 https://github.com/backnotprop/pstack 、https://github.com/michael-denyer/pstack-claude | SpaceXAI 工程师 Lauren Tan 的工程 skill 栈；Grok Bot 可装插件。官方仓名易变，先 Learning 链移植仓+使用说明，勿当「官方仓」 | Skills & Playbooks / Learning | **X** 高热 + gh |
| X 必读合集 24 篇 | https://x.com/0xlangeai/status/2111396742264742034 | 中文向 9 类 24 篇高阅读合集（~24k 展示）；可作 Learning 索引，需抽可复用步骤、去营销 | Learning | **X** 2026-10-17 |
| Bots 进 grok.com / App | https://x.com/raul_g/status/2111490586087756027 | Bot 能力进主 App，与独立 Grok Bot App 能力接近——产品形态信号 | Official（备注） | **X** 2026-10-17 |
| 1 路由 + 4 专家 | https://x.com/YAYACA11/status/2111353772131934334 | webhook/Slack/GitHub/邮件打到同一路由；强调「没活闭嘴」控成本——与 war-room 同构 | Multi-bot / Learning | **X** 2026-10-17 |
| Claude↔Grok 桥（续） | 例：https://x.com/danmercede/status/2110769669456187797 ；中文 https://x.com/LawrenceW_Zen/status/2110993612838441143 | webhook 400 / 无官方 API，社区用 Python 桥或 4 次 API 调用；与本仓协作同构。上轮已列，夜班仅补新帖 | Learning | **X** |

### Maybe / Skip（夜班）

| 名称 | 链接 | 原因 |
|------|------|------|
| AgwaB/grok-bot-audit | https://github.com/AgwaB/grok-bot-audit | 当日新建 0★ fleet audit plugin，续观（T1 Maybe 已有） |
| brokep/grok-bots-for-deepseek-harness | 同上文 | Claude T5 已拒：无 License + marketplace 重打包版权疑 |
| h100envy/crawl-hive | — | memecoin 向，偏题 |
| danielfebrero/Grok-Bot-app（MCP/box monitor） | — | 0★、无 License、偏逆向监控，合规风险 |
| oh-my-grokbot / t3bot / 大量 0★ 新仓 | — | 过早，先观察 |
| 华为云代金券 / AK·SK 帖 | — | 要密钥与羊毛，跳过 |
| 个人参考向仓 | — | 不点名、不进公开 README（按涛哥约束） |

### 给 Claude loop 的合并建议

1. **优先核实**：orca、devspace、agentrove、last30days-skill（星高但要确认「Grok Bot 可用性」表述是否准确）、browserpaw。
2. **谨慎**：无 License 的 iwork_mcp / hermes-bridge；星极少的 wechat / Claude2GrokBot / grok-cc——可 Learning 短链或先观。
3. **玩法向**：邮箱 +别名、Library tip、pstack（标非官方移植）值得 Learning/Routines 短链；勿把营收/额度营销文写进 README。
4. 我未改 README；夜班会持续到约 **03:00 Asia/Shanghai**，每约 30 分钟追加一节（无新增则静默）。
