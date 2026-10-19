# 公开前隐私审计（T19）

- 审计人：Claude
- 首轮：2026-10-18；首发前（10/26）再跑一轮
- 范围：工作区全部文件 + 全部 git 历史（`git log -p --all`，40 个 commit）
- 查了什么：邮箱、手机号、本机路径、key/token 形态、营收数字、真名/个人仓名、reason-network 组队链接

## 结果

| # | 发现 | 位置 | 处理 | 状态 |
|---|---|---|---|---|
| 1 | 本机绝对路径（含用户名） | `.collab/prompts/claude-loop.md` 第 6 行 | 改成通用 `cd awesome-grokbot-playbooks` | 工作区已修；**历史仍在** |
| 2 | 某个人参考仓的名字（一位开发者的 GitHub 名），共 14 处 | `inbox/candidates.md`、`.collab/to-grok.md` 的旧版本 | 工作区早已改成「某个人参考仓」 | 工作区 0 处；**历史仍在** |
| 3 | 提交作者邮箱（个人 Gmail） | 全部 40 个 commit 的作者信息 | 公开后任何人都能在 commit 里看到 | 涛哥选 C（10/18）：历史不动，本机仓已改用 noreply 邮箱；Grok 云电脑待改 |
| 4 | `~/.reason/...` 等路径 | reason-network 卸载说明 | 通用路径，不含用户名 | 无需处理 |
| 5 | key / token / 手机号 / 营收数字 | — | 0 处命中；「营收」出现的地方都是「红线：无营收」这类规则文字 | 通过 |
| 6 | reason-network 组队链接 | — | 0 处命中，当时只在对话里贴过，没进仓库 | 通过 |
| 7 | 「涛哥」「铁柱」 | 多处 | 都是公开昵称，不算隐私 | 通过 |

## 需要涛哥拍板（C 档）

第 1、2、3 条都只存在于 git 历史里。按规矩不删历史，可选做法：

- **A. 接受**：路径只暴露本机用户名；人名是公开的 GitHub 账号，而且只在雷达笔记里出现；邮箱本来就是这个 GitHub 账号的提交邮箱。风险低。
- **B. 首发用干净新仓**：新建一个公开仓，只带当前文件、不带历史；现在这个私有仓留作归档。代价是丢掉 40 个 commit 的协作记录，「真实作战室」这个卖点会弱一些。
- **C. 只处理邮箱**：以后的提交改用 GitHub 的 noreply 邮箱（`git config user.email <id>+<name>@users.noreply.github.com`）。历史不动，也就是 A 加上这一步。

Claude 建议 **C**。**涛哥 2026-10-18 拍板：C。**

## 首发前复查命令

```bash
git log -p --all > /tmp/hist.txt
grep -nE '/Users/|/home/' /tmp/hist.txt
grep -nE '(sk-|xai-|ghp_|AKIA)[A-Za-z0-9]{12,}|-----BEGIN' /tmp/hist.txt
grep -rnE '/Users/|/home/' . --exclude-dir=.git
```

## 第二轮（2026-10-19 首发前）

- 范围：工作区 + 全部 52 个 commit，包括 10/18 晚到 10/19 早 Grok 的雷达提交
- 工作区：本机路径、key、邮箱（除 noreply）、手机号、飞书链接全部 0 命中。审计报告里的复查命令本身不算
- 历史：只剩第一轮已知的 3 项，都已按 C 处理，没有新增
- 提交邮箱：10/18 15:20 起，Claude 和 Grok 的提交都已是 noreply
- 结论：**可以公开**
