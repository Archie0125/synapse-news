---
title: "Google's Gemini 3.6 Flash Brings Built-In Computer Use and Becomes the Default for Managed Agents"
summary: "Google launched Gemini 3.6 Flash on July 21 at $1.50 per million input tokens, adding built-in computer use, a 1-million-token context window, and 280 tokens per second throughput. The model is now the default powering Gemini API Managed Agents, which simultaneously gained background execution, remote MCP connections, scheduled cron triggers, and a free tier — making autonomous cloud agents significantly easier to build and run."
category: "developer-tools"
publishedAt: 2026-08-01
lang: "en"
featured: false
trending: true
sources:
  - name: "GCN"
    url: "https://gcn.com/google-upgrades-gemini-api-managed-agents/20244/"
  - name: "Google AI Blog"
    url: "https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/"
  - name: "Gemini API Changelog"
    url: "https://ai.google.dev/gemini-api/docs/changelog"
  - name: "BenchLM"
    url: "https://benchlm.ai/models/gemini-3-6-flash"
tags:
  - "Google"
  - "Gemini"
  - "AI agents"
  - "developer tools"
  - "MCP"
  - "LLM"
relatedSlugs:
  - "2026-07-31-google-deepmind-gemini-robotics-2-whole-body-en"
  - "2026-08-01-deepseek-v4-flash-0731-agent-benchmarks-en"
---

Two separate Google releases, arriving two weeks apart, have together shifted what developers can build with the Gemini API. On July 7, Managed Agents — Google's hosted sandbox infrastructure for autonomous agents — gained background execution, remote MCP connections, and scheduled triggers. On July 21, Gemini 3.6 Flash launched as the new default model powering those agents, bringing computer use, multimodal input, and a price point that undercuts its predecessor. Together they form a coherent developer story: a faster, more capable agent runtime at lower cost.

## Gemini 3.6 Flash: What Changed

Gemini 3.6 Flash sits between the flagship Gemini 3.5 Pro and the cost-optimized 3.5 Flash-Lite in Google's current model lineup. Its defining characteristics:

**Price**: $1.50 per million input tokens, $7.50 per million output tokens. This is competitive with other mid-tier frontier offerings but sits above the deeply discounted models from DeepSeek and the latest round of OpenAI price cuts.

**Speed**: The model runs at approximately 280 tokens per second, making it suitable for interactive applications where latency matters, including real-time voice interfaces and streaming code generation.

**Efficiency**: Google reports that 3.6 Flash uses roughly 17% fewer output tokens than its predecessor on equivalent tasks — a meaningful improvement for workloads billed by the output token.

**Context and output limits**: A 1-million-token context window accommodates entire codebases, long documents, or extended agent conversation histories. The maximum output per request is capped at 64,000 tokens.

**Input modalities**: The model accepts text, images, video, audio, and PDFs natively, which widens its applicability in enterprise workflows that mix document types.

**Computer use**: Perhaps the most significant new capability. Computer use — the ability for an agent to perceive and interact with a graphical interface, click elements, fill forms, and navigate applications — is now a built-in client-side tool accessible directly via the Gemini API and through Gemini Enterprise. This capability previously required external tooling or was accessible only through the Gemini Enterprise Agent Platform.

## Managed Agents: The Infrastructure Upgrade

The July 7 update to Managed Agents addressed some of the limitations that had made the platform less suitable for production workloads.

**Background execution.** Agents can now run long-horizon tasks asynchronously without maintaining an open connection from the client side. A developer triggers an agent, receives a task ID, and can poll for results — or configure a webhook to receive a completion notification. This is the difference between running a five-minute code review pipeline and running a four-hour repository audit.

**Remote MCP connections.** Agents can now connect to external Model Context Protocol servers, enabling them to use tools defined by third-party services without the tool code running inside the Google sandbox. A developer can wire an agent to a company's proprietary code search server, a customer database MCP endpoint, or any MCP-compatible internal tooling stack.

**Scheduled triggers.** Google added support for binding an agent, a prompt, and an environment to a cron expression, creating a persistent scheduled resource. An agent can be configured to run a nightly analysis of system logs, generate a weekly competitive intelligence report, or trigger on any recurring interval. Failed runs pause the schedule after five consecutive failures — a guard against silent cost accumulation from broken automations.

**Budget controls.** Developers can now set hard token budgets per agent run, preventing runaway inference costs on tasks that loop unexpectedly or encounter adversarial inputs designed to inflate context.

**Free tier.** Managed Agents are now available on API key projects without requiring a Gemini Enterprise subscription. This extends the platform to individual developers and small teams who previously couldn't access the sandboxed execution environment.

## The Antigravity Agent as a Starting Point

Google's reference agent for the Managed Agents platform is called Antigravity. It is a general-purpose agent that can reason, plan, write and execute code, manage files, and browse the web — all within an isolated Linux sandbox container — without any custom orchestration code. Developers interact with it through a prompt in Google AI Studio or the API, and it handles tool selection and sequencing autonomously.

The practical value is a significantly reduced setup cost for experimenting with agentic capabilities. A developer who wants to test whether an agent-based approach can handle their use case can do so against Antigravity before investing in custom orchestration. Companies including Ramp, Klipy, and Stitch reported using Managed Agents in early testing across financial operations, sales intelligence, and design automation workflows.

Custom agents extend the Antigravity foundation through AGENTS.md and SKILL.md markdown files that define behavior, registered via the API. Google's approach here prioritizes configuration-as-code, which means agent definitions can be version-controlled, reviewed, and deployed through standard software development workflows.

## Competitive Positioning

The timing of these releases places them squarely in the middle of an accelerating platform competition. OpenAI launched Presence — its enterprise agent governance platform — on July 22, one day after Gemini 3.6 Flash. Anthropic has had its enterprise operator toolkit available since early in the year. Microsoft continues to build Agent Mode into Azure AI and GitHub Copilot.

Google's differentiator is the depth of sandbox isolation and the integration with the broader Google Cloud ecosystem. MCP compatibility broadens the tool landscape. The free tier opens experimentation to a wider developer audience than enterprise-only platforms can reach.

What Google lacks relative to OpenAI's Presence is the governance and enterprise-grade policy layer: Managed Agents is fundamentally an execution platform, not an audit and compliance platform. Enterprise buyers who need documented human oversight and change management for deployed agents will still need to build that layer themselves, or look to platforms explicitly designed around it.

For independent developers and startups, though, the combination of Gemini 3.6 Flash's multimodal capability, the background execution infrastructure, remote MCP integration, and free tier access represents a materially improved platform for building autonomous agents compared to what was available even 90 days ago.

## What Developers Should Test

The highest-value experiments right now involve the intersection of computer use and background execution: tasks where an agent needs to navigate a graphical interface to extract or input information, and where that task runs for minutes or hours without requiring a live connection. Scheduled code review pipelines, competitive analysis crawlers, and document processing automations are the workflows most immediately suited to the new capability stack.

The Gemini API changelog notes that the gemini-robotics-er-1.6-preview model will be shut down on August 31, 2026, and several image generation models are being deprecated on August 17. Developers relying on those specific model identifiers should plan migrations before those dates.
