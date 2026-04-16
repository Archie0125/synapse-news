---
title: "微軟發布三款自研 AI 模型，宣告戰略去 OpenAI 依賴"
summary: "微軟 MAI 超級智慧團隊於 4 月 2 日發布 MAI-Transcribe-1、MAI-Voice-1 及 MAI-Image-2，正式在語音辨識、語音合成與圖像生成領域向 OpenAI 和 Google 發起挑戰。這場由 Mustafa Suleyman 主導的技術獨立宣言，標誌微軟 AI 策略的根本性轉變。"
category: "developer-tools"
publishedAt: 2026-04-05T09:50:00Z
lang: "zh"
featured: true
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/"
  - name: "Microsoft AI 官方部落格"
    url: "https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/microsoft-mai-models-openai-independence"
tags:
  - "微軟"
  - "MAI"
  - "基礎模型"
  - "語音辨識"
  - "圖像生成"
  - "Mustafa Suleyman"
  - "OpenAI"
relatedSlugs:
  - "2026-04-04-openai-gpt5-leak-zh"
  - "2026-04-04-cursor-devin-war-zh"
  - "2026-04-05-google-gemma-4-apache-license-zh"
---

過去五年，微軟的 AI 戰略可以用兩個字概括：押注 OpenAI。130 億美元的投資，以及 GPT 模型深度嵌入 Microsoft 365、Azure 和 Copilot，讓這家雷德蒙德巨頭成為 OpenAI 技術最強大的分銷商——但同時也讓自己對一個野心日益膨脹的合作夥伴形成了危險的單點依賴。2026 年 4 月 2 日，這個格局開始改變。

微軟 MAI 超級智慧團隊（MAI Superintelligence team）一口氣發布了三款自研基礎模型：MAI-Transcribe-1、MAI-Voice-1 與 MAI-Image-2，即日起透過 Azure Foundry 及全新的 MAI Playground 對外開放。這三款模型直接對標 OpenAI 的 Whisper 和 GPT-Transcribe（語音辨識）、ElevenLabs 的 Scribe 和 OpenAI 語音 API（音訊生成），以及圖像生成領域的眾多競爭者。在微軟提供的主要基準測試中，三款模型均聲稱躋身前三名。

## 三款模型詳解

**MAI-Transcribe-1** 是微軟的語音轉文字模型，專為微軟產品中使用最頻繁的 25 種語言而訓練。在 FLEURS 基準測試中，它在這 25 種語言上的平均詞錯率（WER）達到 3.8%，同時比微軟原有的 Azure Fast 方案快 2.5 倍。根據微軟公布的對比數據，MAI-Transcribe-1 在全部 25 種語言上優於 OpenAI 的 Whisper-large-v3，在 22 種語言上超越 Google Gemini 3.1 Flash，並在 15 種語言上壓制了 OpenAI 的 GPT-Transcribe 與 ElevenLabs 的 Scribe v2。

定價每小時 0.36 美元，與 AWS Transcribe 相當，並略低於 OpenAI Whisper API。

**MAI-Voice-1** 是文字轉語音模型，能在一秒鐘內生成 60 秒的自然語音，並支援從短音訊樣本訓練自訂語音。定價每百萬字元 22 美元，低於 ElevenLabs 的企業版方案。早期測試者特別稱讚其在技術性內容上的韻律表現——這向來是競爭模型的軟肋。

**MAI-Image-2** 是三款中最成熟的一款，代表微軟自研圖像生成模型的第二代。公司表示，MAI-Image-2 在 Arena.ai 排行榜上位居前三，生成速度比上一代在 Foundry 和 Copilot 上快至少兩倍。定價為文字輸入每百萬 token 5 美元、圖像輸出每百萬 token 33 美元，在同等品質層級下低於 OpenAI 的 DALL-E 3。

## Suleyman 的新使命

