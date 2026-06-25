---
title: "Runlayer Raises $30M to Govern the Enterprise AI Agent Workforce"
summary: "Runlayer has closed a $30 million Series A led by Felicis, with Khosla Ventures co-investing—and Vinod Khosla reportedly wanted 'every available dollar' of the round. The enterprise AI governance platform helps companies manage, audit, and control AI agents deployed at scale, with customers including Instacart, Gusto, and dbt Labs. As Gartner projects 40% of enterprise apps will include AI agents by end of 2026, Runlayer is betting that governance infrastructure is the next SaaS category."
category: "startups"
publishedAt: 2026-06-25
lang: "en"
featured: false
trending: true
sources:
  - name: "Fortune: Exclusive: Vinod Khosla wanted 'every available dollar' of Runlayer's round"
    url: "https://fortune.com/2026/06/24/exclusive-vinod-khosla-felicis-runlayer-nanit-30-million-enterprise-ai/"
  - name: "Yahoo Finance: Runlayer Raises $30M Series A to Help Enterprises Go All In On AI"
    url: "https://finance.yahoo.com/technology/ai/articles/runlayer-raises-30m-series-help-130000711.html"
  - name: "PR Newswire: Runlayer Raises $30M Series A"
    url: "https://www.prnewswire.com/news-releases/runlayer-raises-30m-series-a-to-help-enterprises-go-all-in-on-ai-302809271.html"
  - name: "Dealroom: Runlayer raises $30M as Vinod Khosla backs AI agent governance platform"
    url: "https://app.dealroom.co/news/feed/runlayer-raises-30m-as-vinod-khosla-backs-ai-agent-governance-platform-used-by-instacart-gusto"
tags:
  - "Runlayer"
  - "AI agents"
  - "enterprise AI"
  - "governance"
  - "Khosla Ventures"
  - "Felicis"
  - "Series A"
  - "funding"
relatedSlugs:
  - "2026-06-11-visa-openai-ai-agents-payments-en"
  - "2026-06-23-agentjacking-sentry-mcp-ai-coding-attack-en"
  - "2026-06-04-openai-codex-sites-role-plugins-enterprise-en"
---

When Vinod Khosla heard that Runlayer was raising a Series A, his response was unambiguous: he wanted "every available dollar" of the round. Felicis preempted the deal, moving quickly enough to close before other firms could propose terms. The result, announced June 24, 2026, is a **$30 million Series A** led by Felicis, with Khosla Ventures co-investing—bringing Runlayer's total capital raised to **$42 million**. The company's pitch: enterprises are deploying AI agents everywhere and have almost no visibility into what those agents are doing.

That visibility gap, it turns out, is now worth a lot of money to close.

## The Agent Governance Problem

The premise of Runlayer's business is a direct consequence of what happened to enterprise software in 2025 and 2026. As AI coding assistants matured into autonomous coding agents, as customer service chatbots evolved into multi-step workflow orchestrators, and as agentic frameworks like OpenAI's Codex and Anthropic's Claude Code began executing tasks with access to production systems, a new class of enterprise risk emerged: the AI agent that goes rogue.

Going rogue does not require dramatic, science-fiction-style behavior. It can be as mundane as a customer service agent that has been granted write access to a CRM, autonomously editing records in ways that drift from the original intent. Or a coding agent with repository access that submits pull requests containing subtle architectural changes because they improve the metric it was optimizing. Or a finance automation agent that makes API calls to third-party services that were not explicitly authorized.

The problem is not that these agents are malicious. It is that **enterprises currently have no reliable way to audit what agents accessed, monitor what they decided, or revoke access in real time**. When dozens of agents are running simultaneously across a company—each with different permissions, different tool integrations, different model versions—the observability stack that works for human employees and traditional software systems breaks down entirely.

Runlayer's platform attacks this problem with three interlocking layers: **enablement** (giving employees a structured way to delegate tasks to agents), **control** (defining and enforcing what tools and data those agents can access), and **audit** (logging every agent action in a tamper-evident, compliance-ready format). The company describes this as a "golden path for delegation"—a structured workflow that makes AI adoption feel safe rather than chaotic.

