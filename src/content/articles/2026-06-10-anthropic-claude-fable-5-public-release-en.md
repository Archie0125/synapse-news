---
title: "Anthropic Opens the Vault: Claude Fable 5, Its Most Powerful AI, Is Now Public"
summary: "Anthropic released Claude Fable 5 on June 9, making the first publicly available version of its Mythos model available to developers and consumers. The model ships with safety guardrails in high-risk domains and costs double the price of Opus 4.8, a bet that peak capability and responsible deployment can coexist, released just days after the company urged major AI labs to coordinate a brake on frontier AI development."
category: "ai-ml"
publishedAt: 2026-06-10
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: true
trending: false
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/"
  - name: "Anthropic Newsroom"
    url: "https://www.anthropic.com/news/claude-fable-5-mythos-5"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/06/09/anthropic-mythos-claude-fable-5.html"
  - name: "gHacks Tech News"
    url: "https://www.ghacks.net/2026/06/10/anthropic-releases-claude-fable-5-to-pro-max-and-enterprise-users-free-until-june-22/"
  - name: "Amazon About"
    url: "https://www.aboutamazon.com/news/aws/claude-fable-5-anthropic-available-amazon-bedrock"
tags:
  - "Anthropic"
  - "Claude"
  - "Fable 5"
  - "LLM"
  - "AI models"
  - "AI safety"
  - "benchmarks"
relatedSlugs:
  - "2026-06-09-anthropic-ipo-s1-one-trillion-en"
  - "2026-06-08-microsoft-ai-independence-mustafa-suleyman-mai-en"
---

Anthropic spent years insisting that its most capable models were simply too powerful to release broadly. On June 9, that calculus changed. The San Francisco AI safety company made Claude Fable 5 — its first Mythos-class model — available to the public, offering consumers, developers, and enterprises access to capabilities the company had previously restricted to a vetted inner circle.

The launch arrived in a charged moment. Critics were quick to note the apparent contradiction. The company's implicit answer: Fable 5 ships with the most elaborate safety architecture it has ever built into a public model.

## A New Tier of Performance

On the software engineering benchmark SWE-bench Verified, Fable 5 scores 95% — a figure that eclipses Claude Opus 4.8's 88.6% and sets a new public high-water mark. In third-party evaluations, the gains were even more striking in applied settings.

Analytics platform Hex reported that Fable 5 was "the first model to reach 90% on our core analytics benchmark," a proprietary test measuring real-world data analysis quality. Genspark, an AI search and workflow company, found it "beat every other model" across their internal suite, particularly on UI design generation and game coding. App-building platform Base44 highlighted its superiority in generating complex, multi-component applications from natural language prompts.

Anthropic says the model excels at software engineering, knowledge work, and vision. For code-heavy enterprise workflows, the benchmark numbers carry direct business weight — companies paying for AI coding assistance are acutely aware of the difference between a 75% and a 95% success rate on real tasks.

Alongside Fable 5, Anthropic also released Claude Mythos 5, an updated version of the underlying frontier model, to organizations that had already been approved for Mythos access through Anthropic's restricted program.

## Safety by Architecture, Not Policy

What distinguishes Fable 5 from simply releasing an unconstrained frontier model is its new set of safety classifiers. In high-risk areas — cybersecurity, biology and chemistry, and distillation — classifiers detect the request, Fable 5's response is blocked, and Claude Opus 4.8 handles it instead.

This two-tier approach represents a significant engineering departure. Rather than relying on fine-tuning Fable 5 to refuse dangerous requests — a method that has proven porous across the industry — Anthropic built the restriction into the routing layer itself. Users are informed whenever the fallback occurs.

The results appear robust. Anthropic ran an external bug bounty program that produced no universal jailbreaks in over 1,000 hours of testing, though it noted the UK AISI made progress toward one within a brief initial testing window. Early deployment data shows that approximately 95% of sessions run entirely on Fable 5 responses, meaning the fallback triggers rarely in practice — less than 5% of sessions.

"The model includes safeguards that would make this risk manageable," Anthropic said in its release documentation, framing the release as a demonstration that safety and capability are not inherently at odds.

## The Price of Power

Fable 5 comes with a significant cost increase. Pricing is set at $10 per million input tokens and $50 per million output tokens — exactly double what enterprises pay for Opus 4.8. For applications that make frequent or high-volume API calls, the economics require careful recalibration.

To soften the transition, Anthropic made Fable 5 available at no extra charge through June 22 to subscribers on Pro, Max, Team, and seat-based Enterprise plans. After that date, Anthropic will remove Fable 5 from those plans and require usage credits, though it aims to restore it as a standard part of subscription plans when capacity allows.

## A Controversial Data Retention Change

Tucked into the release announcement was a policy change: Anthropic will require 30-day retention for all traffic on Mythos-class models, including Fable 5 and Mythos 5, for business customers.

For developers who chose Anthropic's API specifically for its zero-retention guarantee — a promise that requests and responses would never be stored — this marks a material breach of expectations. Anthropic framed the retention as a security necessity, explaining that logs are required to identify novel jailbreak attempts and coordinate responses to emerging attack patterns.

Privacy-focused legal and compliance teams at large enterprises are likely to treat this change as a renegotiation of risk. Several developer communities flagged the move as a reason to evaluate alternative providers.

## The Paradox at the Center

The timing of Fable 5's release is impossible to separate from its context. Anthropic's researchers have positioned the company for years as the safety-first alternative in a race they believe could end in catastrophe. Releasing a model this capable to the public days after urging labs to coordinate a brake on AI development is, at minimum, a communications challenge.

The company's answer — that robust safety architecture makes such releases responsible rather than reckless — is philosophically coherent. Whether it is practically adequate depends on whether the 5% of sessions that trigger guardrails are the right 5%, and whether the 30-day log retention creates new attack surfaces of its own.

What is not in dispute is the strategic logic. As OpenAI moves forward with its IPO and Google continues embedding Gemini across its ecosystem, Anthropic needed to demonstrate that its most capable models are not merely safe in a vault. Fable 5 is the company's clearest answer to the question of whether responsible AI development can also be commercially competitive.

For the developers who build on it, the answer will arrive in the weeks ahead — measured in benchmarks, billing cycles, and the eventual scrutiny of whatever the first 5% of blocked sessions turn out to be.

*Correction (November 15, 2026): 11 sentences were corrected or removed to match the sources listed on this page.*
