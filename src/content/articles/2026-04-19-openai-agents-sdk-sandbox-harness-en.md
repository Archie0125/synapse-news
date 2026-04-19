---
title: "OpenAI Rewrites Its Agents SDK With a Native Sandbox and Model-Native Harness for Long-Horizon Tasks"
summary: "OpenAI this week released a major update to its Agents SDK, adding a model-native harness with configurable memory and filesystem tools, plus native sandbox execution through integrations with E2B, Modal, Vercel, and others. Launching first in Python, the update gives enterprise developers the full infrastructure layer they previously had to build from scratch."
category: "developer-tools"
publishedAt: 2026-04-19
lang: "en"
featured: false
trending: true
sources:
  - name: "OpenAI"
    url: "https://openai.com/index/the-next-evolution-of-the-agents-sdk/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents/"
  - name: "Help Net Security"
    url: "https://www.helpnetsecurity.com/2026/04/16/openai-agents-sdk-harness-and-sandbox-update/"
  - name: "Dataconomy"
    url: "https://dataconomy.com/2026/04/17/openai-updates-agents-sdk-with-sandboxed-execution-tools/"
tags:
  - "OpenAI"
  - "Agents SDK"
  - "AI agents"
  - "sandbox"
  - "developer tools"
  - "enterprise AI"
  - "Python"
relatedSlugs:
  - "2026-04-10-anthropic-claude-managed-agents-en"
  - "2026-04-11-microsoft-agent-framework-1-0-ga-en"
  - "2026-04-04-mcp-protocol-explosion-en"
---

OpenAI released a substantial update to its Agents SDK on April 15, 2026, adding capabilities that significantly close the gap between what the framework provided out of the box and what production-grade agentic applications actually require. The update centers on two major additions: a model-native harness that lets agents operate across files and tools on a computer, and native sandbox execution that lets that work run safely inside isolated environments — without developers having to wire up both layers themselves.

The release, which launched initially in Python with TypeScript support planned for a future update, reflects OpenAI's read on where enterprise AI development has been stalling: not at the model capability level, but at the infrastructure layer that connects model intelligence to real-world task execution.

## What the Harness Does

The model-native harness is the conceptual center of this update. Where the previous Agents SDK required developers to manually configure how agents interact with tools, memory, and execution environments, the new harness provides a turnkey but flexible foundation that handles those primitives as first-class constructs.

Specifically, the updated harness includes:

**Configurable memory**: Agents can now maintain context across turns and across tasks through a structured memory interface, rather than relying on developers to manage state externally or cram everything into a context window.

**Sandbox-aware orchestration**: The harness natively understands that its tools may be running inside a sandboxed execution environment, adjusting how it routes tasks and handles outputs accordingly.

**Filesystem tools**: A suite of built-in tools modeled on the Codex-style toolkit — reading files, writing files, running commands, navigating directory structures — that agents can use without custom implementation.

**Standardized integrations**: Rather than requiring developers to build their own adapters for common agent system primitives, the harness ships with standardized bindings that match what has emerged as de facto standard architecture across production agent systems.

The result is a harness that removes a significant portion of the boilerplate work from enterprise AI teams. Instead of spending engineering cycles on scaffolding, teams can focus on the specific tools and workflows that differentiate their applications.

## Native Sandbox Execution

The second major addition is native sandbox support — what OpenAI describes as giving developers "the execution layer out of the box." Prior to this update, developers who wanted their agents to run code safely inside isolated environments had to source and integrate their own sandbox infrastructure, then wire it into the SDK manually.

The updated Agents SDK supports bring-your-own-sandbox or turn-key integration with seven providers at launch: **Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, and Vercel**. Each provides a controlled computer environment where agents can execute code, access files, install dependencies, and perform long-horizon workflows without the risk of escaping into the host environment or accidentally touching production systems.

This is particularly significant for enterprise security and compliance postures. Many organizations have been cautious about deploying AI agents that can run arbitrary code, precisely because managing the blast radius of unintended behavior required significant custom work. With sandbox execution standardized into the SDK, that barrier drops substantially.

## The Manifest Abstraction

Complementing the sandbox integration is a new Manifest abstraction — a workspace contract that describes the agent's operating environment in a portable, provider-agnostic format. The Manifest specifies:

- Local files and directories the agent has access to
- Git repositories to mount
- Environment variables and configuration
- User and group permissions
- Storage mounts from external providers

For storage, the Manifest supports cloud providers including **AWS S3, Google Cloud Storage, Azure Blob Storage, and Cloudflare R2**, allowing agents to work directly with data in existing cloud infrastructure rather than requiring developers to pre-stage data in a specific format.

The Manifest's portability is key: an agent configured to run on E2B can be moved to Daytona or Vercel with minimal configuration changes, avoiding vendor lock-in at the sandbox layer.

## Why This Release Matters Now

The timing of this update is not incidental. The past six months have seen a proliferation of agentic frameworks — Anthropic's Claude Managed Agents, Microsoft's Agent Framework 1.0, open-source projects like AutoGen and Mastra — each with their own conventions for memory, tool use, and execution. Developers building enterprise applications face a fragmented landscape with few shared standards below the model API layer.

OpenAI's SDK update doesn't attempt to unify this landscape, but it makes a specific bet: that the harness-plus-sandbox pattern will become the dominant architecture for production agents, and that OpenAI's implementation of it should be the default starting point. The sandbox provider integrations — spanning cloud giants like Cloudflare and Vercel, and specialized providers like E2B and Modal — signal that OpenAI is trying to build an ecosystem rather than a closed stack.

This also represents a subtle but significant shift in OpenAI's developer strategy. The original Agents SDK, launched in early 2025, was a relatively thin layer — useful for orchestrating multi-step tasks but requiring substantial custom work to deploy in production. This update is a statement that OpenAI intends the SDK to be the full-stack platform for enterprise agent development, not just a starting point that teams immediately replace with custom infrastructure.

## Enterprise Implications

For enterprise development teams, the practical implications are several:

**Reduced time-to-production**: The harness and sandbox eliminate two of the largest categories of custom infrastructure work required to deploy production agents. Teams that previously spent weeks on scaffolding can now start from a much higher baseline.

**Improved security posture**: Standardized sandboxing reduces the attack surface of agentic deployments and makes it easier to reason about what an agent can and cannot access in a production environment.

**Storage integration**: The Manifest's support for S3, GCS, Azure Blob, and Cloudflare R2 means agents can work directly with data in enterprise data infrastructure rather than requiring data engineering teams to create specialized data pipelines.

**Ecosystem coherence**: As more teams adopt the same harness conventions, it becomes easier to share agents, tools, and workflows across teams and organizations — a network effect that strengthens as adoption grows.

Pricing for the new SDK capabilities uses standard API pricing, billed on tokens and tool use. There is no additional charge for the harness or Manifest abstractions; sandbox provider costs are billed directly by the respective providers.

## What's Next

OpenAI committed to bringing the harness and sandbox capabilities to TypeScript in a future release, acknowledging that a significant portion of enterprise development work happens in TypeScript rather than Python. The company is also working on additional agentic capabilities — including code mode and subagents — for both languages.

The broader direction is clear: OpenAI sees the Agents SDK as the primary interface through which enterprise developers will interact with its models for task execution — and it is investing accordingly to make that interface competitive with alternatives that have had more time to mature.
