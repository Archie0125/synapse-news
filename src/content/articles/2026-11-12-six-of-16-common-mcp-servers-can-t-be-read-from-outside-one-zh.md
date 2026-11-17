---
category: developer-tools
faqs:
- answer: 在 2026 年 10 月 12 日至 11 月 11 日觀察的 16 個常見 MCP 伺服器中，有 6 個因需要驗證或封鎖爬蟲而無法公開讀取。可讀取的
    10 個裡，有 8 個共修改了 28 次工具定義。
  question: HISTOR 對 MCP 伺服器的觀察發現了什麼？
- answer: AI 代理依靠工具描述與 schema 決定行動，定義一改，代理行為就可能跟著改變。28 次修改中有 13 次發生在版本號未變時，全部來自 Firecrawl，因此很難被察覺。
  question: MCP 工具定義在版本號不變的情況下修改，為什麼值得注意？
- answer: 不是。對於能存取程式碼、工單、文件和金流的伺服器，要求驗證是正確做法。代價是任何公開紀錄都看不到這些伺服器對代理描述了什麼、何時改過，所以團隊必須自行在內部監控。
  question: MCP 伺服器要求身分驗證是壞事嗎？
featured: false
lang: zh
publishedAt: '2026-11-12T06:00:00+00:00'
relatedSlugs: []
sources:
- name: Dev.to
  url: https://dev.to/alexar76/six-of-16-common-mcp-servers-cant-be-read-from-outside-one-of-the-others-changed-19-times-in-a-1dh4
summary: 最常接觸敏感資料的 MCP 伺服器，偏偏外部都無從稽核。工具定義在沒有任何通知的情況下被修改，每個開發 AI 代理的人都應該提高警覺。
tags:
- cybersecurity
- ai-ml
- developer-tools
title: 16 個常見 MCP 伺服器中，有 6 個無法從外部檢視；另一個則在一個月內被改了 19 次
trending: false
type: news
---

We wrote down sixteen MCP servers that a software team could plausibly connect to its agents: the hosted servers of

GitHub, Notion, Linear, Atlassian, Sentry and Stripe; Context7, DeepWiki, Hugging Face and Cloudflare's docs server

for reading; Firecrawl, Brave Search and Tavily for the web; and three local packages, Playwright, MongoDB and Sentry.

It is a sample we picked, not a customer's setup and not a survey.

