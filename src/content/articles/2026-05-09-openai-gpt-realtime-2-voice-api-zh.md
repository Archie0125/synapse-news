---
title: "OpenAI 發布 GPT-Realtime-2：首個能在對話中即時推理的語音 AI 模型"
summary: "OpenAI 於 5 月 7 日為其 Realtime API 發布三款新模型——具推理能力的 GPT-Realtime-2（128K 上下文視窗）、即時語音翻譯的 GPT-Realtime-Translate（支援 70 種以上語言），以及串流轉錄的 GPT-Realtime-Whisper。GPT-Realtime-2 是首個基於 GPT-5 等級智能的語音模型，開發者得以打造能在對話中思考複雜問題、無需陟入尷尬沉默的語音 AI 代理。"
category: "developer-tools"
publishedAt: 2026-05-09
lang: "zh"
featured: false
trending: true
sources:
  - name: "OpenAI Blog"
    url: "https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/openai-gpt-realtime-2-voice-models"
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/05/08/openai-releases-three-realtime-audio-models-gpt-realtime-2-gpt-realtime-translate-and-gpt-realtime-whisper-in-the-realtime-api/"
  - name: "Latent Space"
    url: "https://www.latent.space/p/ainews-gpt-realtime-2-translate-and"
tags:
  - "openai"
  - "語音AI"
  - "gpt-realtime-2"
  - "API"
  - "開發者工具"
  - "語音辨識"
  - "即時翻譯"
relatedSlugs:
  - "2026-05-08-openai-ai-phone-2027-mediatek-jony-ive-zh"
  - "2026-05-03-mistral-medium-35-vibe-remote-agents-zh"
  - "2026-04-24-openai-gpt-5-5-agentic-model-zh"
---

過去兩年，要打造一個能用於正式產品的語音 AI 代理，開發者必須將三個獨立服務拼湊在一起：語音轉文字、推理模型、再轉回語音輸出。結果往往是延遲高、銅接處容易出錯，使用者甚至能感覺到這些「縮走」的存在。 5 月 7 日，OpenAI 發布三款新模型，從根本改變了這個架構——同時也大幅提升了語音介面的能力上限。

這次發布的核心是 GPT-Realtime-2，OpenAI 首款基於 GPT-5 等級智能的語音模型。但整個發布其實是一套三件組：GPT-Realtime-2 主打智能語音互動，GPT-Realtime-Translate 提供即時多語言對話翻譯，GPT-Realtime-Whisper 則提供串流語音轉錄。三款模型即日起均可透過 Realtime API 取用。

## GPT-Realtime-2：會思考的語音

GPT-Realtime-2 最核心的能力，是在即時對話中進行推理——這是過去所有語音 AI 模型都沒能做好的事。此前的語音系統，包括 OpenAI 自家舊版 Realtime API 模型，都是以較小、較快、強調降低延遲的模型為基礎。它們能流暢對話、呼叫基本工具，但面對需要多步驟推理、細膚理解指令或長上下文的複雜請求時，往往力不從心。

GPT-Realtime-2 將語音轉語音的處理流程與 GPT-5 等級的推理能力整合進單一模型，從根本改變了這個局面。上下文視窗從 32K 擴展至 128K tokens，讓模型能夠維持更長的對話、回渆會話前段的內容，並處理隨時間累積大量上下文的代理式工作流程。

開發者可設定五個推理強度等級——minimal、low、medium、high、xhigh——讓應用程式根據任務需求在延遲與準確度之間靈活取捨。處理例行查詢的客服機器人或許只需 minimal；解析複雜症狀的醫療問診助理，則可能需要調高至 high 或 xhigh。

兩項新的開發者功能讓推理過程不再是沉默等待。**前置語句（Preambles）**讓模型在呼叫工具前先說出「讓我查一下」或「稍等一下」，消除了過去讓推理代理顯得「當機」的死寂空白。**平行工具呼叫（Parallel tool calls）**讓模型能同時觸發多個後端請求，並以語音告知目前執行進度，例如：「我正在同步查詢您的訂位資訊和目的地天氣。」

這些絕非裝飾性功能。語音使用者體驗研究一致顯示，無法解釋的沉默是導致使用者在語音互動中放棄的首要原因。讓模型的運作過程可聽見，能在推理延遲期間有效維持使用者的參與感。

