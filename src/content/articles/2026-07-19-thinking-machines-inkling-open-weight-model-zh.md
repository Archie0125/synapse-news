---
title: "穆拉提的 Thinking Machines 發布 Inkling：九千七百五十億參數開放權重模型正面挑戰閉源生態"
summary: "前 OpenAI 技術長 Mira Murati 創立的 Thinking Machines Lab 正式推出 Inkling，這是一個擁有 9,750 億總參數的混合專家（MoE）開放權重模型，採 Apache 2.0 授權免費開放。這支僅有 200 名員工的團隊在九個月內完成了這個支援百萬 token 上下文窗口的多模態模型，並透過 Tinker 微調平台讓企業能在自己的基礎設施上訓練專屬 AI，無需支付授權費。"
category: "ai-ml"
publishedAt: 2026-07-19
lang: "zh"
featured: true
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/"
  - name: "Fortune"
    url: "https://fortune.com/2026/07/15/what-is-mira-murati-thinking-machines-first-ai-model-inkling/"
  - name: "Thinking Machines Lab"
    url: "https://thinkingmachines.ai/news/introducing-inkling/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/thinking-machines-open-sources-first-multimodal-language-model-inkling-focused-on-low-cost-and-resistance-to-censorship"
tags:
  - "Thinking Machines"
  - "Mira Murati"
  - "開放權重"
  - "大型語言模型"
  - "AI 模型"
  - "多模態"
  - "開源"
relatedSlugs:
  - "2026-07-17-moonshot-kimi-k3-open-weight-model-zh"
  - "2026-07-07-deepseek-custom-ai-chip-inference-zh"
  - "2026-04-04-open-source-llm-race-zh"
---

當 Mira Murati 在 2023 年 10 月離開 OpenAI、創立 Thinking Machines Lab 時，整個 AI 產業既好奇又存疑。九個月內從零開始建立一個能與頂尖開放權重模型競爭的前沿 AI 實驗室，即便在進展神速的 2026 年，也令人難以置信。2026 年 7 月 15 日，Thinking Machines 以行動打臉質疑者：正式推出 Inkling，一個擁有 9,750 億參數的混合專家（MoE）架構模型，以 Apache 2.0 授權向全球開放。

這次發布重新定義了開放權重 AI 生態在前沿層級的可能性，也恰好出現在企業界開始認真質疑「完全依賴閉源模型的經濟邏輯與策略風險」的關鍵時刻。

## Inkling 是什麼，又不是什麼

Thinking Machines 對 Inkling 的定位出乎業界意料地坦誠。公司公告直接寫道：「Inkling 在今天並非整體表現最強的模型，無論是開放或閉源。」在一個每次模型發布都充斥精心篩選基準測試的產業，這種坦誠極為罕見。

Inkling 提供的是另一種組合：廣度、效率與客製化能力。其架構採用稀疏 MoE 設計，總參數量 9,750 億，但每次推論實際啟用的僅約 410 億。這種稀疏性使 Inkling 的推論成本大幅低於同等總參數量的稠密模型——對需要每日處理數百萬次請求的企業而言，這是核心競爭力。

模型訓練語料涵蓋文字、圖片、音訊與影片共 45 兆 token，是原生多模態架構。目前輸出仍限於文字和程式碼，但底層表示跨越多種模態，意味著未來微調版本有潛力直接生成或解讀音訊與影片。

上下文窗口達 100 萬 token，與閉源前沿模型的最大規格相當。更重要的是 token 效率：獨立測試顯示，Inkling 完成等量編程任務所消耗的 token 數，僅為前任開放權重編程標竿 Nvidia Nemotron 3 Ultra 的三分之一。在大規模部署時，這個效率差距直接換算成基礎設施成本的節省。

## 「可控思考力度」：全新的推論界面

技術層面最引人注目的功能是 Thinking Machines 所稱的「可控思考力度（controllable thinking effort）」。不同於 OpenAI o 系列模型普及的思考開關（開或關），Inkling 開放一個從 0.2 到 0.99 的連續調節旋鈕，讓開發者以程式化方式控制模型在生成回應前投入多少計算資源進行推論。

