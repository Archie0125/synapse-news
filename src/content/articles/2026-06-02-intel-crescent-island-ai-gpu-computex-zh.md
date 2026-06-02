---
title: "英特爾 Crescent Island：挑戰 Nvidia 資料中心霸主地位的 480GB AI GPU"
summary: "英特爾在 2026 年 Computex 大展上公布 Crescent Island AI GPU 完整規格，這款基於 Xe3P 架構的加速卡最高可配置 480GB LPDDR5X 記憶體，以 350W 的低功耗設計搭配標準 PCIe 介面，主攻代理式 AI 推論市場。預計 2026 年下半年開始客戶取樣，英特爾正以截然不同的路線向 Nvidia 的 HBM 主導地位發起挑戰。"
category: "hardware"
publishedAt: 2026-06-02
lang: "zh"
featured: true
trending: true
sources:
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/pc-components/gpus/intel-details-long-awaited-crescent-island-ai-gpu-at-computex-boasts-up-to-480-gb-of-lpddr5x-to-combat-memory-shortages-company-shares-more-details-of-its-xe3p-inference-accelerator-at-computex"
  - name: "Neowin"
    url: "https://www.neowin.net/news/computex-2026-intel-launches-crescent-island-gpu-with-up-to-480gb-vram/"
  - name: "Data Center Dynamics"
    url: "https://www.datacenterdynamics.com/en/news/intel-teases-crescent-island-ai-data-center-gpu-supports-up-to-480gb-of-lpddr5x/"
  - name: "WCCFTech"
    url: "https://wccftech.com/intel-crescent-island-xe3p-gpu-packs-480-gb-of-cost-optimized-lpddr5x-memory/"
tags:
  - "英特爾"
  - "Crescent Island"
  - "Xe3P"
  - "AI GPU"
  - "Computex 2026"
  - "AI 推論"
  - "LPDDR5X"
  - "資料中心"
relatedSlugs:
  - "2026-06-01-nvidia-n1x-computex-arm-laptop-launch-zh"
  - "2026-05-27-nvidia-vera-rubin-q3-launch-5x-blackwell-zh"
  - "2026-06-02-amd-epyc-venice-2nm-production-zh"
---

在 2026 年台北 Computex 展上，英特爾拋出了近年來最具戰略意義的 AI 硬體賭注。公司正式公布 Crescent Island 完整規格——這款基於 Xe3P 架構的資料中心 GPU，在設計理念上與 Nvidia 長期建立的路線截然不同。英特爾並非要在原始運算效能和昂貴的 HBM 記憶體上正面競爭，而是押注於容量、靈活性，以及更易取得的供應鏈優勢。

## 480GB 記憶體的不同賭法

這個數字本身就夠震撼。Nvidia H100 配備 80GB HBM3，Blackwell B200 提供 192GB HBM3e；相比之下，英特爾 Crescent Island 的參考設計就配備了 160GB LPDDR5X，而其架構允許合作夥伴 OEM 廠商擴充至最高 480GB。這不只是市場上容量最大的 AI 加速卡，更代表了一種截然不同的記憶體哲學。

HBM（高頻寬記憶體）是 AI 訓練與高密度推論的黃金標準，但它昂貴、相對耗電，供應鏈幾乎完全集中在 SK 海力士與三星手中。英特爾選用 LPDDR5X，一口氣規避了這三個問題。透過 640 位元匯流排連接 20 顆 LPDDR5X 模組，Crescent Island 的估算記憶體頻寬約為 684 GB/s——遠不及 H100 的 3.35 TB/s——但 LPDDR5X 造價更低廉、供應更充裕，且在風冷機架環境中可達到 HBM 無法企及的容量規模。

英特爾將 Xe3P 架構定位為「為代理式 AI 而生」，這句話既反映了技術現實，也點出了市場轉型的方向。代理式工作負載——連續推論管線、多模型協同、長上下文推理鏈——日益受到記憶體容量而非原始吞吐量的限制。一套以 128,000 個 token 的上下文視窗運行 700 億參數模型的系統，需要的是更大的記憶體空間，而非更多的 FLOPS。Crescent Island 最高 480GB 的配置直接回應了這個需求。

## 架構與設計抉擇

