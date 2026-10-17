# Field notes

> 日期：2026-10-18（Asia/Shanghai）
> 验证级别总说明：本机 box **无法**端到端跑 Grok Bot GUI 配置。本轮是 **文档审阅 + 仓库结构/样例配置可读 + 公开 API/raw URL 冒烟**；**未能真机跑通**。未 star / fork。

---

## 1. [botteams](https://github.com/ellelion/botteams)

| 项 | 内容 |
|----|------|
| 建议标签 | ✅ 结构扎实，可作作战室编排参考 |
| 验证级别 | 文档审阅 / 配置可读 / API 冒烟 / **未能真机跑通** |
| License | MIT |
| 规模（clone 当日） | `teams/` 15 · `bots/` 60 · 站点 [botteams.io](https://botteams.io) |

### 试了什么

1. shallow clone 公开仓，读 README、CONTRIBUTING、`docs/examples/sample-team.md` / `sample-bot.md`
2. 精读可安装样例：`teams/engineering-release.md`、`teams/founder-os.md`（front matter：`bot_roster` / `rooms` / `routines` / `connector_modes` / `suggest`）
3. 公开 API 冒烟：`GET https://botteams.io/api/teams?limit=3` → `version: 2`，返回 `botRoster` 等字段正常
4. **未**在 Grok Bot 里粘贴 installer prompt，**未**真建 bot / 群聊 / routine

### 结果（结构结论）

- 产品模型清楚：**一个 markdown = 一支团队**；站点从 front matter 生成 installer prompt，粘贴进 Grok Bot 后由 Bot 创建命名 Bots、群聊，并提议 routines 等人确认
- `kind: team|bot` + `status: installable|example` + JSON Schema（`team.schema.json`）+ CI，贡献门槛写明「你自己端到端跑过」
- 护栏写进 persona / `suggest`：常见「Never send mail / Never merge or deploy / Never move funds」；`connector_modes` 为 `read|draft|ask`
- **关键诚实点（文档原话）**：connector mode 是 **prompt 措辞，不是权限**；Grok Bot 连接器账号级共享，多 Bot **不是安全边界**，真正开关在 Settings → Plugins

### 用户须准备

- 可用的 Grok Bot 账号与对应 Plugins（GitHub / Gmail / Stripe 等按团队清单）
- 从团队页或 Customize 复制 **installer prompt**（Customize 存在 URL hash，可分享、站点不存）
- 理解：建完后仍要人工确认 routines；发信 / 合并 / 动资金等动作靠人闸，不靠多 Bot 隔离

### 坑

- 误以为 `connector_modes: draft` = 产品级只读 → 实际仍靠 prompt 自律
- 未先连 Plugins 就装团队 → Bot 会卡在要授权
- `status: example` 与 `installable` 混用 → example 是格式演示，不是可跑 listing
- 仓内还有站点自身的 Stripe / X mention worker / DB 等（`.env.example` 仅变量名）；**用目录装团队不需要那些 key**，别当成 Grok Bot 配方依赖
- 大量 `from_xai: true` 单 bot 来自 xAI use-case 改写，是 sourcing 不是 xAI 背书

### 本仓配方能否引用

- **可以**。与 `examples/war-room.md`、README Multi-bot teams 高度同构（群聊 + 角色 + routine + 人闸）
- 适合作「一整支团队一次装好」的外部样例链接；引用时注明验证级别，勿写成「本仓已真机跑通」
- 引用优先 `installable` 团队（如 engineering-release / founder-os），避免 example 模板当成品

---

## 2. [grok-bot-profiles](https://github.com/HAEGONG/grok-bot-profiles)

| 项 | 内容 |
|----|------|
| 建议标签 | ✅ 审批边界写得极清楚，研发分工可直接套结构 |
| 验证级别 | 文档审阅 / 配置可读 / raw URL 200 / **未能真机跑通** |
| License | CC BY 4.0（改编需署名 + 链回仓与许可证） |
| 规模（clone 当日） | 4 个 development profile + `templates/bot/` |

### 试了什么

1. shallow clone，读 README（含 mermaid 工作流）、CONTRIBUTING、CREATE_YOUR_OWN_BOT
2. 精读四角色 `PROFILE.md` / `SETUP.md` / `README.md`：Spec Writer、Bug Reproducer、PR Producer、PR Verifier
3. raw URL 冒烟：`SETUP.md` / `PROFILE.md` → HTTP 200（安装路径依赖 raw，不可本地文件 import）
4. **未**在 Grok Bot 创建上述 Bot，**未**走 Spec→批准→PR→Verifier 真链路

### 结果（结构结论）

- 安装路径明确：新建 Bot → 粘贴 **SETUP.md raw URL** 作首条消息 → Bot 拉取 PROFILE 填 Name/Title/Description → 连 GitHub → 发 First task；**不要**手贴 PROFILE 进 Description
- 三文件契约清晰：`PROFILE.md` 耐久身份与边界；`SETUP.md` 一次性安装+操作清单；`README.md` 集成与 First task
- 核心设计：**产出与校验分离**；交接 ≠ 批准；PR Producer 与 PR Verifier **不得同 Bot / 同会话 / 同生产群**
- 状态词收紧：如 Spec 仅 `READY_FOR_APPROVAL|NEEDS_INPUT|BLOCKED`；Verifier 仅 `PASS|BLOCK|HOLD`；缺证据用 HOLD 而非猜
- 文档同样写明：同账号 Bot **共享电脑与浏览器会话**，角色分离保护的是**裁决依据**，不是安全沙箱

### 用户须准备

- Grok Bot + **GitHub** Plugin；PR Producer 还依赖内置 **Cursor Cloud Agent**（文档称无需额外 plugin）
- 生产三角色可同群；**PR Verifier 单独对话**，只收 PR URL
- 改编/二次发布注意 **CC BY 4.0** 署名义务（与 botteams 的 MIT 不同）

### 坑

- 把群里出现的草稿当成下一角色开工信号 → 违反「仅用户直呼或显式 handover」
- 把 handover 当成对 Spec/brief 的批准 → Producer 仍要用户点名版本批准后才实现
- Verifier 与 Producer 同群或转发带评论的交接 → 应 HOLD，要求干净 URL-only
- 无 GitHub / Cloud Agent 权限时链路在 Producer 处断
- 只审文档时容易高估「边界=权限」；实际仍是 prompt 契约 + 人闸

### 本仓配方能否引用

- **可以，且强烈建议**作研发向多 Bot 护栏范本
- 可支撑未来 `examples/` 里「需求 / 复现 / 出 PR / 验 PR」类配方；与现有 war-room「人闸门后再发」互补（本仓偏运营编排，该仓偏工程审批）
- 引用时标明 CC BY 与「未能真机跑通」；短评勿暗示已替代官方 docs

---

## T8 进度（本周实测）

| # | 对象 | 标签 | 验证级别 |
|---|------|------|----------|
| 1 | botteams | ✅ 结构可推荐 | 文档/配置/API · 未真机 |
| 2 | grok-bot-profiles | ✅ 结构可推荐 | 文档/配置/raw · 未真机 |

本周 ≥2 条 field note：**已达标（结构向）**。真机 GUI 跑通仍缺，后续若有本机 Grok Bot 会话可补「配置可读 → 真机跑通」升级记录。

---

提交前自查：无 key / token / cookie 值，无营收数字，无内部业务路径，无可识别个人信息；未改 README。
