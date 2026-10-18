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
| 某个人参考仓 | — | 用户明确：仅自用参考，**不进 README / 不写本候选主表** | 约束 |

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
4. 勿把某个人参考仓、归档逆向仓、营收文写进 README。

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

## 夜班 2026-10-18 ~00:41（Asia/Shanghai）

- **窗口**：相对夜班 #1（~00:15）之后约半小时；X 近几小时 + `gh search` created≥2026-10-15
- **负责**：Grok 夜班半小时雷达 #2
- **方法**：X `search_posts_all` / `get_posts_by_ids` + `gh api`/`gh search repos`
- **红线**：无 key / 营收 / 内部路径 / 隐私；未 star / fork；未改 README
- **去重**：相对 README + 上文 T1 / 夜班 #1；个人参考仓不点名

### 推荐入清单（夜班新）

| 名称 | 链接 | 一句理由 | 建议 README 节 | 标签 | ★/License | 来源 |
|------|------|----------|----------------|------|-----------|------|
| grok-bot-t3-code-superpowers | https://github.com/gavasques/grok-bot-t3-code-superpowers | Skill + 脚本：经 MCP 让 Grok Bot 远程驱动 T3 Code（Claude/Codex/Grok 线程）。安装步骤帖齐全 | Skills & Playbooks | `skill` `mcp` `t3-code` | 0 / MIT | **X** @Ga_Vasques + gh |
| grokbot-relay | https://github.com/devicki/grokbot-relay | 本机/服务器 Cursor BDK 中继 → Grok Bot agents（给 Claude Code/Cursor 的 MCP）。与本仓协作同构 | Skills / Multi-bot | `relay` `mcp` `claude-code` | 0 / MIT | gh search |
| Badland Line | https://github.com/Badland-AI/grokbot | 任意手机 SMS 遥控 Grok Bot（remote MCP + skill） | Skills & Playbooks | `sms` `mcp` `mobile` | 0 / MIT | gh search |
| grokbot-plugins（keyless） | https://github.com/punk5322/grokbot-plugins | 五个免 key 的托管 remote MCP 插件包，可当「零配置插件」样板 | Skills & Playbooks | `plugins` `mcp` `keyless` | 0 / MIT | gh search |
| varosity grok-bot studio | https://github.com/varosity-ai/grok-bot | 经 Varosity remote MCP 给 Bot 接 60+ 视频/图/语音/音乐模型 | Skills & Playbooks | `mcp` `media` `studio` | 0 / MIT | gh search |
| siri-grokbot | https://github.com/enzoenrico/siri-grokbot | iPhone / CarPlay Siri intents 接 Grok Bot | Hardware / Skills | `siri` `ios` `carplay` | 0 / MIT | gh search |
| oh-my-grokbot | https://github.com/liziye627-design/oh-my-grokbot | 「能力分发与集成核心」；#1 Maybe 里有，现 ~4★ MIT，可再核 README 是否真可用 | Skills / Self-hosted | `core` `integration` | ~4 / MIT | gh（相对 #1 升星） |

### 玩法 / 产品信号（无强仓或仓弱）

| 名称 | 链接 | 一句理由 | 建议节 | 来源 |
|------|------|----------|--------|------|
| 家庭多 Bot 群「日常饮食」 | https://x.com/turingou/status/2111483937822474526 | 中文高互动：订餐/家务等职责管家进同一群；与 war-room 同构，适合 Learning 或 `examples/` 配方灵感 | Multi-bot / Learning | **X** @turingou（~5.5k 展示 / 37❤） |
| HireQuay A2A | https://app.hirequay.com ；帖 https://x.com/KoetaInc/status/2111494967994536143 | Claude ↔ Grok Bot 交接上下文/技能，人审回复；免费 beta。无开源仓，当 Multi-bot 产品对照 | Multi-bot（备注） | **X** ~5.5k 展示 |
| BlackOps Comms | https://www.blackopscenter.com/blog/agent-comms ；帖 https://x.com/BlackOpsTools/status/2111495147359723599 | 多 agent 同笔记轮流、签名、点名下一棒，默认 10 条停；Claude+Grok Bot webhook | Multi-bot / Learning | **X** |
| 事件触发 vs 定时轮询 | https://x.com/Mateq007/status/2111489541450141833 | 邮件/Slack/GitHub/webhook 唤醒，少空跑——与邮箱+别名、本仓 X 雷达「无信号不推」同向 | Routines | **X** |
| Bland 电话 MCP | https://docs.bland.ai/integrations/mcp/grok-bot | 官方 MCP：Bot 自助开美号、通话/短信；第三方非 xAI 背书。可作 Outbound 配方外链 | Skills / Official-adjacent | **X** @grok 多次确认 + docs |
| Spam-Call Scrubber 技能 | https://x.ai/bot/fUj6TYhiW_cjtzWvbsFgz | 市场第三方免费技能：data-broker 退订；隐私敏感，仅作「可分享技能」样例，勿当主推 | Learning（备注隐私） | **X** 刷屏 |

### Maybe / Skip（夜班 #2）

| 名称 | 链接 | 原因 |
|------|------|------|
| robbin/x-news | https://github.com/robbin/x-news | 范凯说AI 新闻房背后仓；4★ **无 License**；玩法已有 Chrome/新闻房 X 帖，仓本身先观 |
| WeirdBrains/grokbot-tui | https://github.com/WeirdBrains/grokbot-tui | 0★ TUI，描述过短 |
| sunny0826/grokbot-smartring | https://github.com/sunny0826/grokbot-smartring | 动画/硬件 demo，License NOASSERTION，偏展示 |
| ConverseNation/mybusybots-status | — | 0★ 无 License 监控页 |
| pstack / poteto-mode 再刷 | — | #1 已列；Claude loop #2 已拒（GitHub 仅 Claude/Codex 移植） |
| Teach-a-Task 警示帖 | 多 | README 已有 teach-a-task 配方，勿重复堆 |
| 营收/agency/$1M 类 | 多 | 跳过 |

### 给 Claude loop 的合并建议

1. **优先看**：t3-code-superpowers、grokbot-relay（和本仓 Claude↔Grok 同构）、家庭多 Bot 群帖（适合写成 examples 灵感，不必挂仓）。
2. **谨慎**：其余多为 0★ 当日/近两日仓——有 MIT 可进 Maybe 观察表，勿急收 README；HireQuay / BlackOps 无开源仓，只 Learning 短链。
3. Bland / Spam Scrubber：第三方 + 隐私，短评须写清风险。
4. 未改 README；脏树里有 `.collab/loop-state.md`（非我改），本提交只动 `inbox/candidates.md` + `.collab/to-claude.md`。

## 夜班 2026-10-18 ~01:11（Asia/Shanghai）

- **窗口**：相对夜班 #2（~00:41）之后约半小时；X 近几小时（`start_time`≈2026-10-17T12:00:00Z）
- **负责**：Grok 夜班半小时雷达 #3
- **方法**：X `search_posts_all` / `get_posts_by_ids`（多查询；github.com 向近几小时几乎空）
- **红线**：无 key / 营收 / 内部路径 / 隐私；未 star / fork；未改 README
- **去重**：相对 README + 上文 T1 / 夜班 #1–#2；个人参考仓不点名

### 推荐入清单（夜班新）

（本轮无强新仓；多为可复用玩法 / 模板 / 文章。）

### 玩法 / 产品信号（无强仓或仓弱，Learning / Routines 短链）

| 名称 | 链接 | 一句理由 | 建议节 | 来源 |
|------|------|----------|--------|------|
| T3→Grok Bot ask-back | https://x.com/firestormodk/status/2111503562366984662 | Codex/Claude 在 T3 用 `list_bots` / `ask_bot` / `notify_bot` CLI 回问 Grok Bot，webhook Routine 路由唤醒；人只做最后兜底。与已列 t3-code-superpowers（Bot 驱动 T3）互补 | Multi-bot / Skills | **X** @firestormodk |
| CNR Grok Bot 指南+免费模板 | https://cnrcode.com/guides/ ；帖 https://x.com/CNR_Consulting/status/2111494385946734616 | 7 篇英文 how-to（Routines/Skills/额度）+ 可下载 skill；含 5 套小生意 copy-paste Bot 设定 | Skills / Learning | **X** @CNR_Consulting |
| CoS 额度效率审查 prompt | https://x.com/Michael_Fenech_/status/2111478843202818102 | 可粘贴给首席 Bot：按频率/结果/触发/变更检测/价值给 Routine 打 KEEP/SLOW/EVENT/CHANGE/RETIRE，估用量且先不改。~1.6k 展示 | Routines | **X** @Michael_Fenech_ |
| Routine 色历 + 额度重置线 | https://x.com/luisbarragan/status/2111501299938398306 | 让首席 Bot 画「每条 Routine×Bot」色历并标 usage reset，临近额度先停可缓跑的 | Routines | **X** @luisbarragan |
| Bot Budget Guard（市场技能） | https://x.ai/bot/CFNwEKsM5nPPRQhPVZMCD ；帖 https://x.com/MikeysMolecules/status/2111480053456413149 | 只读：预测周额度、安全日 burn、bot/routine 红黄绿；第三方市场技能，短评须写清非官方 | Routines / Learning | **X** |
| 晨晚交接 Routine 提示 | https://x.com/ScottyBeamIO/status/2111485286785941852 | 早晨：日历/邮件/项目→优先级与是否需批准；晚间：选≤3 个有明确成品的任务过夜。~900 展示 / 44❤ | Routines | **X** @ScottyBeamIO |
| 一夜从零 + rug filter 文 | https://x.com/0xboan/status/2111502544904012233 （文章） | 「Grok Bot from zero in one night」全量搭设 + 可复制过滤；Learning 短链，注意标题偏加密语境 | Learning | **X** @0xboan |
| Put Grok to Work 文 | https://x.com/tonysimons/status/2111503386961154150 （文章） | 「Elon Gave Grok a Computer…」上手用法长文；Learning 索引 | Learning | **X** @tonysimons |
| Codex CLI MCP + OpenRouter | https://x.com/lgtwet/status/2111496186167164993 | 中文：服务器装 Codex CLI，做 MCP 给 Grok Bot，挂 OpenRouter 调免费模型。无公开仓，先 Learning/Skills 短链 | Skills / Multi-bot | **X** @lgtwet |
| Orca 编排器中文教程 | https://x.com/xiaoanlab/status/2111457972660605344 （文章） | 多 agent 并行 worktree + 配额避坑；README 已有 orca，可作 Learning 中文旁注 | Learning | **X** @xiaoanlab |
| CoS 需要 Company Brain | https://x.com/RemingtonBegg/status/2111469626710176030 （文章） | 给首席 Bot 挂公司知识脑的写法；与作战室文件交接同向 | Learning | **X** @RemingtonBegg |

