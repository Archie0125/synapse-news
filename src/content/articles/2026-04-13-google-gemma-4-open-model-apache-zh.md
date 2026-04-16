---
title: "Google Gemma 4：採用 Apache 2.0 授權、擊敗 4000 億參數對手的開放權重模型"
summary: "Google 發布的 Gemma 4 系列共四個模型，參數規模從 20 億到 310 億，全部採用完全開放的 Apache 2.0 授權——這是開放式 AI 模型有史以來最重要的效能躍升之一。310 億稠密模型在 Arena AI 排行榜全球名列第三，在 AIME 2026 數學測試中得到 89.2 分，LiveCodeBench 編程測試達 80%，且可免費商業部署、修改與再發布。"
category: "developer-tools"
publishedAt: 2026-04-13T09:05:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "Google Blog – Gemma 4"
    url: "https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/"
  - name: "Google DeepMind – Gemma 4"
    url: "https://deepmind.google/models/gemma/gemma-4/"
  - name: "Google Cloud Blog – Gemma 4"
    url: "https://cloud.google.com/blog/products/ai-machine-learning/gemma-4-available-on-google-cloud"
  - name: "Engadget – Gemma 4"
    url: "https://www.engadget.com/ai/google-releases-gemma-4-a-family-of-open-models-built-off-of-gemini-3-160000332.html"
tags:
  - "Google"
  - "Gemma 4"
  - "開源"
  - "Apache 2.0"
  - "開放權重"
  - "大型語言模型"
  - "開發者工具"
relatedSlugs:
  - "2026-04-13-google-gemma-4-open-model-apache-en"
  - "2026-04-13-stanford-ai-index-2026-report-zh"
  - "2026-04-12-zai-glm51-open-source-swe-bench-zh"
---

2026 年 4 月 2 日，Google 發布 Gemma 4，這不只是一次模型更新，更像是一份意圖宣言。Gemma 4 系列建立在 Google 最新旗艦商用模型 Gemini 3 的研究基礎之上，並以 Apache 2.0 授權發布——完全開放商用、無使用限制、可自由修改與再發布，毋須支付任何授權費。這是 Google 有史以來對具競爭力的 AI 模型採取最寬鬆的授權姿態，而測試成績顯示，這並非虛有其表的姿勢。

## 四款模型，覆蓋所有部署場景

Gemma 4 陣容橫跨四個差異化模型，分別針對不同的部署環境。**Effective 2B（E2B）**和 **Effective 4B（E4B）**專為邊緣裝置設計，包含智慧型手機、筆記型電腦與嵌入式系統，兩者均原生支援文字、圖片、影片與音訊輸入。**26B 混合專家模型（MoE）**和 **31B 稠密模型（Dense）**則瞄準雲端與高效能本地部署，以遠低於其他模型的參數量，達到頂尖級別的推理能力。

四個模型均具備 256K 的上下文視窗，支援逾 140 種語言。可配置的「思考模式（thinking mode）」讓開發者能調節推理深度——對延遲敏感的應用採用快速模式，對複雜多步驟任務則啟用深度模式。這項功能過去僅見於頂級商用閉源模型。

## 改寫開放模型版圖的基準測試成績

這些效能聲稱看起來很大膽，但實際數字驗證了它們。在**Arena AI 文字排行榜**——被業界普遍認為最具實用參考價值的獨立人類偏好排名——31B 稠密模型在全球所有開放模型中**排名第三**，26B MoE 則位居**第六**，兩者均超越其他實驗室規模大得多的模型。

在專項測試中，成績更加亮眼。數學方面，31B 模型在 **AIME 2026** 競賽數學測試中拿下 **89.2 分**——這個分數在不久前還是只有最大型商用模型才能觸及的領域。在程式設計方面，它在 **LiveCodeBench v6** 達到 **80.0%**，對比 Gemma 3 27B 在同一測試的 29.1%，單代提升超過 2.7 倍。

在開發者社群引發最廣泛討論的那句話，來自 Google 自己的模型文件：「按參數量換算，效能最高的開放模型。」這說的是效能與參數量之比——從 Gemini 3 訓練萃取出的 Gemma 4 架構，展現出遠超其體量的能力表現。

