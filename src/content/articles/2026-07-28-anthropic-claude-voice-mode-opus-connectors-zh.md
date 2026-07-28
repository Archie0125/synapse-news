---
title: "Anthropic升級Claude語音模式：Opus模型加持、跨App自動化、支援11種語言"
summary: "Anthropic於7月23日大幅翻新Claude語音模式，新增Opus與Sonnet模型支援，並整合Gmail、Google日曆、Slack、Canva與Notion等App連接器。用戶現在可以透過語音觸發跨應用程式的真實操作，讓語音AI從聊天工具升級成具備代理能力的生產力前端。"
category: "ai-ml"
publishedAt: 2026-07-28
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

2026年7月23日，這家公司對Claude語音模式推出了重大更新，將原本僅限Haiku的功能升級為完整的模型自選體驗，預設值為用戶上一次在文字對話中選用的模型。更重要的是，這次更新引入了App連接器——在對話進行中透過語音指令在Gmail、Google日曆、Slack、Canva和Notion觸發真實操作的能力。

這個組合將語音模式從方便的輕量查詢介面，蛻變為代理工作流程的可行前端：說出一項任務，讓Claude在你的生產力工具堆疊中執行，全程不需切換App、不需打一個字。

## 從Haiku到Opus：改變了什麼

Claude語音模式的最初版本於2026年初推出，僅在Haiku上運行——Anthropic速度最快、最輕量的模型。Haiku的優點是低延遲和低成本；當用戶想透過語音模式梳理複雜問題或進行深度分析對話時，其局限性便顯而易見。

7月23日的更新解鎖了Sonnet和Opus。語音模式現在預設為用戶在文字會話中最後選用的模型，確保跨互動模態的連貫性。在語音對話中，用戶可透過語音指令明確切換模型——這個功能看似細微，但當對話性質從快速提問轉向複雜推理時，它在實踐中的重要性毋庸置疑。

延遲影響是真實存在的。Opus是Anthropic能力最強、也最耗費算力的模型；在Opus上進行的語音對話回應速度，明顯慢於Haiku。Anthropic表示已優化服務架構以縮小差距，為每個模型層級的語音會話提供「最快的可用版本」，但尚未公布三個層級的具體延遲基準。

對於主要用語音模式進行快速查詢、查看日程和簡單任務的用戶，Haiku依然是正確的預設選擇。對於想透過語音免持手談戰略決策、分析文件、或進行深度解題對話的用戶——也就是讓語音AI對知識工作者真正有用的使用情境——Opus語音模式是實質性的能力擴展。

## App連接器：語音觸發的自動化

這次更新更具變革意義的部分是連接器系統。Anthropic在首批支援五個應用程式：

- **Gmail**：透過語音閱讀、撰寫、發送、搜尋和整理郵件。「找出這個月所有來自我律師的郵件並摘要」現在只需一個語音指令。
- **Google日曆**：創建活動、確認空檔、重新安排行程、查看日程——無需切換到日曆App。
- **Slack**：透過語音指令發送訊息、閱讀頻道更新、設定提醒、搜尋對話記錄。
- **Canva**：語音觸發的設計操作——建立新專案、套用模板、請求設計修改——適用於雙手操作不便的情境。
- **Notion**：透過語音指令創建和編輯頁面、搜尋工作空間內容、管理資料庫。

連接器底層架構採用Anthropic的MCP（模型上下文協定）標準，與Anthropic自2024年底以來持續建置於Claude更廣泛生態系中的協定相同。語音模式獲得連接器存取意味著，它現在運行在與Claude文字工具使用相同的代理基礎設施上——這種融合暗示Anthropic正在朝向統一的代理後端邁進，無論互動模態為何。

免費用戶可以連接一個外部應用程式。Claude Pro及以上付費訂閱用戶可解鎖多App功能，讓語音模式在單一對話線程中跨多個已連接服務協調操作。

## 語言擴展：十一個市場

7月23日的更新也將語音模式的語言支援從僅限英語擴展至十一種語言：英語、法語、德語、印地語、印尼語、義大利語、日語、韓語、葡萄牙語和西班牙語。這項擴展對Anthropic的國際成長野心意義重大——在海外市場，Claude歷來比在美國市場更缺乏存在感。

這11種語言涵蓋約32億母語使用者，讓Claude語音模式在西歐、南亞和東南亞、東亞以及拉丁美洲都有了可行的市場觸及——這些都是OpenAI語音產品快速擴張的市場，也是Anthropic一直在投資縮小差距的地方。

## 架構問題：輪流制vs雙工制

Claude的語音模式採用輪流制架構：系統聆聽、處理完整的語句，然後做出回應。這與OpenAI的GPT-Live模式不同，後者採用全雙工設計，同時處理語音並生成回應，實現更自然的打斷和來回互動。

輪流制有其取捨。建立和除錯更簡單，避免了部分語句處理產生的音訊失真，在嘈雜環境中效果更好——因為系統需要確認語音輸入已結束，才能生成回應。它感覺上不那麼像人類對話，更像是一個具備顯著更強推理能力的語音助理——相當於推理能力大幅提升的Alexa。

OpenAI認為雙工制是語音AI的正確長期架構，援引用戶研究數據，顯示人們偏好能被打斷、能動態回應的系統。Anthropic尚未公開承諾會轉向雙工架構，7月23日的更新也沒有改變底層架構。

對大多數實際使用情境——口述郵件、管理日程、搜尋文件、提問分析問題——輪流制已綽綽有餘。當語音AI移向需要真實即時對話的使用情境時，架構之爭才變得更為相關：談判、協作解題，或對話節奏本身就有意義的情感支持場景。

## 這在AI語音競賽中的位置

Anthropic的語音更新在2026年一個已顯著加劇競爭的市場中推出。OpenAI的GPT-Live模式已整合至ChatGPT的手機和桌面應用程式，確立了強勁的消費者市場地位。Google的NotebookLM音訊摘要功能和Gemini Live擴展已讓Google語音AI觸及數億Android用戶。Apple由Apple Intelligence驅動的增強版Siri在設備端本地運行——這種隱私定位是依賴雲端架構的Anthropic和OpenAI所無法複製的。

Claude的連接器生態系是其在語音領域最具差異化的競爭優勢。OpenAI在ChatGPT中也有插件整合，但連接器深度——首批五款App加上MCP支撐的擴展路徑——讓Claude語音模式成為企業生產力使用情境的更有力競爭者；而這些使用情境中涉及的App（Slack、Notion、Gmail）本就是日常工作流程的一部分。

定價結構強化了這種定位。完整連接器存取的Claude語音模式需要付費訂閱，這隱含地針對已在為生產力軟體付費的用戶——這類用戶更可能將Claude語音模式整合進現有工具堆疊，從中發現複合價值，而非偶爾使用以嚐鮮。

自推出以來，Anthropic尚未公布語音模式的使用人數。7月23日的更新是迄今為止對這個功能最實質性的擴展，其受歡迎程度將揭示，公司將語音視為嚴肅生產力界面（而非展示功能）的押注，究竟是否合理。
