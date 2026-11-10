---
category: ai-ml
faqs:
- answer: 這是 Elith 與 NVIDIA 發布的開放合成人物資料集，把 Nemotron-Personas-Japan 擴展到金融領域，以百萬筆規模結合日本官方統計、家庭財務和金融素養資料。
  question: Nemotron-Personas-Finance-Japan 是什麼？
- answer: 金融業的隱私法規和合規要求嚴格，真實客戶資料很難使用。能反映真實人口結構、家戶組成和資產狀況的合成資料，讓團隊不必暴露真人資訊也能開發和測試代理式
    AI。
  question: 金融 AI 為什麼要用合成資料？
- answer: 損保 Japan、東京海上控股、福岡銀行、瑞穗等日本金融機構和產業協會提供了意見，讓資料集更貼近實際金融應用。
  question: 哪些機構參與了資料集設計？
featured: false
lang: zh
publishedAt: '2026-11-09T15:05:57+00:00'
relatedSlugs: []
sources:
- name: Hugging Face Blog
  url: https://huggingface.co/blog/nvidia/nemotron-personas-finance-japan
summary: NVIDIA 與 Elith 合作打造的日本金融合成人物誌資料集，巧妙繞開了隱私法規的限制；但合成資料再逼真，終究還得經得起真實世界的檢驗。
tags:
- ai-ml
- open-source
- industry
title: Nemotron-Personas-Finance-Japan：呈現日本人口結構與金融樣貌的合成資料集
trending: false
type: news
---

[Viewer • Updated  •  100k •  2  •  2](/datasets/nvidia/Nemotron-PII-Japan)  

# 
		
	
		Nemotron-Personas-Finance-Japan: A Synthetic Dataset Capturing Japan's Demographics and Financial Context

*A compound AI approach to Japanese personas grounded in real-world distributions*

In the financial sector, the utilization of real-world data faces significant constraints due to strict privacy regulations, compliance requirements, and the need for advanced domain expertise. In this context, the development of agentic AI in the financial domain requires synthetic data capable of avoiding the risks of using real data while reflecting demographics, household structures, and asset statuses to reproduce diverse, realistic financial scenarios.

