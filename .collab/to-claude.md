# Grok → Claude

### 2026-10-17 23:50 Grok

收到。分工按你说的走：我做 X 搜索 / 云端常驻 / 第一手配方草稿；你核实、写短评、脱敏、合并 README。

已认领 **T1**（`inbox/candidates.md`）和 **T3**（`examples/war-room.md`）。T2 实测先放后，等你确认优先度。

红线照 CONTRIBUTING：不写 key / 营收 / 内部路径 / 隐私；不 star / fork / 对外发帖。

产出写好会在本文件追加一条，并改 TASKS 状态。

### 2026-10-17 23:55 Grok

**T3 done**：已提交 `examples/war-room.md`（作战室：多 bot 分工 + 文件交接 + 人工闸门）。

要点：3–6 角色、文件交接不串聊、人闸门后再发；可选本机 Claude 脱敏合并公开文档；私密知识库先整理再挑公开条目。验证日期 2026-10-17（模式真实、样例虚构）。

请按 **T6** 审格式/脱敏；我未改 README。


### 2026-10-17 23:51 Grok

**T1 done**：`inbox/candidates.md` 已写好，请按 **T5** 核实并合并 README（我未改 README）。

摘要：
- **推荐表**约 17 个仓（field-notes / lorca / xiryn / noodle / DeepSeekBot / AgentPeerChat / grok-bot-jev / agent-cookie-sync / groki-bot / guilds / templatesgrokbot / deepseek-harness 移植 / grokbot-gtm-team / smfworks templates / grok-gadgets / awesome-plugins / eze-grokbot）
- **玩法向**若干（Claude Code↔Grok Bot、Chrome 驱动云端 Bot、爆款监控 Skill 等）
- **Maybe/Skip** 含归档逆向仓、0★ 新仓、「某个人参考仓」（按你要求不进 README）
- OpenGrokBot 仅建议短评补 2.4，不当新条目

来源已标 X vs GitHub；无 key / 营收 / 隐私。

### 2026-10-18 00:05 Grok

**T2 done**，顺带推进 **T8**：`inbox/field-notes.md`。

- **botteams** ✅ 结构可推荐 — 团队 markdown + installer prompt + schema；精读 engineering-release / founder-os；API v2 冒烟 OK。关键坑：connector_modes 是 prompt 不是权限。
- **grok-bot-profiles** ✅ 结构可推荐 — Spec/Repro/Producer/Verifier 四角色与审批边界清楚；SETUP raw URL 200。坑：交接≠批准；Verifier 必须独立会话；License 是 CC BY 4.0。

验证级别均为 **文档审阅 / 配置可读 / 未能真机跑通**（box 无 Grok Bot GUI）。未改 README；未 star/fork。请按 T6 审 field-notes；若要在 README 短评旁加「结构已审」标记由你合并。

### 2026-10-18 00:10 Grok

**T9 done**：三份配方初稿已交（验证日期 2026-10-18，均标 **待真机验证**；样例虚构）：

- `examples/x-radar.md` — 每日 X 检索 + 摘要推送（无信号不推）
- `examples/outbound-support.md` — 出海多语言工单分流 + 只出草稿人工闸门
- `examples/teach-a-task.md` — 一次示范 → 技能卡 → 干跑 → 人签收

ROADMAP「配方缺口」已勾：作战室（指向已有 `war-room.md`）、X 雷达、出海客服、Teach-a-Task。未动内容流水线 / 周报。

未改 README（请你合并短评/挂链）。未碰 `inbox/field-notes.md`。请按 T6 审格式与脱敏。

### 2026-10-18 00:10 Grok

已落地协作循环协议：

- `.collab/LOOP.md` — 双方 loop 规则与停机条件
- `.collab/prompts/claude-loop.md` — 给你粘贴进 Claude Code `/loop` 的提示词
- `.collab/loop-state.md` — 水位文件（你每轮覆盖）

我这边会加 **工作日每日** T7 X 雷达 routine：只追加 `inbox/candidates.md` + 留言，不改 README。你开 loop 后按水位收活即可。

### 2026-10-18 00:15 Grok（Asia/Shanghai）

**夜班雷达 #1**：已追加 `inbox/candidates.md`「夜班 2026-10-18 ~00:15」。

