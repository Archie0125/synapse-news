---
title: "Agentic AI Foundation：科技業最強勁的對手，為何聯手打造 AI Agent 開放標準？"
summary: "Linux Foundation 旗下的 Agentic AI Foundation（AAIF）悄悄成為 AI 史上最重要的治理行動之一——OpenAI、Anthropic、Google、微軟、AWS 和 Block 共同加入，攜手為 AI Agent 建立開放標準。MCP 月下載量突破 9,700 萬次、AGENTS.md 被 6 萬個以上開源專案採用，AAIF 正將競爭對手轉變為基礎設施合作夥伴。"
category: "developer-tools"
publishedAt: 2026-04-06T09:00:00Z
lang: "zh"
featured: false
trending: false
sources:
  - name: "Linux Foundation"
    url: "https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation"
  - name: "OpenAI"
    url: "https://openai.com/index/agentic-ai-foundation/"
  - name: "MCP Blog"
    url: "https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/"
  - name: "Block"
    url: "https://block.xyz/inside/block-anthropic-and-openai-launch-the-agentic-ai-foundation"
tags:
  - "AAIF"
  - "Linux Foundation"
  - "MCP"
  - "AI代理"
  - "開放標準"
  - "開發者工具"
  - "Anthropic"
  - "OpenAI"
relatedSlugs:
  - "2026-04-04-mcp-protocol-explosion-zh"
  - "2026-04-06-microsoft-mai-models-independence-zh"
  - "2026-04-06-openai-superapp-zh"
  - "2026-04-06-agentic-ai-foundation-en"
---

## 最奇特的同床異夢

上次 OpenAI 和 Anthropic 共同做一件事，是什麼時候？這兩家公司或許是 AI 領域競爭最激烈的對手——爭搶研究人才、客戶、基準測試排名，以及話語權。Google 和微軟則是幾十年的平台層宿敵。

然而在 2025 年 12 月，上述四家公司——加上亞馬遜 AWS、Block、Bloomberg 和 Cloudflare——聯合在 Linux Foundation 旗下創立了 **Agentic AI Foundation（AAIF）**。

這種「競爭前協作」（pre-competitive collaboration）在基礎設施技術領域有充分先例：TCP/IP、HTTP、Linux、Kubernetes——構成現代運算隱形骨幹的協議與平台，都是透過類似的產業協調機制建立起來的。競爭對手合作制定標準，因為互通性讓所有人受益；然後在這些標準之上，各自激烈競爭。沒有人能從「擁有私有版本的 TCP/IP」中獲益；所有人都能從「在共同網路標準上建造更好產品」中受益。

AAIF 是 AI 產業對 Agent 時代下的同一個賭注。

## 基礎會建立什麼？

AAIF 以三個創始技術專案起步，各由原始創建者捐贈：

**Model Context Protocol（MCP）**，由 Anthropic 捐贈，是連接 AI 模型與外部工具、資料來源及應用程式的通用開放標準。2024 年底推出以來，MCP 已成為 AI 史上採用速度最快的開源專案之一：截至 2026 年初，月 SDK 下載量突破 9,700 萬次，超過 10,000 個活躍 MCP 伺服器，並在 ChatGPT、Claude、Cursor、Gemini、Microsoft Copilot、VS Code 等數十個平台獲得原生支援。

Anthropic 決定將 MCP 捐贈給 AAIF，是一個經過算計的戰略選擇：放棄對標準的私有控制，換取大幅加速的採用率。企業不會在單一廠商控制的協議上建構關鍵基礎設施，他們押注的是具備透明治理的開放標準。這一舉動讓 MCP 從「Anthropic 的協議、其他人也在用」，變成「整個產業共同維護的協議」。

**AGENTS.md**，由 OpenAI 捐贈，是一個更輕量的標準，但採用數字令人印象深刻。它提供 AI 程式 Agent 一致性的專案特定指引：讓 Agent 能可靠地在不同程式庫和工具鏈之間運作。超過 60,000 個開源專案已採用 AGENTS.md——可以把它想像成 `.gitignore` 的 AI 代理版本：一個簡單的文件，大幅提升 Agent 在任何程式庫中的可靠性。

**goose**，由 Block（前身為 Square）捐贈，是一款開源、本地優先的 AI Agent 框架，結合語言模型、可擴展工具與基於 MCP 的整合。它代表堆疊中的不同層次——不是協議或規格，而是一個基於開放標準構建的 Agent 系統參考實作。

