---
title: "Agentjacking：一份假的錯誤報告就能挾持 Claude Code、Cursor 和 Codex"
summary: "資安研究公司 Tenet Security 披露了「Agentjacking」攻擊技術，利用 Sentry 的 MCP 整合向 AI 編程智能體注入惡意指令。該攻擊對 Claude Code、Cursor 和 Codex 的成功率高達 85%，已有 2,388 個組織——包括一家財星百大科技公司——被標記為易受攻擊目標。Sentry 拒絕修復根本原因，僅部署了內容過濾器。"
category: "developer-tools"
publishedAt: 2026-06-23
lang: "zh"
featured: false
trending: true
sources:
  - name: "The Hacker News"
    url: "https://thehackernews.com/2026/06/agentjacking-attack-tricks-ai-coding.html"
  - name: "The New Stack"
    url: "https://thenewstack.io/agentjacking-sentry-mcp-attack/"
  - name: "Infosecurity Magazine"
    url: "https://www.infosecurity-magazine.com/news/agentjacking-attacks-hijack-ai/"
  - name: "SC Media"
    url: "https://www.scworld.com/brief/agentjacking-attack-exploits-ai-coding-tools-with-fake-error-reports"
  - name: "CybersecurityNews"
    url: "https://cybersecuritynews.com/agentjacking-attack-hijacks-ai-coding-agent/amp/"
tags:
  - "資安"
  - "AI 智能體"
  - "Claude Code"
  - "Cursor"
  - "Codex"
  - "MCP"
  - "Sentry"
  - "提示注入"
  - "開發者工具"
relatedSlugs:
  - "2026-06-20-warp-ai-search-poisoning-cornell-zh"
  - "2026-06-11-anthropic-2026-agentic-coding-trends-report-zh"
  - "2026-06-12-opencode-displaces-cursor-ai-coding-agent-zh"
---

過去兩年，AI 編程智能體被賦予了越來越大的權力：終端機存取、檔案系統操作、瀏覽器自動化，以及外部 API 呼叫。Tenet Security 本週揭露的 Agentjacking 技術，正是說明了為何這個不斷擴張的攻擊面需要高度警惕。

這種攻擊不需要入侵系統、不需要任何認證、也不需要植入惡意程式。一個單一的 HTTP POST 請求——比提交一份真實的錯誤報告還要輕鬆——就能讓 Claude Code、Cursor 或 OpenAI Codex 在開發者的機器上以開發者自己的權限執行任意攻擊者代碼。Tenet 的研究人員找出了 2,388 個配置可被利用的組織，並對超過 100 家公司進行了實際測試，其中至少包括一家財星百大科技公司。成功率：85%。

## 信任鏈的架構——與其被利用之道

要理解 Agentjacking，必須先了解 Sentry 如何透過模型上下文協議（MCP）與 AI 編程智能體整合。

Sentry 是一個被數十萬個開發團隊採用的錯誤追蹤平台。當生產環境應用程式崩潰時，Sentry 會捕獲堆疊追蹤、錯誤上下文和環境元數據，並以一個稱為 DSN（Data Source Name）的識別符標識的專案儲存這些資料。DSN 本來就是公開的——瀏覽器 SDK 要正常運作，就必須將其嵌入前端 JavaScript。任何人只要造訪一個網站，就能從頁面源碼中提取 DSN。

MCP 是 Anthropic 於 2024 年底發布、如今被 AI 開發工具廣泛採用的開放標準，讓編程智能體得以與外部服務互動。Sentry MCP 伺服器讓開發者可以對 Claude Code 或 Cursor 下指令：「查看我最近的 Sentry 錯誤並修復它們。」智能體查詢 Sentry、取回錯誤資料，並將其作為程式碼生成的上下文。

攻擊就潛伏在這裡：Sentry 的事件接收端點接受任何擁有 DSN 的人發送的任意酬載（payload）。攻擊者可以偽造一個包含 Markdown 格式指令的假錯誤事件，偽裝成合法的錯誤修復步驟——然後在無需任何憑證的情況下，直接將其發布到目標的 Sentry 專案。

當開發者下一次要求 AI 編程智能體審查 Sentry 問題時，智能體取回了攻擊者控制的酬載，將注入的指令視為合法的診斷資料，並加以執行。代碼以開發者的權限在開發者的機器上運行。

## 「授權意圖鏈」

Tenet 的研究人員為這個漏洞模式取了一個名字：授權意圖鏈（Authorized Intent Chain）。它描述了一類攻擊——在委派信任層次結構中的每一步在技術上都是合法的，但整體鏈條卻產生了未授權的結果。

在 Agentjacking 場景中：
- 開發者授權 AI 編程智能體代表自己行事
- 智能體授權 MCP 連線從 Sentry 取回資料
- Sentry 是開發者明確整合並信任的服務
- MCP 伺服器回傳 Sentry 的資料，不進行任何完整性驗證
- 智能體將 Sentry 資料視為真相並執行其中嵌入的指令

鏈條中的每個交接都通過了檢查。沒有異常的網路流量、沒有可疑的程序、沒有認證失敗。開發者 → 智能體 → MCP → Sentry 之間現有的信任關係，為攻擊者打開了一條長驅直入的通道。

