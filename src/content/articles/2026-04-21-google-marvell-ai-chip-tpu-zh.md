---
title: "Google 洽談與 Marvell 聯合開發兩款 AI 晶片，重塑訂製矽競賽格局"
summary: "Google 正在洽談與 Marvell Technology 共同開發兩款新 AI 晶片：一款專門消除推理瓶頸的記憶體處理器（MPU），以及一款更便宜、更節能的推理優化 TPU。此舉將 Marvell 納為第三個訂製晶片設計夥伴，消息一出 Marvell 股價大漲，Broadcom 股價則應聲重挫。"
category: "hardware"
publishedAt: 2026-04-21
lang: "zh"
featured: false
trending: true
sources:
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/04/20/marvell-stock-google-custom-ai-chips.html"
  - name: "BNN Bloomberg"
    url: "https://www.bnnbloomberg.ca/investing/2026/04/20/marvell-shares-gain-on-report-of-deal-talks-with-google-to-develop-two-ai-chips/"
  - name: "WCCFTech"
    url: "https://wccftech.com/google-pulls-marvell-into-a-two-chip-tpu-plan-reshaping-ai-inference-for-asics/"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/google-marvell-ai-chips-inference-tpu-broadcom"
tags:
  - "google"
  - "marvell"
  - "tpu"
  - "ai晶片"
  - "訂製矽"
  - "推理"
  - "硬體"
relatedSlugs:
  - "2026-04-15-meta-broadcom-mtia-chip-deal-zh"
  - "2026-04-10-tsmc-q1-2026-record-revenue-zh"
  - "2026-04-08-semiconductor-sales-record-2026-zh"
---

Google 減少對 Nvidia 依賴的戰略出現重大新進展。根據《The Information》的報導，Alphabet 正積極洽談與 Marvell Technology 共同開發兩款獨立的 AI 晶片——此安排將使 Marvell 成為繼 Broadcom 和 MediaTek 之後的第三個訂製矽設計夥伴，也標誌著 Google 在推理成本成為 AI 部署核心變數的背景下，刻意推動 AI 基礎設施供應鏈多元化的決心。

消息傳出後，Marvell 股價於 4 月 20 日盤前大漲逾 5%，延續其今年迄今約 84% 的漲幅。目前負責設計 Google 張量處理器（TPU）的 Broadcom 股價則應聲重挫，顯示投資人將此訊息解讀為 Google 訂製晶片策略的局部重組。

## Google 想讓 Marvell 打造的兩款晶片

據報導，此次合作涵蓋兩款具有不同功能定位的晶片：

**記憶體處理器（MPU）**：第一款晶片將作為 Google 現有 TPU 群的補強。TPU 針對主導模型訓練與大規模推理的矩陣乘法工作負載進行了優化，但在記憶體介面面臨日益嚴重的瓶頸——即資料進出處理核心的速度限制。擬議中的 MPU 將直接解決這一問題，緊鄰 TPU 部署，以專用硬體管理記憶體操作，降低目前制約大型模型吞吐量的延遲損耗。

Google 和 Marvell 據報計劃在未來一年內完成 MPU 設計，再進入試量產階段，初始生產目標約為 200 萬顆。

**推理優化 TPU**：第二款晶片則是全新架構的 TPU，專為推理工作負載設計——即已訓練好的模型實際服務用戶請求的階段。這款晶片的設計目標是比現有 TPU 世代更低的生產成本和更高的每次推理能耗效率，現有 TPU 原本是以訓練工作負載為設計基礎。隨著 AI 應用從數千擴展至數億日活用戶，推理成本——而非訓練成本——已成為 AI 公司的主要營運支出。

## 為什麼重要：推理才是當下的戰場

