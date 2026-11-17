---
title: "PrismML 發布 Bonsai 27B：專為在 iPhone 上運行而打造的 270 億參數 AI 模型"
summary: "由加州理工研究人員創立、獲 Khosla Ventures、Cerberus 與 Google 支持的 PrismML 發布 Bonsai 27B，這是一個 270 億參數的模型，其較小版本約 3.9GB，據 PrismML 白皮書，在 iPhone 17 Pro Max 上每秒約可生成 11 個 Token。模型權重以 Apache 2.0 授權開放，該版本在 PrismML 自家評測中保留了原模型約 90% 的性能。"
category: "developer-tools"
publishedAt: 2026-07-17
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: false
sources:
  - name: "9to5Mac"
    url: "https://9to5mac.com/2026/07/14/prismml-releases-bonsai-27b-claiming-first-major-ai-model-of-its-size-fit-for-iphone/"
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/07/14/prismml-releases-bonsai-27b-1-bit-and-ternary-builds-of-qwen3-6-27b-that-run-on-laptops-and-phones/"
  - name: "The Decoder"
    url: "https://the-decoder.com/bonsai-27b-is-a-full-open-reasoning-model-that-fits-on-an-iphone/"
tags:
  - "端側AI"
  - "PrismML"
  - "Bonsai 27B"
  - "行動裝置AI"
  - "開源"
  - "量化技術"
  - "iPhone"
relatedSlugs:
  - "2026-07-17-prismml-bonsai-27b-iphone-on-device-en"
  - "2026-07-17-moonshot-kimi-k3-open-weight-model-zh"
---

AI 從雲端遷移至邊緣端的故事已醞釀多年。由加州理工研究人員創立的 PrismML 發布了 Bonsai 27B，一個 270 億參數的模型，其較小版本約佔 3.9GB，且據 PrismML 白皮書，在 iPhone 17 Pro Max 上每秒約可生成 11 個 Token。

這個基於阿里巴巴 Qwen3.6 27B 底座、但以極端量化技術從底層重建的模型，其模型權重以 Apache 2.0 授權開放，PrismML 另提供限時免費的開發者預覽版 API。開發者今天就能下載 Bonsai 27B，完全在消費級裝置上本地運行，並打造出能夠處理文字、圖片和文件、無需任何雲端 API 調用的應用程式。

這與哪怕十二個月前的端側 AI 世界，都是截然不同的圖景。

## 如何將 270 億參數塞進手機

技術挑戰相當明確。這個規模的模型通常佔用約 54GB 儲存空間，而 12GB 的 iPhone 只能提供約 6GB 給單一應用程式使用。壓縮至 3.9GB，意味著在不造成災難性性能損失的前提下實現約 14:1 的壓縮比。這正是 PrismML 過去一年努力解決的問題。

公司的方案是同時發布兩種量化版本：**1-bit 版本**的每個權重只有兩種狀態，是約 3.9GB 的較小版本，也是供 iPhone 使用的版本；**三元版本**每個權重使用三種狀態，是約 5.9GB、著重品質的較大版本，適用於筆記型電腦。

兩種版本均建立在 1.58-bit BitNet 研究傳統之上，但 PrismML 的實現為 ARM 和 Apple Silicon 架構的推理引入了多項專有優化，公司表示這是大部分實際速度提升的來源。在 PrismML 自家進行的 15 項評測中，較小版本保留了原模型約 90% 的性能，PrismML 並表示數學與程式碼能力「幾乎未受影響」。

視覺模組——讓模型能夠處理圖片、截圖和相機輸入——以緊湊的 4-bit 形式保留，而非完全捨棄，在手機記憶體限制內維持了多模態能力。

## 投機解碼進一步放大優勢

Bonsai 27B 內建了投機解碼（Speculative Decoding）實現——一種由較小的「草稿」模型快速預測接下來可能的 Token，再由主模型並行驗證的技術。在相容硬體上，這在每秒 11 Token 的基礎速率之外進一步提升了實際吞吐量——公司表示在最新 iPhone 硬體上的連續散文生成任務中，可達每秒 15 至 17 Token。

26.2 萬 Token 的上下文窗口是另一個亮點數字。對於在手機上本地運行的模型而言，26.2 萬 Token 意味著無需分塊或檢索增強，便能處理一份 200 頁的 PDF、一個完整的代碼庫，或一段漫長的多輪對話。此前 100 億參數以下的端側模型通常最多支持 8000 至 3.2 萬 Token。Bonsai 27B 的上下文窗口是台階式的躍升，徹底改變了本地構建哪些應用是可行的。

## 公司背景與投資人陣容

PrismML 是由一群加州理工研究人員創立的公司。公司創立時獲得 Khosla Ventures、Cerberus 和 Google 的支持，三星則持續給予支持。

三星的參與尤為值得關注。三星每年出貨數億台 Android 裝置，並在過去兩年持續構建自家的端側 AI 平台（Galaxy AI）。Bonsai 27B 為三星提供了一個可在 Galaxy 硬體上運行、無需為每次推理支付雲端費用的 270 億參數級模型——這是三星創投部門支持其發展的強烈動機。

## 開發者的機會

從開發者視角看，Bonsai 27B 開啟了一系列此前實際上無法觸及的應用類別。

**隱私優先應用**：文件處理、筆記、日記和健康監測等用戶不希望數據離開裝置的場景。一個本地運行的 270 億參數級模型，能以過去只有雲端 API 才能提供的能力，在設備內部處理和推理個人數據。

**離線優先企業工具**：無法保證穩定網路連接的現場工作人員、醫療專業人員和軍事應用。能從手機內部儲存運行前沿級別的模型，不依賴任何網路，徹底改變了一大類企業軟體的架構。

**低延遲消費體驗**：即便在快速網路環境下，雲端往返延遲也會引入數百毫秒的等待。端側推理完全消除了這一問題。對於即時翻譯、無障礙工具、代碼輔助等實時應用，這是使用者體驗上的質性差異。

**新興市場普及**：在雲端推理成本令人望而卻步、或網路基礎設施不可靠的地區，一個完全離線運行的強大模型，改變了誰能夠獲得高能力 AI 工具的問題。

## 「DeepSeek 時刻」的比喻

多個報導 Bonsai 27B 發布的媒體使用了「DeepSeek 時刻」這一說法——呼應 2026 年 1 月 DeepSeek R1 的發布：它以遠低於預期的成本實現了前沿級別的推理能力，震撼了 AI 基礎設施投資論的基本假設。這個類比捕捉到了某些真實的東西：兩個事件都涉及以戲劇性更低的成本，達到此前被認為需要昂貴資源才能實現的能力。

這個類比並不完美——DeepSeek R1 的成本效率是在訓練階段實現的，而 Bonsai 27B 的效率是在特定硬體的推理階段實現的。但核心邏輯成立：「270 億參數級別的智慧需要雲端基礎設施」這一假設，已被一份開源、Apache 授權的發布所推翻。

對於 AI 開發者而言，這值得深思。相當比例的 AI 應用架構，是建立在「這個規模的模型只能活在雲端」的假設之上的。Bonsai 27B——以及它所代表的那類模型——表明這個假設需要重新審視。

模型權重現已可在 PrismML GitHub 儲存庫中獲取。據 PrismML 表示，12GB 的 iPhone 只能提供約 6GB 給單一應用程式使用，由模型與快取共用。iPhone 17 Pro、iPhone 17 Pro Max 和近期的 iPad Pro 機型均符合要求。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 11 處。*