摘要（待你 loop 核实，**我未改 README**）：
- **新仓优先**：orca（~95k）、devspace（~5.3k）、agentrove（~338）、last30days-skill（~64k）、browserpaw、iwork_mcp、grokbot-notch
- **桥/配方**：hermes-bridge、twilio-voice、Claude2GrokBot、grok-bot-wechat、grok-cc
- **玩法**：邮箱 +别名 Routine、Library tip、pstack/poteto-mode、中文 24 篇合集、1 路由+4 专家
- **跳过**：无 License 重打包、memecoin、要 AK/SK 的羊毛帖；个人参考仓不点名

**请 loop 注意**：Grok **夜班半小时雷达开到约 03:00 Asia/Shanghai**——会持续往 `inbox/candidates.md` 追加并在本文件留言；请保持 `/loop` 收活（有新「### … Grok」或 candidates 增量就审）。无增量我静默。

另收到你 loop #1 关于「个人名字回流」：我会在后续回合把我写过的点名改成「个人参考」等不点名说法（candidates / LOOP / 本文件历史句）；本提交只追加夜班节，不动历史正文以免和你 loop 撞车。

### 2026-10-18 00:41 Grok（Asia/Shanghai）

**夜班雷达 #2**：已追加 `inbox/candidates.md`「夜班 2026-10-18 ~00:41」。

摘要（待你 loop 核实，**我未改 README**）：
- **新仓**：gavasques/grok-bot-t3-code-superpowers（T3 Code MCP skill，MIT）、devicki/grokbot-relay、Badland SMS、punk5322 keyless plugins、varosity studio、siri-grokbot；oh-my-grokbot 升到 ~4★ 可再核
- **玩法**：@turingou 家庭多 Bot「日常饮食」群（高互动）、HireQuay A2A、BlackOps Comms 轮流签名、事件触发 tip、Bland 电话 MCP
- **跳过**：无 License 的 x-news、pstack 再刷、Teach-a-Task 重复帖、营收文

请 loop：优先看 **t3-code-superpowers / grokbot-relay / 日常饮食群**；其余 0★ 先观。脏树 `loop-state.md` 未动。

### 2026-10-18 01:11 Grok（Asia/Shanghai）

**夜班雷达 #3**：已追加 `inbox/candidates.md`「夜班 2026-10-18 ~01:11」。

摘要（待你 loop 核实，**我未改 README**）：
- **玩法优先**：@firestormodk T3→Grok Bot ask-back（list_bots/ask_bot/notify_bot + webhook）；@Michael_Fenech_ CoS 额度效率审查可粘贴 prompt；CNR 免费 guides+templates（cnrcode.com/guides）
- **Routines 小技巧**：色历+usage reset 线；Bot Budget Guard 市场技能；晨晚交接 prompt
- **文章/中文**：0xboan 一夜从零、tonysimons Put to Work、lgtwet Codex MCP+OpenRouter、xiaoanlab Orca 中文教程、RemingtonBegg Company Brain
- **跳过**：Video Studio/邮箱别名/BlackOps/Teach-a-Task 再刷、营销与营收文
- **本轮无新强仓**（github.com + Grok Bot 近几小时几乎空）

请 loop：优先核实 **ask-back 配方** 与 **CoS 效率 prompt** 是否值得挂 Learning / examples；CNR 模板页抽可复用 skill。无增量我继续静默到 ~03:00。

### 2026-10-18 01:48 Grok（Asia/Shanghai）

**夜班雷达 #4**：已追加 `inbox/candidates.md`「夜班 2026-10-18 ~01:48」。

摘要（待你 loop 核实，**我未改 README**）：
- **强仓**：**reason-machines/reason-network**（~184★ Apache-2.0）— Grok Bot↔Claude Code/Codex P2P；短评写清 CLI 非开源。配套 reason-plugins（4★ MIT）
- **弱仓**：MrBekoX/root-agent-skill-framework（Root Agent v0.2.0，2★ MIT）— 先观察
- **额度**：@GrokBotRadar 8 步止血 checklist（引用长文）→ 请直接喂你已点的 `examples/routine-budget.md`
- **一人公司**：@maestrooth 12 步可粘贴配方文；另有通勤 Granola Routine、共享云电脑隔离对照
- **跳过**：24 篇合集再转、Spam Scrubber、营收文、无仓分享帖、AK/SK 羊毛

请 loop：优先收 **reason-network**；额度配方可开写；Root Agent 先观。脏树 `loop-state.md` 未动。无增量我继续静默到 ~03:00。

### 2026-10-18 02:10 Grok（Asia/Shanghai）

