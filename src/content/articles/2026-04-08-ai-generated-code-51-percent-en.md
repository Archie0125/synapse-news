---
title: "JetBrains Survey: Over Half of All GitHub Code Is Now AI-Generated"
summary: "A JetBrains survey of 10,000+ developers finds that 51% of code committed to GitHub is now AI-generated or substantially AI-assisted, with the AI coding tools market hitting $12.8B. GitHub Copilot retains the widest adoption but satisfaction growth has stalled, while Claude Code has surged to lead all tools on satisfaction metrics with 91% CSAT."
category: "developer-tools"
publishedAt: 2026-04-08T09:00:00Z
lang: "en"
featured: false
trending: false
sources:
  - name: "JetBrains AI Pulse 2026"
    url: "https://www.jetbrains.com/lp/devecosystem-2026/"
  - name: "GitHub Octoverse 2026"
    url: "https://octoverse.github.com/"
tags:
  - "ai-coding"
  - "github-copilot"
  - "claude-code"
  - "developer-survey"
  - "jetbrains"
  - "ai-tools"
  - "software-development"
relatedSlugs:
  - "2026-04-04-cursor-devin-war-en"
  - "2026-04-04-mcp-protocol-explosion-en"
---

For the first time in recorded software history, more than half of the code landing in GitHub repositories is written by machines. JetBrains' April 2026 AI Pulse survey — based on responses from 10,272 professional developers across 183 countries, collected in January 2026 — puts the share of AI-generated or substantially AI-assisted commits at **51.3%**, a figure that has more than doubled from 24% in the same survey eighteen months ago.

The survey defines "AI-generated" broadly: code where an AI tool produced the initial draft, even if the developer subsequently edited it. The "substantially AI-assisted" category includes code where AI autocompletion, inline suggestions, or chat-based refactoring contributed more than 50% of the keystrokes. Taken together, the 51.3% figure represents a genuine inflection point — a majority of the world's professional software output now passes through an AI system before it reaches version control.

## The Market Behind the Number

The AI coding tools market has reached $12.8 billion in annual contract value, up from $5.1 billion in 2024 and roughly $1.2 billion in 2022, when GitHub Copilot first hit general availability. JetBrains projects the market will reach $28 billion by 2028, driven primarily by enterprise seat expansion and the maturation of agentic coding workflows that go beyond single-file autocompletion.

This growth has not been evenly distributed. The survey reveals a market in the middle of a significant reshuffling, with the legacy leader facing saturation while newer entrants capture disproportionate satisfaction and mindshare.

## GitHub Copilot: Wide But Flat

GitHub Copilot remains the most widely recognized AI coding tool: **76% awareness** among professional developers, and **29% workplace adoption** — meaning nearly three in ten professional developers now use Copilot in their day-to-day work, enabled and paid for by their employers. These are remarkable numbers for any software tool category.

But Copilot's growth trajectory has flattened. Awareness grew only 3 percentage points year-over-year (from 73%), and workplace adoption is up just 4 points (from 25%). Net Promoter Score has declined from 38 to 31. The most cited friction point is context window limitations: developers working in large codebases report that Copilot struggles to maintain coherent understanding across files and modules, resulting in suggestions that are locally syntactically correct but semantically wrong in the broader project context.

Microsoft has responded by integrating Copilot more deeply into Visual Studio Code's extension ecosystem and launching Copilot Workspace, an agentic feature that attempts multi-file reasoning. But developer sentiment suggests these updates have not yet moved the needle on core satisfaction.

## Claude Code's Rapid Rise

The most striking data point in the survey is Claude Code's trajectory. Anthropic's CLI-based AI coding agent has surged from **31% awareness** in mid-2025 to **57% awareness** in January 2026 — a 26-point gain in roughly six months. Workplace adoption has reached **18%**, making Claude Code the third most widely adopted AI coding tool behind Copilot and Cursor.

