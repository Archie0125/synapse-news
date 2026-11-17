---
title: "ARD 規格發布：讓 AI Agent 跨越整個網路相互發現的開放標準"
summary: "Google、Microsoft、GitHub、Nvidia、Salesforce、Snowflake 與另外五家科技公司聯合發布「Agentic Resource Discovery（ARD）」規格，這是一套開放標準，讓 AI Agent 無需手動接線，即可跨越網路發現、驗證並連接工具、技能與其他 Agent。ARD 類比搜尋引擎解決早期網路可發現性問題的方式。"
category: "developer-tools"
publishedAt: 2026-06-28
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "Google Developers Blog"
    url: "https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/"
  - name: "Microsoft Command Line"
    url: "https://commandline.microsoft.com/agentic-resource-discovery-specification-ard/"
  - name: "Hugging Face Blog"
    url: "https://huggingface.co/blog/agentic-resource-discovery-launch"
  - name: "Search Engine Journal"
    url: "https://www.searchenginejournal.com/google-microsoft-back-draft-ai-agent-discovery-spec/579894/"
tags:
  - "ARD"
  - "AI Agent"
  - "開放標準"
  - "Google"
  - "Microsoft"
  - "互通性"
  - "MCP"
  - "開發者工具"
relatedSlugs:
  - "2026-06-27-arcade-60m-ai-agent-security-mcp-zh"
  - "2026-06-23-agentjacking-sentry-mcp-ai-coding-attack-zh"
  - "2026-06-11-visa-openai-ai-agents-payments-zh"
---

早期網路曾面臨一個事後看來顯而易見的問題：數百萬個頁面存在，但大多數人只瀏覽預設書籤裡的那幾個網站。內容在那裡，但沒有人能找到它。搜尋引擎並沒有創造網路——它是透過解決可發現性問題，讓已經存在的網路真正變得有用。

2026 年的 AI Agent 生態系統正面臨同樣的問題。

如今網路上存在數十萬個 AI 工具、API、MCP Server 與專業化 Agent。但今天的 AI Agent 只能使用開發者明確預先接線的資源——手動發現、逐一整合、並在工具 API 演進時持續維護。隨著生態系統的擴張速度超過任何團隊手動跟進的能力，Agent 能力的根本瓶頸已不再是智慧，而是接線。

6 月 17 日以草案形式發布、由十一家公司聯合背書的 Agentic Resource Discovery 規格，試圖以搜尋引擎解決網頁問題的同一種思路來解決這個接線問題：建立一個標準化的發現層，讓 Agent 在執行時找到所需資源，而不是要求開發者事先接線。

## 誰在背後支持

這項規格由 **Google**、**Microsoft**、**Cisco**、**Databricks**、**GitHub**、**GoDaddy**、**Hugging Face**、**Nvidia**、**Salesforce**、**ServiceNow** 與 **Snowflake** 共同開發，以 Apache 2.0 授權發布，並建構於 Linux Foundation AI Catalog 工作組的 AI Catalog 資料模型之上。橫跨雲端基礎設施、開發者工具、企業軟體與 AI 平台的廣泛支持，顯示這是作為基礎層設計，而非專有格式。

## ARD 究竟如何運作

規格建立在兩個核心基元上。

第一個是**目錄（Catalog）**：組織在其網域的知名路徑發布的機器可讀 `ai-catalog.json` 文件。目錄描述組織提供的 AI 能力——工具、Agent、API、技能——並附上足夠的結構化元數據，讓 AI 系統能理解每項能力的用途、所需輸入、所需權限以及如何調用。網域所有權用來驗證目錄的發布者：由於每份目錄都放在發布者自己的網域上，存放於該處的目錄就是發布者自己的清單。

第二個是**登錄器（Registry）**：爬取已發布目錄、索引其內容，並回應自然語言發現查詢的搜尋層。登錄器並非單一集中式資料庫——它是關於登錄器如何運作的規格，這意味著多個登錄器可以並存、在品質上競爭，並按領域專業化。組織可以運行私有登錄器，僅索引內部目錄與選定的供應商資源，同時也可以向全球開發者可查詢的公開登錄器公開其公開能力。

ARD 團隊刻意援引 DNS 的類比。DNS 啟用本地控制——任何組織都可以管理自己的網域——同時參與全球命名空間。ARD 將同樣的架構應用於 AI 能力發現：組織控制自己的能力定義，發現基礎設施可以分散式存在，而非依賴單一瓶頸。

## 這對 MCP 意味著什麼

