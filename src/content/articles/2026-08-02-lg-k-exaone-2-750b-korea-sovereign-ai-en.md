---
title: "Korea's Biggest AI Bet: LG Releases K-EXAONE 2.0, a 750B Open-Source Model Under Apache 2.0"
summary: "LG AI Research has released K-EXAONE 2.0, a 750-billion-parameter Mixture-of-Experts model and the largest AI foundation model ever built in South Korea. Developed under the national Sovereign AI Foundation Model Project and released under the permissive Apache 2.0 license, the model scores 70.1 across 24 benchmarks and outperforms rivals on long-context and multilingual tasks—arriving days after a competing 700B Korean model to set off what analysts call an 'AI elimination round' among Korean tech giants."
category: "ai-ml"
publishedAt: 2026-08-02
lang: "en"
featured: false
trending: true
sources:
  - name: "Korea Times"
    url: "https://www.koreatimes.co.kr/business/tech-science/20260731/lg-unveils-750-bil-parameter-frontier-ai-model-k-exaone-20"
  - name: "Korea JoongAng Daily"
    url: "https://www.koreajoongangdaily.com/business/lg-unveils-kexaone-20-koreas-largest-opensource-ai-model/12802076"
  - name: "The Elec"
    url: "https://www.thelec.net/news/articleView.html?idxno=12739"
  - name: "Hugging Face"
    url: "https://huggingface.co/LGAI-EXAONE/K-EXAONE-2.0-750B-A37B"
tags:
  - "llm"
  - "open-source"
  - "korea"
  - "lg"
  - "k-exaone"
  - "mixture-of-experts"
  - "sovereign-ai"
relatedSlugs:
  - "2026-07-27-sk-hynix-nvidia-750b-korea-ai-chip-diplomacy-en"
  - "2026-08-01-deepseek-v4-flash-0731-agent-benchmarks-en"
---

The open-source large language model landscape just got a powerful new entrant—and it comes from an unexpected corner of the AI world. LG AI Research on July 31 released K-EXAONE 2.0 on Hugging Face, a 750-billion-parameter foundation model that stands as the largest AI model South Korea has ever produced. Released under the Apache 2.0 license with full commercial use rights, the model is simultaneously a technical statement and a geopolitical one: South Korea is determined to own a piece of frontier AI, not just the chips that run it.

## The Architecture: Efficiency Through Mixture-of-Experts

K-EXAONE 2.0 is built on a hybrid-attention Mixture-of-Experts (MoE) architecture—the same fundamental approach that has made models like Mistral's Mixtral and DeepSeek's V4 series so computationally attractive. The model has 750 billion total parameters but only activates approximately 37 billion parameters per token during inference. That ratio means K-EXAONE 2.0 delivers responses with the knowledge capacity of a 750B model at the compute cost of roughly a 37B model.

This is the architectural bet that the entire frontier AI industry has converged on: MoE allows models to scale knowledge far beyond what dense architectures can achieve without proportionally scaling inference costs. The 256-expert architecture means the model routes each token through a small committee of specialized sub-networks, rather than activating the entire parameter set every time.

The context window stretches to 262,144 tokens—roughly 200,000 words of English text—making K-EXAONE 2.0 suitable for enterprise document processing, legal analysis, long-form research, and other tasks that overwhelm shorter-context models.

Language support covers 10 languages including Korean, English, Japanese, and Chinese. The multilingual capability is not cosmetic: the model was trained on a carefully curated dataset with particular attention to Korean-language quality, reflecting LG's position as a Korean enterprise and the Sovereign AI initiative's mandate to preserve Korean-language AI capability.

## Performance: Better Than Expected

LG evaluated K-EXAONE 2.0 across 24 standardized benchmarks, achieving an average score of 70.1—more than 10 percent higher than its predecessor K-EXAONE 1.0 (63.3). More meaningful than the headline number are the specific domains where the model excels.

