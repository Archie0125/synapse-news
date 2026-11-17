---
title: "Meta 推出 Muse Spark：從開源轉向專有，豪賭超級智能"
summary: "Meta 發布 Muse Spark，這是由 Alexandr Wang 領導的 Meta 超級智能實驗室推出的第一個模型，標誌著 Meta 從開源 Llama 系列轉向專有模型。此次發布正值 Meta 試圖迎頭趕上 OpenAI、Anthropic 與 Google。"
category: "ai-ml"
publishedAt: 2026-04-12T09:25:00Z
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "Meta AI 部落格"
    url: "https://ai.meta.com/blog/introducing-muse-spark-msl/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/08/meta-debuts-the-muse-spark-model-in-a-ground-up-overhaul-of-its-ai/"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/04/08/meta-debuts-first-major-ai-model-since-14-billion-deal-to-bring-in-alexandr-wang.html"
  - name: "Axios"
    url: "https://www.axios.com/2026/04/08/meta-muse-alexandr-wang"
tags:
  - "meta"
  - "muse-spark"
  - "大型語言模型"
  - "alexandr-wang"
  - "開源"
  - "AI模型"
relatedSlugs:
  - "2026-04-12-meta-muse-spark-superintelligence-labs-en"
  - "2026-04-10-google-gemini-31-flash-live-zh"
---

九個月前，Meta 投資 143 億美元於 Scale AI，將 Alexandr Wang 納入麾下。如今，Meta 終於有了一個模型可以交代。

4 月 8 日，Meta 發布 **Muse Spark**，這是 **Meta 超級智能實驗室**（Meta Superintelligence Labs，MSL）的首個成果。MSL 是 Zuckerberg 在對既有 AI 研究團隊的進展感到不耐煩後，圍繞著 Wang 重新組建的內部單位。這個最初代號為「酪梨」（Avocado）的模型是專有模型，與 Meta 在 Llama 系列模型上採取的開源路線劃清界線。

Muse Spark 是專有模型。這短短幾個字，背後承載著巨大的策略意義。

## Llama 霸主地位的終結

Meta 的 Llama 系列自 2023 年問世以來，徹底改變了 AI 版圖。透過以寬鬆授權釋出基礎模型，Meta 讓全球開發者免費取得強大的基礎架構，圍繞自家軟體建立起龐大的開源生態，並將自己定位為 OpenAI、Anthropic 等封閉實驗室的反制力量。

這個策略在 2025 年初開始遇到麻煩。去年四月發布的 Llama 4 未能激起前幾代的熱情。開發者批評模型在基準測試上的表現與參數規模不相符，在真實任務上落後 GPT-5 和 Gemini 3，也缺乏競爭對手微調後的精緻度。曾是 Llama 忠實用戶的開發者社群，開始繞道而行。

Zuckerberg 的回應是拆解既有研究層級、重新搭建。Wang 引進的不只是一個人，而是一套完整的哲學：嚴謹的資料工程、工業規模的評估流程，以及把 AI 開發視為產品學科而非研究習題的態度。Meta 超級智能實驗室被設立為獨立單位，擁有自己的算力配置、招募自主權與發布節奏，與過去讓 Llama 進展緩慢的內部政治切割開來。

## Muse Spark 的能力

Meta 形容 Muse Spark「設計上輕巧且快速，但足以推理科學、數學與健康領域的複雜問題」。Meta 表示，模型在**多模態感知、推理、健康與代理任務**上具有競爭力的表現，同時持續投資於仍有差距的領域，例如長時程代理系統與程式撰寫工作流程。

健康面向的強調頗耐人尋味。Meta 已悄悄為消費者健康 AI 策略耕耘兩年，在 Instagram 和 WhatsApp 試行幫助用戶追蹤營養、心理健康與體能的功能。Muse Spark 被設計來大規模驅動這一層——一個能解讀醫學影像、解析檢驗報告、進行細緻健康對話、無需專業微調的模型。

在標準基準測試上，早期預覽將 Muse Spark 置於與 GPT-5.4 在推理和程式撰寫任務上旗鼓相當的位置，但 Meta 尚未公布全面的公開評估。獲得早期使用權的獨立研究人員形容模型的輸出品質「明顯和 Llama 不同——是好的那種不同」：更緊實、更一致，在多步驟問題上較少出現幻覺。

## 發布計畫

Muse Spark 立即作為 **Meta AI 應用程式與官網**的核心推出，取代了過去驅動這些產品的 Llama 系統。未來幾週，Meta 計畫將模型延伸至 WhatsApp、Instagram、Facebook、Messenger，以及 Ray-Ban AI 眼鏡。

尤其是眼鏡整合，代表 Meta 重金投注的產品方向。Wang 的團隊據報在建構 Muse Spark 的多模態管道時，以可穿戴設備推論為頭等目標，針對有限頻寬下的低延遲回應進行優化——這與 OpenAI 和 Google 以資料中心為優先的架構路線大相徑庭。

## 設計上的專有——至少目前如此

封閉 Muse Spark 原始碼的決定，在公司內部被框架為競爭必要。當 Meta 需要開發者好感、尚未站在前沿時，開源 Llama 是合理的。現在它已在前沿競爭（或至少有這個抱負），算盤就得重新打。

話雖如此，Meta 並未完全拋棄開源。公司表示，「希望能開源該模型的未來版本」。

就目前而言，訊息是清楚的：Meta 不再甘於扮演開源替代方案。它要贏。

## 能否縮短差距？

Muse Spark 是否能兌現這個抱負，仍是未解的問題。模型首秀獲得了溫暖卻謹慎的回應。評測者肯定比起 Llama 4 的真實進步，但也指出一次模型發布並不能抹去過去一年 Llama 停滯所造成的差距。

與模型本身同樣重要的，是它所傳遞的組織決心信號。九個月前，Zuckerberg 做出了牽涉大量資本和個人公信力的非凡承諾。Muse Spark 是這筆投資的第一個有形回報。下一代模型——Meta 表示已在開發中——將告訴我們，這次重組究竟帶來了持久的質變，還是只是一次短暫的修正。

AI 競賽正在進入一個領先者與落後者差距可能迅速拉大的階段。Meta 至少已清楚表態：它要參與角逐。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 9 處。*
