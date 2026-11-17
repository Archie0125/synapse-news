---
category: ai-ml
faqs:
- answer: 推論時每個專家都必須留在記憶體裡，但每個 token 只會用到少數幾個。以 Qwen3.5-122B 為例，專家 MLP 約佔約 250GB 參數記憶體的
    95%，每層 256 個專家中每個 token 只用到 8 個。
  question: MoE 模型為什麼這麼吃記憶體？
- answer: 這些方法逐一替專家打分數，再刪掉分數最低的。研究顯示專家會形成穩定的協作群組，忽略這種關係會讓剪枝效果變差，剪得越多越明顯。
  question: 現有的專家剪枝方法有什麼問題？
- answer: HOPE（Higher-Order Pruning of Experts）會考慮共同啟用的專家之間的交互作用，而不是只看單一專家的分數。目標是刪掉更多專家，同時保住更多模型效能。
  question: HOPE 有什麼不同？
featured: false
lang: zh
publishedAt: '2026-11-09T12:34:29+00:00'
relatedSlugs: []
sources:
- name: Hugging Face Blog
  url: https://huggingface.co/blog/amazon/higher-order-pruning-experts
summary: HOPE 研究發現，MoE（混合專家）模型中的專家其實是以團隊形式協同運作。逐一剪枝專家，就像不聽整首歌就隨意裁掉樂團成員一樣。
tags:
- ai-ml
- open-source
title: MoE 專家也有好搭檔：HOPE 讓它們不被拆散
trending: false
type: news
---

Mixture-of-Experts (MoE) models have enabled state-of-the-art LLMs to be scaled to hundreds of billions of parameters, but they come with a fundamental and costly caveat: every expert MLP must occupy memory at inference time, even though the vast majority are idle for any given token. For example, Qwen3.5-122B has 256 experts in each of its 48 MoE layers, and 95% of its \~250 GB parameter memory footprint is taken up entirely by these expert MLPs alone. However, for any given token, only 8 experts in each layer are actually used.

