---
title: "Anthropic 終結算力套利時代：6 月 15 日起 Agent SDK 獨立計費"
summary: "Anthropic 宣布自 6 月 15 日起，Agent SDK 呼叫、claude -p 指令、Claude Code GitHub Actions 及 OpenClaw 等第三方代理將獨立從月度額度扣除，按 API 費率計算。Pro 用戶獲 20 美元額度；Max 20x 用戶獲 200 美元。終端機互動式 Claude Code 不受影響。"
category: "developer-tools"
publishedAt: 2026-05-15
lang: "zh"
featured: false
trending: false
sources:
  - name: "The New Stack"
    url: "https://thenewstack.io/anthropic-agent-sdk-credits/"
  - name: "XDA Developers"
    url: "https://www.xda-developers.com/anthropics-claude-subscriptions-no-longer-include-agent-sdk-and-claude-p-usage/"
  - name: "The Decoder"
    url: "https://the-decoder.com/claude-subscriptions-get-separate-budgets-for-programmatic-use-billed-at-full-api-prices/"
  - name: "Dev Tool Picks"
    url: "https://devtoolpicks.com/blog/anthropic-splits-claude-subscriptions-agent-sdk-credit-june-2026"
tags:
  - "Anthropic"
  - "Claude"
  - "Claude Code"
  - "Agent SDK"
  - "開發者工具"
  - "定價"
  - "API"
relatedSlugs:
  - "2026-05-07-anthropic-44b-arr-claude-code-growth-zh"
  - "2026-05-04-mcp-protocol-explosion-zh"
  - "2026-05-02-anthropic-claude-security-enterprise-beta-zh"
---

Anthropic 正式劃定訂閱方案的使用邊界——這項改變將顯著影響開發者、獨立駭客和企業團隊規劃 AI 代理工作流程的預算方式。

5 月 13 日，Anthropic 透過官方 @ClaudeDevs 帳號宣布：自 6 月 15 日起，透過 Agent SDK 的使用、`claude -p` 命令列旗標、Claude Code GitHub Actions，以及 OpenClaw 等第三方代理整合，將不再從現有訂閱的 token 配額扣除，而是改由一個全新的獨立月度額度支出。

這項公告終結了一個日益難以為繼的缺口：部分每月支付 20 至 200 美元的訂閱用戶，透過代理工作流程消耗的 token 量，若按直接 API 費率計算，市值可達 500 美元甚至更高。Claude Code 負責人 Boris Cherny 直白地形容這種現象：在緩存系統之外運作的第三方工具，「實在很難永續經營下去。」

## 什麼會變、什麼不變

Anthropic 劃定的界線，在於「互動式」使用與「程式化或自動化」使用之間：前者是人坐在終端機前與 Claude Code 互動；後者是軟體系統代表用戶調用 Claude，無法享有相同的對話層級緩存優勢。

**現有訂閱繼續涵蓋的內容：** 在終端機中的互動式 Claude Code 對話。這項用途被明確保留且不受影響。以 Claude Code 作為主力 AI 輔助程式設計環境的開發者，6 月 15 日後工作流程不會中斷。

**移至新額度系統的內容：**
- 以程式方式進行的 Agent SDK 呼叫
- `claude -p`（非互動模式、管道傳輸、腳本調用）
- Claude Code GitHub Actions（自動化 CI/CD 整合）
- 透過訂閱存取 Claude 的第三方代理，包括 OpenClaw 及其他基於 MCP 的自動化框架
- 任何繞過對話緩存的非互動式、自動化使用

月度 Agent SDK 額度耗盡後，程式化使用將暫停，除非用戶啟用「額外使用」計費選項——按標準隨用隨付 API 費率收費，無月度上限。額度以用戶為單位，每月到期，不得累積結轉。

## 各方案的額度金額

月度 Agent SDK 額度依訂閱方案而異：

| 方案 | 月度代理額度 |
|------|-------------|
| Pro（$20/月）| $20 |
| Max 5x（$100/月）| $100 |
| Max 20x（$200/月）| $200 |
| Team 方案 | $100/座位 |
| Enterprise 方案 | $200/座位 |

額度需在 6 月 15 日前依照 Anthropic 發送至帳號電子郵件的指示主動領取，未領取者不會自動啟用。

