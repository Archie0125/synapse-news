---
title: "中國 GLM-5.2 在編程基準測試中超越 GPT-5.5，成本僅六分之一"
summary: "Z.ai（前身為智譜 AI）於 6 月 17 日發布的開放權重模型 GLM-5.2 擁有 7530 億參數的混合專家架構，在 SWE-bench Pro 上以 62.1 分超越 GPT-5.5 的 58.6 分，同時每百萬輸出 Token 僅收費 4.40 美元，約為 GPT-5.5 的六分之一。模型採用 MIT 授權，權重可從 Hugging Face 免費下載，為被鎖在高價閉源模型之外的開發者提供了新選擇。"
category: "ai-ml"
publishedAt: 2026-06-23
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: true
trending: true
sources:
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/z-ais-open-weights-glm-5-2-beats-gpt-5-5-on-multiple-long-horizon-coding-benchmarks-for-1-6th-the-cost"
  - name: "The Decoder"
    url: "https://the-decoder.com/zhipu-ais-glm-5-2-closes-in-on-closed-source-leaders-in-coding-marathons/"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/318543/20260617/glm-52-open-weights-live-top-coding-benchmark-api-use-carries-china-data-risk.htm"
  - name: "Labellerr"
    url: "https://www.labellerr.com/blog/glm-5-2-open-weight-ai-model/"
tags:
  - "GLM-5.2"
  - "智譜 AI"
  - "Z.ai"
  - "開源 AI"
  - "中國 AI"
  - "編程基準"
  - "GPT-5.5"
  - "開放權重"
relatedSlugs:
  - "2026-06-14-moonshot-kimi-k2-7-code-open-source-coding-model-zh"
  - "2026-06-12-minimax-m3-open-weight-frontier-model-zh"
  - "2026-06-04-open-source-llm-race-zh"
---

當 Anthropic 的 Fable 5 在 6 月 12 日因美國出口管制措施而被迫下線，AI 前沿性能出現了明顯缺口。北京人工智能公司 Z.ai（前身為智譜 AI）剛剛展示了這個缺口能以多快速度被填補——且來自一個令人意外的方向。

模型權重採用 MIT 授權，可從 Hugging Face 和 ModelScope 下載，無地區限制。

## 架構：以效率換規模

GLM-5.2 是一個擁有 7530 億參數的混合專家（MoE）模型，但對於任一輸入僅啟動約 400 億個參數。這種稀疏激活架構——原理上與 Mistral 的 Mixtral 系列及 Google Gemini Ultra 相似——讓 GLM-5.2 在擁有 7530 億稠密模型容量的同時，以遠小得多的模型成本完成推理。

模型在前一代 GLM-5 基礎上引入了兩項架構創新：IndexShare 和多 Token 預測（Multi-Token Prediction）。IndexShare 在每四個稀疏注意力層之間重複使用同一個注意力索引器，在 100 萬 Token 上下文下將每個 Token 的運算量降低 2.9 倍；多 Token 預測則讓模型一次預測多個 Token 而非一個，加快解碼速度。完整上下文窗口達到 100 萬 Token，與 OpenAI 和 Anthropic 的頂級產品持平。

## 基準表現：數字說話

最受矚目的指標是 SWE-bench Pro——這是衡量真實世界軟體工程能力的黃金標準，測試題目源自真實 GitHub Pull Request。GLM-5.2 得分 62.1，高於前代 GLM-5.1 的 58.4，明顯超越 GPT-5.5 的 58.6。作為參考，Claude Opus 4.8 在 SWE-bench Pro 上得分 69.2，GLM-5.2 約落後其七分。

在 FrontierSWE Dominance（專為衡量需要數小時才能完成的長鏈路工程任務而設計的基準）上，GLM-5.2 得分 74.4%，超過 GPT-5.5 的 72.6%，僅略低於 Claude Opus 4.8 的 75.1%。這一模式在 PostTrainBench 上同樣成立，GLM-5.2 超越 GPT-5.5，僅次於 Opus 4.8 排名第二；在 SWE-Marathon 上，GLM-5.2 雖落後 Opus 4.8，但仍僅次於 Opus 系列。這三項都是長鏈路編程基準。

尤為值得關注的是 GLM-5.2 在 Design Arena 眾包 HTML 和網頁設計排行榜上的第一名，Elo 分數約 1360，超越了 Claude Fable 5 以及 Opus 4.6 和 4.7 模型。Design Arena 以真人評分衡量模型輸出的偏好，表明 GLM-5.2 的能力提升不僅限於程式正確性，更延伸至程式碼生成的美感與結構判斷。

