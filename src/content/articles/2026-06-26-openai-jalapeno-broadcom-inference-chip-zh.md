---
title: "OpenAI 與 Broadcom 發布 Jalapeño：ChatGPT 製造商正式進軍晶片設計"
summary: "OpenAI 與 Broadcom 共同發布首款自研 AI 推論晶片 Jalapeño，從設計到流片僅花費九個月——打破高效能 ASIC 的開發紀錄。這款晶片專為 ChatGPT 及 OpenAI 企業產品的推論工作負載而生，能效表現據稱大幅優於現有 NVIDIA 方案，預計 2026 年底開始部署。"
category: "hardware"
publishedAt: 2026-06-26
lang: "zh"
featured: true
trending: false
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/"
  - name: "OpenAI Blog"
    url: "https://openai.com/index/openai-broadcom-jalapeno-inference-chip/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/infrastructure/openai-unveils-first-custom-ai-inference-chip-jalapeno-with-broadcom-and-its-development-was-sped-up-with-openais-own-models/"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/broadcom-and-openai-unveil-custom-built-jalapeno-inference-processor-openais-first-chip-is-a-massive-reticle-sized-asic-built-in-an-ultra-fast-nine-month-development-cycle"
tags:
  - "openai"
  - "broadcom"
  - "AI 晶片"
  - "硬體"
  - "推論"
  - "矽晶片"
relatedSlugs:
  - "2026-06-25-nvidia-vera-rubin-nvl72-78m-rack-memory-cost-zh"
---

多年來，AI 產業幾乎完全依賴單一矽晶片供應商：NVIDIA。訓練 GPT-4、Gemini、Claude——每一個都大量消耗 H100 和 A100 GPU。然而，2026 年 6 月 24 日，OpenAI 邁出了打破這種依賴的關鍵一步，至少在技術棧的某個關鍵環節上是如此。

OpenAI 發布了首款自研 AI 推論晶片 **Jalapeño**，與 Broadcom 共同開發。這不是因為 OpenAI 要取代 NVIDIA 的訓練晶片，而是因為它正在為算力需求的另一半打造專用矽晶片：*服務* 數億名用戶的推論工作。

## Jalapeño 是什麼？

Jalapeño 是業界所稱的 ASIC（特定應用積體電路）——完全針對一個目的從頭設計：執行 OpenAI 大型語言模型的推論工作負載。不同於 GPU 這種通用並行處理器，Jalapeño 的硬體邏輯是專門為 LLM 回應用戶查詢所需的特定數學運算而生。

這是一顆全倍縮晶粒（reticle-sized）晶片，意即在製程光刻限制下，盡可能佔用最大晶圓面積——這個設計選擇能最大化計算密度。根據 OpenAI 表示，早期測試顯示其「每瓦效能大幅優於當前最先進方案」，但完整基準數字尚未公布。

「我們對工作負載有深刻的理解，」OpenAI 總裁 Greg Brockman 在發布聲明中說。「我們一直在尋找那些服務不足的特定工作負載，問自己：我們能建造什麼來加速可能性？」

## 九個月完成 ASIC：AI 設計 AI 晶片

讓 Jalapeño 技術上同樣令人印象深刻的，是它的開發速度。OpenAI 與 Broadcom 的合作夥伴關係於 2025 年 10 月宣布。從初始設計到製造流片（量產前的最後一步），只花了**九個月**。

這相當驚人。高效能生產級 ASIC 的典型開發週期需要 18 至 24 個月。將時間縮短一半，需要兩個條件：Broadcom 在客製化矽晶片實作方面的深厚專業知識，以及一個嶄新的作法——OpenAI 自身的模型被用於加速晶片的設計與優化過程。

這是一項真正遞迴式的成就：AI 協助設計將運行 AI 的晶片。工程師使用 OpenAI 模型來探索設計空間、驗證時序約束，並優化若僅靠人類團隊可能還需要數月的電路佈局。

## 推論 vs. 訓練：為何重要

訓練與推論晶片之間的區別，是理解 Jalapeño 重要性的關鍵。

訓練需要原始計算暴力。你需要在數兆個參數上執行梯度下降，對記憶體頻寬有巨大需求。NVIDIA 的 H100 和 H200 GPU，憑藉其龐大的 HBM3 記憶體和 NVLink 互連，在這個工作負載上仍無可匹敵。OpenAI 將繼續使用 NVIDIA 硬體訓練其前沿模型。