## 政策調整背後的經濟邏輯

此次政策終結的「算力套利」，是 Claude 訂閱方案原始設計的結構性後果——那些方案本是為人類在鍵盤前打字或透過語音介面互動的情境所設計。代理工作流程的 token 消耗模式，與此截然不同。

在終端機中使用 Claude Code 的開發者，每小時主動工作可能產生約 2 萬至 5 萬 token，且有相當可觀的緩存命中率可降低實際算力成本。而透過 Agent SDK 以多個並行任務自動調用 Claude 的代理程式——尤其是透過未參與 Anthropic 緩存基礎設施的工具路由的情況——在同等時間內可能產生 50 萬至 200 萬 token，緩存效率幾近於零。

20 美元的 Pro 訂閱從來不是為支撐這種使用模式而定價的。2026 年的轉變在於，工具生態系統——OpenClaw、第三方 MCP 伺服器、GitHub Action 整合、`claude -p` 管道——已成熟到可以系統性規模化利用這個套利空間。數以千計的開發者已發現，一個 20 美元的 Claude 訂閱可以充當月費 500 美元的 API 金鑰，而且這種模式正在加速擴散。

## 開發者社群的反應

開發者社群的反應喜憂參半，但大體上表示理解。對自動化使用「免費搭便車」不可持續，多數人已有共識。更尖銳的批評指向額度金額本身。

按目前 Claude API 定價，20 美元的月度 Agent SDK 額度在 Haiku 等級定價下約可支應 4,000 萬至 8,000 萬個輸入 token，在 Sonnet 等級下約為 400 萬至 800 萬個輸入 token。對打造輕量自動化的開發者——GitHub issue 分類機器人、文件摘要管道、程式碼審查助手——這個預算勉強夠用。但對跑複雜多代理系統、處理大型程式碼庫或執行長程任務的開發者，則明顯不足。

Zed 編輯器團隊發布了針對此次改變如何影響其 Claude 整合的具體分析，指出重度依賴自動化程式建議的用戶可能需要啟用額外使用計費，才能維持現有工作流程。其他多個 IDE 和開發者工具廠商預計也將在 6 月 15 日前更新各自的引導文件。

## 策略背景：代理規模化的定價難題

Anthropic 的計費調整，折射出所有基礎模型提供商都在面對的共同挑戰：如何為程式化、代理式、自動化的存取模式定價，讓提供商能夠永續，同時讓開發者能夠預測成本。

OpenAI 從一開始就嚴格區隔 API 使用與 ChatGPT 訂閱使用。Google 同樣將 Gemini API 存取與 Gemini 應用程式使用視為完全獨立的產品。Anthropic 最初允許 Claude 訂閱同時服務兩種用途，這對開發者非常友善，也推動了 Agent SDK 和 Claude Code 生態系統的快速採用。6 月 15 日的調整，代表的是這套方法的進化成熟，而非放棄。

Boris Cherny 將此次改變定調為持續投資開發者生態的前提條件：沒有可持續的程式化存取經濟基礎，Anthropic 就無法為 Agent SDK 規模化所需的基礎設施和工程資源提供合理依據。

## 6 月 15 日及其後的影響

以程式方式使用 Claude 的開發者，應在改版前審視自己的使用模式。核心問題是：現有工作流程屬於互動式還是程式化？月度 Agent SDK 額度是否足以涵蓋典型消耗量？

對於超出額度的用戶，「額外使用」計費選項以標準 API 費率提供服務連續性，按 token 計費、沒有任意上限。Anthropic 已表示此選項將在 6 月 15 日前開放帳號層級啟用。

更長遠的走向值得關注。如果 Agent SDK 額度對開發者社群的實際用量而言過於保守，Anthropic 很可能面臨調高配額的壓力——尤其是 Max 和 Enterprise 方案，目前的配額可能無法反映代理部署的實際規模。反之，若此次改變成功使按 token 計費的自動化存取正常化，也將為更精細的開發者定價層次奠定基礎，更好地服務生態系統中的各種工作負載。

就眼前而言：算力套利時代已告終結。代理式存取 Claude 需要付費——只是對大多數開發者來說，金額可能比想像中低。
