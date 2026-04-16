---
title: "Anthropic Accidentally Leaks 512,000 Lines of Claude Code Source via npm Bug"
summary: "A Bun bundler bug exposed the complete source code of Claude Code v2.1.88 — 1,900 TypeScript files and 512,000 lines — on the npm registry for over three hours. A trojanized HTTP client bundled in the same window raised supply chain attack concerns before Anthropic pulled the package."
category: "developer-tools"
publishedAt: 2026-04-05T09:00:00Z
lang: "en"
featured: true
trending: false
sources:
  - name: "The Register"
    url: "https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/"
  - name: "TechRadar"
    url: "https://www.techradar.com/pro/security/anthropic-confirms-it-leaked-512-000-lines-of-claude-code-source-code-spilling-some-of-its-biggest-secrets"
  - name: "Cybernews"
    url: "https://cybernews.com/security/anthropic-claude-code-source-leak/"
  - name: "NodeSource"
    url: "https://nodesource.com/blog/anthropic-claude-code-source-leak-bun-bug"
tags:
  - "anthropic"
  - "claude-code"
  - "security"
  - "supply-chain"
  - "open-source"
  - "npm"
relatedSlugs:
  - "2026-04-04-mcp-protocol-explosion-en"
  - "2026-04-04-cursor-devin-war-en"
---

In the early hours of March 31, 2026, security researcher Chaofan Shou noticed something unusual on the npm registry: the complete, unobfuscated source code of `@anthropic-ai/claude-code` version 2.1.88 — approximately 1,900 TypeScript files totaling 512,000 lines — sitting in a publicly accessible Cloudflare R2 storage bucket, linked directly from the published package.

By the time Anthropic pulled the package at 03:29 UTC, the repository had been forked more than 41,500 times. The window of exposure — just over three hours — was enough to make one of the most consequential accidental open-sourcings of a proprietary AI tool's codebase a permanent fact of the internet.

## The Bug That Broke the Build

The root cause traces back to an acquisition Anthropic made in late 2024: Bun, the high-performance JavaScript bundler and runtime. After integrating Bun into the Claude Code build pipeline, a known Bun bug continued generating source maps even when the `development: false` flag was explicitly set in the build configuration. Source maps, which are normally used to aid debugging by mapping minified code back to its original form, are almost never intended for public distribution in production releases.

In this case, the source maps contained direct URLs pointing to an unobfuscated zip archive of the entire TypeScript codebase on Anthropic's Cloudflare R2 bucket. Any developer who installed the package and knew where to look — or who simply ran the right tooling — could retrieve the complete source.

"This was a release packaging issue caused by human error, not a security breach of our systems," Anthropic stated in its post-incident communication. The company emphasized that no customer data was accessed and no internal AI model weights were exposed. What was exposed, however, was the company's internal architecture for its flagship developer product: the slash command implementations, tool call structures, built-in prompt scaffolding, and the mechanics of how Claude Code communicates with Anthropic's backend APIs.

## A Trojan in the Same Window

The source code exposure was alarming enough. But security researchers discovered a second, more troubling anomaly in the same 03-hour window: a trojanized HTTP client library bundled as a dependency of the compromised Claude Code release.

The malicious package — described by Cybernews and NodeSource analysts as a cross-platform remote access trojan (RAT) — was not Anthropic's doing. It appears to have been injected by a third party who detected the vulnerable package in real time and modified one of its dependency chain links before the window closed. The RAT was designed to be cross-platform, targeting macOS, Linux, and Windows developer environments.

Anthropic confirmed awareness of the RAT component but stopped short of attributing it or confirming the attack vector. Independent researchers noted that the package's dependency resolution at install time made it possible for a poisoned transitive dependency to reach developers who ran `npm install` during the window — a classic supply chain attack scenario.

The incident underscores a structural vulnerability in the way AI tooling is distributed. Unlike traditional software, AI developer tools like Claude Code sit at the intersection of high-trust environments (developer machines with full file system access) and high-value targets (access to LLM APIs with billing implications and potential data exposure). A successful RAT deployment in this context would be significantly more dangerous than in a typical SaaS context.

## What the Source Code Revealed

For the 41,500+ forks that captured the source before removal, the codebase offered a detailed view into how Anthropic has engineered its flagship developer product. The exposed code included:

**Slash command implementations**: The internal architecture of commands like `/commit`, `/review-pr`, and other built-in Claude Code skills — including the prompts, tool chains, and control flow logic that power them.

**Tool call schemas**: The complete JSON schemas defining how Claude Code structures calls to Anthropic's API, including tool use definitions that were not previously documented publicly.

**Session management logic**: Code governing how Claude Code manages conversation state, context compression, and the handoff between different agent types.

**Backend communication patterns**: Details of how the client authenticates and communicates with Anthropic's infrastructure, which security researchers noted could theoretically be used to build unauthorized API clients.

**Internal testing scaffolds**: Unit tests and integration test fixtures that, while not directly exploitable, give competitors a detailed map of the product's intended behavior and edge cases.

Anthropic has declined to provide a complete inventory of what was in the leaked source, but the 1,900-file scope suggests the leak captured substantially all of Claude Code's client-side implementation.

## The Bigger Picture: AI Tool Supply Chains Are Fragile

The incident arrives at a moment when AI developer tools have become critical infrastructure for a growing share of software development teams. Claude Code, GitHub Copilot, and Cursor each have hundreds of thousands of daily active users who route significant portions of their coding workflow through these tools — including code that may contain sensitive business logic, API keys, and proprietary algorithms.

The supply chain attack dimension is particularly sobering. The same npm package delivery mechanism that made Anthropic's source code accidentally public also made it a vector for malicious code injection. The 2021 Log4Shell vulnerability demonstrated how a widely-used library could become a catastrophic attack surface overnight; the Claude Code incident suggests AI tooling distributions are subject to the same dynamics.

NodeSource's post-mortem analysis recommended several mitigations: lockfile enforcement to prevent transitive dependency substitution, reproducible build attestation for AI tool releases, and out-of-band integrity verification for packages that run with elevated system permissions. Anthropic has not yet published its own post-incident security improvements.

For the developer community, the incident raises a harder question: as AI coding assistants become more deeply integrated into build pipelines, CI/CD systems, and IDE workflows, the security surface they represent grows correspondingly. The Claude Code source leak was, in Anthropic's own framing, human error — not a targeted attack. The trojan injection that rode alongside it was not.

The combination of both in a single three-hour window is a stress test result the industry will be digesting for some time.