### Maybe / Skip（夜班 #3）

| 名称 | 链接 | 原因 |
|------|------|------|
| smfworks Video Studio 再推 | https://github.com/smfworks/grok-bot-templates | T1 / 上文已列 |
| 邮箱 +别名 / 事件触发 | 多帖 | 夜班 #1–#2 已列 |
| BlackOps / BenENewton 再刷 | https://x.com/BenENewton/status/2111491392937570344 | #2 已有 BlackOps Comms |
| Teach-a-Task / Spam Scrubber | 多 | README 或上文已有 |
| SpaceXAI 10 bots / Elon 回复增长文 | 多 | 营销或增长诱饵，跳过 |
| 营收 / $10k weekend | 多 | 跳过 |

### 给 Claude loop 的合并建议

1. **优先看**：T3 ask-back（@firestormodk）— 与本仓 Claude↔Grok 协作同构；CoS 效率审查 prompt（可放 `examples/` 灵感）。
2. **次优**：CNR 免费模板页（核实可下载 skill 是否可复用、有无 paywall）。
3. Budget Guard / Spam Scrubber 同类：第三方市场技能，短评写清风险，勿当官方。
4. 文章向（0xboan / tonysimons / RemingtonBegg / xiaoanlab）：Learning 短链即可，勿急收 README。
5. 未改 README；本提交只动 `inbox/candidates.md` + `.collab/to-claude.md`。

## 夜班 2026-10-18 ~01:48（Asia/Shanghai）

- **窗口**：相对夜班 #3（~01:11）之后约半小时；X 近几小时（`start_time`≈2026-10-17T16:00:00Z 起）
- **负责**：Grok 夜班半小时雷达 #4
- **方法**：X `search_posts_all` / `get_posts_by_ids` + `gh api` 核实仓
- **红线**：无 key / 营收 / 内部路径 / 隐私；未 star / fork；未改 README
- **去重**：相对 README + 上文 T1 / 夜班 #1–#3；个人参考仓不点名

### 推荐入清单（夜班新）

| 名称 | 链接 | 一句理由 | 建议节 | 星 / License | 来源 |
|------|------|----------|--------|--------------|------|
| reason-network | https://github.com/reason-machines/reason-network | Grok Bot / Muse ↔ Claude Code / Codex / Cursor 等 P2P 互问互派；引擎 Apache-2.0；产品页注明 CLI 本身非开源。配套站点 https://reasonmachines.com/network ；MCP/插件仓 https://github.com/reason-machines/reason-plugins（4★ MIT，简述面向 Claude/Codex/MCP，Grok Bot 可经 Cursor 市场装） | Multi-bot teams | ~184 / Apache-2.0 | **X** @reasonmachines 高热帖（~44万展示）+ gh |
| root-agent-skill-framework | https://github.com/MrBekoX/root-agent-skill-framework | Root Agent v0.2.0：按目标动态扩缩 Bot 队、委派 domain Lead、stall/交付证明、取消清理；市场安装页 https://x.ai/bot/1pTKHkJIEgxD9MjlPYE4P | Multi-bot / Skills | 2 / MIT | **X** @mrbeko_ + gh（刚 push） |

### 玩法 / 产品信号（无强仓或仓弱，Learning / Routines 短链）

| 名称 | 链接 | 一句理由 | 建议节 | 来源 |
|------|------|----------|--------|------|
| 额度一周烧完·8 步止血 | https://x.com/GrokBotRadar/status/2111513393538732162 （引用长文 https://x.com/i/article/2105065351595847680 ） | 可操作 checklist：放慢最快 Routine、仅工作日时段、把 Routine 挪出聊天 Bot、Duplicate 清上下文、prompt 指 skill 且无新则静默、优先连接器、规则活脚本化、测试时关 on-demand。**直接喂** Claude 已请的 `examples/routine-budget.md` | Routines / examples | **X** @GrokBotRadar |
| 一人公司 12 步配方文 | https://x.com/maestrooth/status/2111505949131227180 | 可粘贴：职能地图→三人岗描述→House Rules→干跑→存 skill→Auto-review→无人值守句→晨报→30 日审计；与本仓「一人三岗」同向，适合 Learning / 对照 `examples/` | Chinese solo-founder / Learning | **X** @maestrooth（~213 展示 / 12❤ / 11🔖） |
| 通勤 Granola→Slack Routine | https://x.com/steitiyeh/status/2111506107487154565 | 开车回家语音过会议笔记：加行动项 / 写纪要发 Slack / 设跟进提醒——「停车前 inbox zero」 | Routines | **X** @steitiyeh |
| 共享云电脑 vs 分隔离 | https://x.com/ianjcam/status/2111510052872106374 | Grok Bot 全员共一台云电脑（session/文件/登录共享）；对照 Hermes 每 Bot 独立 profile。作战室安全边界对照 | Learning / Multi-bot | **X** @ianjcam |
| Bot 是技能镜像 | https://x.com/shaivpidadi/status/2111505997902852496 | 「Bot 只会你允许的技能」；附自审 prompt 找自己否决过的 GTM 建议。Learning 软链 | Learning | **X** @shaivpidadi |

### Maybe / Skip（夜班 #4）

| 名称 | 链接 | 原因 |
|------|------|------|
| 24 篇合集再转发 | https://x.com/will_lion1/status/2111505199546487190 | 夜班 #1 已有 0xlangeai 原帖 |
| Spam-Call Scrubber 再刷 | 多 | #2/#3 已 Skip |
| SpaceXAI 9-bot / $500K / $1M | 多 | 营收/营销，跳过 |
| CrawlHive | https://github.com/...（X 帖） | 叙事狙击/加密语境，偏离本仓 |
| morrimoz Claude+Codex pipeline | https://x.com/morrimoz/status/2111511751615553906 | 愿分享但无公开仓/配方文 |
| ann0nip 要监控仪表盘 | https://x.com/ann0nip/status/2111510788225556601 | 需求帖非配方 |
| 华为云 AK/SK 羊毛 | 多 | 要密钥，红线跳过 |
| 邮箱 +别名 / Teach-a-Task | 多 | 上文已列 |

### 给 Claude loop 的合并建议

1. **优先看**：**reason-network**（~184★ Apache-2.0，过你们 ≥10★ 门槛）— Multi-bot 桥接刚需；短评须写清「引擎开源、Reason CLI 本身非开源」。
2. **额度配方**：本轮 GrokBotRadar 8 步 + #3 CoS/色历/Budget Guard → 合成 `examples/routine-budget.md`（你 loop #4 已点名）；提示词用自己的话重写。
3. **一人公司文**：maestrooth 12 步与 `examples/one-person-three-roles.md` 对照，可抽 House Rules / 晨报进 Learning 或 examples 补丁，勿整篇照抄。
4. **Root Agent**：2★ 当日活跃，先观察表；≥10★ 或建仓≥7 天再推 README。
5. 未改 README；脏树里有 `.collab/loop-state.md`（Claude loop 本地），本提交只动 `inbox/candidates.md` + `.collab/to-claude.md`。

## 夜班 2026-10-18 ~02:10（Asia/Shanghai）

- **窗口**：相对夜班 #4（~01:48）之后约半小时；X `start_time`≈2026-10-17T12:00:00Z（主扫）+ 16:00/16:30Z 收紧窗
- **负责**：Grok 夜班半小时雷达 #5
- **方法**：X `search_posts_all` / `get_posts_by_ids` + `gh api` 核实仓
- **红线**：无 key / 营收 / 内部路径 / 隐私；未 star / fork；未改 README
- **去重**：相对 README + 上文 T1 / 夜班 #1–#4；个人参考仓不点名

### 推荐入清单（夜班新）

| 名称 | 链接 | 一句理由 | 建议 README 节 | 标签 | ★/License | 来源 |
|------|------|----------|----------------|------|-----------|------|
| github-grok-bot-webhook-forwarder | https://github.com/doitian/github-grok-bot-webhook-forwarder | Cloudflare Worker：GitHub webhook → Grok Bot routine webhook；HMAC 校验、路径路由、失败可在 GitHub Recent Deliveries 重投。当日新建 | Routines & Digests / Skills | `webhook` `github` `cloudflare` | 0 / MPL-2.0 | **X** @doitian https://x.com/doitian/status/2111514792834027811 + gh |

### 玩法 / 产品信号（无强仓或仓弱，Learning / Routines 短链）

| 名称 | 链接 | 一句理由 | 建议节 | 来源 |
|------|------|----------|--------|------|
| 40 条可复制 Custom rules | https://x.com/unicodef1wn/status/2111518189511147682 | 安全文档提炼：✓ allow / ? ask first；? 冲突优先、审批约 10 分钟过期、密码/2FA/付款永不自动。与 field-notes 同作者，可作 Skills/护栏短链（帖末有营销 CTA，摘规则即可） | Skills & Playbooks / Learning | **X** @unicodef1wn |
| 24/7 DM Assistant 配方文 | https://x.com/KanikaBK/status/2111516185825268054 （文章 https://x.com/i/article/2111509806620266496 ） | 全量 setup+prompts：Bot 扫 DM、分流、只出草稿等人批。与出海客服「只出草稿」同向 | Routines / Chinese solo-founder | **X** @KanikaBK |
| Grok Bot in Practice 文 | https://x.com/shancha103/status/2111518339667529836 （文章 https://x.com/i/article/2111518270276956160 ） | 中文向「可复用 AI 工作流」实践指南；Learning 短链，需抽可复用步骤 | Learning | **X** @shancha103 |

### Maybe / Skip（夜班 #5）

| 名称 | 链接 | 原因 |
|------|------|------|
| tonysimons field guide 再推 | https://x.com/tonysimons/status/2111518353710010776 | 夜班 #3 已有原文章帖 |
| GrokBotRadar / maestrooth / Granola | 多 | #4 已列 |
| firestormodk ask-back | 已列 | #3 |
| SpaceXAI 9-bot / $1M | https://x.com/leopardracer/status/2111508903229796561 | 营收营销，跳过 |
| PennyLedgerr Elon reply 增长文 | https://x.com/PennyLedgerr/status/2111489661172437341 | 增长诱饵，跳过 |
| Spam Scrubber / 事件触发再刷 | 多 | 上文已 Skip/列 |
| Pebble→Grok Bot webhook | https://x.com/aku11i/status/2111500593995100480 | 硬件玩具向、无仓 |
| 加密交易 multi-agent 桌 | grok 回复串 | 金融签名/资金向，偏离本仓 |

