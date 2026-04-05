---
title: "DeepSeek V4 Launch Imminent: 1 Trillion Parameters, Apache 2.0, $5.2M Training Cost"
summary: "DeepSeek's V4 model is reportedly weeks away from release, rewritten to run on Huawei Ascend chips rather than Nvidia hardware. Leaked benchmarks claim 80%+ on SWE-bench Verified and a $5.2 million training cost — figures that, if confirmed, would make it the most capable open-weights model ever released and deepen China's AI stack decoupling from US-controlled hardware."
category: "ai-ml"
publishedAt: 2026-04-05
lang: "en"
featured: false
trending: false
sources:
  - name: "The Information"
    url: "https://www.theinformation.com/articles/deepseek-v4-imminent-release-huawei-chips"
  - name: "Dataconomy"
    url: "https://dataconomy.com/2026/03/16/deepseek-v4-and-tencents-new-hunyuan-model-to-launch-in-april/"
  - name: "NxCode"
    url: "https://www.nxcode.io/resources/news/deepseek-v4-release-specs-benchmarks-2026"
tags:
  - "deepseek"
  - "open-source"
  - "china-ai"
  - "huawei"
  - "llm"
  - "apache-2.0"
relatedSlugs:
  - "2026-04-04-open-source-llm-race-en"
  - "2026-04-03-us-china-chip-war-en"
---

DeepSeek V4 is weeks away from release, according to a report from The Information published on April 3. The model represents a significant evolution from the V3 that shocked Western AI labs when it debuted in early 2025 — not just in capability, but in its hardware dependencies. The launch has been delayed by a deliberate rewrite of the inference stack to run natively on Huawei Ascend chips and Cambricon accelerators rather than Nvidia hardware, a change that signals an intentional strategic decoupling from US-controlled silicon.

The leaked benchmarks — unverified by independent testers as of this writing — describe a model that would be the most capable open-weight release in history. If they hold, DeepSeek V4 would substantially close the remaining gap between Chinese open-source AI and Western closed frontier models, while being available for anyone to download, fine-tune, and deploy without restriction.

## The Architecture: Trillion Parameters, Efficient Activation

DeepSeek V4 uses a Mixture-of-Experts (MoE) architecture with approximately 1 trillion total parameters — but only around 37 billion active parameters per forward pass. This MoE design is the same approach that made DeepSeek V3 so efficient: most parameters are "specialists" that activate only for relevant token contexts, keeping inference costs manageable even at enormous total parameter counts.

The 1M token context window is a substantial expansion, enabling the model to reason across book-length documents, large codebases, and extended conversation histories without truncation. Native multimodal capability across text, images, and video brings it to feature parity with GPT-5 and Claude's current capabilities.

The $5.2 million estimated training cost is the figure that will generate the most skepticism. DeepSeek V3 claimed a training cost of approximately $5.5 million — a figure that was disputed by Western researchers who argued the accounting excluded pre-training amortization, hardware depreciation, and infrastructure costs. If V4's $5.2M figure is computed on a comparable basis, it represents either a genuine breakthrough in training efficiency or an accounting approach that obscures the full cost picture.

Either way, the cost figure matters for competitive dynamics. If DeepSeek can genuinely train frontier-class models for single-digit millions, the capital advantages of OpenAI ($852B valuation, $122B raised) and Anthropic ($30B round) become structural overkill — and the barrier to entry for the next generation of challenger labs falls dramatically.

## The Huawei Chip Rewrite: A Strategic Signal

The delay caused by rewriting DeepSeek V4 for Huawei Ascend hardware is the most strategically significant element of this story.

DeepSeek V3 was trained primarily on Nvidia A100 GPUs — hardware that has been under US export control restrictions since 2022 but was available to Chinese companies through various channels during the lead-up to V3's development. Post-V3, the US tightened its export controls further, cutting off access to remaining Nvidia chips above a certain compute threshold.

The V4 rewrite for Huawei Ascend is a direct response to that tightening. By building the inference stack (and reportedly much of the training pipeline) around Huawei's Ascend 910C and 910D accelerators, DeepSeek ensures that V4 and future models can be developed and deployed without Nvidia dependency.

This matters beyond DeepSeek. If V4 demonstrates that frontier-class model development is achievable on Huawei silicon at scale, it validates Huawei's Ascend platform as a genuine Nvidia alternative for AI training workloads — a development that would have implications for the entire US export control framework. The controls were premised on the assumption that cutting off Nvidia access would meaningfully slow Chinese AI development; a V4 success on Huawei chips would challenge that assumption directly.

The Cambricon compatibility is a secondary signal in the same direction: China is investing in multiple domestic AI chip platforms simultaneously, hedging against single-vendor risk in the domestic ecosystem.

## Leaked Benchmark Claims

The leaked benchmarks circulating ahead of the official V4 release (sourced from NxCode's compilation and Dataconomy's April reporting):

- **HumanEval**: 90% — matching or exceeding current state-of-the-art for code generation
- **SWE-bench Verified**: 80%+ — which would place it ahead of Kimi-K2.5 (76.8%), GLM5 (77.8%), Alibaba's Qwen 3.6-Plus (78.8%), and within 1 point of Claude Opus 4.5 (80.9%), the current reported leader
- **GPQA Diamond** (graduate-level science reasoning): 85%+ — competitive with GPT-5.x
- **MMLU**: 95%+ — saturating this benchmark

These figures have not been verified by the ML community, and DeepSeek's prior benchmark presentations have attracted scrutiny over methodology. Benchmark inflation — selecting favorable evaluations, cherry-picking few-shot prompting configurations, or using evaluation sets with training data contamination — is a known problem across all AI labs, not unique to Chinese developers.

The SWE-bench Verified score deserves particular attention because it is harder to inflate: it requires actually solving real GitHub issues in production codebases with automated tests that verify correctness. An 80%+ score on SWE-bench would be a genuinely significant achievement.

## Open Weights, Apache 2.0

Like DeepSeek V3, V4 is expected to release with full open weights under Apache 2.0 — the same license Google adopted for Gemma 4. This means the complete model can be downloaded, fine-tuned, and deployed commercially by anyone without licensing restrictions or royalty obligations.

The combination of frontier-class capabilities and Apache 2.0 licensing represents a specific competitive threat to the closed-model API businesses of OpenAI and Anthropic. Enterprises that currently pay for API access to GPT-5 or Claude for coding, reasoning, or multimodal tasks may find that a locally deployed DeepSeek V4 — fine-tuned on their proprietary data, running on their own infrastructure — provides comparable results at lower marginal cost.

The enterprise adoption dynamic depends heavily on inference efficiency. Running 37 billion active parameters from a 1 trillion parameter MoE model still requires significant hardware; the cost crossover point between API pricing and self-hosted deployment varies significantly by use case and usage volume.

## What Comes After the Release

If the benchmarks hold and DeepSeek releases V4 under Apache 2.0 within the next few weeks as reported, the response from Western AI labs will be instructive. The V3 release in early 2025 triggered a significant repricing of "AI model" risk assets and accelerated several open-weight releases from Meta, Google, and Mistral.

V4, if it performs as claimed, would be a larger shock — not because the benchmarks would be unprecedented (Claude Opus 4.5 is already near 81% on SWE-bench), but because it would demonstrate that an open-weight model on non-Nvidia hardware has achieved near-parity with the best closed models in the world. That combination — open, cheap, hardware-independent, near-frontier — is the scenario Western AI labs have been working to prevent.

The next few weeks will determine whether DeepSeek V4 is that model.
