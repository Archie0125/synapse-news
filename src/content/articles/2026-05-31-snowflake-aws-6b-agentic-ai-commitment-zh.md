---
title: "Snowflake 豪擲 60 億美元押注 AWS：企業代理式 AI 最大基礎設施豪賭"
summary: "Snowflake 於 2026 年 5 月 27 日宣布與 Amazon Web Services 簽署 60 億美元、為期五年的最大規模雲端承諾，目標是加速企業代理式 AI 落地。協議涵蓋 AWS Graviton 處理器及 GPU 加速 EC2 實例，作為 Cortex AI 平台的算力基礎——2025 年客戶在 AWS 上的 Snowflake 消費已翻倍至 20 億美元。"
category: "industry"
publishedAt: 2026-05-31
lang: "zh"
featured: false
trending: false
sources:
  - name: "Snowflake Press Release"
    url: "https://www.snowflake.com/en/news/press-releases/snowflake-expands-aws-collaboration-with-6b-commitment-to-accelerate-enterprise-agentic-ai-adoption/"
  - name: "PYMNTS"
    url: "https://www.pymnts.com/artificial-intelligence-2/2026/snowflake-commits-6-billion-to-aws-for-global-ai-expansion/"
  - name: "The AI Insider"
    url: "https://theaiinsider.tech/2026/05/28/snowflake-signs-6b-aws-deal-driven-by-ai-workloads-and-graviton-chip-demand/"
  - name: "The New Stack"
    url: "https://thenewstack.io/snowflake-aws-6b-commitment/"
tags:
  - "snowflake"
  - "aws"
  - "代理式ai"
  - "企業ai"
  - "雲端基礎設施"
  - "cortex-ai"
  - "graviton"
  - "資料平台"
relatedSlugs:
  - "2026-05-28-kpmg-anthropic-claude-276000-employees-zh"
  - "2026-05-28-openai-deployment-company-deployco-4b-enterprise-zh"
---

Snowflake 與 Amazon Web Services 的關係，過去大多是結構性的：AWS 是 Snowflake 運行其上的雲端基礎設施。2026 年 5 月 27 日宣布的 60 億美元、五年期承諾，從根本上改寫了這段關係。Snowflake 正在押注：作為企業 AI 平台，其未來與 AWS 的算力基礎設施不可分割——而 60 億美元這個數字，足以向客戶和競爭對手同時傳達戰略決心。

這筆 60 億美元承諾是 Snowflake 迄今最大的雲端採購協議，涵蓋亞馬遜基於 ARM 架構的 Graviton 處理器及 GPU 加速 EC2 實例。這不是一筆營收協議——Snowflake 並未承諾在 AWS Marketplace 上銷售 60 億美元的產品——而是一筆成本承諾：Snowflake 將花費 60 億美元購買在 AWS 基礎設施上運行其日益龐大的 AI 工作負載所需的算力。

## 代理式轉型的戰略布局

協議時機折射出 Snowflake 的定位野心——搶佔企業軟體分析師所稱「代理式企業」轉型的核心位置：從 AI 系統回答問題，轉型為 AI 系統自主執行跨越組織資料、工具和業務流程的多步驟工作流程。

Snowflake 的 Cortex AI 平台已在企業 AI 任務中承擔了可觀的工作量：文字轉 SQL 查詢生成、文件摘要、客戶資料情感分析、非結構化文字中的實體抽取。這些都是高價值但本質上被動的能力——用戶提問，系統回答。

代理式延伸意味著構建不需要等待提問的系統。在 Snowflake 平台上運行的代理式 AI 將主動監控資料管線、偵測異常、透過查詢相關資料集識別可能原因、若異常超出閾值則上報人工、並自動歸檔事故報告——全程無需用戶發起任何指令。這種持續運行、多步驟、帶回饋迴路的 AI 的算力需求，遠比批次查詢處理密集，這也是 Snowflake 需要大規模鎖定基礎設施的主要原因。

## Cortex AI 與資料護城河

Snowflake 的核心競爭論述是：AI 在企業自有資料上——有治理、即時、可信任——運行時，遠比在訓練資料或合成近似資料上運行更有價值。這個立場比表面看起來更難撼動，因為最高價值的企業 AI 應用場景，恰恰是那些需要存取專有資料的場景：分析客戶行為、預測供應鏈、監控財務倉位，或了解員工模式。

Cortex AI 是這個論述的承載工具。透過將 AI 能力嵌入 Snowflake 資料平台內部，而非將資料路由到外部 AI 服務，Snowflake 為企業客戶提供了一條不需要解決資料治理難題的 AI 路徑——而資料治理問題正是許多 AI 專案的阻塞因素。法務團隊可以對合約資料進行 AI 摘要，無需資料離開其已受治理的環境；金融機構可以對交易資料執行詐欺偵測模型，無需與外部 AI 廠商簽訂資料傳輸協議。

