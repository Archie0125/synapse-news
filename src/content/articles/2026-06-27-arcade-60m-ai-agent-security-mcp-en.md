---
title: "Arcade Raises $60M to Solve the Permission Problem That's Blocking Enterprise AI Agents"
summary: "Arcade, the startup that authored the MCP authorization spec and runs secure AI agent actions across Fortune 500 companies, has raised $60 million in Series A funding led by SYN Ventures. The round reflects growing enterprise urgency around AI agent governance — specifically, the inability to audit which agent took which action on whose behalf in production systems."
category: "startups"
publishedAt: 2026-06-27
lang: "en"
featured: false
trending: true
sources:
  - name: "BusinessWire"
    url: "https://www.businesswire.com/news/home/20260615229631/en/Arcade-Raises-$60M-to-Become-the-Secure-Action-Layer-Behind-Every-Production-AI-Agent"
  - name: "Pulse2"
    url: "https://pulse2.com/arcade-raises-60-million-series-a-to-secure-ai-agents-in-production/"
  - name: "PYMNTS"
    url: "https://www.pymnts.com/news/investment-tracker/2026/arcade-raises-60-million-to-control-ai-agents/"
tags:
  - "Arcade"
  - "AI agents"
  - "MCP"
  - "enterprise security"
  - "Series A"
  - "agent governance"
relatedSlugs:
  - "2026-06-27-anthropic-claude-tag-slack-enterprise-en"
  - "2026-06-27-deepseek-v4-pro-permanent-price-cut-en"
---

## The Question Security Teams Can't Answer

When an AI agent running on your company's infrastructure takes an action — sends an email, queries a database, submits a purchase order, modifies a configuration file — can you answer the following: which agent was it, on behalf of which user, and was that agent actually authorized to do that on that system?

For most enterprises deploying AI agents in 2026, the honest answer is no. That gap is what Arcade was built to close, and it's what just earned the company $60 million in Series A funding.

The round was led by SYN Ventures, with strategic participation from Morgan Stanley and Wipro. Combined with Arcade's $12 million seed round from 2025, the company has now raised $72 million in total, reflecting investor conviction that AI agent governance is no longer a nice-to-have — it's the prerequisite for enterprise adoption at scale.

## What Arcade Actually Does

Arcade describes itself as the "secure action layer" for production AI agents, and the framing is precise. It sits between AI models and the enterprise systems those models act on — providing three capabilities that individually feel obvious but in practice have been missing from nearly every AI agent deployment:

**Authorization**: Before an agent executes an action, Arcade verifies whether that specific agent, acting on behalf of that specific user, is permitted to perform that action on that resource. Not just a blanket capability check, but a granular, per-action, per-user, per-resource authorization decision.

**Execution**: Arcade runs the action itself, in a controlled environment, rather than allowing the agent to call enterprise APIs directly with broad credentials.

**Audit trails**: Every action is logged in a way that can be reconstructed: which model invoked it, which user triggered the workflow, what data was accessed, what was changed.

The CEO, Alex Salazar, put the core problem in characteristically direct terms: "Nobody can prove that for any given action by an agent, whether that agent on behalf of that user can perform that action on that resource. Agents don't fail in production because the model is wrong — they fail because the permissions model is wrong."

## The MCP Connection

Arcade isn't just a security wrapper; it's the organization that authored the MCP (Model Context Protocol) authorization specification, now adopted by Anthropic. MCP has become the de facto standard for how AI agents connect to tools and external systems. The authorization layer Arcade built on top of it defines how those connections are governed.

This positioning is strategically significant. By writing the spec, Arcade has made itself structurally relevant to every enterprise deploying MCP-compatible agents — which, as Anthropic's Claude and competing platforms standardize on MCP, increasingly means every major enterprise AI deployment.

The company currently maintains over 8,000 MCP tools built for enterprise agent workflows, and its platform has seen tool call volumes increase 25-fold over six months. Production deployments span a leading US bank, Prosus, and LangChain — each representing the kind of high-volume, high-stakes agent operation where a permissions failure isn't just embarrassing; it's a compliance event.

## Why This Problem Is Getting Worse Before It Gets Better

The AI agent governance challenge is a direct consequence of how quickly the underlying technology has outpaced the institutional frameworks built to manage it. In 2024 and early 2025, AI agents were largely confined to sandboxed demos and proof-of-concept deployments. By 2026, they're routing customer claims, executing trades, managing infrastructure, drafting and sending communications, and operating with access privileges that would never be granted to a single human employee acting alone.

The permission models inherited from human-centric identity and access management (IAM) systems weren't designed for agents. A human employee gets a role, a set of permissions, and accountability through organizational structure. An AI agent can be invoked by multiple users, running in parallel across thousands of concurrent workflows, with credentials that don't map cleanly to any individual person. Traditional IAM gives you a blunt instrument when you need a scalpel.

Jay Leek, a partner at SYN Ventures, articulated the investor thesis cleanly: "Adoption outruns the infrastructure that makes it safe. Agents are at that wall right now." SYN Ventures' portfolio skews toward security infrastructure in frontier technology categories, and the firm's lead on this round reflects a judgment that agent governance is the security category of the current AI cycle.

## The Enterprise Adoption Calculus

For enterprises, the security concern isn't abstract. Regulators in financial services (where several of Arcade's existing customers operate), healthcare, and critical infrastructure have made clear that AI system governance must be auditable, documentable, and reversible. "The AI did it" is not a defense in front of a bank examiner or an SEC investigator.

The practical implication: many enterprises have reached a point where AI agent deployments have been tested, validated for capability, and approved internally — only to stall at the security and compliance gate because no one can provide an answer to basic governance questions. Arcade's pitch is that it removes that blocker without requiring enterprises to build their own authorization infrastructure from scratch.

The strategic investors in this round — Morgan Stanley (a major financial institution with direct interest in AI governance tools) and Wipro (a consulting firm deeply engaged in enterprise AI deployments globally) — signal that demand for this solution is not hypothetical. Both organizations have operational skin in the game.

## What the $60M Buys

The new capital will accelerate product development, expand the MCP tool ecosystem, and grow Arcade's engineering and go-to-market teams. The company is also expanding integrations with major enterprise identity platforms — connecting Arcade's authorization layer to existing corporate SSO and IAM infrastructure, which is a prerequisite for seamless enterprise deployment.

With 25x tool call growth in six months and production deployments at globally significant financial institutions, Arcade has demonstrated that the market exists and the product works. The question the Series A answers is whether the company can scale it — from a handful of marquee design partners to the thousand-plus enterprise deployments that would make Arcade genuinely foundational to the AI agent economy.

Given that AI agent adoption shows no signs of slowing, the governance infrastructure that makes it safe to scale represents a large and largely unaddressed market. Arcade is currently the closest thing to a purpose-built solution that exists.
