---
title: "Google 全押企業 AI 代理：Ironwood TPU、第八代晶片與 Gemini 企業代理平台"
summary: "在拉斯維加斯舉行的 Google Cloud Next 2026 大會上，Google 宣布第七代 Ironwood TPU 正式開放商用，預覽兩款針對訓練與推理分別設計的第八代晶片，並將整個企業 AI 技術棧整合重命名為 Gemini 企業代理平台——這是 Google 迄今最完整的全棧 AI 佈局，直接挑戰 OpenAI、Anthropic、微軟與 AWS。"
category: "ai-ml"
publishedAt: 2026-04-26
lang: "zh"
featured: false
trending: true
sources:
  - name: "Google Cloud 官方部落格：Next '26 第一天回顧"
    url: "https://cloud.google.com/blog/topics/google-cloud-next/next26-day-1-recap"
  - name: "Google Blog：第八代 TPU"
    url: "https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/"
  - name: "Google Cloud：Ironwood TPU"
    url: "https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/google-cloud-next-ai-agents-agentic-era"
  - name: "Computer Weekly"
    url: "https://www.computerweekly.com/news/366641999/Google-launches-Gemini-Agent-Platform-eighth-generation-TPUs"
tags:
  - "Google"
  - "TPU"
  - "AI 代理"
  - "企業 AI"
  - "雲端運算"
  - "Gemini"
  - "Google Cloud"
relatedSlugs:
  - "2026-04-24-anthropic-19b-arr-claude-code-growth-zh"
  - "2026-04-24-cambridge-neuromorphic-chip-ai-energy-zh"
  - "2026-04-25-google-anthropic-40b-investment-zh"
---

美國拉斯維加斯——Google 帶著一個醞釀多年的核心訊息，再度登上年度 Cloud Next 大會舞台：代理式企業 AI 時代已然來臨，而 Google 要掌控這個時代的每一個層次。從自研晶片到前沿模型，再到服務數十億 Workspace 用戶的統一軟體平台，Google 發布了有史以來規模最大的企業 AI 公告套組，挑戰對象不僅是 Amazon Web Services 與 Microsoft Azure，更直指 OpenAI 和 Anthropic 的核心領地。

## Ironwood 正式開放商用

基礎設施公告的重頭戲，是第七代 Tensor Processing Unit（TPU）**Ironwood** 的正式商業化——也是 Google 首款明確為「推理時代」而非訓練所設計的 TPU。每顆晶片峰值 FP8 算力達 4.6 petaFLOPS，約為上一代 Trillium 的四倍，搭載 192 GB HBM3e 記憶體，頻寬達每秒 7.37 TB。

在叢集規模下，9,216 顆 Ironwood 晶片可提供 42.5 exaflops 的總算力，超過目前所有公開宣布的超級電腦。最具代表性的早期客戶是 Anthropic：根據擴大後的合作協議，這家 AI 安全公司將在 2026 年獲得多達 100 萬顆 TPU 晶片及逾 1 GW 的運算容量，初期階段涵蓋 40 萬顆 Ironwood 單元，已完成機架的採購金額估計約達 100 億美元。

## 下一代架構：TPU 8t 與 TPU 8i

然而，Ironwood 在當天的硬體新聞中幾乎已成配角。Google 同步預告了第八代 TPU 架構，並首度將其一分為二，打造兩款針對不同工作負載的專用晶片。

**TPU 8t** 主攻訓練任務。單一超級節點（superpod）容納 9,600 顆晶片，透過重新設計的晶片間互連（ICI）提供 121 exaflops 算力與 2 petabytes 共享高頻寬記憶體，是 Ironwood 的三倍算力、最高兩倍能效比。首次能在單一節點內完整存放大型模型，徹底消除訓練過程中耗時的跨節點通訊瓶頸。

**TPU 8i** 為推理場景而生，專注於代理規模的低延遲需求。它採用全新「Boardfly」拓撲架構，在單一節點中直接連接 1,152 顆晶片；片上 SRAM 是上一代的三倍，可在晶片上完整快取 KV 儲存而無需存取 HBM；並整合了專用集合通訊加速引擎。結果：推理工作負載的每元算力提升 80%，具備同時執行數百萬個 AI 代理所需的延遲特性——正是企業代理式工作流程的核心需求。

「堪稱傑作，」Google AI 與基礎設施資深副總裁 Amin Vadhat 在台上形容第八代架構。

兩款晶片均由 Google DeepMind 聯合設計，預計透過 AI Hypercomputer 預留計畫於 2026 年下半年開放客戶使用。

## Gemini 企業代理平台：重新定義企業 AI

在軟體層面，Google 將 Vertex AI 與 Agentspace 整合為單一產品：**Gemini 企業代理平台**。這次整合的意義遠不止於品牌重組——統一後的平台涵蓋企業代理的完整生命週期，分為四大能力支柱：構建、擴展、治理與最佳化。

