# Grok Bot Quickstart

[中文](quickstart.md) · [Back to README](../README.en.md)

For first-time Grok Bot users. Spend one afternoon on 5 steps and you end up with a bot that does real work every day, does not burn through your usage, and asks before anything irreversible.

Every step links only to resources verified in this repo. This repo is unofficial; the UI and plans on the [official site](https://x.ai/bot/marketplace) win. The recipes are written in Chinese.

| Step | What | Time | Uses |
|---|---|---|---|
| 0 | Set safety rules | 5 min | The checklist below |
| 1 | Import your first bot, give it a small job | 10 min | Template marketplace |
| 2 | Teach it one manual task as a skill | 15 min | [Teach-a-Task recipe](../examples/teach-a-task.md) |
| 3 | Start your first Routine | 15 min | [X radar recipe](../examples/x-radar.md) |
| 4 | Put guardrails on usage | 10 min | [Routine budget recipe](../examples/routine-budget.md) |
| 5 | Add more bots when you need them | As needed | [War room recipe](../examples/war-room.md) |

> All 10 recipes here are 🔍 reviewed or not yet verified; none is ✅ tested end to end yet. Expect UI differences, and if you get one running, please [report back](../CONTRIBUTING.en.md).

## Three terms first

| Term | What it is | In one line |
|---|---|---|
| **bot** | An AI teammate with a name and a role | Your bots share one always-on cloud computer (browser, files, terminal) |
| **Routine** | A task that runs on a schedule or an event | Where most usage gets burned |
| **Skill** | A reusable way of doing something you taught the bot | Teach once, get asked less |

Grok Bot is a different product from the Grok chat assistant and the Grok Build coding CLI.

## Step 0 · Set safety rules (5 min)

Do these before anything else so you never have to clean up later:

- [ ] **If you installed the desktop app, turn off "run on this computer" and "route traffic through this computer".** A cloud bot should not touch your local files and keys ([tip from @fankaishuoai](https://x.com/fankaishuoai/status/2111740064409756037), in Chinese)
- [ ] **Draw the irreversible line**: posting, sending email, paying, deleting files and `git push` all start as drafts and only happen after you confirm ([@wutujiang1999's four steps](https://x.com/wutujiang1999/status/2112034366998315408), in Chinese)
- [ ] **Never paste keys, tokens, cookies or billing screenshots into a chat**
- [ ] **Using it from mainland China**: if websites behave oddly, check the bot computer's exit IP first ([@chenmo's note](https://x.com/chenmo/status/2110380646824816682), in Chinese)

Importing a template, installing a skill or connecting an MCP server all hand permissions to the bot. Check which accounts it can touch before you click.

## Step 1 · Your first bot: import, don't start from scratch (10 min)

1. Open the official [template marketplace](https://x.ai/bot/marketplace), pick the template closest to your role, and click Add
   - To install a whole team at once, look at the teams marked `installable` on [botteams](https://github.com/ellelion/botteams)
   - Too many to choose from? Browse [Templates & directories](../README.en.md#-templates--directories) in the README
2. Give it a small job **you already did by hand 3+ times this week**, for example:
   - a daily digest of what changed
   - one piece of content rewritten for three platforms
   - inbox triage
   - a list of tomorrow's to-dos before bed
3. Check the result. If it falls short, fix the role description and rules; that beats correcting it in chat again and again

**Done when**: the bot hands back something you would use as is.

## Step 2 · Teach it one manual task as a skill (15 min)

Follow the [Teach-a-Task recipe](../examples/teach-a-task.md):

1. **Demonstrate**: you do the task once end to end; the bot watches and does not act
2. **Skill card**: the bot writes the goal, steps, success criteria and forbidden actions, with anything that changes turned into `{{placeholders}}`
3. **Edit it**: remove real paths and accounts, add what it must never do
4. **Dry run**: walk through with fake data, plan only, no real actions
5. **Sign off**: once it checks out, the bot follows this card for every task of that kind

**Done when**: next time, the bot does the same kind of task without asking you for the steps.

## Step 3 · Start your first Routine (15 min)

Follow the [X radar recipe](../examples/x-radar.md) and set up a Routine that runs once a day. Three rules for beginners:

- **Once a day is enough**: hourly runs hit rate limits and fragment the digest
- **Stay silent without signal**: when nothing real happened, output "no update" and send nothing
- **Read only**: likes, replies and posts are yours to do

Not on X? Use the [competitor radar](../examples/competitor-radar.md) or the [weekly review routine](../examples/weekly-review.md) instead; same rules.

**Done when**: for 3 days in a row, you get a readable digest on days with signal and nothing on days without.

## Step 4 · Put guardrails on usage (10 min)

With several Routines, usage drains quietly. Set the ground rules from the [Routine budget recipe](../examples/routine-budget.md):

```text
[ ] High-frequency Routines don't run on the bot you chat with every day
[ ] Routines run only on weekday daytime hours (say 9–19)
[ ] Prompts that "report even when nothing changed" now stay silent
[ ] On-demand mode used for testing is turned off afterwards
[ ] One weekly usage check: KEEP / SLOW / EVENT / CHANGE / RETIRE
```

Already close to the limit? Pause everything first, then re-enable one by one as the recipe says.

To pick a plan, see [@op7418's breakdown of the tiers](https://x.com/op7418/status/2109839549706969259) (in Chinese).

## Step 5 · Add more bots when you need them (as needed)

Wait until one bot has run reliably for a week. Don't build a team on day one.

| Your situation | Start with |
|---|---|
| 3–6 bots splitting research and drafts | [War room](../examples/war-room.md) |
| Running a go-global product alone | [One person, three roles](../examples/one-person-three-roles.md), [outbound support](../examples/outbound-support.md) |
| Letting bots take GitHub issues without letting them merge | [Dev four roles](../examples/dev-four-roles.md) |

Two hard rules for multiple bots:
- **Hand off through files only**, no free-for-all group chat
- **A human gate before anything gets published**

More team setups: [Multi-bot teams](../README.en.md#-multi-bot-teams) in the README.

## Pick a path

| You are | Read first | Then copy |
|---|---|---|
| Not a coder | [How non-engineers can use Grok Bot well](https://x.com/KinGao476942/status/2097915898971742325) (in Chinese) | Budget check → weekly review |
| An engineer | [grokbot-field-notes](https://github.com/unicodef1wn/grokbot-field-notes) `AGENTS.md` | Dev four roles |
| Making content or selling abroad | [Grok Bot articles from top X creators](x-articles.md) | X radar → war room |
| Not wanting the cloud | [Self-hosted bots](../README.en.md#-self-hosted-bots) in the README | — |

## Common beginner mistakes

- **Starting a pile of Routines on day one**: usage runs out in days and you can't tell which one burned it
- **Correcting in chat instead of fixing the rules**: it repeats the mistake. Write changes back into the skill card or role description
- **Letting the bot send things itself**: posts, emails and merges start as drafts and go out only after you approve
- **Trusting links the model made up**: spot-check that radar links actually open
- **Putting real paths and accounts into skills you share**: replace them with placeholders first

## Next

- **Learn properly**: [GrokBotGuide](https://github.com/JeffShanCha/grokbotguide) (Chinese and English), [awesome-grok-bot](https://github.com/ZeroPointRepo/awesome-grok-bot) (English ecosystem list)
- **See how others use it**: [Grok Bot articles from top X creators](x-articles.md)
- **Find something ready-made**: the README [Contents](../README.en.md#-contents)
- **Got a recipe running**: report back per the [contributing guide](../CONTRIBUTING.en.md) and it can earn ✅
