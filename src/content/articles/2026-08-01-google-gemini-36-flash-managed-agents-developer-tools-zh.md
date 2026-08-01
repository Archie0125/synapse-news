---
title: "Google Gemini 3.6 Flash 內建電腦操作能力，成為 Managed Agents 預設模型"
summary: "Google 於 7 月 21 日推出 Gemini 3.6 Flash，每百萬輸入 token 定價 1.5 美元，原生支援電腦操作、100 萬 token 上下文窗口，推論速度達每秒 280 tokens。此模型同步成為 Gemini API Managed Agents 的預設引擎，而 Managed Agents 本身也於 7 月 7 日新增後台執行、遠端 MCP 連線、排程觸發器與免費方案，讓開發者建構自主雲端代理的門檻大幅降低。"
category: "developer-tools"
publishedAt: 2026-08-01
lang: "zh"
featured: false
trending: true
sources:
  - name: "GCN"
    url: "https://gcn.com/google-upgrades-gemini-api-managed-agents/20244/"
  - name: "Google AI Blog"
    url: "https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/"
  - name: "Gemini API Changelog"
    url: "https://ai.google.dev/gemini-api/docs/changelog"
  - name: "BenchLM"
    url: "https://benchlm.ai/models/gemini-3-6-flash"
tags:
  - "Google"
  - "Gemini"
  - "AI 代理"
  - "開發者工具"
  - "MCP"
  - "LLM"
relatedSlugs:
  - "2026-07-31-google-deepmind-gemini-robotics-2-whole-body-zh"
  - "2026-08-01-deepseek-v4-flash-0731-agent-benchmarks-zh"
---

兩次相差兩週的 Google 發布，合在一起為 Gemini API 的開發生態帶來了一次實質性的升級。7 月 7 日，Managed Agents——Google 為自主代理提供的雲端沙箱執行環境——新增了後台執行、遠端 MCP 連線和排程觸發器；7 月 21 日，Gemini 3.6 Flash 上線並成為這些代理的預設模型，帶來了電腦操作能力、多模態輸入，以及更具競爭力的定價。兩者合在一起，構成了一個對開發者清晰的訊號：以更低的成本，跑更強、更自主的代理。

## Gemini 3.6 Flash：哪些地方變了

Gemini 3.6 Flash 在 Google 現有模型陣容中，位居旗艦 Gemini 3.5 Pro 和高度優化的 3.5 Flash-Lite 之間。核心規格如下：

**定價**：輸入每百萬 token 1.5 美元，輸出 7.5 美元。這個價格與其他中端前沿模型相比具有競爭力，但仍高於 DeepSeek 或 OpenAI 近期大幅降價後的部分選項。

**速度**：每秒約 280 tokens，適合需要即時回應的場景，例如串流語音介面或互動式程式碼生成。

**效率**：Google 表示，3.6 Flash 在同等任務上比前代模型少用約 17% 的輸出 token，對按量計費的工作流程而言是實際的成本節省。

**上下文與輸出限制**：100 萬 token 上下文窗口，足以容納完整的程式碼倉庫、長文件或代理的長期對話記錄。每次請求的最大輸出上限為 64,000 tokens。

**輸入模態**：原生支援文字、圖片、影片、音訊和 PDF，讓它能無縫融入企業中混合文件類型的工作流程。

**電腦操作（Computer Use）**：這或許是最值得注意的新能力。代理現在可以感知圖形介面、點擊元素、填寫表單、操作應用程式——這個能力已成為 Gemini API 的內建工具，同時也整合進 Gemini Enterprise。此前，電腦操作能力需要外部工具，或僅能在 Gemini Enterprise Agent Platform 中使用。

## Managed Agents：基礎設施全面升級

7 月 7 日的 Managed Agents 更新，正面解決了過去讓平台在生產環境應用上受限的幾個痛點。

**後台執行。** 代理現在可以非同步執行長時間任務，無需客戶端保持開放連線。開發者觸發代理後收到一個任務 ID，之後可以輪詢結果，或設定 Webhook 在任務完成後接收通知。這讓五分鐘的程式碼審查任務和四小時的倉庫掃描任務，都可以納入同一套代理基礎設施。

