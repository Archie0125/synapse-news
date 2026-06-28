---
title: "ARD 規格發布：讓 AI Agent 跨越整個網路相互發現的開放標準"
summary: "Google、Microsoft、GitHub、Nvidia、Salesforce、Snowflake 等共十一家科技巨頭聯合發布「Agentic Resource Discovery（ARD）」規格，這是一套開放標準，讓 AI Agent 無需手動整合，即可在網路任何角落自動發現、驗證並連接工具、API 與其他 Agent。ARD 類比搜尋引擎解決早期網路可發現性問題的方式，可能從根本上改變企業多 Agent 系統的建構邏輯。"
category: "developer-tools"
publishedAt: 2026-06-28
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

如今網路上存在數十萬個 AI 工具、API、MCP Server 與專業化 Agent，能夠執行程式碼分析、法律文件審查、財務建模、供應鏈優化等數千種任務。但今天的 AI Agent 只能使用開發者明確預先接線的資源——手動發現、逐一整合、並在工具 API 演進時持續維護。隨著生態系統的擴張速度超過任何團隊手動跟進的能力，Agent 能力的根本瓶頸已不再是智慧，而是接線。

6 月 17 日發布、由十一家全球頂尖科技公司聯合背書的 Agentic Resource Discovery 規格，試圖以搜尋引擎解決網頁問題的同一種思路來解決這個接線問題：建立一個標準化、可爬取的發現層，讓 Agent 在執行時動態找到所需資源，而不是要求開發者在建構時預先猜測需要什麼。

## 誰在背後支持

這項規格由 **Google**、**Microsoft**、**Cisco**、**Databricks**、**GitHub**、**GoDaddy**、**Hugging Face**、**Nvidia**、**Salesforce**、**ServiceNow** 與 **Snowflake** 共同開發，以 Apache 2.0 授權發布，並建構於 Linux Foundation AI Catalog 工作組的 AI Catalog 資料模型之上。橫跨雲端基礎設施、開發者工具、企業軟體與 AI 平台的廣泛支持，顯示這是作為基礎層設計，而非專有格式。

值得注意的是，擁有最大活躍開發者社群的 OpenAI 與 Anthropic 並未出現在發布聯盟中。規格主要作者——Google 的 Junjie Bu（資深首席軟體工程師）與 Srinivas Krishnan（傑出軟體工程師）——在發布公告中表示，更廣泛的產業參與是目標，且規格設計為任何平台均可採用。

## ARD 究竟如何運作

規格建立在兩個核心基元上。

第一個是**目錄（Catalog）**：組織在其網域的知名路徑發布的機器可讀 `ai-catalog.json` 文件。目錄描述組織提供的 AI 能力——工具、Agent、API、技能——並附上足夠的結構化元數據，讓 AI 系統能理解每項能力的用途、所需輸入、所需權限以及如何調用。網域所有權作為加密身份驗證：若目錄存放於 `stripe.com/ai-catalog.json`，它對 Stripe AI 能力的描述具有權威性，這是第三方對「Stripe 支付 API」的目錄條目所無法比擬的。

第二個是**登錄器（Registry）**：爬取已發布目錄、索引其內容，並回應自然語言發現查詢的搜尋層。登錄器並非單一集中式資料庫——它是關於登錄器如何運作的規格，這意味著多個登錄器可以並存、在品質上競爭，並按領域專業化。組織可以運行私有登錄器，僅索引內部目錄與選定的供應商資源，同時也可以向全球開發者可查詢的公開登錄器公開其公開能力。

ARD 團隊刻意援引 DNS 的類比。DNS 啟用本地控制——任何組織都可以管理自己的網域——同時參與全球命名空間。ARD 將同樣的架構應用於 AI 能力發現：組織控制自己的能力定義，發現基礎設施可以分散式存在，而非依賴單一瓶頸。

## 這對 MCP 意味著什麼

Anthropic 於 2024 年底發布的模型上下文協議（MCP）已成為連接 AI 模型與外部工具的主導標準，ARD 並不取代它——而是與之互補。

MCP 回答的問題是*如何*調用資源：它定義了呼叫工具、傳遞參數、接收結果與管理會話的線路協議。ARD 回答的是不同的問題：從全宇宙可用選項中，*選擇哪個*資源來執行特定任務。

在完整的 Agent 工作流中，ARD 在 MCP 之前運作。Agent 收到任務——「分析這份合約的法律風險」——並查詢 ARD 登錄器，以發現哪些法律分析工具、Agent 或 MCP Server 可用、適合該任務，以及被此 Agent 的操作者授權使用。登錄器返回帶有調用細節的排名匹配結果。Agent 再使用 MCP（或 REST API，或資源指定的任何原生協議）實際呼叫工具。