### 给 Claude loop 的合并建议

1. **优先核实**：**doitian/github-grok-bot-webhook-forwarder**（MPL-2.0，配方完整）— 事件触发 Routine 的现成 Worker；短评可链「少空跑」玩法。0★ 当日仓，可先 Learning/Routines 短链或观察表。
2. **护栏**：unicode 40 rules 值得 Skills 短链或并入 field-notes 旁注；勿抄帖末「赚钱」CTA。
3. **DM Assistant / Practice 文**：Learning 或对照 `examples/outbound-support.md`；抽步骤勿整篇照抄。
4. 未改 README；本提交只动 `inbox/candidates.md` + `.collab/to-claude.md`。


## 夜班 2026-10-18 ~02:46（Asia/Shanghai）

- **窗口**：相对夜班 #5（~02:10）之后约半小时；X `start_time`≈2026-10-17T17:00:00Z（主扫）+ 17:30Z 收紧
- **负责**：Grok 夜班半小时雷达 #6（本周日夜班末轮，cron 窗止于 02:xx）
- **方法**：X `search_posts_all` / `get_posts_by_ids` + HF/gh 快核
- **红线**：无 key / 营收 / 内部路径 / 隐私；未 star / fork；未改 README
- **去重**：相对 README + 上文 T1 / 夜班 #1–#5；个人参考仓不点名

### 推荐入清单（夜班新）

| 名称 | 链接 | 一句理由 | 建议 README 节 | 标签 | ★/License | 来源 |
|------|------|----------|----------------|------|-----------|------|
| （本轮无新强仓） | — | gh 搜索当日新仓仍仅 doitian webhook（#5 已列）；推送窗内无第二仓 | — | — | — | gh |

### 玩法 / 产品信号（无强仓或仓弱，Learning / Routines 短链）

| 名称 | 链接 | 一句理由 | 建议节 | 来源 |
|------|------|----------|--------|------|
| 额度夜班·Meter 全配方文 | https://x.com/Aannzzo/status/2111525291944460293 （文章 https://x.com/i/article/2111478730799325184 ） | 「醒来 96 条过期审批 + 账单暴涨」场景的完整 playbook，与 #4 GrokBotRadar 8 步同向，可并入 `examples/routine-budget.md` 材料 | Routines / examples | **X** @Aannzzo |
| Proactive Suggestions | https://x.com/AndrewCurran_/status/2111522784438587767 | Bot 主动 DM「找事做」：heartbeat 类产品信号；用户触发→周期→主动。Learning 短链（~4.5k 展示） | Learning | **X** @AndrewCurran_ |
| 中文去 AI 味 LoRA（Grok Bot 训） | https://huggingface.co/Frankfika/deai-flavor-qwen2.5-1.5b-lora （帖 https://x.com/FrankFika/status/2111524182630760566 ） | Mac 上用 Grok Bot 跑通数据→训练→上传；中文内容向案例。HF 权重非 playbook 仓，Learning / Chinese solo 短链 | Learning / Chinese solo-founder | **X** @FrankFika + HF |
| OpenClaw VPS + Slack 自托管对照 | https://x.com/kyle_e_walker/status/2111528433586946095 | 不用订阅：OpenClaw 多 agent 挂自有 VPS、Slack app 互通、Tailscale 审批进 Mac。无公开配方仓，作战室/Self-hosted 对照信号 | Learning / Self-hosted | **X** @kyle_e_walker |

### Maybe / Skip（夜班 #6）

| 名称 | 链接 | 原因 |
|------|------|------|
| /hibernate + eggbot 截图 | https://x.com/edtadros/status/2111529344044826899 | 额度止血思路可取，但依赖 marketplace「dr eggbot」截图 prompt，无仓无全文 |
| Side Hustle CEO 案例 | https://x.com/thebtchodlr/status/2111525358809845785 | AlexFinn 市场 Bot 使用故事，无可复制开源配方 |
| SpaceXAI PDF / $1M 9-bot | 多 | 营收营销，跳过 |
| Spam-Call Scrubber / doitian / unicode / Kanika / shancha / 0xboan | 多 | #5 及更早已列 |
| 加密钱包扫描 / invite code | 多 | 金融/营销，偏离本仓 |

### 给 Claude loop 的合并建议

1. **额度文合并**：Aannzzo Meter playbook + #4/#5 Radar 8 步 → 继续喂 `examples/routine-budget.md`；自写短评，勿整篇照抄。
2. **产品信号**：Proactive Suggestions 可 Learning 一行；注意「主动找事」会烧额度，宜与 budget 护栏同页。
3. **FrankFika**：HF LoRA 作「Grok Bot 跑通训练管线」中文案例短链即可，勿当 Skills 主条目。
4. **kyle OpenClaw**：无仓则不上 README；可对照已收录 OpenGrokBot / lorca 写一句差异。
5. 未改 README；本提交只动 `inbox/candidates.md` + `.collab/to-claude.md`。

## 白天 2026-10-18 ~07:45（Asia/Shanghai）

- **窗口**：夜班 #6（~02:46）之后至周日上午；Reason Network 已搁置，**仅 git 协作**
- **负责**：Grok 白天玩法雷达（即时一轮）
- **方法**：X `search_posts_all`（近 48h）+ `gh api repos/...` 核实 + Web 检索；相对 README + `inbox/candidates.md` 全表去重
- **红线**：无 key / 营收 / 内部路径 / 隐私；未 star / fork；未改 README；个人参考不点名
- **卫生**：本轮已将 Grok 侧文件（LOOP.md / to-claude.md / candidates.md）中的个人名点名改为「个人参考」（不改 Claude 留言）

### 推荐入清单（白天新）

| 名称 | 链接 | 一句理由 | 建议 README 节 | 标签 | ★/License | 来源 |
|------|------|----------|----------------|------|-----------|------|
| grokbot-imessage-skill | https://github.com/jeffhuber/grokbot-imessage-skill | macOS 本地 launchd 桥：读/分拣/搜/发 iMessage，隐私优先、无云同步 | Skills & Playbooks | `imessage` `macos` `skill` | ~36 / MIT | **GitHub** + awesome 生态交叉 |
| grokbot-sdk | https://github.com/adam91holt/grokbot-sdk | 运行中 Grok Bot host 的 TypeScript SDK（typed gateway + sand-data 读盘） | Official & SDK | `sdk` `typescript` | ~20 / MIT | **GitHub** |
| grok-bot-skill | https://github.com/adamanz/grok-bot-skill | Cursor/Agent Skill：终端聊 teammates、创建新 Bot（用本地桌面会话，不拷 token） | Skills & Playbooks | `cli` `skill` `cursor` | ~11 / MIT | **GitHub** |
| lauren-poteto-rules | https://github.com/unicodef1wn/lauren-poteto-rules | 可信 coding-agent 工作流工程规则（与 field-notes 同作者线，可作 AGENTS 配套） | Learning / Skills | `agents.md` `rules` | ~90 / MIT | **GitHub** |
| grok-bot-delegation | https://github.com/agent-skills-lab/grok-bot-delegation | Claude Code skill：名册/简报格式/skills·routines/审批边界 + 双语模板；与本仓 Claude↔Grok 协作同构 | Skills & Playbooks | `claude-code` `delegation` `bilingual` | ~1 / 无 SPDX | **GitHub** + Web |

### 玩法 / 产品信号（无强仓或仓弱，Learning / Routines 短链）

| 名称 | 链接 | 一句理由 | 建议节 | 来源 |
|------|------|----------|--------|------|
| 任务→Skill→再 Routine 阶梯 | https://x.com/joeapfelbaum/status/2111594967114113329 | 「先手工跑通再存 skill，最后才上 schedule」——与本仓 teach-a-task / 脱敏配方同向 | Skills / examples | **X** @joeapfelbaum |
| 一职一 Bot + never-list + 周审 skill | https://x.com/grovr_au/status/2111594375260111249 | 每个 Bot 只一事；「从不做」清单指向其他 Bot；专 Bot 每周扫过期 skill | Multi-bot / Skills | **X** @grovr_au |
| Import Bot（Hermes→Grok 迁移） | https://x.ai/bot/marketplace/bots/import-bot （帖 https://x.com/joshuaday/status/2111600012929192086 ） | 官方 marketplace Import Bot：把 Hermes 等 setup 迁入；装后核对 private skills 是否到齐 | Learning / Official | **X** @joshuaday + marketplace |
| Claude Code→Grok Bot 四次 API（跳过 webhook） | https://x.com/mikan77_aoi/status/2111043148088816045 | webhook 400 时用 stdlib Python 四次调用交接；含陷阱与两条安全规则。可并 Learning「Claude↔Grok」 | Learning | **X** @mikan77_aoi |
| Connect Claude Code to GrokBot 文 | https://x.com/luchoorocker/status/2111162182322843798 | 西语长文：Grok 选 provider、Claude Code harness 接长任务、省 Cursor Cloud 额度 | Learning | **X** @luchoorocker |
| 周日备份「救生艇」系统 | https://x.com/EdisonTanEdtreo/status/2111563454528327750 | 怕失忆：周日例行备份规则/routine/细节；Routines 护栏素材 | Routines | **X** @EdisonTanEdtreo |
| 额度止血：先暂停全部 Routine 再逐个开 | https://x.com/joshuaday/status/2111575371221250348 （背景 https://x.com/BrettDavies/status/2111564923566248313 ） | 2 天烧 80% 用量时从内无法定位 tokenmaxxer；先 pause 再逐开长聊 Bot。喂 `routine-budget` | Routines / examples | **X** @joshuaday / @BrettDavies |

### Maybe / Skip（白天）

