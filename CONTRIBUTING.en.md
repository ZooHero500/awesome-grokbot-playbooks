# Contributing

[中文](CONTRIBUTING.md)

## Inclusion criteria

### Repos and tools (README entries)

All three must hold:

1. **Used or maintained**: 10+ stars, or at least 7 days old with commits after creation
2. **Licensed**: a LICENSE file in the repo, or a license clearly stated in the README. Websites, docs and template links that are not repos are exempt
3. **Directly about Grok Bot**: built for Grok Bot, or the README treats Grok Bot as a main use. General agent tools that only mention Grok Bot in passing are out

On-topic repos that miss rule 1 go into [`.collab/recheck.md`](.collab/recheck.md) and are checked again when due.

### X articles and threads ([Grok Bot articles from top X creators](docs/x-articles.md))

1. **Author or post has weight**: about 5k+ followers, or about 100+ likes or 50+ bookmarks
2. **Substance**: a tutorial, recipe, real setup or retrospective, readable in full. A screenshot with no link is out
3. **Chinese or English only**
4. **At most 2 posts per author per week**; pick the best
5. **Out**: giveaways, tokens, trading gains, income bait ("make $X a month"), pure promotion, reposts or summaries of official announcements

Dates use Beijing time and the original post date.

## Entry format

Each entry has a link, a short review and tags.

```
- [Name](link) - Short review (what it does or why it stands out). Tags: `tag1` `tag2`
```

- Review in 1–3 sentences: why it is worth a look, plus any risk (account access, pasting cookies, data sent to a third party, ...). Do not copy the project's own blurb
- Put it in the single best-fitting section; no duplicates
- Tags in lowercase English, 2–4 of them

## Not accepted

These are removed on sight:

- API keys, tokens, cookies, passwords or any other credentials (including "expired" ones)
- Revenue, sales, user counts or other business numbers
- Internal paths, intranet addresses, links to private repos
- Personally identifying information (names, addresses, contact details, employee or family details, ...)

Sanitize recipes before submitting.

## Verification marks

| Mark | Meaning | Who can set it |
|---|---|---|
| ✅ Tested | Run end-to-end in Grok Bot, with the date it passed | Whoever ran it; a maintainer double-checks |
| 🔍 Reviewed | Docs and config read, readability smoke test done, not run | Any contributor, stating the level |
| no mark | Repo verified to exist and be maintained | — |

Reading docs alone never earns ✅.

## Recipe submissions

- Put them in `examples/`, following [`examples/_template.md`](examples/_template.md)
- `验证日期` (verification date) is required; recipes not rechecked for 90 days get ⚠️
- Use `{{placeholders}}` for variables and fictional data in examples

## Disclosure

- If you or a maintainer has a commercial relationship with an entry, add "author-related" at the end of its review
- At most 1 commercial entry per section

## What we don't do

- No automatic stars or forks of any repo
- No paid placement or star-for-star entries

## Review

Every PR is reviewed by a maintainer before merging. Direct pushes are not open.
