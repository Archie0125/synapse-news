---
title: "Meta Launches Muse Spark, Its First Proprietary AI Model From Superintelligence Labs"
summary: "Meta has officially launched Muse Spark, the first AI model built by Meta Superintelligence Labs under Alexandr Wang. The proprietary model marks a dramatic break from Meta's open-source Llama tradition, competing with frontier models from OpenAI and Google on benchmarks while showing standout strength in health reasoning and multimodal vision tasks."
category: "ai-ml"
publishedAt: 2026-04-09
lang: "en"
featured: true
trending: true
sources:
  - name: "Meta AI Blog"
    url: "https://ai.meta.com/blog/introducing-muse-spark-msl/"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/04/08/meta-debuts-first-major-ai-model-since-14-billion-deal-to-bring-in-alexandr-wang.html"
  - name: "Fortune"
    url: "https://fortune.com/2026/04/08/meta-unveils-muse-spark-mark-zuckerberg-ai-push/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/goodbye-llama-meta-launches-new-proprietary-ai-model-muse-spark-first-since"
  - name: "Artificial Analysis"
    url: "https://artificialanalysis.ai/articles/muse-spark-everything-you-need-to-know"
tags:
  - "Meta"
  - "Muse Spark"
  - "Alexandr Wang"
  - "AI models"
  - "Superintelligence Labs"
  - "LLM"
  - "multimodal"
relatedSlugs:
  - "2026-04-08-meta-hybrid-open-source-models-en"
  - "2026-04-04-open-source-llm-race-en"
  - "2026-04-05-openai-gpt-oss-open-weight-en"
---

Nine months after Mark Zuckerberg brought in Alexandr Wang in a deal that valued Scale AI at roughly $14 billion, Meta has delivered its first answer to the question everyone was really asking: can Wang actually build something that competes with OpenAI and Google? On Wednesday, Meta launched Muse Spark — a fully proprietary large language model and the inaugural release from Meta Superintelligence Labs (MSL) — to a cautious but genuine industry reception.

The model, which was developed under the codename "Avocado," represents a deliberate pivot in Meta's AI strategy. For years, the company's competitive identity was inseparable from its open-source Llama series. Muse Spark abandons that posture almost entirely. The model will be proprietary, with Meta noting only that it "hopes to open-source future versions." In a company whose research culture was built on publishing and sharing, the shift carries real symbolic weight.

## What Muse Spark Can Do

Muse Spark accepts voice, text, and image inputs, but generates text-only output — a constraint Meta says it plans to address in future releases. The model runs in two modes: standard and "Contemplating," the latter spinning up parallel subagents to tackle complex, multi-part problems. Meta describes Contemplating mode as capable of competing "with the extreme reasoning modes of frontier models such as Gemini Deep Think and GPT Pro."

On the Artificial Analysis Intelligence Index, a composite benchmark of model capabilities, Muse Spark scores 52 — placing it in the top five AI models globally, ahead of Claude Sonnet 4.6, GLM-5.1, MiniMax M2.7, and Grok 4.20, but trailing Gemini 3.1 Pro Preview and GPT-5.4. It is not the state of the art, but it is unambiguously competitive.

Where Muse Spark is genuinely exceptional is in health-related reasoning. On HealthBench Hard — a demanding benchmark for medical query response — the model scored 42.8%, surpassing all rivals including GPT-5.4 and Claude Opus 4.6. Meta invested heavily in health-focused training data, a priority Wang made explicit when he joined: his ambition was not just a general-purpose frontier model, but one with deep domain expertise in medicine and science.

Multimodal vision performance is another bright spot. Muse Spark scored 80.5% on MMMU-Pro, ranking second globally behind only Gemini 3.1 Pro Preview (82.4%). In Contemplating mode, it outperforms both Gemini and GPT-5.4 on CharXiv Reasoning — a benchmark measuring AI's ability to interpret scientific figures and charts — scoring 86.4 versus Gemini's 80.2 and GPT-5.4's 82.8.

Reasoning benchmarks also show strength. On Humanity's Last Exam, a notoriously difficult test of expert-level knowledge, Muse Spark's Contemplating mode scored 50.2%, ahead of GPT-5.4 Pro and Gemini Deep Think.

## The Efficiency Play

Beyond benchmark positioning, Meta is making a pointed argument about compute efficiency. The company claims Muse Spark can reach the same capability level as Llama 4 Maverick — its previous generation midsize model — using more than ten times less compute. That efficiency claim matters in a market where inference cost is increasingly a strategic differentiator, and where the hyperscalers running Meta AI across billions of users are acutely sensitive to GPU bills.

The nine months Wang and MSL spent on Muse Spark were not just spent training a model — they rebuilt Meta's entire AI infrastructure from scratch. New training pipelines, revised data curation methods, and a retooled evaluation framework were all part of the overhaul. The company says this ground-up rebuild is what enabled the compute efficiency gains.

## A Gap That Remains: Coding

Meta is unusually candid about where Muse Spark still falls short. Coding is the acknowledged weak point. A Meta executive told reporters that while the model is "competitive at certain tasks, including multimodal understanding and processing health information, there is a gap in coding compared to available models." This matters for developer adoption — the cohort most likely to build on a new model API and generate the third-party ecosystem Meta needs to stay relevant.

The company says it continues "to invest in areas with current performance gaps, specifically long-horizon agentic systems and coding workflows." Given that Muse Spark only completed a nine-month development cycle, a coding-focused iteration in 2026 seems likely.

## Rollout and Availability

Muse Spark is currently powering meta.ai and the Meta AI assistant website, with a US-only rollout at launch. Integration into WhatsApp, Instagram, Facebook, Messenger, and Meta's AI glasses is expected in the coming weeks. An API private preview is available for select enterprise partners.

The model is not open-source, and Meta has not committed to a timeline for any public weights release. This puts the company in the unfamiliar position of going against the grain of the developer culture it spent years cultivating through Llama. Whether that trade-off pays off commercially will be watched closely.

## The Bigger Bet

The Muse Spark launch is as much about credibility as it is about capability. Meta spent $14 billion on the Wang deal — through a combination of valuation, equity, and commitments — and spent the following months watching OpenAI roll out GPT-5.4, Anthropic confirm Claude Mythos, and Google ship Gemini 3.1 Pro. The company needed to demonstrate that the investment was producing real results.

What Muse Spark offers is a model that is genuinely competitive with the best currently available systems in specific domains — health, vision, and complex reasoning — while being unusually efficient. It is not, by Meta's own admission, the overall frontier leader. But it establishes Meta as a serious full-stack AI lab rather than an open-source model distributor, and it sets the stage for the next phase of MSL's roadmap.

The Llama era of Meta AI is not over — the company says open-source remains part of its long-term strategy. But Muse Spark marks a clear inflection point: Meta is now competing for the enterprise and developer audience on proprietary terms, with a model designed to win in production rather than just on leaderboards. Whether the bet on Wang's vision pays off will become clearer over the next several quarters.
