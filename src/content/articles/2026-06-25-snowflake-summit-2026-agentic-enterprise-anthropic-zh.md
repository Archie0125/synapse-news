---
title: "Snowflake 全力押注企業 AI 代理，CoWork、CoCo 攜手 Anthropic 重塑數據平台"
summary: "Snowflake Summit 2026 於 6 月 2 日在舊金山登場，執行長 Sridhar Ramaswamy 以「代理型企業」為主軸，發布超過 26 項新功能，包含面向知識工作者的個人 AI 代理 CoWork，以及全棧 AI 編程代理 CoCo。Anthropic 總裁 Daniela Amodei 上台共同主講，Claude Opus 4.8 同步上架驅動兩款新品，標誌 Snowflake 從數據平台向企業 AI 作業系統的戰略轉型。"
category: "industry"
publishedAt: 2026-06-25
lang: "zh"
featured: false
trending: false
sources:
  - name: "Snowflake: CoWork Powers the Agentic Enterprise"
    url: "https://www.snowflake.com/en/news/press-releases/snowflake-cowork-powers-the-agentic-enterprise-as-the-personal-agent-for-knowledge-workers-to-work-smarter/"
  - name: "Snowflake: CoCo Redefines Enterprise AI Development"
    url: "https://www.snowflake.com/en/news/press-releases/snowflake-coco-redefines-enterprise-ai-development-as-the-coding-agent-built-for-faster-easier-and-more-powerful-innovation-anywhere/"
  - name: "Snowflake and Anthropic Accelerate Enterprise AI Adoption"
    url: "https://www.snowflake.com/en/news/press-releases/snowflake-and-anthropic-accelerate-enterprise-ai-adoption-driven-by-rising-demand-for-governed-ai/"
  - name: "Flexera: Snowflake Summit 2026 recap"
    url: "https://www.flexera.com/blog/perspectives/snowflake-summit-2026/"
  - name: "Atlan: Snowflake Summit 2026 — All the Announcements and What They Mean"
    url: "https://atlan.com/know/snowflake/summit-2026-announcements/"
tags:
  - "Snowflake"
  - "CoWork"
  - "CoCo"
  - "Anthropic"
  - "企業AI"
  - "AI代理"
  - "數據平台"
  - "Claude"
  - "企業軟體"
relatedSlugs:
  - "2026-06-04-anthropic-claude-opus-48-dynamic-workflows-zh"
  - "2026-06-23-openai-codex-record-replay-workflow-automation-zh"
  - "2026-06-12-openai-acquires-ona-gitpod-codex-cloud-agents-zh"
---

2026 年 6 月 2 日，Sridhar Ramaswamy 在舊金山 Moscone 中心走上台，迎接他擔任 Snowflake 執行長以來的第二次 Summit 大會。他帶來的，是一家在定位上已明顯轉型的公司。「數據雲」這個詞幾乎消失了；取而代之的，是一個以超過 26 項新功能建構的全棧代理平台，兩款大幅改版並重新命名的產品，以及 Anthropic 總裁 Daniela Amodei 親自登台共同主講的場景。

訊號清晰：Snowflake 要建的，不是最好的數據庫，而是「代理型企業」的作業系統。

## CoWork：一個已經了解你公司的個人 AI 代理

Summit 2026 最具戰略意義的發布，或許正是外表最低調的一個：將 **Snowflake Intelligence** 更名並大幅擴展為 **Snowflake CoWork**。

CoWork 定位為「知識工作者的個人代理」——一個能存取公司受治理 Snowflake 數據、將其轉化為可執行洞察，並在連接的企業系統中採取結構性行動的 AI 系統。與需要在每次對話中從頭建立脈絡的通用 AI 助理不同，CoWork 在 Snowflake 的數據治理框架內運作，每一筆查詢、每一份輸出、每一個行動都有記錄、可稽核，且受到既有數據存取權限的管控。

Ramaswamy 稱之為「已經了解你公司業務的 AI」。邏輯很簡單：通用 AI 助理在企業部署中表現欠佳，往往不是模型能力的問題，而是那些模型缺乏機構脈絡——內部術語、業務邏輯、數據欄位的真實定義——讓輸出結果對特定公司真正有用。

Summit 上宣布的三項新功能充實了這個前提。**Artifacts** 讓 CoWork 可以產生持久、可分享的輸出物——圖表、報告、分析——並與 Snowflake 的數據血緣圖譜掛鉤，讓下游使用者能追溯任何分析結果來自哪些原始數據表。**Cortex Sense**（詳見下文）確保 CoWork 理解數據標籤的業務含義，而非只看技術schema。新的個人化功能則讓不同角色的使用者——資料科學家與業務主管問同一個問題——能收到深度和術語都適合自己的回答。

## CoCo：Snowflake 殺入 AI 編程代理市場

Summit 2026 的第二個重磅更名，將 **Cortex Code** 升格為 **Snowflake CoCo**——Snowflake 的全棧 AI 編程代理，直接在 GitHub Copilot、Cursor、OpenAI Codex 已佔據的市場中亮相。

CoCo 的差異化主張在於脈絡。通用編程代理只能看到開發者正在撰寫的程式碼；CoCo 還能看到 Snowflake 的數據結構（schema）、轉換管線，以及定義程式碼運行環境的數據合約。開發者請 CoCo 為新數據模型撰寫 SQL 轉換程式時，不需要解釋有哪些表、欄位名稱是什麼、或資料適用什麼業務邏輯——CoCo 透過 Cortex Sense 早已掌握這些。

