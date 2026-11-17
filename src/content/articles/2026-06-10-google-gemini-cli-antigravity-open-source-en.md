---
title: "Google Took 6,000 Community Contributions, Then Closed Gemini CLI — Developers Are Furious"
summary: "Google announced on May 19 that Gemini CLI will stop serving free users, Google AI Pro and Ultra subscribers, and individual Gemini Code Assist users on June 18, and that its replacement, Antigravity CLI, is closed source. External contributors had merged more than 6,000 pull requests into the Apache 2.0 repository over nearly a year."
category: "developer-tools"
publishedAt: 2026-06-10
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: false
sources:
  - name: "The Register"
    url: "https://www.theregister.com/ai-ml/2026/05/20/bye-bye-gemini-cli-google-nudges-devs-toward-antigravity/5243605"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/317407/20260529/linux-foundation-tool-spotlighted-furious-developers-accuse-sickening-google-gemini-cli-bait-and-switch.htm"
  - name: "TechTimes (contributions)"
    url: "https://www.techtimes.com/articles/317056/20260523/google-accepted-6000-gemini-cli-contributions-then-closed-tool-enterprise-only.htm"
  - name: "AI Builder Club"
    url: "https://www.aibuilderclub.com/blog/google-kills-gemini-cli-june-18-2026"
tags:
  - "Google"
  - "Gemini CLI"
  - "Antigravity CLI"
  - "open source"
  - "developer tools"
  - "community"
  - "Linux Foundation"
  - "enterprise"
relatedSlugs:
  - "2026-06-04-google-io-2026-search-ai-agents-overhaul-en"
  - "2026-06-01-github-copilot-ai-credits-billing-change-en"
  - "2026-06-02-microsoft-build-2026-mai-coding-models-en"
---

Open-source software has a long history of companies making promises to communities, then walking them back. But even by that standard, what Google is doing with Gemini CLI has struck a nerve with unusual intensity.

On May 19, 2026, Google announced that Gemini CLI — an Apache 2.0-licensed command-line agent that it had encouraged the developer community to build and extend for nearly a year — would stop serving free users on June 18. The replacement is Antigravity CLI, a closed-source Go binary developed internally at Google. Community developers, who collectively contributed more than 6,000 merged pull requests to the Gemini CLI repository, are left holding a license that technically remains open but lacks the backend infrastructure to run it.

The GitHub announcement post received 31 thumbs-down reactions as its most prominent response. Developer @anthuanvasquez captured the community mood bluntly: "As always, Google being Google."

## What Gemini CLI Was

Gemini CLI launched roughly a year ago as Google's answer to the command-line AI agent trend. It was open-source under the Apache 2.0 license, available on GitHub, and positioned as a first-class developer tool for building multi-step workflows in the terminal. It could browse the web, execute code, manage files, and interact with the Gemini API — and importantly, it could be extended, forked, and modified by anyone.

The community responded enthusiastically. The repository accumulated more than 104,000 GitHub stars. By the time Google announced the shutdown, more than 6,000 pull requests from external contributors had been merged. By the time Google announced the shutdown, more than 6,000 pull requests had been merged, representing a substantial amount of unpaid engineering work.

## The Bait-and-Switch Mechanics

Developer @lingyaochu identified the pattern precisely in the GitHub issue thread: "open source Gemini CLI, get developers contribute to this, and then migrate the code to a close source project."

The mechanism is technically subtle. The Apache 2.0 license on the Gemini CLI repository is not being revoked. Google has stated the repository will remain publicly accessible. What is being revoked is access to the infrastructure that makes the tool functional: the authentication backend, the API quota system, and the service endpoints that Gemini CLI calls when a developer runs a command.

As journalist Christine Hall wrote, Google "effectively removes only the open source part" — the code remains visible but the tool no longer works for free users. Enterprise customers with paid Gemini Code Assist Standard or Enterprise licenses keep access to Gemini CLI, along with model updates and security patches, while free users do not.