推論則是另一回事。當你在 ChatGPT 輸入訊息時，模型在數毫秒內執行前向傳播計算，逐一生成 token 直到回應完成。這個工作負載高頻率、對延遲敏感，並在數百萬名同時在線的用戶中大規模運行。成本結構也不同：推論是 OpenAI 每天花費最多計算費用的地方。

客製化推論晶片——如 Google 的 TPU v5、Amazon 的 Inferentia、Microsoft 的 Maia——可以針對生產 LLM 服務實際使用的批次大小、精度格式（INT8、FP8、FP4）和記憶體訪問模式進行優化。GPU 雖靈活，但對這些工作負載而言效率較低，因為其硬體為 OpenAI 根本不需要的使用場景而設計。

透過部署 Jalapeño，OpenAI 可以大幅降低每 token 的推論成本、改善延遲，並——關鍵在於——減少對 NVIDIA 定價和供應限制的運營暴露。

## 策略背景：矽晶片主權競賽

OpenAI 在這條路上並不孤單。每個主要的 AI 超大規模廠商都意識到了同一件事：如果你花費數十億美元在計算上，你會想擁有自己的晶片。

Google 自 2016 年起就在部署 TPU。Amazon 的 Trainium 2 處理其自身模型的訓練並為 Bedrock 提供動力。Microsoft Maia 100 在內部執行 Copilot 推論。Meta 的 MTIA 晶片以大規模處理推薦系統推論。

值得注意的是，相對於其建立的模型，OpenAI 加入這場競賽的時間有多*晚*。這家公司每年花費數十億美元租用 NVIDIA GPU 來服務 ChatGPT——這種依賴使它同時成為全球最重要的 NVIDIA 客戶，以及在定價談判中最脆弱的一方。

對 Broadcom 而言，OpenAI 交易驗證並擴展了其 AI 客製化矽晶片業務，該業務預計在 2026 年單獨創造 120 億美元收入。OpenAI 使用自身模型加速晶片設計，也開啟了一個引人入勝的產品飛輪：更好的模型幫助設計更好的晶片，更好的晶片能實現更快更便宜的推論，更多的收入用於訓練更好的模型。

## 晶片架構細節

雖然 OpenAI 尚未公布完整技術規格——這對部署前的 ASIC 發布很常見——但一些細節已經浮現。Jalapeño 被描述為「全倍縮晶粒」設計，與 NVIDIA H100 晶粒屬於同一尺寸類別，意味著它正在突破當前光刻限制下單片矽晶片所能容納的物理極限。

該晶片針對推論而非訓練進行優化，這意味著其記憶體架構與訓練導向的 GPU 不同。訓練晶片需要龐大的高頻寬記憶體來儲存中間梯度和激活值。推論晶片則優先考慮 KV 快取查詢（實現高效多輪對話的快取注意力狀態）的低延遲記憶體訪問，以及前向傳播的高吞吐量張量運算。

「每瓦效能大幅優於最先進水準」的說法意義重大：在每天處理數百萬 ChatGPT 查詢的資料中心，瓦特效率直接轉化為運營成本。若在 OpenAI 的推論規模下比 NVIDIA H 系列硬體提升 30% 的效率，每年將節省數億美元。

## 後續展望

Jalapeño 預計將於 2026 年底開始在 OpenAI 資料中心進行初始部署，「並在未來幾年擴展」。這是一個謹慎的措辭——新 ASIC 的初始部署幾乎總是遇到整合挑戰，OpenAI 顯然為自己留有空間，在全面推出前吸收早期迭代的經驗教訓。

其影響超越成本節省。客製化矽晶片讓 OpenAI 能夠共同優化模型和硬體——這是以前只有 Google 才有的能力。未來的 OpenAI 模型可能會針對 Jalapeño 的特定記憶體層次結構、精度支援和互連特性進行設計，創造出純軟體優化無法複製的效能優勢。

消息公布當日，NVIDIA 股票下跌 3.2%，後來才回穩——這是市場理解長期影響的信號。推論市場龐大且持續增長。OpenAI 每天透過 Jalapeño 而非 NVIDIA GPU 處理的每十億次查詢，都是對 NVIDIA 服務收入的直接衝擊。

AI 基礎設施競賽不再只是關於模型規模。它關乎誰能掌控底層的矽晶片。
