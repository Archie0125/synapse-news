---
title: "NVIDIA Cosmos 3：全球首個開放式實體AI基礎模型正式登場"
summary: "NVIDIA 於 2026 年 6 月 1 日 GTC 台北發表 Cosmos 3，這是全球首個完全開放的實體 AI 全能模型。其創新的混合式 Transformer 架構將視覺推理、世界模擬與機器人動作生成整合為單一系統，有望將機器人研發週期從數月壓縮至數日。"
category: "ai-ml"
publishedAt: 2026-06-05
lang: "zh"
featured: true
trending: true
sources:
  - name: "NVIDIA 新聞室"
    url: "https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai"
  - name: "Hugging Face 部落格"
    url: "https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai"
  - name: "HPCwire / AIwire"
    url: "https://www.hpcwire.com/aiwire/2026/06/01/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai/"
tags:
  - "NVIDIA"
  - "Cosmos 3"
  - "實體AI"
  - "機器人"
  - "基礎模型"
  - "開源"
  - "Computex 2026"
relatedSlugs:
  - "2026-06-03-nvidia-rtx-spark-superchip-computex-zh"
  - "2026-06-01-nvidia-n1x-computex-arm-laptop-launch-zh"
---

十多年來，打造一台有實際能力的機器人，意味著要把數十個各自獨立開發的組件拼湊在一起：電腦視覺系統、物理模擬器、動作規劃器、語言介面——每個模組用不同的資料格式說話，彼此之間幾乎不共通。NVIDIA 在 2026 年 6 月 1 日 GTC 台北大會上發表的 Cosmos 3，正是業界迄今最大膽的嘗試：把這整套複雜流程壓進一個單一的開放模型。

「實體 AI 的大爆發已經近在眼前，」NVIDIA 執行長黃仁勳在發表會上說，「多模態推理、視覺與世界模型的突破，正是這一切的引擎。」

## 一種全新的基礎模型

NVIDIA 將 Cosmos 3 定義為「全能模型」（omnimodel）——一個能同時理解並生成文字、圖片、影片、環境音與機器人動作的單一神經系統。它與過去多模態模型的差異遠不只是能力範疇的擴大：Cosmos 3 不只是描述眼前所見，或根據文字提示生成圖片；它能夠對物理交互進行推理，模擬物體在空間中的移動方式，並輸出機器人完成任務所需的精確動作軌跡。

支撐這一切的是創新的混合式 Transformer（MoT）架構，由兩個緊密耦合的組件構成：**推理 Transformer** 負責解讀輸入的多模態資訊，建立對世界的結構化理解；**專家生成 Transformer** 則將這些表示轉換為物理上合理的輸出——無論是場景的影片模擬，還是機械臂的動作序列。

這種設計讓 Cosmos 3 得以在生成之前先進行推理，解決了過去世界模型的一大痛點：早期系統產生的影片視覺上看似真實，卻可能違背基本物理定律——物體穿牆而過、液體逆流而上。Cosmos 3 的推理步驟作為隱式的物理約束，讓生成結果始終限制在符合現實動力學的範疇內。

## 三種規格，對應不同工作負載

NVIDIA 在發布當日推出兩個可立即使用的版本，透過 Hugging Face、GitHub、build.nvidia.com 及 NIM 微服務提供存取：

**Cosmos 3 Nano** 將 80 億參數的推理模型與 80 億參數的生成模型配對。針對快速推理與邊緣部署設計，適合對延遲敏感的場景——例如生產線上的即時品質檢測，或自主移動機器人的快速反應。

**Cosmos 3 Super** 將 320 億參數的推理模型與 320 億參數的生成模型配對。這是主力版本，針對精度優先於推理成本的訓練與評估工作負載。目前在七項主要基準測試中拿下全開放模型最高分：Physics-IQ、PAI-Bench、R-Bench、RoboLab、RoboArena、VANTAGE-Bench 及時序動作識別（TAR）基準。

**Cosmos 3 Edge** 已宣布即將推出，細節尚未公開。從命名判斷，這將是一個高度壓縮的版本，目標是直接部署在機器人嵌入式硬體上，參數量可能低於 80 億。

