# Grok Bot 教程盘点（草稿）

> 状态：**草稿，待 Claude loop 核实链接 + 脱敏**；未进 README。
> 盘点时间：2026-10-18（北京时间）。来源：X 公开接口（@sitinme 时间线 + 关键词搜索，窗口约 2026-08-18 至 2026-10-18）、本仓连载排期。
> 日期均为北京时间；互动数（赞 L / 收藏 BM / 浏览 V）为抓取时快照，仅作排序参考，不进 README。
> 原则：Awesome 仓只放「标题 + 一句短评 + 原文链接」，正文留在原处。
> 建议分类（对齐本仓分类）：入门上手 · 多 Agent 作战室 · routine 雷达 · skills · 出海一人公司配方。
> 「重复」= 已在 `inbox/candidates.md` 或 README 里出现过（同一条帖子）；「同作者」= 作者的其他内容已收过，这条是新的。

---

## 一、sitin 自己的教程

### 1.1 「Grok Bot 实战」连载（X 长文 / 公众号）

公开链接只列 X 上已发的版本。公众号这几篇目前都在草稿箱或还没推，群发后再补 `mp.weixin` 链接。飞书 Grok 知识库是私有空间，**不放链接**。

- [我养了十几个 Grok机器人，起飞！](https://x.com/sitinme/status/2109814883688796459) — 2026-10-13 · 连载总起：一个首席助理 + 十几个专职机器人，一句话派活、每天定时收总简报、对外动作必须人点头；X 长文，L290 / BM693 / V11.4 万 · `多 Agent 作战室` `入门上手` ⭐ 配方候选
- [升级 $300 的 Grok bot，我让 AI 并行干了这几件事](https://x.com/sitinme/status/2110304146628976881) — 2026-10-14 · 额度条从 97% 到放开用：第一晚并行跑哪些长任务、Heavy 值不值；公众号版标题「半夜升级了 $300 的 Heavy…」在草稿箱 · `routine 雷达` `入门上手`
- [一头连云端电脑，一头连我的 Mac：Grok Bot 最被低估的能力](https://x.com/sitinme/status/2110579602133237816) — 2026-10-15 · 手机上说三句话：云端写稿排版 → 连本机 Mac 用本地脚本推公众号草稿箱；讲清楚云电脑和本机各自该干什么；公众号版在草稿箱 · `skills` `出海一人公司配方` ⭐ 配方候选
- [牛逼！Grok Bot 帮我揪出 240 美金（10 个月没人用，我还在付钱）](https://x.com/sitinme/status/2111358802368827741) — 2026-10-17 · 只读授权 Vercel 做账单审计，找出 2 个闲置席位；另附几千行流水整理成脱敏 PDF、无脸短视频从脚本到成片、喂官方指南；X 串帖，公众号版在草稿箱 · `出海一人公司配方` `skills` ⭐ 配方候选
- 《Claude Code 停了、GPT 也限了，我 12 秒在 Mac 装上 Grok 命令行》 — 2026-10-15 · 已写完，未推草稿箱、未公开，**暂无链接** · `skills`
- 《39 个 AI 机器人，我砍掉了一批：一次大盘点做的 8 项优化》 — 2026-10-16 · 初稿，含「国内免翻墙」一节，**暂无链接**；发出后可作「机器人多了怎么做减法」配方 · `多 Agent 作战室` `routine 雷达`
- 排期中（未写完，发出后补链接）：翻完 30 条老外玩法我抄了 5 个 · Grok Bot 住进飞书 · X 雷达改成每天 4 档省额度 · 公众号一步到位流水线 · 给 AI 团队定规矩（单一入口 + 三档审批）

### 1.2 X 帖子（@sitinme，Grok Bot / 多 Agent 相关）

- [gork bot 用起来，小龙虾牛逼 Plus 版：十几个机器人每个只管一件事](https://x.com/sitinme/status/2109628651897594022) — 2026-10-12 · 列出每个机器人的岗位（X 运营官、早报、调研、写作等）和一键建机器人的体感；L57 / V1.4 万 · `多 Agent 作战室` `入门上手`
- [Grok bot 自动管理其他机器人 + 飞书 CLI 同步](https://x.com/sitinme/status/2109990284771872987) — 2026-10-13 · 让首席机器人去管其他机器人的状态，所有信息经飞书 CLI 同步到飞书，国内办公场景少见的实操；L34 / V4.6k · `多 Agent 作战室` `skills` ⭐ 配方候选
- [我睡觉的时候，AI 团队干了啥](https://x.com/sitinme/status/2110181293824553314) — 2026-10-14 · 一晚并行 5 件事：夜间长任务、新建「公司群」拉入 HRBP/财务/法律助手（合同模板一律标「须律师审核」）、4 周学习助手等；L35 / V1.2 万 · `routine 雷达` `多 Agent 作战室` ⭐ 配方候选
- [花 $300 升级 Grok Bot，终于体验到十几个 AI 同时干活](https://x.com/sitinme/status/2110720093613150324) — 2026-10-15 · 用到 97% 额度后升 Heavy 的真实体感：不是更聪明，而是敢放开跑；L61 / BM61 / V8.2k · `入门上手` `routine 雷达`
- [Cursor 并进 X 订阅，晒下我自己的账](https://x.com/sitinme/status/2109840998910276066) — 2026-10-13 · Premium+ → SuperGrok Heavy 的选择理由，适合放「套餐怎么选」；V6.6k · `入门上手`
- [公众号自动发布流程：一条命令都没敲](https://x.com/sitinme/status/2110901539321856242) — 2026-10-16 · 云端电脑写稿、排版、处理图片 → 连接本机 Mac 推公众号草稿箱 → 同步飞书知识库，分步骤写清；L45 / BM66 / V5.9k · `出海一人公司配方` `skills` ⭐ 配方候选（与上面「一头连云端」合并成一个配方）
- [每个 Grok Bot 都有自己的邮箱了](https://x.com/sitinme/status/2110233522409742396) — 2026-10-14 · 订阅和通知让 bot 的邮箱收，读完再汇总给我，自己的邮箱保持干净；配合[每天早上让 grok 读 Gmail 找问题](https://x.com/sitinme/status/2110234159344218280) · `skills` `routine 雷达` ⭐ 配方候选
- [DeepSeek Bot（DS Bot）：Grok Bot 的开源免费平替](https://x.com/sitinme/status/2110975023531839754) — 2026-10-16 · 串帖讲 DS Bot 群聊长什么样、怎么装（含国内镜像源）、群聊费 token 和权限分级的坑、怎么选；L42 / V7.3k · `入门上手`（平替对照，可挂 Self-hosted 旁注）
- [生财 MCP 接入 Grok Bot，副业玩法不遗漏](https://x.com/sitinme/status/2111647666346361273) — 2026-10-18 · 把第三方社群知识库经 MCP 接进 bot 当信息源；L21 / BM21 / V4.4k · `skills` `出海一人公司配方`
- [多 Agent 消息要分频道，不能全塞一个聊天框](https://x.com/sitinme/status/2111425240492281976) — 2026-10-17 · 读文章笔记：上游任务 / 下游汇报 / 同级协调 / 人工介入 / 系统告警分开，否则权限混乱、回复发错地方；和本仓「作战室只靠文件交接」一个思路 · `多 Agent 作战室`
- [养了十几个 Grok Bot，最头疼每个都要重新交代背景](https://x.com/sitinme/status/2109890718567473547) — 2026-10-13 · memory transfer 对多机器人是刚需（短帖，可并入作战室配方的「记忆」一节） · `多 Agent 作战室`
- [个人 Agent 赛道扎堆：Grok Bot / Muse / Cue / dots 门槛对比](https://x.com/sitinme/status/2105180871682884093) — 2026-09-30 · 订阅门槛、地区、功能定位对比，入门选型用；V3.4k · `入门上手`
- [GrokBot 都用上了么？值得借鉴的 11 点](https://x.com/sitinme/status/2094964024630989241) — 2026-09-02 · 转述 Agent Native 整理：监控 bot、接 X 分析数据、Slack 触发等 11 条，结论是先留一个通用入口，重复了再拆岗位 · `入门上手` `多 Agent 作战室`
- [X 自动化内容工作流：Grok 找素材 → Claude/Codex 写 → Grok 挑错 → 发布 → Webhook 复盘](https://x.com/sitinme/status/2094687048288674268) — 2026-09-01 · 内容生产链路，偏 Grok 模型而非 Grok Bot，可当 routine 参考 · `routine 雷达` `出海一人公司配方`
- [Anthropic：怎么做一个能长期运行的「每日简报」机器人](https://x.com/sitinme/status/2108461964116865055) — 2026-10-09 · 每个信息源存书签增量读、读失败要明说、发前复核状态；不是 Grok Bot 专属，但正是雷达 routine 的设计要点；L272 / BM310 / V1.8 万 · `routine 雷达`

### 1.3 建议做成 `examples/` 配方的 top 7（脱敏后）

1. **首席 + 十几个专职机器人**（长文《我养了十几个 Grok机器人》+ 10-12 分工帖）→ 新配方「一人 AI 团队编制表」，补到作战室旁边
2. **云端写稿 + 本机推草稿箱**（「一头连云端电脑」+ 10-16 公众号流程帖）→ 新配方「云端 × 本机发布流水线」，脚本路径、账号全部去掉
3. **只读账单审计**（240 美金串帖）→ 新配方「只读 SaaS 账单体检」：只读授权、不改设置、不读环境变量，人工确认后再动
4. **夜间并行长任务**（「我睡觉的时候」）→ 新配方「夜班批处理」，白天收结果、对外动作一律等审批
5. **首席管机器人 + 飞书同步纪要**（10-13 帖）→ 新配方「飞书纪要同步」，国内办公差异化
6. **Bot 专属邮箱分拣**（10-14 邮箱帖 + 读 Gmail）→ 新配方「Bot 邮箱收订阅 + 早间问题清单」
7. **额度 97% → 分档**（Heavy 帖 + 待发「X 雷达改 4 档」）→ 不新开，补进已有 `examples/routine-budget.md` 作真实案例

---

## 二、其他博主分享

### 2.1 中文

- [10 条必备经验，让你的 Grok Bot 变得更好用（@eze_is_1）](https://x.com/eze_is_1/status/2109850538045264151) — 2026-10-13 · X 长文：什么时候用 Bot、怎么搭 multi-bots 工作流等 10 条实测经验，中文圈引用最多的入门文之一；L343 / BM706 / V5.6 万 · `入门上手` `多 Agent 作战室` · 同作者（web-access、eze-grokbot 已收），本帖新
- [X 上 Grok Bot 必读文章合集：9 类 24 篇（@0xlangeai）](https://x.com/0xlangeai/status/2111396742264742034) — 2026-10-17 · 中文高阅读文章索引，可挂 Learning；L428 / BM851 · `入门上手` · **重复**（candidates 已收）
- [Grok Bot 系列教程干货合集（@KinGao476942）](https://x.com/KinGao476942/status/2110689770892648953) — 2026-10-15 · 作者一个多月写的系列：工程师 / 非工程师 / 自媒体怎么用好 Grok Bot 等；L334 / BM653 · `入门上手` · 同作者（DeepSeek Harness 帖已收），本帖新
- [Grok bot 橙皮书（@KinGao476942）](https://github.com/KinGao294/grok-bot-orange-book) — 2026-09-11（[推文](https://x.com/KinGao476942/status/2098259606241980676)）· 开源中文入门到进阶手册，作者建议直接喂给 bot 当上下文；L28 / BM79 · `入门上手` · 新（需核 License）
- [别再让一个 AI 干所有活了：6 天把内容生产拆给 14 个机器人（@ai_goge）](https://x.com/ai_goge/status/2110331990566449273) — 2026-10-14 · X 长文：写短推、长文、公众号、出图、核事实、数据复盘各一个机器人的完整搭建思路；L76 / BM158 / V1.5 万 · `出海一人公司配方` `多 Agent 作战室` · 新
- [Grok bot 省钱教程 + 公开 Prompt 文档库（@czzzzzzJ_）](https://x.com/czzzzzzJ_/status/2109600412366160101) — 2026-10-12 · $20 档怎么够用：省额度的 prompt 模板，附公开飞书文档；L121 / BM129 · `routine 雷达`（额度）· 新（文档库为作者自有飞书，需核是否公开）
- [把 Grok Bot 和本地 Agent 打通：Webhook + GitHub Action（@fankaishuoai）](https://x.com/fankaishuoai/status/2111361067041673452) — 2026-10-17 · 本地 Agent 写任务文档 → 推仓库触发 Bot webhook 接活；另配 Pi Agent 跑其他模型；L67 / BM108 · `skills` · 同作者（本机 Chrome 驱动帖已收），本帖新
- [铁柱 AGI 三篇：额度续航 / Webhook + 快捷指令入库 / Agent 系统备份（@cgnot996）](https://x.com/cgnot996/status/2111402146159861840) — 2026-10-17 · `routine 雷达` `skills` · **重复**（candidates 已收，学习站已进 README）
- [Grok Bot 案例合集网站 usegrokbot.com（@cnyzgkc 推荐，站长 @Chris62771610）](https://x.com/cnyzgkc/status/2095500855797748032) — 2026-09-03 · 收集大量真实案例和高质量文章的导航站；L367 / BM517 / V5.1 万 · `入门上手` · 新（站点本身需单独核实）
- [官方 Grok Bot 教程中文版（@Mileson07）](https://x.com/Mileson07/status/2108384482063688060) — 2026-10-09 · 把官方英文指南整理成中文版，适合不想读英文的人；L54 / BM76 · `入门上手` · 新
- [把 Grok Bot 用成同事：一份能照着做的教程（@Remake___）](https://x.com/Remake___/status/2106996626707607818) — 2026-10-05 · X 长文，按官方文档逐步写，标注了版本日期（易过时要注意）；互动低但内容扎实 · `入门上手` · 新
- [用 Tailscale SSH 连接 Grok Bot 云电脑（保姆级）（@SpringHaoAI）](https://x.com/SpringHaoAI/status/2095915259521585458) — 2026-09-05 · 从自己电脑 SSH 进 bot 的云电脑传文件、看日志、写脚本；BM7 · `skills` · 新（注意：开 SSH 等于扩大权限面，短评需提醒）
- [用 Grok Bot 做开源项目宣传片的实战（@seekjourney）](https://x.com/seekjourney/status/2110986767549739151) — 2026-10-16 · 从产品理解、创意到分镜、画面、视频生成一整套，附提示词；L15 · `出海一人公司配方` · 新
- [用 Grok Bot 自动化一切的全套视频教程（@laobaishare）](https://x.com/laobaishare/status/2092930631546417599) — 2026-08-27 · 带章节：首席助理、多机器人群聊、教技能、5 个真实案例、局限；L24 / BM32 · `入门上手` · 新（疑为搬运英文视频，需核出处）
- [Grok Bot 当总调度，云电脑里装 Codex / Cursor / Gemini CLI 分工（@luhuamfl0）](https://x.com/luhuamfl0/status/2100155813528768516) — 2026-09-16 · 写代码给 Cursor、复杂任务给 Codex、长上下文给 Gemini 的编排思路；互动低 · `多 Agent 作战室` · 新（备选）
- [Grok Bot 教程怎么选？三步走的热门教程（@lanvjian）](https://x.com/lanvjian/status/2109560084418490771) — 2026-10-12 · X 长文，把热门教程按入门 → 进阶 → 实战排了顺序；互动低 · `入门上手` · 新（备选）

### 2.2 英文

- [How To Build a One-Person Company Using Grok Bot（@sairahul1）](https://x.com/sairahul1/status/2089995692874068433) — 2026-08-19 · X 长文：找线索、写外联、做图、回复、周复盘全交给 bot 团队，一人公司主题里传播最广；L4769 / BM1.8 万 / V558 万 · `出海一人公司配方` · 新
- [Grok Bot 20 课实操教程模板（@SawyerMerritt）](https://x.com/SawyerMerritt/status/2103664821459685708) — 2026-09-26 · 可导入的教学模板，从对话、文件、连接应用、Routine、Skill 到团队协作一课一练；L5613 / BM7763 / V68 万 · `入门上手` · 新
- [每周让 Grok Bot 对照新功能检查你的用法（@Michael_Fenech_）](https://x.com/Michael_Fenech_/status/2108145378323542306) — 2026-10-08 · 一条可直接粘贴的周度 routine：比对产品更新和你的实际使用，提示该换的做法；L337 / BM637 · `routine 雷达` · 同作者（额度审查 prompt 已收），本帖新
- [周一 routine：交给 Chief of Staff 的周度自查（@mikepat711）](https://x.com/mikepat711/status/2107130731382079767) — 2026-10-05 · 可复制给首席的 routine 原文；L80 / V39 万 · `routine 雷达` · 新
- [10 分钟搭一整支团队：Chief of Staff 做唯一入口（@zodchiii）](https://x.com/zodchiii/status/2090778823050592662) — 2026-08-21 · 先建首席、粘贴描述字段、再让它建其他岗位的步骤；L132 / BM195 · `多 Agent 作战室` `入门上手` · 新
- [4 分钟搭出「贾维斯」：首席 + 岗位 bot（@Av1dlive）](https://x.com/Av1dlive/status/2090366905169379554) — 2026-08-20 · 早期爆款入门串，偏营销口吻，可作「最小团队」参考；L743 / BM1364 / V299 万 · `入门上手` · 同作者（另一条已收），本帖新
- [像入职新员工一样配 Grok Bot：hire / train / equip（@0xShoopy）](https://x.com/0xShoopy/status/2107874318244032867) — 2026-10-08 · 官方工作坊笔记：一个 bot 一个岗位、演示一次存成 skill、有连接器先用连接器；L42 · `skills` `多 Agent 作战室` · 新
- [25+ bots：Chief of Staff + PM + QA + 15 个 worker 的演示笔记（@shirosignal）](https://x.com/shirosignal/status/2110077526924317019) — 2026-10-14 · 30 分钟演示怎么把一个 bot 变成有分工的团队；L65 / BM97 · `多 Agent 作战室` · 新
- [SpaceXAI 工程师的 Chief of Staff 配置（@0xRafy）](https://x.com/0xRafy/status/2096017149999358316) — 2026-09-05 · 内部工程师 10+ bot 组队、首席掌握全局的做法转述；L194 / BM346 · `多 Agent 作战室` · 新
- [官方 1 小时工作坊要点：从「任务」到「岗位」心智（@AleiahLock）](https://x.com/AleiahLock/status/2095924854335631840) — 2026-09-05 · 官方 workshop 的转述和时间轴；L59 / BM94 · `入门上手` · 新
- [20 个 Grok Bot 相关 GitHub 仓库（@maestrooth）](https://x.com/maestrooth/status/2105310670535184774) — 2026-09-30 · 自托管、加工具、连应用、抄工作流的仓库清单，可用来对照本仓 Self-hosted / Skills 是否漏收；L492 / BM965 · `skills` · 同作者（Jev 帖已收），本帖新
- [How to Grok Bot (Non-Slop)（@im_insulting）](https://x.com/im_insulting/status/2099228547760128299) — 2026-09-14 · X 长文：把非核心任务交给 bot 的实用做法；L14 · `入门上手` · 新（备选）

### 2.3 跳过（不收）

- 「6 个 agent 交易台」「15 分钟三个交易机器人赚 2353 刀」一类：多账号复制粘贴、收益无法核实
- `$GROKBOT` 代币帖、扫码领会员、「17 份指南」搬运串：营销或引流
- 「200+ 泄露仓库」类标题党：先不收，等仓库逐个核实

---

## 三、给 Claude loop 的核对清单

1. 逐条打开链接，确认帖子还在、标题 / 作者与原文一致（尤其 X 长文标题）。
2. 外链再核：橙皮书仓 License、usegrokbot.com、@czzzzzzJ_ 的文档库是否公开可访问。
3. 脱敏：sitin 条目只保留公开内容；不写营收、Key、内部路径、员工、家人、合作方；飞书私有空间链接一律不放。
4. 进 README 时只放「标题 + 一句短评 + 链接 + 标签」，互动数不进 README；建议新开「作者教程」小节或进 `docs/sitin-tutorials.md`，由 sitin 定。
