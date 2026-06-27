---
title: "Google Gemini 2.5 Deep Think 橫掃數學、科學與推理基準，登上全球之冠"
summary: "Google 於 6 月 22 日推出 Gemini 2.5 Pro Deep Think 模式，在 MMLU-Pro 拿下 89.8%、GPQA Diamond 達 82.4%，全面超越 Anthropic Fable 5 與 OpenAI GPT-5.5。這款採用平行推理架構的模型現已對 Google AI Ultra 訂閱者開放，開發者 API 存取即將到來。"
category: "ai-ml"
publishedAt: 2026-06-27
lang: "zh"
featured: false
trending: true
sources:
  - name: "Google Blog"
    url: "https://blog.google/products-and-platforms/products/gemini/gemini-2-5-deep-think/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/ai/google-releases-olympiad-medal-winning-gemini-2-5-deep-think-ai-publicly-but-theres-a-catch"
  - name: "Engadget"
    url: "https://www.engadget.com/ai/google-introduces-the-deep-think-reasoning-model-for-gemini-25-pro-and-a-better-25-flash-174531020.html"
tags:
  - "google"
  - "gemini"
  - "deep think"
  - "推理模型"
  - "基準測試"
  - "ai-ml"
relatedSlugs:
  - "2026-06-27-openai-gpt56-sol-terra-luna-preview-zh"
  - "2026-06-27-five-eyes-ai-cyber-threat-warning-zh"
  - "2026-06-26-google-gemini-talent-exodus-adler-pritzel-anthropic-zh"
---

過去幾個月，前沿 AI 實驗室之間的基準大戰大多是以微幅進步換取排行榜上的幾個百分點。2026 年 6 月 22 日，Google 用一次發布打破了這種節奏——這次不只在單一任務上領先，而是同時橫掃科學、數學與推理三大類別。

**Gemini 2.5 Pro Deep Think** 是 Google DeepMind 迄今公開推出的最強大模型。它的進步並非單純靠更大規模的訓練，而是在推理過程中引入了一種根本性的新計算模式：延長的、平行化的推理（inference-time compute）。

## Deep Think 究竟做了什麼

Deep Think 不是「算更久的 Gemini」。它是一套改變模型面對困難問題方式的架構。啟動後，Gemini 2.5 Pro 會同時生成多條思維鏈——平行探索不同的解題路徑——再收斂至最終答案。配合新型強化學習技術，模型的逐步推理能力還能隨時間持續改進。

實際效果在基準分數上一覽無遺。在涵蓋 57 個學科研究生程度問題的 **MMLU-Pro** 上，Gemini 2.5 Pro Deep Think 拿下 **89.8%**，是目前所有公開模型中的最高分。在考驗物理、化學、生物博士級知識的 **GPQA Diamond** 上，它達到 **82.4%**，超越 Anthropic Fable 5（79.1%，現已遭美國政府暫停存取）和 OpenAI GPT-5.5（76.3%）。

在持續更新以防資料污染的競技程式設計基準 LiveCodeBench V6，以及難度登峰造極的 Humanity's Last Exam 上，Deep Think 同樣名列前茅。

## 國際數學奧林匹亞的里程碑

最令人印象深刻的能力展示來自數學領域：Gemini 2.5 的進階研究版本，在 2025 年國際數學奧林匹亞（IMO）中達到了**金牌水準**。IMO 考驗的是頂尖數學家才具備的創意解題能力，這種層次的成就——即便是在研究環境中——標誌著機器推理能力的真正轉折點。

消費者版 Gemini 應用程式中的 Deep Think 則達到 **銅牌水準**，雖低於研究版，但仍相當可觀，且速度快得多。兩者之差距，反映的是推理計算量與現實部署限制之間的永恆取捨。

## 開放範圍與限制

基準數字之外，存取限制才是用戶最切身感受到的現實。

Deep Think 目前僅向 **Google AI Ultra 訂閱者** 開放，透過 Gemini 應用程式中的切換按鈕啟用，每日提示配額有限。一旦用盡，當天就只能使用標準 Gemini 2.5 Pro。開發者透過 Gemini API 存取的功能預計「數週內」上線。

以 Gemini 2.5 Pro 標準定價（每百萬 Token 輸入 2.5 美元、輸出 15 美元）推算，Deep Think 模式的成本約是標準推理的 **4 倍**。這讓它定位為需要前沿推理能力的高價值任務——複雜科學分析、高階數學推導、多步驟系統架構設計——而非日常問答場景。

## 安全性與過度拒絕的取捨

值得留意的一個技術細節：Deep Think 在內容安全評分上優於標準 Gemini 2.5 Pro，但也展現出更高的拒絕回答傾向，包括部分合理的無害請求。這是前沿推理模型的典型張力——隨著模型識別潛在危害的能力增強，其「安全網」的邊界往往也跟著擴張，誤殺合法請求。

在資安研究、醫學分析、競爭情報等領域，這種過度拒絕的傾向將成為企業用戶的實際摩擦點。Google 若要讓 Deep Think 在 API 全面開放後被開發者信賴為生產推理層，這個校準問題必須在發布前解決。

## 競爭格局

Deep Think 的發布時機對 Google 而言頗為有利，無論是否刻意為之。Anthropic Fable 5 在 6 月 12 日遭美國政府暫停全球存取，讓 Google 得以在少了最強對手的情況下宣稱推理能力王座。OpenAI 在 6 月 26 日以限量預覽形式發布的 GPT-5.6 Sol，將是 Deep Think 接下來面臨的直接考驗。

## 推理時計算：改變遊戲規則的槓桿

Deep Think 更深遠的意義在於：它清楚宣示了一個新方向——模型能力的提升，不再只靠訓練規模，同樣可以來自推理時投入的計算量。

OpenAI 的 o 系列早已示範過延伸思考，但 Gemini 2.5 Deep Think 在廣泛基準上的領先幅度，讓這個方向得到了前所未有的有力驗證。對企業而言，AI 採購決策的問題已不只是「哪個模型訓練得最好」，而是「你願意為每次查詢分配多少思考時間，又願意為此付出多少成本」。

Deep Think 讓這道問題，從研究議題變成了產品決策。