基礎模型以數十億筆多模態實體 AI 樣本訓練，涵蓋真實世界互動錄影、物理模擬輸出，以及帶有動作標籤的機器人資料集，讓模型對物質如何在物理約束下運動有深刻的實證理解。

## 機器人的資料瓶頸

機器人領域的核心難題向來是資料。訓練機器人執行一項新任務——比如從傳送帶上抓取形狀不規則的零件、在陌生倉庫中導航——傳統上需要數千小時的真實世界示範，再加上數個月的模擬到現實遷移工作。整個流程昂貴、高度專業化，而且極度緩慢。

Cosmos 3 從兩個層面同時攻克這個問題。作為**世界模型**，它能生成全新物理場景的合成影片，等同於在現實世界不存在的情況下「製造」訓練樣本。作為**動作模型**，它將模擬經驗轉換為機器人可直接使用的軌跡資料，打通想像與執行之間的環節。

NVIDIA 宣稱由此可將訓練週期從數月壓縮至數日。即使實際加速倍數因應用複雜程度而異，光是 10 倍的研發速度提升，對一個原型開發週期動輒以年計、平均成本動輒達數百萬美元的產業而言，就足以改變遊戲規則。

## Cosmos 聯盟

為加速生態系採用，NVIDIA 宣布成立 **Cosmos 聯盟**，召集 AI 實驗室與機器人公司承諾基於並貢獻於 Cosmos 3 平台。創始成員包括 Agile Robots、Black Forest Labs、Generalist、LTX、Runway 及 Skild AI。

聯盟的跨領域設計頗為用心：Runway 的影片生成專長為模型提供更豐富的視覺訓練資料；Skild AI 的機器人學習研究直接推進動作模型改進；Black Forest Labs 的圖像生成能力協助填補靜態場景理解與動態世界模擬之間的鴻溝。

在企業開發者端，NVIDIA 宣布與東山機器人、LG 電子、三星電子、理想汽車、Centific、Fogsphere、Linker Vision、Milestone Systems 及 Yuan 達成整合合作，橫跨汽車、消費電子、工業機器人與智慧建築等多個領域。

## 「開放」的另一面

Cosmos 3 的「開放」標籤值得仔細審視。NVIDIA 公開了模型權重，並透過 Hugging Face 提供存取，比起 Boston Dynamics、Agility Robotics 等採取完全封閉策略的競爭對手，確實邁出了有意義的一步。然而，訓練資料與完整訓練流程並未公開，這意味著研究人員可以微調與部署 Cosmos 3，但無法從零開始完整復現。

這與 Meta LLaMA 系列的定位相近：開放權重，而非完整開放科學。對大多數商業用戶——機器人新創、企業整合商、工業自動化廠商——而言，這個區別無關宏旨。但對於想深入研究實體 AI 如何從資料中學習的學術研究者，這個差距仍然存在。

## 競爭格局

Cosmos 3 進入的是一個快速整合中的市場。Google DeepMind 透過機器人團隊與 Gemini 整合持續推進實體 AI 研究；Figure AI 與 Physical Intelligence（Pi）正在以大量風險投資打造專有機器人基礎模型；亞馬遜機器人部門則悄悄在物流網絡中大規模部署 AI 原生系統，累積專有資料。

Cosmos 3 的差異化優勢在於開放性與基準表現的結合——目前沒有任何開放競爭對手能在視覺推理與動作生成排行榜上同時媲美它。這個領先可能是暫時的，實體 AI 的進展速度異常迅猛，但 NVIDIA 已經在關鍵位置插上了一面重要的旗幟。

## 後續觀察

最值得關注的近期動態是 Cosmos 3 Edge，NVIDIA 尚未公開其規格。若它能在嵌入式硬體——尤其是 NVIDIA 自家的 Jetson 平台——上實現有競爭力的推理效能，可能成為下一代低成本自主系統的預設基底，讓機器人在無需雲端連線的情況下獨立運作。

長遠來看，Cosmos 3 的影響力最終不會以基準分數衡量，而是以真正量產上市的機器人數量衡量。若 Cosmos 聯盟的開發時程如期推進，預計最早 2027 年初就能看到第一批 Cosmos 3 驅動的商業部署出現在製造業與物流領域。黃仁勳說的「實體 AI 大爆發」也許還差一步之遙——但倒數計時，已然正式開始。
