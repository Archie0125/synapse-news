---
title: "Google 以 Apache 2.0 釋出 Gemma 4——授權條款的改變或許比評測成績更重要"
summary: "Google DeepMind 於 4 月 2 日發布 Gemma 4，首次採用 Apache 2.0 開源授權，移除了前幾代限制商業應用的自定義條款。旗艦版 31B Dense 模型在 Arena AI 排行榜全球排名第三，超越眾多商業閉源系統；而 26B MoE 版本以僅約 4B 的推理成本達到全球第六的性能表現。"
category: "developer-tools"
publishedAt: 2026-04-06T09:25:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "Google Blog: Gemma 4 — Byte for byte, the most capable open models"
    url: "https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/"
  - name: "VentureBeat: Google releases Gemma 4 under Apache 2.0"
    url: "https://venturebeat.com/technology/google-releases-gemma-4-under-apache-2-0-and-that-license-change-may-matter-more-than-benchmarks"
  - name: "Revolution in AI: Gemma 4 Apache License Change Analysis"
    url: "https://www.revolutioninai.com/2026/04/gemma-4-apache-license-benchmark-open-model-2026.html"
tags:
  - "google"
  - "gemma"
  - "開源"
  - "LLM"
  - "Apache 2.0"
  - "評測"
relatedSlugs:
  - "2026-04-04-open-source-llm-race-zh"
  - "2026-04-04-cursor-devin-war-zh"
---

4 月 2 日，Google DeepMind 發布了 Gemma 4。開發者社群的目光第一時間落在了發布部落格中幾乎像是附帶說明的一行字：本次釋出採用 **Apache 2.0 授權**。

這一行字對所有在生產環境中使用開放權重 AI 模型的人而言，意義難以高估。前幾代 Gemma 採用 Google 自訂的 Gemma 使用條款，帶有使用限制和歸屬要求，在商業應用上造成了明顯摩擦。Apache 2.0 徹底消除了這些障礙：你可以在商業產品中使用 Gemma 4、修改它、再發行它，甚至基於它構建閉源產品——無需付費授權、無需標注來源、也不需要梳理 Google 的特定使用規範。

評測數字本身已經令人印象深刻，但授權條款的變化才是讓 Gemma 4 在性質上與前幾代截然不同的關鍵。

## 四個模型，一次發布

Gemma 4 以四個不同規格的模型家族形式推出，各自針對不同部署場景：

- **E2B**（23 億有效參數）：專為設備端與嵌入式應用設計，包括行動裝置部署。需要在手機或邊緣硬體上執行推理時，這是首選。
- **E4B**（45 億有效參數）：在保持消費者硬體可行性的同時提升能力，適合 GPU 記憶體有限的場景。
- **26B A4B MoE**（總參數 260 億，激活參數 38 億）：混合專家架構（Mixture-of-Experts），以等效大型模型中的一小部分算力成本提供強勁性能。38 億的激活參數使推理成本接近小模型，而非大型模型。
- **31B Dense**（旗艦版）：310 億參數的全密集模型，追求最大性能，設計為在高端工作站或單伺服器 GPU 環境下運行。

這樣的架構選擇反映了 Google 對部署現實的深刻理解：並非所有人都需要 31B。許多生產用例反而更適合 E2B 或 MoE 版本，四個模型都被視為一線發布，而非縮水的附加品。

## 評測表現：全球第三，不只是開源模型中

最令人矚目的數字是：31B Dense 模型在 Arena AI 文字排行榜上全球排名**第三——涵蓋所有模型，包括 OpenAI、Anthropic 和 Google 自家 Gemini 系列的閉源商業系統**。

Arena AI 排行榜不是學術評測的堆疊；它基於真人盲測偏好投票——真實用戶在不知道哪個模型產生哪個答案的情況下並排比較輸出。這可以說是目前最貼近人類需求的性能評測，Gemma 4 的 31B 排在第三，超越了許多運行成本更高的系統。

在結構化評測上，表現同樣出色。31B 在數學競賽評測 AIME 2026 上得分 89.2%，相比前代 Gemma 3 27B 的 20.8%——單代提升了四倍的數學推理能力。MMLU Pro（廣泛知識）得分 85.2%；LiveCodeBench v6（競賽程式設計）達到 Codeforces ELO 2,150，穩穩落在競賽程式設計師梯隊。

值得一提的是，26B MoE 版本在 Arena AI 排行榜上達到全球第六，超越參數規模是其二十倍的模型。MoE 架構的效率優勢在這裡充分體現：以約 4B 激活參數的推理成本，換來全球第六的表現。

## Apache 2.0 為何改變了一切

要理解授權條款為何如此重要，必須正視舊版 Gemma 使用條款帶來的實際困境。建構商業產品的開發者面對「什麼是可接受使用」的法律不確定性；擁有法律團隊的企業在部署前需要審查這份自訂授權；蒸餾（Distillation）——用較大模型的輸出訓練較小模型的過程——在舊授權下存在法律灰色地帶，使部分微調工作流程難以為繼。

Apache 2.0 用一份每個開發者、法律團隊和企業採購部門都已熟悉的授權解決了所有這些問題。它是 Linux、Kubernetes、TensorFlow 以及數百個基礎架構組件的授權。選擇它，代表 Google 認真地將 Gemma 定位為基礎設施，而不只是展示模型。

實際效應將隨時間複利發酵：原本因授權問題排除 Gemma 的 Hugging Face 存儲庫、LangChain 整合、微調流程和企業部署，現在可以無限制採用；從 Gemma 4 蒸餾到更小的自定義模型，法律層面完全清晰；希望在不揭露底層模型的情況下交付產品的公司，也可以放心行事。

## 對開放權重生態的意義

過去兩年，開放權重模型競賽由三種力量驅動：性能、安全限制，以及授權。Meta 的 Llama 系列之所以主導開放生態，很大程度上是因為它的授權雖非完全開放，但比其他方案對商業更友善。Mistral 在效率和歐洲資料主權上積極競爭。Google 的 Gemma 有強勁的性能故事，但授權造成摩擦。

Gemma 4 搭配 Apache 2.0，徹底移除了這個摩擦。加上全球第三的性能表現，Google 如今對開放權重生態的核心地位提出了有力主張——不只針對研究者，更針對需要可部署、無法律風險模型的基礎架構構建者、企業開發者和新創創辦人。

時機也值得關注。Apache 2.0 的切換發生在開放權重模型生態快速成熟之際，Mixtral、DeepSeek、Llama 和 Qwen 都在積極爭奪開發者心佔率。Google 顯然已判斷，限制性授權是它再也承擔不起的競爭劣勢。

## 開發者體驗與部署

Gemma 4 家族從第一天起就在 Google AI Studio、Vertex AI、Kaggle 和 Hugging Face 上提供。Google 發布了 E2B 和 E4B 模型的量化版本，支援純 CPU 推理，將可存取的部署範圍擴展至無 GPU 硬體。MoE 和 31B Dense 模型以 BF16 及 INT4/INT8 量化格式提供本地部署。

對大多數開發者而言，最快的上手路徑是透過 Hugging Face 的 transformers 函式庫——Gemma 4 無需特殊依賴即可整合。微調文件和 LoRA adapter 範例也隨同發布。

頂尖的評測表現、不受限制的開源授權，以及完善的部署工具鏈，使 Gemma 4 成為生產環境開放權重模型的有力競爭者。評測排名會隨時間更迭，但 Apache 2.0 是永久的——而這或許才是 Gemma 4 最持久的競爭優勢。
