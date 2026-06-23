---
title: "Android 17 將 Gemini Omni 嵌入作業系統層，Google 把行動平台改造成代理人基礎設施"
summary: "Google 於 6 月 16 日發布 Android 17，將 Gemini Omni 以作業系統基礎設施的形態內建，而非以 App 形式提供。本次更新帶來 Lyria 3 音樂生成、AudioLM 語音翻譯、新的 App Functions 框架，以及能跨 App 在背景執行任務的 Gemini Intelligence 代理層。"
category: "products"
publishedAt: 2026-06-22
lang: "zh"
featured: false
trending: false
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/16/android-17-launches-with-new-multitasking-tools-as-google-expands-gemini-features/"
  - name: "AI Weekly"
    url: "https://aiweekly.co/alerts/google-launches-android-17-with-gemini-omni-and-lyria-3"
  - name: "Android Developers Blog"
    url: "https://android-developers.googleblog.com/2026/05/17-things-android-developers-google-io.html"
tags:
  - "Android 17"
  - "Google"
  - "Gemini"
  - "行動 AI"
  - "代理 AI"
  - "開發者工具"
  - "Lyria 3"
  - "作業系統"
relatedSlugs:
  - "2026-06-22-android-17-gemini-omni-os-level-ai-en"
  - "2026-06-22-chatgpt-market-share-below-50-percent-ai-race-zh"
---

2011 年 Apple 將 Siri 內建於 iOS 時，外界普遍讚譽此舉讓語音 AI 真正成為手機的一部分，而非外掛功能。十五年後，Google 正以 Android 17 嘗試一件在結構層面更具野心的事：不是一個更聰明的助理，而是 AI 與作業系統之間關係的根本性重塑。

Android 17 於 2026 年 6 月 16 日發布，最初率先在 Pixel 裝置上推出，隨後擴及更廣泛的 Android 生態系，並同步附上一次 Pixel Drop 的 AI 模型更新。主打功能——Gemini Omni 影片編輯、Lyria 3 音樂生成、增強型語音翻譯——各自都令人印象深刻。但真正引發開發者與平台策略師關注的，是這些功能背後的架構轉變，那是 Google 早在 5 月 Google I/O 就已揭示的方向。

## Gemini 成為基礎設施，而非 App

Google 為 Android 17 選擇的敘事框架意圖明確：Gemini 是作業系統層級的基礎設施。這個區別在技術上至關重要。

過去在 Android 上的 Gemini 透過 App 更新交付——是一個疊加在作業系統之上的獨立層，需要用戶主動喚起才能使用。Android 17 改變了這一切。Google 為內建於 OS 的 AI 能力套件總稱「Gemini Intelligence」，以系統層級子層（system-level sub-layer）的形態運作。它在後台持續執行，能存取跨 App 的上下文，並可透過 Google 全新的 App Functions 框架在已登錄的第三方 App 中執行操作——即使那些 App 並非在前台執行。

對用戶而言，這意味著 Gemini 現在可以跨 App 完成多步驟任務。對 Gemini 說「從[App 名稱]訂我的老樣子」，系統可以找到 App 已登錄的功能、擷取參數並執行訂單，用戶甚至不需要打開那個 App。說「把這段影片剪成 90 年代風格存到相簿」，Gemini Omni 就能在 OS 層操作媒體檔案。

對開發者而言，這個訊號更為直接：未登錄 App Functions 的 App，對 Gemini 代理人而言形同隱形。在 Gemini 日益成為用戶與手機互動的環境介面的生態中，「對 Gemini 不可見」可能意味著真實的流量分發劣勢。

## Android 17 的核心功能

**Gemini Omni。** 這個多模態 AI 模型現在支援透過自然對話進行影片編輯——用戶可以用文字描述想要的修改（「移除背景」、「加西班牙文字幕」、「加速中間段落」），系統便會執行。這讓生成式影片編輯以標準系統功能的形態落地於 30 億台 Android 裝置，而非僅是某個高價第三方 App 的特色功能。