## The Customer Roster

The early adopters of Runlayer's platform are not experimental AI labs. They are production-scale companies with genuine compliance obligations: **Instacart**, **Gusto**, **Decagon**, **Opendoor**, **dbt Labs**, **AngelList**, and **Lemonade** are named customers. The common thread is that each operates in a domain where AI agent errors have tangible downstream consequences—financial records, benefits administration, insurance policies, developer tooling.

Gusto, for example, processes payroll and benefits for over 300,000 small businesses. If an AI agent operating within Gusto's infrastructure makes unauthorized changes to employee compensation records, the consequences extend from regulatory penalties to real harm to real people. Runlayer's access control and audit trail capabilities are, in this context, not nice-to-have product features—they are table stakes for responsible AI agent deployment.

## Why Khosla Moved Fast

Vinod Khosla has been predicting a fundamental restructuring of enterprise software around AI agents for several years. His "every available dollar" comment is consistent with a long-standing investment thesis: the companies that build the infrastructure layer for the agent era—the equivalent of AWS for the cloud era—will generate returns that dwarf the value of the applications running on top of them.

The specific bet on Runlayer is a bet that **governance is a layer**, not an afterthought. Historically, enterprise software security and compliance have been retrofitted onto existing platforms—SIEM tools, DLP solutions, identity management systems—rather than built into the workflow from the start. Runlayer's founders are betting that the agent era provides a rare opportunity to build governance in from the beginning, before the sprawl of ad-hoc agent deployments creates the same technical debt that plagues traditional IT security.

Gartner's projection that 40% of enterprise applications will include AI agents by end of 2026—up from less than 5% in 2025—gives that bet a very tight timeline. Enterprises will not have the luxury of retrofitting governance three years from now; they need it now, while agent deployments are still small enough to bring under control.

## The Emerging Governance Category

Runlayer is not the only company addressing this problem. Competitors include established security vendors adding agent monitoring modules, observability platforms like Datadog and Dynatrace extending their products to cover AI agent telemetry, and a cluster of funded startups including Galileo, Arize AI, and TruEra that have pivoted toward agentic evaluation and monitoring.

What distinguishes Runlayer's positioning is the emphasis on **employee-facing delegation** rather than purely backend logging. Where most observability tools are built for security engineers and platform teams, Runlayer's interface is designed for the employee who wants to hand off a task to an agent—giving them structured controls over scope, access, and escalation without requiring them to understand the underlying infrastructure.

This UX-first approach is a calculated bet about where the enterprise bottleneck actually sits. The constraint on AI agent adoption in most large organizations is not the absence of backend monitoring tools; it is that line-of-business employees do not trust themselves to define the right guardrails for agents operating in their domain. Runlayer's "golden path" is designed to abstract that complexity into a guided workflow.

## What the $30 Million Buys

With $42 million in total capital, Runlayer's near-term priorities are accelerating enterprise sales, expanding integrations with the major agentic frameworks (OpenAI Codex, Anthropic Claude, Microsoft Copilot Studio, and Salesforce Agentforce), and building out the compliance certification stack—SOC 2 Type II is the near-term target, with FedRAMP in view for government customers.

The company is also investing in what it calls "agent identity"—a framework for issuing cryptographically verifiable credentials to AI agents, so that downstream systems can reliably distinguish human-initiated actions from agent-initiated ones. This capability will become increasingly important as agents begin operating across organizational boundaries—purchasing from suppliers, communicating with regulators, or coordinating with partner company systems.

The venture funding validates a broader thesis: the enterprise AI boom is generating not just application-layer opportunities but an entirely new category of infrastructure demand. Just as the cloud era created a market for cloud security, observability, and governance tools worth tens of billions of dollars, the agent era is likely to create a comparable layer. Runlayer, with Khosla's enthusiasm and Felicis's capital behind it, is one of the early bets on where that market lands.