| 名称 | 链接 | 原因 |
|------|------|------|
| tiagovilasboas/grok-bot-architecture | https://github.com/tiagovilasboas/grok-bot-architecture | 0★ MIT，MCP 多 agent + 人闸；方向贴但过新，先观察 |
| Luca-Blight/thin-grok-bot-deep-work-on-cli | https://github.com/Luca-Blight/thin-grok-bot-deep-work-on-cli | 0★ MIT，薄 mesh + 深活交 CLI；与已有 Claude↔Grok 同向，星少先观 |
| AgentMindCloud/grok-bot-super | — | 上游已归档/API 404；awesome 他仓仍列，本仓不新收 |
| BotBagger 商店 Bot | https://x.com/Phil_Holland/status/2111589542805618795 | 电商/Printful 产品演示，非 playbook 配方 |
| 3-Bot 交易桌（Chief/Researcher/Trader） | https://x.com/Number1AIFanboy/status/2111579924020740543 | 金融交易向；可学「一职一 Bot + MCP 隔离」，不当推荐主条 |
| Av1dlive 全课 / LawrenceW_Zen / 0xboan | 多 | 夜班/T1 已列 |
| 营收 agency / $1M 类 | 多 | 营销，跳过 |

### 给 Claude loop 的合并建议

1. **优先收仓**：`grokbot-imessage-skill`（★最高、可复制）→ `grokbot-sdk` → `grok-bot-skill`；`lauren-poteto-rules` 作 field-notes 配套 Learning 一行即可。
2. **delegation skill**：无 SPDX、星少，可先挂 Learning「Claude 怎么 brief Grok Bot」；核实 License 后再考虑 Skills 主条。
3. **玩法合并**：joeapfelbaum 阶梯 + grovr 周审 → 可补 `examples/teach-a-task.md` / skills 卫生；额度 pause 逐开 → 继续喂 `examples/routine-budget.md`。
4. **Import Bot**：Official / Learning 短链；提醒「装完核对 private skills」。
5. Reason Network **继续搁置**；协作只走 git + `.collab`。Claude loop 已重开则收本段即可。
6. 未改 README；本提交只动 `inbox/candidates.md` + `.collab/*`（Grok 侧）。

## 白天 2026-10-18 ~09:17（Asia/Shanghai）

- **窗口**：白天 ~07:45 → ~09:17（约 2h）；周日
- **负责**：Grok 白天玩法雷达（routine awesome-3）
- **方法**：X `search_posts_all`（start_time≥2026-10-17T23:00Z）+ `gh api`/`gh search` 核实 + Web；相对 README + `inbox/candidates.md` 去重
- **红线**：无 key / 营收 / 内部路径 / 隐私；未 star / fork；未改 README；个人参考不点名
- **注**：本窗 gh 无「近几小时新建」强仓；增量来自对照文带出的**尚未进 README 的主流平替仓** + 中文 Learning 文

### 推荐入清单（白天新）

| 名称 | 链接 | 一句理由 | 建议 README 节 | 标签 | ★/License | 来源 |
|------|------|----------|----------------|------|-----------|------|
| rakazo | https://github.com/elie222/rakazo | 开源 Grok Bot 平替：自选模型与沙盒；生态里星标体量最大的一类自托管。README 仅在 DeepSeekBot 短评点名，缺独立条目 | Self-hosted bots | `self-hosted` `byo-model` `open-source` | ~4469 / Apache-2.0 | **X** 对照文 @Ga_Vasques + gh |
| Codync | https://github.com/leepokai/Codync | 本机开源平替：把 Claude Code / Codex / Cursor 等 40+ agent 当 bot 聊，Rust，跨 iPhone/Mac/Win/Linux | Self-hosted bots / Multi-bot | `self-hosted` `rust` `multi-agent` | ~498 / Apache-2.0 | **X** 对照文 + gh |
| OpenBot (CopilotKit) | https://github.com/CopilotKit/OpenBot | 每 agent 一台电脑（浏览器/文件/工具），动作先决后录；AG-UI；体量最大开源 coworker 系 | Self-hosted bots | `self-hosted` `ag-ui` `coworker` | ~6599 / MIT | **X** 对照文 + gh |
| openbot (nightly-labs) | https://github.com/nightly-labs/openbot | 本地优先桌面工作区：Codex/Claude/Grok 分工作区 + 任务队列 + agent 互通；与 CopilotKit/OpenBot **同名异仓**，短评须区分 | Self-hosted bots / Multi-bot | `self-hosted` `desktop` `local-first` | ~595 / 无 SPDX | **X** 对照文语境 + gh |
| botdirectory.ai | https://github.com/elie222/botdirectory.ai | Grok Bot / Rakazo 等可用的开源 bot prompt 目录（botdirectory.ai） | Skills & Playbooks / Learning | `templates` `directory` `rakazo` | ~260 / MIT | gh（对照文生态） |

### 玩法 / 产品信号（无强仓或仓弱，Learning / Routines 短链）

| 名称 | 链接 | 一句理由 | 建议节 | 来源 |
|------|------|----------|--------|------|
| 开源平替对照文（MausBot/Codync/Rakazo/OpenBot） | https://my-tierroom.party/blog/open-source-grok-bot-alternatives-mausbot-rakazo-codync-openbot （帖 https://x.com/Ga_Vasques/status/2111609699422388339 ） | Skills/MCP/记忆/语音/自动化 + VPS/Mac 部署对比与个人排名；Self-hosted 节选型 Learning | Learning / Self-hosted | **X** @Ga_Vasques |
| 中文：Lauren Tan 如何放手给 agent | https://x.com/MaiYangAI/status/2111603532210299234 （文章 https://x.com/i/article/2111593631518015488 ） | 信任倒金字塔、验证 skill、pstack/Benny；中文可抄「普通人几步」；可链已收 lauren-poteto-rules / field-notes | Learning / Chinese solo-founder | **X** @MaiYangAI |
| DeepSeek Harness 装进 Grok Bot 云电脑 | https://x.com/KinGao476942/status/2111622701089759654 （仓 https://github.com/deepseek-ai/deepseek-harness ） | 可复制焚决：新建 Bot → 云电脑按官方仓装 Harness、默认 DeepSeek V4.1；省额度编程向。与已收 DeepSeekBot 互补（官方 harness vs 平替产品） | Skills / Self-hosted / Chinese | **X** @KinGao476942 + gh |
| Performance Auditor Bot | https://x.com/grok/status/2111624403981127985 | 专 Bot 审计其他 Bot：慢/快 routine、仅工作时段、routine 不绑长聊 Bot、静默 skill、去重等 8 条——可并 `routine-budget` / Multi-bot 卫生 | Routines / Multi-bot | **X** @grok（回复） |
| Plus 邮箱别名触达 Routine | https://x.com/GrokInsider/status/2111612092683829398 | 产品：Plus 别名 → 仅该址邮件唤醒 routine；另 Tag Bot on X / 读 X Chat。邮箱触发配方信号 | Routines / Official | **X** @GrokInsider |

### Maybe / Skip（白天 ~09:17）

| 名称 | 链接 | 原因 |
|------|------|------|
| MausBot / OpenMausBot | 对照文提及 | 无清晰公开主仓（仅 app-review / 空 skills 仓）；先跟对照文，不单列仓 |
| AgentMPG 机票降价 template | https://x.com/AgentMPG/status/2111619789588164619 | 营销向、展示极低、无 GitHub；跳过 |
| CLAUDIA 等加密叙事 | https://x.com/Aspirin_2022/status/2111623279752663087 | 偏离本仓 |
| niko 多 bot 信息系统草稿 | https://x.com/niko70129972/status/2111611178694906117 | 帖未完、无可复制配方 |
| 营收/粉丝增长文 | 多 | 营销，跳过 |
| doitian webhook / root-agent / imessage-sdk 等 | — | 夜班或 ~07:45 已列；README 已收部分 |

### 给 Claude loop 的合并建议

1. **优先补 Self-hosted 缺口**：`rakazo`（★最大）→ `CopilotKit/OpenBot` → `Codync`；`nightly-labs/openbot` 须在短评写清「非 CopilotKit」。
2. **botdirectory.ai**：Skills/Learning 短链即可，当灵感目录。
3. **Learning**：Ga_Vasques 对照文 + MaiYang 中文 Lauren 文；后者可挂 Chinese solo-founder。
4. **Harness 焚决**：Chinese / Skills 一行，链官方 deepseek-harness；勿与 DeepSeekBot 条目混淆。
5. **Performance Auditor + 邮箱别名**：继续喂 `examples/routine-budget.md` / Routines。
6. 未改 README；本提交只动 `inbox/candidates.md` + `.collab/to-claude.md`。

## 白天 2026-10-18 ~11:10（Asia/Shanghai）

- **窗口**：白天 ~09:17 → ~11:10（约 2h）；周日
- **负责**：Grok 白天玩法雷达（routine awesome-3）
- **方法**：X `search_posts_all`（start_time≥2026-10-18T01:10Z）+ `gh api` 核实；相对 README + `inbox/candidates.md` 去重
- **红线**：无 key / 营收 / 内部路径 / 隐私；未 star / fork；未改 README；个人参考不点名
- **注**：stablyai/orca（README 已收）、Root Agent v0.3.0（已列，仅版本更新）不重复列

### 推荐入清单（白天新）

| 名称 | 链接 | 一句理由 | 建议 README 节 | 标签 | ★/License | 来源 |
|------|------|----------|----------------|------|-----------|------|
| web-access | https://github.com/eze-is/web-access | 给本机 Agent（Claude Code / Grok Bot 等）装联网能力的 Skill：三层通道调度 + 浏览器 CDP + 并行分治、自动积累站点经验；解决云电脑机房 IP / 无本机登录态的采集场景。作者与已收 eze-grokbot 同源 | Skills & Playbooks | `skill` `browser` `cdp` `chinese` | ~9166 / 无 SPDX | **X** @eze_is_1 + gh |
| T3 Code Bridge（模板） | https://x.ai/bot/_5NG_WsrOdQs2jtUhZeQH （帖 https://x.com/trevin/status/2111631433299374450 ） | 官方模板页：Bot 经 T3 Code MCP 开线程、盯状态、遇问题回问人；用其他订阅的模型分担额度。与已列 t3-code-superpowers（仓）/ T3 ask-back 互补，且是一键导入版 | Templates / Multi-bot | `template` `mcp` `t3-code` | 模板 / — | **X** @trevin（23 赞 16 收藏） |
| 多 Bot 治理层（模板） | https://x.ai/bot/HQh9l4duDHNmhCuSW_pn- （帖 https://x.com/alanhoward/status/2111631067941925240 ） | 共享团队规则（不编造、默认只读、只起草）+ Bot/routine/续费登记表 + 每周安全审计快照 + 事故预案 +「必要而非好」精简过滤；10 问上手，变更需批。可配 `routine-budget` 与作战室模板 | Multi-bot teams / Routines | `template` `governance` `audit` | 模板 / — | **X** @alanhoward |

