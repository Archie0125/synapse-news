---
title: "Meta 推出 Muse Spark：從開源轉向專有，豪賭超級智能"
summary: "Meta 發布 Muse Spark，這是由 Alexandr Wang 領導的 Meta 超級智能實驗室打造的第一個模型，代表 Meta 從開源 Llama 策略的最大轉向——改走專有封閉路線。此舉清楚表明 Zuckerberg 在競爭敗退數月後，決心縮短與 OpenAI、Google 的差距。"
category: "ai-ml"
publishedAt: 2026-04-12T09:25:00Z
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

九個月前，Mark Zuckerberg 砸下 143 億美元引進 Scale AI 的 Alexandr Wang——這是 AI 產業史上規模最大的人才延攬案。如今，Meta 終於有了一個模型可以交代。

4 月 8 日，Meta 發布 **Muse Spark**，這是 **Meta 超級智能實驗室**（Meta Superintelligence Labs，MSL）的首個成果。MSL 是 Zuckerberg 在對既有 AI 研究團隊的進展感到不耐煩後，圍繞著 Wang 重新組建的內部單位。這個代號為「酪梨」（Avocado）的模型，與 Meta 過去三年的 AI 身份識別做出了乾淨的切割——開源。

Muse Spark 是專有模型。這短短幾個字，背後承載著巨大的策略意義。

## Llama 霸主地位的終結

Meta 的 Llama 系列自 2023 年問世以來，徹底改變了 AI 版圖。透過以寬鬆授權釋出基礎模型，Meta 讓全球開發者免費取得強大的基礎架構，圍繞自家軟體建立起龐大的開源生態，並將自己定位為 OpenAI、Anthropic 等封閉實驗室的反制力量。

這個策略在 2025 年初開始遇到麻煩。去年四月發布的 Llama 4 未能激起前幾代的熱情。開發者批評模型在基準測試上的表現與參數規模不相符，在真實任務上落後 GPT-5 和 Gemini 3，也缺乏競爭對手微調後的精緻度。曾是 Llama 忠實用戶的開發者社群，開始繞道而行。

Zuckerberg 的回應是拆解既有研究層級、重新搭建。Wang 引進的不只是一個人，而是一套完整的哲學：嚴謹的資料工程、工業規模的評估流程，以及把 AI 開發視為產品學科而非研究習題的態度。Meta 超級智能實驗室被設立為獨立單位，擁有自己的算力配置、招募自主權與發布節奏，與過去讓 Llama 進展緩慢的內部政治切割開來。

## Muse Spark 的能力

Meta 形容 Muse Spark「設計上輕巧且快速，但足以推理科學、數學與健康領域的複雜問題」。模型在四個核心領域表現具競爭力：**多模態感知、結構化推理、健康與生活應用，以及代理任務執行**。

健康面向的強調頗耐人尋味。Meta 已悄悄為消費者健康 AI 策略耕耘兩年，在 Instagram 和 WhatsApp 試行幫助用戶追蹤營養、心理健康與體能的功能。Muse Spark 被設計來大規模驅動這一層——一個能解讀醫學影像、解析檢驗報告、進行細緻健康對話、無需專業微調的模型。

在標準基準測試上，早期預覽將 Muse Spark 置於與 GPT-5.4 在推理和程式撰寫任務上旗鼓相當的位置，但 Meta 尚未公布全面的公開評估。獲得早期使用權的獨立研究人員形容模型的輸出品質「明顯和 Llama 不同——是好的那種不同」：更緊實、更一致，在多步驟問題上較少出現幻覺。

## 發布計畫

Muse Spark 立即作為 **Meta AI 應用程式與官網**的核心推出，取代了過去驅動這些產品的 Llama 系統。接下來幾週，Meta 計畫將模型延伸至 WhatsApp、Instagram、Facebook、Messenger，以及 Ray-Ban AI 眼鏡——潛在日活躍用戶規模以十億計，這是其他任何 AI 實驗室都無法企及的分發優勢。

尤其是眼鏡整合，代表 Meta 重金投注的產品方向。Wang 的團隊據報在建構 Muse Spark 的多模態管道時，以可穿戴設備推論為頭等目標，針對有限頻寬下的低延遲回應進行優化——這與 OpenAI 和 Google 以資料中心為優先的架構路線大相徑庭。

## 設計上的專有——至少目前如此

封閉 Muse Spark 原始碼的決定，在公司內部被框架為競爭必要。當 Meta 需要開發者好感、尚未站在前沿時，開源 Llama 是合理的。現在它已在前沿競爭（或至少有這個抱負），算盤就得重新打。

話雖如此，Meta 並未完全拋棄開源。公司表示，計畫**部分開源未來的 Muse 模型**，可能會釋出較小的蒸餾版本或可微調的研究用變體，同時保留完整前沿模型的專有性。這套做法與其他實驗室的模式如出一轍：用封閉模型捕捉商業價值，釋出較小版本維繫開發者生態系的黏著度。

就目前而言，訊息是清楚的：Meta 不再甘於扮演開源替代方案。它要贏。

## 能否縮短差距？

Muse Spark 是否能兌現這個抱負，仍是未解的問題。模型首秀獲得了溫暖卻謹慎的回應。評測者肯定比起 Llama 4 的真實進步，但也指出一次模型發布並不能抹去過去一年 Llama 停滯所造成的差距。

與模型本身同樣重要的，是它所傳遞的組織決心信號。九個月前，Zuckerberg 做出了牽涉大量資本和個人公信力的非凡承諾。Muse Spark 是這場賭注的第一個有形回報。Muse 系列的下一個模型——Meta 已在內部透露——將告訴我們，這次重組究竟帶來了持久的質變，還是只是一次短暫的修正。

AI 競賽正在進入一個領先者與落後者差距可能迅速拉大的階段。Meta 至少已清楚表態：它要參與角逐。