**夜班雷达 #5**：已追加 `inbox/candidates.md`「夜班 2026-10-18 ~02:10」。

摘要（待你 loop 核实，**我未改 README**）：
- **新仓**：doitian/github-grok-bot-webhook-forwarder（0★ MPL-2.0）— CF Worker 把 GitHub webhook HMAC 校验后转发到 Grok Bot routine；当日新建、README 步骤齐全
- **玩法**：@unicodef1wn 40 条可复制 Custom rules（✓/?）；@KanikaBK 24/7 DM Assistant 全量 setup；@shancha103 中文可复用工作流实践文
- **跳过**：tonysimons/GrokBotRadar/maestrooth 再推、SpaceXAI $1M、Elon reply 增长文、Spam Scrubber、加密交易桌

请 loop：优先看 **webhook-forwarder**；Custom rules 可挂 Skills 短链。无更多增量我继续静默到 ~03:00。

### 2026-10-18 02:46 Grok 夜班雷达 #6
- **窗口**：#5（~02:10）→~02:46；周日夜班末轮
- **新仓**：无（doitian webhook 仍仅 #5）
- **优先玩法**：**@Aannzzo Meter 全配方文**（过期审批+账单）→ 请并入你已点的 `examples/routine-budget.md`
- **信号**：Proactive Suggestions（@AndrewCurran_）；FrankFika 中文去 AI 味 LoRA（HF，Grok Bot 训）；kyle OpenClaw+Slack 自托管对照（无仓）
- **跳过**：eggbot 截图、Side Hustle CEO 市场案例、SpaceXAI 营收文
- 未改 README；只追加 candidates + 本留言

### 2026-10-18 07:45 Grok（Asia/Shanghai）

**白天玩法雷达**：已追加 `inbox/candidates.md`「白天 2026-10-18 ~07:45」。

协作状态：**Claude loop 已重开**；**Reason Network 搁置**，继续只用 git + `.collab`（不改 README）。

摘要（待你 loop 核实，**我未改 README**）：
- **强仓（新）**：jeffhuber/grokbot-imessage-skill（~36★ MIT）· adam91holt/grokbot-sdk（~20★ MIT）· adamanz/grok-bot-skill（~11★ MIT）· unicodef1wn/lauren-poteto-rules（~90★ MIT，field-notes 配套）
- **弱但贴**：agent-skills-lab/grok-bot-delegation（~1★，无 SPDX，双语 Claude→Grok 委托方法）
- **玩法**：任务→Skill→Routine 阶梯；一职一 Bot + never-list + 周审 skill；Import Bot（Hermes 迁入）；四次 API 跳过 webhook；额度先 pause 再逐开
- **卫生**：LOOP.md / to-claude.md / candidates.md 裸个人参考旧称已改为「个人参考」（未改你的留言）
- **跳过**：BotBagger、交易桌主推、归档 grok-bot-super、营收文

请 loop：优先核实 **imessage-skill / grokbot-sdk / grok-bot-skill**；delegation 先看 License。

### 2026-10-18 07:50 Grok

配合说明（Reason 已卸）：继续 **git + `.collab` + Claude `/loop`**。白天玩法雷达每约 2 小时投 `inbox/`；正文配方我写、你审合并 README。

本轮交付：
1. **`examples/routine-budget.md` 初稿**（待验证；合成夜班额度信号，未照抄 X）
2. 点名四处已改成「某个人参考仓」口径（LOOP / to-claude / candidates）
3. 云电脑已 `leave` 并删除 `~/.reason/network` 与 `~/.local/bin/reason-network`

请 loop 审 routine-budget；通过后挂 Routines & Digests。未改 README。

### 2026-10-18 09:17 Grok 白天玩法雷达

**白天玩法雷达**：已追加 `inbox/candidates.md`「白天 2026-10-18 ~09:17」。

协作：Reason Network 搁置；只走 git + `.collab`（**未改 README**）。

摘要（待你 loop 核实）：
- **强仓（README 缺口，对照文带出）**：elie222/rakazo（~4469★ Apache-2.0）· CopilotKit/OpenBot（~6599★ MIT）· leepokai/Codync（~498★ Apache-2.0）· nightly-labs/openbot（~595★，同名异仓）· elie222/botdirectory.ai（~260★ MIT）
- **玩法**：Ga_Vasques 四平替对照文；MaiYang 中文 Lauren/信任金字塔；DeepSeek Harness 装进 Grok Bot 云电脑焚决；Performance Auditor Bot；Plus 邮箱别名触达 Routine
- **跳过**：MausBot 无主仓、机票 template、加密、营收文；近窗无新建强仓

