---
title: "Mastra 完成2200萬美元A輪融資，搶當 TypeScript AI 代理人框架的標準答案"
summary: "開源 TypeScript AI 代理人框架 Mastra 宣布完成由 Spark Capital 領投的2200萬美元A輪融資，總融資額達3500萬美元。憑藉逾22,000個 GitHub Star、每週30萬次 npm 下載量，以及 Brex、Sanity、Factorial 等企業的生產環境採用，Mastra 正朝著「AI 代理人的 Rails」目標大步前進。"
category: "developer-tools"
publishedAt: 2026-04-10
lang: "zh"
featured: false
trending: true
sources:
  - name: "Mastra Blog"
    url: "https://mastra.ai/blog/series-a"
  - name: "DEV Community"
    url: "https://dev.to/gabrielanhaia/mastra-in-2026-what-it-is-when-to-use-it-and-how-it-compares-2go1"
  - name: "Generative Inc."
    url: "https://www.generative.inc/mastra-ai-the-complete-guide-to-the-typescript-agent-framework-2026"
tags:
  - "Mastra"
  - "TypeScript"
  - "AI代理人"
  - "開源"
  - "開發者工具"
  - "A輪融資"
  - "Spark Capital"
  - "RAG"
relatedSlugs:
  - "2026-04-04-cursor-devin-war-zh"
  - "2026-04-04-solo-founder-ai-stack-zh"
  - "2026-04-06-agentic-ai-foundation-zh"
---

成為 AI 代理人開發預設框架的競賽，剛剛變得更加激烈。開源 TypeScript AI 代理人框架 Mastra，在4月9日宣布完成由 Spark Capital 領投的2200萬美元A輪融資，繼2025年底的1300萬美元種子輪之後，總融資額達到3500萬美元。

這個里程碑的重要性，不僅在於 Mastra 本身的發展軌跡，更在於它說明了企業 AI 開發正在走向何方：遠離以 Python 為核心的機器學習工作流程，轉向已驅動大多數 Web 和全端應用的 TypeScript 生態系。

## Mastra 正在解決什麼問題

在生產環境中構建 AI 代理人，遠不是把幾個 LLM 呼叫串起來那麼簡單。開發者需要能在故障中存活的持久性工作流程執行機制、可查詢知識庫的 RAG 流程、跨工作階段維護上下文的記憶系統、用來除錯代理人行為的可觀測性工具，以及將代理人連結到外部工具和 API 的整合層。

現有大多數框架只處理其中一兩項需求。Mastra 的賭注是：TypeScript 開發者想要一個單一的、可組合的框架，能夠一次處理所有問題，而不需要引入 Python 互通層，或被迫將六、七個不同函式庫拼湊在一起。

Mastra 的創辦人在開發者社群中說過：「我們想打造的是 Web 開發中 Rails 的角色」——一個「慣例優於配置」的框架，替開發者做好困難的預設決策，讓他們能專注在應用邏輯，而非基礎管線。

## 數字說明一切

Mastra 的採用曲線陡得出奇。框架於2024年10月推出，2025年2月登上 Hacker News 首頁，一週內 GitHub Star 從1,500暴增至7,500。到2026年1月，1.0版本正式發布時，專案已累積逾22,000個 GitHub Star，每週 npm 下載量超過30萬次。

對照一下：30萬次週下載量，與 React 生態系中中等規模的函式庫處於同一數量級——這個等級通常代表的是生產環境使用，而非只是開發者的嘗鮮。隨著依賴 Mastra 的新專案不斷增加，這個數字還會持續複利成長。

已知在生產環境採用的企業包括 Brex（金融服務）、Sanity（內容管理基礎設施）和 Factorial（人力資源平台）。這三家都是有真實生產流量的成長期公司，這意味著 Mastra 的抽象設計已在非平凡的負載與複雜度下獲得驗證。

## 框架實際提供什麼

Mastra 圍繞三個核心原語構建：

