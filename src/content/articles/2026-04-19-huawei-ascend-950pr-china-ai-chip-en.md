---
title: "Huawei Ascend 950PR Debuts as ByteDance and Alibaba Plan Orders, Challenging Nvidia in China"
summary: "Huawei's Ascend 950PR, an inference chip that Huawei says delivers about 2.8 times the FP4 performance of Nvidia's H20, debuted with the Atlas 350 accelerator card. Reuters reported that ByteDance and Alibaba plan to place orders and that Huawei plans to ship around 750,000 units this year."
category: "hardware"
publishedAt: 2026-04-19
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: false
sources:
  - name: "TrendForce"
    url: "https://www.trendforce.com/news/2026/03/23/news-huawei-debuts-atlas-350-on-ascend-950pr-with-in-house-hbm-touting-2-8x-h20-performance/"
  - name: "CNBC / Reuters"
    url: "https://www.cnbc.com/2026/03/27/bytedance-alibaba-planning-to-order-huaweis-new-ai-chip-reuters.html"
  - name: "Tech Insider"
    url: "https://tech-insider.org/huawei-ascend-950pr-ai-chip-nvidia-china-2026/"
  - name: "Nerd Level Tech"
    url: "https://nerdleveltech.com/huawei-ascend-950pr-atlas-350-ai-chip-challenges-nvidia"
tags:
  - "Huawei"
  - "Ascend 950PR"
  - "AI chips"
  - "China semiconductor"
  - "ByteDance"
  - "Nvidia"
  - "export controls"
relatedSlugs:
  - "2026-04-19-deepseek-300m-fundraise-v4-huawei-chips-en"
---

For three years, the central question haunting China's AI ambitions has been hardware. U.S. export controls, progressively tightened from 2022 onward, have restricted Chinese companies' access to the most advanced Nvidia GPUs — the chips that power frontier model training and the inference infrastructure that scales AI applications to hundreds of millions of users. China's AI champions — ByteDance, Alibaba, Tencent, Baidu, and Huawei's own cloud division — have been forced to stockpile older-generation chips, pay gray-market premiums, or adapt their workflows to hardware that was never designed for modern AI.

That constraint is now being directly addressed. Huawei has debuted the Ascend 950PR, an AI inference chip, with mass production expected to begin in April, according to Reuters. Paired with the Atlas 350 accelerator card unveiled at the Huawei China Partner Conference on March 20, the 950PR delivers performance specifications that, for the first time, make domestic Chinese silicon genuinely competitive with the hardware that has powered the global AI revolution.

## Performance Specifications: 2.8× the H20

The headline performance claim is aggressive and specific. In FP4 precision — the numerical format increasingly preferred for large-scale AI inference because it reduces memory consumption and compute cost — the Ascend 950PR delivers 2.8 times the performance of Nvidia's H20. The H20 is the most advanced Nvidia chip currently permitted to be sold in China under U.S. export control regulations; it was itself a downgraded version of the H100, modified specifically to meet export compliance thresholds.

Raw performance numbers: the Atlas 350 card delivers 1.56 PFLOPS at FP4 precision, according to Huawei. Interconnect bandwidth is reportedly 2.5 times that of the previous generation of Ascend chips.

Memory is a meaningful differentiator. The 950PR integrates 112 GB of Huawei's proprietary HiBL 1.0 high-bandwidth memory — 1.16 times the capacity of Nvidia's H20 (which carries 96 GB of HBM3). Memory capacity is a practical bottleneck for serving large language models: larger memory means larger models can be loaded on fewer cards, reducing infrastructure cost and inference latency. The memory bandwidth of the Atlas 350 card is 1.4 TB/s, well below the roughly 4.0 TB/s cited for the H20.

## The CUDA Bridge: Software as the Real Moat