從訓練轉向推理的重心轉移，反映了 2026 年 AI 產業運作方式的根本性變化。2022 至 2023 年間，最耗費算力的工作負載是前沿模型的預訓練——需要地球上最龐大的 GPU 叢集持續運行數月的一次性任務。如今，這些訓練仍持續進行，但每天為 ChatGPT、Gemini、Claude 及其企業 API 客戶服務數十億次查詢的持續成本，在總量上已遠超訓練成本。

Google 的內部經濟學遵循同樣的邏輯。在搜尋、Workspace 和消費者 App 中服務 Gemini 查詢需要持續大規模運行的推理容量，優化這些工作負載的每 token 成本已成為首要工程優先事項。更便宜、更高效的推理專用 TPU 將大幅降低每次 Gemini API 呼叫的運營成本。

根據市場研究，涵蓋 Google TPU、Meta MTIA、Amazon Inferentia 和微軟 Maia 的訂製 ASIC 市場預計在 2026 年成長 45%，並在 2033 年達到 1,180 億美元。根本驅動力正是這一轉變：超大規模雲端業者正發現，通用 GPU 並非其規模下穩定推理的最經濟工具。

## Marvell 在 AI 晶片生態系中的位置

Marvell 在消費科技領域並非家喻戶曉，但在半導體供應鏈中占據戰略要地。該公司在訂製 ASIC 設計、網路矽和高速互連方面擁有深厚積累——正是超大規模業者設計專用晶片時所需的核心能力。

Marvell 已在為亞馬遜 AWS 和微軟 Azure 設計訂製晶片，在長期大量客戶關係的管理上已有成熟模式。若將 Google 納入客戶名單，將鞏固 Marvell 作為主要雲端業者首選訂製矽設計夥伴的地位——在三大超大規模業者為 AI 基礎設施合計投入數千億美元的背景下，這一利基市場正在快速成長。

Marvell 今年 84% 的年初至今漲幅，反映出投資人對這一定位的認可，遠超 Nvidia 同期約 30% 的漲幅——表明訂製 ASIC 廠商在 AI 資本支出激增的背景下，正被視為結構性受益者。

## Broadcom 的糾葛

Marvell 談判的複雜之處在於 Broadcom 與 Google 現有的合作關係。Broadcom 多年來一直是 Google 的主要 TPU 設計夥伴，據報導雙方本月初剛剛敲定了一份涵蓋現有 TPU 路線圖、延伸至 2031 年的新協議。Broadcom 執行長 Hock Tan 已將 AI 訂製矽定位為公司核心成長驅動力，並在投資人面前對其進行多年收益順風的描繪。

Google 同時與 Marvell 進行談判，未必意味著要退出 Broadcom 關係——討論中的兩款晶片與 Broadcom 現有 TPU 的功能不同。但傳遞給 Broadcom 的信號十分清晰：Google 不滿足於在訂製矽上採用單一供應商方式，正在積極培養同時管理多個晶片設計關係的能力。

這種多元化在戰略上完全合理。隨著 AI 基礎設施成本成為競爭定位的決定性變數，超大規模業者有強烈動機在其矽供應鏈中保持靈活選擇空間，避免對任何單一廠商形成可能產生定價籌碼的關鍵依賴。

## 下一步展望

Google 與 Marvell 的討論尚未形成簽署的合約，兩家公司均拒絕就報導的談判置評。晶片開發週期漫長——從初始設計規格到量產，一款新訂製 ASIC 通常需要兩至三年——因此此次合作中誕生的任何晶片，最早可能在 2028 或 2029 年進入部署。

從近期市場反應來看，投資人將這則報導視為訂製 AI 晶片市場擴張速度超出預期的證明，以及 Marvell 有望在此擴張中捕獲重要份額的信號。對於持續主導通用 AI 算力市場的 Nvidia 而言，超大規模業者不斷擴大的訂製 ASIC 計畫，代表著可定址市場的緩慢但持續的邊際侵蝕。

矽晶大戰並非二元對立。它將在數十種專業化工作負載上決定勝負——每一顆超大規模業者自行設計的晶片，都是 Nvidia 少賣出的一顆。
