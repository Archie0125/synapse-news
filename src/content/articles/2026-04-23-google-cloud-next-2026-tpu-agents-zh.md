---
title: "Google Cloud Next 2026：全新 TPU 晶片、Gemini 企業代理平台，以及 7.5 億美元的生態系押注"
summary: "Google 在 2026 年 Cloud Next 大會上發表第八代 TPU 晶片、完整的 Gemini 企業代理平台，並宣布投入 7.5 億美元扶植合作夥伴生態系，全力押注成為代理式 AI 時代的全堆疊基礎設施供應商。目前已有 75% 的 Google Cloud 客戶使用 AI 產品，330 家客戶每月處理超過一兆個 token，規模之龐大令競爭對手難以忽視。"
category: "developer-tools"
publishedAt: 2026-04-23
lang: "zh"
featured: true
trending: true
sources:
  - name: "Google Cloud 官方部落格"
    url: "https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next26"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/22/google-cloud-next-new-tpu-ai-chips-compete-with-nvidia/"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/google-cloud-next-ai-agents-agentic-era"
  - name: "9to5Google"
    url: "https://9to5google.com/2026/04/22/google-workspace-intelligence/"
tags:
  - "Google"
  - "TPU"
  - "Gemini"
  - "AI 代理"
  - "雲端運算"
  - "開發工具"
  - "企業 AI"
relatedSlugs:
  - "2026-04-10-google-gemini-31-flash-live-zh"
  - "2026-04-17-microsoft-mai-image-2-efficient-zh"
  - "2026-04-22-google-chrome-gemini-apac-skills-zh"
---

每年的 Google Cloud Next 大會都是觀察這家搜尋巨頭企業野心的最佳窗口，但 2026 年的版本在規模與急迫感上截然不同。在舊金山的兩天議程裡，Google 推出了多年來最全面的硬體與軟體平台更新——挑戰輝達地位的新晶片、對抗微軟與 Anthropic 的全堆疊代理協作框架，以及 7.5 億美元的資金承諾，拉攏旗下 12 萬個合作夥伴一同進入代理式 AI 時代。

Google 的核心論點很明確：它要掌控從自製晶片到行銷人員每天使用的無代碼代理建構工具的整條 AI 價值鏈。

## 兩款晶片，正面挑戰輝達推論霸主地位

最受矚目的硬體公告，是 Google 首次將張量處理器（TPU）產品線一分為二，針對不同工作負載推出專屬架構。

**TPU 8t** 定位於 AI 訓練，效能是上一代 Ironwood 的三倍、每瓦效能提升兩倍。每個 TPU 8t 超級節點可擴展至 9,600 顆晶片並共享 2 PB 記憶體，目標是將前沿模型的訓練週期從「數月壓縮至數週」。

**TPU 8i** 則是專為推論設計的晶片，也是更具攻擊性的競爭動作。其 Boardfly 拓撲架構在單一機架中直接連接 1,152 顆 TPU，片上 SRAM 容量是上一代的三倍，以存放更大的鍵值快取（KV cache）。Google 宣稱在低延遲目標下，TPU 8i 的每美元效能比 Ironwood 提升 80%——尤其針對混合專家（MoE）架構的大型前沿模型。在這類模型的規模下，SRAM 容量直接決定能否避免昂貴的記憶體存取，TPU 8i 的設計正是圍繞這個瓶頸展開。

Google 同時發表了 **Virgo Network**，一個專為 AI 工作負載打造的網路架構，可將輝達 Vera Rubin NVL72 機架或 TPU 8t 超級節點連接成大規模共享超級電腦。這明確承認了 AI 基礎設施之戰不只是晶片算力的競爭，互連能力同樣關鍵。配套基礎設施同樣亮眼：Managed Lustre 儲存透過 RDMA 直連 TPU 8t，吞吐量達 10 TB/秒；Rapid Storage 從 6 TB/秒提升至 15 TB/秒；Google Kubernetes Engine 每秒可部署 300 個安全沙箱，首個指令的響應時間低於一秒。

## Gemini 企業代理平台全面上線

軟體層面，Google 發表了 **Gemini 企業代理平台（Gemini Enterprise Agent Platform）**，圍繞「建構、擴展、治理、優化」四大支柱，打造企業級 AI 代理的全生命週期管理框架。