More significantly, Claude Code leads all tools on satisfaction metrics: **91% CSAT** (customer satisfaction score) and an **NPS of 54** — more than 20 points above Copilot's 31 and 15 points above Cursor's 39. The gap is consistent across role types (frontend, backend, full-stack, DevOps) and company sizes (under 50 to over 1,000 employees).

Developers cite several reasons for high Claude Code satisfaction. First, its extended context window and strong performance on multi-file tasks — the exact area where Copilot users report the most friction. Second, Claude Code's CLI architecture means it integrates into existing terminal workflows without requiring IDE-specific plugins. Third, the tool's ability to reason about and execute multi-step agentic tasks — running tests, reading error output, proposing fixes, and iterating — resonates strongly with developers who have outgrown simple autocomplete workflows.

The survey data suggests Claude Code's user base skews toward senior engineers and staff-level developers, who tend to work on larger, more complex codebases where the limitations of simpler autocomplete tools are most apparent.

## Cursor's Niche Dominance

Cursor occupies a distinct position: **48% awareness**, **22% workplace adoption** (edging out Claude Code in raw adoption numbers), and an NPS of 39. Cursor's strength is concentrated among individual contributors and small-team startups, where its VS Code-based experience and aggressive free tier drive strong organic adoption.

The survey data suggests Cursor and Claude Code serve somewhat different use cases. Cursor users are more likely to be working on consumer products and web applications. Claude Code users skew toward infrastructure, backend systems, and large enterprise codebases. This market segmentation may explain why both tools can show strong growth simultaneously without directly cannibalizing each other.

## The Agentic Turn

Beyond the tool-by-tool breakdown, the survey identifies a structural shift in how developers are using AI coding assistance. In 2024, the dominant pattern was **autocomplete** — AI providing suggestions as developers typed, accepted or rejected line by line. In 2026, a growing segment of developers (34% of survey respondents) report regularly using AI in **agentic mode**: giving the AI a task description, letting it execute across multiple files and steps, then reviewing the result.

The agentic pattern dramatically increases the leverage of AI tools on output volume but also raises new quality concerns. Survey respondents who use agentic workflows report higher overall productivity gains (median self-reported estimate: 3.8x on routine tasks) but also higher rates of subtle bugs introduced by AI that required significant debugging effort to resolve (62% report at least one agentic-mode bug in the past month that took more than 30 minutes to diagnose).

This is the core tension in the 51% figure: AI-generated code is now the majority of commits, but code review practices, testing cultures, and quality assurance workflows have not yet fully adapted to a world where the primary author is non-human. Senior developers interviewed in the qualitative portion of the survey consistently raised this point.

"The problem isn't that AI writes bad code. It writes plausible code," said one staff engineer at a fintech firm. "Plausible code that compiles and passes unit tests but fails in edge cases under production load is much harder to catch than obviously wrong code."

## What This Means for Software Teams

The survey's implications for engineering teams are significant. Hiring patterns are already shifting: JetBrains found that companies using AI tools extensively are hiring 23% fewer junior engineers relative to senior engineers compared to companies with low AI tool adoption. The hypothesis is that AI is handling a large portion of the work previously done by junior developers, compressing the traditional hiring pyramid.

Code review workloads are also changing. With more than half of commits AI-generated, reviewers are increasingly focused on architectural and semantic correctness rather than syntactic style — a shift that demands more experienced reviewers but potentially fewer of them. Several of the larger companies in the survey have begun piloting AI-assisted code review tools that specifically flag likely AI-generation artifacts.

The 51% threshold is likely to be a waypoint rather than a ceiling. JetBrains' own modeling suggests the figure will reach 70-75% by the end of 2027 as agentic workflows mature and more developers shift from AI-assisted to AI-directed development. At that point, the question of how to structure software teams, evaluate engineering performance, and define "programming skill" will require more fundamental rethinking than any single tool update can provide.

For now, the majority-AI-generated codebase is a reality that engineering leaders are managing in real time — with tools, processes, and mental models that were built for a different era.