在 Artificial Analysis Intelligence Index v4.1（跨推理、編程和知識任務的綜合基準）上，GLM-5.2 得分 51，在所有開放權重模型中居首，領先 MiniMax-M3（44）、DeepSeek V4 Pro（44）和 Kimi K2.6（43）。

## 成本算術

對許多開發者而言，成本故事不亞於基準故事。Z.ai 提供的 Anthropic 相容 API 端點定價為：每百萬輸入 Token 1.40 美元、每百萬輸出 Token 4.40 美元。GPT-5.5 的輸出 Token 約 30 美元每百萬——約貴 6.8 倍。

實際影響相當可觀。一個每天使用 1000 萬輸出 Token 的編程智能體，在 GLM-5.2 上每日成本約 44 美元，而在 GPT-5.5 上則高達 300 美元。對於此前需要頂級模型才能完成工作的新創公司或個人開發者而言，GLM-5.2 大幅改變了 AI 輔助開發的經濟邏輯。

模型同時提供兩種推理強度：「High」僅犧牲少許效能，同時讓 Token 輸出量減少約一半；「Max」則追求最高智慧表現，代價是更多的輸出 Token。這與 OpenAI o 系列和 Anthropic 延伸思考模式的分層推理方法如出一轍。

## 開放權重，開放問題

在 2026 年日益受限的 AI 環境下，GLM-5.2 的 MIT 授權格外引人注目。Anthropic 的 Fable 5 和 Mythos 5 因美國商務部出口管制仍處於下線狀態，OpenAI 也在多個司法管轄區限制存取，GLM-5.2 成為少數幾個可供組織自行下載、自行部署而不依賴供應商的前沿級模型之一。

以完整精度進行本地部署，大約需要 1.5 TB 的 GPU 記憶體；參考部署採用 8 張 NVIDIA H200 GPU，而 FP8 精度可將權重佔用量降至約 744 GB。這讓大多數開發團隊和很大一部分中型企業都難以負擔完全主權部署。

對於透過 Z.ai 託管 API 使用的團隊，資料主權問題更為複雜。作為在中華人民共和國管轄下運作的中國公司，Z.ai 的資料處理行為受中國法律約束，包括潛在的政府調閱條款。在國防、醫療或金融領域的高安全需求組織已將此標記為 API 使用的實質性風險，儘管開放權重允許替代性的本地部署。

## 競爭背景：中國的開源攻勢

GLM-5.2 的出現，是中國 AI 實驗室自 2025 年初 DeepSeek-R1 以來持續推進的戰略體現。這一策略始終如一：用開放權重模型匹配或超越美國閉源前沿性能，透過 API 積極定價，並以寬鬆授權發布權重。Kimi K2.6、MiniMax-M3，如今再加上 GLM-5.2，輪流在短短數週內佔據各主要基準的「最佳開放權重」位置。

這造就了美國 AI 公司未曾充分預見的競爭態勢：開源中國模型正在有效地為閉源美國模型的同等編程性能設定價格上限。當 GLM-5.2 以六分之一的成本解決與 GPT-5.5 同等難度的軟體工程任務，且開放底層權重供免費使用，任何不明確需要「僅限前沿」能力的開發者任務，都更難為高溢價定價辯護。

對整個 AI 產業而言，更深遠的問題在於 GLM-5.2 所揭示的中國 AI 發展速度。Z.ai 的模型在多個編程維度上已接近 Anthropic 兩個月前才發布、定位為最強推理系統的 Opus 4.8 水準。美國閉源前沿與中國開放權重之間的差距，正以快於大多數競爭預測的速度縮小。

## 下一步走向

Z.ai 已透過公開資料表明，Anthropic 公開發表的思維鏈和工具使用擴展研究為 GLM-5.2 的訓練方法提供了部分參考。無論是刻意為之還是巧合，GLM-5.2 的能力與 Anthropic 公開記錄的技術高度吻合，說明 AI 研究的開放發表這一長期業界慣例，如今可能讓競爭對手受益甚多。

對於在 2026 年下半年做出模型選擇的開發者而言，GLM-5.2 已建立了一個新的基準預期：開放權重、MIT 授權、接近前沿水準、遠比閉源替代品便宜。下一個問題是，傳聞將於六月底發布的 GPT-5.6 能否重新建立足以支撐溢價定價的明顯性能優勢。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 10 處。*
