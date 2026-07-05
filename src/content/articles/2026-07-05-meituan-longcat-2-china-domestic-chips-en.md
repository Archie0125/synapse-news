---
title: "China Trains Its First Frontier-Scale AI on Domestic Chips — Meituan's LongCat-2.0 Is the Proof"
summary: "Meituan open-sourced LongCat-2.0, a 1.6-trillion-parameter model pre-trained end-to-end on a 50,000-card cluster of Chinese AI chips — the first time any lab has completed full frontier-scale training without Nvidia, Google TPUs, or AWS. The release rewrites assumptions about whether export controls can actually contain China's AI progress."
category: "ai-ml"
publishedAt: 2026-07-05
lang: "en"
featured: true
trending: true
sources:
  - name: "Silicon Report"
    url: "https://www.siliconreport.com/meituan-open-sources-1-6t-parameter-longcat-2-0-trained-on-domestic-chinese-ai-chips-8436e1c1"
  - name: "South China Morning Post"
    url: "https://www.scmp.com/tech/tech-trends/article/3358854/china-debuts-biggest-ai-model-trained-local-chips-meituan-releases-longcat-20"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/06/30/chinas-meituan-open-sources-massive-longcat-2-0-ai-model-saying-trained-domestic-chips/"
  - name: "CryptoBriefing"
    url: "https://cryptobriefing.com/meituan-longcat-2-coding-model/"
tags:
  - "China"
  - "Meituan"
  - "LongCat"
  - "domestic chips"
  - "Huawei Ascend"
  - "open source"
  - "export controls"
  - "chip war"
  - "frontier AI"
relatedSlugs:
  - "2026-06-29-us-export-control-claude-fable5-foreign-ban-en"
  - "2026-06-29-qualcomm-tenstorrent-riscv-acquisition-en"
  - "2026-04-03-us-china-chip-war-en"
---

The foundational premise of the United States' chip export-control strategy — that denying China access to leading-edge semiconductors would meaningfully slow its AI progress — cracked open on June 30, 2026, when Chinese food delivery giant Meituan open-sourced LongCat-2.0: a 1.6-trillion-parameter Mixture-of-Experts language model trained from scratch on 50,000 Chinese AI chips, with no Nvidia GPUs, no Google TPUs, and no AWS infrastructure in the loop.

It is the first confirmed instance of a frontier-scale large language model completing full pre-training and inference on an entirely domestic Chinese chip stack. The symbolic weight alone is hard to overstate — but the technical details make it harder still to dismiss.

## What Was Built, and How

LongCat-2.0 uses a Mixture-of-Experts architecture that totals 1.6 trillion parameters but activates roughly 33 billion to 56 billion per token during inference, keeping the practical compute cost manageable. It supports a million-token context window and ships a companion model, LongCat-Flash-Thinking, which Meituan claims runs at 2.1x lower cost per token than Seed 2.0 Pro, the company's previous commercial offering.

The training cluster was built around what researchers believe are Huawei Ascend 910C processors — the most powerful chip Huawei can produce domestically without access to TSMC's leading-edge lithography. Indicators include Meituan's use of Huawei's Collective Communication Library for inter-node coordination, a component specifically engineered for Ascend superpod configurations. If confirmed, the training run would represent the largest documented deployment of Huawei's AI silicon for frontier model pre-training.

This distinction matters enormously. DeepSeek-V4-Pro, the model that stunned Western AI labs with its benchmark performance and training efficiency earlier this year, relied on Chinese chips only for inference — the cheaper, less technically demanding half of the AI hardware equation. Pre-training a frontier model requires sustained, perfectly coordinated communication across thousands of chips for weeks or months at a time. The tolerance for hardware failures, memory bottlenecks, and inter-chip latency is near zero. That Meituan completed a run of this scale without Nvidia is a different category of achievement.

## Benchmark Claims and What They Actually Mean

Meituan's self-reported numbers are impressive: a 59.5 on SWE-bench Pro (versus GPT-5.5's benchmark figure of 58.6), 70.8 on Terminal-Bench 2.1, and 77.3 on SWE-bench Multilingual — a newly introduced evaluation for coding tasks across 12 programming languages. The company claims "overall performance comparable to Google's Gemini 3.1 Pro."

Two caveats apply heavily. First, these are self-reported figures. LongCat-2.0 has not yet been submitted to independent third-party evaluation on LMSYS Chatbot Arena or other neutral leaderboards. Meituan itself acknowledges the model "generally trails premium frontier systems like Anthropic's Claude Opus 4.8 across broad general-agent benchmarks." The model is clearly optimized for coding tasks, not general-purpose chat or complex reasoning, and its benchmark suite reflects that narrow excellence.

Second, the more consequential claim is not about performance at all — it's about infrastructure. LongCat-2.0 could have scored 10 points lower on every benchmark and still represented a geopolitical breakthrough by demonstrating that China can complete frontier-scale training without American hardware.

## Open-Sourcing the Playbook

Meituan released LongCat-2.0's weights publicly on Hugging Face under an open-source license, a decision that amplifies the geopolitical signal in ways the company almost certainly understood when it made it. Open-sourcing a frontier model trained on domestic chips is not just a research contribution — it is a public proof-of-concept that other Chinese labs, defense contractors, and state-backed research institutes can build on. The training methodology, the hardware stack, the software tooling that made a 1.6-trillion-parameter run on Ascend chips possible — all of it is now available for inspection and replication.

It also extends the model's reach into global developer communities. Researchers anywhere in the world who want to experiment with a frontier-scale model trained on non-Western hardware now have a concrete artifact to study. Whether that broader access ultimately serves Chinese strategic interests or dissipates them is a question analysts will debate for months.

## What This Means for U.S. Export Controls

The Bureau of Industry and Security has spent the better part of four years tightening restrictions on advanced semiconductor exports to China, operating on the theory that the hardware gap created by those restrictions would compound into a capability gap in AI. The H100, the A100, even the downgraded H800 and A800 variants — each successive generation of controls was designed to preserve a performance moat that would keep Chinese labs at least one to two generations behind their American counterparts.

LongCat-2.0 does not prove those controls were useless. The model has real limitations, its performance outside of coding benchmarks lags behind frontier Western models, and the Ascend 910C is still less efficient than Nvidia's current-generation hardware. The gap has not closed entirely.

But it has closed enough to train a model that can compete on specific benchmarks with GPT-5.5. The export control strategy was never designed to slow China down indefinitely — it was designed to buy time. The question policymakers in Washington now face is: time for what, and has enough of it been used productively?

## The Broader Race

LongCat-2.0 lands at a moment when the Chinese AI ecosystem is more competitive than at any point in the modern era. DeepSeek's training efficiency innovations earlier this year demonstrated that Chinese labs had closed algorithmic gaps with Western peers. Alibaba's Qwen series and Baidu's ERNIE family have both shown strong multilingual performance. Meituan's release now demonstrates that the hardware constraint — always the most difficult piece to circumvent — is not the hard wall Western strategists assumed it to be.

The model weights are on Hugging Face. The story they tell is no longer hypothetical.

---

*LongCat-2.0's weights are publicly available on Hugging Face. The model was released June 30, 2026.*
