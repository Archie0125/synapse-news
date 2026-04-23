---
title: "Google 在 Cloud Next 2026 發表 Ironwood TPU，並將第八代晶片拆分為訓練與推論兩條專用路線"
summary: "Google 在 Cloud Next 2026 大會上正式推出第七代 Ironwood TPU，單顆晶片達 4.6 petaFLOPS、9,216 顆組成的超大 Pod 可輸出 42.5 exaFLOPS，效能較 TPU v5p 大幅提升 10 倍。同時預告第八代架構將一分為二：由 Broadcom 設計的訓練晶片「Sunfish」與 MediaTek 設計的推論晶片「Zebrafish」，均採台積電 2nm 製程，目標 2027 年量產。搭配 7.5 億美元合作夥伴基金與 A2A 智能代理協定擴張，Google 對 Nvidia AI 基礎設施霸主地位的挑戰已是史上最全面的一次。"
category: "hardware"
publishedAt: 2026-04-23
lang: "zh"
featured: false
trending: true
sources:
  - name: "Google Cloud 部落格 — Ironwood TPU"
    url: "https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads/"
  - name: "Google 官方部落格 — Ironwood：推論時代的第一款 TPU"
    url: "https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/"
  - name: "TechCrunch — Google Cloud 發表兩款新 AI 晶片"
    url: "https://techcrunch.com/2026/04/22/google-cloud-next-new-tpu-ai-chips-compete-with-nvidia/"
  - name: "The Next Web — Ironwood TPU 報導"
    url: "https://thenextweb.com/news/google-ironwood-tpu-inference-cloud-next"
tags:
  - "Google"
  - "TPU"
  - "Ironwood"
  - "AI 晶片"
  - "Nvidia"
  - "Cloud Next"
  - "AI 基礎設施"
  - "Gemini"
relatedSlugs:
  - "2026-04-11-rebellions-400m-rebelrack-nvidia-inference-zh"
  - "2026-04-17-nvidia-ising-quantum-ai-models-zh"
  - "2026-04-10-google-gemini-31-flash-live-zh"
---

Google 選擇在其年度最大客戶盛會上，對 Nvidia 的 AI 晶片霸主地位發動迄今最全面的攻勢。4 月 22 日，在拉斯維加斯舉行的 Google Cloud Next 2026 大會上，Google 正式推出第七代張量處理器 Ironwood，同步預告第八代將首度拆分成訓練與推論兩款專用晶片。配合 7.5 億美元的代理 AI 合作夥伴基金，以及智能代理互通協定的大幅擴張，Google 展示了一幅足以讓 Nvidia 正視的競爭藍圖。

## Ironwood：為推論時代而生

命名本身就帶有宣示意味。Google 將 Ironwood 定義為「推論時代的第一款 TPU」，折射出 AI 運算需求的根本轉變。深度學習早年，訓練是 GPU 資源的最大消耗者；如今，隨著前沿模型陸續部署給數億用戶，即時預測——也就是推論——正以更快的速度吃掉資料中心的運算預算。

Ironwood 單顆晶片的算力達 4.6 petaFLOPS，搭載 192 GB 高頻寬記憶體（HBM）。在 9,216 顆晶片組成的超大 Pod 規模下，總算力可達 42.5 exaFLOPS——這個數字放在三年前根本難以想像。與前代相比，Ironwood 的峰值效能較 TPU v5p 提升 10 倍，較不到兩年前推出的 TPU v6e Trillium 提升超過 4 倍，訓練與推論工作負載均受益。

Ironwood 的關鍵設計選擇之一，是採用解耦合的記憶體架構：運算與記憶體可以各自獨立擴展。這對同時服務數百萬推論請求的場景至關重要，因為在此類工作負載中，記憶體頻寬往往比原始算力更早成為瓶頸。Google 同時重新設計了晶片間的互連架構，讓 Pod 中所有晶片能共享統一的高頻寬記憶體池，而非在晶片間反覆複製資料——這是針對長上下文推論的直接優化，Gemini 等模型在單次對話中有時需要處理數十萬個 token，任何額外的記憶體傳輸延遲都會直接影響用戶體驗。

Ironwood 現已在 Google Cloud 上線，客戶可以按需配置，與市面上的 H100 或 GB200 實例直接比較選購——這標誌著 Google TPU 長期只供內部使用的時代正式終結。

## 第八代：一分為二的架構賭注