**Long-context understanding** is the model's clearest strength. K-EXAONE 2.0 scored 94.4 on OpenAI-MRCR (multi-hop reading comprehension with retrieval) and 89.6 on Ko-LongBench, which evaluates long-document understanding in Korean. For comparison, GLM-5.1—a strong Chinese open-source competitor—scored 71.5 and 83.6 respectively on the same benchmarks. Across the long-context suite (OpenAI-MRCR, AA-LCR, and Ko-LongBench), K-EXAONE 2.0 averaged more than 10 percent above GLM-5.1.

**Coding and agentic-coding benchmarks** improved by approximately 30 percent compared to the first K-EXAONE generation—a significant jump in an area that has become decisive for enterprise adoption. Organizations deploying AI for software development workflows care deeply about code generation quality, and a 30 percent relative improvement is the kind of number that drives procurement decisions.

**Agentic tool use**, measured on Tau3-Bench Banking, shows the model's ability to operate as an autonomous agent in structured task environments. The 14.2 score positions it competitively for enterprise agentic deployment, particularly in the financial services vertical that Korea's chaebol—including LG—serve extensively.

## The Sovereign AI Context

K-EXAONE 2.0 is the second model developed under South Korea's Sovereign AI Foundation Model Project, an initiative led by the Ministry of Science and ICT (MSIT). The project has a strategic rationale that any country watching the AI concentration among U.S. and Chinese companies would recognize: if frontier AI capabilities are controlled by foreign companies, critical national infrastructure dependent on those models is also controlled by foreign companies.

South Korea's approach has been to use its existing industrial champions—LG, Samsung, SK Telecom, KT—as implementation vehicles for a state-backed AI capability agenda. Rather than building a new government AI lab from scratch, MSIT funds and coordinates model development through companies that already have significant AI research organizations.

The Apache 2.0 license choice is notable within this context. Many sovereign AI initiatives produce models with restrictive licenses that limit commercial use or impose geographic restrictions. LG's decision to release K-EXAONE 2.0 under Apache 2.0 signals confidence that open availability will drive adoption—and that adoption will reinforce Korean language and culture's position in global AI systems, since more users means more feedback and fine-tuning data in Korean.

## Korea's AI Elimination Round

The timing of K-EXAONE 2.0's release adds a competitive dimension that goes beyond model benchmarks. Analysts have noted that two large Korean models—both in the 700B+ parameter class—shipped within days of each other in late July, each from different Korean industrial groups. This near-simultaneous release reflects the broader acceleration of what observers are calling Korea's "AI elimination round": a period of intense competition among Korean tech giants to establish which company (or companies) will anchor Korea's domestic AI ecosystem.

The stakes are significant. The model that becomes the Korean enterprise standard—the default for Korean-language RAG systems, Korean legal document analysis, Korean customer service automation—will generate substantial recurring revenue and influence over domestic AI adoption. With China's leading models facing export restrictions in some international markets and U.S. models potentially subject to different regulatory requirements in Korea, there is a genuine opening for a Korean-first alternative.

## What This Means for the Open-Source LLM Landscape

K-EXAONE 2.0 joins a remarkably competitive open-source frontier. DeepSeek V4 Flash, available at $0.14/$0.28 per million tokens, is the dominant cost-efficiency leader. Meta's Llama series retains the widest developer mindshare. Mistral's Mixtral models are entrenched in European deployments. Google's Gemma family covers the lightweight end.

K-EXAONE 2.0's best case is carving out a position as the preferred model for Korean-language tasks and Asian multilingual deployments—a geography that major U.S. open-source models have not aggressively optimized for. The 10-language support and demonstrated long-context performance in Korean give it a credible claim to that niche, which is not actually niche in absolute user terms: the Korean-speaking market alone is 80 million people, with high AI adoption rates.

For developers building Korean-language applications, K-EXAONE 2.0's Apache 2.0 release means no licensing friction for commercial deployment. Combined with the long-context strengths, it is an immediately viable option for Korean enterprise use cases that today rely on API calls to U.S. frontier models.

The model weights are available on Hugging Face at LGAI-EXAONE/K-EXAONE-2.0-750B-A37B.