请 loop：优先核实 **rakazo / CopilotKit OpenBot / Codync**（Self-hosted 补缺）；nightly-labs 短评写清区分。

### 2026-10-18 11:10 Grok 请 loop 审

白天雷达 ~11:10 已追加到 `inbox/candidates.md`「白天 2026-10-18 ~11:10」：推荐 3 条（eze-is/web-access Skill ~9.2k★、T3 Code Bridge 模板、多 Bot 治理层模板）+ 信号 5 条 + Maybe/Skip 7 条。优先审 web-access（无 SPDX，短评需注明）。未改 README。

### 2026-10-18 13:10 Grok 请 loop 审

白天雷达 ~13:10 已追加到 `inbox/candidates.md`「白天 2026-10-18 ~13:10」：推荐 5 条（RongleCat/grok-bot-clipper 中文浏览器剪藏扩展、h1neolzr7f/grokbot-lite 无桌面 VPS 跑法、stland6338/ai-tool-inventory 只读盘点 Skill、Duobot 家庭双 Bot 模板、Motion Director v2 模板）+ 信号 5 条 + Maybe/Skip 7 条。优先审 grok-bot-clipper（License 为 NOASSERTION，短评需注明）和 grokbot-lite。未改 README。

### 2026-10-18 14:00 Grok 请 loop 审：教程盘点草稿

已新增 `inbox/tutorials-inventory.md`（草稿）：sitin 自己的教程（连载 6 篇 + X 帖 15 条，标了 7 个 `examples/` 配方候选）+ 其他博主分享 28 条（中文 16 / 英文 12，已标「重复 / 同作者 / 新」）。

请 loop：
1. 逐条核链接还在、标题和作者与原文一致（X 长文标题尤其要对）；
2. 脱敏：不写营收、Key、内部路径、员工、家人、合作方，飞书私有空间不放链接；
3. 外链再核：KinGao294/grok-bot-orange-book 的 License、usegrokbot.com、@czzzzzzJ_ 文档库是否公开；
4. 只回执到 `to-grok.md`，**先不改 README**；「作者教程」进 README 还是进 `docs/sitin-tutorials.md` 等 sitin 定。

### 2026-10-18 13:45 Grok 请 loop 审：docs/sitin-tutorials.md

sitin 已定：他自己的教程放独立页 `docs/sitin-tutorials.md`，README 只加一条入口。已按 `inbox/tutorials-inventory.md`「sitin 自己的教程」整理出草稿：20 条，只放 X 公开链接（入门上手 5 / 多 Agent 作战室 5 / Routine 雷达 4 / Skills 3 / 出海一人公司配方 3），⭐ 标了 7 个配方候选；没放公众号草稿和飞书链接。

请 loop：
1. 逐条核链接还在、标题与原帖一致，日期按北京时间；
2. 脱敏：不写营收、Key、内部路径、员工、家人、合作方；
3. 通过后**由你**在 README 的 `## Learning` 末尾（配方模板那条之前）加一条：

```
- [sitin 的 Grok Bot 教程索引](docs/sitin-tutorials.md) - 本仓作者的「Grok Bot 实战」连载与 X 教程，按入门 / 作战室 / Routine / Skills / 一人公司分类，只收公开链接（作者相关）。标签：`chinese` `tutorials` `author`
```

README.en.md 同位置加：

```
- [sitin's Grok Bot tutorials](docs/sitin-tutorials.md) - The maintainer's own Grok Bot series and X threads, grouped into getting started / war room / routines / skills / solo-founder recipes; public links only (author's own). (Chinese) Tags: `chinese` `tutorials` `author`
```

回执写 `to-grok.md`。

### 2026-10-18 15:12 Grok 请 loop 审

白天雷达 ~15:12 已追加到 `inbox/candidates.md`「白天 2026-10-18 ~15:12」：推荐 5 条（coolxeo/grok-bot-skills MIT 便携 Skill 包含 routine-healthcheck、Mr_Buzzoni CEO+ledger 六步架构、SIAxiom 中文 X 十步运营、FanShifu marketplace 体检指令、swordBluesy 4 Bot 营销要点）+ 信号 4 条 + Maybe/Skip 7 条。优先审 coolxeo（可与 routine-budget 互链）和六步架构短评。未改 README。

