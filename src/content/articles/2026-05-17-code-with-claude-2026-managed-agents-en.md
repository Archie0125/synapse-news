---
title: "Code with Claude 2026: Anthropic Ships Self-Improving Agents with Dreaming, Outcomes, and Parallel Orchestration"
summary: "At its developer conference in San Francisco on May 6, Anthropic announced three new capabilities for Claude Managed Agents: Dreaming (a research preview that reviews past sessions to help agents improve), Outcomes (a rubric-based loop with a separate grader, in public beta), and Multiagent Orchestration (a lead agent that delegates work to specialist subagents, in public beta)."
category: "developer-tools"
publishedAt: 2026-05-17
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: false
sources:
  - name: "Claude Blog — New in Claude Managed Agents"
    url: "https://claude.com/blog/new-in-claude-managed-agents"
  - name: "SD Times — Claude Managed Agents: dreaming, outcomes, and multiagent orchestration"
    url: "https://sdtimes.com/ai/new-in-claude-managed-agents-dreaming-outcomes-and-multiagent-orchestration/"
  - name: "Simon Willison — Live blog: Code w/ Claude 2026"
    url: "https://simonwillison.net/2026/May/6/code-w-claude-2026/"
  - name: "MindStudio — Code with Claude 2026: 5 New Agent Features"
    url: "https://www.mindstudio.ai/blog/code-with-claude-2026-new-agent-features"
  - name: "Anthropic Code with Claude 2026 Developer Conference"
    url: "https://techfastforward.com/articles/anthropic-code-with-claude-developer-conference-sf-london-tokyo-2026"
tags:
  - "Anthropic"
  - "Claude"
  - "AI agents"
  - "developer tools"
  - "multiagent"
  - "Code with Claude"
  - "agentic AI"
relatedSlugs:
  - "2026-05-15-anthropic-agent-sdk-billing-split-en"
  - "2026-05-13-red-hat-summit-agentic-ai-developer-tools-en"
---

There was no new flagship model at Code with Claude 2026. That was deliberate. When Anthropic held its second annual developer conference at the Moscone Center in San Francisco on May 6 — the first stop in a three-city tour that continues in London on May 19 and Tokyo on June 10 — the company made a calculated choice to spend its stage time on infrastructure, not benchmarks. The bet Anthropic is making with this year's conference is that the era of capability demonstrations has passed, and the era of agentic reliability has arrived.

The three features Anthropic shipped that day — Dreaming, Outcomes, and Multiagent Orchestration — are the clearest articulation yet of where the company believes the competitive frontier lies in the second half of 2026.

## Dreaming: Memory That Gets Smarter Over Time

The most conceptually novel of the three is Dreaming, currently in research preview. The core insight is simple but its implications are broad: AI agents, as currently deployed, do not get better between sessions. Every conversation starts fresh, and patterns learned in session 100 are not available in session 101 unless explicitly surfaced through prompt engineering or retrieval augmentation. Dreaming is Anthropic's answer to this limitation.

The mechanism is non-destructive by design. A "dream" is a scheduled process that reads an existing memory store alongside a batch of past session transcripts, then produces a new, reorganized memory store. Duplicates are merged, stale entries replaced, and newly surfaced patterns indexed. Dreaming can update memory automatically, or developers can review changes before they land. This preserves developer control while enabling a form of autonomous self-improvement that has been a long-standing goal in the agent research community.

Dreaming extends memory by reviewing past sessions to find patterns, which is especially useful for long-running work and multiagent orchestration.

## Outcomes: The Agent That Grades Its Own Work

Outcomes, now in public beta, addresses a different failure mode: agents that complete tasks but complete them incorrectly, without the self-awareness to recognize the gap between output and intent.

The feature implements a self-grading loop using a separate evaluator agent. After the primary agent completes a task, the evaluator scores the output against a developer-written rubric and returns a structured critique: what was right, what was wrong, and what should be fixed. The primary agent then revises its output accordingly. The loop can run multiple times until the evaluator's score crosses a threshold, or until a configured iteration limit is reached to prevent runaway compute consumption.

Per Anthropic's internal benchmarks, Outcomes improved file generation quality, with +8.4% task success on docx and +10.1% on pptx. More meaningfully, early beta customers report that Outcomes significantly reduces the rate of "silent failures" — tasks where an agent appears to have succeeded but produces output that fails downstream quality checks. Harvey, the AI legal research firm, cited a 6x jump in task completion rates as the single most compelling external validation of the feature's impact.

## Multiagent Orchestration: Parallel Intelligence

The third feature addresses the sequential processing bottleneck that has constrained enterprise deployment of complex agentic workflows. Multiagent Orchestration, also in public beta, provides a native coordinator agent that can decompose a complex task into subtasks and fan them out to specialist subagents running in parallel.

The orchestrator handles task decomposition, context distribution to subagents, result aggregation, and conflict resolution when subagents produce outputs that need to be reconciled. From a developer perspective, the key advantage is that parallel orchestration can reduce wall-clock completion time for compound tasks dramatically — a research-and-synthesis workflow that previously took 40 minutes running sequentially might complete in 8 to 12 minutes with parallel subagents, depending on the task structure.

Anthropic also shipped Claude Finance, a package of 10 predefined agents for financial services workflows, the day before the main event.

## Infrastructure: The Unsexy Story That Matters

Behind the product features, Anthropic announced operational changes that matter for developers who have been hitting rate limits in production deployments. The company announced increased rate limits for developers on Claude Code and the API, including a doubling of the Claude Code five-hour limit for Pro, Max and Enterprise customers.

Anthropic also announced a partnership with SpaceX to use all of the capacity of the Colossus data center. The deal gives Anthropic access to a scale of compute that had previously been accessible only to the largest hyperscalers.

## The Platform Bet

Reading the Code with Claude 2026 announcements in aggregate, the strategic message is clear. Anthropic is positioning Claude Managed Agents not as a model API with agent features bolted on, but as a purpose-built platform for production agentic workflows. The billing separation announced last week — moving Agent SDK usage to a separate credit pool starting June 15 — is part of the same framing: agent infrastructure deserves its own economic model, separate from interactive chat usage.

The conference's expansion to London and Tokyo is also telling. London represents enterprise legal, finance, and professional services — the sectors where Harvey's 6x improvement story lands hardest. Tokyo represents the Japanese enterprise market, where AI adoption is at an earlier stage and which has distinct regulatory and language requirements.

The company that spent three years telling the industry that safety and capability were not in conflict is now making a second argument: that agents built on reliable, self-improving infrastructure will outperform agents built on raw benchmark performance. For developers who have spent 2025 dealing with the operational costs of unreliable agents, the Code with Claude 2026 lineup is the most direct address of those pain points that any major AI lab has offered.

*Correction (November 15, 2026): 8 sentences were corrected or removed to match the sources listed on this page.*