實際意義相當深遠。處理簡單客服問題的聊天機器人，不需要和審計財務模型或偵錯分散式系統競態條件相同的推論深度。透過可控思考力度，單一部署可根據查詢複雜度動態調配推論資源——對簡單任務降低成本，對困難任務維持品質。目前市面上尚無其他主要模型提供這種界面。

## 基準測試脈絡

Thinking Machines 隨發布公布了完整的基準測試套件。在人類終極測驗（HLE）中，Inkling 純文字模式得分 29.7%，啟用工具後升至 46.0%；在 AIME 2026（高階數學競試基準）得 97.1%；在 GPQA Diamond（研究所級科學推理測試）得 87.2%；在 SWE-bench Verified（軟體工程）得 77.6%。

這些數字在開放權重模型中名列前茅，但與 GPT-5.6 Sol 和 Claude Fable 5 等頂尖閉源模型仍有差距。Thinking Machines 呈現的是一種明確的取捨：對大多數真實企業應用而言，客製化能力與部署經濟性比單純的基準測試排名更重要。

橋水基金（Bridgewater Associates）的案例具體說明了這一點：其量化團隊透過 Tinker 平台以金融推理任務微調 Inkling 後，在內部金融推理測試中達到 84.7% 準確率，不僅超越專有閉源模型在同一任務的表現，推論成本也僅約後者的十四分之一。

## Tinker 平台與商業模式

Thinking Machines 不對 API 使用收費，而是透過 Tinker 微調平台獲利。由於 Inkling 的模型權重可從 Hugging Face 免費下載，公司不收取模型授權費，Tinker 的費用依計算量計算，而非存取模型本身。

這種架構使 Thinking Machines 的商業利益與「建立專有 AI」的企業緊密結合。將 Inkling 在內部知識庫上微調的公司，不會將這些知識洩漏給服務數百萬用戶的共享模型，直接解決了企業部署閉源 AI 時的核心數據主權疑慮。

模型發布時即支援廣泛的推論引擎：vLLM、SGLang、Miles、TokenSpeed 與 Llama.cpp 全部相容，提供工程團隊充分的部署彈性。

## 更大的產業訊號

Inkling 發布最重大的意義，不在於模型今日能做什麼，而在於其存在傳達的產業結構訊號。Thinking Machines 以 200 人的規模，在九個月內建立了一個在開放權重生態中具備前沿競爭力的模型。OpenAI 建立第一個 GPT-4 級別的模型花了五年時間，動員了數千名員工。

開發時程的壓縮並非 Thinking Machines 的個案——這是由更優越的訓練基礎設施、更豐富的合成訓練資料，以及自 2022 年以來大量湧入開放文獻的研究成果共同驅動的結構性轉變。其後果是進入前沿 AI 模型市場的門檻正在下降，速度遠超既有龍頭的預期。

微軟執行長薩蒂亞·納德拉（Satya Nadella）最近指出，企業使用專有模型實際上「付了兩次錢」——一次是訂閱費，第二次是使用模式隱性地回饋給了模型提供商——這個觀察在企業 AI 採購團隊中引發廣泛共鳴。Inkling 的 Apache 2.0 授權直接回應了這個疑慮：模型可完全部署在客戶自己的基礎設施內，不受外部控管。

Thinking Machines 能否單靠 Tinker 收入維持可行的商業模式，仍有待驗證——公司據報今年稍早已暫停一輪 500 億美元的融資計畫。但 Inkling 的發布證明這個實驗室在壓縮時程內確實交出了技術可信的產品，這是無論後續融資走向如何都不可否認的事實。

對台灣的 AI 開發者和企業而言，Inkling 的意義同樣值得關注：開放權重模型的崛起，代表企業可以真正在自己的伺服器或雲端基礎設施上部署前沿 AI，不再受制於單一廠商的定價或服務條款。隨著台灣 AI 應用生態加速成熟，具備客製化彈性的開放模型將在企業採購決策中扮演越來越重要的角色。
