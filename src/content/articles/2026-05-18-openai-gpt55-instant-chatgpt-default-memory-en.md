---
title: "OpenAI Makes GPT-5.5 Instant the New ChatGPT Default, Cutting Hallucinations by Half"
summary: "OpenAI replaced GPT-5.3 Instant with GPT-5.5 Instant as ChatGPT's default model on May 5, delivering 52.5% fewer hallucinations, higher benchmark scores on AIME and MMMU-Pro, and a new memory sources feature that lets the model draw on past conversations, uploaded files, and Gmail to personalize responses."
category: "ai-ml"
publishedAt: 2026-05-18
lang: "en"
featured: false
trending: true
sources:
  - name: "OpenAI"
    url: "https://openai.com/index/gpt-5-5-instant/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/"
  - name: "eWeek"
    url: "https://www.eweek.com/news/openai-gpt-55-instant-chatgpt-default-model/"
tags:
  - "OpenAI"
  - "GPT-5.5"
  - "ChatGPT"
  - "AI models"
  - "hallucinations"
  - "memory"
relatedSlugs:
  - "2026-05-18-openai-chatgpt-ads-manager-self-serve-en"
  - "2026-05-15-openai-gpt-realtime-2-voice-models-en"
  - "2026-05-14-openai-daybreak-cybersecurity-gpt55-en"
---

OpenAI quietly made its largest under-the-hood ChatGPT upgrade in months on May 5, 2026, swapping the default model from GPT-5.3 Instant to GPT-5.5 Instant across all user tiers — from the free tier through Plus, Pro, Business, and Enterprise. The change, which rolled out without a major product event, represents a meaningful step forward in accuracy, conversational quality, and personalization, while setting up the infrastructure for a broader memory architecture that will define how AI assistants handle long-term relationships with users.

## The Hallucination Gap

The headline metric is a 52.5% reduction in hallucinated claims compared to GPT-5.3 Instant on high-stakes prompts spanning medicine, law, and finance. Hallucination reduction is notoriously difficult to benchmark cleanly because the definition of a hallucination depends on the ground-truth source, but OpenAI's internal testing used structured evaluation sets where factual claims could be verified against authoritative references.

For everyday users, the difference is tangible. GPT-5.5 Instant is more likely to respond "I don't know" or "this is uncertain" in domains where it lacks confident grounding, rather than generating plausible-sounding but incorrect information with the same confident tone it uses for well-established facts. The model has also been tuned to be less verbose — fewer gratuitous bullet points, less excessive structure imposed on conversational replies, and fewer unnecessary follow-up questions that add friction without adding value.

## Benchmark Improvements

On the AIME 2025 math competition dataset, GPT-5.5 Instant scores 81.2, up from 65.4 with its predecessor — a 24% improvement in a domain that tests multi-step symbolic reasoning rather than pattern matching. On MMMU-Pro, a multimodal reasoning benchmark that requires integrating visual and textual information, the model scores 76, up from 69.2.

These gains position GPT-5.5 Instant competitively against Claude Mythos on certain evaluations, though Anthropic's frontier model retains advantages in multi-step agentic tasks and extended reasoning benchmarks. For the average ChatGPT user, the AIME and MMMU-Pro numbers are largely academic — what matters is whether the model answers their actual question accurately and clearly, a quality that is harder to summarize in a number than a benchmark score.

## Memory Sources: The More Significant Shift

The more architecturally interesting change in the May 5 update is not the model itself but the memory sources feature rolling out across all ChatGPT models. When GPT-5.5 Instant personalizes a response — by drawing on something a user said three conversations ago, referencing an uploaded document, or surfacing relevant context from a connected Gmail account — it now shows a transparency layer: what specific information was used, and from what source.

For Plus and Pro users on the web, the model can now actively query past conversations, uploaded files, and connected Gmail to construct personalized responses. A user asking "what did I decide to do about the Q3 budget?" can get an answer that references their own uploaded spreadsheet or a prior conversation where they discussed the decision. The memory is not passive — it is retrieved and applied in real time.

Critically, this is opt-in and auditable. Users can see exactly which memories were used in any given response and can delete or correct individual memory entries. OpenAI's framing is transparency as a feature rather than a compliance checkbox — a direct response to criticism that AI personalization had historically been a black box.

The feature is rolling out first to Plus and Pro users on web, with mobile and Free/Go/Business/Enterprise expansion coming in subsequent weeks. The roadmap also hints at cross-session memory for coding projects and long-running research tasks, which would make GPT-5.5 Instant a more capable partner for developers running iterative workflows.

## API Access and Developer Impact

For developers, GPT-5.5 Instant is available in the API as `chat-latest`, which now resolves to the new model. OpenAI has confirmed that GPT-5.3 Instant will remain available as an explicit model option for paid API users for approximately three months before deprecation, giving teams time to test for regression before fully migrating.

The model's improved factuality and reduced verbosity will likely be more impactful for production use cases than for experimental ones. Applications built on ChatGPT for customer support, document analysis, or professional research have tended to struggle most with hallucination — which is precisely where GPT-5.5 Instant's improvements are most concentrated. For developers who have implemented elaborate post-processing filters or fact-checking layers to compensate for GPT-5.3's error rate, the upgrade may allow some of that defensive engineering to be removed.

## What GPT-5.5 Is Not

It is worth being precise about what this update does not represent. GPT-5.5 Instant is an incremental upgrade, not a frontier model release. It is not Claude Mythos, which pushes the state of the art in extended reasoning and agentic benchmarks. It is not a replacement for the o-series reasoning models that OpenAI continues to offer for tasks requiring deep deliberative chains of thought.

OpenAI's model lineup has become deliberately stratified: Instant-class models for fast, conversational, cost-efficient responses; reasoning models for structured problem-solving; and specialty models for voice, image generation, and code. GPT-5.5 Instant occupies the base of the inference-speed stack — the model that handles the majority of ChatGPT interactions worldwide — and improving it matters more for aggregate user experience than any single frontier model release, simply because of the volume at which it operates.

## The Competitive Context

The May 5 rollout was strategically timed. Anthropic launched Claude for Small Business on May 13 with integrations spanning QuickBooks, HubSpot, and Canva. Google is 24 hours away from its I/O 2026 keynote, expected to feature a Gemini model upgrade that analysts predict will be competitive with GPT-5.5 Instant. The model quality race is now continuous rather than episodic — with all three major labs making incremental improvements on timescales of weeks rather than months.

For users, the practical benefit is simple: ChatGPT has become more reliable in the places where unreliability was most costly. For OpenAI, a better default model reduces churn, strengthens the subscription value proposition, and creates a more defensible base from which to layer the advertising, memory, and enterprise features that will define its business model over the next two years.