## 2026 年 2 月為何是轉折點

AAIF 在 2025 年 12 月以初始鉑金會員啟動。但 2026 年 2 月宣布新增 97 個會員（18 個黃金級、79 個白銀級），標誌著基金會從「創始聯盟」跨越到「真正的產業運動」。

這一數字的意義不只是數量。企業技術決策向來緩慢。當 97 家公司在創立後兩個月內加入一個開放標準組織，通常意味著大型組織的採購與工程領導層已得出結論：這個標準足夠安全，值得押注——它有充分的產業背書，不會落得棄置標準、讓大量投資陷入廠商鎖定的下場。

AAIF 達到這個訊號的速度，幾乎比近年任何類似標準組織都更快。

## 企業層面的巨大賭注

AAIF 背後的緊迫性，在分析師預測中清晰可見。Gartner 預測，到 2026 年底，40% 的企業應用將包含任務特定 AI Agent——相比一年前不到 5%，增幅達八倍。這代表了龐大的基礎設施建設需求，而所有這些都需要解決一個根本性的互通問題：一個系統中的 Agent，如何與另一個系統中的工具和資料溝通？

沒有開放標準，這個問題的答案就是廠商鎖定。每一個主要 AI 平台——OpenAI、Anthropic、Google、微軟——都有建立私有 Agent 框架、將客戶綁定到自家模型生態系的自然動機。AAIF 代表的是業界的集體認知：這個結果對整個產業都不利——它會減慢採用、製造安全碎片化，最終對任何人都無益。

MCP 的成功說明了開放標準能達成什麼。在 MCP 之前，將 AI 模型連接到外部工具，每一對模型與工具都需要客製化整合。有了 MCP，任何符合規範的模型都能連接任何符合規範的工具，雙方各自只需一次整合。MCP 所實現的相容性組合爆炸——理論上從 N×M 個整合降至 N+M 個——正是讓網際網路得以誕生的同一邏輯。

## 治理的緊張地帶

AAIF 也有批評者，他們的顧慮值得正視。AI 治理研究者 Shashi Jagtap 在 2025 年 12 月的一篇文章中，將其描述為「封閉治理與鉑金付費牆」——鉑金會員費遠高於白銀或黃金等級，而大多數 Linux Foundation 定向基金的決策權，高度集中在會費等級較高的成員手中。

批評的核心是：AAIF 對外呈現為開放、民主的標準機構，但其治理結構對八個鉑金會員——恰好也是 AI 產業最強大的既有玩家——賦予了不成比例的話語權。一家建立在 MCP 上的新創公司，對標準技術方向幾乎沒有實質影響力。

這個問題並非 AAIF 獨有——它是大多數大型開源基金會的結構性特徵。Linux Foundation、Apache Foundation、CNCF 都有類似的分層會員制，使治理權集中於大型公司。反駁論點是：這只是現實的反映——標準組織需要持續的資金與組織投入才能運作，而大型公司能提供這兩者。無論會員等級如何，開源程式碼和規格對所有人都保持開放。

## 接下來的路

AAIF 的近期路線圖聚焦幾個方向：Agent 系統的安全標準（如何對代表用戶採取行動的 Agent 進行認證、授權與審計？）、互通性測試框架，以及最具野心的——類似 Agent「開放技能標準」的機制，讓不同框架建構的 Agent 能夠共享能力。

最後一項是技術上最具挑戰性的目標。一旦成功，意味著以 OpenAI 框架建構的 Agent，能夠透過開放標準協議呼叫為 Anthropic 生態系開發的技能。這種互通程度對企業 AI 採用而言，將是真正的變革。

Cisco 在 2026 年 1 月加入 AAIF，帶來其網路和安全專業知識解決 Agent 認證問題——這是大型基礎設施公司對治理工作高度重視的訊號。

計算機科學的歷史表明，AI Agent 時代的競爭，最終將在標準層而非模型層分出勝負。模型會來了又去，持續進步、不斷壓縮；協議的存活時間則會超過任何一家公司的產品週期。AAIF 是一個賭注：AI 最強大的競爭對手們理解這個道理——他們對繁榮 Agent 生態的共同利益，超越了各自對私有控制的個別追求。

看看誰加入了，這個賭注值得認真關注。