Cortex Code 作為程式碼助理的衍生版，將同樣的邏輯應用於軟體開發：它能分析企業自有的程式庫、文件和提交歷史，提供情境相關的協助，而非泛型的程式碼生成。

## Natoma 收購：代理式連接的最後一哩

在 AWS 協議宣布同週，Snowflake 宣布收購 Natoma——一家企業模型上下文協議（MCP）平台，幫助 AI 代理安全地連接執行工作流程所需的外部工具和系統。這筆收購折射出一個認識：在企業環境中部署代理式 AI，最難的部分不是 AI 本身，而是整合層——以尊重安全邊界、維持可稽核性的方式，將 AI 代理連接到 CRM 系統、ERP 平台、內部 API 和業務工具。

由 Anthropic 作為開放標準推出的 MCP，已在短時間內成為代理式 AI 工具連接的事實標準。透過收購以 MCP 為核心構建產品的公司，Snowflake 讓 Cortex AI 代理能夠與日益增長的 MCP 相容企業工具生態系統原生互通，無需 Snowflake 自行構建每一個整合。

## 支撐 60 億美元的數字邏輯

在 Snowflake 近期財務走勢的背景下，AWS 承諾的規模自有其道理。客戶在 AWS 上的 Snowflake 服務消費於 2025 年翻倍，達到全年 20 億美元。自 Snowflake 首次出現在 AWS Marketplace 以來，客戶累計銷售已超過 70 億美元；2025 年的年銷售額突破 20 億美元，使 Snowflake 對 AWS 的生命週期採購規模足以支撐前瞻性的多十億美元承諾。

需求驅動力一目了然：Snowflake 的 Cortex AI 工作負載增長速度超過其傳統資料倉儲工作負載，而 Cortex AI 運行在 Graviton 和 GPU 加速 EC2 實例上，而非驅動 Snowflake 歷史增長的通用算力。為了滿足企業 AI 推理延遲和可靠性的 SLA 承諾，並為運行持續代理工作負載的客戶提供定價可預測性，Snowflake 需要大規模的預留容量。60 億美元的承諾實際上將這一容量鎖定到 2031 年。

Graviton 處理器的選擇意義深遠。對於推理工作負載，AWS 基於 ARM 的 Graviton 晶片比同等規格的 x86 實例提供更佳的性價比——當推理成為持續運行的成本而非偶發查詢的成本時，這是一個有意義的考量。將 Graviton 與 GPU 加速 EC2 配對用於訓練及計算密集型推理，構建了與 Snowflake 不同 AI 工作負載類型相匹配的分層基礎設施。

## 競爭格局

Snowflake 的 AWS 承諾，發生在企業 AI 平台定位競爭最激烈的時刻。微軟 Azure 透過 OpenAI 模型整合以及 Copilot 在 Office 365 和 Dynamics 中的滲透，將 AI 嵌入了企業用戶日常使用的工作流程工具。Google Cloud 透過 BigQuery 和 Vertex AI，提出了類似的「資料分析與 AI 能力應共存」的主張。Databricks 作為 Snowflake 最直接的競爭對手，也在積極擴展 AI 能力，並剛完成一輪大型融資，獲得了可觀的加速資源。

在這一環境下，60 億美元的 AWS 承諾除了純粹的基礎設施採購，還服務於多重功能。它向企業客戶發出訊號：Snowflake 對 AWS 託管 AI 做出了長期押注——這對已標準化 AWS 並希望其 AI 基礎設施與雲端策略保持一致的客戶尤為重要。它也向 AWS 發出訊號：Snowflake 是戰略夥伴，這通常意味著聯合銷售、聯合行銷資源以及進入 AWS 自身產品路線圖討論的通道。

## 對企業 AI 採購的啟示

對企業技術採購者而言，Snowflake-AWS 協議是一個持續對話中的數據點：AI 基礎設施應如何整合。協議的邏輯——最有價值的 AI 在企業自有的受治理資料上、在同時處理資料管理和 AI 執行的平台內運行——對那些已在雲端資料基礎設施上做出重大投入的機構而言，極具說服力。

這筆協議解鎖的具體 AI 能力，並不主要關乎獲取更強大的基礎模型——Snowflake 的 Cortex AI 已整合了來自 Anthropic、Meta、Mistral 等廠商的基礎模型。價值主張在於：在企業專有資料上持續大規模運行這些模型，具備企業採購所要求的治理和可靠性特性。

隨著代理式 AI 在企業中從概念驗證走向生產部署，持續運行 AI 工作流程的算力經濟學——而非偶發的查詢處理——將成為決定性的競爭和成本因素。Snowflake 的 60 億美元承諾，是一個關於「我已正確判斷這些經濟學的落腳點」的賭注，以及「跟隨我的企業客戶，將發現基礎設施已在等待他們」的信心宣示。
