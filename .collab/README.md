# 协作协议（Claude ⇄ Grok Bot）

> **给第一次来的读者**：这个仓库由两个 AI 分工维护，人只拍板。Grok Bot 在云电脑里每天搜 X 和 GitHub，把候选和配方初稿推进 `inbox/`、`examples/`；Claude Code 在本机用 `gh api` 核实、脱敏、写短评，只有它改 README；涛哥审稿并做所有对外动作。下面的留言、任务板、loop 状态都是真实工作记录，原样保留。想照搬这套「作战室」，看 [作战室配方](../examples/war-room.md)。

本目录是 Claude（本机 Claude Code）与 Grok Bot（云端）的异步对话通道，经 GitHub 同步。

## 文件

- `TASKS.md` — 任务板，唯一事实来源
- `to-grok.md` — Claude 给 Grok 的留言
- `to-claude.md` — Grok 给 Claude 的留言

## 规则

1. 留言只追加、不改写对方内容；每条以 `### YYYY-MM-DD HH:MM 署名` 开头
2. 改动前先 `git pull --rebase`，完成后立即 commit + push，小步提交
3. 认领任务：在 `TASKS.md` 把状态从 `todo` 改为 `doing (@名字)`；完成改 `done` 并写产出路径
4. 各自只改自己负责的文件，README.md 由 Claude 统一合并
5. 遵守 [CONTRIBUTING.md](../CONTRIBUTING.md) 禁止内容：不写凭据、经营数字、内部路径、隐私
6. 不 star / fork / 对外发帖；对外动作先问涛哥

## Loop

异步循环协议见 [LOOP.md](LOOP.md)；Claude 可粘贴提示词见 [prompts/claude-loop.md](prompts/claude-loop.md)。
