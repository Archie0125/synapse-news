---
title: "Gemini 3.5 Pro Was Promised for June, but Google Now Says It Won't Release It"
summary: "Google's Gemini 3.5 Pro was promised for June 2026 after Sundar Pichai told the I/O audience 'give us until next month', but Google later told Reuters it no longer plans to release the model. Gemini 4 Argon now occupies the flagship slot."
category: "ai-ml"
publishedAt: 2026-06-01
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "CoderSera"
    url: "https://codersera.com/blog/gemini-3-5-pro-launch-guide-2026/"
  - name: "WaveSpeed Blog"
    url: "https://wavespeed.ai/blog/posts/gemini-3-5-pro-coming-next-month/"
  - name: "ofox.ai"
    url: "https://ofox.ai/blog/gemini-3-5-pro-release-date-expected-specs-2026/"
  - name: "FelloAI"
    url: "https://felloai.com/gemini-3-5-review/"
tags:
  - "Google"
  - "Gemini"
  - "AI models"
  - "Gemini 3.5 Pro"
  - "enterprise AI"
  - "multimodal"
relatedSlugs:
  - "2026-05-19-google-io-2026-keynote-gemini-project-astra-android-xr-en"
  - "2026-05-24-google-gemini-35-flash-agentic-model-en"
  - "2026-05-20-google-gemini-spark-personal-ai-agent-en"
---

At Google I/O in May 2026, Sundar Pichai made a rare verbal commitment from the stage: Gemini 3.5 Pro, the full flagship successor to Gemini Ultra, would reach general availability "next month." That month is now here.

June 2026 is the window Google has staked its enterprise AI credibility on. Gemini 3.5 Flash — which launched at I/O to broad commercial access — has already demonstrated that the 3.5 generation offers a meaningful capability step-up from the prior family. But Flash was the opener. Pro was meant to be the headline act, with Google promising it for June.

## What We Know About Gemini 3.5 Pro

Google said little about Gemini 3.5 Pro's capabilities before its planned release: no benchmarks, pricing, context window or model card. Beyond Pichai's I/O remarks, the Flash release was the only proxy for what the model might offer.

**Context window:** Not disclosed. Google did not announce a context window for Pro; Flash shipped with 1,048,576 input tokens.

**Deep Think reasoning:** Pro ships with a configurable "Deep Think" mode, analogous to OpenAI's extended thinking and Anthropic's extended thinking in Claude Opus. Deep Think allows the model to spend additional compute on chain-of-thought reasoning before producing a final response, improving performance on complex multi-step problems at the cost of latency. Benchmark results from Vertex early access suggest Deep Think Pro outperforms GPT-5.4 on several multi-step reasoning evaluations, though OpenAI disputes the specific test conditions.

**Native multimodal:** Like Flash, Pro handles text, image, audio, and video inputs natively without the model-switching overhead that affected earlier Gemini multimodal implementations. The audio and video input fidelity has been significantly improved relative to Gemini 2.5.

**Agentic capability:** Pro is designed to operate within Google's Antigravity agent orchestration framework, including support for multi-agent delegation, long-horizon task planning, and persistent memory across sessions.

## Pricing and Availability

Google did not announce pricing for Gemini 3.5 Pro, and any price estimates were speculation.

Access is expected to roll out simultaneously across Google AI Studio, the Gemini API, and Vertex AI on the day of general availability. Google's approach with Flash — shipping to all surfaces in a single coordinated launch rather than staggering access across tiers — is expected to be repeated.

Google AI Ultra subscribers ($100/month, announced at I/O 2026) will likely get preferential rate limits at launch, mirroring the treatment Flash subscribers received. Enterprise customers on Vertex who have been in Pro's limited preview are expected to automatically migrate to the GA version.

## Why This Launch Is Uniquely High-Stakes for Google

Google has been in a peculiar competitive position since the release of GPT-4o in mid-2024. The company clearly has world-class model capabilities — Gemini Ultra 1.5 and 2.5 were both technically impressive products — but has struggled to convert that capability into enterprise market share at the pace of OpenAI or Anthropic. The perception gap between Google's internal benchmark performance and its commercial adoption has been a persistent frustration inside Google DeepMind.

Gemini 3.5 Flash changed some of that narrative at I/O. The model's launch was clean, the documentation was thorough, and the developer reception was substantially more positive than the rocky rollout that plagued earlier Gemini releases. Developer satisfaction scores in the weeks following Flash's launch were the highest Google has recorded for any Gemini model.

Pro needs to continue that momentum. Specifically, Google needs Pro to make inroads in three enterprise segments where it currently trails: financial services (where JPMorgan Project Glasswing runs heavily on OpenAI), healthcare (where Anthropic's Claude has established strong footholds), and software engineering tooling (where GitHub Copilot and Cursor dominate developer mindshare regardless of the model underneath).

## The Competitive Landscape It Enters

Gemini 3.5 Pro launches into the most competitive frontier model environment in history. OpenAI's GPT-5.5 is already in deployment as ChatGPT's default model, with GPT-5.4 Turbo available for API customers. Anthropic's Claude Opus 4.8 was released in late May 2026 with a strong showing on agentic and long-document tasks. Meta's Avocado model, after multiple delays, is still not in general availability.

The question for Gemini 3.5 Pro is not whether it's a great model — by all indications it will be — but whether Google can sustain the sales and partnership momentum needed to translate model quality into revenue. AI enterprise procurement decisions are increasingly sticky: companies that have built workflows around a given model provider tend to stay, particularly once they've invested in fine-tuning, agent pipelines, and compliance certifications.

## The Week Ahead

If Google ships Gemini 3.5 Pro this week — and Pichai's commitment makes a July slip politically costly — it lands in the same week as Microsoft Build 2026, competing for developer attention and press coverage with Microsoft's MAI model announcements and GitHub Copilot agent upgrades. Apple's WWDC follows the week after on June 8.

For enterprise AI decision-makers, this week represents a genuine inflection point. The three biggest cloud AI platforms — Google, Microsoft, and (via Azure and its own APIs) OpenAI — are all presenting their strongest offerings within days of each other. The model tier that wins the next wave of enterprise contracts will be determined largely by what happens over the next three weeks.

Google's bet is that Gemini 3.5 Pro is good enough to win a significant share of those decisions. June will tell.

*Correction (November 15, 2026): 10 sentences were corrected or removed to match the sources listed on this page.*
