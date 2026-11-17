---
title: "Anthropic升級Claude語音模式：支援Opus、Sonnet與App連接器"
summary: "Anthropic於7月23日更新Claude語音模式，新增能力更強的Opus與Sonnet模型支援，並整合Gmail、Google日曆、Slack、Canva與Notion等工具的App連接器。這次更新讓語音AI不再只是聊天，用戶現在可以透過語音請Claude處理已連接的App。"
category: "ai-ml"
publishedAt: 2026-07-28
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: false
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/07/23/anthropic-updates-claude-voice-mode-with-more-capable-models/"
  - name: "Digital Applied"
    url: "https://www.digitalapplied.com/blog/claude-voice-mode-opus-sonnet-connectors-2026"
  - name: "MacRumors"
    url: "https://www.macrumors.com/2026/07/24/claude-voice-mode-opus-sonnet-model-support/"
  - name: "VoiceOS"
    url: "https://www.voiceos.com/blog/claude-voice-mode"
tags:
  - "Anthropic"
  - "Claude"
  - "語音AI"
  - "AI代理"
  - "多模態"
  - "生產力"
relatedSlugs:
  - "2026-07-26-anthropic-claude-opus-5-launch-zh"
  - "2026-04-04-mcp-protocol-explosion-zh"
---

Anthropic大幅擴展了你和Claude說話時它能做到的事。

2026年7月23日，這家公司對Claude語音模式推出了重大更新，將原本僅限Haiku的功能升級為可自選模型的體驗，預設值為用戶上一次在文字對話中選用的模型。更重要的是，這次更新引入了App連接器——在對話進行中透過語音指令在Gmail、Google日曆、Slack、Canva和Notion觸發真實操作的能力。

這個組合讓語音模式不再只是快速提問：用戶可以說出一項任務，讓Claude處理已連接的App。

## 從Haiku到Opus：改變了什麼

在這次更新之前，Claude語音模式（於去年推出）一直在Haiku上運行——Anthropic速度最快、最輕量的模型。Haiku的優點是低延遲和低成本；當用戶想透過語音模式梳理複雜問題或進行深度分析對話時，其局限性便顯而易見。

7月23日的更新解鎖了Sonnet和Opus。語音模式現在預設為用戶在文字會話中最後選用的模型，確保跨互動模態的連貫性。在語音對話中，用戶可從模型選擇器切換模型，當對話從快速提問轉向複雜推理時，這項功能就很重要。

延遲影響是真實存在的。Opus是Anthropic能力較強的模型之一，而Haiku則是速度最快的模型。Anthropic表示，語音模式預設會使用所選模型的最快版本。

對於主要用語音模式進行快速查詢、查看日程和簡單任務的用戶，Haiku依然是正確的預設選擇。對於想透過語音免持手談戰略決策、分析文件、或進行深度解題對話的用戶——也就是讓語音AI對知識工作者真正有用的使用情境——Opus語音模式是實質性的能力擴展。

## App連接器：語音觸發的自動化

這次更新更具變革意義的部分是連接器系統。語音模式現在可以連接Gmail、Google日曆、Google Docs、Slack、Canva和Notion等已連接的App：

- **Gmail**：透過語音草擬郵件或摘要郵件串。
- **Google日曆**：查看日曆或更新會議時段，無需切換到日曆App。
- **Slack**：透過語音指令草擬Slack回覆。
- **Canva**：透過語音更新Canva設計。
- **Notion**：透過語音指令在Notion建立文件。

免費用戶可以連接一個外部應用程式。Claude Pro及以上付費訂閱用戶可解鎖多App功能，讓語音模式在單一對話線程中跨多個已連接服務協調操作。

## 語言擴展：十一個市場

多語言支援已於今年稍早以測試版加入語音模式，用戶必須手動選擇語言。支援的語言包括英語、法語、德語、印地語、印尼語、義大利語、日語、韓語、巴西葡萄牙語，以及西班牙語（拉丁美洲和西班牙）。

## 架構問題：輪流制vs雙工制

Claude的語音模式採用輪流制架構：系統聆聽、處理完整的語句，然後做出回應。這與OpenAI的GPT-Live模式不同，後者採用全雙工設計，同時處理語音並生成回應，實現更自然的打斷和來回互動。

輪流制有其取捨。它感覺上不那麼像人類對話，更像是一個具備顯著更強推理能力的語音助理——相當於推理能力大幅提升的Alexa。

Anthropic尚未公開承諾會轉向雙工架構，7月23日的更新也沒有改變底層架構。

對大多數實際使用情境——口述郵件、管理日程、搜尋文件、提問分析問題——輪流制已綽綽有餘。當語音AI移向需要真實即時對話的使用情境時，架構之爭才變得更為相關：談判、協作解題，或對話節奏本身就有意義的情感支持場景。

## 這在AI語音競賽中的位置

Anthropic的語音更新在2026年一個已顯著加劇競爭的市場中推出。OpenAI的GPT-Live模式已整合至ChatGPT的手機和桌面應用程式，確立了強勁的消費者市場地位。

Claude的連接器生態系是其在語音領域最具差異化的競爭優勢。OpenAI的語音模式雖然更新了對話風格，卻仍無法使用不同工具來完成工作；相較之下，Claude語音模式可以連接Slack、Notion和Gmail等App。

定價結構強化了這種定位。完整連接器存取的Claude語音模式需要付費訂閱，這隱含地針對已在為生產力軟體付費的用戶——這類用戶更可能將Claude語音模式整合進現有工具堆疊，從中發現複合價值，而非偶爾使用以嚐鮮。

7月23日的更新是迄今為止對這個功能最實質性的擴展，其受歡迎程度將揭示，公司將語音視為嚴肅生產力界面（而非展示功能）的押注，究竟是否合理。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 25 處。*