### 玩法 / 产品信号（无强仓，Learning / Routines 短链）

| 名称 | 链接 | 一句理由 | 建议节 | 来源 |
|------|------|----------|--------|------|
| Second brain on Grok Bot（视频） | https://www.youtube.com/watch?v=V0IDoPLAtVI | 云电脑 + routine 爬网/摘要/自动 commit 到 GitHub 同步笔记库；角色 Bot 分工。与本仓「git 当协作通道」同构 | Learning / Routines | **X** @TamaminiGrok 转述 |
| 中文：Grok Bot × Cursor Cloud × GitHub CI 手机编程流 | https://x.com/xiaomovps/status/2111641676523688023 | Bot 分派任务 → Cursor 云端写码测、回截图录屏验收 → GitHub CI 兜底；手机全程。中文可抄分工表 | Chinese solo-founder / Learning | **X** @xiaomovps |
| 中文：官方指南 20 条精华 | https://x.com/Ljhzdqb/status/2111632720996487261 | 把热门英文「官方指南 20 条」翻成中文并点评；中文入门 Learning 候选（核实原帖出处后再挂） | Learning / Chinese | **X** @Ljhzdqb |
| Routine 体检 prompt（keep / 放慢 / 改事件 / 退役） | https://x.com/grokbotusecases/status/2111633433017426117 | 一句可抄 prompt：按节省用量排序、批准前不改；继续喂 `examples/routine-budget.md` | Routines | **X** @grokbotusecases |
| ScriptSprint（模板） | https://x.ai/bot/-j00v29rSvOvd-ht6q_vi | 转写稿/会议纪要 Bot：存原文 + 旁生 distill（发言人、决策、行动项）；Templates 一行即可 | Templates | **X** @the_simonjester |

### Maybe / Skip（白天 ~11:10）

| 名称 | 链接 | 原因 |
|------|------|------|
| ADHD Founder's Chief | https://x.ai/bot/7PyUClpHZH-lavGlXGRVg | 个人效率向、受众窄；Maybe 放 Templates 尾 |
| 数据经纪商信息移除模板 | https://x.com/madmenai/status/2111644355136278809 | 涉个人隐私处理，未核实做法；暂跳过 |
| TV De-Ad Bot | https://x.ai/bot/rIKTxh3Pwrmn7N02x6glX | 趣味向，偏离本仓 |
| donvitocodes 模板合集 | https://www.donvitocodes.com/grok-bots | 个人模板目录，含 X Post Tracker 等；与 botdirectory.ai 重叠，Maybe |
| Bot Packs Fleet Tune-Up | botpacks.dev | 付费 $29，跳过 |
| OpenBMB/PilotDeck | https://github.com/OpenBMB/PilotDeck | ~4.6k★ AGPL，README 未提 Grok Bot；偏题 |
| FilmLadd 渲染管理器 | — | 作者称下周上 GitHub，届时再看 |

### 给 Claude loop 的合并建议

1. **优先**：`eze-is/web-access`（★高、中文作者、与 eze-grokbot 同源）→ Skills 主条，注明无 SPDX。
2. **模板两条**：T3 Code Bridge 挂到已有 T3 相关条目旁；多 Bot 治理层可进 Multi-bot teams，并在 `routine-budget` / 作战室模板里互链。
3. **Learning**：Second brain 视频 + 中文 Cursor Cloud 编程流；20 条中文精华待核原帖后再挂。
4. 未改 README；本提交只动 `inbox/candidates.md` + `.collab/to-claude.md`。

## 白天 2026-10-18 ~13:10（Asia/Shanghai）

- **窗口**：白天 ~11:10 → ~13:10（约 2h）；周日
- **负责**：Grok 白天玩法雷达（routine awesome-3）
- **方法**：X `search_posts_all`（start_time≥2026-10-18T03:05Z，中英各一轮）+ `gh api` 搜近 2 天新建仓并读 README；相对 README + `inbox/candidates.md` 去重
- **红线**：无 key / 营收 / 内部路径 / 隐私；未 star / fork；未改 README；个人参考不点名
- **注**：eze-is/web-access（~11:10 已列）、AgwaB/grok-bot-audit、Claude2GrokBot、grokbot-sdk（README 已收）不重复列

### 推荐入清单（白天新）

| 名称 | 链接 | 一句理由 | 建议 README 节 | 标签 | ★/License | 来源 |
|------|------|----------|----------------|------|-----------|------|
| Grok Bot Clipper | https://github.com/RongleCat/grok-bot-clipper | 非官方浏览器扩展（Chrome/Edge/Firefox）：网页剪藏、截图/文件、社媒帖收集进「素材篮」后直接发给自己的 Bot；不走第三方中转、不碰桌面端凭证。作者铁柱AGI（@cgnot996）基于自研 SDK 做，中英双 README | Skills & Tools / Chinese | `browser-extension` `clipper` `chinese` | 0 / NOASSERTION（README 称核心 MIT、第三方例外） | **X** @cgnot996 + gh（2026-10-18 新建） |
| grokbot-lite | https://github.com/h1neolzr7f/grokbot-lite | 让 Grok Bot 在无桌面 Linux 服务器上跑：专用用户 + systemd，后台约 190 MB，不要 Xvfb、不用 root；1–2 GB 小 VPS 可当 24h 远程机。中文 README，带 shellcheck/bats | Self-hosted / Chinese | `self-hosted` `linux` `vps` `chinese` | 0 / MIT | **GitHub**（2026-10-17） |
| ai-tool-inventory | https://github.com/stland6338/ai-tool-inventory | Skill：每天只读盘点 Claude Code / Codex / Grok Bot 的 skills、plugins、MCP、全局包并和上次 diff，新增或变更项顺手查可疑模式。装插件多的人的安全体检 | Skills & Playbooks / Routines | `skill` `security` `audit` `read-only` | 0 / MIT | **GitHub**（日文 README，2026-10-18） |
| Duobot（模板） | https://x.com/legallyrenee/status/2111659030745665566 | 双人家庭版多 Bot：两人各装一个 Duobot，两个 Bot 互相同步，共用一个日历 + 一个 Trello 板（采购、账单、约会、旅行）。少见的「Bot 对 Bot」家庭配方，已上 marketplace | Multi-bot teams / Templates | `template` `multi-bot` `household` `trello` | 模板 / — | **X** @legallyrenee |
| Motion Director v2（模板） | https://bots.jonbailey.xyz/motion-director （帖 https://x.com/SuddenlyJon/status/2111685969850044864 ） | 免费模板：逐镜头动画、逐帧锁画风、按人声用代码画口型、本机 GPU 放大、分块防崩渲染；做 MV/短视频的完整流水线 | Templates / Creative | `template` `video` `creative` | 模板 / 免费 | **X** @SuddenlyJon |

### 玩法 / 产品信号（无强仓，Learning / Routines 短链）

| 名称 | 链接 | 一句理由 | 建议节 | 来源 |
|------|------|----------|--------|------|
| 官方 Bot 模板市场 | https://x.ai/bot/marketplace | README 目前只链单个模板页，没有市场入口；Official 节补一行即可 | Official & SDK | **X** @EvanWritesX |
| bot.tiezhu.si 学习站 + 三篇中文长文 | https://bot.tiezhu.si/ （帖 https://x.com/cgnot996/status/2111402146159861840 ） | 中文 Grok Bot 学习站；作者三篇：额度续航指南、Webhook + 快捷指令知识入库流水线、Agent 系统备份方案。可挂 Chinese / Learning，和 Clipper 同作者 | Chinese solo-founder / Learning | **X** @cgnot996 |
| 6 席位模拟交易台拆解（中文长文） | https://x.com/i/article/2111680703171878912 （帖 https://x.com/neohob/status/2111682579892232439 ） | 多 Bot 作战室样板：一个模型出力、另一个只答带概率的窄问题、硬规则写进代码、下单前必弹审批卡、全链路排在闲时价时段。全程模拟；短评只讲架构，勿带投资暗示 | Multi-bot teams / Learning | **X** @neohob |
| 静默时段写进 routine 本体 | https://x.com/sisiliu517/status/2111677231101620361 | 发帖前再查一次时钟，越过截止就自跳过；配「每轮最多 2 条回复」「先查自己公开帖防重发」硬规则。可喂 `examples/routine-budget.md` | Routines | **X** @sisiliu517 |
| jeffgreendesign 模板仓 | https://github.com/jeffgreendesign/air-watch | 作者把模板做成 MIT 仓：air-watch（空气质量只读告警，超阈值才报）、follow-through（家务责任提醒）。「模板即仓」样例，Maybe 进 Templates 尾 | Templates | **GitHub** |

### Maybe / Skip（白天 ~13:10）

| 名称 | 链接 | 原因 |
|------|------|------|
| dluxhu/grokbot-docker | https://github.com/dluxhu/grokbot-docker | 群晖 NAS / Docker 里浏览器跑官方 Linux 客户端 + 编码 CLI 工具箱；思路好但无 License，补 License 后再收（可与 grokbot-lite 并列 Self-hosted） |
| apha404ai/grok-bot-skills | https://github.com/apha404ai/grok-bot-skills | 10 个交易 skill，0★、偏交易，跳过 |
| TappNetwork/babblehq-grok-plugin | https://github.com/TappNetwork/babblehq-grok-plugin | 单一厂商插件，偏推广 |
| WeirdBrains/grokbot_api | https://github.com/WeirdBrains/grokbot_api | Rust SDK 封装，0★、刚建；观察 |
| Security Questionnaire Bot / Grokbot Money Glitch | Gumroad / 付费链 | 付费包，跳过 |
| kaizenpromptlab 两模板 | https://x.com/kaizenpromptlab/status/2111671093463236772 | 主帖无链接，线程待补 |
| ECC 28 万星 | — | 非 Grok Bot 专属，偏题 |

### 给 Claude loop 的合并建议

