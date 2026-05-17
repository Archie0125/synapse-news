---
title: "前OpenAI技術長穆拉蒂的Thinking Machines發布互動模型：0.4秒全雙工AI對話"
summary: "前OpenAI技術長Mira Murati創辦的Thinking Machines Lab發布首款產品「互動模型」（Interaction Models）——一個從零打造、專為即時人機對話設計的原生多模態AI架構。旗艦模型TML-Interaction-Small的回應延遲僅0.4秒，接近自然對話速度，底層為2760億參數的混合專家（MoE）架構，推理時僅啟用120億參數。"
category: "ai-ml"
publishedAt: 2026-05-17
lang: "zh"
featured: false
trending: true
sources:
  - name: "Semafor — 穆拉蒂的Thinking Machines預覽互動模型"
    url: "https://www.semafor.com/article/05/13/2026/mira-muratis-thinking-machines-previews-interaction-models"
  - name: "The AI Insider — Thinking Machines發布0.4秒全雙工AI"
    url: "https://theaiinsider.tech/2026/05/12/mira-muratis-thinking-machines-lab-unveils-full-duplex-ai-that-responds-in-0-4-seconds/"
  - name: "MarkTechPost — Thinking Machines介紹互動模型"
    url: "https://www.marktechpost.com/2026/05/13/mira-muratis-thinking-machines-lab-introduces-interaction-models-a-native-multimodal-architecture-for-real-time-human-ai-collaboration/"
  - name: "TechFunding News — Thinking Machines Lab 20億美元種子輪"
    url: "https://techfundingnews.com/thinking-machines-lab-ai-seed-round-record/"
tags:
  - "Mira Murati"
  - "Thinking Machines Lab"
  - "多模態AI"
  - "語音AI"
  - "AI模型"
  - "即時AI"
  - "新創公司"
relatedSlugs:
  - "2026-04-23-thinking-machines-lab-google-cloud-deal-zh"
---

Mira Murati在OpenAI工作了七年，親手參與塑造了整個AI產業的走向。2024年底以技術長身份離開後，這位募集到史上最大規模種子輪的創辦人，展現了一種在矽谷罕見的自我克制——在還未推出任何產品之前，保持沉默。5月11日，沉默被打破。Thinking Machines Lab正式預覽首款產品：互動模型（Interaction Models）。穆拉蒂強調，這不是現有語音模式技術的迭代升級，而是對「機器如何對話」這個問題從底層重新思考的答案。

## 用架構解決延遲問題

所有擁有語音AI產品的實驗室都在與同一個問題搏鬥：人類自然對話的反應延遲約在200至400毫秒之間。現今最頂尖的系統——包括GPT-4o語音模式和Google Gemini Live——在網路狀況良好時延遲約在400至700毫秒，流量高峰時更長。這個感知差距雖然細微，卻足以讓對話產生一種微妙的「離線感」，如同透過品質欠佳的衛星通話交談。

Thinking Machines發布預覽的核心模型TML-Interaction-Small，宣稱回應延遲為0.40秒。若這個數字能在不同對話情境和規模下穩定維持，就已落在人類聽者感受為「自然」的延遲範圍下緣。目前公司尚未公開詳細的基準測試方法，系統也還未開放公眾使用，獨立驗證仍有待進行。

實現這一目標的架構選擇，是採用總參數量高達2760億的混合專家（Mixture-of-Experts，MoE）設計，但每次推理僅啟用約120億個參數。MoE架構已成為前沿實驗室平衡能力與效率的主流正規——Meta的Llama 4、Google的Gemini系列、OpenAI的GPT-4o都採用了這種架構的變體。Thinking Machines聲稱與眾不同之處在於：他們的模型是專為持續、全雙工互動而從零訓練，而非將一個以文字為基礎的大型語言模型適配到語音場景。

## 全雙工：被忽視的維度

大多數AI語音介面在架構上是回合制的：使用者說話，模型轉錄、處理、回應，然後等待下一個輸入。全雙工通訊——雙方可以同時說話、聆聽和打斷，就像真實的人類對話——要求模型在即時處理傳入音訊的同時，保持對互動狀態的持續表徵。這在工程上的難度遠超低延遲回合制響應。

Thinking Machines將TML-Interaction-Small描述為原生全雙工系統，能夠處理打斷、話題切換以及重疊發言，而不丟失上下文或需要重置對話狀態。在預覽演示中，該模型據報能處理句中更正，以及人類對話中表示理解的「嗯嗯」、「對對對」等反饋訊號，而不會將其解讀為新的提示輸入。

這個設計選擇對企業應用場景有深遠影響。客服代理、輔導教學和醫療問診流程長期受制於回合制互動模式——那種不自然的停頓讓使用者感覺自己是在操作一個工具，而非進行對話。全雙工架構若能在規模上可靠運作，將移除這個根本性的限制。

## 十七個月、20億美元，然後一款產品

Thinking Machines Lab的時間軸值得細細品味。穆拉蒂於2024年底離開OpenAI。到2025年7月——創辦後不到九個月——公司便以120億美元估值完成了20億美元的種子輪，投資方包括Andreessen Horowitz、NVIDIA、AMD、Cisco和Jane Street。2026年3月，公司宣布與NVIDIA建立多年戰略夥伴關係，取得1吉瓦的Vera Rubin運算容量。4月，一項數十億美元的Google Cloud基礎設施協議隨後簽署。

在沒有任何公開產品的情況下聚集如此規模的資本與運算資源，是市場對穆拉蒂個人信譽和她所招募團隊的一次豪賭——據報包括來自OpenAI、Google DeepMind和Meta AI的資深研究員。創辦十七個月後發布的互動模型預覽，是這份信譽迄今所建構成果的第一次公開亮相。

TML-Interaction-Small的限量訪問將在未來幾個月透過候補名單陸續開放，定價尚未公布，更廣泛的公開發布預計在2026年下半年推出。

## 競爭格局

Thinking Machines進入的語音AI市場，在2026年比一年前更為擁擠。ElevenLabs在3月募集5億美元以擴展語音合成與對話AI平台；Hume AI和Sesame AI持續展示情感感知語音互動能力；OpenAI的GPT Realtime API第二版上月剛以顯著改善的延遲和多語言支援正式發布；Google預計在下週二的Google I/O 2026宣布Gemini語音增強功能。

Thinking Machines有別於這些競爭者的，是對全雙工原生架構的堅持——而非把系統級延遲優化疊加在既有模型之上。這種架構差異是否能在規模商用後轉化為有意義的產品優勢，是這次互動模型預覽提出但尚未解答的問題。

更耐人尋味的是：穆拉蒂的團隊下一步要做什麼？120億美元的估值和已就位的基礎設施協議表明，他們建構的不是一個語音助理，而是下一代人機互動的底層基礎設施，以語音作為第一個應用介面。模型的命名——TML-Interaction-**Small**——暗示更大型的兄弟模型正在研發中。對一家沉默這麼久的公司而言，名字裡的「Small」感覺像是刻意為之的低調。
