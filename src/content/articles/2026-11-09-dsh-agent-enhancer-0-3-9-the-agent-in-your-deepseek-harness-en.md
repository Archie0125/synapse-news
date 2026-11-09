---
category: ai-ml
faqs:
- answer: 'The release adds four features to the DeepSeek Harness desktop client:
    a Browser Agent that operates its own Chrome or Edge window, a skills manager,
    MCP connectors, and soft pause with run alerts.'
  question: What's new in DSH Agent Enhancer 0.3.9?
- answer: It runs in a separate browser profile, waits for the user to log in manually,
    refuses to bypass captchas, and asks for approval before actions such as submitting
    forms or sending messages. Screenshots and page DOM are never sent to telemetry.
  question: How does the Browser Agent handle security?
- answer: It suits tasks such as checking orders, reports or config values on internal
    dashboards the user is already logged into, and pulling together information spread
    across several web pages.
  question: What is the Browser Agent useful for?
featured: false
lang: en
publishedAt: '2026-11-09T05:52:36+00:00'
relatedSlugs: []
sources:
- name: Dev.to
  url: https://dev.to/rebornace/dsh-agent-enhancer-039-the-agent-in-your-deepseek-harness-desktop-can-now-drive-its-own-browser-1n8m
summary: Giving a DeepSeek desktop agent its own browser is powerful, and the human-in-the-loop
  guardrails for logins and approvals are what make it worth trusting.
tags:
- ai-ml
- developer-tools
- products
title: 'DSH Agent Enhancer 0.3.9: the agent in your DeepSeek Harness desktop can now
  drive its own browser'
trending: false
type: news
---

`dsh-agent-enhancer` is a plugin for the official DeepSeek Harness (DSH) desktop client. This release, **0.3.9**, brings four things: a **Browser Agent**, a **skills manager**, **MCP connectors**, and **soft pause plus run alerts**. Prompt history, rollback, billing, context and model routing were covered in earlier posts and are not repeated here.

The agent can already edit files in your workspace, but anything on the web was out of reach: dashboards that require a login, forms that need a few clicks before they return anything, information scattered across several pages. The Browser Agent gives it a window.

It runs its own Chrome or Edge with a separate profile directory, so logins persist and nothing collides with the browser you use day to day. Note that this is **not** the web viewer in the official sidebar — that one is for looking, this one is for operating.

**You never start it manually.** Use a `browser_*` tool in a conversation, or `Alt+click` a link, and the window comes up by itself. To switch between Chrome and Edge, change it in settings or the right sidebar; a running window switches over immediately.

**Logins are yours to do.** Hit a site that needs signing in and the window waits on the login page. Sign in yourself, click **"I'm done"**, and the agent continues from where the page is. It will not work around captchas for you.

**Consequential actions ask first.** Anything that changes external state — submitting a form, sending a message — plus `Alt+opening` a link, triggers an approval dialog. Screenshots and page DOM are never sent to telemetry.

**Parallel sessions.** A session is tied to a browser tab, and switching tabs can either **Follow** the current session or **Stay** on the page you picked.

A few things it is good for:

- Checking orders, reports or config values on an internal dashboard you have already signed into
- Opening a page, filling it in, and submitting — with your approval before it sends
- Opening a few tabs, cross-checking data between two pages, and writing the conclusion back into the chat
- Quoting text from a page straight into your next prompt

**Skills**: install from GitHub (`owner/repo`) or a Zip, with visible progress you can cancel, targeting the user or project directory. Once installed, invoke them through the official `/` command. GitHub sources can check for updates.

**Connectors (MCP)**: add Stdio or Remote services in `mcp.json`, toggle each one in the list, and open the detail view to see which tools a service exposes.

**Soft pause**: there is a pause button on the toolbar of your latest message. Press it and **subsequent model calls are held back**, while anything already streaming or already running as a tool finishes normally. Resume when you are ready — what you save is the tokens that would have been spent next. This differs from the official Stop, which cuts the current turn off outright.

**Run alerts**: when a long task finishes, when something is waiting for your approval, or when a session errors out, you get pulled back from whatever window you moved to. The default level is **"when unfocused"**, which covers dual monitors and switching to other apps; notifications go through the system notification center, and if one cannot be delivered you get a toast when you return to the window.

Prompt history / one-click optimization / next-prompt prediction / select-to-quote, rollback (conversation only or with files, undoable), in-workspace file editing and extra folders, session delete, token billing and per-account balance, context occupancy with compaction, and Auto model routing. Details are in the earlier posts.

**Settings → Plugins**, use the add-plugin flow to install `dsh-agent-enhancer`, then fully quit the desktop client and restart it.

Or from the CLI:


```
dsh plugin --profile desktop add dsh-agent-enhancer@0.3.9
```
Targets the `desktop` profile; requires DSH Desktop 0.2.2-rc.1 or above. If you still have the old `dsh-composer-enhancer` package installed, remove it first, and quit all desktop windows and tray processes before installing.

- The Browser Agent is off by default and is a high-risk capability. It supports Chrome and Edge only, will not get past login walls or captchas, and requires approval for consequential actions.
- Soft pause only holds back model steps that have not started yet, and does not survive a restart. The official Stop remains a hard interrupt.
- Rollback tracks UTF-8 text files only; it does not touch processes, terminals, untracked files or binaries.
- Extra folders do not widen the agent sandbox; session delete cannot be undone.
- The estimated "¥" in billing and the context detail figures are approximations, not exact billing data.

## Top comments (0)

## Summary

**TLDR:** Giving a DeepSeek desktop agent its own browser is powerful, and the human-in-the-loop guardrails for logins and approvals are what make it worth trusting.

- Version 0.3.9 of the community plugin adds a Browser Agent, a skills manager, MCP connectors, and soft pause plus run alerts to the DeepSeek Harness desktop client.
- The Browser Agent drives its own Chrome or Edge instance with a separate profile, so logins persist without touching the user's everyday browser.
- Users sign in themselves, the agent won't bypass captchas, and actions that change external state need explicit approval.
- Screenshots and page DOM are never sent to telemetry, which addresses a major privacy worry with browsing agents.
- The release follows the wider trend of agents moving from editing files to operating real web apps.

## 摘要

**重點摘要：** 讓 DeepSeek 桌面代理擁有自己的瀏覽器很強大，但真正值得信任的是登入和送出操作都要人類把關的設計。

- 這個社群外掛的 0.3.9 版為 DeepSeek Harness 桌面版加入 Browser Agent、技能管理、MCP 連接器，以及軟暫停和執行提醒。
- Browser Agent 用獨立的設定檔操作自己的 Chrome 或 Edge，登入狀態會保留，也不會干擾使用者平常用的瀏覽器。
- 登入由使用者自己完成，代理不會幫忙繞過驗證碼，任何會改變外部狀態的動作都要先經過確認。
- 截圖和頁面 DOM 一律不送進遙測資料，回應了瀏覽代理最受關注的隱私疑慮。
- 這次更新反映了一個大趨勢：AI 代理正從修改檔案，走向直接操作真實的網頁應用。