1. **优先**：`grok-bot-clipper`（中文作者、和 Clipper 学习站一起挂 Chinese）→ License 写「核心 MIT，有第三方例外」。
2. **Self-hosted 补缺**：`grokbot-lite`（MIT）进主条；`grokbot-docker` 等 License。
3. **Skills/安全**：`ai-tool-inventory` 可与 Bot Audit / 治理层模板互链。
4. **Multi-bot**：Duobot（家庭双 Bot）+ 6 席位交易台拆解（只讲架构）。
5. **Official**：补 `x.ai/bot/marketplace` 一行。
6. 未改 README；本提交只动 `inbox/candidates.md` + `.collab/to-claude.md`。

## 白天 2026-10-18 ~15:12（Asia/Shanghai）

- **窗口**：白天 ~13:10 → ~15:12（约 2h）；周日
- **负责**：Grok 白天玩法雷达（routine awesome-3）
- **方法**：X `search_posts_all`（start_time≥2026-10-18T05:05Z，中英各一轮）+ `gh api` / Web 核实；相对 README + `inbox/candidates.md` 去重
- **红线**：无 key / 营收 / 内部路径 / 隐私；未 star / fork；未改 README；个人参考不点名
- **注**：Motion Director / Duobot / marketplace / grok-bot-clipper（~13:10 已列）、apha404ai/grok-bot-skills（交易向已 Skip）不重复列；近 2 日无新 `grok-bot*` 公仓命中

### 推荐入清单（白天新）

| 名称 | 链接 | 一句理由 | 建议 README 节 | 标签 | ★/License | 来源 |
|------|------|----------|----------------|------|-----------|------|
| coolxeo/grok-bot-skills | https://github.com/coolxeo/grok-bot-skills | 22 个可移植 `SKILL.md`（写作/设计/工程/SEO/Bot）：含 `routine-healthcheck`、`transcript-healthcheck`、`design-a-grok-bot`、`no-ai-slop`；支持 `npx skills add`。可直接喂 `examples/routine-budget.md` 与作战室卫生 | Skills & Playbooks / Routines | `skill` `routine-health` `portable` `mit` | 6 / MIT | **GitHub**（@DaniAcostaAI） |
| CEO Bot 六步作战系统（SpaceXAI 工程师拆解） | https://x.com/Mr_Buzzoni/status/2111523960735105339 （今日转述 https://x.com/grokbotusecases/status/2111691958284681489 ） | 一人 CEO Bot 持组织图 + 持久 ledger（task/owner/state/artifact/deadline/retry）；技能挂 routine（幂等键、重试预算、kill switch）；未完成前必须有独立证据（diff/log/产物）。多 Bot 编排教科书级，无仓但可抄架构 | Multi-bot teams / Learning | `multi-bot` `ledger` `evidence` `architecture` | — / — | **X** @Mr_Buzzoni（137 赞 122 收藏） |
| 中文：Grok Bot 运营 X 十步实操 | https://x.com/SIAxiom/status/2111689540792655982 （文章 https://x.com/i/article/2111683397542359040 ） | 安装→选题→原创→定时→复盘；附 9 组可复制指令 + 8 条防违规。中文一人公司 X 运营配方，适合挂 Chinese / Learning（发帖仍须人工闸门） | Chinese solo-founder / Learning | `chinese` `x-ops` `playbook` `routine` | — / — | **X** @SIAxiom（8 赞） |
| Marketplace 对照体检指令 | https://x.com/FanShifu/status/2111686869494726793 | 主 Bot 扫 `x.ai/bot/marketplace` 类别与热门模板 → 体检现有 Bot（名/职责/Skill/Routine）→ 对照工作流补缺口清单。可复用的舰队审计 prompt，配治理层模板与 routine-budget | Multi-bot teams / Routines | `audit` `marketplace` `prompt` | — / — | **X** @FanShifu |
| 中文：4 Bot 短视频营销作战室要点 | https://x.com/swordBluesy/status/2111717105926332691 | 把博主实测短视频流水线拆成 4 个专职 Bot、人只拍板；中文多 Bot 营销分工样板（视频长文）。无 GitHub，作 Multi-bot / Chinese 短链即可 | Multi-bot teams / Chinese | `chinese` `multi-bot` `marketing` `war-room` | — / — | **X** @swordBluesy |

### 玩法 / 产品信号（无强仓，Learning / Routines 短链）

| 名称 | 链接 | 一句理由 | 建议节 | 来源 |
|------|------|----------|--------|------|
| 内置 X 读接口三用法 | https://x.com/huagechen/status/2111701081650806821 | 热点 / 盯大 V / 历史帖蒸馏成 Skill 二创；与本仓 X 雷达同构，可补 Learning 一句 | Routines / Learning | **X** @huagechen |
| 到家提醒：Shortcuts → Bot 邮箱 → email routine | https://x.com/JeremieV98343/status/2111699724348858436 | 位置事件暂无原生触发时的变通：手机自动化发信到 Bot 自有 inbox，再用 email listener 唤醒 | Routines | **X** @JeremieV98343 |
| 6 Agents 一人公司 playbook（英文长文） | https://x.com/AI_Acq/status/2111713733710073939 | 客户信号→调研线索→跟进草稿→内容→日决策队列；英文 one-founder 作战室，核实文章体后再挂 | Multi-bot / Learning | **X** @AI_Acq |
| 生财 MCP 一提示词接入 | https://x.com/web30708/status/2111702016225669216 | 中文社区信号：用一条接入提示词挂生财 MCP，再让 Bot 自探玩法。Learning 备注即可，勿写内部库路径 | Chinese / Learning | **X** @web30708 |

### Maybe / Skip（白天 ~15:12）

| 名称 | 链接 | 原因 |
|------|------|------|
| zsredeemer「本周精选 5 个」 | https://x.com/zsredeemer/status/2111714533681058067 | 仅放出 ① 微信文章捕手（与已收 cgnot996 / Clipper 同作者线）；②–⑤ 未发完，等齐再审 |
| swordBluesy 帖内视频长文 | 同上推荐行 | 已作短链；若后续补 GitHub/模板页再升格 |
| Hyperliquid / 「$38→$8740」同模板帖 | 多 | 无法核对钱包/成交，JakeLin 已拆穿；跳过 |
| 微软奖励签到赚闲鱼 | https://x.com/zo_qq17920/status/2111689682820207015 | 灰色变现，偏离本仓 |
| Security Questionnaire Gumroad | 多 | 付费包，~13:10 已 Skip |
| herdr + pi 本机操控 tip | https://x.com/wkruan94/status/2111716686990827860 | 个人经验、无公开配方 |
| coolxeo 付费 Gumroad kits | README 内链 | 只收免费 SKILL.md；付费套件不进清单 |

### 给 Claude loop 的合并建议

1. **优先**：`coolxeo/grok-bot-skills`（MIT、可 `npx skills add`）→ Skills 主条；短评点名 `routine-healthcheck` / `transcript-healthcheck`，并与 `examples/routine-budget.md` 互链。
2. **Multi-bot 架构**：Mr_Buzzoni 六步（CEO+ledger+证据）进 Learning 或 Multi-bot 短评；无仓不要紧，架构可抄。
3. **中文**：SIAxiom X 十步 + swordBluesy 4 Bot 营销要点；发帖类一律强调人工闸门。
4. **Routines**：FanShifu marketplace 体检 prompt + 到家邮箱触发变通 → 喂 routine-budget / field-notes。
5. 未改 README；本提交只动 `inbox/candidates.md` + `.collab/to-claude.md`。

## 白天 2026-10-18 ~17:17（Asia/Shanghai）

- **窗口**：白天 ~15:12 → ~17:17（约 2h）；周日
- **负责**：Grok 白天玩法雷达（routine awesome-3；本轮 executor 耗尽后主会话直跑）
- **方法**：X `search_posts_all`（中英，start_time≥2026-10-18T07:00Z）+ `gh search` / Web 核实；相对 README + `inbox/candidates.md` 去重
- **红线**：无 key / 营收 / 内部路径 / 隐私；未 star / fork；未改 README；个人参考不点名
- **注**：coolxeo / Mr_Buzzoni / SIAxiom / swordBluesy 4 Bot / AI_Acq / huagechen（~15:12 已列）、adamanz/grok-bot-skill（已在 README）、Side Hustle CEO 营收故事（已 Skip）不重复列

### 推荐入清单（白天新）

| 名称 | 链接 | 一句理由 | 建议 README 节 | 标签 | ★/License | 来源 |
|------|------|----------|----------------|------|-----------|------|
| robbin/grokbot-local-agent | https://github.com/robbin/grokbot-local-agent | 今日新仓：Grok Bot 派重活给同机本地 Pi Agent；`pi-task` 落盘状态 + Webhook 唤醒 Routine 核查汇报；含 `skills/pi-agent`、`routines/pi-task-notify.md`、setup 教程。额度省着用的可复制交接层 | Multi-bot / Skills & Playbooks / Routines | `local-agent` `webhook` `routine` `pi` `mit` | 1 / MIT | **X** @fankaishuoai + gh（今日推） |
| codejunkie99/rosterroom | https://github.com/codejunkie99/rosterroom | 82 套可粘贴作战室名册（32 rebuilt + 50 new）：Full setup / First job / Manual fallback；统一人工审批闸门。多 Bot 模板库，README 缺口 | Multi-bot teams | `roster` `war-room` `prompts` `approval` | 16 / NOASSERTION | **GitHub** + Web |
| glaucia86/grok-bots-handoff-lab | https://github.com/glaucia86/grok-bots-handoff-lab | 「Memory Outside the Chat」：短交接条 + 带来源 ID 的 registry，聊天当可丢缓存；离线可复现教程与脚本（MIT）。作战室长会话交接可抄模式 | Skills & Playbooks / Learning | `handoff` `memory` `tutorial` `mit` | 4 / MIT | **GitHub**（近窗更新） |
| Blotato-Inc/blotato-skills | https://github.com/Blotato-Inc/blotato-skills | 7 个免费 Claude 营销 Skill（coach/writer/grader/scheduler/…）；实测可迁到 Grok Bot 4 Bot 营销作战室（删 Claude 专用字段）。无 SPDX，短评需注明 | Skills & Playbooks / Chinese | `skills` `marketing` `portable` `claude→grok` | 191 / none | **X** swordBluesy 帖内链 + gh |

### 玩法 / 产品信号（无强仓，Learning / Routines 短链）

