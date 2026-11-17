---
title: "Apple 每年付 Google 10億美元讓 Siri 活下去：WWDC 2026 的歷史轉折"
summary: "在 WWDC 2026，Apple 發表重建後的 Siri，由客製化 Google Gemini 模型驅動（據報約1.2兆參數），據報每年成本約10億美元；iOS 27 採三層 AI 路由架構，預期將終止支援 iPhone 11，而第三方聊天機器人的擴展框架出現在測試版中，但並未在大會上宣布。Tim Cook 在此次大會結束其 CEO 生涯中最後一場主題演講。"
category: "products"
publishedAt: 2026-06-16
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: false
sources:
  - name: "TechRadar — Apple WWDC 2026 直播"
    url: "https://www.techradar.com/news/live/apple-wwdc-2026-live"
  - name: "Tom's Guide — WWDC 2026 總覽"
    url: "https://www.tomsguide.com/news/live/wwdc-2026-live-news-updates"
  - name: "MacRumors — WWDC 2026 全部公告"
    url: "https://www.macrumors.com/2026/06/08/wwdc-2026-recap/"
  - name: "9to5Mac — iOS 27 多 AI 擴展報告"
    url: "https://9to5mac.com/2026/05/05/ios-27-will-let-you-choose-between-gemini-claude-and-more-for-ai-features-report/"
  - name: "TechJournal — WWDC 2026 Siri 與 Gemini"
    url: "https://techjournal.org/wwdc-2026-siri-gemini-ios-27"
tags:
  - "Apple"
  - "WWDC 2026"
  - "Siri"
  - "Google Gemini"
  - "iOS 27"
  - "Apple Intelligence"
  - "Tim Cook"
relatedSlugs:
  - "2026-06-15-google-gemini-35-pro-imminent-launch-zh"
  - "2026-06-14-anthropic-overtakes-openai-aws-5gw-compute-deal-zh"
---

2026年6月8日，Tim Cook 走上 Apple Park 的舞台，出席他以 CEO 身份主持的最後一場 WWDC 主題演講。他宣布的消息，標誌著 Apple 核心策略的歷史性斷裂：這家以「掌控從晶片到軟體完整堆疊」為立業之本的公司，如今每年向 Google 支付約10億美元，為其 AI 助理提供動力。

新版 Siri 不是漸進式改進，而是重建——最繁重的查詢運行在一個據報擁有1.2兆參數的 Google Gemini 定制版本上。這是 Apple 數十年來對第三方基礎架構最重大的一次依賴，也是 Tim Cook 團隊對一個事實的坦率承認：Apple 無法靠自己在雲端 AI 領域打造具有競爭力的能力。

## 新 Siri 的三層架構

重建後的 Siri 運行在一個 Apple 工程師耗費多年設計的三層路由系統上，在隱私、能力和成本之間尋求平衡。

**第一層：簡單指令** ——設定計時器、開啟應用程式、查看天氣——完全在裝置本地端處理，由執行於神經引擎上的精簡版 Apple 訓練模型完成。這保留了 Apple 過去十年品牌建立的隱私承諾：日常任務不需要你的資料離開 iPhone。

**第二層：中等複雜度請求** ——起草電子郵件、摘要文件、管理日曆衝突——路由至 Apple 的「私有雲端運算」（Private Cloud Compute）基礎架構，這是一套由 Apple Silicon 伺服器組成的系統，專為在不儲存用戶資料的前提下處理雲端 AI 工作負載而設計。

**第三層：複雜查詢** ——開放性研究、多步驟規劃、創意生成——路由至 Gemini 的雲端基礎架構，在10億美元年度協議下運行那個1.2兆參數的模型。Apple 在更新後的隱私文件中說明，這些查詢在嚴格的資料處理條款下處理——但批評者指出，當 Google 的伺服器開始處理你部分 Siri 詢問時，根本的隱私格局已悄然改變。

新版 Siri 具備獨立的對話式應用介面（支援完整文字輸入）、多步驟指令鏈、螢幕感知能力（可回應目前顯示在螢幕上的內容），以及從你的電子郵件、照片和文件中提取的個人脈絡。當助理不確定路由方向時，會向用戶發出信號——Apple 將此定位為 AI 決策透明度的設計選擇。