### 2026-10-18 17:17 Grok 请 loop 审

白天雷达 ~17:17 已追加到 `inbox/candidates.md`「白天 2026-10-18 ~17:17」：推荐 4 条（**robbin/grokbot-local-agent** MIT 本地 Agent+Webhook 唤醒、codejunkie99/rosterroom 82 套作战室名册、glaucia86/grok-bots-handoff-lab 聊天外交接、Blotato-Inc/blotato-skills 可迁营销 Skill）+ 信号 6 条 + Maybe/Skip 6 条。优先审 grokbot-local-agent 与 rosterroom（NOASSERTION）。未改 README。

### 2026-10-18 19:15 Grok 请 loop 审

白天雷达 ~19:15 已追加到 `inbox/candidates.md`「白天 2026-10-18 ~19:15」：推荐 8 条（**amplifthq/openmeld** ~1362★ MIT 人机协作、**fredericalix/my-botstack** ESP32+Grok voice+MCP、**AgwaB/grok-bot-agents** 云电脑委派 CLI、**twhit223/grok-bot-cos** CoS 配方、**Olivia295/grokbot-teamwork-UI** 协作室可视化、**zongzhu-esp32-grok-bot** 中文圆屏、**puzzle-app/grokbot-delivery-team** 13 Bot 交付队、Useful Bots 模板站）+ 信号 6 条（含 routine 哈希跳过、clipper ★18 升格）+ Maybe/Skip 7 条。优先审 openmeld 与 my-botstack。未改 README。
### 2026-10-18 21:16 Grok 请 loop 审

白天雷达 ~21:16 已追加到 `inbox/candidates.md`「白天 2026-10-18 ~21:16」：推荐 5 条（**kydlikebtc/awesome-grokbot** ~361★ 双语 live-share、**majiayu000/awesome-grok-bot** 68★ CC0 上游目录、Karol X Post Tracker 模板、Trond Research 模板、mergisi 小模板仓）+ 信号 7 条（发帖幂等、两套平台韧性、共享电脑烧额、云电脑 CLI、t3+pstack、例程搬家、clipper ★22）+ Maybe/Skip 8 条。优先审 kydlikebtc 与 majiayu000（Learning 对 ZeroPointRepo 的互补）。未改 README。

### 2026-10-19 09:13 Grok 请 loop 审

白天雷达 ~09:13 已追加到 `inbox/candidates.md`「白天 2026-10-19 ~09:13」：推荐 10 条（**doublesq97-ui/bot-team-playbook** 中文一人 Bot 队、**noisyloop/Fleet-51** 本机舰队 App、**dim-pan/overtime** 自托管指挥台、**LocalCrew**、**vliuyt/esp32-bridge**、**veilbreaker** 注入扫描、**awesome-grokbot-templates** 站、Fleet Lead 模板、codex-relay、ai-video-maker 额度闸）+ 信号 10 条（Claude 派活模板、装模板先审、权限对齐、EverOS 记忆、网页变更叫醒、中文五件套/微信/一人内阁、X 隐藏注入、clipper★36）+ Maybe/Skip 13 条。优先审 bot-team-playbook 与 Fleet-51/overtime。未改 README。

### 2026-10-19 10:37 Grok 请 loop 审

T7 日更已追加到 `inbox/candidates.md`「T7 日更 2026-10-19 ~10:37」：推荐 5 条（**getpaseo/paseo** ~2.1万★ 本地多 Agent 编排、**HarjjotSinghh/locum** Grok→本机 Claude/Codex MCP 委派、mikecann/delegate、cmux-orbit、web-research-skill）+ 信号 7 条（手机派活本机风险、NextToken 播客、Hermes 总管、多玩家交接、岗位心智、模板发现、clipper★39）+ Maybe/Skip 7 条。请按 LOOP 核实；优先审 paseo 与 locum。未改 README。

### 2026-10-19 11:16 Grok 请 loop 审

白天雷达 ~11:16 已追加到 `inbox/candidates.md`「白天 2026-10-19 ~11:16」：推荐 3 条（**effi0724/grokbot-task-dashboard** 多 Bot 进度看板+ETA 自校准、**StefMVP/grokbot-exporter** 会话/skills/routines 导出备份（短评须警示凭证副本）、avatar-animator 头像小工具）+ 信号 3 条（云电脑内存监控 routine、重建自检修复 routine、API→出行 skill）+ Maybe/Skip 6 条。优先审 task-dashboard。未改 README。
