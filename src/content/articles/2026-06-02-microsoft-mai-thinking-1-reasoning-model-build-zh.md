---
title: "微軟 Build 2026 發表 MAI-Thinking-1：史上首款「不用蒸餾」訓練的推論模型"
summary: "微軟 AI 長 Mustafa Suleiman 在 Build 2026 發表 MAI-Thinking-1，這是微軟首款專屬推論模型，且明確聲明未使用模型蒸餾技術訓練。加上同步公布的圖像、語音與轉錄模型，整個 MAI 系列已成形，顯示微軟正加速建立完整自主 AI 技術棧，逐步降低對 OpenAI 的依賴。"
category: "ai-ml"
publishedAt: 2026-06-02
lang: "zh"
featured: false
trending: true
sources:
  - name: "Business Standard"
    url: "https://www.business-standard.com/technology/tech-news/microsoft-build-2026-what-to-expect-new-reasoning-ai-model-surface-laptop-ultra-126060200686_1.html"
  - name: "Windows News AI"
    url: "https://windowsnews.ai/article/build-2026-microsofts-windows-ai-models-copilot-super-app-and-dev-setup-reset.421337"
  - name: "Tech Insider"
    url: "https://tech-insider.org/microsoft-mai-in-house-ai-models-openai-2026/"
  - name: "WinBuzzer"
    url: "https://winbuzzer.com/2026/02/13/microsoft-mustafa-suleyman-ai-self-sufficiency-openai-mai-models-xcxwbn/"
tags:
  - "微軟"
  - "MAI-Thinking-1"
  - "推論模型"
  - "Build 2026"
  - "Mustafa Suleiman"
  - "AI 自主性"
  - "企業 AI"
relatedSlugs:
  - "2026-06-01-microsoft-build-2026-mai-coding-models-zh"
  - "2026-06-02-microsoft-build-2026-project-polaris-windows-agents-zh"
  - "2026-05-28-microsoft-cancels-claude-code-licenses-copilot-cli-zh"
---

6 月 2 日，微軟 AI 長 Mustafa Suleiman 走上舊金山 Build 2026 的舞台，做了一件微軟醞釀已久的事：他發表了一款完全由微軟自主研發、從零訓練的推論模型——MAI-Thinking-1。

更關鍵的是訓練方式：微軟明確表示，MAI-Thinking-1 在開發過程中**完全未使用模型蒸餾技術**（model distillation）。在這個幾乎所有小型推論模型都仰賴蒸餾的時代，這句聲明本身就是一個戰略宣言。

## 什麼是模型蒸餾？為何微軟要刻意避開它？

過去 18 個月，市場上的小型推論模型幾乎無一例外地使用蒸餾技術訓練——讓小模型學習、模仿大模型的輸出行為。OpenAI 的 o 系列、Meta 和 Mistral 的各款開源推論模型，乃至部分微軟早期的 Azure AI 模型，追根究柢都是大型前沿系統的「壓縮副本」。

蒸餾效率高、效果好，但它同時也創造了依賴：一個蒸餾模型的推論能力，本質上受限於「老師模型」的知識邊界。對微軟這家正努力建立 AI 自主性的公司而言，推出一款推論能力源自最大供應商（即 OpenAI）的模型，在策略上將是個自我矛盾。

MAI-Thinking-1 完全規避了這個問題。微軟尚未公開詳細的訓練架構，但「不使用蒸餾」的聲明意味著：原生訓練資料、自主設計的強化學習流程，以及完全屬於微軟所有的模型權重。

## 瞄準企業客戶

Suleiman 對目標市場直言不諱：MAI-Thinking-1 第一步瞄準企業客戶。這是正確的起點。企業買家在乎能力、合規性和成本，但他們同樣高度在意**技術溯源與供應商獨立性**。一款可在 Azure 內部部署、不依賴 OpenAI 速率限制、不受其定價調整影響的推論模型，對大型企業 IT 組織而言具有實質價值。

模型並未在 Build 大會上正式開放，微軟計畫近期向企業客戶提供預覽存取，2026 年下半年全面上線。

這樣的企業定位也讓微軟暫時避開與 OpenAI o3、Google Gemini Flash Thinking 的公開基準測試比較——在延遲、成本與部署靈活性同樣重要的商業場景中，微軟可以先建立客戶基礎，再面對公開排行榜的壓力。

## MAI 系列的完整版圖

MAI-Thinking-1 加入了微軟已漸成體系的自研模型家族。Build 2026 確認的完整 MAI 陣容包括：

- **MAI-Coding-1**：Build 第一天發表的程式碼模型，將支援下一代 GitHub Copilot
- **MAI-Thinking-1**：企業多步驟推論、自主工作流程與複雜分析的推論模型
- **MAI-Image-2.5** 與 **MAI-Image-2.5-Flash**：圖像生成模型，後者針對低延遲與大規模 API 呼叫優化
- **MAI-Transcribe-1**：語音轉文字模型
- **MAI-Voice-1**：語音合成與即時語音互動模型

統一的 MAI 命名架構和模態覆蓋的廣度，清楚說明這不是一堆分散的研究專案，而是一條**產品線**。微軟正在系統性地為每個主要模態和任務類型建立第一方模型，長期目標是在自家產品表面全面替代或補充 OpenAI 模型。

## 與 OpenAI 的關係愈發微妙

微軟與 OpenAI 仍然深度綁定。130 億美元的投資隨著 OpenAI 估值飆升帶來了可觀回報，雙方的商業協議至少延伸至 2030 年。

但這段關係已明顯複雜化。2025 年由軟銀主導、規模達 400 億美元的融資輪，稀釋了微軟的持股比例。OpenAI 向更傳統企業結構的轉型，改變了合作動態。而 OpenAI 透過 ChatGPT Enterprise 和 Deployco 收購直接殺入企業市場，與微軟的 Azure AI 業務正面競爭。

在這個背景下，微軟每推出一款 MAI 模型，就是在積累一份戰略自主資本。運行在 MAI 上的 Copilot 產品，從定價到能力到路線圖，都掌握在微軟手中，而非 OpenAI。

2023 年從 Inflection AI 加入微軟的 Suleiman，是這場自主化攻勢的主要推手。他在 Build 2026 的登台時間，是一份組織意圖的聲明：微軟的 AI 野心，不再只是 OpenAI 技術的分銷渠道。

## 後續動向

Suleiman 在 Build 上同步預告的 Copilot 超級應用程式（Super App），將成為微軟龐大模型組合的主要消費端介面。這款超級應用程式把多個專屬 Copilot 助手——程式、研究、創意、企業工作流——整合進單一介面，並配備外掛市集。該應用尚未在 Build 開放，預計將於今年夏末推出預覽版。

對開發者而言，微軟也宣布了 Azure AI Foundry 的更新，允許組織在統一推論管線中並排部署 MAI 模型與第三方模型，並提供微調與蒸餾工具——一邊高調宣稱自家旗艦推論模型不靠蒸餾，一邊提供蒸餾工具給開發者，這個矛盾細節沒有逃過現場觀眾的眼睛。

Build 2026 更深層的故事，不是任何單一的模型發表，而是微軟作為一家真正全棧 AI 實驗室的浮現：能夠訓練前沿品質的模型、透過 Azure 超大規模部署、透過 Copilot 觸達消費端，且整個過程不依賴 OpenAI 的配合。MAI-Thinking-1 是這個架構的一塊基石。其餘部分正在迅速就位，微軟顯然打算在這個十年結束之前讓整棟大廈矗立起來。