**Lyria 3。** Google 最新的音樂生成模型隨 Android 17 和 Gemini App 一同發布，讓用戶可以從文字提示或圖片生成音樂曲目。該模型支援完整曲目生成、風格控制和純器樂創作——兩年前，這類能力只存在於需要等待數分鐘才能出結果的專業網頁應用中。

**AudioLM 語音翻譯。** 在 Pixel 10a 及後續機型上，AudioLM 提供即時語音對語音翻譯，並能保留說話者的音調、語速和聲紋等特徵跨語言呈現。舊有翻譯工具能處理語言轉換，但輸出聲音機械且千篇一律。AudioLM 的方法更接近配音，而非轉錄。

**App Functions 框架。** 這是支撐代理行為的開發者架構。App 透過一個 Jetpack 函式庫將特定功能（「下訂單」、「搜尋庫存」、「查詢最新交易」）對外暴露，並對應至 Google 的 App Functions 平台 API。Gemini 代理人可以發現這些功能並以擷取的參數呼叫它們。Google 將其描述為讓 App「扮演裝置端 MCP 伺服器」——借用了已成為 AI 代理生態連接標準的 Model Context Protocol 語言。

**Android AI Core API。** 第三方開發者透過這個 API 以程式化方式存取裝置端的 Gemini Nano，實現零邊際成本的 AI 推理，不需要呼叫雲端伺服器。這對隱私和延遲都有重大意義：過去必須離開裝置才能處理的敏感查詢，現在可以完全在本地完成。

## 競爭座標

Android 17 的 AI 架構在特定的競爭時刻登場。在 2026 年 6 月的 WWDC 上，Apple 宣布 iOS 27 將採用 Gemini 驅動的 Siri——Apple 以每年約 10 億美元的代價向 Google 授權一個自訂 1.2 兆參數 Gemini 模型，這是個令人意外的發展。AI 助理競爭格局正在快速重塑：就在同一個月，ChatGPT 市占率史上首次跌破 50%，而 Gemini 成為了全球最流行行動 OS 與 Apple iOS 的共同 AI 骨幹。

Google 的結構優勢在 Sensor Tower 的參與深度數據中清晰可見：過去一年，Gemini 的每月每用戶使用時間從 14 分鐘躍升至 100 分鐘，這一激增與更深度的 Android 整合高度相關。Google 的勝利並非單靠聊天機器人的能力，而是透過作業系統層級的環境可及性。

## 開發者的行動窗口

App Functions 框架的登錄機制對 Android App 開發者形成了不容忽視的時間壓力。已登錄相容功能的 App 可以成為 Gemini 代理的操作目標，未登錄者則在用戶發出多步驟請求時不會出現在 Gemini 的視野中。

這是一個具有商業影響的平台選擇。電商 App 若登錄了允許 Gemini 瀏覽與結帳的功能、旅遊 App 若登錄了飯店搜尋與訂房功能、銀行 App 若登錄了餘額查詢與轉帳功能——這些 App 便能觸及數億主要透過 Gemini 與手機互動的用戶。未登錄的 App 則永遠比他們多一個點擊的距離。

Google 的文件揭示，Gemini Intelligence 最強大的代理功能（包括多步驟任務完成）在 6 月 16 日首發時被保留，將以軟體更新形式「在今年夏天稍後推出」。首發的 Android 17 交付的是基礎設施——Gemini Nano、App Functions、Android AI Core——最強大的代理行為將隨後跟進。

## 更長遠的押注

Android 17 是 Google 迄今對其 AI 時代平台論述最清晰的一次表達：在 AI 領域，最持久的護城河不是最好的模型，而是最深度整合進人們實際花費時間的介面之中。這個論述能否成立，取決於用戶究竟想不想要一個主動跨 App 行動的環境 AI，還是更傾向於主動呼叫的互動模式。

早期的參與數據顯示 Google 的押注正在落地。它是否最終能產生足以支撐投入的商業回報，以及是否會迫使 Apple、微軟和三星以相似的 OS 層 AI 架構回應，將是未來 18 個月需要觀察的問題。