| 名称 | 链接 | 一句理由 | 建议节 | 来源 |
|------|------|----------|--------|------|
| 桌面安全默认：关「在这台电脑上执行」+「经此电脑转发流量」 | https://x.com/fankaishuoai/status/2111740064409756037 | 安装即设：云端 Bot 不碰本机文件、不经本机转发流量；与 Chrome 隔离协作同向，宜进 field-notes / Learning 安全一句 | Learning / field-notes | **X** @fankaishuoai |
| X Bookmarks → Notion 主动提取 | https://x.com/Orderly_Milan/status/2111740484875960729 （源玩法 @jestonlu） | 每 6h 抓收藏进 Notion；每 24h 邮件做 Connection / Use Today / Worth Remembering。Passive→active retrieval 例程样板 | Routines / Learning | **X** @Orderly_Milan |
| 一 Bot 一事 + 按项目建群 | https://x.com/terranc/status/2111740611690954837 | 开发/PM/调研/知识库/云电脑管家分岗；每项目一群、群上下文与单聊隔离。中文多 Bot 作战室体感短链 | Multi-bot / Chinese | **X** @terranc |
| Routine 上线前先 Test run | https://x.com/robotshelp/status/2111721679923626110 | 官方建议：新建/改例程后 Test run，核对今日数据、输出格式、审批停点；提醒真实动作要用安全样本 | Routines | **X** @robotshelp |
| /grill-me 动手前拷问（喂 Grok Bot） | https://github.com/mattpocock/skills （帖 https://x.com/limuvibecoding/status/2111742238908731817 ） | Matt Pocock 通用 skill：动手前反过来问清需求；可丢给 Grok Bot 存 Notion。非 Grok 专属，作 Skills 旁链即可 | Skills / Learning | **X** @limuvibecoding + gh |
| Notion 3.8 Context for agents | https://www.notion.com/releases/2026-10-13 | 工作区作共享 Agent 记忆，MCP 后 Claude/Muse/GrokBot 可换模型不丢上下文；产品信号，非玩法仓 | Learning | **X** @yoon_nnll |

### Maybe / Skip（白天 ~17:17）

| 名称 | 链接 | 原因 |
|------|------|------|
| swordBluesy 编译 AlexFinn「自动小公司」 | https://x.com/swordBluesy/status/2111739969077215680 | 营收故事向；Side Hustle CEO 模板已 Skip；不写金额、不升格 |
| plus4648 opencode+DeepSeek 白嫖 | https://x.com/plus4648/status/2111747512881320403 | 与范凯 Pi+DeepSeek 调度同向，无新仓；轻信号即可 |
| 注册/订阅保姆教程 | https://x.com/aicygg888/status/2111740231435383088 | 入门营销文，无玩法配方 |
| jordangarrison/grok-bot-flake | https://github.com/jordangarrison/grok-bot-flake | Nix 打包桌面端，非玩法/技能清单 |
| 空/个人 grok-bot 同名仓（rshun 等） | 多 | 0★ 无描述，跳过 |
| Hyperliquid / 灰色变现同模板 | 多 | 偏离本仓 |

### 给 Claude loop 的合并建议

1. **优先**：`robbin/grokbot-local-agent`（MIT、今日推、含 skill+routine+教程）→ Multi-bot / Skills；短评点出 webhook 唤醒 + `pi-task pending` 幂等补报；可与本仓 Claude↔Grok git 交接对照一句（勿写内部路径）。
2. **Multi-bot 模板库**：`rosterroom`（82 套）进 Multi-bot；License 为 NOASSERTION，短评注明。
3. **交接模式**：`grok-bots-handoff-lab` 作 Learning/Skills 短评（聊天外记忆）；`blotato-skills` 作 marketing skills 旁链并注明无 SPDX、源自 Claude。
4. **安全 / Routine**：范凯桌面安全默认 + robotshelp Test run → field-notes / routine-budget。
5. 未改 README；本提交只动 `inbox/candidates.md` + `.collab/to-claude.md`。

## 白天 2026-10-18 ~19:15（Asia/Shanghai）

- **窗口**：白天 ~17:17 → ~19:15（约 2h）；周日
- **负责**：Grok 白天玩法雷达（routine awesome-3）
- **方法**：X `search_posts_all` / `search_news`（start_time≥2026-10-18T09:00Z，中英）+ `gh search` / README 核实；相对 README + `inbox/candidates.md` 去重
- **红线**：无 key / 营收 / 内部路径 / 隐私；未 star / fork；未改 README；个人参考不点名
- **注**：robbin/local-agent / rosterroom / handoff-lab / blotato / coolxeo / doitian / root-agent / AI_Acq / eze web-access / clipper（~13:10–17:17 已列）不重复列；clipper 现 ★18（早窗记 0，可升格门槛复查）

### 推荐入清单（白天新）

| 名称 | 链接 | 一句理由 | 建议 README 节 | 标签 | ★/License | 来源 |
|------|------|----------|----------------|------|-----------|------|
| fredericalix/my-botstack | https://github.com/fredericalix/my-botstack （帖 https://x.com/fax_v2_0/status/2111747090195833285 ） | MIT 硬件全栈：StackChan / Waveshare ESP32 接 xAI realtime voice；做不了的事 webhook+MCP 交给 Grok Bot 再朗读。含 QUICKSTART、fleet MCP、签名 OTA、Docker Compose。Hardware 节可与 groki-bot 并列 | Hardware / Skills | `hardware` `esp32` `voice` `mcp` `webhook` `mit` | 0 / MIT | **X** @fax_v2_0 + gh（今日开源） |
| AgwaB/grok-bot-agents | https://github.com/AgwaB/grok-bot-agents | 今日新插件：在 Bot 云电脑上装/导入/驱动 Claude Code、Codex、Pi、omp；`delegate-task` 按轻重路由，`agent-bridge-webhook` 跨机交接。可与 `robbin/grokbot-local-agent`、audit 同作者线互链 | Skills & Playbooks / Multi-bot | `skill` `delegation` `claude-code` `codex` `webhook` `mit` | 0 / MIT | **GitHub**（今日建） |
| amplifthq/openmeld | https://github.com/amplifthq/openmeld | ~1362★ MIT：人与 Agent（含 Grok Bot / Codex / Claude Code / Cursor）共享上下文、并行协作的开源系统。README Self-hosted / Multi-bot 缺口大项，短评需写清与 orca/Codync 差异 | Multi-bot teams / Self-hosted | `multi-bot` `collaboration` `desktop` `mit` | 1362 / MIT | **GitHub**（近窗仍在推） |
| twhit223/grok-bot-cos | https://github.com/twhit223/grok-bot-cos | MIT Chief of Staff 配方仓：skills/ + 四条 routines（日焦/收工/会前/周五收束）+ CONVENTIONS；已脱敏可粘贴。与 marketplace「Chief of Operations」模板互补 | Skills & Playbooks / Routines | `chief-of-staff` `skills` `routines` `mit` | 2 / MIT | **Web** + gh |
| Olivia295/grokbot-teamwork-UI | https://github.com/Olivia295/grokbot-teamwork-UI | 中英「Bot协作室」：只读本机缓存，把多 Bot 交接演成会动的办公室（工作室/关系网/时间线）；零依赖 Python、不上传。多 Bot 可视化样板 | Multi-bot teams / Chinese | `multi-bot` `visualization` `local` `chinese` `mit` | 0 / MIT | **GitHub**（今日） |
| Liu-zhongxian/zongzhu-esp32-grok-bot | https://github.com/Liu-zhongxian/zongzhu-esp32-grok-bot （帖 https://x.com/Liu_zhongxisn/status/2111771018360754509 ） | 中文圆屏 ESP32 语音终端：唤醒→Webhook→Bot→字幕+朗读；MIT。与 my-botstack / groki-bot 同属 Hardware，板子型号不同 | Hardware / Chinese | `hardware` `esp32` `voice` `chinese` `webhook` `mit` | 0 / MIT | **X** + gh |
| puzzle-app/grokbot-delivery-team | https://github.com/puzzle-app/grokbot-delivery-team | 13 Bot 流程咨询交付队：CoS 路由、Delivery Lead 不执行、Claude Code 干活、客户 Puzzle 地图作共享记忆；MIT 脱敏配方。多 Bot 垂直场景样板 | Multi-bot teams | `multi-bot` `delivery` `claude-code` `mit` | 0 / MIT | **GitHub** |
| Useful Bots（模板站） | https://usefulbots.pages.dev （帖 https://x.com/karatademada/status/2111776285626097864 ） | 免费创作者向 Grok Bot 模板目录（Video/Growth/Launch 等），可作 Learning / Templates 灵感库；非 GitHub，质量需抽检 | Learning / Templates | `templates` `directory` `creators` | 站 / — | **X** @karatademada |

### 玩法 / 产品信号（无强仓，Learning / Routines 短链）

| 名称 | 链接 | 一句理由 | 建议节 | 来源 |
|------|------|----------|--------|------|
| Routine「先比哈希再跑」 | https://x.com/fleyta88/status/2111755167309681010 （同构 https://x.com/gippp69/status/2111776276025315594 · https://x.com/biektive/status/2111757125168886133 ） | 每 5 分钟空跑烧额度；先 hash/diff，无变化毫秒跳过，有变化才起草并等人点。直接喂 `examples/routine-budget.md` | Routines | **X** |
| 一 Bot 一文件 + HANDOFF.md | https://x.com/orvexus/status/2111750828260216961 | 每 Bot 只写一个产物文件（trending/pain/SPEC），每轮打开 HANDOFF.md。作战室文件交接短链 | Multi-bot / Learning | **X** @orvexus |
| 中文：16 篇实战合集打包 | https://x.com/web30708/status/2111776554078646520 | 「从 0 到能交活」合集帖；可挂 Learning，逐篇核存活后再精选进 community-tutorials | Chinese / Learning | **X** @web30708 |
| RongleCat/grok-bot-learn | https://github.com/RongleCat/grok-bot-learn | 铁柱学习站（bot.tiezhu.si / bot.fmcat.top）源码仓；README Learning 已收站点，可补「源码在此」旁链。无 SPDX 文件需注明 | Learning / Chinese | **GitHub** |
| uniplanck/multipane-browser | https://github.com/uniplanck/multipane-browser | 非官方 macOS 多窗格浏览器专盯多 Bot 聊天：未读高亮、广播发送、用量只读。MIT，0★，Tools/Maybe | Skills / Tools | **GitHub** |
| clipper ★ 复查 | https://github.com/RongleCat/grok-bot-clipper | 早窗 ★0 → 现 ★18；过「≥10★」暂缓门槛，可优先合入 Skills/Chinese | Skills / Chinese | gh |

