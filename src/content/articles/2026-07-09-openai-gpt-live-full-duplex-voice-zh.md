---
title: "OpenAI 推出 GPT-Live：能同時說話又能聆聽的全雙工語音模型"
summary: "OpenAI 於 7 月 8 日發布 GPT-Live-1 與 GPT-Live-1 mini，以全新世代的全雙工語音模型取代舊版 Advanced Voice Mode。這次發布標誌著語音介面成為主要運算入口的重要里程碑。"
category: "ai-ml"
publishedAt: 2026-07-09
lang: "zh"
featured: true
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/07/08/openai-releases-new-voice-models-for-more-natural-live-conversations/"
  - name: "OpenAI"
    url: "https://openai.com/index/introducing-gpt-live/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/openai-launches-gpt-live-a-full-duplex-voice-upgrade-that-lets-chatgpt-talk-more-like-a-person"
tags:
  - "OpenAI"
  - "ChatGPT"
  - "語音AI"
  - "GPT-Live"
  - "全雙工"
  - "對話式AI"
relatedSlugs:
  - "2026-07-09-openai-gpt-live-full-duplex-voice-en"
  - "2026-07-08-openai-us-government-stake-sovereign-wealth-fund-zh"
---

OpenAI 在台灣時間 7 月 9 日凌晨正式發布 GPT-Live，這是一個全新的語音模型家族，目標是讓與 AI 對話的體驗，從查詢資料庫進化為真正的人際互動。這次毫無預警的發布，以截然不同的底層架構取代了 ChatGPT 的舊版 Advanced Voice Mode，並為即時 AI 互動設立了新的競爭標竿。

## 真正的「聆聽」是什麼

GPT-Live 的核心技術突破，在於「全雙工」（full-duplex）音訊處理。過去的語音 AI 流程——包括 OpenAI 自家的方案——採循序執行的方式：先將語音轉為文字，送進語言模型，再輸出音訊。每個步驟都會累積延遲，而且系統在任意時刻只能「說」或只能「聽」，無法同時進行。

GPT-Live 徹底打破這道限制。新模型能同步處理輸入語音與產生輸出音訊，每秒做出多次互動決策：該說話、繼續聆聽、暫停、插入簡短的回應語氣詞，還是將查詢轉交給下游工具。最終呈現的效果，是一個能在使用者說話中途接話、無需等待停頓便能回應修正的系統——這種對話節奏過去只有真人才做得到。

「長遠來看，我們認為這將讓語音成為電腦運算的主要介面，」ChatGPT Voice 產品負責人 Atty Eleti 表示。「語音作為介面，而非功能」——這個定位揭示了 OpenAI 更長遠的野心。

## 兩款模型、分層取用

OpenAI 同時發布兩個版本。GPT-Live-1 mini 成為所有 ChatGPT 使用者的預設語音體驗，取代自 2024 年中便一直沿用的舊版 Advanced Voice Mode；GPT-Live-1 則是更強大的大型模型，提供給 Plus、Pro 和 Team 方案的付費訂閱者使用。

兩款模型均建構於 OpenAI 現行旗艦模型 GPT-5.5 之上。若遇到需要網路搜尋、深度推理或代理工具使用的問題，GPT-Live 會在背景悄悄交棒給 GPT-5.5，將結果無縫融入語音回覆中——無需強迫使用者切換到文字介面處理複雜查詢。

系統支援 30 至 40 分鐘的持續對話——相較於舊版語音模式經常在 10 分鐘內逾時，這是顯著的進步。語音回覆也能同步呈現圖表、參考圖片等視覺資訊。

## 為何此刻至關重要

GPT-Live 的發布時機絕非偶然。OpenAI 正與一票強勁對手賽跑，搶在 Google Gemini Live、升級版 Apple Siri，以及層出不窮的語音 AI 新創之前，確立語音領域的主導地位。

語音被普遍視為消費性運算的下一波重大介面革命，尤其在行動裝置領域更是如此。OpenAI 與 Apple CarPlay 的整合（同週宣布）顯示，GPT-Live 正在突破智慧型手機，進軍螢幕操作不切實際甚至危及安全的使用場景。CarPlay 整合意味著 GPT-Live 有望成為全球數億駕駛者的預設對話介面。

全雙工架構也為即時翻譯開啟大門——OpenAI 已確認此功能正在開發中。初期測試顯示，系統能以尚可接受的延遲進行跨語言即時傳譯，但 OpenAI 尚未廣泛開放此功能。

## 青少年安全護欄

OpenAI 在同一版本中也導入了適齡安全防護措施。對於通過驗證的青少年帳號，GPT-Live 會套用比成人更嚴格的內容過濾器與更保守的行為預設值。OpenAI 並未說明年齡驗證的具體執行方式——這個細節在大規模可靠年齡驗證仍屬難題的背景下，勢必引來監管機關的高度關注。

這套青少年安全機制恰好在監管壓力升高之際上線。歐盟 AI 法案已在全體 27 個成員國執行，要求可能與兒童互動的 AI 系統必須配備強化安全措施與揭露要求。就在 GPT-Live 發布前兩天，美國伊利諾州才剛通過自己的 AI 安全法，多個州也正考慮類似立法。

## GPT-5.6 的前哨戰

GPT-Live 的發布，被業界普遍解讀為鋪路之作。OpenAI 預計將在數週內推出旗艦文字模型 GPT-5.6 Sol。這次以語音優先的推出方式，似乎是為了暖身使用者，建立完整的產品敘事：旗艦模型搭配高度優化的專屬語音層。

追蹤 OpenAI 企業業務的分析師指出，能進行長時間、富含情境的語音對話，在客服、業務銷售和醫療健康領域特別具有價值。據悉，已有多家企業客戶正透過 Realtime API 測試 GPT-Live，該 API 向開發者開放了全雙工功能，可用於打造自訂語音代理。

## 競爭格局

Google Gemini Live 在 2026 年初廣泛推出，已累積數百萬月活躍用戶，並深度整合於 Android 裝置。Apple Intelligence 的強化版 Siri 預計隨 iOS 26.6 全面上線，將直接在同一塊語音對話市場上與 OpenAI 正面交鋒。Meta 也預告了 Ray-Ban 智慧眼鏡的語音功能，瞄準的是 OpenAI 和 Google 尚未直接涉足的「隨身環境運算」場景。

OpenAI 的反制論點是底層模型品質與生態系深度。GPT-Live-1 與 GPT-5.5 工具調用基礎設施的連結，意味著它能在口語對話過程中直接採取行動——起草電子郵件、搜尋網頁、設定提醒——而非只是回答問題。對於已深度嵌入 OpenAI 生態系的使用者而言，這種整合度代表著實質競爭優勢。

GPT-Live 是否足以在競爭對手追上之前鎖住語音優先的使用者，目前仍是未知數。可以確定的是，爭奪日常運算主要對話層的競賽已進入更快速的新階段——而 OpenAI 擺明要扮演領頭羊的角色。
