---
title: "MiniMax M3 Beats GPT-5.5 on Coding at 5% of the Compute Cost"
summary: "Chinese AI lab MiniMax released M3 on June 1, an open-weight multimodal model that outperforms both GPT-5.5 and Gemini 3.1 Pro on the SWE-Bench Pro coding benchmark while running at just 1/20th the per-token compute of its predecessor. With a 1-million-token context window and native multimodality built from pretraining, M3 is the most credible open-weight challenge to frontier closed models yet."
category: "ai-ml"
publishedAt: 2026-06-12
lang: "en"
featured: false
trending: true
sources:
  - name: "MiniMax Blog"
    url: "https://www.minimax.io/blog/minimax-m3"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/minimax-m3-debuts-eclipsing-gpt-5-5-and-gemini-3-1-pro-on-key-benchmark-performance-for-just-5-10-of-the-cost"
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/06/01/minimax-releases-minimax-m3-with-msa-architecture-supporting-1m-token-context-native-multimodality-and-agentic-coding/"
tags:
  - "MiniMax"
  - "open-source AI"
  - "LLM"
  - "SWE-bench"
  - "multimodal"
  - "coding AI"
relatedSlugs:
  - "2026-06-04-open-source-llm-race-en"
  - "2026-06-10-anthropic-claude-fable-5-public-release-en"
  - "2026-06-04-deepseek-74b-funding-59b-valuation-close-en"
---

When MiniMax released M3 on June 1, the Chinese AI lab did not just ship another model — it shipped a benchmark result that stopped the open-source community cold. M3 scored 59.0% on SWE-Bench Pro, the most demanding software engineering evaluation currently in widespread use, surpassing both OpenAI's GPT-5.5 and Google's Gemini 3.1 Pro on the same test. The score arrived on an open-weight model. The cost to run it, according to MiniMax's own measurements, is roughly 5–10% of comparable frontier alternatives.

For a field that has spent the last eighteen months debating whether open-source can close the gap with closed frontier labs, M3 represents the clearest evidence yet that the gap is narrowing faster than most observers expected.

## The Architecture That Makes It Possible

The efficiency gains behind M3 are not magic — they are the product of a fundamental architectural rethink. MiniMax built M3 around a proprietary attention mechanism called MSA, or MiniMax Sparse Attention, which attacks the most compute-intensive bottleneck in transformer models: the relationship between context length and computational cost.

Standard attention mechanisms scale quadratically with context length. At one million tokens — the context window M3 supports — that quadratic scaling makes inference prohibitively expensive for most deployment scenarios. MSA replaces the dense attention pattern with a sparse equivalent that preserves the model's reasoning quality while dramatically reducing the computation required. The practical results are striking: per-token compute is approximately 1/20th of what M3's predecessor required at equivalent context lengths, with 9× prefilling speedup and 15× decoding acceleration when processing million-token inputs.

The efficiency gains are not purely theoretical. M3's Terminal-Bench 2.1 score of 66.0% and MCP Atlas score of 74.2% — both long-horizon agentic tasks that require sustained reasoning across large contexts — suggest the architectural improvements hold up under the kinds of real-world workloads developers care about, not just curated benchmark suites.

## Multimodality From the Ground Up

Most multimodal language models are fundamentally text models with vision capabilities grafted on afterward. Image and video understanding is handled by a separate encoder whose representations are injected into the text model, creating a fusion architecture that is functional but rarely seamless.

MiniMax took a different approach with M3, engineering the model to be natively multimodal from what the company calls "Step Zero." Rather than fusing a pretrained text network with a separate vision system, MiniMax redesigned the data ingest pipeline from scratch to blend naturally interleaved sequences of text, images, and video. The total pretraining corpus exceeded 100 trillion tokens. The result is a model that does not treat vision as a secondary capability — it reasons over images and video in the same representational space as text.

M3 accepts text, image, and video inputs, produces text output, and includes computer operation capability, meaning it can navigate graphical interfaces directly. The native multimodality matters particularly for agentic use cases where models need to observe and interact with visual environments, a capability that M3's architecture handles more gracefully than fusion-based alternatives.

## Benchmark Performance in Context

The SWE-Bench Pro result deserves some unpacking. The original SWE-Bench measured whether models could fix real software engineering issues from GitHub repositories. SWE-Bench Pro is a harder variant that draws from more complex, less-studied codebases, reducing the risk of contamination with training data and raising the bar for genuine reasoning capability.

M3's 59.0% score on SWE-Bench Pro is the highest open-weights result on that benchmark, tied with Gemini 3.1 Pro and ahead of GPT-5.5. For context, the best closed models on the original SWE-Bench Verified currently range from roughly 70% to 82%, suggesting the gap between open and closed remains meaningful but has narrowed substantially.

On Terminal-Bench 2.1, which evaluates long-horizon terminal-based software engineering tasks, M3's 66.0% score places it firmly in the top tier of available models. The KernelBench Hard score of 28.8% — evaluating the ability to write optimized GPU kernels — is more modest but still competitive with models far larger and more expensive to run.

## Open Weights and Accessibility

MiniMax announced at launch that open-source model weights would be released within ten days, under a permissive license that includes commercial use. By the time this article publishes, those weights should be publicly available on Hugging Face, making M3 deployable on private infrastructure without API dependencies.

The pricing for the hosted API reflects the efficiency gains. MiniMax's token plans start at $20 per month for approximately 1.7 billion tokens, with professional and enterprise tiers at $50 and $120 respectively. The per-token API pricing is competitive with mid-tier models, not frontier pricing, despite frontier-level benchmark performance on specific tasks.

## The Chinese Open-Source Moment

M3 arrives at a moment when Chinese AI labs have become unusually competitive at the open-source frontier. DeepSeek's V4 Pro, released in late April, brought a 1.6-trillion-parameter MoE architecture with frontier-level coding performance at dramatically lower inference costs. Qwen 3.7 Max reached fourth place on web development benchmarks. Now MiniMax has added a genuinely multimodal, million-context-window open-weight model to the mix.

The pattern is not coincidental. Chinese labs operate under tighter constraints on acquiring the latest NVIDIA GPU hardware, driven partly by U.S. export controls. The response has been to invest heavily in architectural efficiency — building models that extract more capability per FLOP rather than simply scaling up compute. The result is a generation of models that are more efficient by design, and that efficiency is now appearing on benchmarks as performance at a fraction of the cost.

The implications for the broader industry extend beyond competitive dynamics. If open-weight models can deliver frontier-equivalent performance on specific capability domains at 5–10% of the cost, the entire economic case for proprietary API dependency weakens. Developers who need coding assistance, long-context document analysis, or multimodal understanding can increasingly access competitive capability without committing to a vendor.

## Limitations and Open Questions

M3 is not a universal frontier replacement. Its knowledge cutoff and overall reasoning on complex multi-step problems likely still trail the very best closed models on tasks outside coding and long-context processing. MiniMax is a Chinese company, which raises sovereignty and compliance questions for organizations with data residency requirements or government-contracting restrictions.

The open weights also come with the standard caveat of open-weight models: MiniMax retains control of training and fine-tuning data, and the model's safety properties — particularly around harmful outputs at scale — have not received the same level of external evaluation as models from labs that operate under more comprehensive AI safety programs.

Still, for the majority of developers building agentic coding workflows, long-context analysis pipelines, or multimodal applications, M3 represents the most compelling case yet that the open-source ecosystem can serve as a credible alternative to the frontier API stack. The benchmark numbers suggest the architecture choices are working. The pricing suggests they may not be limited to research for long.