比 Ironwood 的正式上市更具戰略意義的，是 Google 預告的第八代晶片路線圖——這將是 Google 首次為訓練與推論分別設計專用晶片，而非延續過去「一顆晶片打天下」的通用路線。

代號「Sunfish」的 TPU 8t 由 Broadcom 聯合設計，專攻訓練工作負載。單個超大 Pod 可擴展至 9,600 顆晶片，支援 2 PB 共享 HBM，預計算力為 Ironwood 的三倍。訓練晶片與推論晶片均採用台積電 2nm 製程，預計 2027 年底量產。

代號「Zebrafish」的 TPU 8i 則由 MediaTek 聯合設計——這個組合頗不尋常，也說明了 Google 在矽智財設計上的合作半徑有多廣。Zebrafish 採用全新「Boardfly」拓撲，單個 Pod 可直接互連 1,152 顆晶片，片上 SRAM 是前代的三倍（讓 KV 快取可以完整存放在晶片上，避免讀寫較慢的外部記憶體），並整合了專用的集體運算加速引擎。Google 表示，與前代相比，Zebrafish 的推論性價比提升 80%。

這個拆分決策，是對 Nvidia 所代表的通用 GPU 典範的直接否定。它押注的是：到 2027 年，訓練與推論在記憶體存取模式、並行需求與功耗特性上的差異，將大到一顆晶片無法兼顧的程度。研究機構 HyperFrame Research 形容這是「迄今為止任何超大規模雲端業者對 GPU 典範最直接的架構否定」，並預測如果 Google 能如期量產，未來幾年企業的 AI 硬體採購決策將面貌大變。

## 代理 AI 平台：7.5 億美元基金與 A2A 協定

Cloud Next 2026 不只是一場晶片發布會。Google 宣布投入 7.5 億美元成立代理 AI 合作夥伴基金，面向其 12 萬家合作夥伴生態系，協助企業客戶建置、原型開發與部署自主代理系統。基金內容涵蓋 Google 前線部署工程師的直接技術支援、基礎設施點數、技能培訓計畫，以及原型開發資源。

大會軟體主軸的核心，是 Agent-to-Agent（A2A）協定的擴張。A2A 讓 Gemini 原生代理可以與來自 ServiceNow、Salesforce、Atlassian、SAP 等平台的第三方代理直接通訊，無須任何客製化整合程式碼。實際意義相當顯著：一個在 Salesforce Agentforce 上運行的代理，可以在工作流程進行中將任務移交給 Vertex AI 上的 Gemini 代理，後者再去查詢 ServiceNow 的 IT 資產資料——整個過程透過 A2A 完成，三個系統不需要理解彼此的內部架構。

Google 也發布了 Agent Gateway，一個支援 MCP、A2A 及各種私有協定的多代理系統集中式策略管理層，提供代理間呼叫的可視化、流量限速、合規稽核日誌與存取控制——這正是製造、金融、醫療等受監管產業在大規模部署自主代理前不可缺少的治理基礎設施。

Merck 與 Google Cloud 宣布戰略合作，將在研發工作流程與製造自動化中部署 Gemini Enterprise。顧問公司 Deloitte 則宣布將利用 A2A 協定為企業客戶建置跨平台代理工作流程，打通高價值的端對端業務場景。

## 競爭格局

時機的選擇並非偶然。Nvidia 的 GB200 NVL72 系統仍是密集 AI 訓練的性能標竿，其軟體生態與客戶關係構成的護城河，多年來幾乎未受動搖。但競爭環境已在改變：Nvidia 硬體供應持續吃緊，倒逼主要 AI 實驗室加速分散供應鏈風險。Anthropic 與 Google 的合作協議正在擴大至 2027 年的 3.5 GW 算力規模，成為 Ironwood 與第八代平台的最大錨定客戶。Meta 與 Mira Murati 的 Thinking Machines Lab 同樣在本月簽署了數十億美元規模的 Google Cloud 算力協議。

對 Nvidia 而言，Cloud Next 2026 最大的警訊，不是任何單一晶片規格，而是一個事實逐漸成形：全球最大的前沿 AI 實驗室，正在把 Google Cloud 當成 GPU 供應鏈之外真正可行的替代選項。Google 尚未在原始效能上超越 Nvidia，但它已讓業界相信，到 2028 年，AI 硬體市場的面貌將遠比今天多元。
