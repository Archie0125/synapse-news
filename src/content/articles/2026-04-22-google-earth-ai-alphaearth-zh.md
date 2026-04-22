---
title: "Google DeepMind AlphaEarth：每一個衛星像素，都能成為 AI 洞察的起點"
summary: "適逢 2026 年地球日，Google 宣布旗下 Earth AI 計畫重大進展，核心是 AlphaEarth Foundations 基礎模型——一個以 PB 級多源衛星數據訓練、以每 10 公尺解析度覆蓋全球陸地與沿岸水域的地理空間模型。錯誤率比同類模型低 24%，聯合國糧農組織、史丹佛大學等 50 多個合作夥伴已在實際部署中使用。"
category: "ai-ml"
publishedAt: 2026-04-22
lang: "zh"
featured: false
trending: true
sources:
  - name: "Google AI Blog"
    url: "https://blog.google/innovation-and-ai/products/google-earth-ai/"
  - name: "Google Research"
    url: "https://research.google/blog/google-earth-ai-unlocking-geospatial-insights-with-foundation-models-and-cross-modal-reasoning/"
  - name: "Data Center Dynamics"
    url: "https://www.datacenterdynamics.com/en/news/google-launches-earth-ai/"
  - name: "Google Earth on X"
    url: "https://x.com/googleearth/status/2031024842498023718"
tags:
  - "Google"
  - "DeepMind"
  - "AlphaEarth"
  - "地理空間AI"
  - "衛星影像"
  - "地球日"
  - "氣候科技"
  - "基礎模型"
relatedSlugs:
  - "2026-04-17-nvidia-ising-quantum-ai-models-zh"
  - "2026-04-13-google-gemma-4-open-model-apache-zh"
---

在第 56 屆地球日（2026 年 4 月 22 日），Google 選擇以一套真正能重塑人類理解地球方式的 AI 系統作為獻禮。AlphaEarth Foundations 由 Google DeepMind 開發，本次同步更新至 2025 年衛星覆蓋數據，是一個以 PB 等級（Petabyte）多源地球觀測資料訓練而成的地理空間基礎模型（geospatial foundation model）。

這不是一場公關活動。地理空間 AI 正在經歷一場類似 2019 至 2022 年自然語言處理領域的基礎模型革命，而 AlphaEarth 是這場革命迄今最具代表性的成果。

## AlphaEarth 究竟做了什麼？

傳統衛星影像分析的邏輯是：一個任務，一個模型。偵測森林濫伐要訓練一個模型、監控藻華（algae bloom）要訓練另一個模型，每個任務都需要大量人工標記的訓練資料，往往耗費數年。

AlphaEarth Foundations 徹底打破這個範式。類比大型語言模型學習文字的通用表徵，AlphaEarth 學習的是地球表面的通用表徵——Google 稱之為「衛星嵌入向量」（satellite embeddings）。

模型針對地球上每一塊 10×10 公尺的陸地和沿岸淺水區域，生成一個 64 維的向量，編碼該區域的光譜特性、時間變化和空間上下文。這些嵌入向量可以作為幾乎任何地理空間任務的起點，只需少量額外訓練資料即可微調。

換句話說：一家自來水公司不再需要從頭訓練藻華偵測模型，只要基於 AlphaEarth 的嵌入向量微調，用極少的標記數據就能達到可用的準確率。一個政府單位要監控非法開墾，可以複用同一套基礎；城市規劃部門要追蹤不透水面積擴張，也不需要重新建模。

Google 報告指出，AlphaEarth 在標準基準測試中比同類地理空間模型錯誤率低 **24%**——這個差距在實際業務中，往往是一套監控工具「可用」與「誤報太多無法使用」的分水嶺。

## 2025 年數據更新與地球日的選擇

地球日當天，Google Earth 宣布 AlphaEarth 衛星嵌入向量資料集已完成 2025 年覆蓋更新，現已透過 Earth Engine Data Catalog 和 Google Cloud Storage 公開提供，覆蓋全球陸地表面及沿岸淺水區域。

2025 年更新的意義遠超過定期刷新數據。它讓一個地理空間領域幾十年來追求的能力成為現實：**全球尺度的變化偵測（change detection）**。透過比對 2024 年與 2025 年的嵌入向量，分析師可以在不標記任何一張影像的情況下，找出地表變化的位置——新建道路、城鎮擴張、冰川萎縮、河道改道——由模型的學習表徵完成初步篩選。

