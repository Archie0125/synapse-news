---
title: "The Agentic AI Foundation: How Tech's Biggest Rivals United to Build Open Standards for AI Agents"
summary: "The Linux Foundation's Agentic AI Foundation (AAIF) has quietly become one of the most significant governance moves in AI history — uniting OpenAI, Anthropic, Google, Microsoft, AWS, and Block behind open standards for AI agents. With MCP crossing 97 million monthly downloads and AGENTS.md in 60,000+ open source projects, the foundation is turning competitive rivals into infrastructure collaborators."
category: "developer-tools"
publishedAt: 2026-04-06T09:00:00Z
lang: "en"
featured: false
trending: false
sources:
  - name: "Linux Foundation"
    url: "https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation"
  - name: "OpenAI"
    url: "https://openai.com/index/agentic-ai-foundation/"
  - name: "MCP Blog"
    url: "https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/"
  - name: "Block"
    url: "https://block.xyz/inside/block-anthropic-and-openai-launch-the-agentic-ai-foundation"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-google-openai-and-anthropic-join-forces-to-form-agentic-ai-alliance-according-to-report-organization-backed-by-the-linux-foundation-is-set-to-create-open-source-standards-for-ai-agents"
tags:
  - "AAIF"
  - "Linux-Foundation"
  - "MCP"
  - "AI-agents"
  - "open-standards"
  - "developer-tools"
  - "anthropic"
  - "openai"
relatedSlugs:
  - "2026-04-04-mcp-protocol-explosion-en"
  - "2026-04-06-microsoft-mai-models-independence-en"
  - "2026-04-06-openai-superapp-en"
---

## Strange Bedfellows

When was the last time OpenAI and Anthropic did something together? The two companies are perhaps the fiercest rivals in AI — competing for researchers, customers, benchmark supremacy, and narrative dominance. Google and Microsoft have spent decades as platform-layer adversaries. Yet in December 2025, all four — plus Amazon Web Services, Block, Bloomberg, and Cloudflare — co-founded the Agentic AI Foundation (AAIF) under the Linux Foundation.

The precedent for this kind of pre-competitive collaboration is well-established in infrastructure technology. TCP/IP, HTTP, Linux itself, Kubernetes — the protocols and platforms that form the invisible backbone of modern computing were built through exactly this kind of industry coordination. Competitors cooperate on standards because interoperability benefits everyone, and then compete fiercely on top of those standards. Nobody gains by owning a proprietary version of TCP/IP; everybody gains by building better products on top of a shared network.

The AAIF is the AI industry making the same bet for the agentic era.

## What the Foundation Is Building

The AAIF launched with three founding technical projects, each donated by its original creator:

**Model Context Protocol (MCP)**, contributed by Anthropic, is the universal open standard for connecting AI models to external tools, data sources, and applications. Introduced in late 2024, MCP has grown into one of the fastest-adopted open-source AI projects in history: as of early 2026, it registers over 97 million monthly SDK downloads, more than 10,000 active MCP servers, and first-class support across ChatGPT, Claude, Cursor, Gemini, Microsoft Copilot, Visual Studio Code, and dozens of other platforms.

By donating MCP to the AAIF, Anthropic made a calculated choice: accept the loss of proprietary control over the standard in exchange for dramatically faster adoption. Enterprises don't build critical infrastructure on protocols controlled by single vendors. They build on open standards with transparent governance. The move transformed MCP from "Anthropic's protocol that others are adopting" into "the industry's protocol that everyone maintains."

**AGENTS.md**, contributed by OpenAI, is a lighter-weight standard — but its adoption numbers are striking. The specification provides AI coding agents with a consistent source of project-specific guidance: instructions, constraints, and context that allow agents to operate reliably across different repositories and toolchains. Over 60,000 open source projects have already adopted AGENTS.md. Think of it as a `.gitignore` for AI agents — a simple file that dramatically improves the reliability of agentic operation in any given codebase.

