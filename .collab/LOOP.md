# 协作 Loop 协议（Claude Code ⇄ Grok Bot）

目标：用 Git + `.collab/` 当邮箱，Claude Code 用 `/loop` **只审不乱改**；Grok 用 routine **只投料不合并 README**。

## 角色

| 角色 | 做什么 | 不做什么 |
|------|--------|----------|
| Grok Bot | X/GitHub 搜候选、配方草稿、实测笔记；写 `inbox/` / `examples/`；留言 `to-claude.md`；改 `TASKS` 自己的行 | 不改 `README.md` / `README.en.md`；不 star/fork；不对外发帖 |
| Claude Code | `gh` 核实、脱敏、格式、**统一合并双语 README**；留言 `to-grok.md`；改 `TASKS` 自己的行 | 无新信号不空转造活；C 档只留言不执行 |
| 涛哥 | C 档拍板：公开设置、对外发帖、star/fork、删东西、花钱 | — |

## Claude `/loop` 一轮（建议间隔 20 分钟）

1. `cd` 到本仓 → `git pull --rebase`（有冲突先停，留言 `to-grok.md`）
2. 读信号（任一为真才干活）：
   - `to-claude.md` 是否有比上次处理更新的 `### … Grok` 块
   - `TASKS.md` 是否有 grok 行变为 `done` 且 Claude 侧仍待审
   - `inbox/`、`examples/` 是否有未入 README 的新/改文件
3. 有活：核实链接（`gh api`）→ 脱敏/改格式 → 合并 README（中英同步）→ 更新 `TASKS` → 在 `to-grok.md` **追加**一条回执
4. `git add` 相关文件 → 小步 `commit` → `git push`
5. 记录本轮处理到水位：`.collab/loop-state.md`（见下）
6. sleep 到下一轮

### 停机条件（必须遵守）

- 连续 **3** 轮「无新信号」→ 退出 loop，并在 `to-grok.md` 写一行「loop 休眠，有活再叫」
- 本 session 已跑 **≥8** 轮或墙钟 **≥3 小时** → 退出
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

## 红线

见 [CONTRIBUTING.md](../CONTRIBUTING.md)。另：不自动 star/fork；不把「某个人参考仓」类资料写进公开 README。
