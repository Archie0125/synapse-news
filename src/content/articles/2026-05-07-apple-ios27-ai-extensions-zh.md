---
title: "蘋果 iOS 27 開放 AI 選擇權：用戶可自選 Gemini、Claude 等第三方模型"
summary: "蘋果計劃在 iOS 27 中推出「Extensions」框架，允許用戶在 Siri、Writing Tools 及 Image Playground 中自由切換 Google Gemini、Anthropic Claude 等第三方 AI 模型。這是蘋果在 AI 開放策略上的最大轉向，也預示著一場在全球最大消費裝置平台上的 AI 生態戰爭。"
category: "products"
publishedAt: 2026-05-07
lang: "zh"
featured: false
trending: true
sources:
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-05-05/ios-27-features-apple-plans-to-let-users-swap-models-across-apple-intelligence"
  - name: "9to5Mac"
    url: "https://9to5mac.com/2026/05/05/ios-27-will-let-you-choose-between-gemini-claude-and-more-for-ai-features-report/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/05/apple-plans-to-make-ios-27-a-choose-your-own-adventure-of-ai-models/"
tags:
  - "蘋果"
  - "iOS 27"
  - "Apple Intelligence"
  - "Gemini"
  - "Claude"
  - "Siri"
  - "AI 模型"
relatedSlugs:
  - "2026-04-11-apple-ios264-siri-gemini-rollout-zh"
  - "2026-04-07-apple-ios26-sdk-msca-zh"
  - "2026-04-26-apple-john-ternus-ceo-tim-cook-succession-zh"
---

蘋果正在籌備一場影響深遠的 AI 策略轉型。根據彭博社本週的報導，即將在 6 月 8 日 WWDC 上亮相的 iOS 27、iPadOS 27 與 macOS 27，將引入全新的「Extensions」框架，讓用戶能自行選擇要在 Apple Intelligence 中使用的 AI 模型，包括 Google Gemini、Anthropic Claude 等第三方服務。

這對一向以封閉生態聞名的蘋果而言，是相當罕見的開放姿態。距離蘋果以隱私優先為訴求推出 Apple Intelligence 還不到兩年，公司似乎已承認一個現實：用戶想要選擇權，而蘋果再也無法單靠自家模型撐起整個 AI 體驗。

## Extensions 框架如何運作

Extensions 的核心是在 Apple Intelligence 內建立一個 AI 路由層。只要用戶從 App Store 安裝了 Gemini 或 Claude 等應用程式，這些 App 就會自動出現在 Siri、Writing Tools 和 Image Playground 的可選引擎清單中。撰寫郵件時，用戶可以選擇讓 Anthropic Claude 處理潤稿工作，而非蘋果內建模型；使用 Image Playground 時，也可以改用 Gemini 的圖像生成能力。

更值得注意的是語音個人化設計。系統將為蘋果自身回應和第三方模型的回應分別配置不同的 Siri 聲音，讓用戶能從音頻上辨別目前是哪個 AI 在說話。這是應對多模型裝置「身份辨識」問題的巧妙 UX 解法。

Siri 本身並不會被取代，蘋果似乎仍有意讓它扮演預設的「指揮調度」角色。但訊號已經很清楚：Siri 將成為一個介面，而非大腦。

## 蘋果為何選在此時開放

時間點絕非偶然。Apple Intelligence 在 2024 年底上市以來評價平平，始終未能跟上 OpenAI、Google 和 Anthropic 快速迭代的腳步。在複雜寫作、程式碼生成與圖像生成等任務上，能力差距已讓一般用戶有感。

法規壓力也是關鍵因素。歐盟《數位市場法》已迫使蘋果開放 iOS 的瀏覽器引擎，AI 模型選擇權符合同樣的監管邏輯。主動開放讓蘋果能按自己的條件設計整合方式，而非等待布魯塞爾或美國未來法規的強制要求。

商業考量同樣不可忽視。Apple Intelligence 對 iPhone 16 和 iPhone 17 的換機吸引力本就有限。一個能把全球最頂尖 AI 模型無縫整合進 iOS 的框架，同時保留蘋果在隱私保護和端側運算上的獨特優勢，才是真正有說服力的升級理由。

## 平台生態的賭注

對 Google 和 Anthropic 而言，Extensions 框架是一個千載難逢的發行管道。進入全球逾二十億台蘋果裝置的 AI 預設層，其戰略價值遠超任何獨立 App 的上架。兩家公司與蘋果早有淵源：Gemini 已為 iOS 26.4 的 Siri 後端提供支援，Claude 也透過類 ChatGPT 擴充套件在現有版本中可用。此次在 OS 層級正式化整合，將大幅鞏固雙方的合作關係。

彭博報導中沒有提到 OpenAI，但這或許反映的是談判時程問題，而非永久排除。自 2024 年 WWDC 宣布 ChatGPT 整合以來，OpenAI 與蘋果的關係就時有摩擦，加上 OpenAI 近期積極布局自有 AI 手機硬體，競爭關係更加緊張。

對於規模較小的 AI 新創來說，Extensions API 可能帶來轉機，也可能是殘酷的篩選機制。設計良好的整合介面，理論上能讓專業領域模型（如程式碼助手、多語言工具、法律寫作模型）直接觸及 iPhone 用戶。然而蘋果歷來讓第三方整合保持足夠高的門檻，App Store 審核流程很可能以新的形式成為守門人。

## 隱私架構的難題

最關鍵的問題，是蘋果如何在開放性與隱私之間取得平衡。現行的 Apple Intelligence 架構核心賣點是「資料不離開裝置」或透過蘋果伺服器作為隱私中介。但若底層模型是 Google 或 Anthropic 的雲端服務，這個論述就難以維持。

蘋果很可能會要求 Extensions 合作夥伴在 App Store 審核環節簽署嚴格的資料處理條款，這與 HealthKit、HomeKit 等敏感資料框架的做法如出一轍。但當 AI 推論實際上在第三方伺服器執行時，蘋果向消費者傳達的隱私承諾將不可避免地需要重新定義。

這是蘋果在 WWDC 前必須解決的核心矛盾。隱私架構的說明方式，將決定 Extensions 究竟被外界視為 Apple Intelligence 的升級，還是一種退讓。

## WWDC 的觀察重點

蘋果全球開發者大會將於 6 月 8 日在庫帕提諾 Apple Park 登場。Extensions 框架若如報導所言，將是主要亮點之一，與之並列的預計還有 iOS 27 的多項新功能、強化端側推理能力的全新 Siri，以及下一代蘋果晶片的 AI 能力預覽。

開發者社群的反應至關重要。若蘋果將 Extensions 限制在少數特定夥伴，或將設定入口藏得過深，實際影響將相當有限。但若框架真正開放且顯眼，iOS 有望成為全球每家主要 AI 實驗室的首選部署平台，進而重塑整個 AI 模型產業的商業邏輯。

無論如何，蘋果獨自主導 AI 生態的時代，已然結束。
