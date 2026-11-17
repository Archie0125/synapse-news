---
title: "DeepSeek Releases V4 Preview With Huawei Chip Support as U.S. Alleges AI Copying"
summary: "China's DeepSeek released a preview of its V4 model, which it says was trained on Huawei's Ascend processors, at far lower prices than Western rivals. The release came a day after a White House adviser alleged Chinese developers run industrial-scale campaigns to copy U.S. technology."
category: "ai-ml"
publishedAt: 2026-06-21
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: true
trending: true
sources:
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseek-launches-1-6-trillion-parameter-v4-on-huawei-chips-as-us-escalates-ai-theft-accusations"
  - name: "Fortune"
    url: "https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/"
  - name: "South China Morning Post"
    url: "https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency"
  - name: "Tom's Hardware (Huawei post-training)"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-led-team-claims-it-post-trained-deepseeks-1-6-trillion-parameter-models-on-ascend-910c-chips"
tags:
  - "deepseek"
  - "huawei"
  - "china-ai"
  - "llm"
  - "export-controls"
relatedSlugs:
  - "2026-06-17-deepseek-74b-first-funding-tencent-catl-50b-en"
  - "2026-06-06-us-chip-ban-chinese-overseas-subsidiaries-en"
---

# DeepSeek Releases V4 Preview With Huawei Chip Support as U.S. Alleges AI Copying

DeepSeek, the Hangzhou-based AI startup owned by the Chinese hedge fund High-Flyer, has released a preview of its newest model, with V4-Pro at 1.6 trillion parameters. DeepSeek said it used Huawei's Ascend AI processors to train the model. The release, a preview launched on a Friday, comes more than a year after DeepSeek's V3 and R1 models shook markets.

The timing is no accident. Washington has ramped up pressure at the same time: on Thursday, Michael Kratsios, science and technology adviser to President Trump, alleged that Chinese AI developers were engaged in "industrial-scale campaigns" to copy U.S. technology. Beijing's foreign ministry dismissed the characterizations as "groundless."

## What the Model Actually Does

V4-Pro is enormous: 1.6 trillion total parameters across 256 experts, activating approximately 37 billion at inference time. In raw parameter count, that places it alongside GPT-5.4 and Gemini 3.1 Pro. DeepSeek's own technical report says V4 "falls marginally short of GPT-5.4 and Gemini 3.1 Pro," suggesting a trajectory that trails state-of-the-art frontier models by approximately three to six months.

A companion model, V4-Flash, delivers a 284 billion-parameter variant at dramatically lower cost, targeting latency-sensitive applications where the full flagship would be impractical.

The 1 million-token context window is V4's other headline capability. At a moment when context length has become a primary competitive axis—Gemini 3.5 Pro recently expanded to 2 million tokens, and Anthropic's Mythos models offer comparably long windows—V4's context capability keeps it within striking range of leading Western alternatives.

## The Price Weapon

DeepSeek's most disruptive contribution has never been raw capability alone. It is price. V4-Pro enters at $3.48 per million output tokens. OpenAI's comparable tier runs at $30 per million; Anthropic charges $25. That is roughly an 8-to-10x cost difference for models with substantially overlapping practical utility. V4-Flash at $0.28 per million output tokens undercuts even the leanest Western mini-models.

DeepSeek expects to lower V4-Pro prices later in the year as Huawei scales up production of its new Ascend 950 AI processors.

Financial markets responded accordingly. SMIC, the Chinese foundry manufacturing Huawei's Ascend chips, saw shares jump 10% on the announcement. Rival Chinese AI firms MiniMax and Knowledge Atlas each fell over 9%, as investors recalculated the competitive landscape.

## The Huawei Silicon Story

The technically significant aspect of V4 is the chip stack. Until now, training large frontier models outside the Nvidia H100/H200/GB200 supply chain was considered largely theoretical. V4 appears to have changed that calculus.

A research group that includes Huawei Technologies demonstrated full-parameter post-training of V4-Pro using a cluster of at least 1,000 Huawei Ascend 910C chips—a significant engineering achievement in cluster coordination at that scale. Huawei announced that its Ascend processors would offer "full support" for DeepSeek's models.

The implication is geopolitically significant: China now has at least one domestic model-training stack capable of producing frontier-adjacent results without any Nvidia involvement. That was not assumed to be possible when the Biden administration imposed its first export controls in October 2022.

Huawei is projecting $12 billion in AI chip revenue for 2026 as domestic demand absorbs the orders that would otherwise have gone to Nvidia. The American company's market share in China has effectively reached zero since the most recent export control tightening.

## The Intellectual Property Dimension

The release came a day after U.S. officials made new allegations of IP copying by Chinese AI developers. The specific claims center on model distillation—training a student model to mimic a more capable teacher model's outputs—which government documents allege Chinese labs pursued at "industrial scale" using API access to American frontier models before export restrictions closed that pathway.

DeepSeek's early V2 and V3 releases sparked similar accusations, particularly after analysis of V3's outputs showed response patterns some researchers attributed to distillation from GPT-4 and Claude 3 family models. DeepSeek denied those characterizations.

V4 provides a partial answer to those allegations: because it was trained from scratch on Huawei hardware without RLHF feedback from American model APIs, the distillation attack surface simply did not exist in the same form. Whether that fully satisfies U.S. government concerns is unclear, given broader allegations about architectural and data theft that go beyond API-based distillation techniques.

## Enterprise and Developer Implications

For enterprises and developers operating outside the U.S. export control regime, V4 represents a genuine competitive alternative. The combination of long context, competitive benchmark performance, and sub-$4 pricing for the flagship tier creates a compelling proposition for high-volume inference applications—document analysis, code review, RAG pipelines—where Western frontier model costs become prohibitive at scale.

V4's Huawei-native architecture does create certain limitations. Deployments in cloud environments that depend on Nvidia-optimized toolchains—CUDA kernels, TensorRT, most mainstream MLOps platforms—require adaptation. DeepSeek has released Ascend-specific documentation and a compatibility layer, but developer tooling remains less mature than the Nvidia ecosystem it competes against.

For organizations in China or in markets less constrained by U.S. technology policy, those friction points are likely to recede quickly as the ecosystem develops. The question is how quickly this alternative technology stack will percolate into global enterprise procurement decisions.

## A Geopolitical Inflection Point

The release lands in a context where U.S. chip controls are being stretched in both directions. The Trump administration tightened restrictions further in June 2026, expanding the ban to overseas Chinese-owned subsidiaries. At the same time, V4's launch demonstrates that those controls have not frozen Chinese AI capability—they have redirected it toward indigenous hardware.

"We're no longer in a world where you can assume that AI progress is contingent on access to Nvidia chips," said one industry analyst briefed on the V4 architecture. "That assumption was the foundation of the export control strategy."

Whether V4 represents a durable capability crossing or a high-water mark that Chinese labs will struggle to maintain without continued access to Western research outputs remains genuinely contested. What is no longer contested is that Huawei's Ascend platform is a serious training substrate for frontier-scale models.

The next six months—as Ascend 950 production scales and V4 gets deployed across enterprise customers—will determine whether this moment represents a lasting strategic shift in the global AI balance or a demonstration that outpaces the underlying supply chain's capacity to sustain it.

*Correction (November 15, 2026): 10 sentences were corrected or removed to match the sources listed on this page.*