Antigravity CLI, the replacement, is a single native binary without publicly available source code. Its GitHub repository contains documentation and configuration files but no implementation. The tool is invoked with `agy` rather than `gemini`, a change that means binary-name changes and configuration rewrites for existing shell scripts and CI pipelines built on Gemini CLI commands.

## What Antigravity Actually Offers

To be fair to Google's position: Antigravity CLI is a genuinely different tool, not just Gemini CLI rebranded. It is purpose-built for multi-agent workflows, designed around Google's Antigravity platform — an umbrella for what Google is now calling its "agent-first development" stack.

At launch, however, Antigravity CLI does not have full feature parity with Gemini CLI. Google acknowledged in its migration guide that agent skills, hooks, and subagent support are launching with partial coverage. For the subset of developers who had built sophisticated Gemini CLI workflows relying on the full extensibility of the open-source tool, the migration involves real capability loss, not just a binary swap.

The migration deadline of June 18 also gives affected developers less than a month from the announcement to rebuild pipelines on a tool that is still filling in feature gaps.

## The Linux Foundation Angle

The controversy has elevated a relatively obscure initiative from the Linux Foundation: the Model Openness Tool, accessible at isitopen.ai. The tool scores AI-related software projects across 17 components — from training data transparency to inference infrastructure to the openness of build tooling — and is explicitly designed to surface the gap between "open-source" claims and operational reality.

Gemini CLI's Apache 2.0 license would score high on code availability, but its dependence on Google's backend infrastructure would likely pull the overall system lower, which is exactly the failure mode that made the shutdown possible. The Linux Foundation's framing positions Gemini CLI's situation as a case study in why labeling something open-source does not guarantee the community access that open-source users have historically expected.

The Model Openness Tool has gained renewed attention from developers evaluating other AI CLI tools, including those distributed by Anthropic, OpenAI, and smaller AI companies. In a space where every vendor is competing for developer mindshare by touting open-source credentials, the Gemini CLI episode has made developers measurably more skeptical about the durability of those claims.

## The Broader Pattern

Google's AI developer tooling history in the current cycle has been marked by acceleration and fragmentation. The company has launched, rebranded, or deprecated significant developer-facing products at an unusual pace: Google AI Studio, the Gemini API, Gemini Code Assist, Gemini CLI, Firebase Genkit, and now Antigravity represent a string of partly overlapping initiatives, each requiring developers to make adoption decisions about tools that may not exist in their current form in 18 months.

That fragmentation has a compounding cost. Developers build workflows, CI integrations, and internal tooling on top of these products. When the underlying tool changes or disappears, those investments depreciate. The Gemini CLI situation is notable not because developer tool churn is unusual at Google — it isn't — but because this particular instance involved soliciting unpaid open-source contributions for a year before restricting access.

## What Developers Should Do Now

For developers affected by the June 18 deadline, the practical options are:

Migrate to Antigravity CLI and accept the current feature gaps, betting that Google ships full parity before those gaps block their workflows. The `agy` binary is available now and supports basic multi-agent use cases.

Move to a competing tool. Developers are evaluating Claude Code (Anthropic), the GitHub Copilot CLI, and several open-source alternatives built on locally hosted models. Claude Code in particular has comparable terminal-native agentic functionality and a paid-but-transparent pricing model.

Fork and self-host Gemini CLI using the Apache 2.0 license. The code remains accessible, and technically sophisticated teams can maintain their own fork with custom backend configuration, though this requires engineering investment that most teams cannot justify for a development tool.

For the broader AI developer community, the Gemini CLI situation is a reminder that open-source labels on infrastructure-dependent tools require scrutiny. The real question is not whether the code is visible — it is whether the backend is accessible, and on whose terms.

Google has not replied to developers' questions in the GitHub discussion thread. The June 18 date stands.

*Correction (November 15, 2026): 8 sentences were corrected or removed to match the sources listed on this page.*
