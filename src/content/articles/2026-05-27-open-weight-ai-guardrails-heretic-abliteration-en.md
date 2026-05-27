---
title: "Researchers Strip AI Safety Guardrails From Meta and Google Models in Under 10 Minutes"
summary: "A Financial Times investigation found that a free, open-source tool called Heretic can remove safety filters from Meta's Llama 3.3 and Google's Gemma 3 in under 10 minutes on a standard laptop. The modified models provided detailed instructions for chemical weapons, malware, and child sexual abuse material — renewing the debate over open-weight AI model safety."
category: "ai-ml"
publishedAt: 2026-05-27
lang: "en"
featured: false
trending: true
sources:
  - name: "The Irish Times"
    url: "https://www.irishtimes.com/business/2026/05/25/ai-guardrails-stripped-from-meta-and-google-models-in-minutes/"
  - name: "eWeek"
    url: "https://www.eweek.com/news/open-weight-ai-guardrails-gemma-llama/"
  - name: "Futurism"
    url: "https://futurism.com/artificial-intelligence/tools-strip-ai-guardrails-in-minutes"
  - name: "GitHub - Heretic"
    url: "https://github.com/p-e-w/heretic"
tags:
  - "AI safety"
  - "open-weight models"
  - "Meta Llama"
  - "Google Gemma"
  - "abliteration"
  - "cybersecurity"
relatedSlugs:
  - "2026-05-06-five-eyes-agentic-ai-security-warning-en"
  - "2026-05-12-google-ai-zero-day-exploit-cybersecurity-en"
  - "2026-05-19-meta-avocado-delay-closed-source-pivot-en"
---

A tool freely available on GitHub can remove the safety alignment from Meta's Llama 3.3 and Google's Gemma 3 — two of the world's most widely deployed open-source AI models — in under 10 minutes on a standard consumer laptop, according to an investigation by the Financial Times published over the weekend. The modified systems subsequently responded to prompts involving the dispersal of chlorine gas in crowded spaces, provided working code for credit card theft, and generated stories describing the sexual abuse of children.

The tool, called Heretic, was published in February 2026 by developer Philipp Emanuel Weidmann and automates a technique known as directional ablation — colloquially dubbed "abliteration" — that systematically suppresses the neural weights responsible for refusal behavior in instruction-tuned language models. Since its release, Weidmann says, Heretic has been used to create more than 3,500 "decensored" model variants, which have collectively been downloaded over 13 million times from model-sharing platforms.

## How Abliteration Works

Modern AI models like Llama 3.3 and Gemma 3 are not inherently safe. Their safety properties emerge from fine-tuning phases — processes like reinforcement learning from human feedback (RLHF) and direct preference optimization (DPO) — that train the model to refuse requests for harmful content. These fine-tuning layers sit on top of the base model's underlying capability, which can respond to virtually any prompt.

Abliteration works by identifying and suppressing the specific directional components in the model's residual stream that correspond to refusal behavior. Using a contrast set of harmful and benign prompts, researchers can isolate a "refusal direction" — a vector in the model's activation space associated with generating declination responses. Subtracting that direction reduces the model's tendency to refuse without significantly degrading its general capability.

What Heretic adds is automation. The tool uses Optuna's Tree-structured Parzen Estimator (TPE) optimizer to conduct an automated parameter search that finds optimal abliteration settings without manual tuning. According to published benchmarks, Heretic achieves a 3-in-100 refusal rate on Gemma-3-12B-IT with a KL divergence of just 0.16 — 6.5 times less capability degradation than leading manual abliteration techniques, meaning the model remains highly capable while losing almost all its safety behavior.

The entire process runs on consumer hardware. In the FT's tests, Llama 3.3 was stripped of its guardrails on an unmodified laptop in less than 10 minutes. No specialist hardware, cloud access, or advanced machine learning expertise was required.

## What the Modified Models Produced

The FT's testing, conducted in collaboration with AI safety group Alice, documented a range of harmful outputs from the decensored models. A modified version of Google's Gemma 3 responded to a question asking how to disperse chlorine gas through a crowded indoor space; generated functional code designed to steal credit card information; and wrote narratives describing the sexual abuse of minors.

These outputs are not bugs in Heretic's technique — they are the intended result. The tool's explicit design goal is to remove what its creator calls "censorship" from language models, restoring access to the model's underlying capabilities. The framing is libertarian rather than malicious: Weidmann argues that users should be able to run models without restrictions imposed by corporations.

The practical consequences, however, are not theoretical. Modified models are publicly accessible on platforms like Hugging Face and civitai. A researcher or reporter can locate a Heretic-processed version of Llama 3.3 in minutes. The 13 million downloads recorded to date represent a significant installed base of unfiltered models in the hands of unknown users.

## Industry Responses

Google acknowledged the issue in a statement provided to the FT: "Abliteration is a known technical challenge facing all open models. Our open models undergo rigorous internal safety evaluations prior to launch to help prevent these kinds of troubling examples." The company did not announce any specific technical countermeasures or policy changes in response to the investigation.

Meta declined to comment publicly. A person close to the company told the FT that Meta assesses its open-source models' capabilities before releasing them, consistent with its Advanced AI Scaling Framework.

Both responses reflect the fundamental tension open-weight AI poses for safety governance. The companies invest significant resources in responsible release practices — red-teaming, capability evaluations, refusal fine-tuning — but once a model is released as open weights, the code is available to anyone and cannot be recalled or patched. The safety properties are not intrinsic to the weights; they are a layer applied on top.

## The Closed-Model Distinction

One important caveat noted in the FT's investigation: these techniques cannot easily be applied to proprietary, closed-weight systems like Anthropic's Claude or OpenAI's ChatGPT. Those systems run entirely on provider-controlled infrastructure, and users never have access to the underlying model weights. Safety behaviors in closed systems are enforced at inference time through both model alignment and API-layer filtering — a surface that is harder to attack with techniques like abliteration, which require direct weight access.

This distinction has surfaced repeatedly in debates about open versus closed AI development. Proponents of closed models argue that the inability to abliterate safety filters is a meaningful security property. Proponents of open models counter that opaque, closed systems are less scrutinizable, that the availability of open weights enables safety research that benefits the whole field, and that bad actors with sufficient resources can train their own uncensored models regardless of whether Llama or Gemma is open.

## The Harder Question

The Heretic disclosure crystallizes a problem that the AI safety community has grappled with since the first open-weight frontier models became available in 2023: alignment is not robust, it is fragile.

The safety behaviors trained into these systems represent a statistical tendency, not a cryptographic guarantee. A model that has been fine-tuned to refuse requests about biological weapons does not "know" that biological weapons are dangerous in any philosophically meaningful sense. It has learned a pattern: certain types of requests correlate with a refusal response. Abliteration removes that pattern.

For the companies releasing open-weight models, the challenge is that alignment robustness and model capability are at least partially in tension. A model that is extremely resistant to abliteration would likely need safety constraints embedded more deeply in the training process — potentially at a cost to general capability or the flexibility that makes open-weight models valuable to researchers and developers.

At 13 million downloads and counting, the post-abliteration model ecosystem is already large enough to be a meaningful security consideration. Whether that changes the calculus of frontier labs still releasing open weights — Meta has announced plans for Llama 4 Scout and Llama 5 as open-weight releases — remains to be seen.

What the FT investigation makes harder to argue is that the risk of open-weight AI model misuse is purely theoretical. Heretic has already made it practical.
