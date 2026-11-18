---
title: 'Microsoft''s MAI Code 2 Is a Price War Pitch: 96% of Claude Opus 5.5 at 5% of the Cost'
summary: At Ignite, Microsoft launched seven MAI models led by MAI Code 2, which it says delivers 96% of Claude Opus 5.5's performance on 4 coding benchmarks at 5% of the price. These are Microsoft's own numbers, and they come with conditions.
category: ai-ml
publishedAt: '2026-11-18T14:02:26Z'
lang: en
type: news
safeForPublic: true
featured: false
trending: false
sources:
- name: Microsoft AI
  url: https://microsoft.ai/news/microsoft-ignite-2026/
- name: Microsoft AI
  url: https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/
- name: Interesting Engineering
  url: https://interestingengineering.com/ai-robotics/microsoft-seven-mai-models-launch
- name: Dataconomy Media
  url: https://dataconomy.com/2026/11/18/microsoft-unveils-cheaper-ai-models-to-challenge-openai/
tags:
- Microsoft
- MAI Code 2
- GitHub Copilot
- Anthropic
- OpenAI
- Azure
- AI pricing
relatedSlugs:
- 2026-11-16-hugging-face-and-openrouter-join-forces-to-make-open-weight-en
- 2026-11-15-cohere-finding-shows-self-hosted-open-weight-models-still-ne-en
- 2026-11-13-the-agent-wars-are-really-about-who-owns-the-customer-en
---

Microsoft says MAI Code 2 delivers 96% of Claude Opus 5.5's performance at 5% of the price. Against OpenAI the gap is smaller but still large: 98% of GPT-6.1 Sol's performance at 40% of the price.

MAI Code 2 leads a group of 7 models that Microsoft announced on November 17. The rest cover cybersecurity, image editing, real-time speech, medical transcription and model routing. The common thread is cost. Microsoft's argument is that token spend is climbing fast and customers want models cheap enough to run agents around the clock.

## The coding numbers

Microsoft averaged the Code 2 results across 4 benchmarks it says reflect everyday enterprise coding in GitHub Copilot: DeepSWE 1.1, Terminal Bench 2.1, SWE-Atlas and FrontierCode v1.1. In blind evaluations of frontend work, reviewers chose MAI Code 2's output over GPT-6 Sol's 64% of the time.

The lighter MAI Code 2 Flash is meant for code explanations, targeted edits and routine fixes. Microsoft says it performs comparably to GPT-6 Luna at 65% of the cost and to Claude Haiku 5.5 at 20%.

Distribution is already in place. MAI Code 2 is available in GitHub Copilot's Pro, Pro+, Max, Business and Enterprise plans, and Code 2 Flash also reaches Free and Student users. Code 2 Flash is in limited-access preview in Microsoft Foundry.

## The fine print

Microsoft is open about the limits. The company says the 2 coding models have not yet been tuned for harder work such as fundamental science research or agentic tasks that run over very long horizons. It also says the performance and cost comparisons depend on workload, model configuration, reasoning effort and pricing assumptions.

All of the comparison figures are Microsoft's own claims. One of them already conflicts with an outside report. Microsoft calls MAI Image 2.7 the world's best image editing model and says it holds the #1 spot on Artificial Analysis, ahead of GPT Image 2.6 Sunburst (max) at one fifth of the price. Dataconomy reported that Artificial Analysis ranked the model second on its AA-Image-Editing v2.1 leaderboard, at 1,193 Elo behind GPT Image 2.5 Sunburst at 1,199, and third on the Arena Edit leaderboard. The two may describe different points in time, since Dataconomy says the model went out as a preview on Oct. 27. Still, it shows why these rankings deserve a second look.

## Security, images, speech and routing

- **MAI Cyber 2 Flash** is built for continuous defensive security work, including patching live production systems. On the CyberGymE2E benchmark, Microsoft claims it equals GPT-6 Astra while costing under 2% as much per task. Output tokens are priced 86% below MAI Cyber 1.1 Flash. Access is limited to a small group of customers.
- **MAI Image 2.7 Flash** handles high-volume image generation at about $10 per 1,000 images.
- **MAI Realtime 1** is Microsoft's first speech-to-speech model and starts at $0.01 per audio minute. In Microsoft's own testing it beat GPT-Realtime 2.1.
- **Dragon Copilot Transcribe** runs on MAI-Transcribe-2. Microsoft says it handles 10 million encounters monthly, cuts multilingual error rates in half and has reached a third of US physicians.
- **Decision 1.1** sends work to larger, more expensive models only when a task needs them. Microsoft says it has 4,000 customers and is 50x faster and 79x cheaper than GPT-Sol 6.1.

Microsoft is presenting the models as specialists for particular workloads, not one system that does everything.

## "Your weights," on Azure

Microsoft also introduced MAI Licensed Weights. Customers can customise a MAI model with their own data and run it in their own Azure environment. Mustafa Suleyman, who leads Microsoft AI, said licensing depends on the models being deployed within Azure. Microsoft's example is AT&T, which built a custom MAI model for 5G network analytics that Microsoft says beat GPT-6.1 Sol at 50x lower cost.

Microsoft says customers decide who can access the model and that their data and adaptations remain theirs. Microsoft's pitch openly questions whether open weights can be trusted.

Microsoft is also using these models across its own products. A model derived from Code 2 Flash, MAI Work Flash, now serves products across M365 and Fabric IQ. Microsoft also highlighted its in-house accelerator, Maia 200, which runs its largest models in production and, by the company's account, gets up to 1.7 times as many tokens per watt as leading GPU hardware.

Suleyman also made clear this lineup is not the end goal: "My team is building true superintelligence," he said, without giving a launch date for a general-purpose frontier model. Of the specialist approach, Suleyman said it is "not a flash in the pan".

## What to Watch

- Whether Code 2 Flash arrives on Open Router, Vercel, Hermes, Open Code and Kilo as promised, where developers can price it against rivals directly.
- Whether MAI Cyber 2 Flash expands beyond its small group of customers.
- Where MAI Image 2.7 settles on the Artificial Analysis editing leaderboard compared with Microsoft's #1 claim.
- Any launch date for Suleyman's general-purpose frontier model.

---

*This article was written by AI from the sources listed on this page. Figures, names and quotes were checked against those sources by software before publishing.*