**goose**, contributed by Block (formerly Square), is an open-source, local-first AI agent framework that combines language models with extensible tools and MCP-based integration. It represents a different point in the stack than MCP or AGENTS.md — not a protocol or a specification, but a reference implementation of an agentic system built on open standards.

## Why February 2026 Was a Turning Point

AAIF launched in December 2025 with its founding platinum members. But the February 2026 announcement of 97 new members — 18 at the Gold tier and 79 at Silver — signaled that the foundation had crossed a threshold from founding coalition to genuine industry movement.

This matters for reasons beyond the headline number. Enterprise technology decisions move slowly. When 97 companies join an open standards body within two months of its founding, it typically means procurement and engineering leadership at large organizations has concluded that the standard is safe to build on — that it has enough industry backing to avoid the fate of abandoned standards that left billions of dollars of vendor lock-in stranded.

The AAIF has achieved that signal faster than almost any comparable standards body in recent memory.

## The Enterprise Stakes

The urgency behind AAIF is visible in the analyst forecasts. Gartner predicts that 40% of enterprise applications will include task-specific AI agents by the end of 2026 — up from less than 5% just a year earlier. That eight-fold increase represents an enormous infrastructure buildout, and all of it requires solutions to the fundamental interoperability problem: how does an agent in one system talk to tools and data in another?

Without open standards, the answer to that question is vendor lock-in. Every major AI platform — OpenAI, Anthropic, Google, Microsoft — has a natural incentive to create proprietary agent frameworks that bind customers to their model ecosystem. The AAIF represents the collective recognition that this outcome would be bad for the entire industry: it would slow adoption, create security fragmentation, and ultimately benefit no one.

The MCP's success illustrates what open standards can achieve. Before MCP, connecting an AI model to an external tool required custom integration for every model-tool pair. With MCP, any compliant model can connect to any compliant tool with a single integration on each side. The combinatorial explosion of compatibility that MCP enables — theoretically infinite model-tool combinations from N+M integrations rather than N×M — is the same logic that made the web possible.

## Governance Tensions

The AAIF has critics, and their concerns are worth acknowledging. A Medium post by AI governance researcher Shashi Jagtap in December 2025 catalogued what he called "closed governance and a platinum paywall" — noting that platinum membership costs significantly more than silver or gold tiers, and that decision-making power in most Linux Foundation directed funds tracks closely to membership tier.

The critique: the AAIF presents as an open, democratic standards body, but its governance structures give disproportionate weight to the eight platinum members who are also the AI industry's most powerful incumbents. A startup building on MCP has no meaningful vote on the standard's technical direction.

This is not unique to AAIF — it's a structural feature of most large open-source foundations. The Linux Foundation, Apache Foundation, and Cloud Native Computing Foundation all have tiered membership structures that concentrate governance power. The counterargument is that this is simply realistic: standards bodies need sustained funding and organizational commitment to function, and large companies provide both. The open-source code and specifications remain available to everyone regardless of membership tier.

## What Comes Next

The AAIF's near-term roadmap focuses on several areas: security standards for agentic systems (how do you authenticate, authorize, and audit agents that take actions on users' behalf?), interoperability testing frameworks, and — perhaps most ambitiously — something analogous to an "open skills standard" for agents, enabling agents built on different frameworks to share capabilities.

The last item is the most technically ambitious. If successful, it would mean that an agent built using OpenAI's framework could invoke a skill developed for Anthropic's ecosystem, mediated by open standard protocols. That level of interoperability would be genuinely transformational for enterprise AI adoption.

Cisco joined AAIF in January 2026, bringing its networking and security expertise to the agent authentication problem — a signal of how seriously large infrastructure companies are taking the governance work.

The history of computing suggests that the battle for agentic AI will ultimately be won at the standards layer, not the model layer. Models will come and go, improve and compress. The protocols they run on will outlast any individual company's product cycle. AAIF is a bet that the most important rivals in AI understand this — and that their collective interest in a thriving agentic ecosystem outweighs their individual interest in proprietary control.

Given who signed up, it's a bet worth watching closely.