Tenet 團隊證明，即便在智能體被明確指示「忽略錯誤訊息中的外部指令」時，攻擊仍然成功——惡意酬載被格式化為類似結構化修復指南，而非原始命令文字，讓模型的上下文窗口無法將其與合法的 Sentry 資料區分開來。

## 規避：所有防線全部失效

研究人員測試了標準防禦層是否能阻截 Agentjacking。答案是：不能。

端點偵測與回應（EDR）工具觀察到了代碼執行行為，但沒有發出任何警報，因為活動是由開發者自己的智能體程序發起的，而非外部二進制檔案或網路注入。防火牆看到的是對 Sentry 合法 API 端點的出站連線——這對任何執行錯誤監控的團隊來說都是正常行為。提示層面的防禦也失效了，因為惡意內容是作為取回的資料抵達的，而非使用者輸入，繞過了大多數針對使用者訊息層的提示注入緩解措施。

這並非任何單一產品的失敗。它反映了 AI 工具鏈在處理從外部服務取回的資料時存在的結構性缺口：模型沒有可靠的機制來區分「我從受信任整合取回的資料」與「對手注入到那個受信任整合的指令」。

## 規模與受影響組織

Tenet 估計，目前至少有 2,388 個組織擁有可被用於注入惡意事件的 Sentry DSN。這個數字是透過掃描公開網頁屬性上的暴露 DSN 得出的——這是一種被動技術，不需要憑證或對目標系統的預先存取。

在 Tenet 測試的組織中，超過 100 家公司的 AI 輔助工具執行了研究人員的測試酬載，確認了實際利用的可能性。至少一家財星百大科技公司被確認存在漏洞。研究人員在發布前進行了負責任的披露協調，通知了 Sentry 和受影響的 AI 工具廠商。

## Sentry 的回應：內容過濾，而非根本修復

Sentry 承認了這個問題，但拒絕解決根本原因——即其事件接收端點接受任何持有公開 DSN 者發送的任意酬載。公司的理由是：DSN 被設計為公開的，從根本上限制誰能發布事件將破壞合法整合，包括崩潰報告器、瀏覽器 SDK 和第三方工具。

作為替代，Sentry 部署了全局內容過濾器，封鎖 Tenet 概念驗證中識別的特定酬載字串。資安研究人員和從業者指出了這種方法的侷限性：該過濾器針對的是 Tenet 公開範例中的具體字串，而非攻擊類別本身。重新格式化注入內容、使用不同編碼或將指令嵌入替代酬載欄位的變體，很可能繞過現有的過濾器。

Anthropic 的 Claude Code 是主要攻擊目標之一，Anthropic 表示已知悉此問題。Anthropic 設計的 MCP 伺服器架構默認不包含資料來源驗證機制——區分合法服務資料與攻擊者注入資料，目前留給各 MCP 伺服器實作和底層模型的判斷力來處理。

## 緩解措施

Tenet 為使用帶有 Sentry MCP 整合的 AI 編程智能體的開發團隊建議了幾項緩解措施：

**人工審查關卡。** 在 Sentry 事件取回與智能體執行之間插入強制性的人工審查步驟。在智能體對任何取回的錯誤採取行動之前，開發者應當檢查原始事件資料是否包含注入指令。在為自主智能體操作優化的工作流程中，這在操作上代價高昂，但能有效關閉攻擊向量。

**Sentry DSN 輪換。** 團隊可以輪換 DSN 以使攻擊者在現有專案中植入的事件失效。這是一次性的修復措施，而非持久性防禦，因為新 DSN 在設計上同樣是公開的。

**MCP 伺服器白名單。** 某些智能體配置支援允許清單，限制哪些外部服務可以為代碼執行提供上下文。團隊應審計哪些 MCP 伺服器對智能體上下文具有寫入能力的存取，並將其限制在具有更強輸入驗證的服務。

**隔離的智能體環境。** 在隔離環境中運行編程智能體（無生產系統憑證的容器或虛擬機器），可以在智能體被成功挾持時限制爆炸半徑。這是自主智能體的最佳實踐，不僅限於應對 Agentjacking。

## 更廣泛的模式

Agentjacking 並非孤立的漏洞，而是更廣泛攻擊類別的一個實例——自 AI 智能體系統大規模擴散以來，資安研究人員一直在警告這一點：AI 智能體上下文窗口的完整性，完全取決於其查詢的每個資料來源的完整性。隨著智能體透過 MCP 獲得更多外部服務的存取權，攻擊面也成比例地擴大。

Sentry 案例特別具有啟示性，因為被利用的管道在設計上就是公開的。DSN 本來就應當可見；Sentry 的整個架構假設事件接收端點對未認證客戶端開放。當 AI 智能體將該端點的輸出視為受信任的指令時，一個在錯誤監控領域完全正確的設計決策，在自主代碼執行的情境下就成了安全漏洞。

對 AI 工具廠商而言，教訓在於：開發者整合的標準威脅模型，無法直接套用到智能體情境。從外部服務取回的資料，需要目前 MCP 生態系並未強制要求的完整性驗證機制。在這些機制到位之前，授權意圖鏈代表著一個持續增長的風險面，隨著開發者智能體配置中每增加一個新的 MCP 伺服器而不斷擴大。