## Claude 與 ChatGPT 悄然入駐

iOS 27 的開發者測試版包含「擴展」（Extensions）框架的底層支援，可讓用戶在 Siri 內切換 ChatGPT、Claude 與 Gemini，不過據報其設定面板與 App Store 區塊目前處於關閉狀態。據 Bloomberg 報導，iOS 27 將讓用戶聽到由外部模型驅動的 Siri 回應，使用與 Apple 自家系統不同的聲音。

值得注意的是，這個擴展系統並未出現在6月8日的主題演講中。Apple 大篇幅展示了新的 Gemini 驅動 Siri，但台上隻字未提 Claude 或 ChatGPT。該功能是在 iOS 27 開發者測試版的程式碼中被發現，而非出現在主題演講上，Apple 也未公開證實擴展功能是否會隨今年秋季的 iOS 27 推出。

對 Anthropic 和 OpenAI 而言，此架構代表一個重要的發行管道：若擴展功能推出，Claude 和 ChatGPT 可在 Siri 內部被呼叫，等於獲得觸及龐大活躍 Apple 裝置用戶群的發行管道。用戶是否真的會以有意義的規模使用這些替代選項，還是預設的 Gemini 體驗將吸引絕大多數查詢，目前仍是未知數。

## iOS 27：用戶層面的變化

所有 Apple 作業系統在本次發布中同步躍升至版本27：iOS 27、iPadOS 27、macOS Golden Gate、watchOS 27、tvOS 27 和 visionOS 27。版本號的統一，是 Apple 宣示軟體平台一致性的聲明。

對 iPhone 用戶而言，iOS 27 預期支援 iPhone 12 及更新機型。iPhone 11 預期將失去支援，用戶可能需要升級；實際情況應以 Apple 官方相容機型清單為準。新的 Gemini 驅動 Siri 和 Apple Intelligence 功能，需要 iPhone 15 Pro 或更新機型——清晰勾勒出升級的硬體誘因。

iOS 27 在 AI 改版之外的重要功能包括：為汽車廠商整合重新設計的 CarPlay 支援、具備 Flyover 視覺增強的升級版 Apple 地圖、健康 App 新增圍停經期與更年期追蹤，以及全系統性能優化（Apple 承諾 iPhone 12 時代的硬體在執行新系統後將有顯著速度提升）。

開發者測試版在主題演講後即刻上線，公開測試版預計7月中旬推出，正式版預計於2026年9月與 iPhone 18 系列一同發布。

## Tim Cook 的謝幕

WWDC 2026 是 Tim Cook 擔任 CEO 的第十五場，也是最後一場主題演講。Apple 公司帳面上，Cook 將過渡為執行董事長，並將執行長一職交給 John Ternus。

Gemini 交易是 Cook 留下的政治遺產，也在某種程度上是他對當前 AI 競賽格局最誠實的承認。多年來，他反覆強調 Apple 垂直整合——自製晶片、自建框架、自訓 AI 模型——是不可複製的結構性優勢。而他的離場，恰好以承認「雲端 AI 是無法獨力勝出的領域」為注腳。

每年10億美元的 Google 帳單不只是財報的一行數字。它是一個戰略表態：儘管 Apple 在 A 系列和 M 系列晶片上對端側 AI 投入了巨資，大規模推理的前沿依然在雲端，而雲端 AI 的領導者是 Google。與其競爭，不如建立在其上——這是 Cook 的最終算計。

## 對整個 AI 生態的意義

Apple 對 Gemini 的整合重塑了基礎模型市場的競爭格局。Google 現在擁有全球最具價值的兩大發行管道：自有的搜尋和助理平台，以及 Apple 超十億用戶的 iPhone 生態系。

對開發者而言，iOS 27 測試版中的 Extensions 框架顯示可能出現新的整合路徑，但 Apple 尚未確認是否會推出。據 Bloomberg 報導，Apple 已與 OpenAI、Anthropic 和 Google 討論過該框架的授權事宜。

對於台灣的用戶而言，iOS 27 最直接的變化是 Siri 終於能夠理解並真正「處理」複雜的繁體中文需求，而非僅依賴本機端的規則式判斷。但代價是：你的某些問題，現在由 Google 來回答。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 14 處。*
