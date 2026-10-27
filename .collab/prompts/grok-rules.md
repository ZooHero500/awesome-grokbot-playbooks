# Grok Bot 提示词补丁

涛哥贴进 Grok Bot 的雷达 routine 提示词（或 bot 描述）末尾。仓库内的完整规则见 [LOOP.md 红线](../LOOP.md#红线)。

```
硬规则：docs/x-articles.md 和 docs/community-tutorials.md 里只写给读者看的短评。
「对照 @bot」「同作者已收/已在 inbox」「本轮最值得看」「过线」「待 Claude 核」「待 recheck」这类审稿备注（短评里写「约 X 万粉、X 赞」可以），只写进 .collab/to-claude.md 或 inbox/candidates.md，一个字都不进 docs。
提交前执行：grep -cE '对照 @bot|已收|已在 inbox|本轮最值得看|过线|待 Claude|recheck|inbox' docs/x-articles.md docs/community-tutorials.md
每个文件都必须输出 0；不是 0 就先删掉备注再提交。
```
