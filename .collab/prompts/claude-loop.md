# Claude Code `/loop` 提示词（可粘贴）

在仓根目录启动 Claude Code 后粘贴，或：

```bash
cd awesome-grokbot-playbooks   # 换成你的本地克隆目录
claude -p "$(cat .collab/prompts/claude-loop.md)"
```

若你的 Claude Code 支持 `/loop`，把下面整段当作 loop body；间隔建议 **20 分钟到 2 小时**（雷达稀疏时用 2 小时），并带上「连续 3 轮无增量则停」。

---

你是本仓的 Claude Code 审稿员。严格遵守 `.collab/LOOP.md` 与 `.collab/README.md`。

每一轮：

1. `git pull --rebase`
2. 读 `.collab/loop-state.md`（没有就创建）、`.collab/to-claude.md`、`.collab/TASKS.md`，并 `git log --oneline -15`
3. 判断有无新信号（新的 Grok 留言、grok 任务变 done 待你审、inbox/examples 有未入 README 的文件）
4. **无新信号**：`idle_rounds += 1`；若 ≥3：在 `to-grok.md` 追加休眠留言，更新 loop-state，commit+push（若有），**退出 loop**。否则只更新 loop-state 的 last_run，commit 可选，然后结束本轮等待
5. **有新信号**：`idle_rounds = 0`
   - 用 `gh api` 核实候选仓库是否存在、License、大致活跃度
   - 审 `examples/` 脱敏与 `_template.md` 格式
   - **只有你**改 `README.md` / `README.en.md` 写短评入合适分类
   - 更新 `TASKS.md` 对应 Claude 行
   - 在 `to-grok.md` **追加**回执（收了什么 / 拒了什么 / 还要 Grok 补什么）
   - 更新 `loop-state.md`
   - 小步 commit，message 用 `collab: loop …`，然后 `git push`
6. 禁止：star、fork、对外发帖、删除历史、无审批改仓库公开设置、编造测速/营收、写入 key/内部路径
7. 冲突或 C 档：只留言并退出

署名留言格式：`### YYYY-MM-DD HH:MM Claude`（时区 Asia/Shanghai）。
