---
title: "Apple WWDC 2026 主題演講：Gemini 驅動的 Siri、iOS 27，以及 Tim Cook 的告別"
summary: "Apple WWDC 2026 主題演講帶來了公司近年來最重大的 AI 轉型：由 Google 1.2 兆參數 Gemini 模型全面重建的 Siri、iOS 27 的 Liquid Glass 設計語言、允許用戶自選 AI 供應商的 Extensions 系統，以及 Tim Cook 以 CEO 身份最後一次的舞台告別。這場演講標誌著 Apple Intelligence 在兩年的跳票與延遲之後，終於迎來了徹底的重置。"
category: "products"
publishedAt: 2026-06-08
lang: "zh"
featured: true
trending: true
sources:
  - name: "Tom's Guide WWDC 2026 Live"
    url: "https://www.tomsguide.com/news/live/wwdc-2026-live-news-updates"
  - name: "MacRumors WWDC 2026"
    url: "https://www.macrumors.com/roundup/wwdc/"
  - name: "Let's Data Science"
    url: "https://letsdatascience.com/news/apple-unveils-gemini-powered-siri-and-ios-27-at-wwdc-2026-b757953c"
  - name: "Apple Newsroom"
    url: "https://www.apple.com/newsroom/2026/05/apple-kicks-off-worldwide-developers-conference-on-june-8/"
tags:
  - "Apple"
  - "WWDC"
  - "Siri"
  - "Google Gemini"
  - "iOS 27"
  - "Apple Intelligence"
  - "Tim Cook"
relatedSlugs:
  - "2026-06-06-apple-wwdc-2026-preview-siri-ios27-zh"
  - "2026-06-01-apple-wwdc-2026-ai-reset-siri-core-ai-zh"
---

太平洋時間週一早上 10 點，Tim Cook 最後一次以 CEO 身份走上 Apple Park Steve Jobs Theater 的舞台。今年的主題是「All Systems Glow」——一個再明顯不過的暗示：2026 年的全球開發者大會，將全力押注人工智慧。結果也沒讓人失望。

在兩年的延遲跳票、搞砸的 Demo，以及讓用戶大失所望的 Apple Intelligence 推進之後，Apple 用 WWDC 2026 全面重設了 AI 戰略。核心成果包括：由授權自 Google 的 Gemini 模型從零重建的 Siri、深度整合 AI 的 iOS 27 系統級改版、允許用戶選擇不同 AI 供應商的全新 Extensions 框架，以及 Tim Cook 動情的告別致詞。曾堅持所有技術自研的 Apple，如今簽下一筆每年約 10 億美元的 Google 合約，並在舞台上公開承認了這一切。

## 全新 Siri：Gemini 引擎，Apple 設計

WWDC 2026 的核心是一個幾乎與舊版毫無相似之處的 Siri。這套系統基於 Google Gemini 的 1.2 兆參數客製版本，年授權費用估計約 10 億美元——這是 Apple 迄今規模最大的 AI 基礎設施合作案。

全新 Siri 首次以獨立 App 形式登場，支援 iOS 27、iPadOS 27 及 macOS 27。用戶透過類似 iMessage 的持續對話介面進行互動，完整對話記錄透過 iCloud 同步。在 iPhone 上，Siri 嵌入動態島（Dynamic Island），提供常駐的視覺存在感，不再像過去那樣短暫浮現即消失。

更實質的改變在於，Siri 獲得了深度個人情境感知——可存取郵件、照片、檔案、行事曆及聯絡人——讓它得以回答過去需要手動切換多個 App 才能處理的問題。它能感知螢幕內容、跨 App 執行操作，並完成複合任務，例如「找出上個月我會計師寄來的郵件，整理成待辦清單」。

Apple 將這套雲端系統稱為「Siri Intelligence」，並明確說明部分查詢會透過 Private Cloud Compute（私有雲端運算）這一隱私保護推論架構，路由至 Google 伺服器。涉及敏感資料的請求則透過 Apple Silicon 及神經引擎在裝置端完成處理。

## iOS 27：Liquid Glass 全面滲透

iOS 27 將 Apple 去年引入的 Liquid Glass 設計語言擴展至整個系統，並針對此前外界批評的「視覺雜訊過多」問題進行了調整。狀態列、通知中心、控制中心均採用這一風格，讓 iPhone 呈現出能動態呼應桌布與環境光的整體透明質感。