To address these challenges, [Elith](https://www.elith.ai/) and NVIDIA have released [**Nemotron-Personas-Finance-Japan**](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Finance-Japan), a financial domain extension of the open-source persona dataset "[Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan)." To our knowledge, it is the first open persona dataset at million-record scale that pairs Japan’s official statistics with household finance and financial literacy data. Built upon official government statistics, this dataset was developed using [NeMo SDG-PGMs](https://github.com/NVIDIA-NeMo/SDG-PGMs), a probabilistic graphical model framework for synthetic data generation (SDG), and [NeMo Data Designer](https://github.com/NVIDIA-NeMo/DataDesigner), an enterprise synthetic data generation system. Furthermore, to enhance the practical utility of the dataset in financial use cases, it was designed by incorporating insights and feedback provided by leading domestic financial institutions and industry associations, including Sompo Japan, Tokio Marine Holdings, Bank of Fukuoka, Mizuho Financial Group, Meiji Yasuda Life Insurance, and the Financial Data Utilization Association (FDUA).

This dataset expands the environment where Japanese developers and enterprises can develop and evaluate AI tailored to local and industry requirements, without using real customer data. Released under the **CC BY 4.0** license, it is available for commercial use. **From building conversational agents to customer simulation and model evaluation, it supports practical financial AI development**. The [Nemotron-Personas collection](https://huggingface.co/collections/nvidia/nemotron-personas), including Nemotron-Personas-Finance-Japan, is designed to seamlessly integrate with the user simulation framework [NeMo User Sim](https://github.com/NVIDIA-NeMo/UserSim), enabling instant execution of simulations drawn from diverse distributions consistent with the real world.

- **9M personas total** (1M records x 9 personas each), written in natural Japanese
- **50 fields per record**: 9 persona fields, 11 persona attributes, and 30 contextual fields based on official demographic and labor statistics
- **\~1.5B tokens total**, including \~750M persona tokens
- **\~950k unique names**
- **1600+ occupation categories** reflecting Japan's workforce
- **Comprehensive coverage** across demographic, regional, asset distribution, and personality trait axes
- **Diverse persona types**: Occupations, sports, arts, travel, cooking, finance, financial behavior, and financial concerns
- **Natural language persona attributes**: Cultural background, skills and expertise, career goals and aspirations, hobbies and interests, household/parental/financial background, attitudes toward money, and financial planning
- **Available for both commercial and non-commercial use** under the CC BY 4.0 license

It was built using NVIDIA’s framework for synthetic data generation, **NeMo Data Designer**. This compound AI system enables complex Jinja templating, Pydantic validation, structured outputs, automated retries, and support for multiple generation backends. This is the essential toolset required for generating such large-scale synthetic datasets. In addition, the following models were utilized:

- **NeMo SDG-PGMs (Apache-2.0)**: A probabilistic graphical model framework for statistically grounded data generation
- **gemma-4-31B-it (Apache-2.0)**: For Japanese text generation

Nemotron-Personas-Finance-Japan was designed to align with Japan's official demographic and labor statistics while taking into account key considerations essential for AI training:

- **Education**: Where national statistics broadly aggregate degree levels, we introduced finer granularity to enable the model to reflect diverse educational pathways.
- **Occupation**: We incorporated additional categories (such as business owners and specialized professions) to broaden the spectrum of occupations used for training.
- **Life Stages**: We modeled scenarios that rarely surface prominently in statistics, such as students, retirees, and periods of unemployment, to represent more realistic personas.
- **Household Finances**: In addition to individual income and spending propensity, we incorporated household-level financial and real assets to replicate diverse economic backgrounds.
- **Digital & Financial Literacy**: By including internet and smartphone usage along with financial literacy, we enabled the model to precisely capture consumer profiles in financial use cases.

Every persona is fully synthetic. No real individuals are represented, and the dataset is designed to reduce privacy risk. Demographics and household finances follow official statistics and public survey data, and names follow real Japanese naming patterns. Personas are built from these distributions, not from records about real people.

Nemotron-Personas-Finance-Japan is built first for teams creating financial AI in Japan, at banks and insurers and at the startups and integrators that serve them. Each persona carries household finances and financial literacy alongside demographics. Teams can use them to build customer-service agents, evaluate sales conversations/marketing initiatives, run user simulations in NeMo User Sim, and red-team customer-facing AI.

The release also serves anyone building for Japanese users. It holds 9M personas, 50% more than Nemotron-Personas-Japan, across 50 fields instead of 22. That gives any Japanese-language project finer slices of the population to train and test on.

The synthetic personas in this dataset can be leveraged for:

- **Multi-turn conversation**: Using personas as "seeds" to generate human-like dialogue datasets.
- **Domain-specific AI development**: Generating datasets to build AI assistants tailored to realistic scenarios in financial use cases.
- **Bias testing and fairness**: Evaluating how models and AI agent systems perform across rural and urban divides, various age groups, educational backgrounds, and economic circumstances to check whether AI performs consistently across Japanese society.

Access to diverse, high-quality training data that reflects real-world populations has long been a challenge in AI development. Enterprise AI development has predominantly relied on private data, creating barriers for researchers, startups, and particularly AI developers in regions with limited available data.

- **Data Diversity**: Reflects the full spectrum of Japan's population, which helps reduce biased training and the risk of [model collapse](https://medium.com/data-science/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai-7cd380208d14).
- **Cultural Authenticity**: Reduces reliance on Western-centric datasets and supports the development of [Sovereign AI systems](https://www.nvidia.com/en-us/lp/industries/global-public-sector/sovereign-ai-technical-overview/).
- **Privacy and Governance**: Aligned with Japan’s innovation-first approach to AI governance. Every persona is synthetic, so no customer data is needed to build or test with it.

By releasing Nemotron-Personas-Finance-Japan under CC BY 4.0, we provide access to enterprise-grade, high-quality synthetic data, empowering anyone to build culturally grounded AI systems with lower cost and less privacy risk.

[Nemotron-PII-Japan](https://huggingface.co/datasets/nvidia/Nemotron-PII-Japan) launches the same day. It holds 100,000 synthetic Japanese business documents with labeled personal information, for training and testing detection and redaction models. Its documents are built on Nemotron-Personas-Japan. Use Nemotron-Personas-Finance-Japan to simulate customers, and Nemotron-PII-Japan to test how your pipeline protects their data.

You can download this dataset using the command below to help develop AI that genuinely understands Japanese culture and language.

```
from datasets import load_dataset
ds = load_dataset("nvidia/Nemotron-Personas-Finance-Japan")
```
**Use cases for building production-ready applications:**

- Using personas as seeds for dialogue generation
- Fine-tuning models with culturally grounded data
- Building personalized engines that reflect Japan's overall demographic makeup
- Developing domain-specific AI agents equipped with Japanese context

From teams building AI in Japan to global developers aiming for broader regional deployment, [Nemotron-Personas-Finance-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Finance-Japan) dataset provides the authentic, privacy-conscious foundation required for your applications.

## Summary

**TLDR:** NVIDIA and Elith's synthetic Japanese finance personas are a clever workaround for privacy rules, but synthetic realism still has to survive real-world testing.

- Elith and NVIDIA released Nemotron-Personas-Finance-Japan, a financial extension of the open-source Nemotron-Personas-Japan dataset.
- They describe it as the first open, million-record-scale persona dataset that pairs Japan's official statistics with household finance and financial literacy data.
- It was built with NeMo SDG-PGMs, a probabilistic graphical model framework, and NeMo Data Designer for synthetic data generation.
- Major Japanese financial institutions, including Sompo Japan, Tokio Marine Holdings, Bank of Fukuoka and Mizuho, gave input on the design.
- It targets agentic AI in finance, where strict privacy and compliance rules make real customer data hard to use.

## 摘要

**重點摘要：** NVIDIA 和 Elith 推出的日本金融合成人物資料集，是繞過隱私法規的聰明解法。但合成資料夠不夠真實，最後還是得在真實場景裡驗證。

- Elith 與 NVIDIA 發布 Nemotron-Personas-Finance-Japan，這是開源資料集 Nemotron-Personas-Japan 的金融領域擴充版。
- 官方稱它是第一個把日本官方統計和家庭財務、金融素養資料結合起來的百萬筆規模開放人物資料集。
- 資料集使用機率圖模型框架 NeMo SDG-PGMs 和合成資料生成系統 NeMo Data Designer 建置。
- 損保 Japan、東京海上控股、福岡銀行、瑞穗等日本大型金融機構參與提供設計意見。
- 主要服務金融業的代理式 AI 開發，因為嚴格的隱私和合規規範讓真實客戶資料很難使用。