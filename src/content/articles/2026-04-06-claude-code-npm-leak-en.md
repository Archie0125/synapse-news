---
title: "Anthropic Accidentally Publishes 512,000 Lines of Claude Code Source to npm"
summary: "A misconfigured build step in Claude Code v2.1.88 exposed 1,906 TypeScript files and 512,000 lines of source code to the public npm registry — the agentic harness governing how Claude uses tools, manages files, and orchestrates multi-agent workflows. The code spread to 50,000+ GitHub stars within hours before Anthropic pulled the package."
category: "developer-tools"
publishedAt: 2026-04-06
lang: "en"
featured: false
trending: true
sources:
  - name: "The Register"
    url: "https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know"
  - name: "Gizmodo"
    url: "https://gizmodo.com/source-code-for-anthropics-claude-code-leaks-at-the-exact-wrong-time-2000740379"
  - name: "The Hacker News"
    url: "https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html"
tags:
  - "anthropic"
  - "claude-code"
  - "open-source"
  - "npm"
  - "source-code-leak"
  - "developer-tools"
  - "security"
relatedSlugs:
  - "2026-04-06-anthropic-claude-mythos-en"
  - "2026-04-04-mcp-protocol-explosion-en"
  - "2026-04-04-cursor-devin-war-en"
---

## How 512,000 Lines of Code Escaped

On March 31, 2026, Anthropic shipped Claude Code v2.1.88 to the public npm registry. Alongside the bundled production code, it contained something it shouldn't have: a 59.8 MB source map file containing 1,906 TypeScript source files and 512,000 lines of code — the complete, human-readable source of the Claude Code agent harness.

The root cause traces to a tooling migration. Anthropic had switched Claude Code's bundler to Bun after acquiring the company in late 2024. Bun contains a known bug: it generates source maps even when the `development: false` flag is explicitly set. In production builds, source maps should be omitted — they exist to help developers debug minified code and have no place in a published package. The flag was set correctly. The bundler ignored it.

The package went live with the source map attached. Nobody at Anthropic noticed.

## Discovered by an Intern, Seen by Millions

Discovery credit goes to Chaofan Shou, a software engineering intern at Solayer Labs. Shou was exploring the published npm package for a routine integration task when he noticed the source map, realized what it was, and posted about it on X. The tweet generated 16 million views within 24 hours.

On GitHub, a repository forked from the leaked source code hit 50,000 stars and 41,500 forks in under two hours — making it one of the fastest-spreading code repositories in the platform's history. By the time Anthropic pulled the affected npm package at approximately 08:00 UTC, the code had already been downloaded, mirrored, and archived across dozens of platforms.

Anthropic acknowledged the incident and attributed it to the Bun toolchain bug. They have since patched their build pipeline to strip source maps regardless of bundler behavior.

## Why This Is More Sensitive Than a Model Weight Leak

The immediate instinct when hearing "AI source code leak" is to think of model weights — the billions of parameters that encode what a model knows and how it reasons. Claude's weights were not exposed. What was exposed is arguably more strategically sensitive in a different way: the agentic harness.

Claude Code's source governs how the Claude model interfaces with the real world. This code determines how Claude reads and writes files, executes bash commands, calls external APIs, manages conversation context across long-running agent sessions, coordinates with sub-agents in multi-agent workflows, and handles error recovery when tools fail. It is the operational layer — the difference between a language model that generates text and an agent that takes actions.

Understanding this harness gives competitors a detailed map of Anthropic's architectural decisions: how they handle tool use authorization, what safety checks run before file writes or shell commands execute, how they structure agent memory and state management, and where the boundaries between Claude's model layer and its orchestration layer sit. These are decisions that took years of engineering to get right, and they don't appear in any of Anthropic's public research papers.

Security researchers have also noted a more immediate concern: the source code reveals the exact structure of Claude Code's tool call authorization logic, which could theoretically inform attempts to craft prompts or tool responses that bypass intended safety restrictions. Anthropic has said it has found no evidence that the exposed code has been used maliciously, but acknowledged that "any responsible disclosure period was effectively zero."

## The Timing Could Not Be Worse

Anthropic is in the middle of a sensitive period. The company recently confirmed (via a separate accidental leak from a misconfigured CMS) the existence of Claude Mythos, its most powerful model yet, which it is quietly deploying to enterprise customers in the cybersecurity vertical. Two accidental exposures in the span of two weeks has raised questions about Anthropic's internal security posture — particularly ironic for a company whose primary differentiating narrative is careful, responsible AI development.

The Bun acquisition is also newly under scrutiny. Bun was acquired specifically because its bundler is faster than alternatives like esbuild and webpack — a meaningful advantage for developer experience. But the source map bug was a known issue in Bun's open-source tracker before the acquisition. The question of whether Anthropic's infrastructure team properly audited Bun's known issues before migrating a security-sensitive production pipeline is now being asked publicly.

For its part, Bun's development team confirmed the bug and released a patch the same day. The fix ensures `development: false` is honored regardless of other configuration settings.

## What the Code Reveals

Developers who examined the source before it was widely pulled described several notable architectural decisions:

**Multi-agent coordination**: Claude Code implements a hierarchical agent model where a "root" agent can spawn "sub-agents" with explicitly scoped permissions. Sub-agents cannot access files or execute commands outside their designated scope without the root agent's explicit delegation. The architecture appears designed to limit blast radius when a sub-agent misbehaves or is compromised.

**Tool authorization middleware**: Every tool call — file read, file write, bash execution, web fetch — passes through a shared authorization middleware that checks against a session-level permission model. Permissions can be granted broadly ("allow all file reads in this directory") or narrowly ("allow exactly this one bash command").

**Context compression**: For long-running agent sessions, Claude Code implements a rolling compression strategy for conversation history, prioritizing tool call results and recent context over earlier turns. This is a solved problem that multiple teams have independently implemented, but seeing Anthropic's specific approach provides useful competitive intelligence.

**Error recovery**: The harness includes extensive retry logic with exponential backoff for tool failures, and a "degraded mode" that continues agent operation with reduced capabilities when specific tools become unavailable — evidence of production hardening for enterprise reliability requirements.

## The Open-Source Question

In the immediate aftermath, several prominent developers publicly argued that Anthropic should simply open-source Claude Code — accepting the leak as fait accompli and turning a security incident into a community asset. The argument: the code is already public, the reputational damage from the leak is done, and open-sourcing would generate goodwill and community contributions that could improve the harness faster than Anthropic's internal team alone.

Anthropic has declined to comment on whether open-sourcing Claude Code is under consideration. The company's existing open-source footprint is limited primarily to research papers and the MCP specification; its production software has remained proprietary.

Given that the code is now effectively public regardless of Anthropic's preferences, the open-source advocates have a point that is difficult to dismiss entirely. Whether Anthropic chooses to acknowledge the reality or continue treating the code as proprietary in principle, if not in practice, will say something meaningful about how the company handles adversity in its second decade.

For now, Claude Code v2.1.89 is available on npm with the source map correctly omitted. The previous version has been unpublished. The 41,500 forks remain.
