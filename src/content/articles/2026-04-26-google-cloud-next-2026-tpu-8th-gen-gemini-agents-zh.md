---
title: "Google 全押企業 AI 代理：Ironwood TPU、第八代晶片與 Gemini 企業代理平台"
summary: "在 Google Cloud Next 2026 大會上，Google 推出兩款針對訓練與推理分別設計的第八代 TPU，並將 Vertex AI 重新命名為 Gemini 企業代理平台，是其全棧 AI 佈局、掌握代理式企業 AI 時代的一環。"
category: "ai-ml"
publishedAt: 2026-04-26
modifiedAt: 2026-11-15T00:00:00Z
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

美國拉斯維加斯——Google 帶著一個醞釀多年的核心訊息，再度登上年度 Cloud Next 大會舞台：代理式企業 AI 時代已然來臨，而 Google 要掌控這個時代的每一個層次。從自研晶片到前沿模型，再到統一的軟體平台，Google 發布了有史以來規模最大的企業 AI 公告套組，挑戰對象不僅是 Amazon Web Services 與 Microsoft Azure，更直指 OpenAI 和 Anthropic 的核心領地。

## Ironwood 正式開放商用

基礎設施公告的重頭戲，是第七代 Tensor Processing Unit（TPU）**Ironwood** 的正式商業化——也是 Google 首款明確為「推理時代」而非訓練所設計的 TPU。每顆晶片峰值算力達 4,614 TFLOPs，搭載 192 GB HBM（容量為 Trillium 的 6 倍），頻寬達每秒 7.37 TB。

在大規模部署下，9,216 顆 Ironwood 晶片組成的 pod 可提供 42.5 exaflops 的算力，是全球最大超級電腦 El Capitan 的 24 倍以上。Anthropic 已承諾採用多達 100 萬顆 Ironwood 單元。

## 下一代架構：TPU 8t 與 TPU 8i

然而，Ironwood 在當天的硬體新聞中幾乎已成配角。Google 同步推出第八代 TPU，並首度將其一分為二，打造分別針對訓練與推理的兩款專用晶片。

**TPU 8t** 主攻訓練任務。單一超級節點（superpod）容納 9,600 顆晶片，透過重新設計的晶片間互連（ICI）提供 121 exaflops 算力與 2 petabytes 共享高頻寬記憶體，是 Ironwood 的三倍算力、最高兩倍能效比。首次能在單一節點內完整存放大型模型，徹底消除訓練過程中耗時的跨節點通訊瓶頸。

**TPU 8i** 為推理場景而生，專注於代理規模的低延遲需求。TPU 8i 採用全新「Boardfly」拓撲架構，在單一節點中直接連接 1,152 顆晶片；片上 SRAM 是上一代的三倍；並整合了片上集合通訊加速引擎。結果：推理工作負載的每元算力提升 80%，具備同時執行數百萬個 AI 代理所需的延遲特性——正是企業代理式工作流程的核心需求。

「堪稱傑作，」Amin 在台上形容第八代 TPU。

兩款晶片均與 Google DeepMind 合作設計，預計於今年稍後全面開放。

## Gemini 企業代理平台：重新定義企業 AI

在軟體層面，Google 推出 **Gemini 企業代理平台**，為 Vertex AI 的進化版。這次整合的意義遠不止於品牌重組——統一後的平台涵蓋企業代理的完整生命週期，分為四大能力支柱：構建、擴展、治理與最佳化。

**構建**層引入 Agent Studio（面向非工程師的低代碼視覺化介面），以及 Agent Development Kit（ADK，提供以程式碼優先的 AI 原生開發環境）。**擴展**層的核心是重新設計的 Agent Runtime，能維持代理狀態長達數天，並搭配持久性記憶庫（Memory Bank）跨工作階段存儲長期上下文。

