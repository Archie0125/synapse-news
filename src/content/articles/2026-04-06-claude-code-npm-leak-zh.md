---
title: "Anthropic 意外將 51.2 萬行 Claude Code 原始碼上傳至 npm"
summary: "Claude Code v2.1.88 的建置錯誤導致包含 1,906 個 TypeScript 檔案、共 51.2 萬行的原始碼被公開上傳至 npm 套件庫，內容涵蓋 Claude 使用工具、管理檔案、協調多 Agent 工作流程的完整代碼邏輯。在 Anthropic 下架套件前，相關程式碼已在 GitHub 上累積超過 5 萬顆星。"
category: "developer-tools"
publishedAt: 2026-04-06T09:15:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "The Register"
    url: "https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know"
  - name: "Gizmodo"
    url: "https://gizmodo.com/source-code-for-anthropics-claude-code-leaks-at-the-exact-wrong-time-2000740379"
  - name: "The Hacker News"
    url: "https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html"
tags:
  - "Anthropic"
  - "Claude Code"
  - "開源"
  - "npm"
  - "原始碼洩漏"
  - "開發者工具"
  - "資安"
relatedSlugs:
  - "2026-04-06-anthropic-claude-mythos-zh"
  - "2026-04-04-mcp-protocol-explosion-zh"
  - "2026-04-06-claude-code-npm-leak-en"
---

## 51.2 萬行程式碼如何逃出去的

2026 年 3 月 31 日，Anthropic 向公開 npm 套件庫發布了 Claude Code v2.1.88。套件裡除了正常的打包程式碼，還附帶了一個不該存在的東西：一份 59.8 MB 的 source map 檔案，包含 1,906 個 TypeScript 原始檔與 51.2 萬行可讀程式碼——這是 Claude Code Agent 核心邏輯的完整原始碼。

根本原因源於一次工具鏈遷移。Anthropic 在 2024 年底收購 Bun 公司後，將 Claude Code 的打包工具切換為 Bun。Bun 存在一個已知的 bug：即使明確設置了 `development: false` 旗標，它仍會產生 source map。在正式發布的套件中，source map 應該被省略——它的用途是幫助開發者偵錯壓縮後的程式碼，不應出現在已發布的套件裡。旗標設定正確，但打包工具忽略了它。

套件帶著 source map 上線了。Anthropic 內部沒有任何人察覺。

## 一個實習生發現，1,600 萬人看到了

發現這個問題的，是 Solayer Labs 的軟體工程實習生 Chaofan Shou。他在進行一項例行整合任務時瀏覽了已發布的 npm 套件，發現了那份 source map，意識到其中的問題，隨即在 X 上發文。這則推文在 24 小時內獲得了 1,600 萬次瀏覽。

在 GitHub 上，一個從洩漏原始碼分叉出的儲存庫在不到兩小時內獲得了 5 萬顆星和 4.15 萬個分叉——成為該平台歷史上傳播速度最快的程式碼庫之一。Anthropic 在協調世界時間約 08:00 下架了相關 npm 套件，但此時程式碼已被下載、鏡像並在數十個平台上存檔。

Anthropic 確認了這起事件，並將原因歸咎於 Bun 工具鏈的 bug。他們此後已修補建置流程，無論打包工具的行為如何，都會強制移除 source map。

## 為何這比模型權重洩漏更敏感

聽到「AI 原始碼洩漏」時，直覺反應往往是聯想到模型權重——那些數十億個編碼了模型知識與推理能力的參數。Claude 的模型權重並未被洩漏。洩漏的是某種在不同層面上同樣具有戰略敏感性的東西：**Agent 核心邏輯（agentic harness）**。

Claude Code 的原始碼決定了 Claude 如何與真實世界互動：如何讀寫檔案、執行 bash 指令、呼叫外部 API、在長時間執行的 Agent 任務中管理對話上下文、在多 Agent 工作流程中協調子 Agent，以及在工具失敗時如何恢復。這是操作層——是語言模型「產生文字」與 Agent「採取行動」之間的差距所在。

