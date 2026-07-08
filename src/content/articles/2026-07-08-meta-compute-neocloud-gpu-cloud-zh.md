---
title: "Meta Compute 正式成形：Zuckerberg 的 1,300 億美元豪賭將顛覆 AI 雲端市場"
summary: "Meta Platforms 正在打造名為「Meta Compute」的雲端業務，計畫向外部客戶出售多餘的 GPU 算力與 AI 模型 API 存取。彭博社披露此計畫後，Meta 股價單日暴漲逾 10%，CoreWeave、Nebius 等算力新創則重挫逾 15%。Meta 1,150 至 1,350 億美元的年度資本支出，正從財務負擔轉化為新的收入引擎。"
category: "industry"
publishedAt: 2026-07-08
lang: "zh"
featured: false
trending: true
sources:
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-07-01/meta-is-building-a-cloud-business-to-sell-excess-compute"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/319486/20260701/meta-enters-ai-cloud-market-neocloud-rivals-coreweave-nebius-crater.htm"
  - name: "SemiAnalysis"
    url: "https://newsletter.semianalysis.com/p/meta-compute-everyone-wants-to-be"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/meta-reportedly-plans-to-rent-out-its-ai-compute"
tags:
  - "Meta"
  - "雲端運算"
  - "GPU"
  - "算力雲"
  - "AI基礎建設"
  - "CoreWeave"
  - "資料中心"
relatedSlugs:
  - "2026-07-04-microsoft-frontier-company-25b-enterprise-ai-zh"
  - "2026-07-05-h1-2026-vc-funding-record-510b-ai-concentration-zh"
---

七月一日，彭博社披露 Meta Platforms 正在悄悄打造一套面向外部客戶的算力雲業務，市場的反應是立即且激烈的。Meta 股價單日暴漲逾 10%，創下五個月來最大單日漲幅；剛剛上市的 GPU 算力新創 CoreWeave 則重挫 13% 至 15%；Nebius 跌幅相當；另一家算力雲業者 IREN 同樣大跌。

市場傳遞的訊號再清楚不過：Meta 打算出租多餘算力的計畫，不只是一個小型副業，而是一場足以震動 AI 基礎建設產業的地震。

## Meta Compute 到底是什麼？

這個在公司內部被稱為「Meta Compute」的計畫，將向外部客戶提供兩種服務。

**第一層：AI 模型 API**。外部開發者可透過 API 存取 Meta 自家的 AI 模型，包括 Llama 系列及 Meta Superintelligence Labs 即將推出的新一代模型，全部托管於 Meta 自有的 GPU 基礎建設上。這使 Meta Compute 直接對標 AWS Bedrock、Google Vertex AI 和 Azure AI Studio——這些服務都以統一 API 讓開發者存取第三方 AI 模型。

**第二層：裸機 GPU 租用**。Meta 將按小時向第三方租出 GPU 算力，模式與 CoreWeave 和 Nebius 目前提供的服務幾乎相同。這一層直接衝擊算力雲新創的核心商業模式，威脅最為直接。

這個計畫的領導團隊已名花有主：Meta 基礎建設負責人 Santosh Janardhan 主掌技術方向；曾創辦 Cue、主導蘋果收購多家 ML 新創的 Daniel Gross 代表 Meta Superintelligence Labs；前白宮官員、前高盛高管、現任 Meta 總裁 Dina Powell McCormick 負責企業關係開發。這個橫跨基礎建設、AI 研究與商業拓展的組合，清楚顯示 Meta 對此計畫的嚴肅程度。

## 為什麼 Meta 要進入這個市場？

Meta 在 2026 年的資本支出指引為 1,150 至 1,350 億美元——這個金額超過許多中型國家的年度 GDP。靠社群媒體廣告收入支撐這樣規模的基礎建設投資，對投資人而言愈來愈難以接受，監管機構對 AI 支出的審查也與日俱增。

雲端業務是少數能夠將閒置算力直接轉化為收入的路徑之一。在兩次訓練任務之間，Meta 的 GPU 叢集有相當比例是閒置的，邊際成本幾乎為零，出租這些閒置資源不需要額外投資，卻能帶來可觀的收入。更重要的是，Meta 可以藉此取得企業客戶如何使用 AI 基礎建設的第一手數據，進一步優化自家產品。

戰略邏輯更遠不止於單純的利潤計算。Meta 在開源策略上投入了巨大資源讓 Llama 保持開放，而開源模型需要生態系開發者。透過低成本算力加上 Llama 模型 API 的組合，Meta 得以打造飛輪效應：更多開發者在 Llama 上構建應用，更多使用數據回流改善模型，更強的競爭護城河對抗閉源對手。

## 令競爭對手不安的數字

Meta 基礎建設規模所帶來的威懾力不是假設，而是已有合約為證。根據內部文件，Anthropic 每個月向 Meta 支付約 12.5 億美元，換取約 300 MW 的算力；Google 則簽下每月 9.2 億美元的協議，獲得約 11 萬張 GPU 至 2029 年中。這些資料顯示，Meta 的基礎建設早已在為外部客戶提供算力服務，只是尚未以「Meta Compute」品牌對外公開銷售。

對 CoreWeave 而言，Meta 入場的威脅在結構上是存在性的，即便不是即時致命的。CoreWeave 的整個商業邏輯建立在「超大型雲端廠商無法快速提供 GPU 叢集」這個前提上。Meta 加入競爭，不意味著 CoreWeave 立刻消失，但會壓縮其定價空間，並縮小其可觸達的市場規模——尤其是在中大型算力採購上。

對 Amazon、Google、Microsoft 等超大型雲端廠商，威脅則較為複雜。它們規模更大、業務更多元，但 Meta 進入企業算力市場意味著又一個資本雄厚的競爭者，尤其對那些已在使用 Meta 開源模型、可能偏好「模型加算力」一體整合方案的開發者更具吸引力。

## Meta 還沒有說的事

目前為止，Meta 尚未官方確認 Meta Compute 計畫。沒有定價，沒有上線日期，沒有公開的客戶名單。彭博社的報導援引熟悉內部規劃的消息人士，並強調整體策略可能仍有調整空間。

但有一個重要信號：這個計畫已從非正式的內部討論進展到正式的領導層指派和產品架構決策，這在大型科技公司通常意味著公開上線將在六至十二個月內到來。

## 更大的結構性轉變

Meta Compute 是 SemiAnalysis 所稱「算力雲整合浪潮」的一部分。早期的算力雲新創潮（CoreWeave、Nebius、Lambda Labs）得以崛起，根本原因在於超大型雲端廠商反應遲緩、定價昂貴。但如今超大型廠商已迎頭趕上，Meta 則以一家兼具超大型廠商規模、AI 原生架構、且沒有傳統歷史包袱的「第三型態」進入市場。

對台灣科技產業而言，Meta Compute 的影響牽涉廣泛。台灣是全球 GPU 伺服器、AI 加速器模組、高速網路設備的主要供應商，Meta 擴大外部雲端業務，代表的是新一輪算力軍備競賽——直接拉動對台灣製造能力的需求。廣達、緯穎、鴻海旗下的 AI 基礎建設事業，都可能成為這波擴張的主要受益者之一。

企業採購決策者在制定 AI 基礎建設策略時，眼前最關鍵的問題不再是 Meta Compute 是否會成真——市場已以股價反映了這個現實——而是它何時上線、定價如何，以及把 Meta 開源模型與裸機算力緊密整合的「一站式承諾」，是否值得承擔把社群媒體公司當成主力雲端供應商的集中風險。