**治理**層直接回應企業對代理最深層的疑慮：可控性。代理身份識別、代理登錄冊與代理閘道三者共同構成中央化治理框架，讓 IT 團隊能清楚掌握哪些代理正在運行、擁有哪些存取權限，以及執行了哪些操作。**最佳化**層則提供部署前測試的代理模擬、基準評測的代理評估，以及提供完整執行追蹤的代理可觀測性工具。

## Workspace 全面走向代理化

Workspace 的系列公告聚焦於 Workspace Intelligence，以及 Google 文件、Gmail、雲端硬碟和 Chat 中的新 AI 功能。**Google Chat 中的 Ask Gemini** 可綜合 Workspace 各處的資訊、提供洞見並主動推送每日簡報；**Gmail AI 收件匣與 AI 概覽**以 Gemini 打造個人化、主動式的收件匣助理；**Google 雲端硬碟專案**則圍繞工作流程需求即時整理檔案與電子郵件。

Google 同時推出 **Workspace Intelligence**——一個學習組織語氣、風格與品牌形象的語義層，自動將其套用於所有內容創作任務。此外，Canvas 功能支援將 Workspace 文件直接匯出為 Office 格式，這是對企業競爭現實的直接回應：微軟的辦公室主場依然根深柢固。

## 安全性：Wiz 整合與 AI 物料清單

Google 以 320 億美元收購雲端安全公司 Wiz 於 2026 年初完成交割，本次大會首次展示整合成果。Wiz 的新項目之一是 **AI 物料清單（AI-BOM）**——自動盤點組織環境中的 AI 框架、模型及 IDE 擴充套件。隨著企業透過「氛圍程式設計」（vibe coding）與第三方代理採購加速 AI 採用，AI 系統的攻擊面急速擴張；AI-BOM 提供了追蹤實際運行狀況的可見性機制。

Google Security Operations 也推出三款新代理：主動搜索新型攻擊模式的**威脅獵捕代理**（預覽中）、識別偵測覆蓋缺口並建立新偵測的**偵測工程代理**（預覽中），以及以第三方內容的情境資料豐富工作流程的**第三方情境代理**（即將開放預覽）。這些任務過去都需要資深安全工程師耗費數小時才能完成。

代理式資料雲（Agentic Data Cloud）同樣帶來新公告：統一動態商業資料脈絡圖的**知識目錄**（Knowledge Catalog）；針對 Apache Spark 的**閃電引擎**（Lightning Engine），效能比開源替代方案快達 4.5 倍、性價比比主要競品高達 2 倍；以及基於 Apache Iceberg 的**跨雲資料湖倉**，讓企業無需複製資料即可查詢存放於 AWS 或 Azure 中的資料。

## Google 的全棧論據

執行長 Thomas Kurian 將這些公告圍繞在統一技術棧之上，晶片、模型、代理與應用共同打造；其主張是 Google 掌握全部四個層次：自研晶片（TPU）、前沿模型（Gemini）、雲端平台（Gemini 企業代理平台）與企業發行通路（Workspace）。

「為模型設計的晶片、以你的資料為基礎的模型、以這些模型構建的代理與應用，」Kurian 在台上描述他所說的「整合式賭注」。

這個賭注現在明確地將 OpenAI 和 Anthropic 列為對手，就如同它鎖定微軟和 AWS 一樣。一邊透過基礎設施提供 Anthropic 模型、一邊與其直接競爭平台業務——Google 正在下一盤複雜的棋，而少有公司具備這樣的資產基礎。

「我們一直以來的重要焦點，就是成為我們自有技術的第一個客戶，」Pichai 在開場致詞中表示。

## 下一步

兩款第八代 TPU 預計於今年稍後全面開放。Gemini 企業代理平台是 Vertex AI 的進化版。

Google 的全棧策略能否轉化為持久的企業收入——對抗微軟主導的裝機量與 OpenAI 在開發者社群的品牌磁力——或將決定這家公司雲端業務的未來數年走向。Cloud Next 2026，是 Google 迄今最清晰的一次戰略宣示。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 21 處。*