**遠端 MCP 連線。** 代理現在可以連接外部的 Model Context Protocol 伺服器，使用由第三方服務定義的工具，而這些工具的程式碼不需要在 Google 沙箱內部跑。開發者可以把代理接到自家的程式碼搜尋伺服器、客戶資料庫的 MCP 端點，或任何支援 MCP 的內部工具棧。

**排程觸發器。** Google 新增了把代理、提示詞和環境綁定到 cron 表達式的功能，建立持久性的排程資源。代理可以設定為每晚分析系統日誌、每週生成競品情報報告，或按任何自訂時間間隔運行。若連續五次執行失敗，排程會自動暫停——防止損壞的自動化靜默消耗費用。

**預算控制。** 開發者現在可以為每次代理執行設定硬性 token 預算，避免因循環執行或對抗性輸入導致意外高額費用。

**免費方案。** Managed Agents 現已對 API key 專案開放，不再需要 Gemini Enterprise 訂閱。這讓個人開發者和小型團隊也能使用沙箱執行環境，大幅降低了嘗試代理能力的門檻。

## Antigravity：開箱即用的起始代理

Google 為 Managed Agents 平台提供了一個參考代理，稱為 **Antigravity**。這是一個通用代理，能夠在隔離的 Linux 沙箱容器中自主推理、規劃、撰寫並執行程式碼、管理檔案、瀏覽網頁——而且不需要任何自訂的編排程式碼。開發者透過 Google AI Studio 或 API 發送提示詞，Antigravity 自行決定工具選取和執行序列。

這大幅降低了驗證代理方案的準入成本。開發者想知道代理化方式能否處理自家的使用場景，可以先對著 Antigravity 快速原型驗證，再決定是否投入自訂編排。Ramp、Klipy、Stitch 等公司已在早期測試中，將 Managed Agents 用於財務運營、銷售情報和設計自動化等工作流程。

自訂代理透過 AGENTS.md 和 SKILL.md 兩個 Markdown 設定檔定義行為，再透過 API 註冊。Google 的這套設計讓代理定義可以納入版本控制、進行 code review，並透過標準軟體開發流程部署。

## 競爭格局

這兩次發布的時機，正好卡在一場加速演進的平台競爭中間。OpenAI 的 Presence 企業代理治理平台於 7 月 22 日上線——Gemini 3.6 Flash 上線後的隔天。Anthropic 的企業操作員工具套件今年初已可使用。Microsoft 持續在 Azure AI 與 GitHub Copilot 中強化 Agent Mode。

Google 的差異化在於沙箱隔離的深度，以及與 Google Cloud 整合生態的廣度。MCP 相容性拓寬了工具池。免費方案讓更廣泛的開發者群體能夠嘗試，而非只有企業客戶。

相較於 OpenAI Presence，Managed Agents 目前仍缺乏完善的治理與企業政策層：它本質上是一個執行平台，而非審計與合規平台。需要有文件記錄的人工監督和變更管理的企業採購者，仍需自行建構這一層，或選用針對此需求設計的平台。

對於獨立開發者和新創公司而言，Gemini 3.6 Flash 的多模態能力、後台執行基礎設施、遠端 MCP 整合和免費方案，合在一起代表的是一個比 90 天前好了不止一個檔次的代理建構平台。

## 開發者應優先測試什麼

目前最值得探索的，是電腦操作與後台執行的交叉應用：代理需要操作圖形介面來萃取或輸入資訊，且整個任務需要跑幾分鐘甚至幾小時而不保持即時連線。排程程式碼審查流水線、競品情報爬取，以及文件處理自動化，是最適合當前能力棧的使用場景。

另需注意：Gemini API 更新日誌顯示，gemini-robotics-er-1.6-preview 模型將於 2026 年 8 月 31 日關閉，多個圖像生成模型將於 8 月 17 日下線。依賴這些模型識別碼的開發者，請在截止日期前完成遷移。
