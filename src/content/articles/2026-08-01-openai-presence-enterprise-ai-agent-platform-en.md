---
title: "OpenAI Presence Brings Enterprise-Grade Governance to Production AI Agents"
summary: "OpenAI launched Presence on July 22, a managed platform that lets enterprises deploy trusted voice and chat agents connected to their own systems — CRM, ERP, databases — with built-in policy guardrails, Codex-powered continuous improvement, and automatic human escalation. The platform's own phone support line resolves 75% of inbound calls without human help."
category: "products"
publishedAt: 2026-08-01
lang: "en"
featured: false
trending: true
sources:
  - name: "OpenAI"
    url: "https://openai.com/index/introducing-openai-presence/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/orchestration/openai-unveils-presence-a-new-platform-that-lets-enterprises-launch-and-manage-realtime-voice-agents-and-chatbots"
  - name: "Help Net Security"
    url: "https://www.helpnetsecurity.com/2026/07/22/openai-presence-ai-agent-platform/"
  - name: "CX Today"
    url: "https://www.cxtoday.com/security-privacy-compliance/openai-presence-enterprise-ai-agent-governance/"
tags:
  - "OpenAI"
  - "AI agents"
  - "enterprise AI"
  - "voice AI"
  - "customer service"
  - "agentic AI"
relatedSlugs:
  - "2026-07-30-openai-chatgpt-academic-researchers-100k-program-en"
  - "2026-08-01-deepseek-v4-flash-0731-agent-benchmarks-en"
---

For the past two years, enterprise AI adoption has followed a recognizable pattern: IT teams configure an LLM API, developers build a chatbot, the chatbot gets deployed to a single workflow, and then months of manual tuning follow as the system silently fails on edge cases nobody anticipated. OpenAI has watched this play out across hundreds of deployments, and its new product is a direct response to what it saw.

Presence, which launched in limited general availability on July 22, 2026, is OpenAI's attempt to operationalize the full lifecycle of production AI agents — from initial deployment to governance, continuous evaluation, and improvement — inside a single managed platform purpose-built for enterprise environments.

## What Presence Actually Does

The core problem Presence addresses is the gap between an AI demo and an AI deployment. A prototype agent powered by a frontier model can appear to handle almost any customer query in a controlled setting. A production agent that runs millions of conversations per day — some about billing disputes, some about regulatory claims, some from users actively trying to manipulate the system — needs a fundamentally different operational layer around it.

Presence wraps model reasoning in four interconnected components:

**Knowledge and access control.** Enterprise customers connect Presence to their internal systems — CRM platforms, ERP databases, customer service records — with granular policies governing exactly what each agent can see, what it can do, and under what conditions it is authorized to take action. An agent might have read access to a customer's account history but require human approval before processing a refund above a certain threshold.

**Simulation and pre-deployment testing.** Before any agent goes live, Presence runs it through a battery of synthetic scenarios that model real-world edge cases, including adversarial inputs designed to probe guardrail failures. Teams can review how the agent handles difficult conversations without risking live customer interactions.

**Production monitoring and evaluation.** Once deployed, every agent interaction is logged and evaluated. Presence surfaces patterns — categories of questions the agent handles poorly, escalation triggers that fire too frequently or not enough, sentiment signals from customers who remained unsatisfied after an interaction.

**Codex-powered improvement loop.** The platform uses Codex to analyze interaction logs and propose behavioral updates: revised instructions, modified escalation thresholds, new example conversations to reinforce desired behavior. A human review step gates every proposed change before it goes live, which OpenAI describes as the system's most important safety mechanism.

## The 75% Resolution Number

OpenAI chose its own phone support line as the first production deployment of Presence. The company says the system now resolves 75% of all inbound support calls without involving a human agent — a figure that would represent a significant operational improvement for any company running at scale. The claim is marketing, and independent audits of it don't exist, but the willingness to run Presence on its own support infrastructure before selling it to customers is a meaningful signal about the company's confidence in the product's reliability.

The support line handles ChatGPT and API account questions, billing issues, and feature troubleshooting. Calls that involve account security, payment disputes above a threshold, or explicit user requests to speak to a person are escalated immediately.

## Deployment Model: Managed, Not Self-Service

Presence is not a drag-and-drop platform. OpenAI has deliberately kept the product outside self-service reach, at least in this initial phase. Every deployment is led by OpenAI's Forward Deployed Engineers, who work directly alongside the customer team to select workflows, connect internal systems, establish permissions, configure policies, run pre-deployment simulations, and move the agent into production.

This white-glove approach limits how many customers Presence can serve simultaneously — by definition, it cannot scale the way a cloud API does. OpenAI hasn't disclosed its roster of early enterprise customers beyond confirming early testing in customer support, banking, telecom, and insurance use cases. Pricing details are similarly undisclosed, with the company promising broader pricing and availability information as the limited rollout expands.

The model mirrors how Salesforce and Workday expanded into enterprise software in the 2000s: start with high-touch deployments where you can control quality, learn from every integration, and gradually build the self-service tooling that scales once you understand the failure modes.

## Why This Release Matters

Presence is the clearest signal yet that OpenAI is executing a deliberate shift from being a model API provider to being an enterprise AI vendor with a full platform play. The company has watched competitors — Salesforce Agentforce, ServiceNow AI, Microsoft Copilot — build agent governance layers on top of OpenAI's own models. Presence brings that governance layer in-house.

From an enterprise buyer's perspective, the product addresses the two objections that have slowed production AI agent deployments most consistently: liability (who is responsible when the agent does the wrong thing?) and auditability (can we prove to regulators what our agent did and why?). Presence answers both questions with its policy and logging architecture, even if the answers are still relatively early-stage.

The timing also matters competitively. Anthropic launched its enterprise agent operator tools in Q1 2026, and Google's Gemini Enterprise Agent Platform has been in limited availability since I/O. OpenAI moving Presence into limited GA consolidates a three-way platform race among the frontier labs — all of which are betting that enterprise agent governance, not just raw model quality, is where the durable revenue sits.

## What's Still Missing

A few important questions remain unanswered as Presence enters the market. The platform's behavior when a Codex-proposed improvement changes agent behavior in ways that weren't anticipated — and what liability framework applies when it does — is not documented. The pricing model has been kept opaque, which makes it difficult for prospective customers to build cost models. And the absence of self-service tooling means smaller companies or teams with existing AI engineering capacity are effectively excluded from this initial release.

OpenAI has indicated that a broader self-service tier is in development, expected sometime in early 2027. Until then, Presence is a product for large enterprises willing to work closely with an OpenAI team — which, given the complexity of production agent deployments, may be exactly the right first market.
