---
title: "三星與 Cadence 攜手打造 Physical AI Chiplet 平台，瞄準機器人與自動駕駛市場"
summary: "三星晶圓代工與 Cadence 設計系統在 CadenceLive 2026 發布聯合 Physical AI Chiplet 平台，建構於三星 5nm SF5A 製程之上。這套預驗證模組化設計針對即時相機處理、AI 雷達和自動化系統，計畫於 2027 年初進行晶片流片，下半年進入量產。"
category: "hardware"
publishedAt: 2026-05-28
lang: "zh"
featured: false
trending: false
sources:
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/317234/20260527/samsung-foundry-chiplet-platform-eyes-2027-production-robotics-automotive-ai.htm"
  - name: "Samsung Semiconductor"
    url: "https://semiconductor.samsung.com/news-events/tech-blog/samsung-foundry-and-cadence-accelerating-chiplet-solutions-for-physical-ai/"
  - name: "New Electronics"
    url: "https://www.newelectronics.co.uk/content/news/samsung-foundry-and-cadence-advance-chiplet-platform-for-physical-ai-applications"
tags:
  - "三星"
  - "cadence"
  - "chiplet"
  - "physical-ai"
  - "機器人"
  - "自動駕駛"
relatedSlugs:
  - "2026-05-27-nvidia-vera-rubin-q3-launch-5x-blackwell-zh"
  - "2026-05-27-china-nine-domestic-ai-chips-anke-certification-zh"
  - "2026-05-25-amazon-trainium-20b-chip-business-225b-backlog-zh"
---

三星晶圓代工與 Cadence 設計系統在 CadenceLive 2026 發布了聯合 Physical AI Chiplet 平台，這是半導體產業至今最清晰的訊號：Physical AI——嵌入機器人、自動駕駛汽車、無人機和製造系統中的智慧——已是一個足夠獨特的算力類別，需要專為其設計的晶片架構，而非改造現有的資料中心晶片。

這個平台建構於三星 SF5A 5 奈米製程之上，採用模組化 Chiplet 設計方式：一套預先驗證、可互通的矽晶片單元，能夠根據不同 Physical AI 應用的算力、功耗和延遲需求自由組合。機械手臂和自動駕駛車輛的感測系統需求大相徑庭；Chiplet 架構讓兩者都能共用已驗證的矽智財，同時各自針對計算、記憶體和 I/O 元件進行客製化配置。

## Physical AI 對算力的特殊要求

Physical AI 的計算需求，與過去十年推動資料中心 AI 晶片設計的需求有根本性的不同。大型語言模型和 Transformer 系架構本質上是矩陣乘法工作負載：高度並行、高記憶體頻寬，對毫秒到秒級的延遲有一定容忍度。Physical AI 工作負載的優先順序恰恰相反。

製造機器人中的相機處理系統需要即時分析影像——從感測器輸入到執行器響應必須在 10 毫秒以內完成。汽車雷達系統需要在高速公路行駛速度下以確定性延遲偵測物體，而非平均延遲。倉庫分揀機器人需要同時處理多種模態的感測器融合，同時在嚴格的功耗限制下持續電池供電運行。

這是即時性、功耗受限、延遲確定性的工作負載，與資料中心的 Nvidia H100 關係不大，反而更接近 AI 時代之前的汽車級嵌入式處理器。三星與 Cadence 共同打造的 Physical AI Chiplet 平台，正是填補通用 AI 矽晶片與嵌入式系統世界之間這個缺口。

## Chiplet 架構的優勢

過去五年，Chiplet 設計已成為先進半導體產品的主流架構方向，主要驅動力是隨著摩爾定律放緩，單一晶片縮放受到的限制。AMD、Intel、蘋果和台積電都已為 CPU 和 GPU 建立 Chiplet 生態系。三星與 Cadence 的平台，將這一方式專門延伸到 Physical AI 邊緣算力領域。

預驗證的 Chiplet 設計，在商業上至關重要。驗證矽智財是否達到功能、功耗和時序規格，是晶片設計中最耗時且最昂貴的環節之一。一個擁有預驗證 IP 模組的 Chiplet 平台，讓設計第一款客製化矽晶片的機器人新創公司，能從已驗證的基礎出發，而非從零開始，可能縮短數年的開發週期。

