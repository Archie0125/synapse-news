---
title: "MiniMax M3: Chinese Open-Weight AI Achieves Frontier-Class Scores with 1M-Token Context"
summary: "Chinese AI company MiniMax has released M3, an open-weight model with a one-million-token context window and native multimodal inputs. By MiniMax's own numbers, it edges past GPT-5.5 on SWE-Bench Pro and beats Claude Opus 4.7 on the BrowseComp web-search benchmark."
category: "ai-ml"
publishedAt: 2026-06-20
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "The Decoder"
    url: "https://the-decoder.com/minimax-m3-open-weight-model-with-a-million-token-context-challenges-proprietary-leaders/"
  - name: "Codersera"
    url: "https://codersera.com/blog/minimax-m3-developer-guide/"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/317532/20260601/minimax-m3-open-weight-coding-model-frontier-claims-unverified-benchmarks.htm"
  - name: "DataNorth"
    url: "https://datanorth.ai/news/minimax-launches-m3"
tags:
  - "MiniMax"
  - "M3"
  - "open-weight"
  - "LLM"
  - "multimodal"
  - "China"
  - "open-source"
  - "frontier-AI"
  - "context-window"
relatedSlugs:
  - "2026-04-04-open-source-llm-race-en"
  - "2026-06-17-deepseek-74b-first-funding-tencent-catl-50b-en"
---

MiniMax, a Shanghai-based AI company, released M3 on June 1, 2026.

M3 is the first open-weight model to simultaneously combine frontier-class coding performance, a genuine one-million-token context window, and native multimodal inputs. That distinction, until recently a niche concern, has become one of the most commercially significant properties a frontier model can have.

## What M3 Actually Does

The case for M3 begins with three capabilities that, individually, several other models already offer. The combination in a single open-weight package is what makes the release significant.

**One million tokens of context.** M3's context window is five times longer than that of its predecessor, M2.7. This is not merely a benchmark metric — it changes the structure of what AI applications can realistically attempt.

**Native multimodality.** M3 accepts text, images, and video as input, with text as output. MiniMax positions this as a computer-use capability comparable to Anthropic's computer-use API; the model can operate a desktop computer.

**Frontier-class coding.** On SWE-Bench Pro, M3 scores 59.0%, placing it ahead of GPT-5.5's 58.6% and behind Claude Opus 4.7's 64.3%. On BrowseComp, a web research evaluation benchmark, M3 scores 83.5 against Opus 4.7's 79.3.

Caveats apply. Several of MiniMax's benchmark runs were conducted on the company's own infrastructure with its own agent scaffolding, and independent third-party verification is pending. The SWE-Bench Pro gap against Opus 4.7 of 5.3 percentage points is meaningful, not merely cosmetic. M3 is competitive with the frontier; it has not matched it across the board.

## The Architecture: MiniMax Sparse Attention

The enabling innovation behind M3's million-token context is a new architectural component called MiniMax Sparse Attention (MSA). Processing a million tokens with standard full-attention transformers is expensive: attention compares every token against every other token, so compute costs grow quadratically with input length.

MSA approaches the problem with a block-based key-value cache. Rather than computing attention over every token in a sequence for every query, MSA divides stored context into blocks, pre-filters which blocks are relevant to the current query, and batches queries that need the same blocks — eliminating redundant memory reads across a session. The result, according to MiniMax's own measurements, is 15.6x faster decoding and 9.7x faster prefill at million-token context compared to M2, with per-token compute at one million tokens reduced to approximately 1/20th of the previous generation's cost.

This matters enormously for practical deployment. A model that can theoretically process a million tokens but requires $100 of compute per inference is not practically deployable. MiniMax says MSA makes the million-token context affordable without letting compute costs spiral out of control.

## Autonomous Capability Demonstrations

MiniMax published three internal demonstrations of extended autonomous operation that underscore M3's agentic potential:

**Paper reproduction over 12 hours.** M3 was given the task of independently reproducing an ICLR 2025 fine-tuning paper. Without human intervention, the model worked for nearly twelve hours, produced 18 commits and 23 figures, and confirmed the paper's key findings. The multi-hour, multi-commit nature of this task places it well beyond what single-pass generation can accomplish.

**GPU kernel optimization over 24 hours.** Tasked with optimizing a CUDA kernel for NVIDIA Hopper architecture, M3 improved hardware utilization from 7.6% to 71.3% across 147 attempts, a 9x efficiency gain. Most competing models, MiniMax reports, abandoned the optimization after dozens of attempts. M3's persistence — and its ability to maintain coherent context across a full day of iteration — reflects the practical advantage of long-context architecture over extended autonomous tasks.

**PostTrainBench autonomous training.** M3 autonomously trained four base models, including data synthesis and iterative refinement, without human intervention. This is a capability that, if it generalizes, has significant implications for AI self-improvement pipelines.

These demonstrations should be taken with appropriate skepticism — they were conducted and evaluated by MiniMax, not independent researchers. But they are specific enough to be falsifiable, and their publication signals a confidence level that invites verification.

## The Open-Weight Advantage

M3 is available via MiniMax's API with tiered pricing ($20–$120 monthly plans) and at standard per-token rates up to 512,000 tokens, with additional pricing for longer contexts. Model weights and a technical report were scheduled for release on Hugging Face within ten days of the announcement.

The open-weight release is strategically significant beyond the technical specifications. An open-weight model can be self-hosted, fine-tuned, and deployed behind the host organization's own firewall. It cannot be taken offline by a government directive, because there is no central server to pull.

It also matters for the geopolitical texture of the AI market. DeepSeek's earlier releases suggested a Chinese open-weight model could reach near-frontier performance. M3 makes a stronger case that the gap has narrowed further.

The export control dynamics cut both ways. A Chinese open-weight model at frontier-comparable performance, available to anyone with the compute to run it, is not subject to those rules. For international developers and enterprises, M3 and its successors represent a credible alternative supply chain.

## What Comes Next

MiniMax is not alone in this space. The Chinese open-weight AI field has converged on these capability targets — long context, strong coding, multimodal input — within weeks, suggesting coordinated roadmap awareness if not explicit coordination.

For developers evaluating M3, the practical questions center on inference cost, fine-tuning stability, and the gap between MiniMax's internal benchmark methodology and independent replication. Those questions will be answered in coming weeks as the research and development community exercises the released weights.

The bigger-picture question is whether June 2026 marks the point at which frontier-class AI became genuinely available as open infrastructure — not in theory, but in practice, at production cost, with a context window long enough to ingest real-world problem complexity. The M3 release makes a credible argument that it does.

*Correction (November 15, 2026): 19 sentences were corrected or removed to match the sources listed on this page.*
