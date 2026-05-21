---
title: "Google I/O 2026: Gemini Spark, Omni, and the AI Agent That Never Sleeps"
summary: "Google's I/O 2026 keynote delivered its most consequential developer event in years: Gemini 3.5 Flash, a 24/7 background AI agent called Gemini Spark, a world-modeling video platform called Gemini Omni, and a revamped $100/month AI Ultra subscription. The company is betting it can win the AI war by being simultaneously the cheapest and the most capable."
category: "ai-ml"
publishedAt: 2026-05-21
lang: "en"
featured: true
trending: false
sources:
  - name: "Google Blog – 100 Things We Announced at I/O 2026"
    url: "https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/"
  - name: "CNBC – Google debuts new AI models at I/O 2026"
    url: "https://www.cnbc.com/2026/05/19/google-ai-ultra-gemini-spark-omni.html"
  - name: "Latent Space – Google I/O 2026 Recap"
    url: "https://www.latent.space/p/ainews-google-io-2026-gemini-35-flash"
  - name: "Tom's Guide – Biggest Google I/O 2026 Announcements"
    url: "https://www.tomsguide.com/news/live/google-io-2026-live-news-updates"
tags:
  - "Google"
  - "Gemini"
  - "AI agents"
  - "Google I/O"
  - "Gemini Spark"
  - "Gemini Omni"
  - "developer tools"
relatedSlugs:
  - "2026-05-15-google-io-2026-preview-gemini-android-en"
  - "2026-05-15-google-gemini-omni-video-model-leak-en"
  - "2026-05-15-anthropic-agent-sdk-billing-split-en"
---

Every year, Google I/O sets the tone for what the rest of the industry will spend months chasing. This year's conference, held on May 19, 2026 at the Shoreline Amphitheatre in Mountain View, landed harder than most. Sundar Pichai took the stage with a clear thesis: the race is no longer just about who has the best model — it is about who can put AI agents into the hands of the most people, at the lowest cost, running around the clock.

The result was a keynote dense with product announcements. But four threads woven through everything: a new flagship-class model at flash prices, a personal AI agent that operates while you sleep, a world-modeling video platform, and a subscription tier designed to win over the power user.

## Gemini 3.5 Flash: Frontier Performance at Half the Price

The centerpiece model announcement was Gemini 3.5 Flash, which Google is positioning as an unusual achievement — a lighter-weight model that outperforms its own previous-generation pro model on coding and agentic benchmarks. According to Google's internal evaluations, Gemini 3.5 Flash beats Gemini 3.1 Pro on both dimensions while running approximately four times faster.

Pricing tells the story: $1.50 per million input tokens and $9.00 per million output tokens, with cached input at $0.15 per million. That is roughly a 3× increase over Gemini 3 Flash's rates, but Google argues the performance-per-dollar still improves significantly because the model needs far fewer tokens to complete complex tasks.

As of May 19, Gemini 3.5 Flash is the default model powering the Gemini app and AI Mode in Google Search worldwide. For developers, it is available immediately through the Gemini API. The pricing shift reflects a deliberate strategy Pichai articulated directly: "We are building models cheap and fast enough to deploy across products used by billions, while staying at the frontier."

## Gemini Spark: The Agent That Never Closes

The most headline-grabbing announcement was Gemini Spark, Google's direct answer to OpenAI's Operator and Anthropic's autonomous agent research. Unlike conventional AI assistants that only work while you have an active session open, Spark runs 24/7 on dedicated Google Cloud virtual machines — continuing tasks whether your laptop is open, closed, or off entirely.

Spark is powered by Gemini 3.5 and the updated Antigravity agent harness. It is built for long-horizon work: drafting and sending emails autonomously, monitoring feeds and surfacing relevant items, managing calendar scheduling across time zones, and completing multi-step research workflows. On launch, it integrates natively with the full Google Workspace suite. Support for third-party applications via the Model Context Protocol (MCP) is arriving in weeks.

The rollout follows a cautious path. Trusted testers gain access starting this week; the full beta opens to Google AI Ultra subscribers in the United States next week. Google has not yet committed to a global availability date.

The philosophical bet is significant. Google is asserting that the next battleground in consumer AI is not conversational quality — it is persistence. An agent that keeps working while you are asleep or in meetings is fundamentally a different product category than a chatbot, even a very good one.

## Gemini Omni: Video as a First-Class Input and Output

Google also launched Gemini Omni, described internally as a "world model" rather than a video generator. The distinction matters. Omni does not just produce videos from text prompts — it natively ingests video, audio, and text simultaneously, enabling conversational editing of complex multi-modal outputs across long, multi-step sessions. Google is framing it as the model that can understand a video as well as it can generate one.

Gemini Omni Flash (the consumer-facing tier) is live today for paid Gemini users and is rolling out for free in YouTube Shorts and YouTube Create this week. API access is coming in the following weeks for developers who want to build on top of it.

The timing is notable given that this follows the pre-I/O leak of Omni specifications that circulated in mid-May. The actual product landed largely as the leak predicted, suggesting Google's internal information security remains a challenge — but also that the product is substantive enough to withstand the scrutiny of advance disclosure.

## AI Ultra at $100/Month: Google's Premium Tier

The subscription landscape also shifted. Google unveiled AI Ultra at $100 per month, replacing the previous AI One and AI Premium tiers with a cleaner two-tier structure. AI Ultra includes 5× higher usage limits on all Gemini products compared to the $20 AI Pro tier, 20 terabytes of Google One cloud storage, YouTube Premium, and beta access to Gemini Spark.

This puts Google in direct competition with OpenAI's $200/month ChatGPT Pro and Anthropic's own enterprise offerings. At half the price of ChatGPT Pro, Google is signaling that it can afford to subsidize premium AI access at scale — a structural advantage of running the world's largest cloud and search businesses alongside its AI division.

## Managed Agents API: The Developer Play

For developers, the most technically significant announcement may have been the Managed Agents API in the Gemini API. A single API call provisions a remote Linux environment where an agent can reason, plan, call tools using Antigravity, execute code, manage files in an isolated sandbox, and browse the web for live data. Google is positioning this as the infrastructure layer that eliminates the boilerplate of building agentic applications.

Developers can extend the base agent with custom instructions and skills defined in markdown files — an `AGENTS.md` for instructions and `SKILL.md` for capabilities — and register them as named agents. The approach borrows deliberately from the conventions that have emerged in the open-source agent ecosystem over the past year.

Google also announced the Build with Gemini XPRIZE Hackathon, a global competition with a $2 million prize pool — the largest in hackathon history — inviting developers to build applications using the new APIs.

## The Competitive Calculus

Executives at Google, OpenAI, and Anthropic are increasingly describing the frontier race as neck-and-neck, with each company making different tradeoffs around cost, speed, and compute. Google's I/O announcements represent a bet that being simultaneously the cheapest production model and the most deeply integrated into consumer products is a durable competitive position — regardless of who can claim the top score on any given benchmark.

The real test begins now. Gemini Spark will be judged by whether it actually completes the tasks users assign it without supervision. Gemini Omni will be judged by its video quality against Sora, Runway, and Kling. And Gemini 3.5 Flash will be judged by whether developers actually reach for it when they are building the next generation of AI applications.

Google has assembled the pieces. Whether the sum is greater than its parts depends on execution — a quality that has historically been Google's Achilles heel in consumer AI.
