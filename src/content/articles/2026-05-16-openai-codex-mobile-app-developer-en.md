---
title: "OpenAI Brings Codex to Your Phone in the ChatGPT Mobile App"
summary: "OpenAI has launched a preview of Codex inside the ChatGPT mobile app for iOS and Android, letting developers monitor, direct, and approve AI coding tasks remotely without sitting at a computer. The move points to AI-assisted coding becoming less tied to the desktop."
category: "developer-tools"
publishedAt: 2026-05-16
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/14/openai-says-codex-is-coming-to-your-phone/"
  - name: "MacRumors"
    url: "https://www.macrumors.com/2026/05/15/openai-brings-codex-chatgpt-mobile-app/"
  - name: "9to5Mac"
    url: "https://9to5mac.com/2026/05/14/openai-brings-codex-control-to-chatgpt-for-iphone-and-android/"
  - name: "Build Fast With AI"
    url: "https://www.buildfastwithai.com/blogs/openai-codex-mobile-chatgpt-app-2026"
tags:
  - "OpenAI"
  - "Codex"
  - "developer tools"
  - "mobile"
  - "AI coding"
  - "ChatGPT"
relatedSlugs:
  - "2026-05-13-red-hat-summit-agentic-ai-developer-tools-en"
  - "2026-05-11-spacex-cursor-60b-acquisition-en"
  - "2026-04-04-cursor-devin-war-en"
---

The developer workflow has been moving toward AI for years. Now it is moving toward mobile. OpenAI launched a preview of Codex inside the ChatGPT app for iOS and Android on May 14, enabling developers to remotely monitor, direct, and approve the work of its autonomous coding agent from their phones — no laptop required.

The launch is available across all ChatGPT plan tiers, including Free and Go, in supported regions. That breadth suggests OpenAI wants Codex to be a standard part of the ChatGPT experience rather than a premium add-on.

## What It Actually Does

The Codex mobile integration is best understood as a remote control layer, not a coding environment. Developers do not write code on their phones. Instead, when Codex is running a task on a connected machine — a local laptop, a Mac mini serving as a persistent home development box, or a cloud-managed development environment provided by an employer — the ChatGPT app gives a live window into what Codex is doing.

From the phone, a developer can:
- **Switch between active task threads** — if Codex is working on three separate branches simultaneously, the app shows each task's status and allows context-switching
- **Review output** — read Codex's code, see which tests passed or failed, and examine diffs
- **Approve commands** — Codex pauses before executing potentially risky operations and waits for the developer to tap approve
- **Switch models** — toggle between different underlying reasoning models depending on task complexity
- **Start new tasks** — kick off a new coding task by describing it in natural language, letting Codex begin work before the developer gets back to their desk

Remote SSH is also generally available alongside the launch, meaning Codex can run threads inside remote devboxes or servers.

At launch, the phone app connects only to the **macOS** version of the Codex desktop app. OpenAI says support for remotely accessing Codex for Windows will follow soon.

## The Shift This Represents

The conventional model of AI-assisted coding has been desktop-centric: a developer sits down, opens an IDE, and uses an AI tool like Copilot, Cursor, or the web Codex interface to accelerate work in a focused session. When they leave the desk, the AI tool goes dormant.

The mobile integration breaks that pattern. Codex can now run continuously — executing long-horizon tasks that take minutes or hours — while the developer is away, doing something else, and checking in intermittently via phone. The relationship shifts from "developer uses AI tool" to "developer directs AI agent."

This has implications for how engineering work gets structured. If a developer can start a non-trivial task — writing a new API endpoint, refactoring a module, fixing a flaky test suite — and let Codex work on it while commuting, then review and approve the output before walking into the office, the effective output per engineering-hour increases substantially.

## How It Fits Into OpenAI's Broader Developer Strategy

The Codex mobile launch is the latest move in OpenAI's accelerating push to own the developer tooling layer. Codex arrived on the Mac in February after starting out as a command line interface tool, and OpenAI has been steadily expanding the agent's capabilities.

OpenAI is competing with Anthropic, whose Claude Code has gained popularity among businesses and tech professionals. Anthropic released a similar feature, Remote Control, for Claude Code in February, so OpenAI's mobile launch is not the first of its kind among AI coding tools.

## Caveats and Limitations

The feature is in preview, and the current experience has notable rough edges. The macOS-only requirement for the desktop host means Windows users are excluded for now.

There are also security considerations that the enterprise audience will scrutinize carefully. Approving code execution from a mobile device introduces a new attack surface: a developer who approves a Codex command while distracted, or whose phone is compromised, could inadvertently authorize harmful code changes.

Despite these limitations, the direction is clear: AI coding is becoming continuous, ambient, and mobile-first. The developer who can effectively direct an AI agent from their pocket is going to have a structural productivity advantage over one who can only interact with AI tools at a desk. OpenAI is betting that ChatGPT is the platform where that shift happens.

*Correction (November 15, 2026): 15 sentences were corrected or removed to match the sources listed on this page.*