模型上下文協議（MCP）讓 Agent 有標準方式呼叫工具，ARD 並不取代它——而是與之互補。

MCP 回答的問題是*如何*調用資源：它讓 Agent 有標準方式呼叫工具。ARD 回答的是不同的問題：該調用*哪個*資源。

在完整的 Agent 工作流中，ARD 在 MCP 之前運作。Agent 收到任務後，以自然語言查詢 ARD 登錄器，以發現哪些工具、Agent 或 MCP Server 與之相符。登錄器返回帶有調用細節的排名匹配結果。Agent 再使用 MCP（或 REST API，或資源指定的任何原生協議）實際呼叫工具。

這種分層設計意味著組織在 MCP 相容工具上已進行的投入不會浪費。ARD 讓這些工具更易於被發現，而非降低其相容性。

## 早期實作

數個參考實作與規格本身同步發布。

**GitHub Copilot 的 Agent Finder** 是最引人注目的。它讓 Copilot 在執行時動態發現並呼叫合適的 MCP Server、技能、工具與 Agent，可搜尋 GitHub 精選的公開 AI 資源目錄，或開發者自己的私有登錄器。Copilot 不會預先載入所有資源，而是找出提示所需的資源，並在需要時注入上下文視窗。這避免了不需要的資源讓上下文視窗膨脹。

**Hugging Face 的 Discover Tool** 將 Hub 的語義搜尋——涵蓋數千個 Spaces、ML 應用與 MCP Server——封裝在 ARD 信封中，讓任何 ARD 相容 Agent 均可查詢。

Google Cloud 在 Gemini 企業 Agent 平台中的 Agent Registry 是 Google 的貢獻，Agent Platform 計畫「在未來幾個月」提供原生 ARD 支援。

## 它真正試圖解決的問題

規格的框架具有相當的野心。Microsoft Command Line 部落格上的創始文件將當前 Agent 整合狀態描述為等同於一個「數百萬個頁面存在，但大多數人只瀏覽預設書籤裡的網站」的網路。網路在那裡，卻是黑暗的。

這個框架在一個容易被低估的層面上是準確的。如今，開發者或 IT 管理員必須手動尋找 Agent 或工具、判斷其是否可信、將其連接到 AI 用戶端，並持續維護這些接線。當相關工具空間小而穩定時，這行得通。當每家公司、產品團隊與開發者都能發布自己的工具時，這就行不通了。

目錄加登錄器模型意味著，一個法律科技供應商發布的新工具，會自動對任何查詢索引了該目錄的登錄器的 Agent 可見——無需任何開發者操作，只需供應商發布其 `ai-catalog.json`。整合工作從「每個 Agent 必須了解每個工具」轉移到「每個工具發布一次，任何 Agent 都能找到它」。

## 還需要發生什麼

ARD 是一份有十一家貢獻企業與數個參考實作的草案規格。這是一個有意義的起點——比大多數開發者標準在發布時獲得的支持要多得多——但從「有前景的規格」到「產業實際使用的基礎設施」之間的距離依然漫長。

關鍵變數是工具與平台提供商的採用。如果 Stripe 發布 ARD 目錄，如果 Salesforce 讓其 Agentforce 能力 ARD 可發現，如果企業軟體供應商將 `ai-catalog.json` 視為產品發布的標準環節，ARD 就有可能真正成為 AI 能力發現的 DNS。如果採用停滯在創始聯盟，而無法擴展到工具提供商的更廣泛生態系統，它就會成為眾多「發布當天看起來很有前景，年底前被遺忘」的互通性提案之一。

Apache 2.0 授權與 Linux Foundation 資料模型淵源是積極信號——它們表明建立中立、廣泛可採用基礎設施的意圖，而非對某個供應商平台不成比例有利的標準。

對現在建構 Agent 應用的開發者而言，務實建議是追蹤 ARD，但不要等它。規格是真實的，實作已存在，支持是嚴肅的。但那個殺手級應用——Agent 為任何任務從全部可用資源中發現合適工具——仍然超前於今天的基礎設施所處的狀態。

搜尋引擎的類比仍然具有啟發性。Google 並非命中注定。Yahoo 的手動策展目錄早已存在，在其時代運作良好，並在網路規模大到手動策展無法維持時變得過時。ARD 正在押注 AI Agent 生態系統將遵循同樣的模式——手動接線時代是暫時的，執行時可發現的未來是生態系統的走向。這個押注是合理的。ARD 規格是否具體地成為贏家，仍然是一個開放的問題。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 20 處。*