這種分層設計意味著組織在 MCP 相容工具上已進行的投入不會浪費。ARD 讓這些工具更易於被發現，而非降低其相容性。

## 早期實作

兩個最重要的參考實作與規格本身同步發布。

**GitHub Copilot 的 Agent Finder** 是最引人注目的。它索引 ARD 相容資源——包括 MCP Server、GitHub Copilot Skills 與第三方 Agent——並在執行時讓它們在 Copilot 中可被發現。當開發者要求 Copilot 完成需要外部能力的任務時，Agent Finder 查詢索引目錄，提交匹配結果供開發者審核，並僅將所需資源載入上下文。這解決了當前手動多工具 Copilot 配置中的上下文視窗膨脹問題——開發者過去不論相關與否都要預載數十個 MCP Server。

**Hugging Face 的 Discover Tool** 將 Hub 的語義搜尋——涵蓋數千個 Spaces、ML 應用與 MCP Server——封裝在 ARD 信封中，讓任何 ARD 相容 Agent 均可查詢。鑑於 Hugging Face 作為主導開源模型與工具倉庫的地位，這意味著開源 AI 生態系統中的大量資源立即成為 ARD 可發現的對象。

Google Cloud 在 Gemini 企業 Agent 平台中的 Agent Registry 也支援 ARD，原生支援將「在未來幾個月」在 Agent Platform 中提供。

## 它真正試圖解決的問題

規格的框架具有相當的野心。Microsoft Command Line 部落格上的創始文件將當前 Agent 整合狀態描述為等同於一個「數百萬個頁面存在，但大多數人只瀏覽預設書籤裡的網站」的網路。網路在那裡，卻是黑暗的。

這個框架在一個容易被低估的層面上是準確的。2026 年的企業 AI 部署絕大多數是自定義接線的：一個團隊識別其 Agent 所需的工具，手動整合它們，測試整合，並在工具 API 演進時持續維護。當相關工具空間小而穩定時，這行得通。當一個組織有數十個業務單元，每個都有自己的工具生態系統，或者當 Agent 需要存取它被建構時尚未存在的工具時，這就崩潰了。

目錄加登錄器模型意味著，一個法律科技供應商發布的新工具，會自動對任何查詢索引了該目錄的登錄器的 Agent 可見——無需任何開發者操作，只需供應商發布其 `ai-catalog.json`。整合工作從「每個 Agent 必須了解每個工具」轉移到「每個工具發布一次，任何 Agent 都能找到它」。

## 還需要發生什麼

ARD 是一份有十一家企業支持者與兩個參考實作的草案規格。這是一個有意義的起點——比大多數開發者標準在發布時獲得的支持要多得多——但從「有前景的規格」到「產業實際使用的基礎設施」之間的距離依然漫長。

關鍵變數是工具與平台提供商的採用。如果 Stripe 發布 ARD 目錄，如果 Salesforce 讓其 Agentforce 能力 ARD 可發現，如果企業軟體供應商將 `ai-catalog.json` 視為產品發布的標準環節，ARD 就有可能真正成為 AI 能力發現的 DNS。如果採用停滯在創始聯盟，而無法擴展到工具提供商的更廣泛生態系統，它就會成為眾多「發布當天看起來很有前景，年底前被遺忘」的互通性提案之一。

Apache 2.0 授權與 Linux Foundation 資料模型淵源是積極信號——它們表明建立中立、廣泛可採用基礎設施的意圖，而非對某個供應商平台不成比例有利的標準。OpenAI 與 Anthropic 是否最終加入聯盟，對開發者信任至關重要：一個與 ChatGPT 插件或 Claude 工具無法協作的標準，對其試圖服務的市場而言覆蓋不完整。

對現在建構 Agent 應用的開發者而言，務實建議是追蹤 ARD，但不要等它。規格是真實的，實作已存在，支持是嚴肅的。但那個殺手級應用——Agent 為任何任務從全部可用資源中發現合適工具——仍然超前於今天的基礎設施所處的狀態。

搜尋引擎的類比仍然具有啟發性。Google 並非命中注定。Yahoo 的手動策展目錄早已存在，在其時代運作良好，並在網路規模大到手動策展無法維持時變得過時。ARD 正在押注 AI Agent 生態系統將遵循同樣的模式——手動接線時代是暫時的，執行時可發現的未來是生態系統的走向。這個押注是合理的。ARD 規格是否具體地成為贏家，仍然是一個開放的問題。
