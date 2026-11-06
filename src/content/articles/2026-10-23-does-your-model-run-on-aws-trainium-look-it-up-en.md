---
category: hardware
faqs:
- answer: Developers can check whether a tested Transformers model runs unmodified
    on AWS Trainium. The Space also reports sharding core count, compilation-inclusive
    wall time, peak memory, software versions, and the script used.
  question: What can developers learn from the model-support Space?
- answer: No. A result documents a run with specified Neuron compiler and Transformers
    versions, so later software or model changes can alter compatibility. The published
    script allows developers to reproduce the test in their own environment.
  question: Does a passing result guarantee permanent Trainium compatibility?
- answer: At the time described, testing is limited to Transformers models for text
    generation and image-text-to-text tasks. The project plans to add diffusers, sentence
    transformers, and other Transformers tasks.
  question: Which models are not covered yet?
featured: false
lang: en
publishedAt: '2026-10-23T00:00:00+00:00'
relatedSlugs: []
sources:
- name: Hugging Face Blog
  url: https://huggingface.co/blog/torch-neuronx-model-support
summary: Trainium compatibility becomes more credible when users can inspect reproducible
  model-level results, though today’s narrow test coverage still limits purchasing
  confidence.
tags:
- hardware
- developer-tools
- open-source
title: Does Your Model Run on AWS Trainium? Look It Up
trending: false
type: news
---

[Updated   •  19.6k  •  2](/datasets/aws-neuron/torch-neuronx-model-support)  

In a [previous post](https://huggingface.co/blog/hf-torchneuron), we introduced TorchNeuron, the native PyTorch backend for AWS Trainium (the `torch-neuronx` package). With it, Transformers runs its own modeling code on Trainium, as it does on any other device, so any Transformers model on the Hub may run. Which ones actually do?

The [torch-neuronx model support](https://huggingface.co/spaces/aws-neuron/torch-neuronx-model-support) Space answers that question for the most popular models on the Hub. It tells you whether a model runs unmodified on Trainium, and gives you the script to run it yourself.

The Space opens on the **Selected** view: our own selection of models picked among the top models on the Hub by downloads and by trending score. Each row gives the result, the number of Trainium cores the model is sharded over, the wall time of the run (compilation included) and the peak device memory.

To look up a given model, switch to the **Trending** or **Downloads** view and type part of its name. These views follow the Hub's own rankings, one task at a time, whether a model was tested or not. When a model was left out on purpose, the Space tells you why (most of the time it was not prioritized, sometimes it is truly incompatible). You can also pick the versions of the Neuron compiler (`neuronx-cc`) and of Transformers to look at.

At the time of writing, only Transformers models are tested, and our selection is limited to `text-generation` and `image-text-to-text` models. We plan to expand to diffusers, sentence transformers, and other transformers tasks.


Select a model to see how to run it. The Space lists the Neuron stack the model was tested on, the packages to install on top of it, and the `run.py` script that ran. The script follows the recipe of the [TorchNeuron announcement](https://huggingface.co/blog/hf-torchneuron): it loads the model with `from_pretrained`, sharded when it needs to be, then generates with a static cache and `torch.compile(backend="neuron")`.

On a Trainium2 (`trn2`) instance with that stack, for example in the [AWS Neuron Deep Learning Container](https://github.com/aws-neuron/deep-learning-containers#torch-neuronx), install the packages, then run:

```
python3 run.py
```
No need for `torchrun`: the script launches its own `torch.distributed` ranks when the model is sharded.

A first run starts by compiling the model's graphs. To skip that step, copy the graphs the same compiler built during the test, from the public [NEFF cache](https://huggingface.co/buckets/aws-neuron/torch-neuronx-neff-cache) bucket. The Space gives you the command, with the right compiler version:

```
hf buckets sync hf://buckets/aws-neuron/torch-neuronx-neff-cache/neuronxcc-<version> /tmp/neff_cache
```
Each test loads the model on a `trn2` instance, sharded over the smallest number of Trainium cores that can hold its weights. Most models are sharded with tensor parallelism. Mixture-of-experts models without a tensor-parallel plan use expert parallelism only. The test then generates 32 tokens and checks them. On a single core, the tokens are compared with those of a CPU run of the same checkpoint. When the model is sharded, a small judge model checks that the text is fluent English.

At the time of writing, only models that fit on 4 Trainium2 devices are tested, which means 16 cores at most. A `PASS` says nothing about throughput, or about longer generations.

Everything the Space shows comes from the public [`aws-neuron/torch-neuronx-model-support`](https://huggingface.co/datasets/aws-neuron/torch-neuronx-model-support) dataset, with one Parquet file per pair of `neuronx-cc` and library versions.

Each row holds a model's result, the error when it failed, the versions of the whole stack and the `run.py` that ran. You can query it directly:

```
import pandas as pd
df = pd.read_parquet("hf://datasets/aws-neuron/torch-neuronx-model-support/data")
df[df.model_id == "Qwen/Qwen3-0.6B"][["neuronx_cc", "library", "library_version", "neuron_cores", "result"]]
```
The [dataset card](https://huggingface.co/datasets/aws-neuron/torch-neuronx-model-support) gives the exact meaning of each result.

Next time you wonder whether a model runs on Trainium, [look it up](https://huggingface.co/spaces/aws-neuron/torch-neuronx-model-support).

## Summary

**TLDR:** Trainium compatibility becomes more credible when users can inspect reproducible model-level results, though today’s narrow test coverage still limits purchasing confidence.

- A new Hugging Face Space reports whether popular Transformers models run unmodified on AWS Trainium through the TorchNeuron backend.
- Each tested entry includes core count, wall time including compilation, peak device memory, package versions, and the exact execution script.
- Users can browse selected, trending, or highly downloaded models and see why an untested model was skipped or judged incompatible.
- Results are tied to specific Neuron compiler and Transformers versions, making them useful but version-dependent rather than permanent compatibility guarantees.
- Current testing covers only Transformers text-generation and image-text-to-text models, with broader libraries and tasks planned.

## 摘要

**重點摘要：** Trainium 相容性有了可重現的逐模型結果後更具可信度，但目前測試範圍仍窄，還不足以完全消除採購疑慮。

- Hugging Face 推出的 Space 會實測熱門 Transformers 模型，確認它們能否透過 TorchNeuron 在 AWS Trainium 上不經修改直接運行。
- 每筆測試列出 Trainium 核心數、包含編譯的總時間、裝置峰值記憶體、套件版本，以及實際使用的執行腳本。
- 使用者可依精選、趨勢或下載排名查找模型；未測試的項目也會標示是尚未排入，還是真的不相容。
- 測試結果綁定特定 Neuron 編譯器與 Transformers 版本，因此是可查證的快照，而非永久相容承諾。
- 現階段只涵蓋 Transformers 的文字生成與圖文轉文字模型，diffusers 等其他類型仍待擴充。