## Apache 2.0：改變商業應用計算邏輯的授權轉變

測試成績固然重要，但授權的故事對整個產業格局的影響或許更深遠。早期的 Gemma 系列採用自訂授權，對特定使用情境有所限制，讓商業部署方——尤其是涉及再發布或衍生模型訓練的應用——面臨法律上的不確定性。Gemma 4 切換至 **Apache 2.0** 後，這些限制全部消失。

對於開發 AI 原生產品的新創公司而言，這大幅改變了自建與採購的考量。一個在關鍵基準測試上媲美乃至超越許多商用 API 的模型，自行部署時無需按呼叫量付費，且在商業再發布上零授權風險，根本地改變了 AI 產品開發的經濟學。過去兩年，大型企業的法務團隊逐字審查各種 AI 模型授權條款；Apache 2.0 一出，這場討論宣告終結。

與 Meta Llama 系列相比，後者的自訂授權在技術上對一定規模的商業使用仍有所限制——Gemma 4 的選擇是刻意的差異化，開發者社群對此心知肚明。

## 第一天即完整的生態系整合

Google 在 Gemma 4 發布上投入大量資源，確保模型在理論上具備價值的同時，在實踐上也立即可用。發布首日即整合的工具包括：

- **Hugging Face**（Transformers、TRL、Transformers.js、Candle）
- **vLLM**、**llama.cpp**、**MLX**、**Ollama**、**SGLang** 用於本地推理
- **NVIDIA NIM 和 NeMo** 用於企業部署
- **Google AI Studio** 提供 31B Dense 和 26B MoE 雲端存取
- **Google AI Edge Gallery** 用於 E2B 和 E4B 的裝置端部署
- **LM Studio**、**Unsloth**、**Baseten**、**Keras**、**Docker** 等

E2B 模型針對 Google 的 LiteRT-LM 行動推理引擎專項優化，讓智慧型手機部署真正實用，而非玩具等級的展示。結合 E4B，這為開發者提供了可信賴的裝置端 AI 技術棧，特別適合雲端資料傳輸受限於合規或隱私考量的敏感應用場景。

## 原生多模態，而非事後補丁

Gemma 4 的多模態能力值得特別關注，因為其架構設計有別於過去的做法。許多模型是將視覺能力後期拼接到語言主幹上，而 Gemma 4 的 E2B 和 E4B 模型則從架構底層原生整合音訊與視覺處理。較大的 26B 和 31B 模型則進一步延伸至影片理解。

對於需要在不調用獨立專用模型的情況下推理圖片、音訊或影片的開發者而言，這大幅簡化了技術棧。一個採用 Apache 2.0 授權、在單一上下文視窗中同時處理文字、程式碼、語音和視覺的模型，是比串接多個 API 品質上不同的開發原語。

## Gemma 4 對開放模型生態的意義

2026 年初，開放權重 AI 生態的競爭已出乎意料地激烈。Meta 的 Llama 系列、Mistral 模型家族，以及數家中國實驗室的發布，共同構建了一個能力不俗的開放模型世界。但 Gemma 4 在多個維度同時提升了天花板：更強的能力、更全面的多模態支援、更開放的商業授權，以及有史以來最完整的發布首日生態整合。

對 Google 而言，戰略邏輯清晰：以 Gemma 為核心形成繁榮的開放模型生態，有助於壯大 Google Cloud、Google AI Studio 及更廣泛 Google AI 平台的開發者群體。每一個基於 Gemma 4 構建應用的公司，都是潛在的 Google Cloud 基礎設施客戶。

對開發者生態而言，一個具有 Apache 2.0 授權、全球排名第三、310 億參數的模型出現，意味著對商用 API 依賴的計算邏輯已真正改變。支撐付費使用閉源模型的效能溢價已大幅收窄。它是否已完全消失，是每個開發團隊現在都必須自行判斷的問題。

對許多人來說，2026 年 4 月的答案，和六個月前會截然不同。