各個 Chiplet 可針對特定電壓和頻率需求進行優化——這對電池供電的邊緣設備尤為有價值，不同功能模組可能需要同時運行在不同的電源狀態。平台也瞄準良率提升：較小的單一晶片相較大型單塊晶片具有更高的製造良率，隨著出貨量規模增長，單位成本下降。

## 目標應用與市場背景

平台第一波鎖定的目標應用包括：即時相機處理、汽車自動駕駛中的 AI 增強雷達、智能製造設備，以及感測器驅動的機器人系統。這些類別有一個共同特點：在空間受限的實體環境中需要高算力密度，功耗和散熱條件嚴苛，且故障模式的後果是物理上的損害，而非單純的服務降級。

汽車應用可能是近期最大的市場。先進駕駛輔助系統（ADAS）和完全自動駕駛需要持續處理相機、雷達和激光雷達的輸入，速度要求使資料中心 AI 推理的延遲完全不可接受。目前 Mobileye、高通和輝達 Drive 平台等汽車 AI 晶片已為此設計，但三星與 Cadence 平台定位為第二和第三代汽車 AI 系統更靈活的基礎——晶片設計商可以根據特定的安全和性能要求進行配置，而非購買固定解決方案。

製造機器人應用也在快速增長。隨著工廠自動化投資加速——特別是供應鏈備援策略推動製造業回流——對工廠機器人用高能效感知和控制晶片的需求相當可觀。符合 ISO 26262 和 IEC 61508 功能安全標準（汽車和工業安全認證框架）的 Physical AI Chiplet，代表著一個重要的市場機會。

## 時程與競爭格局

三星與 Cadence 的目標是在 2027 年初完成原型流片，使用 SF5A 製程的量產預計在 2027 年下半年啟動。這對一個全新的 Chiplet 生態系而言時程頗為積極，既反映了 Physical AI 市場的緊迫性，也反映了三星晶圓代工在台積電持續領先製程前沿的情況下，對差異化先進節點收入的迫切需求。

過去兩年，三星晶圓代工在半導體產業的定位持續受到關注。其 3nm 和 4nm 製程的良率問題使台積電得以維持在高端先進節點製造的主導地位。Physical AI Chiplet 平台代表一個戰略轉向：在系統層面的整合價值上競爭，而非純粹的製程節點之爭——提供整合式設計解決方案，不僅包含晶圓代工製程，還包括預驗證 IP、設計工具以及 Cadence 完整的 EDA 生態系。

Cadence 在此合作中的角色，超越了為 Chiplet 設計提供 EDA 工具。公司的驗證智財和設計規則檢查已嵌入平台，意味著在此生態系內創建的 Chiplet 設計，自帶 Cadence 的認證，證明其符合特定標準。對於需要安全關鍵矽晶片第三方驗證的汽車和工業客戶而言，這個內嵌的 Cadence 驗證具有重要的商業意義。

## 超越晶片的更大意義

三星與 Cadence 的合作，是 Physical AI 算力市場走向的先行指標。過去幾年，Physical AI 大多運行在為其他用途設計的晶片上——行動 SoC、遊戲 GPU、資料中心推理加速器。隨著 Physical AI 應用走向成熟、出貨量規模擴大，專用矽晶片的經濟邏輯愈發清晰。

輝達已透過 Drive Thor 和對機器人公司的投資，在汽車方向認識到這一點。高通的 Snapdragon Ride 平台也在類似領域布局。不同之處在於，三星和 Cadence 提供的是「晶圓代工＋設計生態系」的整合解決方案，而非一款完整的成品晶片，這讓 Physical AI 公司有了一條通往客製化矽晶片的路徑，無需從零建立自己的晶片設計團隊。

流片時程意味著量產最快在 2027 年下半年啟動——也就是說，第一批基於此平台的產品，將在 2028 至 2029 年出現在商業機器人、汽車和工業系統中。Physical AI 公司今天在矽晶片策略上做出的決策，將塑造十年後自動化系統的競爭格局。
