---
title: "MCP 是新的 API：為什麼 Model Context Protocol 正在悄悄重塑 AI 基礎設施"
summary: "Anthropic 的開源 AI 工具連接協議剛突破一萬個社群實作。MCP 可能是自 REST 以來最重要的基礎設施標準。"
category: "developer-tools"
publishedAt: 2026-04-04T09:40:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "Anthropic"
    url: "https://www.anthropic.com"
  - name: "GitHub"
    url: "https://github.com"
tags:
  - "mcp"
  - "anthropic"
  - "ai-infrastructure"
  - "developer-tools"
  - "protocols"
relatedSlugs:
  - "2026-04-04-cursor-devin-war-zh"
---

## 沒人預料到的協議

2024 年 11 月，Anthropic 安靜地開源了 Model Context Protocol (MCP) — 一個連接 AI 模型和外部工具、資料來源和服務的標準。AI 社群集體聳了聳肩。

十八個月後，MCP 有超過一萬個社群建造的實作，在 Claude Code、Cursor、Windsurf 和十幾個其他 AI 工具中都有原生支援，正在快速成為 AI Agent 與世界互動的預設方式。

這是 AI 領域最重要的基礎設施發展，而幾乎沒有人在談論它。

## MCP 到底做什麼

在 MCP 之前，每個 AI 工具都自己建整合層。Claude 有它的 tool-use 格式。GPT 有 function calling。每個 Agent 框架都有自訂 API。如果你想讓你的資料庫能跟三個不同的 AI 工具運作，你要寫三套整合。

MCP 把這標準化成一個協議：

- **MCP Server** 暴露能力（讀資料庫、寄信、搜尋檔案）
- **MCP Client**（AI 工具）發現並使用這些能力
- **協議處理**認證、能力協商、串流和錯誤處理

就像 REST 標準化了 Web API。REST 之前，每個服務都有自己的協議。REST 之後，所有東西都說同一種語言。MCP 正在對 AI 與工具的通訊做同樣的事。

## 為什麼它在贏

MCP 的採用曲線對一個協議標準來說異常陡峭，原因很值得分析：

**它真的很簡單。** 一個基本的 MCP server 只要 50 行程式碼。對比建一個自訂的 OpenAI function calling 整合（200 行以上，處理邊界情況更多）。

**Anthropic 免費送出去了。** 協議完全開源，MIT 授權。沒有供應商鎖定、沒有使用費、不需要 API key。這移除了最大的採用障礙。

**網路效應啟動了。** 一旦 Cursor 採用 MCP，它的 100 萬以上使用者就能用任何 MCP server。一旦 Claude Code 採用，Anthropic 的整個用戶群都有存取權。每一個新的 client 都讓每一個現有 server 更有價值。

**社群建造了生態系。** GitHub、Slack、Notion、資料庫、雲端供應商、監控工具 — 社群已經為所有東西建了 MCP server。你現在可以透過幾行設定就給 AI agent 存取你整個技術棧的權限。

## 更大的圖像

MCP 不只是讓 AI 工具更好用。是讓 AI Agent 成為可能。

一個能讀你的 Email、查你的行事曆、更新你的專案追蹤器、查詢你的資料庫、部署你的程式碼的 AI Agent，需要一個標準方式來跟所有這些系統互動。沒有 MCP，你要為每個整合寫客製化的黏合程式碼。有了 MCP，你像拼樂高一樣插上 server 就好。

這就是為什麼 Agent 框架（LangChain、CrewAI、AutoGPT）都在採用 MCP。這不是選擇 — 它是唯一有臨界規模的標準。

## OpenAI 的回應

OpenAI 顯著地沒有採用 MCP。他們在推自己的 Responses API 和 tool-use 模式。這在生態系中造成了分叉：

- **MCP 生態**：Anthropic、Cursor、開源 Agent、大部分開發者工具
- **OpenAI 生態**：ChatGPT 外掛、GPT Actions、自訂 GPTs

歷史告訴我們開放標準會贏。但 OpenAI 有不能被忽視的分發優勢。結果還沒有定論。

## 觀察重點

- OpenAI 會採用 MCP 還是加倍投入自己的工具整合
- 企業 MCP 採用 — 當公司把內部工具標準化到 MCP 上，這個協議就變成基礎設施
- 安全性影響 — 給 AI 存取生產資料庫的 MCP server 需要嚴格的存取控制
- MCP 市集的出現 — 為企業使用而策展、驗證的 server

*每一次重大平台轉移都有一個協議時刻：HTTP 之於網路，REST 之於 API，OAuth 之於認證。MCP 可能就是 AI 的那個時刻。現在建立在它之上的公司，在 Agent 成為主流時會有結構性優勢。*
