---
title: "iOS 26.5 正式確認：RCS 跨平台訊息將支援端對端加密（Beta），iPhone 與 Android 對話終於受到保護"
summary: "蘋果釋出 iOS 26.5 候選版本（RC），確認「訊息」App 將透過支援的電信業者提供端對端加密的 RCS 訊息（Beta 版）。此次更新還包含地圖「附近熱門地點」推薦，以及 Pride Luminance 桌布。"
category: "products"
publishedAt: 2026-05-06
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: false
sources:
  - name: "9to5Mac"
    url: "https://9to5mac.com/2026/05/04/apple-confirms-ios-26-5-messages-app-adds-rcs-end-to-end-encryption/"
  - name: "MacRumors"
    url: "https://www.macrumors.com/2026/05/05/ios-26-5-three-new-iphone-features/"
  - name: "Privacy Guides"
    url: "https://www.privacyguides.org/news/2026/05/05/apple-confirms-rcs-e2ee-will-ship-with-ios-26-5/"
tags:
  - "蘋果"
  - "iOS 26.5"
  - "RCS"
  - "端對端加密"
  - "訊息"
  - "隱私"
  - "Android"
relatedSlugs:
  - "2026-05-05-wwdc-2026-preview-ios27-siri-gemini-zh"
  - "2026-05-06-apple-ios-265-rcs-end-to-end-encryption-en"
---

蘋果已釋出 iOS 26.5 候選版本（Release Candidate），其發行說明確認了隱私社群等待多年的功能：iPhone 與 Android 裝置之間的 RCS 訊息將支援端對端加密。

此次更新預計將於下週釋出。與重大 iOS 版本相比規模較小，卻標誌著全球逾十億 iPhone 用戶與另一半智慧型手機市場之間的溝通方式，迎來真正的轉捩點。

## RCS 端對端加密的真正意義

蘋果在 iOS 18 時為「訊息」App 加入 RCS（Rich Communication Services）支援，取代了 iPhone 與 Android 之間老舊的 SMS 協定。RCS 帶來了已讀回條、正在輸入指示、高畫質多媒體分享及表情回應——這些功能 iMessage 用戶早已習以為常。但 RCS 當時缺少的，是隱私保護。

標準 RCS 訊息不同於兩台 iPhone 之間的 iMessage，並未加密。這意味著電信業者，乃至任何截取傳輸內容的人，理論上都能讀取訊息內容。蘋果的「訊息」App 將這類對話標示為綠色氣泡，加密缺口是藍色氣泡（iMessage）與綠色氣泡（RCS）之間的重要差異。

iOS 26.5 改變了這一切。根據蘋果的官方確認和 RC 發行說明，端對端加密 RCS 將以 Beta 版形式透過支援的電信業者推出，並隨時間擴大覆蓋範圍。

GSMA 於 2025 年 3 月發布 Universal Profile 3.0，並隨之推出基於 MLS 標準的 RCS 端對端加密，但目前尚不清楚蘋果將支援哪些具體功能。這一點很重要：該標準並非蘋果私有。Google Messages 採用的是自家基於 Signal 協定的加密，且電信業者也必須支援新的加密，此功能才能運作。

## 為何花了這麼長時間

延遲並非蘋果技術上的猶豫。RCS 端對端加密需要三個條件同步到位：GSMA 完成跨平台標準的定案、電信業者更新基礎設施以路由加密流量，以及雙方手機廠商實作相容的用戶端。蘋果一直積極參與制訂此標準的 GSMA 工作組。

電信業者的依賴性，正是 iOS 26.5 說明「將陸續推出」而非即時全面啟用的原因——尚未完成基礎設施升級的電信業者，其用戶將無法使用此功能，直到業者完成更新。

## 其他新功能：地圖推薦

除了 RCS 加密這項重點功能，iOS 26.5 還包含蘋果在發行說明中強調的另外兩項功能：

**地圖「附近熱門地點」推薦**：地圖 App 會根據附近的熱門趨勢及用戶近期搜尋記錄顯示推薦。今年稍後，此區塊將開始在美國與加拿大出現廣告。蘋果的實作盡可能在裝置端處理，以減少隱私曝露。

## 更大的隱私背景

iOS 26.5 推出的時間點，正值加密通訊從小眾關注升級為主流議題之際：Musk v. Altman 訴訟讓數據控制與 AI 訓練問題登上各大媒體；全球政策制定者正在辯論政府對通訊內容應有多少存取權；Mandiant 的研究也指出，AI 生成的釣魚攻擊已在測試中超越人工紅隊的表現。

RCS 跨平台端對端加密無法解決上述所有問題，但它確實大幅提升了普通用戶日常通訊的基礎安全水準。當一個 iPhone 用戶傳訊息給使用 Android 的家人，這段對話可以被加密，讓蘋果或任何第三方都無法攔截讀取——前提是雙方裝置和業者都支援此功能。

蘋果長期以消費者隱私為品牌核心。iOS 26.5 是一次行銷話語背後有真實技術承諾的更新。綠色氣泡，終於有了真正的隱私。

## RC 之後，接下來怎麼走

iOS 候選版本通常在公開發布前約一週釋出。若 RC 階段未發現重大問題，用戶可預期在 2026 年 5 月 11 日當週收到更新推送。RCS 端對端加密被標示為 Beta 版，將隨時間透過支援的電信業者陸續推出。

距離 6 月的 WWDC 2026 開幕在即，iOS 26.5 是 iOS 27 預覽之前的最後一次重要更新——讓蘋果的發布節奏維持在軌道上，為秋季公告周期做好準備。根據早前報導，iOS 27 將以多模態新世代 Siri 為核心，帶來更深度的 AI 整合。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 15 處。*