對氣候監測而言，這是關鍵突破。追蹤全球植樹造林計畫的進度、監測永久凍土解凍範圍擴張、識別保護區內的非法開墾，過去都需要龐大的人工標記成本或昂貴的商業衛星分析合約。AlphaEarth 讓具備一定技術能力但資源有限的組織，也能以合理成本進行這些分析。

## 地理空間推理：讓 AI 成為地球分析師

除了 AlphaEarth Foundations，Google 也發布了「地理空間推理」（Geospatial Reasoning）框架——將 AlphaEarth 嵌入向量與 Gemini 的語言和推理能力整合，讓複雜的空間分析查詢可以用自然語言完成。

過去要分析「美國東南部哪些河流出現藻華」，需要一名 GIS 專家花幾個小時手動篩選衛星波段、設定閾值、輸出地圖。Geospatial Reasoning 讓用戶直接輸入這樣的查詢，系統自動選擇衛星層、套用 AlphaEarth 嵌入、在地圖上標示結果，並附上文字說明。

這個能力將透過 Google Cloud Platform 的 API 開放給開發者和企業，方便將地理空間推理整合進監控儀表板、環境合規系統和基礎設施規劃工具。

對台灣開發者而言，值得關注的是 AlphaEarth 的嵌入向量資料集已可在 Google Cloud Storage 直接取用，搭配台灣本地的農業、林業或災防數據進行微調，有潛力開發出高價值的在地化應用，例如山坡地崩塌風險監測、農業用地分類或颱風後損失評估。

## 已在生產環境部署的 50 多個合作夥伴

AlphaEarth 不是研究原型。過去一年，已有超過 50 個組織將它用於實際業務，2025 年數據更新進一步擴展了可用場景：

**聯合國糧農組織（FAO）** 使用 AlphaEarth 追蹤糧食不安全地區的農地轉換情況，強化糧食危機預警模型的準確度。

**哈佛森林（Harvard Forest）** 和 **奧勒岡州立大學** 將嵌入向量用於森林組成和生物量變化偵測，成果用於碳信用計量和政策制定。

**MapBiomas**（巴西土地分類聯盟）使用 AlphaEarth 加速亞馬遜、塞拉多（Cerrado）和大西洋森林的年度土地覆蓋分類，這些數據是巴西國家森林砍伐報告的基礎。

**史丹佛大學** 地理空間研究團隊整合 AlphaEarth 研究全球南方城市的熱島效應動態。

**地球觀測組（Group on Earth Observations）** 擁有 113 個成員國，已將 AlphaEarth 列為其全球地球觀測系統（GEOSS）數據基礎設施的核心工具。

## 同步更新的 Earth 平台新功能

除了 AlphaEarth 本身，Google 也為 Google Earth 平台宣布多項具體更新：

**影像搜尋（Imagery Search）：** 新的實驗性功能，讓用戶直接用自然語言描述視覺特徵搜尋衛星與航空影像，無需了解衛星波段組合或指數閾值。

**全球等高線：** 20 公尺和 40 公尺間距的等高線首次在全球範圍提供，讓各地的基地規劃、洪水風險評估和農業排水分析都能取得地形背景資料。

**向量數據表格（Data Tables）：** 允許用戶直接在 Google Earth 中以表格形式查看向量數據，簡化了過去必須匯出至 Excel 才能進行的數據分析流程。

## 為什麼這比地球日更重要

AlphaEarth 在地球日宣布，時機是刻意安排的，但它的意義遠超環境議題。Google 實質上建構了一個**物理世界的通用表徵層**——AI 系統可以用它來回答關於地理、基礎設施、生態系統和人類聚落的問題，以前所未有的規模和速度。

對 AI 研究社群而言，AlphaEarth 展示了基礎模型範式並不局限於文字、程式碼或一般影像。地球觀測數據——高維度、多時態、多光譜、本質上空間化——是機器學習中最複雜的模態之一。成功地將基礎模型技術應用於它，為海洋學、大氣科學和地下地質學的類似嘗試打開了大門。

對地理空間產業而言，AlphaEarth 是一個競爭格局的轉折點：建立在窄域特定任務模型上的商業衛星公司、GIS 軟體供應商和環境顧問機構，都需要重新評估自己的護城河。

而對那些默默從事森林監測、水質追蹤和土地使用製圖的機構而言，AlphaEarth 只是讓重要工作變得更快、更易取得的工具。在一個環境變化監測能力與需求之間差距以年計算的世界，這本身就意義重大。
