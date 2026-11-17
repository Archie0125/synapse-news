---
title: "Anthropic Launches Claude Opus 4.8 With Dynamic Workflows and Hints at Mythos-Class Models"
summary: "Anthropic released Claude Opus 4.8 on May 28, bringing improved benchmark results, a fast mode that is three times cheaper, and a research-preview feature called Dynamic Workflows that lets Claude run hundreds of parallel subagents in a single Claude Code session. The company also said it plans to release a new class of model with even higher intelligence than Opus."
category: "ai-ml"
publishedAt: 2026-05-29
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: true
trending: true
sources:
  - name: "Anthropic News"
    url: "https://www.anthropic.com/news/claude-opus-4-8"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/anthropics-claude-opus-4-8-is-here-with-3x-cheaper-fast-mode-and-near-mythos-level-alignment"
  - name: "Gizmodo"
    url: "https://gizmodo.com/anthropic-debuts-claude-opus-4-8-teases-upcoming-launch-of-mythos-class-models-2000764742"
  - name: "GitHub Changelog"
    url: "https://github.blog/changelog/2026-05-28-claude-opus-4-8-is-generally-available-for-github-copilot/"
  - name: "Simon Willison's Blog"
    url: "https://simonwillison.net/2026/May/28/claude-opus-4-8/"
tags:
  - "anthropic"
  - "claude"
  - "opus"
  - "ai-models"
  - "agentic-ai"
  - "developer-tools"
  - "llm"
relatedSlugs:
  - "2026-05-27-anthropic-2026-agentic-coding-trends-report-en"
  - "2026-05-17-code-with-claude-2026-managed-agents-en"
---

Anthropic shipped Claude Opus 4.8 on May 28, and Anthropic itself describes it as a modest but tangible improvement on Opus 4.7, with gains in benchmarks, a cheaper fast mode and, notably, more honesty about its own limitations. Paired with a teaser for upcoming "Mythos-class" models and a new Claude Code feature called Dynamic Workflows, this release points to larger models still to come.

## The Numbers: Real But Measured Progress

Anthropic published benchmark comparisons between Opus 4.7 and Opus 4.8 across three core dimensions. Agentic coding score — the metric most relevant to developers using Claude Code — climbed from 64.3% to 69.2%, a roughly 7.6% relative improvement that places Opus 4.8 ahead of GPT-5.5 Instant on long-horizon coding tasks according to third-party evaluations. Multidisciplinary reasoning with tools rose from 54.7% to 57.9%, and a composite knowledge-work score improved from 1,753 to 1,890.

Simon Willison highlighted Anthropic's own description of the release as "a modest but tangible improvement" on its predecessor, and said it was refreshing to see a lab describe a release so honestly. The model does not leap over the frontier; it presses against it with notably more reliability than its predecessor, particularly in scenarios requiring extended autonomous operation without human check-ins.

Pricing is unchanged from Opus 4.7: $5 per million input tokens and $25 per million output tokens. Prompt caching delivers up to 90% savings, and batch processing cuts costs by 50%. Those numbers put Opus 4.8 in the same pricing tier as GPT-5.5 on a per-token basis, which is a reasonable competitive position given the model's advantage on agentic benchmarks.

## Fast Mode Gets Three Times Cheaper

The headline number for many production users will be the cost reduction for fast mode, which lets Claude Opus operate at 2.5x its baseline output speed. Fast mode for Opus 4.8 is three times cheaper than it was for previous models, according to Anthropic, though Willison notes it is only available to organizations in the research preview.

Fast mode was initially introduced as a tool for scenarios that prioritize throughput over precision. Even so, fast mode is priced at $10 per million input tokens and $50 per million output tokens, twice the regular rate.

## Dynamic Workflows: Parallel Agents at Scale

The most technically significant announcement is Dynamic Workflows, currently in research preview inside Claude Code. The feature lets Claude approach a large task by first generating a structured plan, then spawning hundreds of parallel subagents that each execute a portion of that plan simultaneously, and finally verifying and integrating the outputs before returning results to the user.

