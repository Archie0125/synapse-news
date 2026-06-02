---
title: "GPT-5.6 Is Leaking Out of OpenAI's Own Logs — and Prediction Markets Are 85% Sure It Drops This Month"
summary: "Codex backend log traces referencing a 'gpt-5.6' model identifier, three internal codenames, and developer reports of a 1.5-million-token context window have convinced prediction markets there is an 85%+ probability of a GPT-5.6 release before June 30. The signals point to multiple model variants, a major context upgrade, and a new UltraFast tier for Codex — arriving into the most competitive frontier AI summer on record."
category: "ai-ml"
publishedAt: 2026-06-02
lang: "en"
featured: false
trending: true
sources:
  - name: "WaveSpeed Blog — Codex Log Canary Analysis"
    url: "https://wavespeed.ai/blog/posts/gpt-5-6-canary-leak-what-we-know/"
  - name: "CometAPI — GPT-5.6 Release Date & Features"
    url: "https://www.cometapi.com/gpt-5-6-release-date-features-development/"
  - name: "Perplexity AI Magazine — GPT-5.6 Leaks and Expectations"
    url: "https://perplexityaimagazine.com/ai-news/gpt-56-release-date-features-leaks-openai-2026/"
  - name: "Polymarket"
    url: "https://manifold.markets/prismatic/when-will-gpt56-be-released-L8pNyNgctq"
tags:
  - "OpenAI"
  - "GPT-5.6"
  - "AI models"
  - "Codex"
  - "context window"
  - "prediction markets"
  - "frontier AI"
relatedSlugs:
  - "2026-06-02-xai-grok-41-fast-enterprise-api-grok5-roadmap-en"
  - "2026-05-10-openai-gpt55-instant-chatgpt-default-en"
---

Three weeks after GPT-5.5 launched on April 23, 2026, a researcher named Haider was poring through routing metadata in OpenAI's Codex deployment backend when he spotted something that wasn't supposed to be visible yet: a rollout-mapping entry referencing `gpt-5.6`. The entry disappeared within hours. By then, it had been screenshotted, shared, and set off a chain of analysis that now has Polymarket pricing a greater than 85% probability of a public GPT-5.6 release before June 30.

As of June 2, OpenAI has made no official statement about a model by that designation. There is no API entry, no model card, no published benchmarks. What exists is a set of signals that, taken together, paints a fairly clear picture of what is coming — and when.

## The Canary Evidence

The Codex log entry was the first indicator, but it wasn't the last. Security and API researchers who track OpenAI's infrastructure spotted additional signals over the following weeks:

**Three internal codenames** have been identified: iris-alpha (likely the flagship variant), ember-alpha (possibly an Instant or Fast counterpart), and beacon-alpha (possibly a specialized vertical variant). The existence of three codenames suggests GPT-5.6 is not a single model but a family, consistent with OpenAI's pattern since GPT-5 of releasing a flagship alongside lower-latency variants.

**A 1.5-million-token context window** has been reported by ChatGPT Pro users who hit what appeared to be a higher-than-expected ceiling during extended sessions, with inputs up to 900,000 tokens being handled smoothly and requests exceeding 1.05 million — GPT-5.5's documented maximum — completing without truncation. A 1.5-million-token context would represent a 43% increase over GPT-5.5's 1.05M limit, continuing the trajectory that has seen OpenAI's context window nearly double every major release.

**A UI screenshot** attributed to an early access session showed the model generating a minimal note-taking application interface called "Lumen Notes" from a brief, unstructured prompt — a capability that exceeds what GPT-5.5 can do reliably in zero-shot settings, particularly for web-standard output.

**Codex UltraFast mode** has been mentioned in developer documentation fragments — a new inference tier designed to significantly reduce latency for code completion and agent tool use, targeting the same speed bracket as current fast models but with the capability of the full 5.6 flagship.

## Why the Market Is So Confident

Polymarket prediction markets, which have accumulated a reasonable track record on AI release timing, currently price GPT-5.6 at 85%+ probability for release before June 30, 2026. Manifold Markets is in the 80-89% range.

The confidence reflects several factors beyond the specific signals. OpenAI has maintained a release cadence of roughly 6-8 weeks between major model versions in 2026, with GPT-5.5 arriving April 23 and GPT-5.5 Instant following in early May. Six weeks after GPT-5.5's API launch places us precisely in the June 2-9 window for a potential GPT-5.6 announcement. OpenAI's recent pattern of Friday API drops followed by wider consumer rollout over the following days would fit that timeline.

Competitive pressure is also a real factor. xAI's Grok 5 roadmap is public, its 10-trillion-parameter ambitions are on the record, and Grok 4.1 Fast just entered the enterprise API. Google's Gemini 3.5 Pro launched in June with strong benchmark numbers. Allowing a multi-week gap between GPT-5.5 and the next flagship while competitors are releasing would be out of character for OpenAI's 2026 posture.

## What GPT-5.6 Would Change

If the leaks are accurate, GPT-5.6's most consequential upgrade is the context window expansion. At 1.5 million tokens, the model would be able to hold an entire codebase, a year of email correspondence, or a multi-hundred-page legal document in active context and reason about it coherently. The practical use cases this unlocks — multi-repository code refactoring, comprehensive audit trail analysis, deep document discovery — are precisely the enterprise workflows that have been the hardest to automate with shorter-context models.

The Codex UltraFast tier, if it materializes, would address the latency gap that has made real-time coding applications feel sluggish at the frontier. Current Codex inference on the GPT-5.5 series is fast enough for background suggestions but too slow for keystroke-level completion in demanding engineering environments. A UltraFast tier could change the competitive calculus against GitHub Copilot, which just announced Project Polaris as its new default model.

The three codename variants suggest OpenAI is also continuing its strategy of fragmenting the product line by use case — a flagship for complex reasoning, a fast tier for latency-sensitive applications, and potentially a domain-specific variant. That fragmentation serves different customer segments but also increases the surface area of what needs to be evaluated and maintained.

## What It Means for the Summer

The AI model release calendar for summer 2026 is shaping up to be the most congested in the industry's short history. GPT-5.6 expected in June. Grok 4.4 and 4.5 within weeks. Grok 5 in Q2-Q3. Potential Claude updates from Anthropic. The WWDC 2026 keynote on June 8 where Apple is expected to announce major AI platform expansions.

For developers and enterprise customers trying to make AI infrastructure decisions, this pace creates a genuine planning challenge. Commitments made today to a specific model tier may look different by August. The organizations best positioned to navigate this environment are those with abstraction layers in their own architecture — API clients that can swap underlying models, evaluation pipelines that can benchmark new releases quickly, and deployment infrastructure that doesn't tightly couple to a specific model version.

OpenAI has said nothing publicly about GPT-5.6. The signals say something else.
