# 短内容合集（草稿 v1，待涛哥审）

10/19 首发日版本。所有对外发布由涛哥执行。顺序：13:30 社群预告 → 14:00 公开 → 14:10 社群 → 即刻 → X thread（`x-thread.md`）→ 20:00 公众号 + 视频号/小红书。

---

## 1. 视频号 / 小红书脚本 A：额度体检（约 60 秒）

**封面字**：Grok Bot 额度 3 天烧光？先做这 5 步

| 秒 | 画面 | 口播 / 字幕 |
|---|---|---|
| 0–5 | 额度条见底（打码） | 「Grok Bot 一周的额度，三天就烧光了？」 |
| 5–15 | Routine 列表，逐个点暂停 | 「第一步急停：先把不关键的 Routine 全暂停。先止血，再找原因。」 |
| 15–25 | 把雷达 Routine 挪到另一个 bot | 「第二步挪窝：高频雷达别挂在聊天主 bot 上，单独放一个轻量 bot。」 |
| 25–40 | 首席 bot 输出 KEEP / SLOW / RETIRE 分级表 | 「第三步让首席 bot 给每条 Routine 打标签：留着、放慢、退休。它只给建议，不动配置。」 |
| 40–52 | 按顺序重新开启 | 「最后按顺序一条一条打开，每开一条看一轮。」 |
| 52–60 | 仓库首页 | 「完整 prompt 在 awesome-grokbot-playbooks，搜这个名字就能找到。」 |

素材：涛哥实测 routine-budget 的录屏，额度数字和账号全部打码。

## 2. 视频号 / 小红书脚本 B：AI 作战室（约 60 秒）

**封面字**：两个 AI 帮我维护开源仓库，我只拍板

| 秒 | 画面 | 口播 / 字幕 |
|---|---|---|
| 0–6 | 分屏：左边 Grok Bot，右边终端里的 Claude | 「这个开源仓库是两个 AI 在维护。」 |
| 6–18 | Grok 推送候选，`to-claude.md` 滚动 | 「Grok Bot 每两小时去 X 和 GitHub 找新玩法，写进仓库留言。」 |
| 18–32 | Claude 跑 `gh api` 核实，然后改 README | 「Claude 醒来逐个核实：有没有开源许可、还更不更新、和 Grok Bot 有没有关系，再写中文短评。」 |
| 32–44 | `to-grok.md` 回执：收了 3 条、暂缓 5 条、拒 3 条 | 「收什么、拒什么、为什么，都写成回执。」 |
| 44–54 | 涛哥点 merge 或审稿 | 「我只做一件事：拍板。」 |
| 54–60 | 仓库首页 | 「配方和全部协作记录都开源了：awesome-grokbot-playbooks。」 |

## 3. 即刻（中文短帖）

> 一人公司用 Grok Bot，最怕两件事：额度烧光，bot 越开越乱。
>
> 我们做了个中文配方库 awesome-grokbot-playbooks，62 个条目，9 个能直接抄的配方：作战室、X 雷达、出海客服、额度体检……还有 25 篇社区教程精选。每条都标了跑没跑过，✅ 只给真机跑通的。
>
> 仓库本身由 Grok Bot 找料、Claude 核实，我只拍板，协作记录全公开。
>
> github.com/sit-in/awesome-grokbot-playbooks

## 4. 千里会社群

**13:30 预告**

> 今天 14:00 发一个开源项目：Grok Bot 中文配方库。
> 想提前看的、手上有 Grok Bot 愿意帮忙实测配方的，回复「实测」，我拉你进首批。
> 跑通的配方会署你的名。

**14:10 首发通知**

> 上线了：github.com/sit-in/awesome-grokbot-playbooks
> 1. 觉得有用就点个 star，帮它上 GitHub Trending
> 2. 有 Grok Bot 的，去 Issues 认领一个「实测认领」，跑完回帖就行
> 3. 有自己的玩法，按 `examples/_template.md` 投稿
> 今晚我在群里答疑。

## 5. 给 ZeroPointRepo/awesome-grok-bot 的 PR（10/26 前后，涛哥提）

**标题**：Add Chinese playbook collection: awesome-grokbot-playbooks

**正文**：

> Adds a link to [awesome-grokbot-playbooks](https://github.com/sit-in/awesome-grokbot-playbooks), a Chinese-first (with English README) collection of copy-paste Grok Bot recipes: war room, X radar, routine budget check, global support triage and more. Each recipe is marked as run end-to-end (✅), reviewed (🔍) or unverified. Complements this list's English index rather than duplicating it.

**改动**：在对方最合适的分类（Learning / Resources）末尾加一行：

```markdown
- [awesome-grokbot-playbooks](https://github.com/sit-in/awesome-grokbot-playbooks) - Chinese-first, bilingual collection of copy-paste Grok Bot recipes with verification marks.
```

先读对方的 CONTRIBUTING，照他们的格式改。

---

## 发布前自查

- [ ] 数字和当天 README 一致
- [ ] 视频里的账号、额度、私人对话都已打码
- [ ] 无 key / 营收 / 内部路径
