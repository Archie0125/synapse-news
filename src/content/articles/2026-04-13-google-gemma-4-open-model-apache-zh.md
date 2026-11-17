---
title: "Google Gemma 4：採用 Apache 2.0 授權、勝過體積達其 20 倍對手的開放模型"
summary: "Google 發布的 Gemma 4 系列共四個模型，參數規模從 20 億到 310 億，全部採用允許商用的 Apache 2.0 授權，Google 稱其為迄今能力最強的開放模型系列。310 億稠密模型在 Arena AI 文字排行榜的開放模型中名列第三，260 億模型則排名第六。"
category: "developer-tools"
publishedAt: 2026-04-13T09:05:00Z
modifiedAt: 2026-11-15T00:00:00Z
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

2026 年 4 月 2 日，Google 發布 Gemma 4，這不只是一次模型更新，更像是一份意圖宣言。Gemma 4 系列建立在與 Gemini 3 相同的研究基礎之上，並以允許商用的 Apache 2.0 授權發布。早期的 Gemma 模型採用 Google 自家的 Gemma 授權。

## 四款模型，覆蓋所有部署場景

Gemma 4 陣容橫跨四個差異化模型，分別針對不同的部署環境。**Effective 2B（E2B）**和 **Effective 4B（E4B）**專為手機、Raspberry Pi 與 NVIDIA Jetson Orin Nano 等邊緣裝置打造，兩者均原生支援圖片、影片與音訊輸入。**26B 混合專家模型（MoE）**和 **31B 稠密模型（Dense）**則瞄準雲端與高效能本地部署，以遠低於其他模型的參數量，達到頂尖級別的推理能力。

邊緣模型提供 128K 的上下文視窗，較大型模型最高可達 256K，且整個系列原生訓練涵蓋逾 140 種語言。

## 改寫開放模型版圖的基準測試成績

這些效能聲稱看起來很大膽，但實際數字驗證了它們。在業界標準的 **Arena AI 文字排行榜**上，31B 稠密模型在開放模型中**排名第三**，26B MoE 則位居**第六**；Google 表示 Gemma 4 勝過體積達其 20 倍的模型。

在專項測試中，成績更加亮眼。數學方面，Google 表示 Gemma 4 在數學與指令遵循基準測試上有顯著進步。

Google 自己對此次發布的說法是：「按參數量換算，最強大的開放模型。」這指的是 Gemma 4 的「每參數智慧」，且這些模型與 Gemini 3 出自相同的研究與技術。

## Apache 2.0：改變商業應用計算邏輯的授權轉變

測試成績固然重要，但授權的故事對整個產業格局的影響或許更深遠。早期的 Gemma 系列採用 Google 自家的 Gemma 授權。Gemma 4 切換至 **Apache 2.0** 後，使用者可以更自由地依自身需求修改模型。

對於開發 AI 原生產品的新創公司而言，這大幅改變了自建與採購的考量。

## 第一天即完整的生態系整合

Google 在 Gemma 4 發布上投入大量資源，確保模型在理論上具備價值的同時，在實踐上也立即可用。發布首日即整合的工具包括：

- **Hugging Face**（Transformers、TRL、Transformers.js、Candle）
- **vLLM**、**llama.cpp**、**MLX**、**Ollama**、**SGLang** 用於本地推理
- **NVIDIA NIM 和 NeMo** 用於企業部署
- **Google AI Studio** 提供 31B Dense 和 26B MoE 雲端存取
- **Google AI Edge Gallery** 用於 E2B 和 E4B 的裝置端部署
- **LM Studio**、**Unsloth**、**Baseten**、**Keras**、**Docker** 等

Gemma 4 也在發布首日即支援 LiteRT-LM。結合 E4B，這為開發者提供了可信賴的裝置端 AI 技術棧，特別適合雲端資料傳輸受限於合規或隱私考量的敏感應用場景。

## 原生多模態，而非事後補丁

Gemma 4 的多模態能力值得特別關注，因為其架構設計有別於過去的做法。所有 Gemma 4 模型都原生處理影片與圖片，E2B 和 E4B 另外原生支援音訊輸入。

對於需要在不調用獨立專用模型的情況下推理圖片、音訊或影片的開發者而言，這大幅簡化了技術棧。

## Gemma 4 對開放模型生態的意義

2026 年初，開放權重 AI 生態的競爭已出乎意料地激烈。Google 稱 Gemma 4 是其迄今能力最強的開放模型系列，其 Apache 2.0 授權也比早期的 Gemma 授權給予更多自由。

對 Google 而言，戰略邏輯清晰：以 Gemma 為核心形成繁榮的開放模型生態，有助於壯大 Google Cloud、Google AI Studio 及更廣泛 Google AI 平台的開發者群體。每一個基於 Gemma 4 構建應用的公司，都是潛在的 Google Cloud 基礎設施客戶。

對開發者生態而言，一個具有 Apache 2.0 授權、全球排名第三、310 億參數的模型出現，意味著對商用 API 依賴的計算邏輯已真正改變。支撐付費使用閉源模型的效能溢價已大幅收窄。它是否已完全消失，是每個開發團隊現在都必須自行判斷的問題。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 25 處。*
