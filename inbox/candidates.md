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
