---
title: "Silicon Valley Unites Against Chinese AI Theft: The Frontier Model Forum Goes to War"
summary: "OpenAI, Anthropic, and Google have activated the Frontier Model Forum as a live threat-intelligence operation, pooling defenses against an industrial-scale adversarial distillation campaign traced to DeepSeek, Moonshot AI, and MiniMax. Anthropic alone documented 16 million unauthorized extractions via 24,000 fake accounts and has banned all Chinese-controlled companies from Claude."
category: "policy"
publishedAt: 2026-04-13
lang: "en"
featured: true
trending: true
sources:
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-04-06/openai-anthropic-google-unite-to-combat-model-copying-in-china"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/02/24/anthropic-openai-china-firms-distillation-deepseek.html"
  - name: "BanklessTimes"
    url: "https://www.banklesstimes.com/articles/2026/04/07/openai-google-anthropic-team-up-to-block-chinese-scraping/"
  - name: "Prism News"
    url: "https://www.prismnews.com/news/openai-anthropic-google-team-up-to-block-chinese-ai"
tags:
  - "openai"
  - "anthropic"
  - "google"
  - "china"
  - "ai-policy"
  - "frontier-model-forum"
  - "distillation"
  - "deepseek"
  - "cybersecurity"
relatedSlugs:
  - "2026-04-13-us-match-act-duv-chip-export-ban-en"
  - "2026-04-12-anthropic-mythos-cybersecurity-model-en"
---

OpenAI, Anthropic, and Google have formally declared that they are sharing threat intelligence to combat what they describe as an industrial-scale campaign to steal their frontier AI models — and for the first time, they have named the adversaries: DeepSeek, Moonshot AI, and MiniMax.

The disclosure, made through the Frontier Model Forum — the industry nonprofit the three companies co-founded alongside Microsoft in 2023 — represents an unprecedented activation of the Forum as a live, operational threat-intelligence hub. Previously the organization had focused on policy advocacy and safety research. Now it is functioning more like an AI-sector equivalent of the Financial Services Information Sharing and Analysis Center: a trusted clearinghouse for real-time attack signatures and coordinated defenses.

## The Attack: Adversarial Distillation at Industrial Scale

The technique at the center of the dispute is called adversarial distillation. In legitimate machine learning, distillation allows engineers to compress a large "teacher" model into a smaller, more efficient "student" model by training the student on the teacher's outputs. The result is a compact model that approximates the teacher's capabilities at a fraction of the compute cost.

Adversarially applied, the same technique becomes a form of intellectual property theft. Attackers create fraudulent accounts, flood frontier AI APIs with millions of carefully engineered prompts, harvest the responses, and use that synthetic data to train their own competitive models — effectively bootstrapping themselves onto years of R&D investment and hundreds of billions of dollars in training compute.

The numbers Anthropic has published are striking: more than 16 million unauthorized exchanges extracted from Claude, routed through approximately 24,000 fraudulently created accounts — all traced to three Chinese AI companies. OpenAI and Google each confirmed comparable patterns at similar scale, though they declined to publish specific figures.

## How the Alliance Works

The Frontier Model Forum's new threat-sharing arrangement is explicitly modeled on cybersecurity intelligence sharing. When one company's detection systems flag an adversarial distillation pattern — a suspicious query structure, an IP range, a burst of statistically unusual prompt sequences — it encodes the signature and distributes it to the other members. Early detection by one lab instantly becomes a shared defense for all three.

The response toolkit is layered and surgical. The bluntest measures are account termination and IP blocking. More sophisticated defenses include rate-limiting adjustments that throttle suspicious query patterns without affecting legitimate users, and a particularly clever technique the companies are calling "output perturbation": subtly altering the statistical properties of API responses in ways that introduce noise into any training corpus assembled from those responses, degrading the quality of a student model trained on them without being perceptible in any individual response.

"This is the first time the Forum has been activated as an active threat-intelligence operation against a specific external adversary," a source familiar with the negotiations told Bloomberg. The transition from policy forum to operational defense network reflects how seriously the frontier labs now view model extraction as a strategic threat.

## Anthropic Takes the Most Aggressive Stance

Among the three companies, Anthropic has gone furthest. Beyond flagging accounts and deploying output perturbation, it has imposed a blanket ban on access by all Chinese-controlled companies — a sweeping measure that effectively severs Claude from a significant share of its commercial addressable market in Asia.

The policy applies to both API and consumer products. It is, in effect, a unilateral decoupling, and it mirrors the company's broader posture on its Mythos model: Anthropic has declined to release Mythos publicly at all, citing dual-use security risks. "We treat adversarial distillation as a form of IP theft with national security implications," the company said in a statement. "It is not simply a terms-of-service violation."

This framing is significant. By invoking national security rather than mere IP protection, Anthropic is signaling that it views model extraction as part of a broader geopolitical competition — one where the company has chosen a side.

The seriousness of Anthropic's concerns is underscored by a technical footnote buried in the Mythos disclosures: researchers using the model found a 27-year-old vulnerability in the OpenBSD operating system. The implication is clear — a model capable of finding such obscure, high-value bugs is not something its creators are willing to expose to systematic intelligence extraction.

## The Named Adversaries

DeepSeek, Moonshot AI, and MiniMax are each significant players in China's AI ecosystem. DeepSeek became globally prominent in early 2025 when its R1 model delivered benchmark performance competitive with GPT-4 at a fraction of the publicly stated training cost — a result that prompted significant industry speculation about data sourcing practices.

Moonshot AI operates Kimi, one of China's most widely used large language models, and has raised over $3 billion from investors including Alibaba. MiniMax, backed by Tencent and Hillhouse Capital, has focused on multimodal and conversational AI applications.

None of the three companies has publicly responded to the specific allegations. Chinese state media has characterized the U.S. companies' actions as protectionist measures dressed up in security language.

## The Geopolitical Dimension

The disclosures land in an already charged environment. Multiple rounds of U.S. semiconductor export controls have attempted to limit China's access to the advanced GPUs needed to train frontier models. Critics of those hardware-focused controls have long argued that they are incomplete: if Chinese labs can extract model intelligence through software-level API attacks, restricting chip access solves only half the problem.

The Frontier Model Forum's intervention suggests the industry has reached the same conclusion. Model extraction may now be a more efficient path to capability parity than building indigenous training infrastructure — which makes the API perimeter a more strategically consequential battleground than the chip supply chain.

Congressional offices have reportedly requested briefings from all three companies, and the disclosures are expected to inform pending legislation, including the MATCH Act, which targets semiconductor equipment exports to China.

## What Comes Next

The Frontier Model Forum is in discussions about formalizing a shared technical standard for "distillation resistance" — a set of API design principles and output-perturbation specifications intended to make adversarial distillation substantially less productive without degrading the experience for legitimate developers.

OpenAI, Anthropic, and Google are each independently training detection models on known adversarial distillation query patterns; the Forum would facilitate cross-company validation of these detectors and establish shared criteria for escalating confirmed attacks to law enforcement and regulators.

For the developers who build on these APIs, the practical impact is mostly invisible — the defenses are designed to be transparent. But the symbolic shift is real: three companies that compete fiercely on model capability have concluded that on this issue, collective defense is more effective than individual vigilance. The era of frontier AI APIs as freely harvestable training data pipelines is, by their account, over.
