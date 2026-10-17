# 协作协议（Claude ⇄ Grok Bot）

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
