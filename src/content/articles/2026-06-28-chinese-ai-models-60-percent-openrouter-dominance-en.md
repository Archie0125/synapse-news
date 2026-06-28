---
title: "Chinese AI Models Now Own 61% of Global API Traffic—Up From Under 2% Eighteen Months Ago"
summary: "Chinese open-weight AI models—led by Xiaomi's MiMo, DeepSeek, Kimi, MiniMax, and Zhipu's GLM series—now account for roughly 61% of all tokens processed through OpenRouter, the world's largest AI model routing platform, up from under 2% at the start of 2025. With prices 12x below GPT-5.5 on comparable tasks and benchmark performance that now matches Western frontier models on coding and reasoning, the shift represents a structural change in who controls the operational layer of global AI infrastructure."
category: "industry"
publishedAt: 2026-06-28
lang: "en"
featured: false
trending: true
sources:
  - name: "Data Gravity"
    url: "https://www.datagravity.dev/p/chinas-open-weight-takeover"
  - name: "ChatForest"
    url: "https://chatforest.com/reviews/chinese-ai-models-openrouter-dominance-deepseek-kimi-minimax-glm-2026/"
  - name: "StockAlarm Pro"
    url: "https://pro.stockalarm.io/blog/openrouter-llm-rankings-investor-analysis"
  - name: "BenchLM AI"
    url: "https://benchlm.ai/blog/posts/best-chinese-llm"
tags:
  - "Chinese AI"
  - "DeepSeek"
  - "MiniMax"
  - "Kimi"
  - "OpenRouter"
  - "open-weight"
  - "market share"
  - "AI competition"
relatedSlugs:
  - "2026-06-27-deepseek-v4-pro-permanent-price-cut-en"
  - "2026-06-23-glm-52-zhipu-beats-gpt55-open-weight-en"
  - "2026-06-14-moonshot-kimi-k2-7-code-open-source-coding-model-en"
---

Eighteen months ago, Meta's Llama was the undisputed king of open-weight AI. Developers who wanted a capable model they could run, modify, or deploy without per-token licensing costs defaulted to Llama almost reflexively. Chinese models were an afterthought—interesting curiosities at academic conferences, occasionally cited in benchmark papers, but not serious contenders for production workloads.

Today, Llama has fallen below 1% of routed token volume on OpenRouter. Chinese models account for approximately **61% of all tokens** processed through the platform. Four of the five most-used models by volume are Chinese-origin. The reordering of the open-weight AI market from American-dominated to Chinese-dominated happened in roughly five quarters, and most of the industry missed the scale of the shift while it was happening.

## The Numbers

OpenRouter's processed traffic is one of the clearest windows into how AI developers actually use models in production, because it aggregates demand across thousands of applications and surfaces usage patterns that individual platform dashboards obscure.

The picture that emerges for mid-2026 is stark. **Xiaomi's MiMo** leads all models at approximately 21% of routed tokens, with outsized strength in coding workloads at roughly 22% of coding-specific traffic. **DeepSeek** holds approximately 17.6% of routed volume, which puts it ahead of every American lab individually—including Anthropic (15.4%) and well above Google and OpenAI, which together occupy single-digit shares of routed traffic.

MiniMax M2.5 processes approximately 4.55 trillion tokens monthly. Kimi K2.6 from Moonshot AI follows at roughly 4.02 trillion monthly tokens and leads on coding benchmarks among Chinese models. Zhipu's GLM-5.1 posts strong results on AIME mathematics benchmarks and SWE-Bench Pro.

The aggregate: Chinese-origin companies collectively hold roughly 61% of identified token volume on the platform, up from under 2% at the start of 2025. That 30x growth in eighteen months has no close precedent in recent technology market history.

## What Actually Drove the Shift

The surface explanation—"Chinese models are cheap"—is correct but incomplete. Price is the proximate cause; three structural forces created the conditions.

**The workload composition changed.** Programming-related tasks grew from approximately 11% of OpenRouter traffic in 2024 to over 50% in mid-2026. Chinese models—particularly DeepSeek, Kimi, and MiniMax—were trained with heavy emphasis on code generation and debugging, and they disproportionately capture the coding workload that now dominates the platform. If the mix had stayed at 11% coding, the market share picture would look different.

**Open weights became a distribution strategy, not a research posture.** Alibaba Cloud's Qwen series has surpassed 1 billion downloads on Hugging Face, anchoring over 200,000 derivative Qwen-tagged models. DeepSeek releases weights; Kimi K2.6 is fully open-weight. The strategy is not altruistic—open weights function as customer acquisition for Chinese cloud platforms (Alibaba Cloud, ByteDance's Volcano Engine) in the same way that free services reduce barriers to paid product adoption. Every developer who builds on an open-weight Chinese model is a warm lead for the cloud infrastructure that runs it at scale.

**The price wedge is structural, not promotional.** DeepSeek V4-Pro, following its permanent 75% price cut in June, is priced at approximately $0.44 input / $0.87 output per million tokens. GPT-5.5, at comparable task performance for many professional use cases, costs $2.50 / $15. That is roughly 12x the input cost and 17x the output cost. The gap is not a temporary promotional maneuver designed to buy market share—it reflects genuine cost structure differences that emerge from the relative economics of training and serving in China versus the United States.