**構建**層引入 Agent Studio（面向非工程師的低代碼視覺化介面），以及 Agent Development Kit（ADK，提供以程式碼優先的 AI 原生開發環境）。**擴展**層的核心是重新設計的 Agent Runtime，能維持代理狀態長達數天，並搭配持久性記憶庫（Memory Bank）跨工作階段存儲長期上下文。

**治理**層直接回應企業對代理最深層的疑慮：可控性。代理身份識別、代理登錄冊與代理閘道三者共同構成中央化治理框架，讓 IT 團隊能清楚掌握哪些代理正在運行、擁有哪些存取權限，以及執行了哪些操作。**最佳化**層則提供部署前測試的代理模擬、基準評測的代理評估，以及提供完整執行追蹤的代理可觀測性工具。

### A2A 協議：多代理通訊的共用語言

本次大會技術含量最高的公告之一，是 **Agent-to-Agent（A2A）協議**的擴展——使 Gemini 原生代理能與 ServiceNow、Salesforce、Atlassian、SAP 等第三方企業軟體廠商的代理進行通訊，無需自行開發整合代碼。對於已部署碎片化代理生態系的企業而言，A2A 有望成為多代理協作的通用標準。

## Workspace 全面走向代理化

Workspace 的系列公告針對每天在 Google 文件、Gmail 和雲端硬碟中工作的逾 3 億企業用戶。**Google Chat 中的 Ask Gemini** 可跨越組織整體資料資產綜合資訊、提供洞見並主動推送每日簡報；**Gmail AI 收件匣與 AI 概覽**充當個人助理，自動分類郵件並起草回覆；**Google 雲端硬碟專案**則圍繞工作流程需求即時整理檔案與電子郵件。

Google 同時推出 **Workspace Intelligence**——一個學習組織語氣、風格與品牌形象的語義層，自動將其套用於所有內容創作任務。此外，Canvas 功能支援將 Workspace 文件直接匯出為 Office 格式，這是對企業競爭現實的直接回應：微軟的辦公室主場依然根深柢固。

## 安全性：Wiz 整合與 AI 物料清單

Google 以 320 億美元收購雲端安全公司 Wiz 於 2026 年初完成交割，本次大會首次展示整合成果。亮點是 **AI 物料清單（AI-BOM）**——自動盤點組織環境中部署的每一個 AI 框架、模型及 IDE 擴充套件。隨著企業透過「氛圍程式設計」（vibe coding）與第三方代理採購加速 AI 採用，AI 系統的攻擊面急速擴張；AI-BOM 提供了追蹤實際運行狀況的可見性機制。

Google Security Operations 也預告了三款新的代理式防禦工具：主動搜索新型攻擊模式的**威脅獵捕代理**、識別偵測覆蓋缺口並自動撰寫偵測規則的**偵測工程代理**，以及以外部情資豐富安全工作流程的**第三方情境代理**。這些任務過去都需要資深安全工程師耗費數小時才能完成。

代理式資料雲（Agentic Data Cloud）同樣帶來新公告：統一動態商業資料脈絡圖的**知識目錄**（Knowledge Catalog）；針對 Apache Spark 的**閃電引擎**（Lightning Engine），效能比開源替代方案快達 4.5 倍、性價比比主要競品高達 2 倍；以及基於 Apache Iceberg 的**跨雲資料湖倉**，讓企業無需複製資料即可查詢存放於 AWS 或 Azure 中的資料。

## Google 的全棧論據

執行長 Thomas Kurian 將所有這些公告整合為一個核心論點：Google 是唯一掌握現代 AI 技術棧全部四個層次的公司——自研晶片（TPU）、前沿模型（Gemini）、雲端平台（Gemini 企業代理平台）與企業發行通路（Workspace 的 30 億用戶）。

「為模型設計的晶片、以你的資料為基礎的模型、以這些模型構建的代理與應用，」Kurian 在台上描述他所說的「整合式賭注」。

這個賭注現在明確地將 OpenAI 和 Anthropic 列為對手，就如同它鎖定微軟和 AWS 一樣。一邊透過基礎設施提供 Anthropic 模型、一邊與其直接競爭平台業務——Google 正在下一盤複雜的棋，而少有公司具備這樣的資產基礎。

Alphabet 執行長 Sundar Pichai 將 AI 代理全面取代企業試點描述為 2026 年的核心挑戰。「我們一直以來的重要焦點，就是成為我們自有技術的第一個客戶，」他在大會上對與會者表示。

## 下一步

第八代 TPU 預計透過 AI Hypercomputer 預留計畫於 2026 年下半年開放客戶使用。Gemini 企業代理平台即日起全面開放，取代此前透過 Vertex AI 和 Agentspace 的存取路徑。針對企業 SaaS 合作夥伴的 A2A 協議擴展正在 2026 年 Q2 陸續推出。

Google 的全棧策略能否轉化為持久的企業收入——對抗微軟主導的裝機量與 OpenAI 在開發者社群的品牌磁力——或將決定這家公司雲端業務的未來數年走向。Cloud Next 2026，是 Google 迄今最清晰的一次戰略宣示。
