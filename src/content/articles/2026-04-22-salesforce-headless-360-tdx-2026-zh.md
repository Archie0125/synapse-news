---
title: "Salesforce Headless 360：把整個企業平台變成 AI Agent 的基礎設施"
summary: "在 TrailblazerDX 2026 大會上，Salesforce 宣布 Headless 360——其 27 年來最大規模的架構重組。平台上所有功能現在都以 API、MCP 工具或 CLI 指令暴露，供 AI Agent 直接調用，無需開啟瀏覽器。60 多個 MCP 工具相容 Claude Code、Cursor、Codex 和 Windsurf，免費開發版內建 Claude Sonnet，Salesforce 正押注企業的未來由 Agent 而非 GUI 驅動。"
category: "developer-tools"
publishedAt: 2026-04-22
lang: "zh"
featured: false
trending: false
sources:
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/salesforce-launches-headless-360-to-turn-its-entire-platform-into-infrastructure-for-ai-agents"
  - name: "Salesforce Ben"
    url: "https://www.salesforceben.com/salesforce-headless-360-and-agentforce-vibes-2-0-revealed-at-tdx-2026/"
  - name: "The Register"
    url: "https://www.theregister.com/2026/04/15/salesforce_headless_360/"
  - name: "Diginomica"
    url: "https://diginomica.com/salesforce-tdx-2026-why-salesforces-headless-360-announcement-tdx-really-about-operating-model"
tags:
  - "Salesforce"
  - "Headless 360"
  - "MCP"
  - "AI Agent"
  - "企業軟體"
  - "Agentforce"
  - "TDX 2026"
  - "開發者工具"
relatedSlugs:
  - "2026-04-04-mcp-protocol-explosion-zh"
  - "2026-04-11-microsoft-agent-framework-1-0-ga-zh"
  - "2026-04-10-mastra-22m-series-a-typescript-agents-zh"
---

上週，Salesforce 在舊金山的 TrailblazerDX 2026（TDX 2026）大會上推出 Headless 360，公司產品領導層稱其為「Salesforce 27 年來最具雄心的架構轉型」。這種誇張說法在矽谷產品發表會上並不罕見，但 Headless 360 的實質內涵確實值得認真對待，它代表了企業軟體公司面對 AI Agent 時代所做的一個根本性選擇。

核心概念直截了當：**Salesforce 平台上的所有功能，現在都可以透過 API、模型上下文協議（MCP）工具或命令列介面（CLI）指令存取**。無論是銷售管道、客服工單佇列、行銷自動化流程、Einstein Analytics 儀表板，還是 Apex 程式碼執行、Flow 自動化——全部都可以由 AI Agent 自主調用、讀取和修改，無需任何人點擊 Salesforce 介面。

## MCP 層：60 多個工具，持續增加

Headless 360 的核心是超過 **60 個新 MCP 工具**的工具庫，這些工具將 Salesforce 功能暴露給 AI 編程 Agent。它們設計為與開發者已在使用的主流 AI 編程工具原生相容：Claude Code、Cursor、Codex 和 Windsurf。

同時發布的還有 **30 個預設編程技能（coding skills）**，這些是針對常見 Salesforce 開發模式預建的 Agent 指令，讓 Agent 能夠執行建立 Apex 觸發器、修改 Flow 設定、執行 SOQL 查詢、部署元數據變更等任務，無需開發者進行大量的提示詞工程。

對台灣開發者和企業 IT 團隊而言，實際影響是這樣的：如果你已經在用 Claude Code 或 Cursor 做一般軟體開發，現在可以讓這些 Agent 直接取得你的 Salesforce 組織資料、業務邏輯和工作流程設定。一個幫助開發者除錯客服案件升級流程的 Agent，可以直接查詢底層 Salesforce 物件、對真實數據執行 SOQL 查詢，並提出修改 Flow 自動化的建議——所有這些都在同一個對話中完成。

Salesforce 也在自家伺服器上托管 MCP 伺服器，開發者不需要自行管理 MCP 基礎設施，降低了小型團隊的運維負擔。

## Agentforce Vibes 2.0：平台內的多模型開發環境

去年推出的 Agentforce Vibes（Salesforce 原生的 vibe coding 環境）在 TDX 2026 獲得重大升級。2.0 版帶來多模型支援，開發者現在可以在 Salesforce 原生 IDE 中選擇 Claude Sonnet、GPT-5 或其他模型作為編程夥伴。

