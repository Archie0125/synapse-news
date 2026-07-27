---
title: "OpenAI 推出 ChatGPT Health，3 億用戶可接入個人醫療紀錄"
summary: "OpenAI 正式在全美推出 ChatGPT Health 功能，用戶可將 Apple Health、醫院病歷、One Medical 及 Peloton、MyFitnessPal 等健身應用程式連接至 ChatGPT。每週已有逾 3 億人透過 ChatGPT 詢問健康問題，此次更新讓 AI 對話首次得以接觸用戶的真實醫療數據，同時引發 HIPAA 隱私保護適用範圍的法律爭議。"
category: "products"
publishedAt: 2026-07-27
lang: "zh"
featured: false
trending: true
sources:
  - name: "OpenAI: Launching Health in ChatGPT"
    url: "https://openai.com/index/health-in-chatgpt/"
  - name: "gHacks: OpenAI Launches Health in ChatGPT"
    url: "https://www.ghacks.net/2026/07/25/openai-launches-health-in-chatgpt-for-us-users-connecting-apple-health-and-medical-records/"
  - name: "Startup Fortune: HIPAA analysis"
    url: "https://startupfortune.com/openai-launched-chatgpt-health-and-quietly-moved-your-medical-records-outside-hipaa/"
  - name: "9to5Mac: OpenAI relaunches Apple Health feature"
    url: "https://9to5mac.com/2026/07/23/openai-relaunches-apple-health-connected-chatgpt-feature-with-expanded-access/"
tags:
  - "openai"
  - "chatgpt"
  - "健康"
  - "apple-health"
  - "醫療紀錄"
  - "隱私"
  - "消費者ai"
relatedSlugs:
  - "2026-07-27-chatgpt-health-apple-health-medical-records-launch-en"
  - "2026-07-26-anthropic-claude-opus-5-launch-zh"
---

OpenAI 上週悄悄完成了消費者健康科技領域最具份量的產品動作之一：在全美正式推出 ChatGPT Health，讓所有 18 歲以上的已登入用戶能將真實病歷與 Apple Health 資料連接至 ChatGPT 對話。此功能橫跨 Free、Go、Plus、Pro 各個方案，透過網頁與 iOS 均可使用，而其影響早已超越單純的設定開關。

為什麼說這件事意義重大？數字說明一切。OpenAI 表示，每週已有逾 3 億人使用 ChatGPT 詢問健康相關問題。在此次功能推出前，這些對話全屬假設性質——ChatGPT 只能籠統討論症狀與藥物，無從得知眼前這個用戶的實際狀況。ChatGPT Health 從根本上改變了這一點。

## 可連接的數據來源

首版支援的數據範圍比多數觀察者預期的還要廣泛。用戶可連接：

**醫療紀錄：** 全美各大醫療院所、亞馬遜旗下初級醫療網絡 One Medical，以及主打全面預防性健診的會員制服務 Function Health。

**健身與生活方式平台：** Apple Health（iPhone 用戶的主要健康資料彙整平台）、MyFitnessPal（飲食與熱量記錄）、Peloton（運動與心肺數據）、Instacart（食品雜貨採購紀錄）、AllTrails（戶外活動）、Weight Watchers（飲食管理）。

一旦連接，ChatGPT 可取得藥物清單、檢驗報告、近期門診摘要、睡眠數據、活動量，以及各健康指標的長期變化。預想的使用情境包括：比對新舊檢驗結果的差異、摘要上次就診後的身體變化、或將睡眠與運動模式與自述症狀相互對照。

## 沒人大聲問的 HIPAA 問題

這次發布最值得關注的爭議，在主流報導中被低調帶過，卻在醫療政策與法律圈廣泛討論。OpenAI 並非 HIPAA 規定下的「受涵蓋實體」——美國醫療資料隱私法規定，只有醫療機構、健保公司等特定類型的機構需要遵守。當患者病歷從醫院系統進入 OpenAI 的基礎設施時，這份資料便不再受到與臨床環境相同的聯邦保護。

OpenAI 的回應是承諾：所連接的健康資料不會用於基礎模型訓練，也不會用於廣告定向。公司也對健康相關對話採用超出標準的額外加密保護。但「額外加密」是資安技術聲明，不是法律隱私聲明。這份資料的保護，靠的是 OpenAI 對用戶的合約承諾，而非 HIPAA 背後的聯邦執法機制。

對多數用戶而言，這個差別在實際使用中或許感受不到——讓 ChatGPT 根據自己的真實病史幫助解讀檢驗報告，確實有切實的價值。但對於帶有敏感診斷的患者——精神健康狀況、生殖健康、特定傳染病——缺乏正式 HIPAA 保障，是一個與他們可能以為的情況截然不同的事實。

## 為何選在此時推出

三個因素的匯合讓此次推出得以在 2026 年中期實現。

其一，Apple HealthKit API 的成熟度已大幅提升，第三方整合的可靠性遠勝兩年前，蘋果本身也有擴展健康生態系的動機。其二，聯邦互操作性規定要求多數美國主要醫療系統在 2023 年前開放 FHIR 格式的機器可讀患者資料，這讓 OpenAI 終於有了一套標準化的跨院所查詢方式，不必為每家醫院個別建置整合。其三，OpenAI 的企業營收成長讓公司看準健康與生命科學垂直市場，而消費端的健康功能是最有效率的能力展示途徑。

Instacart 的加入尤其值得關注。食品雜貨採購紀錄是出乎意料的敏感數據，能揭露飲食習慣、家庭組成與消費能力。從臨床角度，飲食數據確實有醫療意義；但從隱私角度，購物紀錄比步數更具識別性。

## 更大的競爭格局

ChatGPT Health 進入的是一個所有主要 AI 平台都在搶攻健康賽道的市場。Google 透過與主要醫療院所的夥伴關係，持續將健康能力整合至 Gemini。亞馬遜透過 One Medical 和 Amazon Clinic 有天然優勢。蘋果則走長期路線，透過 Apple Intelligence 將健康資料留存於裝置本地，同時透過 2024 年簽訂的正式協議與 OpenAI 合作。

OpenAI 的策略——接入已散落在各系統中的資料，帶入 3 億人已習慣使用的對話介面——可以說是目前最務實的近期策略。飛輪效應顯而易見：用戶分享越多健康脈絡，ChatGPT 對健康問題的回答就越有用，這又激勵用戶分享更多。這正是 2010 年代消費網路公司建立護城河的邏輯。

健康倡議人士正開始提出的問題是：數億人健康資料最終由誰掌控？若 OpenAI 的隱私承諾日後有所改變，問責機制又在哪裡？

## 現在能用什麼、接下來會有什麼

目前功能僅限美國，未公布國際上線時程。需要有效的 ChatGPT 帳號並完成年齡驗證（18 歲以上）。Apple Health 整合目前僅限 iOS，使用 Android 裝置或無 iPhone 的桌面用戶暫時無法使用。

OpenAI 尚未公布目前支援的醫院名單，僅以「美國醫療院所」概括，預計隨後續 FHIR 整合協議陸續簽署而擴展。One Medical 與 Function Health 已於首發完整整合。

至於是否會納入更多敏感類別——生殖健康追蹤、心理健康服務、藥物戒癮輔助工具——將是 OpenAI 如何在功能效益與最脆弱用戶隱私保護之間取得平衡的重要考驗。
