---
title: "Google Gemini 3.1 Flash Live：即時多模態語音AI正式向開發者開放"
summary: "Google 發布 Gemini 3.1 Flash Live，一款支援低延遲音訊對話、螢幕分享互動與即時工具呼叫的語音與視覺模型，全程透過單一 API 完成。模型支援逾90種語言，在多步驟函式呼叫基準測試中拿下90.8%，現已透過 Google AI Studio 與 Vertex AI 的 Live API 向開發者開放。"
category: "ai-ml"
publishedAt: 2026-04-10
lang: "zh"
featured: false
trending: true
sources:
  - name: "Google DeepMind Blog"
    url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-live/"
  - name: "Google Developers Blog"
    url: "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-3-1-flash-live/"
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/03/26/google-releases-gemini-3-1-flash-live-a-real-time-multimodal-voice-model-for-low-latency-audio-video-and-tool-use-for-ai-agents/"
  - name: "eWeek"
    url: "https://www.eweek.com/news/google-gemini-3-1-flash-live-voice-ai-launch/"
tags:
  - "Google"
  - "Gemini"
  - "語音AI"
  - "多模態"
  - "即時AI"
  - "開發者工具"
  - "AI模型"
relatedSlugs:
  - "2026-04-04-google-gemini-everywhere-zh"
  - "2026-04-05-google-gemma-4-apache-license-zh"
  - "2026-04-05-google-turboquant-kv-cache-zh"
---

即時語音 AI 一直是生成式 AI 浪潮中最被冷落的環節——Demo 裡表現亮眼，上了生產環境就令人抓狂。延遲尖刺、口音辨識落差、僵硬的輪流對話、以及無法讀懂使用者情緒狀態，種種問題讓語音介面用起來更像在跟語音導覽系統說話，而非和一個自然的對話者互動。Google 於3月26日發布、現已向開發者與企業全面開放的 Gemini 3.1 Flash Live，是一次認真彌合這道鴻溝的技術嘗試。

## Gemini 3.1 Flash Live 是什麼

Gemini 3.1 Flash Live 是 Google 品質最高的即時音訊模型，專為持續性低延遲對話而設計，而非單輪轉錄任務。不同於傳統語音轉文字流程——將音訊轉錄成文字、送入語言模型、生成回應、再轉回音訊——Flash Live 直接在音訊串流上原生運作，保留了文字處理過程中會丟失的聲學細節。

模型支援逾90種語言的即時多模態對話。除音訊外，它還接受即時影片與螢幕分享輸入，讓使用者可以在說話的同時對著攝影機或分享螢幕——這為 AI 助理「親眼」看見你正在做什麼、並做出情境回應的應用場景打開了大門。

100萬 token 的上下文視窗，意味著對話不需要積極地摘要壓縮或截斷，對企業客服部署或需要長時間互動的代理人任務來說是實質改善。

## 基準測試數字

在 ComplexFuncBench Audio 基準測試上——這個測試專門衡量即時音訊環境下的多步驟函式呼叫能力——Gemini 3.1 Flash Live 拿下90.8%，超越包括前代模型在內的同類所有模型。對於構建需要根據語音指令呼叫 API、檢索資料或串接工具的語音代理人開發者而言，這個數字相當實在：它是代理人能可靠完成任務，還是在對話中途幻覺或失去指令脈絡之間的差距。

Google 同時報告了相較前代顯著改善的延遲表現。模型在「首字音訊延遲」這項指標上的設計，讓對話感覺自然流暢而非像在等待處理——這對語音模態的重要性，幾乎超過其他任何指標。

## 聲學細節感知與情緒回應

Google 特別強調的一項能力，是模型辨識「聲學細節」的能力——語調、節奏、重音以及受挫信號等情緒狀態線索的變化。模型能偵測使用者似乎感到困惑、沮喪或不確定，並動態調整回應風格：放慢語速、簡化用語，或主動承認難度所在。

這不是無足輕重的附加功能。大多數語音 AI 系統把每一句話都當成情緒中立來處理，當使用者明顯遇到困難時，回應往往顯得機械或缺乏同理心。Gemini 3.1 Flash Live 的聲學敏感度能否在不同口音、背景噪音環境和文化多樣性的使用者群體中持續表現，仍有待規模化驗證——但這個目標的野心，已把 Google 的語音 AI 帶入與純粹追求準確率的競品截然不同的維度。

## 內建安全機制：SynthID 音訊浮水印

Gemini 3.1 Flash Live 生成的每一段音訊，都嵌入了 Google 的 SynthID 浮水印——一種在生成時植入、人耳無法察覺的信號，事後可透過 Google 的驗證工具偵測。隨著 AI 生成語音越來越難與人聲區分，浮水印對於信任建立和來源追溯的重要性正與日俱增。

對企業部署的實際意涵不容小覷。客服中心、客戶體驗平台和語音類消費者應用，都面臨 AI 揭露義務的法規壓力。SynthID 音訊浮水印提供了一種技術機制，能夠證明 AI 生成的內容具有可追溯性，即便終端使用者無從感知。

## 開發者生態與整合方式

開發者可透過 Google AI Studio 與 Vertex AI 的 Live API 存取此模型。Live API 專為串流互動設計——採用長連線的 WebSocket，維護工作階段狀態、優雅處理中斷，並允許使用者在說話途中插嘴，而非等待輪流信號。

Gemini 3.1 Flash Live 同時整合了消費者端的即時對話產品 Gemini Live，已在全球200多個國家上線。為開發者 API 提供動力的模型，就是使用者在 Search Live 和 Gemini 應用語音模式中互動的同一個模型。這種架構統一性，意味著在生產規模測試中的改進會回流到開發者工具，而開發者基於 API 構建的創新也有機會出現在消費者產品中。

## 競爭格局

Gemini 3.1 Flash Live 進入的是一個競爭明顯加劇的語音 AI 市場。OpenAI 的即時音訊 API（由原生支援音訊的 GPT-4o 驅動）在2024年驗證了這條路的可行性，此後已整合進越來越多的企業應用。Anthropic 尚未推出原生音訊模型，但 Claude 的文字能力正越來越多地透過合作夥伴的語音介面被存取。ElevenLabs、Hume AI 和 Cartesia 則都在語音合成和對話式語音代理人領域競逐。

Google 的優勢不容忽視：基礎設施規模、與 Android 和 Chrome 生態系的深度整合、多語言訓練資料的廣度，以及透過 Search 和 Workspace 觸及數十億現有用戶的能力。Gemini 3.1 Flash Live 的推出，代表 Google 給想構建語音原生 AI 體驗的開發者的產品跳升了一個量級——也是一個信號：那個被承諾多年的即時、永遠線上 AI 助理，可能終於已經唾手可得了。

對正在規劃2026年 AI 佈局的企業而言，語音互動不再只是邊緣用例，它正在成為主要介面。而 Gemini 3.1 Flash Live，是迄今最清晰的訊號：底層模型已經準備好了。