Hardware specifications tell only part of the story. Nvidia's dominant position in AI hardware has always rested as much on software as on silicon — specifically, CUDA, the parallel computing platform that has become the default substrate for virtually all AI research and production workloads. Over 15 years, the AI research community has built frameworks, libraries, toolchains, and intuitions on top of CUDA. Switching to a new hardware architecture has historically required rewriting code, retraining engineers, and accepting performance uncertainty during the transition.

Huawei's previous generation Ascend chips, particularly the 910B and 910C, suffered from limited CUDA compatibility. Models ran, but required significant engineering effort to port, and performance was unpredictable compared to running the same models on Nvidia hardware. This compatibility gap was a major adoption barrier even for Chinese companies facing export restrictions.

The Ascend 950PR significantly narrows this gap. According to Reuters sources, the chip is more compatible with Nvidia's CUDA software system, which lets developers migrate existing models more easily. Where Huawei previously stuck to its proprietary CANN software system, the new chips are meant to let developers at Chinese tech firms migrate models more easily. This is not perfect CUDA compatibility — no non-Nvidia chip has achieved that — but it is materially better than previous generations, and it appears to be sufficient to make migration economically and technically feasible for major operators.

## ByteDance and Alibaba Plan Orders

The most concrete validation of the 950PR's commercial viability is the scale of orders being placed. Reuters reported ByteDance's and Alibaba's intentions to order the chip in late March, citing two people familiar with the matter.

Reuters' sources said the standard version with traditional DDR memory will be priced at around 50,000 yuan ($6,900) per card, while a premium version with faster HBM will sell for around 70,000 yuan. ByteDance is, in effect, making a bet that the 950PR's CUDA compatibility is sufficient, that its performance is adequate for its inference workloads, and that the strategic benefit of reducing Nvidia dependence outweighs any residual performance disadvantage.

## DeepSeek V4: The Ultimate Proof of Concept

The planned orders from ByteDance and Alibaba are significant validation, but the most consequential endorsement of the 950PR may be a software one. DeepSeek's V4 model — reportedly a trillion-parameter system expected to launch in late April — is being built to run entirely on Ascend 950PR chips.

This is a deliberate architectural choice. DeepSeek gave Huawei and Cambricon early access to V4 development, while denying that access to Nvidia. The engineering team rewrote core components of the training and inference pipeline to run natively on the Ascend architecture. If V4 performs at or above the level of the best models from Anthropic, OpenAI, and Google — models that were trained on Nvidia's most advanced hardware — it will be the first definitive evidence that domestic Chinese silicon can support frontier AI at the highest level of global competition.

The Ascend 950PR's value proposition does not depend on V4 succeeding, but V4's success would substantially accelerate the chip's adoption. Every Chinese AI company watching DeepSeek's results is running a mental calculation: if the best model in the world was trained on this chip, can we afford not to use it?

## Geopolitical Context and Market Implications

The timing of the 950PR's mass production launch is not accidental. It arrives as U.S.-China technology competition has intensified, with export controls expanded and updated, and as Chinese policymakers have made semiconductor self-sufficiency an explicit national priority. The 950PR represents the intersection of that policy priority with genuine engineering progress — a combination that has taken longer to materialize than Chinese officials hoped, but that is now arriving at a moment when the stakes are maximally high.

For Nvidia, the implications are complex. The company's H20 chip is the baseline Huawei compares the 950PR against. Nvidia's China revenue, though reduced by export controls, has remained material to the company's results. A credible domestic alternative that outperforms the H20 on key metrics, with improving software compatibility, represents a structural erosion of that revenue over the medium term.

The 950PR will not immediately displace Nvidia in China. The installed base of older Nvidia chips is enormous, the CUDA software ecosystem is deeply entrenched, and performance on training workloads (as opposed to inference) has not yet been demonstrated at scale. But the direction of travel is now clearly established: China is building chips that can do the job, at prices that work, with software compatibility that makes migration increasingly feasible. The question is no longer whether China will have competitive AI hardware — it is how long it will take for that hardware to become the default choice inside the country's borders.

*Correction (November 15, 2026): 16 sentences were corrected or removed to match the sources listed on this page.*
