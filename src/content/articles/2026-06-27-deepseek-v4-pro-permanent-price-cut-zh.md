---
title: "DeepSeek 將 V4-Pro 降價 75% 改為永久定價，前沿 AI 成本戰進入新階段"
summary: "DeepSeek 宣布將 V4-Pro API 的 75% 折扣正式轉為長期定價，每百萬 token 輸出僅收 $0.87 美元，比 GPT-5.5 便宜 34 倍。這不再只是促銷手段，而是一次對整個前沿 AI 市場成本結構的重新定義，逼迫所有頂級實驗室重新思考「前沿 AI 該值多少錢」這個根本問題。"
category: "ai-ml"
publishedAt: 2026-06-27
lang: "zh"
featured: false
trending: true
sources:
  - name: "Engadget"
    url: "https://www.engadget.com/2180062/deepseek-permanently-reduces-the-price-of-its-flagship-v4-model-by-75-percent/"
  - name: "Apidog"
    url: "https://apidog.com/blog/deepseek-v4-pro-permanent-price-cut/"
  - name: "InfoWorld"
    url: "https://www.infoworld.com/article/4176709/deepseeks-steep-v4-pro-price-cut-escalates-ai-pricing-war.html"
tags:
  - "DeepSeek"
  - "AI定價"
  - "V4-Pro"
  - "API"
  - "定價戰"
  - "中國AI"
relatedSlugs:
  - "2026-06-27-deepseek-v4-pro-permanent-price-cut-en"
  - "2026-06-27-eu-europa-consortium-frontier-ai-grand-challenge-zh"
---

## 折扣不再是折扣，而是新定價

2026 年 5 月，DeepSeek 以「期間限定優惠」的名義，將旗艦模型 V4-Pro 的 API 價格砍了 75%，原訂 5 月 31 日恢復原價。但截止日靜悄悄過去，DeepSeek 沒有任何通知，也沒有任何公告——降價就這樣默默成為永久定價。

現在的 V4-Pro 定價如下：
- 輸入（未快取）：每百萬 token $0.435 美元
- 輸出：每百萬 token $0.87 美元
- 快取命中輸入：每百萬 token $0.003625 美元

這不是小幅調整，而是對整個前沿 AI 市場定價邏輯的一次正面挑戰。

## 數字說什麼

拿幾個現行旗艦模型的輸出定價來對比：
- GPT-5.5：每百萬 token $30 美元
- Claude Opus 4.7：每百萬 token 約 $15 美元
- DeepSeek V4-Pro：每百萬 token $0.87 美元

比 GPT-5.5 便宜 **34 倍**。

更關鍵的是，V4-Pro 在程式碼生成和推理類基準上的表現，與 GPT-5.5 相差僅 3 到 7 個百分點。對大多數生產環境的任務來說，這個差距是可以接受的。

工程師的最優策略因此變得清晰：把最複雜、最高風險的任務留給 GPT-5 或 Claude Fable；把標準吞吐量的任務——程式碼審查、文件摘要、客服、資料萃取——全部導向 V4-Pro。混合策略下，整體計算成本可輕易壓低 70% 以上。

## 這不只是促銷，是平台策略

讓這次降價不同於一般價格競爭的，是「永久」這兩個字背後的戰略邏輯。

DeepSeek 的盤算，業界普遍解讀為教科書級的平台經濟學：主力模型薄利甚至虧本，換取開發者生態的壟斷性黏著——一旦開發者的 pipeline、評估框架和 prompt 都針對 V4-Pro 校調完畢，切換成本就會形成實質上的護城河。之後再用企業合約、客製微調、私有部署等方式回收利潤。

這套打法並不新鮮。AWS 早年以近乎零毛利運營換取雲端市場主導權；Twilio 以遠低於電信商的 API 定價，成為一整代 app 的通訊基礎設施。DeepSeek 顯然在押同一個賭注——但這次是大模型 API 市場。

## 整個市場被迫重新定錨

DeepSeek 的永久降價不是在孤立的真空中發生的。

OpenAI 今年稍早已將 O3 降價 80%；Anthropic 也推出了分層定價架構，讓 Claude 覆蓋從輕量到旗艦的不同成本區間。但在「前沿等級模型的絕對價格地板」這個維度上，沒有任何西方實驗室跟上了 V4-Pro。

2026 年的 AI 定價市場正在形成雙速結構：頂層是 GPT-5.5、Claude Fable 5、Gemini 2.5 Pro Deep Think，以高單價服務最嚴苛的任務；底層是 DeepSeek V4-Pro，以前所未有的低成本提供「前沿鄰近」的推理能力。

對新創公司和獨立開發者而言，這個變化意義深遠。2024 年，一個人開發 AI 應用的算力成本足以讓規模化無法負擔；現在，V4-Pro 加上更輕量的 V4-Flash（每百萬 token 輸入 $0.14），讓真正可用的 AI 應用在過去不可能的使用量規模下也有了經濟可行性。

## 地緣政治面不能略過

DeepSeek 的定價策略無法脫離地緣政治背景來理解。DeepSeek 是中國公司，以遠低於美國競爭對手的成本維持前沿等級的模型能力，已成為華盛頓持續關注的議題。

有分析師指出：DeepSeek 等中國 AI 實驗室可能在能源成本、替代供應鏈的硬體取得、研究人力成本等方面，享有美國實驗室難以複製的結構性優勢。如果 V4-Pro 的低價並非市場策略，而是反映了真實的成本差距，那麼美國實驗室面對的競爭壓力，可能遠超一般商業層面的定價競爭。

美國政府 6 月針對 Anthropic 最先進模型頒布出口管制，部分動機是阻止中國取得美國前沿 AI 能力；而 DeepSeek 的永久降價，則是從另一個方向施壓——一個比任何美國選項都更便宜、更開放的中國前沿模型，正在成為全球開發者生態的預設選項。

## 市場底線已被重新畫定

V4-Pro 的永久降價，讓它在企業 AI 工作負載中成為可信賴的預設選項。接下來的關鍵問題是：它能否繼續縮小與 GPT-5 和 Claude Fable 的能力差距，還是隨著美國實驗室在最複雜推理任務上繼續拉開距離，效能差距反而擴大？

如果 V4-Pro 持續維持在 GPT-5.5 一位數百分點之內、卻只要三十四分之一的輸出成本，那麼把非最高風險任務送到美國前沿模型的經濟邏輯，將越來越難以支撐。

這是市場結構的改變，不是一時的促銷。DeepSeek 已經重新畫定了成本的底線。