這種垂直整合，正是 Snowflake 的核心論點：內嵌於數據層的 AI，比附加在數據層之上的 AI 產出更好的結果。公司押注的是：在 Snowflake 環境中建置 dbt 模型、Snowpark 應用程式和 SQL 管線的數據工程師，會更傾向選擇了解其數據環境的編程代理，而非每次工作都需要手動填充脈絡的通用工具。

這個賭注能否兌現尚有疑問。Cursor 在年輕工程師社群中的心智份額已相當穩固。但 Snowflake 的分發優勢是真實的：它擁有超過 9,000 家企業客戶，其開發者每天都在 Snowflake 環境中工作。問題在於，這些開發者有多少願意換用一個懂自己 schema 的垂直工具。

## Cortex Sense：讓全部工具共用一個大腦

Summit 2026 在架構層面最有意思的發布，是 **Cortex Sense**——不在於它本身做什麼，而在於它如何改變其他一切的架構。

Cortex Sense 是一個語義層，將企業數據的業務含義統一成一個共享脈絡物件，供所有 Snowflake AI 產品使用。它讀取數據表 schema、數據合約、欄位描述、數據血緣圖譜以及 dbt 文件，然後產生一個結構化的脈絡物件，讓 CoWork、CoCo 和任何基於 Snowflake Cortex AI API 建置的第三方工具，都能直接使用而無需重新攝取原始文件。

實際後果是：一家認真維護 Snowflake 文件的公司，會自動獲得對業務理解更深的 AI 產品。當數據結構改變時，Cortex Sense 自動更新，CoWork 和 CoCo 隨之保持同步，開發者不需要在每次數據模型演進時重新對 AI 說明情況。

更深層的含義是架構性的：Cortex Sense 讓公司嵌入 Snowflake 數據模型中的文件和機構知識，成為 AI 產品的一等公民——改變了數據品質投資的經濟邏輯。在 Cortex Sense 框架下，寫得好的數據表描述，立刻轉化為更好的 AI 輸出，形成一個過去難以量化的數據治理投資新誘因。

## Anthropic 深度同盟：居於核心的夥伴關係

驅動 CoWork 和 CoCo 的，是 Anthropic 的 Claude 模型系列。Snowflake 在 Summit 上宣布，**Claude Opus 4.8** 與主題演講同步上架 Snowflake Cortex AI，讓企業可以在 Snowflake 的治理環境內運行 Claude，不必將數據輸出至外部端點。對數據落地有嚴格要求的金融、醫療、政府等行業客戶而言，這個治理邊界內的可用性具有實質的法規遵循意義。

這次合作遠超過 API 串接。Daniela Amodei 親自上台與 Ramaswamy 共同主講，在大型企業軟體會議上屬於異常舉動。更具結構性的是，Snowflake 成為 Anthropic **Claude Marketplace** 十個創始合作夥伴之一——這個機制讓已有 Anthropic 企業合約的公司，可以將現有額度直接用於 Snowflake AI 產品，大幅降低聯合客戶的採購複雜度。

這個安排對雙方都有利。Snowflake 藉此觸達 Anthropic 持續擴大的企業客戶群體——這些公司已完成標準化 Claude 的採購決策，正在尋找在治理框架內應用 Claude 數據能力的管道。Anthropic 則藉此進入 Snowflake 的企業客戶基礎，數據資產早已就位，但能在治理框架內對這些數據採取行動的 AI 產品，仍是相對新生的品類。

## 更大的平台賭注

CoWork 和 CoCo 之外，Snowflake 在 Summit 上還公布了幾項平台層面的能力。

**Cortex Training** 讓企業能以自有 Snowflake 數據對模型進行微調，而不需要將數據移至外部訓練基礎設施——大幅降低了擁有專有數據和擁有反映這些數據的模型之間的摩擦。

**Snowflake Datastream** 是一款全托管 Apache Kafka 串流服務，將即時資料攝入帶入平台。對代理應用而言這很關鍵：CoWork 和 CoCo 在即時數據上才能發揮最大價值，Datastream 提供了讓即時數據以受治理方式流入代理脈絡的管道。

## 這對企業 AI 格局意味著什麼

Snowflake 的布局印證了 2026 上半年在企業 AI 逐漸清晰的一個趨勢：競爭已從單一模型能力轉移到整合平台覆蓋。

沒有任何獨立 AI 工具——無論底層模型多強——能在企業環境中有效運作，除非它能在治理框架內存取正確的數據，並具備稽核記錄滿足法規要求。這個打包問題，正是 Snowflake 定位要解決的：以 Anthropic 的 Claude 作為推理引擎，以 Snowflake 的數據平台作為機構記憶。

公司的戰略賭注是：企業 AI 將像雲端基礎設施一樣向平台集中——就像 AWS、Azure、Google Cloud 在早期混戰後逐漸主導市場。這個類比並不完美，但指向一個值得注意的可能：最終勝出的，不一定是擁有最強單一服務的公司，而是企業願意標準化、治理最完整的平台。

若這個邏輯成立，Summit 2026 或許在日後回顧時，正是 Snowflake 正式宣示這個立場的時刻——以 20,000 名開發者與 Daniela Amodei 同台為證。
