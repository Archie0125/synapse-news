---
title: "Mastra Raises $22M Series A to Become the Default TypeScript Framework for AI Agents"
summary: "Mastra, the open-source TypeScript framework for building AI agents, workflows, and RAG pipelines, has closed a $22 million Series A led by Spark Capital, bringing total funding to $35 million. With 22,000+ GitHub stars, 300,000+ weekly npm downloads, and teams at Brex, Sanity, and Factorial building agents with it, Mastra is pitching itself as a framework for every developer."
category: "developer-tools"
publishedAt: 2026-04-10T09:20:00Z
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "Mastra Blog"
    url: "https://mastra.ai/blog/series-a"
  - name: "DEV Community"
    url: "https://dev.to/gabrielanhaia/mastra-in-2026-what-it-is-when-to-use-it-and-how-it-compares-2go1"
  - name: "Generative Inc."
    url: "https://www.generative.inc/mastra-ai-the-complete-guide-to-the-typescript-agent-framework-2026"
tags:
  - "Mastra"
  - "TypeScript"
  - "AI agents"
  - "open source"
  - "developer tools"
  - "Series A"
  - "Spark Capital"
  - "RAG"
relatedSlugs:
  - "2026-04-04-cursor-devin-war-en"
  - "2026-04-04-solo-founder-ai-stack-en"
  - "2026-04-06-agentic-ai-foundation-en"
---

The race to become the default framework for AI agent development just got more serious. Mastra, the open-source TypeScript framework for building AI agents, announced a $22 million Series A led by Spark Capital, bringing its total capital raised to $35 million.

The milestone is significant not just for Mastra's trajectory, but for what it says about where enterprise AI development is heading: away from Python-first ML workflows and toward the TypeScript ecosystem that already powers most web and full-stack applications.

## The Problem Mastra Is Solving

Building AI agents in production involves more than stringing together LLM calls. Developers need durable workflow execution that survives failures, retrieval-augmented generation pipelines that can query knowledge bases, memory systems that maintain context across sessions, observability tooling to debug agent behavior, and integration layers that connect agents to external tools and APIs.

Most existing frameworks address one or two of these concerns. Mastra's bet is that TypeScript developers want a single, composable framework that handles all of them without requiring a Python interop layer or forcing them to stitch together half a dozen different libraries.

"We wanted to build what Rails was for web development," Mastra's founders have said in developer discussions—a convention-over-configuration framework that makes the hard default decisions so developers can focus on application logic rather than plumbing.

## The Numbers Tell a Clear Story

Mastra's adoption curve has been remarkably steep. The framework launched in October 2024, hit the front page of Hacker News in February 2025 and exploded from 1,500 to 7,500 GitHub stars in a single week. By January 2026, the project had published its 1.0 release and was sitting at 22,000+ GitHub stars with over 300,000 weekly npm downloads.

For context, 300,000 weekly npm downloads puts Mastra in the same order of magnitude as mid-tier React ecosystem libraries—a category that typically represents production usage, not hobby experimentation. The weekly download number also grows with every new project that depends on Mastra, not just every developer trying it for the first time.

Teams at scale-ups including Brex, Sanity, and Factorial are building agents within their apps with Mastra. All three are scale-ups with real production traffic, which means Mastra has already proven that its abstractions hold up under non-trivial load and complexity.

## What the Framework Actually Provides

Mastra is structured around four main primitives: agents, tools, workflows, and RAG.

**Agents** — Claude, GPT-4o, Gemini, or any model-compatible entity that can perceive inputs, use tools, and produce outputs. Mastra handles the agent loop, tool dispatch, and error recovery, with built-in support for structured output and multi-step reasoning.

**Workflows** — Durable, graph-based execution engines for multi-step agent tasks. Workflows give explicit control flow: steps can be chained sequentially, branched conditionally, or run in parallel, with suspend/resume for human-in-the-loop approval gates.

**RAG Pipelines** — Mastra provides built-in abstractions for chunking documents, generating embeddings, storing them in vector databases, and retrieving relevant context at query time. The framework supports pgvector (PostgreSQL), Pinecone, Qdrant, and MongoDB for vector storage.

Memory, logging, and telemetry are first-class citizens in the framework, with OpenTelemetry integration for distributed tracing of agent workflows across production systems.

## Why TypeScript Matters

The choice of TypeScript as the primary language is not incidental. Virtually all modern web applications—and the majority of SaaS products—are built in JavaScript or TypeScript. When an AI feature is added to one of these products, the engineering team wants to write it in the same language as the rest of their stack, not context-switch into Python.

Python frameworks like LangChain, LlamaIndex, and LangGraph are mature and widely deployed, but they require a separate runtime, separate dependency management, and a different deployment model from TypeScript services. For a company whose backend is Node.js, adopting a Python-based AI agent framework means either introducing a second language or building an RPC bridge—both of which add complexity and operational overhead.

Mastra sidesteps this entirely. It runs in any Node.js or Bun runtime, integrates with existing TypeScript projects with a standard npm install, and plays nicely with common ecosystem tools like Prisma (database), tRPC (API), and Next.js (frontend).

## Spark Capital and the Funding Context

Spark Capital's lead role in the Series A is notable. The firm backed Twitter, Slack, and Coinbase in their early stages, and has more recently been active in developer-infrastructure plays including Vercel and Linear. Their bet on Mastra fits a consistent thesis: developer tools that reduce friction at the foundation compound adoption faster than application-layer products.

The $22 million round will primarily fund engineering headcount to accelerate the roadmap—which, according to Mastra's public communications, includes enhanced multi-agent coordination, tighter IDE integration (particularly for VS Code and Cursor), improved eval frameworks for testing agent behavior, and managed cloud infrastructure for production agent hosting.

Mastra has also launched the Mastra platform alongside the funding news, including Mastra Server for deploying agents and workflows, extending beyond the framework layer.

## The Bigger Picture

Mastra's Series A reflects a broader maturation in how enterprises think about AI development. The first wave of AI integrations was exploratory—PoCs and chatbots. The current wave is about production deployment of autonomous workflows, and developers are increasingly demanding frameworks that treat reliability, observability, and multi-model flexibility as first-class concerns rather than afterthoughts.

For the TypeScript ecosystem specifically, Mastra's momentum is a sign that enterprise AI development is no longer a Python-only domain. The language barrier between "AI team" and "product team" is shrinking—and for startups that want to ship AI-native features without building separate AI infrastructure teams, that's exactly what they need.

The fact that Mastra is open source is also strategically important. It builds trust in a domain where developers are understandably skeptical of vendor lock-in, and it creates a community-driven feedback loop that accelerates framework quality faster than any closed-source competitor can match.

*Correction (November 15, 2026): 9 sentences were corrected or removed to match the sources listed on this page.*
