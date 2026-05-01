---
title: "Web Pages Are Hijacking AI Agents: Google Warns of 32% Surge in Prompt Injection Attacks"
summary: "Google security researchers scanning billions of public web pages have documented a 32% rise in indirect prompt injection attacks between November 2025 and February 2026. Hidden instructions embedded in ordinary HTML are silently commandeering enterprise AI agents — in some cases to execute PayPal transactions worth thousands of dollars. The findings expose a fundamental security gap that no existing legal framework yet governs."
category: "ai-ml"
publishedAt: 2026-05-01
lang: "en"
featured: false
trending: true
sources:
  - name: "Google Security Blog"
    url: "https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html"
  - name: "Help Net Security"
    url: "https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/"
  - name: "SecurityWeek"
    url: "https://www.securityweek.com/malicious-ai-prompt-injection-attacks-increasing-but-sophistication-still-low-google/"
  - name: "Decrypt"
    url: "https://decrypt.co/365677/google-prompt-injection-ai-agents-paypal-enterprise"
tags:
  - "prompt injection"
  - "AI security"
  - "AI agents"
  - "Google"
  - "cybersecurity"
  - "LLM"
relatedSlugs:
  - "2026-04-15-openai-gpt54-cyber-model-en"
  - "2026-04-12-anthropic-mythos-cybersecurity-model-en"
---

For years, indirect prompt injection was a theoretical concern — a clever attack class that researchers demonstrated in lab environments but rarely encountered in the wild. Google's latest security research ends that comfortable assumption. The company's security team has been sweeping the public web at scale, scanning two to three billion pages per month, and what they found is an arms race already in progress.

Between November 2025 and February 2026, Google recorded a 32 percent relative increase in malicious indirect prompt injection patterns embedded in public web pages. The attacks are not sophisticated. Many are crude. But their prevalence is growing, and the targets are no longer just users — they are the AI agents that enterprises have deployed to browse the web on their behalf.

## What Indirect Prompt Injection Actually Is

A standard prompt injection attack manipulates an AI system by inserting malicious instructions directly into a user-controlled input field. Indirect prompt injection is subtler: the attacker does not need access to the user or the interface. Instead, they plant instructions inside content that an AI agent will eventually read — a webpage, a document, a product listing.

When the agent scrapes that page for information, it ingests the hidden instructions alongside the legitimate content. The model cannot reliably distinguish between the two. It processes the malicious commands as if they came from a trusted principal and executes them accordingly.

The attack surface is enormous. Every webpage an AI agent visits is a potential injection point. Every document an AI assistant opens, every search result it fetches, every third-party data source it queries — all carry the same risk.

## The Attack Techniques

Google catalogued several obfuscation methods attackers use to hide instructions from human visitors while keeping them legible to AI systems:

**Invisible rendering:** Text is shrunk to a single pixel, or rendered in a colour close enough to the background to be invisible to the human eye — white text on a white background being the simplest example. AI models process the raw text from HTML rather than the rendered view, so they see the instruction plainly.

**HTML comment injection:** Instructions are buried inside HTML comment tags (`<!-- ... -->`), invisible in the rendered page but fully present in the markup an AI agent parses.

**Metadata namespace injection:** Directives are embedded in page metadata and `<head>` tags rather than the visible body. The AI's web parser reads both.

**Persuasion amplifiers:** Some payloads include keywords like "ultrathink" or "disregard all prior instructions" intended to increase the likelihood that the model treats the injected directive as authoritative. The effectiveness of these tricks varies by model, but their presence in the wild shows that attackers are actively experimenting.

## A $5,000 PayPal Transaction Waiting to Fire

The most alarming example Google documented involves financial targeting. Researchers found a payload that contained a fully specified PayPal transaction: a PayPal.me link, a fixed amount of $5,000, and step-by-step instructions written explicitly for an AI agent equipped with payment capabilities.

The attack is not designed to steal credentials. It is designed to instruct the agent to authorise a payment directly. As AI assistants gain agentic capabilities — the ability to take actions, not just answer questions — the consequence of a successful injection shifts from a misleading answer to an executed financial transaction.

A second documented case combined metadata injection with a persuasion amplifier to route AI-mediated payments toward a Stripe donation link. The sophistication was low; the potential impact was not.

## The Liability Gap

Google researchers raised an issue that goes beyond technical defence: no legal framework currently determines who is liable when an AI agent with legitimate credentials executes a command planted by a malicious third-party website.

This is genuinely uncharted territory. If a user authorises an AI agent to access their bank account and the agent, while browsing the web on that user's behalf, executes a payment to an attacker's account via an injected instruction — who is responsible? The user who granted permissions? The AI vendor whose model was manipulated? The enterprise that deployed the agent? The website operator who hosted the injection?

Existing legal structures — consumer protection law, fraud statutes, financial regulation — were not written with autonomous AI agents in mind. The gap will likely produce litigation before it produces legislation.

## Scope and Caveats

Google's 32 percent figure should be read with the study's limitations in mind. The scan covered only public, static web pages — roughly two to three billion pages per month. Social media posts, content behind authentication walls, dynamic pages, and private documents were all outside the scope. The actual exposure across the full web, including authenticated enterprise content that agents routinely access, is almost certainly larger.

Google also noted that current attacks are relatively low in sophistication. Most detected injections are either pranks, opportunistic SEO manipulation, or unsophisticated financial lures. The high-capability, targeted attacks — where an adversary conducts reconnaissance on a specific company's AI agent deployment, crafts a precisely tailored payload, and plants it in content the agent is likely to visit — have been demonstrated by researchers but are not yet the dominant pattern in the wild data.

That distinction matters. It suggests there is still time to deploy defences before the attacker population becomes more skilled. It also suggests a natural evolutionary trajectory: as agentic AI use grows and high-value targets become visible, the sophistication of injection attacks will follow.

## What Defenders Can Do

Google's research team outlined several mitigation layers currently in use or under development:

**Output filtering:** AI systems can be trained or prompted to avoid executing instructions that arrive through third-party content channels rather than the trusted user channel.

**Provenance tracking:** Architectures that tag content by source — distinguishing between instructions from the user, instructions from the system prompt, and text retrieved from the web — allow models to apply different levels of trust to different inputs. Several frontier labs have been building variants of this approach into their agent frameworks.

**Sandboxed browsing:** Agents that browse the web in a sandboxed environment, with explicit confirmation required for any action involving external services, limit the blast radius of a successful injection.

**Capability scoping:** Agents should only have the capabilities they need for their current task. An agent deployed to summarise web research does not need payment permissions. Least-privilege design is an old security principle; it applies directly to agentic AI.

None of these measures is a complete solution. The fundamental tension — that AI agents are designed to follow instructions, and that instructions can be planted anywhere in their information environment — does not have an architectural resolution yet.

## The Broader Context

The timing of Google's disclosure is not incidental. The agentic AI deployment wave is accelerating sharply. OpenAI's Agents SDK, Anthropic's Claude with tool use, Google's own Gemini agents, and a growing ecosystem of third-party agent frameworks are moving AI assistants from answering questions to taking actions in the world. Every increase in an agent's capability expands the potential impact of a successful injection.

Google's scan began capturing systematic data in late 2025 — roughly coinciding with the first large-scale enterprise deployments of agentic systems. The 32 percent growth rate over just three months is the early slope of what could become a steeper curve as more agents browse more of the web with more permissions.

The security community has known about indirect prompt injection since at least 2023. What Google's research establishes is that the theoretical attack class has become an empirical reality — growing, financially motivated, and targeting the expanding frontier of what AI agents are trusted to do.
