# 周报 X 串帖 · 第 1 期（10-20 → 10-26）

涛哥发。Claude 起稿，数字截至 2026-10-26 14:50。

- 每条按「不开会员也能发」控制在约 140 个汉字以内。
- 链接全部核过能打开。
- @ 的 4 个人都是本周收录文章的作者。

发帖节奏：
1. 先发第 1 条。
2. 2–10 条在它下面接成串。
3. 最后一条把仓库链接再放一次。
4. 配图建议用 README 首图 `assets/social-preview.png`。

---

**1/11**

Grok Bot 一周新玩法 Top 10（10.20–10.26）

开源清单 awesome-grokbot-playbooks 公开第一周：收录从 75 条涨到 123 条，大 V 文章从 77 篇涨到 190 篇。

从里面挑了 10 个最值得抄的 👇

github.com/sit-in/awesome-grokbot-playbooks

**2/11**

① 先保命：云电脑不是本地硬盘

Reset、恢复或磁盘满时，bot 的云电脑可能退回旧快照，快照之后攒的 skill 和文件会一起没。

重要东西定期同步到 GitHub 或网盘。

@alin_zone 这条 1300 多收藏，建议人手一份
x.com/alin_zone/status/2113995666401710320

**3/11**

② 额度烧得快？大头可能是「重读」

有人把用量 CSV 丢给 Grok 分析：约 9800 万 token 是缓存重读，真正写东西只有约 70 万。

@GrokBotRadar 给了十步止血法：一任务一对话、routine 改成变化才报……
x.com/GrokBotRadar/status/2114409935345971231

**4/11**

③ iPhone 上喊「Hey Grok」直接开语音

快捷指令选 Start Voice Chat with Bot，再用辅助功能里的「人声快捷指令」录 3 遍「Hey Grok」。不用装额外的 App。

@xiangxiang103 有真机视频
x.com/xiangxiang103/status/2114524472820818073

**5/11**

④ 让 bot 替你打电话

IRS 电话永远打不进。@sxzz 周末给 bot 派活：周一 7 点开始自动拨，bot 自己注册了外呼工具，打了 5 通，找到留号回拨的入口。

7:40 IRS 回电。
x.com/sxzz/status/2112344654683492392

**6/11**

⑤ 358 页中文实战书《Grok Bot 黑皮书》

约 20 万字：从国内开通、付费，到搭一支有审批边界、不乱烧额度的 bot 团队。每条事实都标了出处，附 36 套提示词和 Routine 模板，还有专章讲怎么识别代充骗局。

github.com/LJMStark/grok-bot-blackbook

**7/11**

⑥ 只跟一个 bot 说话的「软件工厂」

模板 Firstmate：活分两类，scout 只调研不改代码，ship 才动手。改完先过一轮对抗式评审才开 PR，合并要你点头。

x.ai/bot/__4FfrkUdvpdMk6-LKg5r

**8/11**

⑦ X 上刷到好帖，一键交给 bot

Send to Grok Bot：给 x.com 每条帖子加一个按钮，点一下就送进你的 bot，走 webhook routine。也有 iPhone 快捷指令版。

github.com/jamespendry/send-to-grok-bot

**9/11**

⑧ 多台电脑上的 agent 互相发消息

yobiru（350+★）：经 Tailscale 互传消息、文件，按规则叫醒对方；私聊不经中心服务器。还能把一个 bot 用链接分享给朋友，只开放你给的能力。

github.com/chekusu/yobiru

**10/11**

⑨ 给 bot 一个实体身体

两个 ESP32 圆屏项目：
- 宗主 zongzhu-bot：说唤醒词就把需求交给 bot，屏幕显示并朗读回复。
- 小糖：会眨眼的桌面宠物，按住实体键直接跟 bot 说话。

github.com/Liu-zhongxian/zongzhu-bot
github.com/vliuyt/grok-bot-esp32-bridge

**11/11**

⑩ Claude Code 和 Grok Bot 互相问话

claude-grok-bridge：在 Claude Code 里说一句「ask Grok Bot …」，大约 30 秒后答案回到原会话。走两边各自的 routine，不用中间服务器，也不用拷 key。

github.com/francoCosimo95/claude-grok-bridge

每周一更新。觉得有用点个 Star ⭐
github.com/sit-in/awesome-grokbot-playbooks

---

## 备用

- **想更短**：只发 1/11 + ①④⑤⑥⑨ 五条。中文圈对「保命」「打电话」「中文书」「实体硬件」反应最强。
- **有 X 会员，想发单条长帖**：把 11 条合成一条，去掉每条的序号头即可。
- **作者 @**：只 @ 了有 X 账号的 4 位文章作者。仓库作者的 X 账号没核，不要猜着 @。
