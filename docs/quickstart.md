# Grok Bot 快速上手

[English](quickstart.en.md) · [回到 README](../README.md)

写给第一次用 Grok Bot 的人。花一个下午走完 5 步，你会有一个每天自己干活、不乱烧额度、碰到不可逆操作会先问你的 bot。

每一步都只链本仓核实过的资源。本仓非官方，界面和套餐以 [官方](https://x.ai/bot/marketplace) 为准。

| 步骤 | 做什么 | 用时 | 用到 |
|---|---|---|---|
| 0 | 设安全底线 | 5 分钟 | 下面的清单 |
| 1 | 导入第一个 bot，派一件小活 | 10 分钟 | 模板市场 |
| 2 | 把一次手动操作教成技能 | 15 分钟 | [Teach-a-Task 配方](../examples/teach-a-task.md) |
| 3 | 开第一条 Routine | 15 分钟 | [X 雷达配方](../examples/x-radar.md) |
| 4 | 给额度加护栏 | 10 分钟 | [额度体检配方](../examples/routine-budget.md) |
| 5 | 需要时再上多 Bot | 按需 | [作战室配方](../examples/war-room.md) |

> 本仓 10 个配方目前都是 🔍 或待验证，还没有 ✅ 真机跑通的。照着做时留意界面差异，跑通了欢迎 [回来报告](../CONTRIBUTING.md)。

## 先分清三个词

| 词 | 是什么 | 一句话 |
|---|---|---|
| **bot** | 有名字、有岗位的 AI 队友 | 多个 bot 共用一台一直开着的云电脑（浏览器、文件、终端） |
| **Routine** | 定时或按事件自动跑的任务 | 最容易烧额度的地方 |
| **Skill** | 教会 bot 的可复用做法 | 教一次，下次少问你 |

Grok Bot 和聊天助手 Grok、编码命令行 Grok Build 是三个不同的产品。

## 第 0 步 · 设安全底线（5 分钟）

动手前先做完这几件事，后面就不用回头补救：

- [ ] **装了桌面端，就关掉「在这台电脑上执行」和「经此电脑转发流量」**。云端 bot 不该碰你本机的文件和密钥（[@fankaishuoai 的提醒](https://x.com/fankaishuoai/status/2111740064409756037)）
- [ ] **画清不可逆线**：发帖、对外发信、付款、删文件、`git push`，一律先出草稿，你确认后再动手（[@wutujiang1999 的上手四步](https://x.com/wutujiang1999/status/2112034366998315408)）
- [ ] **别把 key、token、cookie、账单截图贴进对话**
- [ ] **在大陆网络下用**：网站行为反常时先查 bot 电脑的出口 IP（[@chenmo 的踩坑](https://x.com/chenmo/status/2110380646824816682)）

导入模板、装 skill、接 MCP，都等于把权限交给 bot。看清它能碰哪些账号再点。

## 第 1 步 · 第一个 bot：先导入，别从零写（10 分钟）

1. 打开官方 [模板市场](https://x.ai/bot/marketplace)，挑一个和你岗位最接近的模板，点 Add 导入
   - 想一次装一整支团队，可以看 [botteams](https://github.com/ellelion/botteams) 里标了 `installable` 的团队
   - 模板太多不知道挑哪个，翻 README 的 [模板与目录](../README.md#-模板与目录)
2. 派一件**这周你已经手动做过 3 遍以上**的小活，比如：
   - 每天的增量简报
   - 一篇内容改写成三个平台的版本
   - 收件箱分拣
   - 睡前列出明天要做的事
3. 验收产出。不满意就改岗位说明和规则，比在聊天里反复纠正更省事

**过关标准**：bot 交回一份你愿意直接用的产出。

## 第 2 步 · 把一次手动操作教成技能（15 分钟）

照 [Teach-a-Task 配方](../examples/teach-a-task.md) 做：

1. **示范**：你完整做一遍，bot 只看不动手
2. **出技能卡**：让 bot 写出目标、步骤、成功标准和禁止事项，会变的东西都换成 `{{占位符}}`
3. **你改一版**：删掉真实路径和账号，补上不许做的事
4. **干跑**：用假数据走一遍，只出计划，不真动手
5. **签收**：确认无误后，以后同类任务都按这张卡执行

**过关标准**：第二次做同类任务时，bot 不用再问你步骤。

## 第 3 步 · 开第一条 Routine（15 分钟）

照 [X 雷达配方](../examples/x-radar.md) 开一条每天跑 1 次的 Routine。新手最该守的三条：

- **每天 1 次就够**：别设成每小时，容易撞限流，摘要也会变碎
- **没信号就闭嘴**：没有实质内容时只输出「无更新」，不推送
- **只读不互动**：点赞、回复、发帖都由你来

不做 X 的话，可以换成 [竞品雷达](../examples/competitor-radar.md) 或 [周报 routine](../examples/weekly-review.md)，原则一样。

**过关标准**：连续 3 天，有信号的日子推一份能看的摘要，没信号的日子不打扰你。

## 第 4 步 · 给额度加护栏（10 分钟）

Routine 一多，额度就会悄悄烧光。按 [额度体检配方](../examples/routine-budget.md) 先把规矩定下来：

```text
[ ] 高频 Routine 不挂在你天天聊天的那个 bot 上
[ ] 只在工作日白天跑（比如 9–19 点）
[ ] 「无变化也汇报」的 prompt 改成静默
[ ] 测试用的 on-demand 用完就关
[ ] 每周固定一次额度体检：KEEP / SLOW / EVENT / CHANGE / RETIRE
```

额度已经快见底了：先全部暂停，再按配方逐条重开。

套餐怎么选，看 [@op7418 的订阅档位说明](https://x.com/op7418/status/2109839549706969259)。

## 第 5 步 · 需要时再上多 Bot（按需）

单个 bot 稳定跑一周后再考虑这一步，别第一天就建团队。

| 你的情况 | 先看 |
|---|---|
| 想让 3–6 个 bot 分工跑情报和草稿 | [作战室](../examples/war-room.md) |
| 一个人做出海产品 | [一人三岗](../examples/one-person-three-roles.md)、[出海客服](../examples/outbound-support.md) |
| 想让 bot 接 GitHub issue，但不敢让它直接合并 | [研发四角色](../examples/dev-four-roles.md) |

多 Bot 的两条铁律：
- **只靠文件交接**，不在群里乱聊
- **发布前必须过人工闸门**

更多团队做法见 README 的 [多 Bot 团队](../README.md#-多-bot-团队)。

## 按身份挑路线

| 你是 | 先读 | 再抄 |
|---|---|---|
| 不写代码的人 | [非工程师怎么用好 Grok Bot](https://x.com/KinGao476942/status/2097915898971742325) | 额度体检 → 周报 |
| 工程师 | [工程师如何用好 Grok Bot](https://x.com/KinGao476942/status/2096232745538334913)、[grokbot-field-notes](https://github.com/unicodef1wn/grokbot-field-notes) 的 `AGENTS.md` | 研发四角色 |
| 做内容、做出海 | [X 上 Grok Bot 必读文章合集](https://x.com/0xlangeai/status/2111396742264742034) | X 雷达 → 作战室 |
| 不想上云、想用自己的模型 | README 的 [自托管与平替](../README.md#-自托管与平替) | — |

## 新手最常踩的坑

- **一上来就开一堆 Routine**：额度几天见底，还说不清是哪条在烧
- **在聊天里口头纠正，不改规则**：下次照错。改了流程就回写技能卡或岗位说明
- **让 bot 自己发出去**：发帖、发信、合并代码先出草稿，你点头再发
- **信模型编的链接**：雷达类产出要抽查链接能不能打开
- **把真实路径、账号写进要分享的技能**：公开前换成占位符

## 下一步

- **想系统学**：[Grok Bot 橙皮书](https://github.com/KinGao294/grok-bot-orange-book)（中文，约 1.6 万字）、[GrokBotGuide](https://github.com/JeffShanCha/grokbotguide)（中英双语手册）
- **想看别人怎么用**：[社区教程精选](community-tutorials.md)、[X 大 V 文章精选](x-articles.md)
- **想找现成的**：README 的 [目录](../README.md#-目录)
- **跑通了某个配方**：按 [贡献指南](../CONTRIBUTING.md) 回来报告，可以给它打上 ✅