**Expert pruning** is one of the most direct fixes to this memory bottleneck. That is, permanently delete the least useful experts. Pruning avoids the latency issues which make dynamic loading/off-loading of experts impractical; it does not require any training; and [it composes with quantization](https://arxiv.org/abs/2510.13999). Given these attractive benefits and the simplicity of the idea, it's easy to see why expert pruning has become a go-to approach for shrinking MoEs. The difficulty lies in deciding *which* experts are safest to remove.

Existing pruning methods score each expert independently, assigning every expert a scalar importance score (based on a calibration dataset), and cutting out the least important experts (in each layer independently). These are **first-order** methods, because they assume each expert's contribution is independent of all others. In reality, experts form cooperative groups. We observe consistent clusters of co-activated experts in our own experiments, and independent work has shown that [expert cooperation is a stable property of MoEs](https://arxiv.org/abs/2505.20225) and [is important for model performance](https://arxiv.org/abs/2510.16411). Ignoring these interactions leads to suboptimal pruning, especially at aggressive rates.

[Our newest paper](https://arxiv.org/abs/2609.18916) derives **HOPE** (Higher-Order Pruning of Experts), a **second-order** method that accounts for pairwise expert interactions. At 50% pruning, HOPE achieves the best average rank of any method, with gains of up to +6.1% on agentic coding tasks over the next-best pruning method.

In this post, we explain how HOPE works, show where it outperforms existing methods, and walk through how to use it for your own models. For readers unfamiliar with MoE architectures, see [Mixture of Experts (MoEs) in Transformers](https://huggingface.co/blog/moe-transformers).

In a standard MoE, each layer has experts, and each input token is routed independently to such experts ( is a typical choice). Routing is performed by a single layer which produces softmax-normalized gate weights for each expert , wherein the experts with the highest gate weights are selected to form the active set of experts, . The output of the layer is then , where is the output of expert for token .


*Left: typical MoE layer, where each token is routed to the top-K experts. Right: first-order methods rank and delete experts based on a scalar importance score, but the best pruning decisions will also consider the strength of interactions between experts.*

Importantly, experts in the selected set  are not independent. Experts form stable cooperative groups that get consistently co-activated together. This has been observed [before in the literature](https://arxiv.org/abs/2505.20225), as well: expert co-selection patterns emerge early in training and stabilize throughout.

This means that when we prune experts from an MoE layer, pruning decisions need to consider the higher-order effects between these experts. Removing expert A might seem fine on its own, but if expert B—which frequently cooperates with and relies on A—is highly important, then removing A would dismantle a cooperative group just through a single deletion. First-order methods miss this entirely, because they score A and B separately.

This effect compounds at high pruning rates. When we remove up to 50% of experts, we risk breaking many cooperative links. This is where second-order pruning is most advantageous.

*(See Appendix A in [our corresponding paper](https://arxiv.org/abs/2609.18916) for the full derivation of the HOPE objective)*

When we delete a set of  experts from some MoE layer, the selected set of experts  (for any token ) can change. The pruned experts that *would have* been selected are replaced by the experts with the next-highest gate weights. The resulting change in layer output is the **pruning error**. Our goal is to find the prune-set  (of some predefined pruning budget ) that *minimizes* the resulting pruning error (over tokens  from our calibration set).

Unfortunately, minimizing the pruning error over directly is intractable. The pruning error depends on the identities of the replacement experts, which in turn depend on the prune-set itself. HOPE sidesteps this by defining a tractable surrogate , which strictly upper-bounds the dominant component of the pruning error:


Because is a squared sum, expanding it naturally produces cross-terms between pairs of experts. These are the interaction terms that first-order methods discard.

To find the optimal prune-set, HOPE minimizes over the calibration set, which can be reformulated as the following quadratic program:


where is defined as:


This F-matrix is collected on the calibration dataset, and the optimal prune-set is obtained by solving the resulting quadratic program (QP) with a continuous relaxation (then rounding to binary solutions). Each entry  captures the average gate-weighted output product of experts  and , across tokens where both are co-activated. Whereas the diagonal  measures *individual* expert importance, the off-diagonal entries (  for ) measure pairwise *cooperative* contribution.

What does look like in practice? It shows the structure of expert cooperation, which depends on layer:


*Visualization of the interaction matrix F for GLM-4.5-Air (128 experts per layer, 106B parameters total) at three representative layers (early, middle, late). Experts have been clustered to reveal block structure. Bright blocks along the diagonal indicate groups of experts with strong pairwise interaction scores.*

In terms of practical cost, HOPE requires the same calibration pass as any other expert-pruning method (one forward pass over calibration data). The only addition is solving the quadratic program, which is non-convex, but can be solved efficiently via a standard QP solver (1–2 seconds each layer). The total additional overhead is negligible compared to first-order methods, as the time for calibration dominates.

Notably, HOPE has a strong connection to [Router-weighted Expert Activation Pruning (REAP)](https://arxiv.org/abs/2510.13999), a state-of-the-art first-order expert-pruning method. HOPE's F-matrix encodes individual expert importance scores on the diagonal, and this diagonal effectively recovers the scores used by REAP to independently rank experts for pruning (differing only by the variance of expert contributions). The diagonal of  recovers REAP's expert rankings almost perfectly (Spearman ). Thus, any improvement HOPE achieves over REAP is attributable to the second-order interaction terms in the off-diagonal entries of the -matrix.

We evaluated HOPE as an expert pruning method using 3 models (Qwen3.5-122B, Qwen3.5-35B, and GLM-4.5-Air), with 2 calibration datasets (Evol-CodeAlpaca and SWE-Bench Verified trajectories). We used the Tulu3 suite and SWE-Bench Pro (agentic coding) to test the resulting pruned models, comparing HOPE to 4 first-order baselines ([REAP](https://arxiv.org/abs/2510.13999), [MAN](https://arxiv.org/abs/2606.15716), [EAN](https://arxiv.org/abs/2504.05586), and Frequency) across pruning rates spanning from 10% to 50%.


*HOPE achieves the best overall rank across conditions and dominates at aggressive pruning rates. Left: average rank (lower = better) across all models, calibration sets, and benchmarks. Right: SWE-Bench Pro performance on Qwen3.5-35B.*

Across all conditions, HOPE achieved the best average rank (**2.07** out of 5 methods), with the highest rate of top-1 finishes (**39%** of conditions) and top-2 finishes (**67%**). In a head-to-head comparison, HOPE beats every other baseline in the majority of conditions.

As expected, **HOPE's advantage grows at higher pruning rates.** As more experts are removed, more cooperative links are broken, and the off-diagonal terms of  become more important. At 50% pruning, HOPE's average rank improves to **1.58** (vs. **2.42** for the next-best method, REAP). This is also the most deployment-relevant setting, where memory savings are large enough to accommodate longer contexts, deeper reasoning, and more tool calls.

HOPE's advantage is most pronounced on **SWE-Bench Pro**, an agentic coding benchmark where models must solve real GitHub issues autonomously. These problems involve compositionally diverse tasks (e.g. coding, tool calls, reasoning, etc.) over many turns and likely exercise diverse expert combinations—exactly the regime where preserving cooperative structure matters most. On Qwen3.5-35B-A3B at 50% pruning, HOPE achieved **42.3** on SWE-Bench Pro, matching the unpruned model's **41.8** (while REAP dropped to **36.2**, a 13% regression).

Notably, pruned models can occasionally match or exceed the unpruned baseline, likely because the removal of low-relevance experts reduces noise on the target tasks. This effect is not unique to HOPE and [has been observed across pruning methods](https://arxiv.org/abs/2504.06792). Furthermore, our experiments showed that code-focused calibration with any pruning method (including HOPE) did not severely degrade non-coding benchmarks, and HOPE performed well across the Tulu3 suite regardless of calibration set.


*Average strength of cooperation (measured by F-matrix value) with retained experts, split by experts on which HOPE and REAP disagree.*

HOPE's advantage stems from optimizing over the entire interaction matrix . To understand how this affects pruning decisions in practice, we examine the experts where HOPE and REAP disagree. For each disputed expert, we compute its *cooperative score* (i.e. its average F-value with other retained experts). Experts retained only by HOPE consistently have *higher cooperative scores* than experts retained only by REAP. In other words, as part of the QP optimization, HOPE sacrifices some individually high-scoring experts in favor of preserving cooperative clusters. The gains in benchmark performance (shown above) validate that this trade-off is advantageous.


We created a basic [package](https://github.com/awslabs/HOPE) to run HOPE. It has three steps: 1) calibrate; 2) solve; 3) prune. Our package has been tested on Qwen3, Qwen3-Next, Qwen3.5, and GLM-4.5.

```
hope calibrate \
    --model-path Qwen/Qwen3.5-35B-A3B \
    --prompts calibration_prompts.txt \
    --out-path observations.h5
```
The calibration step runs a single forward pass over calibration data, whether it be agentic rollouts or single-turn traces. This uses HuggingFace `transformers` to hook into the forward pass of each individual MoE layer. For each token, this records which experts are selected, their gate weights, output norms, and pairwise co-activation statistics. The output of this step is the F-matrix, stored in an HDF5 file.

```
hope solve \
    --obs-path observations.h5 \
    --prune-frac 0.50 \
    --out-path pruneset.json
```
This command materializes the F-matrix and solves the binary quadratic program via a continuous relaxation. This takes a few seconds per layer, and the output is a JSON file which contains the prune-set. This is technically the final output of the HOPE algorithm.

```
hope prune \
    --model-path Qwen/Qwen3.5-35B-A3B \
    --pruneset-path pruneset.json \
    --out-path ./Qwen3.5-35B-A3B-pruned-50
```
To complete the pipeline, we run this command to actually create the smaller model checkpoint from the prune-set. The pruned model is a standard HuggingFace checkpoint which is smaller on disk and in memory (no changes to vLLM or SGLang model definitions needed).

We also released a more compact Python API:

```
from hope.calibrate import calibrate
from hope.solve import solve
from hope.prune import prune_model
calibrate("Qwen/Qwen3.5-35B-A3B", calibration_prompts, "observations.h5")
solve("observations.h5", prune_frac=0.50, out_path="pruneset.json")
prune_model("Qwen/Qwen3.5-35B-A3B", "pruneset.json", "./Qwen3.5-35B-A3B-pruned-50")
```
HOPE's advantage is most pronounced at higher pruning rates (40–50%). At lower pruning rates (10–20%), first-order methods like REAP and MAN are sometimes competitive, and HOPE's advantage shrinks. Additionally, as with most expert-pruning algorithms, HOPE prunes each layer independently and does not account for cross-layer interactions. In our paper, we presented a theoretical framework for cross-layer HOPE, but the results remain preliminary. Finally, HOPE captures pairwise interactions, but even higher-order interactions (triplets and beyond) could provide additional signal, although they are combinatorially difficult to estimate.

For more information, see our corresponding paper and codebase.

**Paper:** [https://arxiv.org/abs/2609.18916](https://arxiv.org/abs/2609.18916)

**Code**: [https://github.com/awslabs/HOPE](https://github.com/awslabs/HOPE)

To see how HOPE can be applied to next-generation hybrid architectures, see our [corresponding repository](https://github.com/awslabs/hybrid-model-factory/).

**Citation:**

```
@article{tseng2026hope,
    title={Higher-Order Pruning of Experts in Mixture-of-Experts Language Models},
    author={Tseng, Alex M. and Kaul, Prannay and Zancato, Luca and Xia, Wei and Soatto, Stefano},
    journal={arXiv preprint arXiv:2609.18916},
    year={2026},
}
```

## Summary

**TLDR:** HOPE shows that MoE experts work in teams, so pruning them one by one is like cutting a band's members without listening to the song.

- In MoE models, every expert must sit in memory even though only a few are active per token. In Qwen3.5-122B, experts make up about 95 percent of its roughly 250GB footprint, and only 8 of 256 experts per layer fire per token.
- Expert pruning shrinks models without retraining and works alongside quantization, but deciding which experts to remove is the hard part.
- Existing methods score each expert independently, a first-order approach that ignores how experts cooperate.
- HOPE (Higher-Order Pruning of Experts) accounts for groups of co-activated experts, aiming for better quality at aggressive pruning rates.
- If it holds up, large MoE models could fit on much cheaper hardware.

## 摘要

**重點摘要：** HOPE 證明 MoE 的專家是成群合作的。逐一評分再刪減，就像不聽整首歌就開除樂團成員。

- MoE 模型的每個專家都得常駐記憶體，但每個 token 只用到少數幾個。以 Qwen3.5-122B 為例，專家約佔約 250GB 記憶體的 95%，每層 256 個專家中每個 token 只啟用 8 個。
- 專家剪枝不需要重新訓練，也能和量化疊加使用，但難點在於決定刪掉哪些專家。
- 現有方法逐一替每個專家打分數，屬於一階方法，忽略了專家之間的協作關係。
- HOPE（Higher-Order Pruning of Experts）把成群共同啟用的專家納入考量，目標是在高剪枝率下保住模型品質。
- 如果效果站得住腳，大型 MoE 模型就有機會在便宜很多的硬體上運行。