Crescent Island 所搭載的 Xe3P 架構與英特爾消費端 Battlemage 顯卡同屬一個世代，但針對資料中心推論場景進行了大幅改造。它支援從 FP4（最大化 AI 推論吞吐量）到 FP64（科學運算與混合精度任務）的完整資料型別，靈活性超過部分 Nvidia 推論優化加速卡。

350W 功耗設計搭配 PCIe 擴充卡形式是深思熟慮的選擇。在 350W 的熱設計功耗下，Crescent Island 可以部署在標準風冷機架環境中，無需 H100 SXM 和 Blackwell SXM 系統所要求的昂貴液冷基礎設施。這一功耗水準接近 Nvidia RTX Pro 5000 Blackwell 工作站顯卡——這顯然是英特爾向那些因 Nvidia 頂級加速卡的極端基礎設施需求而望而卻步的企業客戶與雲端服務商發出的明確信號。

英特爾目前尚未公布原始運算效能數據，這一態度既耐人尋味，也不失策略性。公司顯然無意在 FLOP 數字的競爭中正面交鋒——那是它必輸的局——而是將 Crescent Island 的論述建立在容量與部署成本這兩個維度上。

## 為何是推論市場？為何是現在？

Crescent Island 選在 Computex 亮相的時機，精準反映了 AI 市場的動態走向。過去三年，AI 硬體的對話被訓練主導：建構基礎模型需要龐大算力，這意味著液冷機架中一排排的 H100 和 A100。

但隨著這些模型走向成熟，量化、蒸餾、混合專家等技術不斷壓低部署成本，經濟重心正在向推論轉移。每一家在 2024 年和 2025 年嘗試 AI 實驗的企業，現在都面對同一個問題：如何以合理的單位成本持續、規模化地運行這些模型？

英特爾認為，這正是 Crescent Island 的市場所在。高容量記憶體讓長上下文推論可以在最少記憶體置換的情況下順暢運行；LPDDR5X 降低了加速卡本身的成本；350W 風冷 PCIe 卡可以直接插入現有伺服器基礎設施，無需建設液冷機房。

## 英特爾亟需贏下的市場

英特爾的資料中心 GPU 野心並非首次受挫。從 Habana Labs 收購而來的 Gaudi 系列，被定位為 Nvidia 的低成本替代方案，卻始終未能建立起開發者生態或取得顯著市占率。2024 年推出的 Gaudi 3 雖然在紙面規格上頗具競爭力，但未能獲得超大規模雲端業者的廣泛採用。

Crescent Island 代表了不同的論述。英特爾不再試圖在 AI 訓練基準測試上追趕 Nvidia，而是以真正差異化的特性切入推論市場：同類產品中最高的記憶體容量、合理的功耗設計、標準 PCIe 形式、以及繞過 HBM 瓶頸的供應鏈。

英特爾預計於 2026 年下半年啟動客戶取樣，後續擴大量產。這個時間窗口恰好對應企業 AI 推論部署開始達到真正規模之際——那些在 2024、2025 年訓練了第一批模型的組織，正在把它們推進生產環境，並切實感受到持續運行的成本壓力。

## 競爭格局展望

Nvidia 不會原地踏步。面向 2026 年第三季的 Vera Rubin 架構預計將帶來約 5 倍於 Blackwell 的吞吐量。AMD Instinct MI450X 系列在訓練與前沿推論領域虎視眈眈。但 Crescent Island 的邏輯不是要在 FLOP 數字上擊敗任何對手——而是認為 AI 推論市場中有相當大的一塊，並不需要最快的晶片，而是需要一塊能夠負擔得起、不需搶購 HBM 配額、不需液冷廠房就能跑大型模型的加速卡。

如果這個判斷是對的，英特爾就有機會在一個分析師預測未來兩三年內將達到數百億美元規模的市場中佔有一席之地。推論市場廣大、分散，尚未像訓練市場那樣被單一供應商牢牢鎖定，足以容納一個做出不同取捨的競爭者。

如果英特爾判斷失誤——如果推論市場最終也向原始效能一邊倒——那 Crescent Island 將步 Gaudi 的後塵，成為另一款技術有趣但未能撼動 Nvidia 地位的產品。

答案將在 2026 年下半年第一批客戶基準測試結果出爐時揭曉。但至少在 2026 年 Computex，英特爾終於說出了一個連貫的、差異化的故事，說明為什麼 Crescent Island 在 AI 基礎設施市場中應該舉足輕重。這一次，業界正在傾聽。
