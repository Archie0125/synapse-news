---
title: "OpenAI, Anthropic, and Google Unite to Block Chinese AI Model Copying"
summary: "Three of the world's leading AI labs are formally sharing intelligence through the Frontier Model Forum to detect and block 'adversarial distillation' — a technique where outside labs bombard US AI systems with automated prompts to clone their behavior. Anthropic alone documented 16 million extraction attempts linked to Chinese AI firms, escalating the fight over intellectual property at the AI frontier."
category: "policy"
publishedAt: 2026-04-07T09:00:00Z
lang: "en"
featured: true
trending: true
sources:
  - name: "Bloomberg: OpenAI, Anthropic, Google Unite to Combat Model Copying in China"
    url: "https://www.bloomberg.com/news/articles/2026-04-06/openai-anthropic-google-unite-to-combat-model-copying-in-china"
  - name: "Japan Times: OpenAI, Anthropic, Google vs. China Distillation"
    url: "https://www.japantimes.co.jp/business/2026/04/07/tech/openai-anthropic-google-china-copy/"
  - name: "StartupNews.fyi: AI Labs Come Together to Combat Model Copying"
    url: "https://startupnews.fyi/2026/04/07/openai-anthropic-google-come-together-to-combat-model-copying-in-china/"
tags:
  - "AI policy"
  - "China"
  - "intellectual property"
  - "OpenAI"
  - "Anthropic"
  - "Google"
  - "model distillation"
relatedSlugs:
  - "2026-04-04-eu-ai-act-enforcement-en"
  - "2026-04-05-trump-eo-state-ai-preemption-en"
  - "2026-04-03-us-china-chip-war-en"
---

# OpenAI, Anthropic, and Google Unite to Block Chinese AI Model Copying

Three of the world's most powerful AI laboratories — OpenAI, Anthropic, and Google DeepMind — have quietly escalated their coordinated response to what they describe as a systemic campaign by Chinese AI companies to reverse-engineer US frontier models through a technique called **adversarial distillation**. The collaboration, formalized through the Frontier Model Forum, the nonprofit the three co-founded alongside Microsoft in 2023, represents one of the most significant moments of collective action the AI industry has taken against a shared competitive and national security threat.

## What Is Adversarial Distillation?

Unlike traditional AI research, which requires enormous datasets and months of expensive compute, adversarial distillation exploits a shortcut: feed a target model millions of cleverly crafted prompts, record its outputs, and use those input-output pairs to train a copycat model. The result can approximate the original's capabilities without bearing the original's training costs — in essence, free-riding on years of R&D investment.

The technique is not new. Academic papers on knowledge distillation have circulated since 2015, and it is used legitimately to compress large models into smaller, faster ones for deployment. But at industrial scale, targeted at frontier models, and orchestrated by state-adjacent actors, the practice crosses into a legally and geopolitically contested space that US AI companies have been reluctant to name publicly — until now.

## Anthropic Documents 16 Million Extraction Attempts

The numbers Anthropic has shared with US lawmakers are striking. The company documented approximately **16 million automated exchange attempts** it attributes to distillation campaigns originating from, or connected to, **DeepSeek, Moonshot AI, and MiniMax** — three Chinese AI firms that have released competitive open-weight or API-accessible models in the past 18 months.

Anthropic's security team found that the queries were not random. They were statistically structured to maximize capability coverage: systematically probing reasoning, coding, multilingual translation, tool use, and safety-critical behavior, in patterns consistent with automated data harvesting rather than organic user activity. In multiple documented cases, the extracted outputs were then used in downstream training pipelines that stripped away Claude's safety guardrails.

"This is not about competition — it's about theft," a senior Anthropic policy official told Bloomberg. "They extracted the capabilities we spent billions building and removed the safety properties we spent years developing. That combination is dangerous."

## OpenAI's Case to Congress

OpenAI has brought its own evidence to Capitol Hill, arguing in written testimony that DeepSeek specifically "attempted to free-ride on the capabilities developed by OpenAI and other US frontier labs." The company pointed to timing correlations between the release of its frontier models and sudden capability jumps in DeepSeek's subsequent releases, which it argued are implausible without significant data harvesting.

The company estimates the cumulative cost of these distillation campaigns to US AI firms at **billions of dollars annually** in lost competitive advantage — though critics note that figure is inherently difficult to verify, and that DeepSeek's success also reflects genuine domestic Chinese AI research capability.

Google has declined to enumerate specific incident counts publicly but has acknowledged sharing threat intelligence through the Frontier Model Forum on attempts to distill from Gemini model families.

## The Frontier Model Forum's New Role

The Frontier Model Forum, historically focused on AI safety benchmarking and red-teaming standards, is now functioning as an intelligence-sharing consortium for IP protection — a significant expansion of its mandate. Under a new working group, participating labs share sanitized attack signatures, IP ranges, and behavioral fingerprints of distillation attempts so that all members can update their rate-limiting, anomaly-detection, and terms-of-service enforcement simultaneously.

This creates a network effect: when one lab detects a new distillation campaign and blocks it, the other three labs can block the same infrastructure within hours, closing the exploit before the attacker can pivot.

## Legal and Regulatory Dimensions

The policy implications are significant. OpenAI and Anthropic are now lobbying for federal legislation that would explicitly classify large-scale adversarial distillation as a form of trade secret theft, punishable under the Economic Espionage Act. Currently, the legal status of distillation-as-copying is murky — model weights themselves may not be protectable as copyrighted works under US law, and prompt-response pairs occupy an even grayer zone.

The US Department of Commerce has also flagged the issue in its ongoing review of AI-related export controls. One option under discussion is treating frontier model API access as a controlled "deemed export," requiring licenses for users in certain jurisdictions — a move that would fundamentally restructure how US AI companies handle international developer access.

The Chinese government has not officially responded to the allegations. DeepSeek, Moonshot AI, and MiniMax did not return requests for comment.

## Industry Skeptics

Not everyone is convinced the threat is as clean-cut as the US labs portray. Several independent AI researchers argue that the labs have a financial interest in framing competition as IP theft, and that much of what appears to be distillation may simply reflect the convergent evolution of transformer architectures trained on similar public data.

"Frontier models are increasingly trained on similar corpora, with similar RLHF techniques, so of course capabilities converge," wrote one AI researcher on X. "Calling that distillation is a convenient narrative."

Others worry that if federal legislation brands distillation as theft broadly, it could threaten legitimate model compression research, open-source fine-tuning, and academic benchmarking — activities that benefit the global research community.

## What Comes Next

The three labs are expected to publish a joint white paper through the Frontier Model Forum in the coming weeks, outlining proposed technical standards for watermarking model outputs to make distillation more detectable. Several cryptographic watermarking schemes have been proposed in the academic literature, though none has yet proven robust at scale against adversarial removal.

On the regulatory side, the coalition is pushing for both domestic legislation and coordinated action through the G7, which has an active working group on AI governance. The outcome will likely shape how frontier AI labs structure their API access tiers, their terms of service enforcement, and their geopolitical positioning for years to come.

What is clear is that the era of treating AI model access as a pure commercial question, uncomplicated by national security concerns, is ending. The US frontier AI labs have drawn a line — and they are asking Washington to help them hold it.