Then we asked [HISTOR](https://histor.modelmarket.dev), the public log of MCP tool definitions we run, what each of

them had told agents over the last 30 days, 12 October to 11 November 2026.

For six of the sixteen the answer was: nothing. HISTOR has never read a tool from them.

GitHub, Notion, Atlassian and Stripe answer an unauthenticated client with HTTP 401. Linear's and Sentry's hosted

servers did the same on every read until 1 November. Since 2 November HISTOR honours robots.txt, and both sites

disallow `/mcp` for all crawlers (Linear's disallows the whole site), so HISTOR no longer sends them a request.

Requiring sign-in is the right call for servers that reach a team's code, tickets, documents and payments. The

consequence is that no public log, ours included, can tell you what these servers describe to your agent, or when

that description changed. The readable servers are not harmless by comparison — MongoDB's package has

`drop-database`, Sentry's package now has `delete_alert_rule` — but at least their definitions are public.

Eight of the ten changed their tool definitions — descriptions or schemas — 28 times between them. Brave Search and

Tavily did not change at all. Thirteen of the 28 changes came while the server kept reporting the same version, and

all thirteen were Firecrawl's. Everywhere else, a change came with a new version number.

A changed definition does not mean a server misbehaved. It means the text and the schemas your model works from are

not the ones somebody reviewed, and the workflows that use those tools deserve a re-run. Three of the ten show three

different kinds of change.

Between the two versions HISTOR read, `@sentry/mcp-server` 0.42.0 and 0.49.0, the package went from 9 tools to 73.

It dropped `execute_sentry_tool`, `search_sentry_tools` and `search_events`, kept six, and added 67. Among the new

ones: `delete_alert_rule`, `delete_metric_monitor`, `delete_monitor_environment`, `delete_uptime_monitor`, seven

`create_*` and five `update_*` tools.

The old design was deliberate. In 0.42.0, `search_sentry_tools` told the model: "Many Sentry operations are

intentionally not exposed as top-level tools", and `execute_sentry_tool` ran them by name. In 0.49.0 those operations

are tools of their own. For a reviewer that is better: the four `delete_*` tools are now visible by name. But a

config that starts `npx -y @sentry/mcp-server` without a version moved to 0.49.0 as soon as npx resolved it, and

nobody had to approve the new tool list.

Each line is a new tool set: HISTOR hashes the tools' names, descriptions and input and output schemas, and a new

digest is a change. The orange lines came with no new version. Some of what they carried:

- an `objective` input became required on 13 October, stopped being required with the 3.30.1 release on 15
October, and became required again on 18 October while the server still said 3.30.3;
- on 10 November `firecrawl_scrape` gained an output field, `retryable`, and the `zeroDataRetention` option
disappeared from `firecrawl_search`'s scrape options — an object that rejects unknown keys, so a call that still
sends the flag no longer validates;
- at 03:21 UTC on 11 November `firecrawl_scrape` dropped its `alexandria` argument, made `url` required, and its
description named `alexandria_library_search` and `alexandria_library_read` where it had named `firecrawl_find_tools`. At 07:58 it was back, byte for byte, to the definition it had before; `firecrawl_search` kept the new names. The server reported 3.39.0 throughout.

We don't know why any of these happened, and nothing about them is wrong. Firecrawl is under active development and

its hosted server is where that shows. What they show is that the version string of a hosted server is not a record

of what it serves. (Yesterday's post on [signed manifest
revisions](https://modelmarket.dev/blog/same-mcp-version-different-tool-description-who-signed-it/) is about who

can vouch for such a change.)

`mongodb-mcp-server` 3.2.2 → 3.3.0 touched 10 input schemas and 8 output schemas. Most of its 47 edits rewrite

`additionalProperties: {}` as `additionalProperties: true` or drop an empty `items: {}`. JSON Schema treats these

forms as identical, so every call that validated before still validates. The rest add guidance on embedding models to

field descriptions and tighten one field mapping in `create-index`.

A digest-based alarm fires on this exactly as loudly as on Firecrawl's `zeroDataRetention`. That is why a change

alert alone is not enough: the person approving it needs the diff.

HISTOR's API is public and needs no key. This is the count behind the orange lines, cut down to one server; it runs on

Python 3.9 or later with the standard library:


```
# usage: python3 same_version.py <server id> <since, e.g. 2026-10-12>
import json, sys, urllib.request
server_id, since = sys.argv[1], sys.argv[2]
api = "https://histor.modelmarket.dev/api/v1"
url = f"{api}/changes?watch={server_id}&limit=200"  # newest first
rows = json.load(urllib.request.urlopen(url, timeout=30))["changes"]
window = [c for c in rows if c["observed_at"] >= since]
silent = [c for c in window
          if c["from_server_version"] == c["to_server_version"]
          and c["from_package_version"] == c["to_package_version"]]
print(f"{len(window)} changes since {since}, {len(silent)} at the same version")
for c in silent:
    tools = [m["tool"] for m in c["summary"].get("modified", [])]
    print(" ", c["observed_at"], c["to_server_version"], ", ".join(tools))
```
```
$ python3 same_version.py 0ae1ed4e4d5d8dd7 2026-10-12
19 changes since 2026-10-12, 13 at the same version
  2026-11-11T07:58:19Z 3.39.0 firecrawl_scrape
  2026-11-11T03:21:09Z 3.39.0 firecrawl_scrape, firecrawl_search
  …
```
A server's id is on its HISTOR page, or from `https://histor.modelmarket.dev/api/v1/servers?q=<name>`. The numbers

move as servers change; the output above is from 11 November.

For what HISTOR cannot read, the check has to run with your credentials. [WARDEN](https://www.npmjs.com/package/@aimarket/warden),

our open-source MCP scanner, records the tool definitions of every server in a repository's `.mcp.json` into a lock

file. It needs Node.js 20 or later, and it starts the local (stdio) servers in the config to read their tools, so run

it where you would run those servers anyway:


```
npx -y @aimarket/warden@0.26.0 scan --project \
  --lock warden.lock.json --update-lock
```
```
WARDEN scan 0.26.0 · ruleset 19 sha256-XfRh1+VZoAM6… · block at high
  read .mcp.json (claude-code, 2 servers)
  ✓ allow   deepwiki  claude-code    3 tools · score 0.90 · lock: updated
  ✓ allow   context7  claude-code    2 tools · score 0.90 · lock: updated
…
Lock written: warden.lock.json. Commit it; the diff is the review.
```
That run is from a test repository with two public servers, on 11 November. Committed, the lock makes CI fail when a

remote server serves different definitions (`TOOL_DEF_DRIFT`, with a field-by-field diff) or when a server nobody

approved appears (`LOCK_MISSING`); `--project` keeps your personal configs out of it.

It reaches a hosted server only with the headers written in the config: a server that takes a token in a header

(GitHub's accepts a personal access token, for example) can be locked this way. A server you sign into through OAuth

in the client answers WARDEN with 401, just as it answers HISTOR. For those, today, the review is the tool list your

client shows you. We don't know of a tool that closes that gap, ours included.

For package servers the oldest fix still works: write the version you reviewed into the config,

`"args": ["-y", "@sentry/mcp-server@0.49.0"]`, and review again when you bump it.

- HISTOR reads remote servers on a six-hour target, and every 30 minutes once a server has changed twice in a week. At 14:44 UTC on 11 November the mean gap between reads was 13.7 hours. A change that is undone between two reads is not seen.
- It reads what a server serves an unauthenticated client. Tools that appear only after sign-in, or only for another client or launch configuration, are outside what it can see.
- Packages are read at whatever version is current when a crawl reaches them, every few days for the ones here. HISTOR never read Sentry 0.43–0.47, and its 0.48.0 install failed, so their changes are inside the 0.42 → 0.49 difference.
- Sixteen servers is a sample we chose. At 14:44 UTC on 11 November HISTOR counted 79,415 tool-set changes in the previous 30 days across the 91,847 registry entries it tracks; that total includes publishers whose servers change on almost every read, so it is not a rate for your stack.

The sixteen records as we read them at 14:20 UTC on 11 November, their SHA-256 sums, the stats snapshot and the

scripts behind every number here are in [one archive](https://modelmarket.dev/blog/six-of-16-common-mcp-servers-cant-be-read-from-outside/stack-audit-data-2026-11-11.zip)

(1 MB).

We are starting to do this as an audit for teams: an inventory of the MCP servers your developers and agents use,

a WARDEN scan of each tool, the lock and an allowlist in your CI, and 30 days of change alerts with a short note on

each change that touches your workflows. The first three teams get it free in exchange for written feedback and a

short, non-binding letter of intent. If that's you, write to [qwezzy721@gmail.com](mailto:qwezzy721@gmail.com) with the MCP clients your team uses.

*We run HISTOR and WARDEN. AI assistance was used for the analysis, the scripts, the figures and this article; the data, code and quoted outputs are reproducible from the linked files.*

## Top comments (0)

## Summary

**TLDR:** The MCP servers that touch your most sensitive data are the ones nobody can audit from outside, and silent tool-definition changes should worry every agent builder.

- Of 16 popular MCP servers tracked by HISTOR from October 12 to November 11, 2026, six could not be read from outside at all.
- GitHub, Notion, Atlassian and Stripe return HTTP 401 to unauthenticated clients. Linear and Sentry block crawlers through robots.txt, which HISTOR has honored since November 2.
- Eight of the ten readable servers changed their tool definitions 28 times in total. Brave Search and Tavily did not change at all.
- Thirteen changes came without a version bump, and all thirteen were Firecrawl's. Agents could receive new instructions while the version number stayed the same.
- Readable doesn't mean harmless: MongoDB's package exposes drop-database and Sentry's now has delete_alert_rule.

## 摘要

**重點摘要：** 碰觸你最敏感資料的 MCP 伺服器，恰恰是外界無法稽核的那些。工具定義悄悄改版，每個打造 AI 代理的人都該擔心。

- HISTOR 在 2026 年 10 月 12 日至 11 月 11 日追蹤了 16 個常見的 MCP 伺服器，其中 6 個完全無法從外部讀取。
- GitHub、Notion、Atlassian、Stripe 對未驗證的請求回傳 HTTP 401；Linear 與 Sentry 透過 robots.txt 封鎖爬蟲，HISTOR 自 11 月 2 日起遵守這項設定。
- 可讀取的 10 個伺服器中，有 8 個共修改了 28 次工具定義，Brave Search 和 Tavily 則完全沒變。
- 其中 13 次修改沒有更新版本號，全部來自 Firecrawl，代表代理可能在版本號不變的情況下收到新指令。
- 可讀取不等於無害：MongoDB 套件提供 drop-database，Sentry 套件也新增了 delete_alert_rule。