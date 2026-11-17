---
title: "Mistral Medium 3.5 Arrives With 77.6% SWE-Bench Score and Cloud-Native Coding Agents"
summary: "Mistral AI launched Medium 3.5, a dense 128B open-weight model that scores 77.6% on SWE-Bench Verified, alongside Vibe remote agents that run asynchronous cloud coding sessions from the CLI or Le Chat. The dual release positions Mistral as a serious challenger in the agentic developer-tools market just ahead of Google I/O 2026."
category: "developer-tools"
publishedAt: 2026-05-03
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "Mistral AI"
    url: "https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5"
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/05/02/mistral-ai-launches-remote-agents-in-vibe-and-mistral-medium-3-5-with-77-6-swe-bench-verified-score/"
  - name: "The Decoder"
    url: "https://the-decoder.com/mistrals-new-flagship-medium-3-5-folds-chat-reasoning-and-code-into-one-model/"
tags:
  - "Mistral AI"
  - "open-weight models"
  - "coding agents"
  - "developer tools"
  - "SWE-Bench"
  - "Le Chat"
relatedSlugs:
  - "2026-04-20-app-store-vibe-coding-surge-en"
  - "2026-04-11-microsoft-agent-framework-1-0-ga-en"
  - "2026-04-04-cursor-devin-war-en"
---

Mistral AI shipped two intertwined products that together reframe what a mid-tier open-weight model can do: **Mistral Medium 3.5**, a dense flagship with 128 billion parameters that scores 77.6 percent on SWE-Bench Verified in Mistral's own benchmarks, and **Vibe Remote Agents**, an asynchronous cloud execution layer for running coding sessions in the cloud.

The release is strategically timed. Google I/O is weeks away, Anthropic's Claude 4 family is expanding, and OpenAI is competing on every front. Mistral needed a statement. Medium 3.5 is it.

## One Model, Three Regimes

The core architectural bet behind Medium 3.5 is density over sparsity. Unlike Mistral Large 3, which deploys a 675B mixture-of-experts architecture with only 41B active parameters per token, Medium 3.5 keeps all 128 billion parameters active on every inference pass. The tradeoff is raw compute cost per token — but the gain is consistency, especially on multi-step agentic workflows where sparse models can produce erratic outputs across sequential reasoning steps.

The model ships with a 256K token context window and native multimodal vision support, handling text, images, and structured data without an external transcription layer. Reasoning effort is now configurable per API request: developers can dial compute down for simple lookups and up for deep multi-step analysis, using the same model across both regimes.

On benchmarks, Medium 3.5 posts numbers that challenge models significantly above its price tier. The headline figure — 77.6% on SWE-Bench Verified — outperforms Devstral 2 (Mistral's own coding-specialist model) and beats Qwen3.5 397B, a model with more than three times the parameter count. On the T3-Telecom benchmark, Medium 3.5 scores 91.4% in Mistral's own benchmarks.

Through the API, pricing is $1.50 per million input tokens and $7.50 per million output tokens.

## Vibe Goes Asynchronous and Cloud-Native

The second half of the announcement is arguably more disruptive to developer workflows than the model itself.

Mistral's Vibe coding tool now supports **remote agents**: coding sessions that run asynchronously in isolated cloud sandboxes, with integrations for GitHub, Linear, Jira, Sentry, Slack, and Teams. The practical upshot is that a developer can issue a task — "fix this bug class, open a PR" — and walk away. When the session completes, a pull request lands in GitHub with full diff, test results, and an explanation of every decision made.

Sessions can be spawned from either the Vibe CLI or from Le Chat, Mistral's consumer-facing assistant. Crucially, local sessions can be "teleported" to the cloud mid-task without losing session history or task state — a feature designed for the common scenario where a developer starts debugging locally, realizes the task is longer than expected, and wants to continue without keeping their laptop open overnight.

The sandboxed execution model is not simply convenient; it is a security architecture decision. Each remote agent session runs in an ephemeral environment with no persistent filesystem access, and all credentials are injected at runtime via Mistral's secrets management layer. For enterprises wary of persistent AI access to codebases, this addresses a real objection.

## Le Chat Gets Work Mode

The announcement also added Work Mode to Le Chat, an agentic mode built for multi-step tasks across multiple tools. Work Mode connects Le Chat directly to email, calendar, Jira, Slack, and document management systems via built-in connectors. The model can execute multi-step workflows across these tools simultaneously — drafting a project update, scheduling a review meeting, and updating a Jira ticket in a single orchestrated run.

The differentiator Mistral is emphasizing: all tool calls and reasoning steps are visible to the user in real time, and explicit approval is required before any sensitive actions are taken (sending an email, modifying a calendar event). This is a deliberate counter-positioning to more autonomous agent frameworks that black-box their decision chains.

Work Mode is available on the Pro, Team, and Enterprise plans, and the Medium 3.5 weights ship under a Modified MIT License that carves out exceptions for high-revenue companies.

## The Competitive Calculus

The timing and packaging of this release expose a clear strategic logic. Mistral's strongest differentiators have always been openness, European regulatory positioning (critical for GDPR-sensitive enterprises), and competitive performance-per-dollar. Medium 3.5 reinforces all three.

Against Cursor and Devin, Vibe Remote Agents competes directly on the agentic coding workflow, with the advantage of being model-provider-native rather than a wrapper layer. Against Claude for Work (Anthropic's enterprise offering) and Microsoft Copilot, Le Chat Work Mode offers open-weight optionality that neither competitor can match.

The benchmark credibility matters, too. A 77.6% SWE-Bench Verified score from a 128B model — available at API prices well below the frontier tier — changes the calculus for startups and mid-market enterprises that have been priced out of GPT-5.5 or Claude 4 at scale.

## What Comes Next

The Medium 3.5 weights are already available for download on Hugging Face, under a Modified MIT License rather than the Apache 2.0 license Mistral has used before.

For developers, the operative question is not whether Medium 3.5 is competitive on benchmarks — it clearly is. The question is whether Vibe Remote Agents' cloud execution model can accumulate the developer ecosystem gravity that competing tools have built. That is a distribution problem, not a capability problem, and it is one Mistral has historically struggled with more than the technical side.

Google I/O and whatever Google announces for Gemini's agentic developer story will be the real stress test for this week's launch.

*Correction (November 15, 2026): 8 sentences were corrected or removed to match the sources listed on this page.*