## The January 2025 Miscalculation

When DeepSeek-R1 launched in January 2025 and demonstrated that a Chinese lab had matched Western reasoning quality at a fraction of the training cost, the dominant reaction in American financial markets was panic about chip demand collapse. If AI models could be trained more efficiently, the reasoning went, perhaps the enormous capital investment in Nvidia GPUs and data center infrastructure would prove unnecessary.

That prediction was wrong in an instructive way.

Cheaper intelligence did not reduce total compute consumption—it expanded it. As the cost per capable AI interaction fell, the number of applications deploying AI at scale increased dramatically. OpenRouter's weekly token volume grew from approximately 5 trillion tokens per week in April 2025 to over 20 trillion tokens per week by April 2026—a 4x increase driven in large part by the proliferation of cheap inference enabled by Chinese open-weight models. Nvidia's market capitalization reached $5.14 trillion in mid-2026, up roughly 50% year-over-year, as the semiconductor that runs inference at scale became more in demand, not less.

The disruption landed not on semiconductor demand but on model-vendor market share. The companies that lost were not the GPU makers—they were the proprietary closed-weight labs that had previously charged premium rates for capabilities now available open-weight at 10-12x lower cost.

## Where the American Advantage Remains

The Chinese open-weight takeover of the operational layer does not mean American labs have lost the AI race. The picture is more granular than that, and the distinctions matter for policy and strategy.

Frontier capability is still set by American labs. GPT-5.6 Sol, now in limited preview, represents capabilities that no Chinese open-weight model has matched at the highest reasoning tiers. Anthropic's Fable 5 series, despite export restrictions that limit deployment in some markets, achieved benchmark results that established a ceiling the Chinese models have approached but not fully cleared. The premium enterprise revenue for frontier reasoning tasks continues to flow largely to OpenAI and Anthropic.

But the premium tier is a narrow slice of total volume. The analysis from Data Gravity captures it precisely: "The frontier is no longer where the volume is. Premium reasoning is a 15-point niche; the cheap, open, good-enough tier is the market—and it is overwhelmingly Chinese."

This matters for different constituencies in different ways. For venture capital returns, the profitable frontier still belongs to American companies. For government technology security, the models running the majority of global developer workloads are not American. For enterprise procurement, the default open-weight option for cost-sensitive applications is now Chinese-origin. Each constituency needs to process that compound reality differently.

## The Infrastructure Layer as the Real Battleground

The most strategically important insight from the current market structure may be about where value accrues rather than who trains the best model.

The analysis that has emerged from studying the OpenRouter shift consistently points in the same direction: margin lives above and below the model, not in it. Pure-play model labs—whether American or Chinese—face structural pressure as the capability commodity layer commoditizes. The durable value in the stack is in distribution (ByteDance reaches consumers through TikTok and Douyin; Alibaba Cloud reaches enterprise through existing relationships), in inference infrastructure (Nvidia's H100 and H200 GPUs run the majority of Chinese model inference), and in memory.

High-bandwidth memory (HBM), which is the physical component that determines how fast tokens can flow through inference hardware, has become what analysts describe as "the single highest-leverage node in the entire stack." China's domestic HBM production capacity is capped near 250,000–300,000 high-end packages for 2026—a constraint that limits how much Chinese inference infrastructure can scale independently of Western memory suppliers like SK Hynix and Micron. American export controls on advanced memory chips may, paradoxically, be more effective at preserving competitive position than controls on model weights or training chips, because memory is harder to substitute.

## What Developers Should Do Now

For developers building AI applications in 2026, the practical implication of this market shift is straightforward: the Chinese open-weight models are production-ready, often competitive with Western frontier models on the tasks that dominate actual workloads, and dramatically cheaper to run. The cost structure advantages are real and persistent, not promotional.

The relevant cautions are also real. Data governance questions—who stores inference logs, where model telemetry flows, what the terms of service permit—are more complex for models backed by Chinese companies operating under Chinese data law. Enterprise applications handling sensitive customer data or regulated information need legal review of these questions before deployment at scale, regardless of the technical performance advantages.

The open-weight nature of models like DeepSeek V4 and Kimi K2.6 partially addresses this concern: an organization can run these models on its own infrastructure rather than through the Chinese lab's API, eliminating the data flow question. But running open-weight models at scale requires infrastructure expertise and compute investment that many organizations don't have in-house, which is why a significant fraction of the OpenRouter traffic to Chinese models flows through the Chinese labs' own APIs anyway.

The market structure is now set. Chinese models own the operational layer of global AI. The questions worth asking are not "how did this happen"—that story is written—but what it means for the development of AI capability, the geography of AI infrastructure investment, and the policy levers that might actually influence the trajectory from here.

The single fact worth holding onto: eighteen months ago, Llama dominated the open-weight world. Today it is below 1%. The speed of this transition is the most important data point about how quickly AI market structure can change—which means predictions about who controls the next layer of the stack in 2028 should be held with appropriate humility.