升級後的 Vibes 環境基於 VS Code 架構，採用瀏覽器型雲端托管形式，直接嵌入 Salesforce 平台。它包含一個「開發夥伴」AI，能維持對你特定 Salesforce 組織的 Schema、已安裝套件、自定義物件和業務邏輯的持續感知——這是外部編程 Agent 在沒有明確授權的情況下很難做到的。

**Developer Edition 版本**（Salesforce 供開發者、ISV 合作夥伴和學習者免費使用的環境）現在免費附帶 Agentforce Vibes 2.0，預設使用 Claude Sonnet 4.5 作為編程模型，同時附帶 Salesforce 托管的 MCP 伺服器。換句話說，完整的 AI Agent 開發環境無需生產級 Salesforce 授權就能取得。

## AgentExchange：企業 AI Agent 的應用程式市集

TDX 2026 的第三根支柱是 **AgentExchange**，一個供企業 AI Agent 發布和探索的市集。AgentExchange 的邏輯類似 Salesforce AppExchange——自 2005 年以來一直是最成功的企業軟體市集之一——但從頭為 Agent 時代設計。

在 AgentExchange 上，Salesforce 合作夥伴和獨立開發者可以發布具有特定能力的 Agent：一個監控發票賬齡並啟動催款流程的應收帳款 Agent、一個分析通話記錄並提供個人化反饋的銷售輔導 Agent、一個稽核客戶資料存取合規性的監控 Agent。組織可以透過 MCP 層直接將這些 Agent 安裝到自己的 Salesforce 環境，組合成多 Agent 工作流程，無需撰寫自定義整合程式碼。

## 為什麼叫「Headless」？

「Headless」這個術語在 Web 開發中有明確含義：後端系統暴露 API，不規定前端呈現方式，讓各種介面——網站、App、現在也包括 AI Agent——可以自由調用。

Salesforce 把這個概念應用到整個平台。「360」指的是 Salesforce 一直以來的「Customer 360」行銷框架——完整的客戶視圖。Headless 360 延伸了這個概念：不只是完整的客戶數據視圖，而是對建立在這些數據之上的所有功能的完整程式化存取。

分析師指出，這項轉型根本上是關於**運營模式的變革**，而不只是開發者工具的更新。採用 Headless 360 部署 AI Agent 的企業，正在改變工作的方式：從人工驅動的順序流程，到 Agent 協調的並行工作流程。合規團隊不再手動審計資料存取日誌，Agent 持續監控；銷售運營團隊不再手動更新區域分配，Agent 在每筆交易關閉後自動重新計算。

## 競爭背景：為什麼現在必須這樣做

Salesforce 的這一步不是孤立的。MCP 已成為軟體功能向 AI Agent 暴露的事實標準，今年 Microsoft、GitHub、Google、Atlassian 和數十家企業軟體公司都已推出 MCP 整合。習慣使用 Claude Code 或 Cursor 的開發者，已能透過 MCP 工具讓 Agent 存取 GitHub 倉庫、Jira 看板、Linear 票單和雲端主機控制台。

Salesforce 的風險在於：如果開發者圍繞 GitHub 和 Linear 建構 Agent 工作流程，但 Salesforce 卻是一個 AI Agent 無法輕易觸及的孤立系統，企業軟體的引力中心就會轉移。Headless 360 是 Salesforce 對這個風險的回應。

還有一個人才維度。現在習慣使用 AI 編程 Agent 的資深工程師，也是未來企業應用的建構者。如果 Salesforce 想成為這些應用選擇的平台，就必須成為 AI Agent 最容易操作的平台。Developer Edition 免費附帶 Claude Sonnet 是達成這個目標的直接策略。

## 開發者現在應該怎麼做？

對 Salesforce 開發者而言，Headless 360 意味著複雜的組織定制方式正在轉變：不再是翻查設定選單或手動撰寫元數據部署，而是逐漸轉向：向連接了 Salesforce MCP 工具的 Claude Code 或 Cursor 工作階段描述需求，讓 Agent 提出實作方案，審核後部署。

對評估 AI Agent 策略的企業架構師而言，Headless 360 改變了 Salesforce 整合的計算方式。如果 Salesforce 是客戶資料和銷售流程的事實標準，而 AI Agent 現在可以透過 MCP 原生操作這些資料，整合層將大幅簡化——Agent 不需要複雜的 Salesforce 連接器函式庫，直接使用人類編程 Agent 同款的 MCP 工具介面即可。

27 年說法是行銷語言，但架構轉型是真實的，而其對企業軟體建構方式——以及運行方式——的影響，才剛剛開始展開。