**Agents（代理人）** — Claude、GPT-4o、Gemini 或任何相容模型都能成為代理人，感知輸入、使用工具、產生輸出。Mastra 處理代理人迴圈、工具派發和錯誤恢復，並內建支援結構化輸出和多步驟推理。

**Workflows（工作流程）** — 用於多步驟代理人任務的持久性圖形化執行引擎。工作流程可設置檢查點、條件分支、平行執行步驟，並在故障後從中斷處恢復而不遺失狀態——對任何耗時超過幾秒、需要在基礎設施中斷中存活的任務至關重要。

**RAG 流程** — Mastra 提供內建的文件切塊、嵌入生成、向量資料庫儲存和查詢時上下文檢索抽象。框架對向量資料庫無偏好，支援 Pinecone、Weaviate、附帶 pgvector 的 Postgres 等。

記憶體、日誌和遙測是框架中的一等公民，並整合了 OpenTelemetry，可對生產系統中的代理人工作流程進行分散式追蹤。

## TypeScript 為何至關重要

選擇 TypeScript 作為主要語言並非偶然。幾乎所有現代 Web 應用——以及大多數 SaaS 產品——都是用 JavaScript 或 TypeScript 構建的。當這些產品需要加入 AI 功能時，工程團隊希望用和其他程式碼相同的語言來撰寫，而不是切換到 Python。

LangChain、LlamaIndex 和 LangGraph 等 Python 框架成熟且部署廣泛，但它們需要獨立的執行環境、獨立的套件管理，以及與 TypeScript 服務不同的部署模型。對後端是 Node.js 的公司而言，採用基於 Python 的 AI 代理人框架，意味著要麼引入第二種語言，要麼架設 RPC 橋接層——兩者都增加複雜度和運維成本。

Mastra 完全繞過了這個問題。它在任何 Node.js 或 Bun 執行環境中運行，透過標準的 npm install 整合現有 TypeScript 專案，並與 Prisma（資料庫）、tRPC（API）和 Next.js（前端）等常見生態系工具無縫配合。

## Spark Capital 與融資背景

Spark Capital 在本輪擔任領投方意義重大。這家投資機構曾早期投資 Twitter、Slack 和 Coinbase，近年在開發者基礎設施領域也頗為活躍，包括 Vercel 和 Linear。對 Mastra 的押注符合他們一貫的投資邏輯：在基礎層降低摩擦的開發者工具，比應用層產品的採用速度複利得更快。

這2200萬美元主要將用於擴充工程師團隊，加速產品路線圖——根據 Mastra 公開的資訊，包括強化多代理人協調、更緊密的 IDE 整合（特別是 VS Code 和 Cursor）、改善代理人行為測試的評估框架，以及生產環境代理人代管的雲端基礎設施。

最後一項值得關注。隨著 Anthropic 和其他模型供應商相繼推出代管代理人平台，Mastra 將面臨選擇：繼續只做框架層，還是延伸進入代管服務以捕獲更多價值鏈。3500萬美元的總融資，給了他們探索兩條路的空間。

## 更宏觀的視角

Mastra 的A輪融資，折射出企業對 AI 開發思路的成熟。第一波 AI 整合是探索性的——PoC 和聊天機器人。現在這波是關於自主工作流程的生產部署，開發者越來越需要把可靠性、可觀測性和多模型彈性當作一等關注點的框架，而不是事後補丁。

對 TypeScript 生態系而言，Mastra 的勢頭說明企業 AI 開發不再是 Python 的禁臠。「AI 團隊」和「產品團隊」之間的語言屏障正在縮小——對於想在不另組 AI 基礎建設專屬團隊的情況下推出 AI 原生功能的新創公司而言，這正是他們需要的。

Mastra 是開源的，這在策略上同樣重要。在一個開發者對供應商鎖定天然保持戒心的領域，開源建立了信任；同時也創造了社群驅動的回饋迴路，讓框架品質的提升速度超越任何閉源競品所能比擬的。
