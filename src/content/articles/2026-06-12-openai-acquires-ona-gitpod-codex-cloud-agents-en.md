---
title: "OpenAI Acquires Ona to Power Long-Running Codex Agents in the Cloud"
summary: "OpenAI has agreed to acquire Ona, the cloud development platform formerly known as Gitpod, to enable its Codex coding agent to run persistent multi-day tasks in secure cloud sandboxes. The deal is OpenAI's sixth acquisition of 2026 and a direct challenge to Anthropic's growing enterprise developer dominance."
category: "developer-tools"
publishedAt: 2026-06-12
lang: "en"
featured: false
trending: true
sources:
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/06/11/openai-acquires-ai-agent-orchestration-startup-ona/"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-06-11/openai-to-acquire-cloud-platform-ona-to-support-ai-agents"
  - name: "OpenTools"
    url: "https://opentools.ai/news/openai-acquires-ona-cloud-startup-codex-2026"
tags:
  - "openai"
  - "codex"
  - "gitpod"
  - "developer-tools"
  - "ai-agents"
  - "acquisitions"
  - "cloud"
relatedSlugs:
  - "2026-06-04-openai-codex-sites-role-plugins-enterprise-en"
  - "2026-06-12-opencode-displaces-cursor-ai-coding-agent-en"
  - "2026-06-11-cognition-devin-1b-26b-valuation-en"
---

OpenAI announced on June 11 that it has agreed to acquire Ona—the cloud-native developer platform formerly known as Gitpod—in what the company described as a foundational investment in its Codex coding-agent ecosystem. Financial terms were not disclosed. The Ona team will join OpenAI's Codex division to lead integration work, and the acquisition remains subject to regulatory review.

The deal marks OpenAI's sixth acquisition of 2026 alone and reflects an accelerating push to control more of the infrastructure layer underneath AI-assisted software development—a market where Anthropic's Claude Code and GitHub Copilot continue to make substantial enterprise inroads.

## From Browser IDE to Agent Execution Layer

Gitpod was founded in 2020 by Johannes Landgraf and Christian Weichel in Germany with a deceptively simple pitch: spin up a fully configured, cloud-hosted coding environment in your browser with a single click, eliminating the hours typically lost to local machine setup. The product grew steadily, eventually serving more than two million developers worldwide.

In September 2025, the company rebranded as Ona and pivoted aggressively toward AI agent infrastructure. Rather than serving human developers at keyboards, Ona began building execution tooling for autonomous agents—workloads that run tests, refactor code, and hunt vulnerabilities without a human in the loop. The timing proved prescient: by early 2026, OpenAI was watching Codex become one of its fastest-growing products, with over five million weekly active users against a global developer population of roughly 47 million.

But as agents grow more capable, the tasks they tackle have grown in both complexity and duration. A one-hour refactor, a three-day vulnerability sweep, a week-long framework migration—none of these fit neatly into a session tied to a single laptop that gets closed at night. That duration problem is precisely what OpenAI is buying Ona to solve.

## Persistent Sandboxes and the "Always-On" Agent

Ona's core technology provisions secure, cloud-based sandboxes that remain live even after the developer who initiated the task has logged off. Agents running inside those sandboxes continue working—compiling, testing, writing, calling external APIs—overnight or across weekends. The human returns asynchronously at natural checkpoints to review progress and redirect rather than supervising every step.

OpenAI confirmed that Ona "will improve Codex's ability to perform long-running tasks that take hours or days" and will give users cleaner interfaces for reviewing agent output and providing feedback mid-task.

The security architecture is equally significant. Ona's sandboxes verify applications through cryptographic hashing rather than relying on filenames, meaning a renamed or relocated malicious binary cannot bypass controls. Sensitive credentials are vaulted separately from the execution environment, and outbound connections to potentially harmful servers are blocked at the infrastructure level. These aren't incidental features: enterprise security teams evaluating AI coding tools have consistently flagged credential leakage and supply chain contamination as their top two concerns when deploying agents at scale.

The acquisition fits a recognizable pattern. In March 2026, OpenAI purchased Promptfoo Inc., which added automated red-teaming and vulnerability scanning to Codex's Frontier security platform. Ona extends the same hardening logic to the execution environment itself—giving enterprise clients not just a smart coding agent, but the secure, observable infrastructure required to actually deploy it across production workflows.

## A Direct Counterweight to Claude Code

The competitive subtext of the deal is difficult to ignore. Anthropic's Claude Code has emerged as the most credible challenger to GitHub Copilot in enterprise software development, particularly among security-conscious organizations drawn to Anthropic's Constitutional AI framework and its dedicated enterprise contracting relationships. According to market research published in May 2026, Claude Code's enterprise seat count grew 340% year-over-year, with particularly strong penetration in financial services and healthcare.

OpenAI's response has been to reposition Codex as a distinct, full-lifecycle product rather than a ChatGPT feature. The Ona deal accelerates that strategy by giving Codex a proprietary execution substrate—infrastructure OpenAI controls end to end—rather than relying on developers to configure their own environments.

The move also differentiates Codex from cloud-native approaches. Google's Gemini Code Assist integrates tightly with Google Cloud Run; Microsoft's GitHub Copilot Workspace is deeply entangled with Azure DevOps pipelines. Ona's architecture is cloud-agnostic, deployable on any major infrastructure provider, which preserves the flexibility that enterprise procurement teams increasingly demand.

"As Anthropic claims the enterprise, OpenAI fights back with the Ona deal," wrote analysts at Techzine Global, noting that Codex's integration of persistent cloud execution creates "a counterweight to the likes of Claude Code" at the infrastructure layer rather than just the model layer.

## What Happens to Existing Users

The Ona team, including engineers carried over from the Gitpod era, will work under OpenAI's Codex division. OpenAI has not yet announced a timeline for how existing Ona subscriptions will be handled or whether the product will continue as a standalone offering. The 2025 rebrand from Gitpod to Ona had already prompted some user migration to competitors including Codeflare and Daytona; the acquisition raises fresh questions about the long-term roadmap for customers not already on Codex.

## The Infrastructure Land Grab

OpenAI's 2026 acquisition spree—spanning security hardening, execution infrastructure, and earlier deals in voice and hardware—reflects a strategic recognition that model capability alone no longer differentiates the leading AI companies. Anthropic, Google, Microsoft, and now OpenAI are all investing in the surrounding infrastructure that makes models useful in real production environments: memory, sandboxing, observability, and the orchestration layers that connect agents to enterprise systems.

The AI coding-assistant market is entering a consolidation phase. The first generation offered suggestions inside existing IDEs. The second generation—Cursor, Devin, Claude Code—handled longer autonomous tasks. The emerging third generation, typified by what OpenAI is building with Codex plus Ona, places persistent, cloud-resident agents at the center of the software development lifecycle, checking back with humans at natural breakpoints rather than at every line of code.

With Codex at five million weekly users and growing, and the enterprise software development market estimated above $650 billion globally, Ona gives OpenAI a durable infrastructure position at precisely the moment that enterprises are deciding which AI coding platform becomes their default. The deal is subject to regulatory review; no closing date has been announced.