理解這套核心邏輯，讓競爭對手能詳細了解 Anthropic 的架構決策：他們如何處理工具使用授權、在檔案寫入或 Shell 指令執行前進行哪些安全檢查、如何建構 Agent 的記憶體與狀態管理，以及 Claude 模型層與編排層之間的邊界在哪裡。這些決策耗費了多年工程積累，且從未出現在任何公開研究論文中。

資安研究者也指出一個更直接的顧慮：原始碼揭露了 Claude Code 工具呼叫授權邏輯的精確結構，這理論上可能為精心設計的提示詞或工具回應提供繞過安全限制的線索。Anthropic 表示目前沒有發現洩漏程式碼遭到惡意利用的證據，但承認「有效的負責任揭露期為零」。

## 時機再糟糕不過

Anthropic 正處於一個敏感時期。就在幾天前，公司剛因 CMS 設定錯誤意外確認了下一代模型「Claude Mythos」的存在——目前正悄悄向資安領域的企業客戶試點部署。兩週內接連發生兩起意外洩漏，讓外界開始質疑 Anthropic 的內部資安管理——對一家以「謹慎、負責任的 AI 開發」作為核心差異化敘事的公司而言，這種諷刺格外刺眼。

Bun 的收購決策也因此受到審視。收購 Bun 的理由之一是其打包速度優於 esbuild 和 webpack——對開發者體驗而言是顯著優勢。但這個 source map bug 在 Anthropic 收購前就已記錄在 Bun 的開源 issue 追蹤器中。Anthropic 的基礎設施團隊在將安全敏感的正式生產流程遷移至 Bun 之前，是否做了充分的已知問題稽核，如今成了公開的問號。

Bun 開發團隊在同日確認了這個 bug 並發布了修補。新版本確保無論其他設定如何，`development: false` 都會被正確執行。

## 程式碼揭露了什麼

在套件被廣泛下架前仔細研究過原始碼的開發者，描述了幾個值得注意的架構決策：

**多 Agent 協調**：Claude Code 實作了一種分層 Agent 模型，「根 Agent」可以生成擁有明確授權範圍的「子 Agent」。子 Agent 在未獲根 Agent 明確委派的情況下，無法存取指定範圍外的檔案或執行指令。這套架構顯然是為了在子 Agent 行為異常或遭到入侵時，將「爆炸半徑」降至最低。

**工具授權中介軟體**：每一次工具呼叫——讀檔、寫檔、執行 bash、抓取網頁——都要通過一個共用授權中介軟體，根據 session 層級的權限模型進行檢查。權限可以廣泛授予（「允許讀取此目錄內所有檔案」），也可以精細控制（「只允許執行這一條 bash 指令」）。

**上下文壓縮**：對於長時間執行的 Agent 任務，Claude Code 實作了一套對話歷史的滾動壓縮策略，優先保留工具呼叫結果與近期上下文，而非早期對話輪次。這是多個團隊已獨立實作過的已解決問題，但看到 Anthropic 的具體做法，仍具有競爭情報價值。

**錯誤恢復**：核心邏輯包含了對工具失敗的廣泛重試邏輯（指數退避）以及一個「降級模式」——當特定工具不可用時，Agent 仍能以降低的功能繼續運作。這是面向企業可靠性需求的生產環境強化的明證。

## 開源的問題

事件發生後，多位知名開發者公開主張 Anthropic 應直接將 Claude Code 開源——將這場安全事件轉化為社群資產。理由是：程式碼已經公開，洩漏帶來的聲譽損失已成事實，開源可以換來社群好感與貢獻，幫助核心邏輯改善得比 Anthropic 內部團隊更快。

Anthropic 拒絕就是否考慮將 Claude Code 開源置評。該公司現有的開源成果主要限於研究論文和 MCP 規格；正式生產軟體始終維持私有。

既然程式碼無論如何已實質公開，開源倡議者的論點很難被輕易駁回。Anthropic 是否選擇接受現實，或繼續在原則上主張程式碼屬於私有（哪怕實際上已不然），將說明這家公司在進入第二個十年後如何面對逆境。

目前，Claude Code v2.1.89 已在 npm 上線，source map 已正確移除。先前的版本已下架。那 4.15 萬個分叉，依然存在。