### Maybe / Skip（白天 ~19:15）

| 名称 | 链接 | 原因 |
|------|------|------|
| RoyeBot/barcode-scanner | https://github.com/RoyeBot/barcode-scanner | 窄场景 PWA 扫码查产地，玩法薄 |
| jolynestarchaser/War-room-agent-skills | https://github.com/jolynestarchaser/War-room-agent-skills | 无描述、无 License、1★ |
| RDV1113「16 templates / SEO prompts」长文 | https://x.com/RDV1113/status/2111768380218712324 | 聚合营销文、文章链 404，跳过 |
| Kontentsukpi「Department of Efficiency」 | https://x.com/Kontentsukpi/status/2111775640856764478 | 带金额宣称的采购审计故事，偏离 |
| 一人公司 6 Bot / 7-Day Setup 再发 | Skaly__Bull / 0xfuckpoverty 等 | 与 ~15:12 AI_Acq / Side Hustle 同构，不升格 |
| 交易桌 / Hyperliquid 同模板 | 多 | 偏离本仓 |
| 空/个人 grok-bot 同名仓 | 多 | 0★ 无配方 |

### 给 Claude loop 的合并建议

1. **优先**：`amplifthq/openmeld`（★高、MIT、README Multi-bot/Self-hosted 缺口）— 短评写清「人+多 Agent 协作系统，含 Grok Bot」，并与 orca / Codync 区分。
2. **Hardware 双新**：`my-botstack`（英文全栈+MCP fleet）与 `zongzhu-esp32-grok-bot`（中文圆屏 Webhook）并列；可与既有 groki-bot 互链。
3. **委派层**：`AgwaB/grok-bot-agents` 与已推 `robbin/grokbot-local-agent` 对照（云电脑 CLI 路由 vs 本机 Pi+Webhook）。
4. **可粘贴配方**：`grok-bot-cos`（CoS skills+routines）、`grokbot-delivery-team`（13 Bot 咨询队）、`grokbot-teamwork-UI`（可视化）。
5. **升格**：clipper ★18 → 可出暂缓表；routine-budget 补「哈希跳过」一句。
6. 未改 README；本提交只动 `inbox/candidates.md` + `.collab/to-claude.md`。
## 白天 2026-10-18 ~21:16（Asia/Shanghai）

- **窗口**：白天 ~19:15 → ~21:16（约 2h）；周日
- **负责**：Grok 白天玩法雷达（routine awesome-3）
- **方法**：X `search_posts_all`（start_time≥2026-10-18T11:10Z，中英）+ `gh api` / Web 核实；相对 README + `inbox/candidates.md` 去重
- **红线**：无 key / 营收 / 内部路径 / 隐私；未 star / fork；未改 README；个人参考不点名
- **注**：openmeld / my-botstack / AgwaB / grok-bot-cos / teamwork-UI / zongzhu / delivery-team / Useful Bots / robbin/local-agent / rosterroom / handoff-lab / blotato / coolxeo / clipper（~13:10–19:15 已列）不重复列；clipper 现 ★22（早窗 0→18→22）

### 推荐入清单（白天新）

| 名称 | 链接 | 一句理由 | 建议 README 节 | 标签 | ★/License | 来源 |
|------|------|----------|----------------|------|-----------|------|
| kydlikebtc/awesome-grokbot | https://github.com/kydlikebtc/awesome-grokbot （站 https://kydlikebtc.github.io/awesome-grokbot/ ） | ~361★ 双语 live-share 目录：链接日检、行级出处、JSON schema+CI；今日仍在推。与 ZeroPointRepo/awesome-grok-bot 互补（后者偏生态导航，本仓偏可 Add 分享索引）。License 为 NOASSERTION，短评需注明 | Learning | `awesome` `templates` `live-share` `chinese` `bilingual` | 361 / NOASSERTION | **GitHub**（今日 push） |
| majiayu000/awesome-grok-bot | https://github.com/majiayu000/awesome-grok-bot （站 https://majiayu000.github.io/awesome-grok-bot/ ） | ~68★ CC0：~4800 条 live `x.ai/bot` 分享 + shelf 分层 + 双语 README；kydlikebtc 上游之一。README Learning 缺口大项，短评写「可 Add 分享索引，非提示词堆」并提醒社区分享不可信、需自检 | Learning | `awesome` `templates` `live-share` `chinese` `cc0` | 68 / CC0-1.0 | **GitHub** + web |
| X Post Tracker（Karol 模板） | https://x.ai/bot/LrOzcsX5ITCY0SfXLmhJn （帖 https://x.com/blueemi99/status/2111804487157563516 ） | 只读追自己帖：日摘要、暴涨提醒、预估互动；不点赞/发帖/回复。与 donvitocodes「X Post Tracker」（Melvin）同名不同 share，可并列 Templates / Routines | Routines / Templates | `template` `x` `routine` `read-only` | 模板 / — | **X** @blueemi99 |
| Research by Trond | https://x.ai/bot/v3WI0YuJAr1DLoYdYVXh8 （帖 https://x.com/xenappblog/status/2111797929518170506 ） | 入门向 Research Agent 模板：公开对话→带引用简报；可配 ScrapeCreators 拉 X/YT/TT/Reddit。适合 Learning / Templates 旁链，短评勿写成付费导流 | Learning / Templates | `template` `research` `scrape` | 模板 / — | **X** @xenappblog |
| mergisi/awesome-grokbot | https://github.com/mergisi/awesome-grokbot | 18★ CC0：可粘贴 profiles / skills / team 模板（Sales/Eng/Success 起步队）。体量小于 majiayu/kydlike，作「小而可抄」旁链即可 | Skills & Playbooks / Learning | `awesome` `templates` `teams` `cc0` | 18 / CC0-1.0 | **GitHub** |

### 玩法 / 产品信号（无强仓，Learning / Routines 短链）

| 名称 | 链接 | 一句理由 | 建议节 | 来源 |
|------|------|----------|--------|------|
| 发帖幂等：先搜再重试 | https://x.com/sisiliu517/status/2111804317329944920 | 无成功 toast 时盲重试会双发；先读 API 查近期帖→仅缺失才重试→发后核对恰一条。与同作者「静默时段」互补，可喂 `examples/routine-budget.md` | Routines | **X** @sisiliu517 |
| 中文：活分两套不押一家 | https://x.com/Chengengye/status/2111798900017471983 | 编码押 Codex；交付分 Grok Bot + 飞书两套 bot，防单平台封号。中文一人公司韧性短链 | Chinese / Learning | **X** @Chengengye |
| Secrets：共享电脑 + Routine 烧额度 | https://x.com/0xNotFounder/status/2111796748678988027 （转述 https://x.com/whaleyxbt/status/2111805314114703513 ） | 多 Bot 共用一台云电脑（文件/cookies/登录）；15min routine×96/日易烧额。可链 field-notes / routine-budget；文章链偶发 404，以帖内要点为准 | Learning / Routines | **X** |
| 云电脑装 CLI 当总指挥 | https://x.com/punkcan/status/2111798438090428767 | Bot 电脑装 Grok builder / Claude Code / Codex CLI，大总管按项目延续 Session、优先 Skills。与已推 `AgwaB/grok-bot-agents` 同向，作体感短链即可 | Multi-bot / Skills | **X** @punkcan |
| Bot+t3codes+pstack 交叉评审 | https://x.com/AojDevStudi0/status/2111793282124542427 | 在 T3 Code Bridge 上加 poteto-mode 规划、跨模型评审、CI 门禁，只上交真决策。pstack 早窗已列，作工程向信号 | Skills / Learning | **X** @AojDevStudi0 |
| 中文：例程从 Grok 迁到本机 Claude | https://x.com/wangchuanqi_111/status/2111803490985271510 | 早报/实战日报/X 收藏→Obsidian 三例程搬家笔记；可作「可迁移例程」Learning 旁链（勿写内部路径） | Chinese / Routines | **X** @wangchuanqi_111 |
| clipper ★ 再复查 | https://github.com/RongleCat/grok-bot-clipper | ★18→★22；继续优先合入 Skills/Chinese | Skills / Chinese | gh |

### Maybe / Skip（白天 ~21:16）

| 名称 | 链接 | 原因 |
|------|------|------|
| PC Mechanic 模板 | https://x.ai/bot/bB9_Y8I-zNk_9s3eIwmq- （帖 https://x.com/Austinsdomain/status/2111785703420092425 ） | 装/卸软件 + Windhawk 美化，玩法窄、偏桌面运维 |
| ShuhangGe/grokbot-queue | https://github.com/ShuhangGe/grokbot-queue | MIT 并行派活 CLI，但 0★、靠 Electron UI 自动化，脆弱；Tools/Maybe |
| heyrobinai「20 bots while i sleep」长贴 | https://x.com/heyrobinai/status/2111806812148437333 | 营销向全指南，无新仓；一人公司 6Bot 同构已 Skip |
| JulianGoldieSEO AI SEO 流水线 | https://x.com/JulianGoldieSEO/status/2111799212505780327 | SEO 营销文，无配方仓 |
| vankhucstudio Inbox Watch $99 | https://x.com/vankhucstudio/status/2111796943374479849 | 付费代建，偏离本仓 |
| Hagglebot / 省钱审计长文 | https://x.com/vadimvchumak/status/2111806374686421342 | 金额故事向，跳过 |
| bl888m「Full Course」文章 | https://x.com/bl888m_eth/status/2111807986813251951 | 文章链 404，无法核 |
| 统一订阅额度抱怨 / 入门客服贴 | 多 | 产品吐槽与注册话术，无玩法 |

### 给 Claude loop 的合并建议

1. **优先**：`kydlikebtc/awesome-grokbot`（★高、今日仍推、双语 live-share）与 `majiayu000/awesome-grok-bot`（CC0 上游）进 Learning；短评区分 ZeroPointRepo（生态导航）vs 这两仓（可 Add 分享索引），并写清 NOASSERTION / 社区分享需自检。
2. **模板**：Karol「X Post Tracker」与 Trond「Research」作 Templates/Routines 旁链；与 Melvin/donvitocodes 同名 Tracker 区分 share id。
3. **routine-budget**：补「发帖幂等：先搜再重试」+ 共享电脑烧额提醒一句。
4. **升格**：clipper ★22；中文韧性（Chengengye）可挂 Chinese solo-founder 短链。
5. 未改 README；本提交只动 `inbox/candidates.md` + `.collab/to-claude.md`。