**建構層**包含基於圖形的代理協作框架 Agent Developer Kit（ADK）、低代碼的 Agent Studio，以及代理的集中發現與治理入口 Agent Registry。Agent Marketplace 上架了來自 Atlassian、Box、ServiceNow、Workday、Oracle 等夥伴的預建代理。

值得注意的是，Google 原生支援 **Model Context Protocol（MCP）**，並已將整個 Google Cloud 服務套件開放為 MCP 端點，讓任何兼容 MCP 的代理框架都能直接調用 Google 的雲端服務。

**擴展層**引入了可在安全隔離沙箱內執行多步驟自主工作流程的長時執行代理（Long-running Agents），以及能跨越數月互動歷史的 **Memory Bank** 持久記憶功能——這一能力是企業部署與消費者聊天機器人的根本差異所在。

**治理層**則回應了企業不可能在缺乏可稽核性的情況下部署自主代理的現實。Agent Identity 為每個代理發行具備可稽核授權策略的加密身份；Agent Gateway 執行即時政策並整合 Model Armor 防護，防範提示注入、工具污染與資料洩漏；Agent Anomaly Detection 主動標記可疑行為。

早期企業部署案例印證了這套平台的深度：KPMG 在首月達到 90% 的員工採用率並部署超過 100 個代理；Mars 將其用作全球員工的「主要 AI 作業系統」；NASA 則部署代理用於 Artemis II 任務的飛行準備評估與太空人安全協定。

## Workspace 獲得智能統合層

在企業開發者平台之外，Google 還宣布了 **Workspace Intelligence**——一個打通 Gmail、雲端硬碟、文件、試算表與簡報的語意整合層。

旗艦功能 **AI Inbox** 以個人助理的角色主動整理 Gmail 收件匣，根據個人工作脈絡自動排序與摘要郵件。**Google Chat 中的 Ask Gemini** 可跨組織整合資訊並執行多步驟任務，包括安排會議、建立文件、從連接服務中提取資料。

在內容創作方面，Google 以代理式工作流程重新打造了核心應用：文件可根據使用者既有的寫作風格生成初稿；試算表能從一句話指令將原始資料轉為互動式儀表板；簡報可從單一提示建立完整的品牌化投影片。

Google 也推出鮮明的跨越移轉訴求，宣稱企業從 Microsoft 365 遷移至 Google Workspace 的速度可「加快五倍」，明確瞄準長期觀望的大型企業客戶。

## 7.5 億美元拉攏合作夥伴生態系

或許最具戰略意義卻也最低調的公告，是面向 12 萬個合作夥伴的 **7.5 億美元基金**，資助系統整合商、ISV 與顧問公司加速建構並部署以代理為核心的解決方案。Google 指出旗下合作夥伴生態系已有 33 萬名受訓顧問。

這個邏輯並不難理解：企業軟體市場歷來由合作夥伴而非直銷決勝負。透過補貼夥伴在 Gemini Enterprise 而非 OpenAI 或 Anthropic API 上建構，Google 試圖鎖定最終決定大型組織標準化哪套 AI 平台的專業服務層。

## 採用曲線已超出預期

Google 公布的商業數字，描繪出一幅 18 個月前難以想像的企業採用圖景：330 家客戶每月在 Google Cloud 上處理超過一兆個 token，其中 35 家超過十兆；API 每分鐘服務 160 億個 token，比上季增加 60 億；Gemini Enterprise 付費月活躍用戶在 2026 年第一季環比增長 40%。

## 全堆疊賭注的本質

Cloud Next 2026 呈現的是一家公司在執行一個連貫的全堆疊策略：針對自有模型調校的自製晶片、代理部署的協作框架、治理代理的安全層、代理規模檢索的資料架構，以及將代理嵌入日常工作的生產力套件。

風險同樣顯而易見——需要同時在如此廣泛的戰線上競爭，對手卻都在單一層面深耕。微軟透過 Office 掌握企業生產力關係；OpenAI 在前沿模型品質上領先；Anthropic 是安全敏感型企業部署的首選。

但 Google 的論點是：代理式時代需要所有這些層次協同運作，當訓練基礎設施、推論晶片、代理框架、資料平台與生產力套件來自同一家廠商時，遷移成本會呈複利累積。Cloud Next 2026，正是 Google 對這場賭注最完整的一次公開宣示。
