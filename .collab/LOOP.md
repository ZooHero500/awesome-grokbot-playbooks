# 协作 Loop 协议（Claude Code ⇄ Grok Bot）

目标：用 Git + `.collab/` 当邮箱，Claude Code 用 `/loop` **只审不乱改**；Grok 用 routine **只投料不合并 README**。

## 角色

| 角色 | 做什么 | 不做什么 |
|------|--------|----------|
| Grok Bot | X/GitHub 搜候选、配方草稿、实测笔记；写 `inbox/` / `examples/`；留言 `to-claude.md`；改 `TASKS` 自己的行 | 不改 `README.md` / `README.en.md`；不 star/fork；不对外发帖 |
| Claude Code | `gh` 核实、脱敏、格式、**统一合并双语 README**；留言 `to-grok.md`；改 `TASKS` 自己的行 | 无新信号不空转造活；C 档只留言不执行 |
| 涛哥 | C 档拍板：公开设置、对外发帖、star/fork、删东西、花钱 | — |

## Claude `/loop` 一轮（白天 9:37–23:37，每 2 小时一轮）

1. `cd` 到本仓 → `git pull --rebase`（有冲突先停，留言 `to-grok.md`）
2. 读信号（任一为真才干活）：
   - `to-claude.md` 是否有比上次处理更新的 `### … Grok` 块
   - `TASKS.md` 是否有 grok 行变为 `done` 且 Claude 侧仍待审
   - `inbox/`、`examples/` 是否有未入 README 的新/改文件
   - 外部 issue / PR / 评论（只审不合并）
   - [`recheck.md`](recheck.md) 里有到期的行
3. 有活：按 [CONTRIBUTING 收录门槛](../CONTRIBUTING.md#收录门槛) 核实（`gh api`、fxtwitter）→ 脱敏/改格式 → 合并 README（中英同步）→ 更新 `TASKS` → 在 `to-grok.md` **追加**一条回执。暂缓的仓写进 `recheck.md`
4. 数字同步：README 条目数或教程数变了，改首屏「为什么」表、徽章、目录计数、学习资源里的篇数、🆕 最近更新（留最近 3 行）。社交预览图 `assets/social-preview.png` 只在条目数跨过整十（90、100…）时重做，并提醒涛哥重新上传。`.collab/promo/` 里的稿件已发出，不再同步
5. `git add` 相关文件 → 小步 `commit` → `git push`；README 有改动就手动跑一次 link-check
6. 记录本轮处理到水位：`.collab/loop-state.md`（见下）
7. 等下一轮

### 停机条件（必须遵守）

- 连续 **3** 轮「无新信号」→ 退出 loop，并在 `to-grok.md` 写一行「loop 休眠，有活再叫」
- 本 session 已跑 **≥8** 轮或墙钟 **≥16 小时** → 退出
- 撞上 C 档（公开仓设置变更、对外发帖、star/fork、删除文件/历史、改 CI 权限）→ **只留言不执行**，退出等涛哥
- `git push` 失败或 rebase 冲突无法自解 → 退出并留言

### 水位文件 `.collab/loop-state.md`

Claude 每轮结束更新（可覆盖写）：

```markdown
# loop-state
- last_run: YYYY-MM-DD HH:MM Asia/Shanghai
- last_to_claude_heading: （最近已处理的 Grok 留言标题原文）
- idle_rounds: 0
- note: …
```

## Grok 侧对称循环

| 节奏 | 做什么 | 产出 |
|------|--------|------|
| 每日（工作日） | T7：X 雷达扫近 24h Grok Bot 相关仓/玩法 | 追加 `inbox/candidates.md`；留言 `to-claude.md`；**不改 README** |
| 每周一 ~16:07 | Awesome 周更候选（已有 routine） | 策展摘要；无增量可静默 |
| 按需 | T8 实测、T9/配方缺口、T10 速报 | `inbox/field-notes.md` / `examples/` / `inbox/news/` |

## Grok 投稿前自查

上次回执里反复出现的问题，投之前先过一遍：

- [ ] **日期**：填原帖发布日期，按北京时间换算（fxtwitter 给的是 UTC，北京时间 = UTC + 8 小时）。不要填当天日期
- [ ] **门槛**：先对照 [CONTRIBUTING 收录门槛](../CONTRIBUTING.md#收录门槛)。仓库不到 7 天且不到 10★ 的，写进候选表时直接标「新仓，待 recheck」，不用催收
- [ ] **同一作者**：在 `docs/x-articles.md` 里搜作者名，近 7 天已有 2 篇就不投，或者换掉较弱的那篇
- [ ] **不投**：官方公告的转发或转述、收益引流、只有截图没有链接的帖子、非中英文
- [ ] **格式**：列表中间不留空行；短评写帖子里真有的内容，「官方」只用于 xAI 官方
- [ ] **去重**：除了 x-articles、README、inbox，再查一遍 [`recheck.md`](recheck.md)
- [ ] **提交**：只在你自己的云电脑上提交，不在涛哥本机的仓库目录里改。提交前 `git log -1 --format=%ae` 确认是 noreply 邮箱
- [ ] **留言时间**：标题时间以 `date` 为准

## 红线

见 [CONTRIBUTING.md](../CONTRIBUTING.md)。另：不自动 star/fork；不把「某个人参考仓」类资料写进公开 README。
