---
title: "Grok 4.3 登陸 Amazon Bedrock：xAI 向企業市場全面進攻"
summary: "xAI 的 Grok 4.3 正式在 Amazon Bedrock 上架，成為繼 Anthropic 和 OpenAI 之後第三個進駐該平台的獨立前沿 AI 實驗室。200,000 token 以下的請求，每百萬 token 收 1.25 美元（輸入）、2.50 美元（輸出），是 Bedrock 上最便宜的美國前沿推理模型，搭配 100 萬 token 上下文視窗、可調推理強度，以及 xAI 宣稱的前沿模型中最低幻覺率。部署使用全新「Mantle」推理引擎，開發者需更新 SDK 整合方式。"
category: "developer-tools"
publishedAt: 2026-06-25
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: false
sources:
  - name: "AWS 新功能公告：Grok 4.3 正式在 Amazon Bedrock 上架"
    url: "https://aws.amazon.com/about-aws/whats-new/2026/06/grok-amazon-bedrock/"
  - name: "AWS 部落格：2026 年 6 月 22 日週報——Grok 4.3 進駐 Bedrock"
    url: "https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026/"
  - name: "xAI：Grok on Amazon Bedrock"
    url: "https://x.ai/news/grok-amazon-bedrock"
tags:
  - "xAI"
  - "Grok"
  - "Amazon Bedrock"
  - "AWS"
  - "企業AI"
  - "開發者工具"
  - "推理模型"
  - "Mantle"
relatedSlugs:
  - "2026-06-02-xai-grok-41-fast-enterprise-api-grok5-roadmap-zh"
  - "2026-06-06-openai-gpt55-codex-aws-bedrock-zh"
  - "2026-06-01-amazon-trainium-20b-custom-silicon-zh"
---

Amazon Bedrock 剛迎來第三個主要獨立 AI 實驗室。2026 年 6 月 15 日起，**xAI 的 Grok 4.3** 正式在 Bedrock 平台上線，讓 xAI 與 Anthropic、OpenAI 並列，成為 AWS 托管 AI 服務上第三家主要的獨立實驗室。定價立即引發市場關注：**每百萬輸入 token 1.25 美元、輸出 token 2.50 美元**，是 Bedrock 上所有美國前沿推理模型中最便宜的，差距相當顯著。

## Grok 4.3 帶來什麼

這個模型搭載了一套專為企業生產環境設計的能力：

**100 萬 token 上下文視窗。** Grok 4.3 單一請求可處理至多 100 萬 token，不過超過 200,000 token 的請求會適用較高的計費級距，每 token 費率加倍。

**可調推理強度。** xAI 在企業場景中最獨特的功能是可在四個層次調整推理強度：無、低、中、高。Grok 4.3 的可調強度讓開發者能逐請求平衡延遲、成本與推理深度，對部分查詢需要深度分析、部分只需快速回應的應用場景非常有價值。

**最低幻覺率聲明。** xAI 宣稱 Grok 4.3 在前沿模型中達到最低幻覺率。客服支援、法律研究和財務文件問答都是對準確性要求很高的領域，這個聲明必然會受到嚴格檢驗。

**工具呼叫、結構化輸出、串流。** 三項功能在 Mantle 上全部支援。

## Mantle 的差異

部署架構值得特別說明。Grok 4.3 在 Bedrock 上執行於 Amazon Bedrock 的全新推理引擎 **Mantle**，而非 Claude 等模型使用的標準 Bedrock Runtime。這意味著**現有的 Bedrock SDK 程式碼無法直接相容 Grok 4.3**。

開發者必須使用 `bedrock-mantle` 端點而非 `bedrock-runtime`，API 路徑採用 OpenAI 相容結構，而非大多數 Bedrock 整合依賴的 Converse 或 InvokeModel API。實際影響：把 Grok 4.3 導入現有 Bedrock 應用需要修改程式碼，不能只換模型 ID。

AWS 將 Mantle 描述為為性價比而設計，支援工具呼叫、結構化輸出和串流。Mantle 最終是否會演變為 Bedrock 高效能模型的通用推理基礎設施層，還是僅限 xAI 使用，對開發者的架構選擇有重大影響。

## 定價算術

每百萬 token 輸入 1.25 美元、輸出 2.50 美元，Grok 4.3 在推理模型層的定價遠低於 Bedrock 上最接近的競爭對手：

- **Claude Sonnet 4.6** 在 Bedrock 的定價為每百萬 token 輸入 3.00 美元、輸出 15.00 美元
- **GPT-5.4（透過 Bedrock）** 約為輸入 2.50 美元、輸出 15.00 美元
- **Grok 4.3** 的輸入價格（1.25 美元）不到 Claude Sonnet 4.6（3.00 美元）的一半，輸出價格（2.50 美元）遠低於 Claude Sonnet 4.6（15.00 美元）的五分之一

對高用量企業工作負載而言，每月 token 使用量以數十億計，成本差距呈複利效應。

這種定價壓力不只是開發者的好消息，也反映了托管模型市場競爭的白熱化——隨著前沿實驗室間的模型品質日趨收斂，各家提供商承受著越來越大的降價壓力。

## xAI 的企業化路徑

Grok 4.3 登陸 Bedrock 是 xAI 執行蓄意企業分銷策略最清晰的訊號——而非只靠 Grok 在 X Premium 和 grok.com 上的消費者影響力。

對 Grok 而言，Bedrock 渠道比 xAI 幾乎任何其他分銷決策都更為重要。已在 Bedrock 上開發的團隊，現在可透過 Mantle 端點評估 Grok 4.3，與其他模型在自己的工作負載上直接比較，若性價比划算就可以切換。這比從頭說服企業採購團隊導入全新 AI 供應商要快得多。

## 開發者實務建議

正在評估 Grok 4.3 on Bedrock 的團隊，以下是幾點實務重點：

模型最適合**文件密集、成本敏感的工作負載**，可透過可調推理強度降低簡單查詢的每請求成本。客服支援、網頁開發、法律案例研究和財務文件問答，是 AWS 特別強調的適用工作負載。

**Mantle 端點需要更新 SDK**，請在假設相容性之前先測試現有的 Bedrock 整合。

xAI 的**幻覺率宣稱**，在合規敏感應用中依賴前請務必以自身領域場景驗證。

企業 AI 模型市場正收斂至三到四家前沿模型透過托管平台激烈競爭性價比的格局。Grok 4.3 登陸 Bedrock，是這個收斂過程迄今最重要的一步。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 21 處。*
