---
title: "Anthropic Releases Claude Opus 5: Near-Frontier Intelligence at Half the Price"
summary: "Anthropic launched Claude Opus 5 on July 24, offering benchmark-beating performance—including a 43.3% score on the Frontier-Bench coding evaluation—at the same $5/$25 per-million-token price point as its predecessor. The model becomes the new default in Claude Code and Claude Max, targeting daily agentic workloads."
category: "ai-ml"
publishedAt: 2026-07-26
lang: "en"
featured: true
trending: true
sources:
  - name: "Axios"
    url: "https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5"
  - name: "ExplainX"
    url: "https://explainx.ai/blog/claude-opus-5-launch-july-2026"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-07-24/anthropic-unveils-more-cost-efficient-model-for-everyday-tasks"
tags:
  - "Anthropic"
  - "Claude"
  - "LLM"
  - "AI models"
  - "agentic AI"
relatedSlugs:
  - "2026-07-25-meta-anthropic-10b-compute-deal-en"
  - "2026-04-05-anthropic-claude-mythos-en"
---

Anthropic has released Claude Opus 5, the company's most efficient frontier-class model to date, drawing an unusually sharp reaction from developers and enterprise buyers who have been waiting to see whether the Fable 5 flagship's capabilities could be replicated at a lower cost tier. The answer, at least on several key benchmarks, appears to be yes—and in some cases, Opus 5 actually exceeds its more expensive sibling.

## A Model That Beats the Frontier at Its Own Game

The headline number is on Frontier-Bench, a coding-intensive evaluation designed to stress-test a model's ability to write, debug, and reason about software. Claude Opus 5 scored 43.3% on the benchmark, compared with Fable 5's 33.7%—a lead of nearly ten percentage points that surprised even close observers of the model race. Anthropic attributed the gap to targeted fine-tuning for agentic workflows, where the model must string together dozens of tool calls and self-corrections across a session without human guidance.

On ARC-AGI-3, a test of novel problem-solving that resists the kind of rote memorization that can inflate benchmark scores, Opus 5 posted 30.2%—roughly three times the performance of competing models at similar price points. Its computer-use score on the OSWorld benchmark hit 70.6%, a figure that points directly at the autonomous agent market: the model can control a desktop environment well enough to handle real office workflows without hand-holding.

## Pricing and Positioning

Anthropic kept the price identical to its predecessor: $5 per million input tokens and $25 per million output tokens. That matches Opus 4.8, which had been the company's workhorse for enterprise deployments, and positions Opus 5 as a transparent upgrade rather than a price increase disguised as a launch.

Fable 5, Anthropic's true frontier offering, remains the recommended choice for the hardest problems—the company describes it as targeting "the edge of what AI can do." Opus 5 is aimed at everything below that ceiling: the daily grind of knowledge work, multi-step research, document processing, and software development tasks where burning flagship compute would be economically wasteful. Anthropic expects Opus 5 to displace Fable 5 for the overwhelming majority of production workloads once teams run their own cost-performance calculations.

A Fast Mode is also available, delivering approximately 2.5 times the generation speed at twice the base cost per token. The option is intended for latency-sensitive pipelines—customer-facing chatbots, real-time coding assistants—where the extra cost is worth the reduced wait.

## Built for Agents, Designed to Be Trusted

Claude Opus 5 ships with thinking enabled by default, reflecting Anthropic's view that deliberate, chain-of-thought reasoning should be the baseline for complex tasks rather than an optional add-on. The model carries a 1 million token context window and supports up to 128,000 output tokens per generation, both specifications that favor long-horizon agentic tasks over short conversational exchanges.

What may matter more to enterprise buyers than the raw performance numbers is the alignment story. Opus 5 posted a 2.30 misalignment audit rating—the lowest of any model in the Anthropic lineup—meaning it produces fewer outputs that conflict with stated instructions or drift toward unintended behavior during extended autonomous operation. Lower variance in outputs was another deliberate design goal; in practice, this translates to more predictable behavior across repeated runs, which is critical for production deployment.

The model also reflects a calculated tradeoff on cybersecurity: Opus 5 can identify software vulnerabilities competently, but Anthropic constrained it from providing detailed exploitation guidance. The company has been explicit that this is an intentional design choice, not a capability ceiling—a signal to enterprise security teams that the model can participate in defensive workflows without becoming a force multiplier for attackers.

## Immediate Platform Integration

Opus 5 went live as the default model in Claude Code and Claude Max on the same day it launched, replacing the previous default without a grace period. The decision reflects Anthropic's confidence that the model is ready for production without a gradual rollout phase, and signals that the team views Opus 5 as a genuine quality upgrade rather than a lateral move.

For developers building on the Anthropic API, Opus 5 is accessible through the standard `claude-opus-5` model identifier. Third-party integrations—including major enterprise platforms that run Anthropic models through partnership agreements—are expected to reflect the new default within days.

## The Broader Race Context

The release comes during a month that has seen OpenAI's GPT-5.6 family and Google's Gemini 3.6 Flash both capture attention, compressing the time between frontier launches to a pace that was unthinkable two years ago. In that context, Opus 5's benchmark numbers carry a particular competitive weight: they demonstrate that the cost-performance curve in large language models is still bending sharply downward.

The more provocative implication of Opus 5's Frontier-Bench score is what it says about capability diffusion. Anthropic's most expensive model can now be outperformed on coding tasks by its mid-tier offering—a pattern that, if it holds across labs, suggests that the gap between "flagship" and "everyday" AI is narrowing faster than pricing structures have adjusted to acknowledge. For buyers who locked in enterprise contracts pegged to Fable 5 pricing, that arithmetic deserves a second look.

What Anthropic is betting on is that the right response to a narrowing capability gap is not to hold back the cheaper model, but to accelerate the frontier one. Fable 5 retains its position on the hardest novel-problem benchmarks. The goal is for the two tiers to chase each other upward—with Opus 5 covering the territory that Fable 5 already mapped, and Fable 5 pushing into the unknown ahead of it.
