---
title: "OpenAI 發布 GPT-Realtime-2：語音 AI 終於學會思考"
summary: "OpenAI 透過 Realtime API 推出三款全新即時音訊模型——GPT-Realtime-2、GPT-Realtime-Translate 與 GPT-Realtime-Whisper，首度將 GPT-5 等級的推理能力導入低延遲語音互動，劍指客服中心與即時翻譯等數十億美元市場。"
category: "products"
publishedAt: 2026-05-15
lang: "zh"
featured: false
trending: false
sources:
  - name: "OpenAI"
    url: "https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/07/openai-launches-new-voice-intelligence-features-in-its-api/"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/openai-gpt-realtime-2-voice-models"
  - name: "Dataconomy"
    url: "https://dataconomy.com/2026/05/08/gpt-realtime-2-expands-openais-voice-intelligence-capabilities/"
tags:
  - "OpenAI"
  - "語音AI"
  - "API"
  - "即時音訊"
  - "GPT-Realtime-2"
relatedSlugs:
  - "2026-05-13-elevenlabs-500m-series-d-voice-ai-zh"
  - "2026-05-14-openai-daybreak-cybersecurity-gpt55-zh"
---

語音 AI 的問題從來不是「聲音」本身，而是聲音背後的「思考」——答話前那段令人不自在的空白、在長時間通話中丟失脈絡，以及當使用者插話或突然換話題時，系統那副不知所措的模樣。OpenAI 這次的新發布，正是針對這個核心缺口而來。

2026 年 5 月 7 日，OpenAI 透過 Realtime API 推出三款全新模型：GPT-Realtime-2、GPT-Realtime-Translate 與 GPT-Realtime-Whisper。三者合在一起，構成自 2024 年底 Realtime API 首次亮相以來最重大的語音 AI 基礎設施升級，也是第一次將 GPT-5 等級的推理能力與低延遲語音介面真正整合在一起。

## GPT-Realtime-2：語音遇上大腦

這次發布的旗艦模型是 GPT-Realtime-2，OpenAI 將其定位為「最先進的語音推理模型」。核心突破在於將 GPT-5 等級的推理直接整合進針對即時語音互動優化的模型中。過去的語音模型將推理與音訊處理分拆在兩個管線，在接縫處引入延遲與上下文耗損。GPT-Realtime-2 原生支援兩者，一氣呵成。

上下文視窗從上一代的 3.2 萬 token 大幅擴展至 12.8 萬 token，讓語音代理在不丟失早期對話的情況下，能維持更長的通話記憶。以客服場景為例，這意味著代理能在同一通電話中引用 45 分鐘前客戶提供的資訊，而不需要對方重複說明。

在基準測試方面，模型在 Big Bench Audio Intelligence 上拿下 96.6% 的成績——涵蓋語音互動中的理解、推理與一致性評估。相比前代 GPT-Realtime-1.5，同一基準提升了 15.2%。

模型也為真實世界的對話亂流做好了準備：支援多位講者同時發言、在被打斷後不失方向，以及在句中優雅地接受語意修正。這些正是讓目前這代 AI 電話客服聽起來像機器人的關鍵失敗點——一被打斷就重頭再來，而不是順勢調整。

定價為每百萬 audio input token 32 美元，每百萬 output token 64 美元，快取輸入享有折扣價 0.40 美元。以一般 10 分鐘客服電話產生的約 15,000 至 20,000 token 估算，每通電話的 audio input 成本遠低於 1 美分——相比真人客服的人力成本幾乎微不足道。

## GPT-Realtime-Translate：70 種語言即時口譯

第二款模型 GPT-Realtime-Translate 瞄準的是即時多語言翻譯市場——過去幾年 Interpreter.ai 和 KUDO 等公司一直在耕耘的領域。

模型可接受 70 多種語言的音訊輸入，同步翻譯成 13 種輸出語言，且能跟上真人說話的語速。過去的系統往往要等到說話者說完一個完整句子才開始翻譯，造成明顯延遲；若改用增量翻譯又容易在說話者臨時改口時輸出錯誤。

OpenAI 的解法是串流架構——先輸出暫定譯文，再隨著更多上下文到來即時修正，而不是等句子結束才一次輸出。根據早期存取開發者分享的演示，結果近乎同步翻譯，聽感遠比傳統口譯系統的兩拍節奏自然。

定價為每分鐘 0.034 美元，遠低於專業人工口譯通常的每分鐘 2 至 4 美元。

## GPT-Realtime-Whisper：比人類打字還快

第三款模型 GPT-Realtime-Whisper 定位為即時轉錄與字幕引擎，適用場景涵蓋會議、法律程序、媒體製作與無障礙輔助。

OpenAI 聲稱這款模型的轉錄速度超過大多數人類打字速度，在嘈雜環境或非標準口音下仍能維持低字詞錯誤率。不同於在事後處理音訊檔案的批次轉錄 API，GPT-Realtime-Whisper 專為串流設計，從語音到顯示文字的延遲低於 300 毫秒。

對聽障輔助字幕而言，這個延遲差距至關重要。300 毫秒的延遲在人類感知上幾乎是同步；舊一代即時字幕系統常見的 1.5 至 3 秒延遲，則明顯讓人覺得字幕與說話者脫節。

## 市場機會有多大

這次發布的矛頭明確指向客服中心市場——OpenAI 估計全球約有 1,500 萬個客服坐席。GPT-5 級推理加上低延遲音訊的組合，意味著 AI 語音代理首次有能力處理真正複雜的查詢：不只是轉接電話或回答常見問題，而是解釋爭議保險理賠、引導客戶完成技術排障，甚至協商還款方案。

ElevenLabs 今年 5 月以 50 億美元估值完成 5 億美元融資，可能感受到最直接的競爭壓力。它的語音合成技術仍是業界一流，但 GPT-Realtime-2 的推理能力搭配 OpenAI 的模型發行網絡，為開發者提供了整合單一 API 的強力誘因，不必再把 OpenAI 推理和 ElevenLabs 語音拼接在一起。

即時翻譯市場的小型玩家——Interprefy、Kudo、Wordly——面臨類似的結構性壓力。每分鐘報價若無法在精準度上比肩 GPT-Realtime-Translate 的 0.034 美元，企業合約在到期續約時就會面臨直接挑戰。

## 下一步

OpenAI 在發布時確認，GPT-Realtime-2 已開始為 ChatGPT 語音模式提供支撐，取代了先前的語音管線。公司也表示，企業自動化產品「workspace agents」將可透過 GPT-Realtime-2 接收語音指令，讓純粹的口語命令足以觸發複雜的多步驟自動化工作流程。

這勾勒出的願景不只是更聰明的電話客服。而是代理 AI 時代的語音介面：說話，不再只是為了方便，而是人類指揮複雜自動化工作的主要方式。
