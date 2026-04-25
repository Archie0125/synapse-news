---
title: "Tencent Launches Hy3 Preview: A 295B-Parameter MoE Model Built in Under 90 Days"
summary: "Tencent's Hunyuan team has released Hy3 Preview, a 295-billion-parameter mixture-of-experts model trained from scratch in under three months. The open-source model achieves 74.4% on SWE-bench Verified, offers a 256K token context window, and claims a 40% inference efficiency improvement — signaling a serious recalibration of Tencent's AI ambitions under new leadership."
category: "ai-ml"
publishedAt: 2026-04-25
lang: "en"
featured: false
trending: true
sources:
  - name: "Dataconomy"
    url: "https://dataconomy.com/2026/04/24/tencent-uses-product-rollout-not-just-benchmarks-to-define-hy3-preview/"
  - name: "South China Morning Post"
    url: "https://www.scmp.com/tech/big-tech/article/3351101/tencent-unveils-first-flagship-ai-model-former-openai-researcher-helm"
  - name: "Cybernews"
    url: "https://cybernews.com/ai-news/tencent-ai-model-openai-alum/"
  - name: "GIGAZINE"
    url: "https://gigazine.net/gsc_news/en/20260424-tencent-hy3/"
  - name: "Caixin Global"
    url: "https://www.caixinglobal.com/2026-04-23/tencent-unveils-new-ai-model-to-close-gap-with-rivals-102437241.html"
tags:
  - "Tencent"
  - "Hy3"
  - "Hunyuan"
  - "mixture-of-experts"
  - "open-source LLM"
  - "China AI"
  - "SWE-bench"
relatedSlugs:
  - "2026-04-06-deepseek-v4-huawei-chips-en"
  - "2026-04-13-google-gemma-4-open-model-apache-en"
  - "2026-04-12-zai-glm51-open-source-swe-bench-en"
---

Tencent has released Hy3 Preview, the first major AI model to emerge from the company's overhauled Hunyuan team following a sweeping leadership change earlier this year. The model — a mixture-of-experts architecture with 295 billion total parameters and 21 billion active parameters per forward pass — was trained from a cold start in late January and shipped on April 23, a development cycle of under 90 days that is itself a statement about where the Chinese tech industry has arrived on AI model development velocity.

The release is significant on multiple dimensions: technical, competitive, and symbolic. For Tencent specifically, it represents the first credible evidence that the company's AI reorganization has moved from announcement to output. For the broader open-source ecosystem, it introduces a capable Chinese-origin model that challenges the narrative that only Western labs or DeepSeek can produce frontier-quality open weights.

## Technical Specifications

Hy3 Preview is built on a sparse MoE architecture in which only 21 billion of its 295 billion parameters are activated during inference on any given token. This design dramatically reduces the computational cost per forward pass relative to a dense model of equivalent parameter count, which is how Tencent achieves what it claims is a 40% improvement in inference efficiency compared to its predecessor Hunyuan models.

The model supports a 256,000-token context window — equivalent to roughly 200,000 words, or a long novel — which places it among the handful of frontier models capable of processing entire codebases, lengthy legal documents, or extended research corpora as a single prompt. This capability is increasingly important for enterprise customers building multi-step agentic workflows that require models to maintain state across long interaction sequences.

On SWE-bench Verified, the standard benchmark for evaluating a model's ability to resolve real-world software engineering issues from GitHub, Hy3 Preview scores 74.4%. For reference, Claude Opus 4.6 sits at 80.8% on the same benchmark, while GPT-5.5 has reported figures in a comparable range. Hy3 Preview's score places it firmly within striking distance of the Western frontier, a remarkable outcome for a model completed in under three months.

The Tencent team describes the architecture as "fast-and-slow-thinking fused" — meaning it integrates both rapid, pattern-matching inference (similar to chain-of-thought shortcuts) and slower, deliberate reasoning into a unified model, rather than requiring the user or application layer to switch between modes.

## New Leadership, New Direction

The speed and quality of Hy3 Preview's development are inseparable from the leadership restructuring that preceded it. Tencent's previous AI efforts were spread across multiple competing internal teams, resulting in duplicated effort and slower iteration cycles. In early 2026, the company consolidated AI research under a new lead who previously worked at OpenAI — a hire that followed a broader pattern of Chinese tech companies recruiting Western AI talent as export controls tightened access to frontier model weights.

The new leadership brought with it a different philosophy: prioritize deployment integration over benchmark-chasing, and measure model quality through product usage rather than leaderboard position. Hy3 Preview launched not as a research artifact but as a production model immediately integrated into more than ten Tencent products, including Yuanbao (the company's consumer AI assistant), WeChat, and QQ.

This product-first approach is evident in how Tencent is pricing and positioning the model. Through its TokenHub API platform, Hy3 Preview is available at RMB 1.2 per million input tokens and RMB 4 per million output tokens — pricing that undercuts most Western alternatives and signals that Tencent intends to compete on value as well as capability.

## Open-Source Strategy and Competitive Positioning

Hy3 Preview is open-source, released with weights available on Hugging Face under a permissive license. This is a deliberate strategic choice. By open-sourcing the model, Tencent participates in an ecosystem dynamic that DeepSeek pioneered: driving adoption through openness, building developer familiarity with the model's behavior and strengths, and positioning the weights as an infrastructure layer that third-party companies can fine-tune for specific domains.

The model enters an increasingly crowded open-source frontier field. DeepSeek's V4 series, released last week, currently leads on many benchmarks and has a head start in developer mindshare. Meta's Llama models remain the most widely deployed open weights globally. Google's Gemma 4 family provides a strong lightweight option. Hy3 Preview differentiates on two vectors: its enterprise-oriented context length and the specific inference efficiency claims that make it economically viable to run at scale without the cost structure of a dense model.

The timing is also notable. Tencent chose to release during a week dominated by DeepSeek V4 coverage and the Google-Anthropic investment story — a decision that either reflects confidence in the model's ability to stand on its own merits, or reflects the compressed timelines of competitive AI development where release windows are dictated by training completion rather than market timing.

## Integration Into Tencent's Product Ecosystem

Perhaps more interesting than the benchmark results is the speed of product integration. Hy3 Preview is already powering Yuanbao, Tencent's consumer AI assistant that competes with Baidu's Ernie Bot and Alibaba's Tongyi Qianwen in the Chinese market. Given WeChat's scale — the platform has more than 1.3 billion monthly active users — even a marginal improvement in AI-powered features driven by a more capable underlying model represents a meaningful user experience change at population scale.

The integration into WeChat and QQ also positions Hy3 Preview as a social-context AI model, trained and deployed in an environment where conversational nuance, tone matching, and cultural fluency matter more than raw coding performance. Tencent's SWE-bench results are competitive, but the more defensible differentiation may ultimately be how well the model handles the Chinese language contexts, humor registers, and conversational patterns that dominate its home platforms.

## Implications for the Open-Source Frontier

Hy3 Preview's release continues a trend that has defined early 2026: the gap between open-weight and proprietary frontier models is narrowing faster than most observers predicted. A model scoring 74.4% on SWE-bench, available for free download with commercial-use rights and priced competitively via API, meaningfully expands the options available to enterprises and developers who cannot or choose not to depend on OpenAI or Anthropic.

For developers building AI-native applications in markets where data sovereignty matters — Southeast Asia, the Middle East, parts of Europe — a Chinese-origin open model from a company with Tencent's infrastructure scale is a credible option in a way that models from the prior generation were not. Whether Hy3 Preview builds the international developer community that DeepSeek has cultivated remains to be seen, but the foundation is now clearly present.