## 定價與開發者的經濟帳

GPT-Realtime-2 定價為每百萬音訊輸入 tokens 32 美元、每百萬音訊輸出 tokens 64 美元，快取輸入 tokens 則降至每百萬 0.40 美元——對能夠重復利用對話上下文的應用程式而言，折扣相當可觀。

以參考値來看，一通典型的三分鐘客服電話大約產生 5,000 至 7,000 個音訊 tokens。以完整定價計算（未計快取），每通約需 0.23 至 0.45 美元。對高流量消費者應用而言，這個成本値得態態處理；但對於要取代每小時 20 至 40 美元真人客服的企業應用而言，幾乎在任何 token 用量下都具備可行的商業邏輯。

五個推理等級也讓開發者能夠精細控制成本。以 minimal 推理運行比 xhigh 便宜許多，且多數正式應用會發現 low 或 medium 推理已足以應付 80 至 90% 的查詢需求。

## GPT-Realtime-Translate：即時多語言對話

第二款模型 GPT-Realtime-Translate 專為即時語音翻譯而生。它支援超過 70 種語言的語音輸入，並能即時輸出 13 種語言的翻譯語音，跟上說話者的速度，而非等待完整句子結束後才開始翻譯。

實際應用場景相當廣泛。客服中心可將任何語言的來電即時轉換給英語客服人員處理，反之亦然，雙方都無需切換為文字模式或等待人工口譯。服務多語言病患的遠距醫療平台，可直接提供無語言障礙的即時問診。跨境派駐的外勤團隊可將模型作為永久在線的翻譯層，隨時溝通。

GPT-Realtime-Translate 依分鐘計費，而非按 token 計算，對通話時長可預測的應用來說，成本建模更為簡便。

## GPT-Realtime-Whisper：串流轉錄

第三款模型 GPT-Realtime-Whisper 针對一個相對聆焦但開發者頻繁提出的需求：逐字即時轉錄，而非等到整句說完才輸出。

過去的即時轉錄方案，讓開發者必須在兩個選項中取捨：低延遲的部分轉錄（但準確率較低，需要後續修正），或高準確度的完整轉錄（但延遲較高，與實際語音感覺脱節）。GPT-Realtime-Whisper 聲稱能打破這個取捨——透過串流輸出 token 機率而非等待句子完成後才確認文字，同時兑現速度與準確度。

同 GPT-Realtime-Translate，GPT-Realtime-Whisper 依分鐘計費。

## 對整個生態系統的意義

OpenAI 的 Realtime API 自 2024 年 10 月推出以來，在企業開發者中的採用率一直受限於推理能力的展。舊版模型能自然對話，但無法應付讓語音代理在正式環境中真正有用的複雜多輮工作流程。GPT-Realtime-2 是首個填補這個缺口的版本。

時機上，這與更廣泛的市場轉變相吸對應。Microsoft、Google 和 Amazon 都已表明，2026 年將大力投資企業級語音 AI 介面，對開發者心智份額的競爭也日益激烈。OpenAI 選擇同時發布 GPT-Realtime-2 與兩款配套模型（而非單一語音升級），顯示公司正試圖以統一的 API 介面握控語音開發者堆疊的全局——涵蓋智能對話、多語言翻譯和語音轉錄。

對於一直在等待語音 AI 能力足以應付複雜企業工作流程的開發者來說，這週的發布移除了最後一道主要的技術障礎。現在的開放問題不再是模型能力是否足夠強——而是定價與延遲取捨是否能通過各個具體應用場景的門溻。

根據多位企業開發者巡回報導的測試結果，GPT-Realtime-2 在 medium 推理強度下，典型查詢的延遲約在 800 至 1,200 毫秒之間——足以維持自然對話；但 xhigh 推理等級在處理複雜請求時會引入 2 至 4 秒的延遲，在期望即時回應的應用中，需要審慎設計使用者體驗。

這次三款模型的發布，是 OpenAI 語音平台自 2024 年推出以來最重要的演進，預計將加速語音 AI 代理在客戶服務、醫療保健與企業生產力應用中的正式部署——尤其在 2026 年下半年。