這三款模型是微軟 MAI 超級智慧團隊最具代表性的成果。該團隊由微軟 AI 執行長 Mustafa Suleyman 領導，於 2025 年 11 月正式成立宣布。Suleyman 是 Google DeepMind 的聯合創辦人之一，2024 年 3 月加入微軟擔任 Copilot 負責人；2026 年 3 月內部重組後，他卸下 Copilot 日常業務，將全部精力集中在前沿模型研發上。

這次重組耐人尋味。讓 Suleyman 從 Copilot 產品職責中解放出來，意味著微軟將第一方模型研發視為戰略優先事項，而非產品層面的實驗。業界分析師指出，從團隊宣布成立到生產級 API 上線，僅歷時約五個月，這是近年任何主要科技實驗室中最快的從 0 到 1 記錄之一。

微軟在官方部落格中寫道：「這些模型代表我們在 AI 基礎設施方式上的根本性轉變。開發者理應在 Foundry 中擁有世界級的原生選擇，而不僅僅是第三方 API 的入口。」

## OpenAI 的陰影

微軟此次發布的時機，無法脫開其與 OpenAI 微妙關係的背景來解讀。微軟仍是 OpenAI 最大的外部投資方和雲端合作夥伴，雙方在 Copilot、Azure OpenAI Service 和 Microsoft 365 生態系中依然緊密耦合。然而，OpenAI 的 8,520 億美元估值、傳聞中最早 2026 年底的 IPO 計畫，以及它對企業軟體市場的積極進攻，使兩家公司的利益衝突愈發明顯。

微軟悄悄建立 AI 備援能力已逾一年。2025 年底推出的 Phi-4 是它在小型高效模型上的佈局，而此次 MAI 多模態套件則是它在能力層面的回應。兩者合力構成一套理論上可以完全不依賴任何 OpenAI API 運作的技術堆疊——儘管微軟並未表示有意拆解現有合作協議。

更直接的戰略目標，似乎是定價談判籌碼與供應鏈安全。當你手中握有具競爭力的自研模型，你便擁有了在談判桌上的選項，而這在你完全依賴單一供應商的路線圖和定價決策時是根本不存在的。

## 開發者反應

在 X（前 Twitter）和 Hacker News 上，開發者社群對這次發布整體反應正面，其中對 MAI-Transcribe-1 多語言準確性的評價尤為熱烈。多位深耕東南亞和中東市場的開發者表示，Whisper 在泰語、泰米爾語和阿拉伯語上的表現長期令人頭疼，而 MAI-Transcribe-1 的早期測試顯示出顯著改善。

一個普遍的顧慮是供應商鎖定問題。微軟目前僅透過 Azure Foundry 和 MAI Playground 提供這些模型，沒有開放權重，也沒有上架 Hugging Face 或支援第三方推理端點。對於已在 Azure 上建立基礎設施的開發者而言這無關緊要，但對那些使用 AWS Bedrock 或獨立推理服務的開發者來說，這是一個不小的限制。

MAI Playground 的介面設計被不少使用者拿來與 OpenAI 的 Playground 相比，語音測試介面的完成度獲得好評——包含即時波形回饋，以及 OpenAI 介面所沒有的並排語音比較工具。

## 下一步走向

Suleyman 對 MAI 未來規劃一貫謹慎，但現有發布的邏輯已指向幾個明顯的後續方向。大型語言模型是目前最顯眼的空缺——微軟目前在文字生成上仍依賴 OpenAI GPT 系列和自家的 Phi 系列。MAI 是否最終會推出一款前沿推理模型，將是衡量這個團隊真實野心的試金石。

就現階段而言，語音辨識、語音合成和圖像生成這三個模態涵蓋了文字生成以外最具商業價值的能力，讓微軟得以一種 12 個月前還無法做到的方式，向企業開發者呈現一個全棧 AI 平台的面貌。傳遞給開發者社群——以及 OpenAI——的訊號已經足夠清晰：微軟正在為技術自主而建設，而且速度比所有人預期的都快。
