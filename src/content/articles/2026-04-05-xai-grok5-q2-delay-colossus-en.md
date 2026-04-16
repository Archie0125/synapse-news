---
title: "Grok 5 Misses Q1 Deadline as xAI Scales Colossus 2 to 1.5 Gigawatts"
summary: "xAI's Grok 5, a reported 6-trillion-parameter Mixture-of-Experts model, slipped past its Q1 2026 launch window and is now targeting Q2. Meanwhile, Elon Musk confirmed that the Colossus 2 supercluster in Memphis is expanding from 1 gigawatt to 1.5 gigawatts by April to support fine-tuning and inference at scale."
category: "ai-ml"
publishedAt: 2026-04-05T10:40:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "NxCode"
    url: "https://www.nxcode.io/resources/news/grok-5-release-date-latest-news-2026"
  - name: "Zelili"
    url: "https://zelili.com/news/grok-5-expected-in-early-2026/"
  - name: "Y Build"
    url: "https://ybuild.ai/en/blog/grok-5-xai-6-trillion-parameters-what-to-expect-2026"
  - name: "xAI"
    url: "https://x.ai/news"
tags:
  - "xAI"
  - "Grok 5"
  - "Colossus 2"
  - "Elon Musk"
  - "LLM"
  - "MoE"
  - "AI infrastructure"
relatedSlugs:
  - "2026-04-04-open-source-llm-race-en"
  - "2026-04-05-deepseek-v4-imminent-launch-en"
  - "2026-04-05-anthropic-claude-mythos-en"
---

When Elon Musk confirmed in early 2026 that Grok 5 would ship in Q1, it joined a growing list of model launches where ambition outpaced schedule. Q1 ended on March 31 with Grok 5 nowhere in sight. Now xAI's flagship model is targeting Q2 — and the company has been conspicuously quiet about exactly when "Q2" means.

The delay matters beyond the usual spectator sport of AI release date forecasting. Grok 5 is the model xAI has staked its competitive position on: a reported 6-trillion-parameter Mixture-of-Experts architecture that would, if the numbers hold, be the largest model by parameter count ever made publicly accessible. For context, GPT-4o is estimated at around 200 billion parameters; Meta's Llama 4 Scout uses 109 billion active parameters within a 400 billion total MoE frame. A 6-trillion-parameter model is an entirely different category of infrastructure challenge.

## Why the Delay

xAI has not published an official explanation for the slip, but sources familiar with the company's technical operations point to two interconnected factors: training stability at previously untested parameter scales, and a supercluster expansion that was completed later than planned.

Training a 6T-parameter model is not simply a larger version of training a smaller one. The engineering challenges grow non-linearly with scale — failure modes like loss spikes, checkpoint instability, and gradient flow problems become harder to diagnose and fix when the model requires hundreds of thousands of GPU-hours to restart from scratch. Industry sources suggest xAI encountered at least one major training instability in January that required backtracking and additional tuning of the MoE routing architecture.

Colossus 2, the xAI supercluster at a Memphis, Tennessee data center, is the physical substrate for Grok 5's training. Musk confirmed that the facility has been expanding from its initial 1-gigawatt power footprint toward 1.5 gigawatts — a 50% increase in compute capacity. The additional power capacity is primarily targeted at supporting fine-tuning and inference at scale once Grok 5's primary training run completes, rather than accelerating the training run itself. That sequencing suggests xAI is more focused on getting Grok 5 right than getting it out fast.

## The Scale Question

The 6-trillion-parameter figure, which has circulated in analyst briefings and leaked roadmap summaries, needs context. In a Mixture-of-Experts architecture, not all parameters are active during any given inference pass. MoE models route each input token to a subset of "expert" sub-networks, activating perhaps 10–15% of total parameters per token. This means a 6T-parameter MoE model might have active parameter counts closer to 600 billion to 900 billion — still enormous, but a different performance and cost profile than the raw number suggests.

The MoE architecture was also a key factor in Grok 3's competitive showing earlier in 2026. Grok 3's benchmark results on coding, mathematics, and long-context reasoning were notably strong relative to its reported compute cost, which observers attributed to the efficiency advantages of its MoE design. Grok 5 appears to be pushing the same architectural philosophy to an extreme — prioritizing raw parameter density while using MoE routing to keep inference costs manageable.

## Colossus 2: The Infrastructure Play

The Memphis supercluster represents one of the most aggressive datacenter buildouts in AI history. The first phase came online in late 2024 with an initial 100,000 Nvidia H100 GPUs and a 200-megawatt power footprint; subsequent expansions brought it to 1 gigawatt, making it one of the largest purpose-built AI compute facilities in the world. The current expansion to 1.5 gigawatts will put it in a class with only a handful of hyperscaler facilities globally.

For xAI, Colossus 2 is more than a training facility — it's a statement about the company's long-term commitment to vertical integration. Unlike Anthropic and OpenAI, which rent compute from Microsoft Azure and Google Cloud respectively, xAI owns its primary training and inference infrastructure. This gives xAI tighter control over training runs, lower inference costs at scale, and a negotiating position independent of cloud hyperscalers. It also means that when something goes wrong at Colossus 2 — a power outage, a hardware failure, a training instability — there's no vendor support escalation path. The engineering challenges are entirely internal.

The expanded 1.5GW capacity is reportedly also intended to support xAI's growing commercial API business. Grok 4.20 Beta 2, the current public flagship, has accumulated significant enterprise customers who use it through xAI's API for reasoning-intensive tasks. Once Grok 5 launches, xAI will need the inference capacity to serve both research and commercial workloads simultaneously — hence the front-loaded infrastructure investment.

## Competitive Dynamics

The Grok 5 delay has given competitors breathing room. At the end of Q1 2026, the frontier model landscape looks like this: GPT-5.4 (OpenAI) leads on agentic task benchmarks with a 1-million-token context window; Anthropic's Claude Mythos is in internal testing with reported "step change" capabilities; Google's Gemini 3.1 Pro holds strong on multimodal tasks; and DeepSeek V4, expected in the coming weeks, threatens to disrupt pricing benchmarks from the Chinese side.

Grok 5's delay means xAI has no new frontier model on the market while every major competitor is either releasing or previewing next-generation capabilities. The current Grok 4.20 Beta 2 is competitive in some benchmarks but was never intended to hold the line against GPT-5-class models. Every week the delay extends, xAI risks losing enterprise API customers to competitors who are actively shipping improvements.

Prediction markets currently assign roughly 33% probability that Grok 5 ships before June 30, 2026. The same markets had been at 70%+ for a Q1 ship date just two months ago.

## The Stakes for xAI

Beyond the competitive optics, the Grok 5 delay tests xAI's narrative in a specific way. The company has positioned itself as the most technically ambitious lab — the one willing to bet on scales and architectures that others consider premature. The 6T parameter bet was a visible expression of that ambition. If Grok 5 delivers on its reported capabilities when it eventually ships — strong performance on hard science and mathematics, extended reasoning chains, competitive cost-per-token — the delay will be forgotten quickly. If it arrives substantially underperforming expectations despite the hardware investment, the narrative becomes significantly harder to sustain.

For now, the company is focused on getting the training run right. The infrastructure is expanding. The current models are holding paying customers. And Musk has been — unusually — restrained in public promises about the timeline. That restraint, more than anything else, may be the most accurate signal about where things actually stand inside Colossus 2.
