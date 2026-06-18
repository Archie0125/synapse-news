---
title: "Google Kills Gemini CLI Today: Forced Migration to Antigravity CLI Sparks Developer Backlash"
summary: "As of June 18, 2026, Google has shut down Gemini CLI — the popular open-source AI coding tool with 100,000 GitHub stars — forcing developers to migrate to Antigravity CLI within 30 days of announcement. The new tool is closed-source, breaks existing automation, and its rushed launch has pushed many developers toward competing platforms."
category: "developer-tools"
publishedAt: 2026-06-18
lang: "en"
featured: false
trending: true
sources:
  - name: "Google Developers Blog"
    url: "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
  - name: "The Register"
    url: "https://www.theregister.com/ai-ml/2026/05/20/bye-bye-gemini-cli-google-nudges-devs-toward-antigravity/5243605"
  - name: "Groundy"
    url: "https://groundy.com/articles/google-sunsets-gemini-cli-on-june-18-forced-migration-to-antigravity-cli-breaks/"
  - name: "Inventive HQ"
    url: "https://inventivehq.com/blog/gemini-cli-deprecated-antigravity-cli-migration"
tags:
  - "Google"
  - "Gemini CLI"
  - "Antigravity CLI"
  - "developer tools"
  - "open source"
  - "AI coding"
  - "developer experience"
relatedSlugs:
  - "2026-06-16-github-copilot-metered-billing-backlash-en"
  - "2026-06-16-spacex-acquires-cursor-60-billion-en"
  - "2026-04-04-cursor-devin-war-en"
---

Today, Google's Gemini CLI stops serving requests. As of June 18, 2026, the command-line AI assistant that accumulated more than 100,000 GitHub stars and merged over 6,000 community pull requests in its short life is dead — replaced by a new tool called Antigravity CLI, announced with just 30 days' notice at Google I/O on May 19th.

The backlash has been swift, loud, and instructive. Not because the replacement tool is necessarily worse — Antigravity CLI has real improvements — but because of how the transition was handled. Developers who built CI pipelines, shell scripts, and automation workflows on top of Gemini CLI are being told to rewrite everything in a month, with no compatibility layer, against a hard deadline that arrives during typical two-week sprint cycles.

## What Was Gemini CLI

Launched in early 2025, Gemini CLI was Google's answer to the proliferation of AI coding assistants. It was open-source under Apache 2.0, terminal-native, and built for developers who wanted Gemini's capabilities without leaving their command line. It gained traction quickly — 100,000 GitHub stars is a meaningful signal of organic adoption — and accumulated community contributions through those 6,000 merged pull requests.

For many organizations, Gemini CLI became load-bearing infrastructure. CI pipelines used it for automated code review. Shell scripts invoked it for documentation generation. Individual developers wired it into their daily workflows. The tool had been around for roughly a year, which made it feel — incorrectly, as it turned out — like something Google would maintain.

## What Antigravity CLI Is (And Isn't)

Antigravity CLI, invoked as `agy` rather than `gemini`, is a ground-up rewrite in Go. It is designed around multi-agent workflows, handling the kind of orchestration that has become central to how AI tools are used in 2026: multiple agents running in parallel, async task execution, long-running background operations.

The feature set is genuinely expanded. Antigravity CLI supports not just Gemini models but also Claude and GPT-OSS-120B, making it a multi-model platform rather than a single-vendor tool. This positions it against tools like Claude Code and OpenCode rather than as a Gemini-specific interface.

But there are two catches. First, Antigravity CLI is **not open source**. Unlike Gemini CLI, which was Apache 2.0, Antigravity CLI ships as a closed binary. The GitHub repository contains a changelog, a README, and a GIF of the interface. This is a fundamental change for organizations with open-source requirements or security audit needs. Second, Google explicitly states there will be **no 1:1 feature parity at launch** — teams are migrating to a tool that doesn't yet do everything the old tool did, on a 30-day timeline.

## The Migration Reality

What actually breaks in a forced migration from `gemini` to `agy` in 30 days?

Everything that assumes the command name. Every shell alias, CI configuration, shebang line, and PATH reference needs updating. But that is the easy part. Authentication mechanisms differ between the two tools, requiring credential regeneration. Extensions — Gemini CLI's plugin system — have been renamed to "Antigravity plugins" with changes to the API. Teams that built custom extensions will need to port their integrations.

The timeline problem is compounding. Most engineering teams run two-week sprints. A 30-day migration window means one sprint for planning and one for execution, with no buffer for testing, approvals, or inevitable bugs in the new configuration. Organizations with large CLI deployments — or those where Gemini CLI is embedded in production automation — are particularly exposed.

Google has acknowledged the disruption in its migration documentation, noting that it "won't be a perfect transition." This is accurate but insufficient.

## Who Gets to Keep the Old Tool

The shutdown does not apply equally to all users. Free-tier users, Google AI Pro subscribers, and Google AI Ultra subscribers lose access today. But organizations using Gemini CLI via Gemini Code Assist **Standard** or **Enterprise** licenses, or through paid Gemini and Gemini Enterprise Agent Platform API keys, retain access with continued model updates.

This creates a two-tier outcome: individual developers and small teams — precisely the community that made Gemini CLI's GitHub repository a 100,000-star success — are cut off first, while enterprise contracts provide a buffer. It is a legitimate business decision, but it lands badly with the open-source community that Google cultivated.

## The Trust Equation

The deeper damage is not to any specific pipeline or workflow. It is to the trust calculus developers use when deciding whether to build infrastructure on a tool.

Gemini CLI launched in early 2025 and is sunset in June 2026 — a lifespan of roughly 15 months. For developers evaluating AI tools in mid-2026, this timeline is now a data point. The question is not whether Antigravity CLI is good. The question is: what happens to Antigravity CLI in 15 months?

Community forums and developer threads have drawn explicit comparisons. Claude Code and OpenAI's coding tools have not executed comparable forced migrations. OpenCode, the viral open-source coding agent with 160,000 GitHub stars and 7.5 million monthly users, runs on any model and is not controlled by a single vendor. These alternatives are benefiting from the Gemini CLI transition, with teams using the disruption as a forcing function to reassess their tooling choices entirely.

## What Antigravity CLI Gets Right

To be fair: the multi-model support in Antigravity CLI addresses a real problem. Developers who were locked into Gemini models because of CLI tooling can now use Claude or other providers through the same interface. The async workflow architecture reflects how AI development has evolved — sequential, single-model prompts are increasingly inadequate for complex development tasks.

The Go rewrite produces a faster binary with lower latency. For CI environments where hundreds of invocations per day accumulate, this matters. And the multi-agent orchestration capabilities, when mature, will likely be more powerful than anything Gemini CLI offered.

But capability improvements do not resolve the process failure. Announcing a forced deprecation of an open-source, community-driven tool with 30 days' notice, shipping a closed-source replacement that lacks feature parity, and cutting off free and prosumer users first — these are the decisions developers will remember when evaluating Google's next developer tool launch.

The signal reaching the market today is not about Antigravity CLI. It is about what it means to build on Google's developer infrastructure.