AI 功能滲透至 iOS 27 的各個角落。Image Playground 新增了寫實風格圖片生成能力——這是相較於此前僅限卡通風格的重大進步。Writing Tools 的「Coach（教練）」模式提供結構化的語氣、清晰度與架構回饋，而非單純改寫文字。照片 App 的生成式搜尋功能允許用戶用情感描述找到照片，例如「那次在海邊大家都在笑的照片」。

Visual Intelligence 結合全新 Siri，讓 iPhone 鏡頭成為複合查詢介面：對著餐廳拍攝，Siri 可同時拉取評論、查閱行事曆，並透過第三方 App 直接訂位。

iOS 27 的無障礙功能也大幅擴充，包括自然語言語音控制、更精細的字幕客製化，以及結合 AI 場景描述的強化版 VoiceOver。

## Extensions 系統：Apple 開放 AI 平台

WWDC 2026 戰略意義最深遠的宣布，是 AI Extensions 框架。Apple 首次允許第三方 AI 供應商——包括 OpenAI 的 ChatGPT、Google Gemini，以及 Anthropic 的 Claude——作為驅動 Apple Intelligence 功能的智慧核心。

用戶可在設定中指定偏好的 AI 供應商，該供應商將接手處理 Writing Tools、Image Playground、Siri 對話介面等 Apple Intelligence 功能的請求。Apple 自家的 Gemini 版 Siri 仍為預設選項，但 Extensions 系統讓 Apple 從封閉 AI 供應商轉型為 AI 平台——這一轉變，既反映了來自各家前沿 AI 實驗室的競爭壓力，也承認了在所有維度全面追趕的實際困難。

對開發者而言，Extensions API 開啟了全新的應用類別：能原生嵌入 Apple 作業系統介面的客製 AI 體驗，而非只能存在於獨立 App 內。這對企業軟體、生產力工具及教育應用的影響，不可小覷。

## 折疊式 iPhone：軟體先行

Apple 確認 iOS 27 已原生支援即將推出的折疊裝置（內部代號 iPhone Fold）的螢幕形態。軟體層面首次在 iPhone 上引入分割檢視模式，展開時支援兩個 App 並排顯示，折疊時則維持一般單 App 佈局。這套多工系統借鑑了 iPadOS 的 Stage Manager，但針對折疊裝置在展開與折疊之間的切換狀態，進行了全新的設計。

硬體發表預計要到 9 月才會登場，屆時 Cook 的繼任者 John Ternus 可能將主持 iPhone 發表會。但 iOS 27 的軟體鋪墊，清楚表明這款產品真實存在，已接近出貨狀態，並是 Apple 2026 年下半年硬體路線圖的核心。

## Tim Cook 的告別

在產品 Demo 開始之前，Tim Cook 發表了一段簡短致詞，卻承載著傳承的分量。他坦承 Apple Intelligence「尚未兌現我們承諾的一切」——這是 Apple 這家以嚴格管控公開敘事著稱的公司，難得一見的公開認錯。他將 WWDC 2026 定位為 Apple AI 時代真正的起點，也是公司積累技術與人才之後，終於準備好全力一搏的轉折。

今年 65 歲的 Cook 在 4 月宣布將於 9 月 1 日卸任，由硬體工程高級副總裁 John Ternus 接班。他的任期見證了 Apple 從 3,500 億美元市值成長為超過 4 兆美元的科技帝國。自 Jobs 於 2011 年辭世後，WWDC 舞台始終是 Cook 最具代表性的主場。他的告別，是他一貫的低調風格：簡短致謝，揮手，然後把麥克風交了出去。

## 接下來呢？

iOS 27、iPadOS 27、macOS 27、watchOS 27、tvOS 27 及 visionOS 27 的開發者測試版現已開放。公開測試版預計 7 月釋出，正式版則預定與 9 月新 iPhone 硬體一同亮相。

Google Gemini 授權協議從根本上改變了 Apple 的競爭格局，其深遠影響需要數月時間才能充分顯現。一方面，這讓 Apple 超過十億台設備的用戶，得以在 Apple 自研時程難以達到的水準下，立刻獲得一個真正能用的 AI 助理。另一方面，這也製造了對競爭對手 Google 的深度依賴，並引出一個根本問題：五年後，當 Gemini 只是一個預設選項而非差異化優勢時，Apple 的 AI 護城河究竟在哪裡？

眼下，Apple 已押下注碼。平台已開放，模型已授權，主題演講也已落幕。WWDC 2026 最確鑿地證明了一件事：Apple，在猶豫兩年之後，決定全力競爭了。