The practical implication is a step-change in the scale of work Claude can address in a single session. Previous Claude Code sessions were constrained by sequential context — Claude could pursue only one thread of work at a time, making large-scale codebase refactors, comprehensive test-suite generation, or multi-repository migrations slow enough that developers routinely broke them into manual subtasks.

Dynamic Workflows reframes Claude Code as an orchestrator rather than a sequential executor. Anthropic describes it as giving Claude the ability to "plan work, run hundreds of parallel subagents within a single session, and verify outputs before returning results." That architecture maps closely to what external multi-agent frameworks like LangGraph and AutoGen have been attempting through scaffolding — except Dynamic Workflows bakes the orchestration directly into the model's operational loop, with Anthropic's safety and alignment constraints applied at every agent boundary.

The feature is available in research preview in Claude Code for Enterprise, Team, and Max plans. But the architectural direction is clear: Anthropic is positioning Claude Code as a direct competitor to specialized multi-agent frameworks, not merely a first-party interface for those frameworks.

## Honesty as a Measurable Property

One of the more substantive claims Anthropic makes for Opus 4.8 is improved honesty, including flagging uncertainties about its work." Earlier Opus models, like most frontier LLMs, tended toward confident assertions even when the underlying evidence was thin — a behavior that creates real problems in production agentic systems where a false assumption early in a multi-step task can cascade into expensive errors.

Anthropic says Opus 4.8 is measurably more likely to flag when it lacks sufficient information to proceed and less likely to generate unsupported claims dressed as conclusions. This is a calibration improvement rather than a capability leap, but for enterprise users deploying Claude in high-stakes domains — legal, financial, medical, defense — calibration matters as much as raw benchmark performance.

## Mythos-Class: The Next Tier Is Coming

The announcement also pointed to "Mythos-class" models, a new class of model with even higher intelligence than Opus. Anthropic said it expects to bring Mythos-class models to all its customers in the coming weeks, and noted that Opus 4.8's rates of misaligned behavior are similar to those of its best-aligned model, Claude Mythos Preview.

The codename echoes a broader trend in frontier AI: OpenAI's o-series, Google DeepMind's Gemini 3.x stack, and now Anthropic's Mythos framing all suggest labs are thinking in generational leaps rather than version increments. The explicit alignment framing hints the differentiation will rest partly on safety properties rather than raw capability alone — a competitive angle that resonates with Anthropic's core brand positioning.

## Distribution: GitHub Copilot Opens the Door

Claude Opus 4.8 is now available as a selectable model within GitHub Copilot for Copilot Pro+, Business, and Enterprise users, with a gradual rollout. Developers can route complex agentic tasks to Opus 4.8 while retaining smaller, faster models for routine code completion.

Making Opus 4.8 natively accessible inside the developer's primary working environment — no context switch required — gives Anthropic a distribution vector that directly contests OpenAI's historical home-field advantage within the Microsoft-GitHub ecosystem.

## The Competitive Moment

Claude Opus 4.8 arrives as OpenAI ships GPT-5.5 Instant as ChatGPT's new default, Google's Gemini 3.5 Flash aggressively targets speed and multimodal capability, and DeepSeek V4 Pro's permanent price cut resets cost expectations market-wide. Anthropic's strategy with Opus 4.8 is legible: hold the premium position on alignment and agentic reliability while closing the cost gap that previously made Opus-tier models inaccessible for latency-sensitive workloads.

The Mythos tease is the more significant signal. If Anthropic delivers Mythos-class models to all customers in the coming weeks as it says it expects to, the competitive picture could shift. For enterprise customers evaluating multi-year AI platform commitments, that signal is worth monitoring closely.

---

*Claude Opus 4.8 is available today via the Anthropic API and Claude Code. Dynamic Workflows is in research preview for Claude Code users. Pricing is unchanged from Opus 4.7.*

*Correction (November 15, 2026): 12 sentences were corrected or removed to match the sources listed on this page.*
