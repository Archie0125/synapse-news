---
title: "DeepSeek V4-Flash 正式發布：代理基準測試全面超越自家旗艦 Pro 模型，價格僅三分之一"
summary: "DeepSeek 於 7 月 31 日發布 V4-Flash-0731，這個擁有 2840 億參數的混合專家模型在所有代理測試上都超過了自家的 V4-Pro-Preview，DeepSWE 分數更是爆增 645%，同時每百萬輸出 token 僅需 0.28 美元。這款 MIT 授權的開源模型重新定義了自動化編程與工具呼叫代理的性價比上限。"
category: "ai-ml"
publishedAt: 2026-08-01
lang: "zh"
featured: true
trending: true
sources:
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/07/31/deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains/"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/322513/20260731/deepseek-retrained-v4-flash-beats-its-flagship-pro-nine-agent-benchmarks.htm"
  - name: "Caixin Global"
    url: "https://www.caixinglobal.com/2026-08-01/deepseek-releases-official-v4-flash-model-as-chinas-ai-race-intensifies-102470292.html"
tags:
  - "DeepSeek"
  - "AI 模型"
  - "代理 AI"
  - "開源模型"
  - "基準測試"
  - "中國 AI"
relatedSlugs:
  - "2026-07-31-openai-gpt56-luna-80-percent-price-cut-zh"
  - "2026-08-01-xai-grok-46-47-rapid-release-roadmap-zh"
---

7 月 31 日，DeepSeek 悄悄在官方技術博客發布了 V4-Flash-0731 的更新日誌，但這份更新引發的波瀾絕不安靜。幾個關鍵數字讓全球 AI 工程師社群瞬間炸鍋：一款定位為「輕量級」的模型，在代理（Agent）基準測試上竟然全面超越了自家的旗艦 Pro 版本，而且售價僅是 Pro 的三分之一。

## 架構沒變，但能力大幅躍進

DeepSeek 這次刻意強調：V4-Flash-0731 的模型架構與四月預覽版完全相同——2840 億參數、混合專家（MoE）設計，每個 token 推論時只啟動 130 億參數，上下文窗口維持 100 萬 token。API 定價同樣未動：輸入 token 0.14 美元/百萬（快取命中僅 0.0028 美元），輸出 0.28 美元/百萬。

真正改變的，是模型架構之外的一切：後訓練流程。DeepSeek 針對工具呼叫、多步驟推理和長程編程任務，進行了一輪全新的強化學習與監督微調。公司沒有揭露訓練計算量、資料集組成或是否引入人類偏好資料——這與他們自 V3 以來一貫低調的風格一致。

結果是，單靠後訓練，這個模型就在幾乎所有代理評測上大幅超越了它曾落後的 Pro 版本。

## 關鍵數字一覽

DeepSeek 公布了三個版本的四項基準比較：四月預覽版 Flash、新版 V4-Flash-0731，以及 V4-Pro-Preview。

**Terminal Bench 2.1**（測試模型自主驅動命令列工作流的能力）：V4-Flash-0731 得到 82.7 分，V4-Pro-Preview 為 72.1 分，四月版 Flash 僅 61.8 分。新版 Flash 比 Pro 高出了 14%。

更驚人的是 **DeepSWE**，這是一個要求模型實際解決 GitHub 真實 Issue 的軟體工程代理評測。四月 Flash 預覽版得 7.3 分，V4-Pro-Preview 得 12.8 分，而 V4-Flash-0731 直接跳到了 54.4——相當於四月預覽版的 745%，比 Pro 版高出 325%。

此外，**Cybergym**（網路安全代理任務）：76.7 vs. 52.7（Pro）；**NL2Repo**（自然語言轉程式碼倉庫任務）：54.2 vs. 38.5（Pro）。

當然，必要的警語也不能少。上述四項測試全部由 DeepSeek 在自家內部評估框架上執行，未公開原始碼；DSBench-FullStack 和 DSBench-Hard 是完全私有的測試集。截至發布當天，還沒有任何外部研究機構獨立驗證這些數字。

## Responses API 整合與 Codex 適配

除了基準分數，V4-Flash-0731 還正式支援 OpenAI 的 Responses API 格式，並針對 Codex 風格的代理迴圈進行了特殊適配。開發者可以透過單一 vLLM 設定標記啟用 DSpark 推測解碼（speculative decoding），有效提升長上下文輸出的吞吐量。

在最高推理強度下，模型最多可輸出 384,000 個 token，對於需要生成大量程式碼、文件或多檔案差異的代理任務非常實用。

## 部署選項與授權方式

DeepSeek 繼續採用 MIT 授權，商業部署無需付費或簽署額外協議。自架需求：3-bit 量化版本約需 110GB 顯存，完整 BF16 精度則需要四節點 GB300 叢集。這個門檻對資金充裕的新創或企業基礎設施團隊來說可以達到，但個人研究者使用消費級硬體仍無法負擔。

API 並發限制提升至 2,500 個平行請求，遠高於預覽版，顯示 DeepSeek 已為正式生產環境備好了充裕的算力。

## 公司背景與戰略意圖

此次發布時機頗具深意。就在數週前，財新全球確認 DeepSeek 完成了約 74 億美元的融資輪，估值達 3500 億人民幣（約 480 億美元），投資方包括騰訊和網易——是本輪融資潮中中國 AI 實驗室最大的一筆。公司宣布計劃將員工人數翻倍，產品路線圖也明確轉向 AI 代理，而非通用對話助理。

這解釋了為什麼此次發布的重點完全放在代理基準：DeepSeek 並不打算在純粹的推理分數上與 GPT-5.6 Sol 或 Claude Mythos 正面交鋒，而是要在低成本、高可靠性的工具呼叫與長程工作流上建立壁壘。以每百萬輸出 token 0.28 美元計算，開發者用同樣的預算可以跑幾萬次代理任務，而同樣的錢在 OpenAI 或 Anthropic 的頂級模型上只能跑幾百次。

值得一提的背景是：路透社上月報導，北京曾就限制海外用戶取用中國頂尖 AI 模型的可能性，與阿里巴巴（Qwen）、字節跳動（Doubao）和智譜 AI（GLM）進行了磋商。DeepSeek 採用開放權重與 MIT 授權的策略，從根本上繞過了這個政策風險：一旦模型權重可下載，任何出口限制都難以在事後收回。

## 開發者社群的初步反應

發布後 24 小時內，社群反應熱烈但謹慎。多個工程師團隊在非正式測試中確認，相較於四月預覽版，新模型的工具呼叫穩定性確實有顯著提升，即便他們尚未重現 DeepSeek 官方公布的正式基準數字。DeepSWE 的 54.4 分若能通過外部審計，將代表開源模型在真實軟體任務上的一個重要里程碑。

對大多數台灣和全球開發者而言，現在的建議是：用 V4-Flash-0731 測試你的代理工作流，尤其是 CI 整合的自動程式碼審查、大規模資料萃取等對吞吐量和成本敏感的場景。V4-Pro 正式版預計在 2026 年第三季末或第四季初推出，屆時又將帶來新一輪的性能評比。
