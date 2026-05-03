---
title: "Mistral Medium 3.5 登場：SWE-Bench 達 77.6%，雲端原生編程代理正式推出"
summary: "Mistral AI 發布 Medium 3.5，這是一款 1280 億參數的稠密開源模型，在 SWE-Bench Verified 上拿下 77.6% 的成績，同時推出 Vibe 遠端代理，可從命令列或 Le Chat 非同步啟動雲端編程任務。雙管齊下的發布讓 Mistral 在 Google I/O 2026 前夕對代理式開發工具市場發出強烈訊號。"
category: "developer-tools"
publishedAt: 2026-05-03
lang: "zh"
featured: false
trending: true
sources:
  - name: "Mistral AI"
    url: "https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5"
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/05/02/mistral-ai-launches-remote-agents-in-vibe-and-mistral-medium-3-5-with-77-6-swe-bench-verified-score/"
  - name: "The Decoder"
    url: "https://the-decoder.com/mistrals-new-flagship-medium-3-5-folds-chat-reasoning-and-code-into-one-model/"
tags:
  - "Mistral AI"
  - "開源模型"
  - "編程代理"
  - "開發者工具"
  - "SWE-Bench"
  - "Le Chat"
relatedSlugs:
  - "2026-04-20-app-store-vibe-coding-surge-zh"
  - "2026-04-11-microsoft-agent-framework-1-0-ga-zh"
  - "2026-04-04-cursor-devin-war-zh"
---

Mistral AI 於 5 月 2 日同步推出兩項互為呼應的產品，合力重新定義中階開源模型的能耐：**Mistral Medium 3.5**，一款稠密架構、1280 億參數的旗艦模型，在 SWE-Bench Verified 上拿下 77.6% 的高分；以及 **Vibe 遠端代理**，一個讓開發者從命令列非同步啟動長時間雲端編程任務的執行框架。

發布時機意味深長。Google I/O 距今只剩數週，Anthropic 的 Claude 4 家族持續擴張，OpenAI 更是四面出擊。Mistral 需要一次有力的宣示——Medium 3.5 就是這個答案。

## 一個模型，三種使用情境

Medium 3.5 的核心架構選擇是「稠密」而非「稀疏」。Mistral Large 3 採用 6750 億參數的混合專家（MoE）架構，每個 token 僅啟用約 410 億個活躍參數；Medium 3.5 則讓全部 1280 億參數在每次推理時都完整運作。這樣的設計代價是每個 token 的運算成本更高，但換來的是更高的一致性——尤其在需要連續推理的多步驟代理任務中，稀疏模型的輸出往往飄忽不定。

模型支援 256K token 的上下文視窗，以及原生多模態視覺能力，可直接處理文字、圖片與結構化資料，無需外部轉錄層。推理運算量現在可以在 API 呼叫層級個別設定：開發者可以對簡單查詢調低算力，對複雜多步驟分析調高，同一個模型即可跨兩種需求使用。

在基準測試上，Medium 3.5 繳出了遠超其定價層級的成績。最受矚目的數字——SWE-Bench Verified 77.6%——不僅超越 Mistral 自家的程式碼專用模型 Devstral 2，也擊敗了參數量超過三倍的 Qwen3.5 397B。在 Tau3-Telecom 代理測試上，Medium 3.5 達到 91.4%，顯示在工具呼叫密集的環境中尤為出色。

API 定價方面，輸入每百萬 token 收取 0.40 美元，輸出每百萬 token 收取 1.20 美元，約為 Anthropic 和 OpenAI 同等效能前沿模型的一半價格。

## Vibe 走向非同步與雲端原生

相較於模型本身，此次發布的第二部分對開發者工作流程的衝擊可能更為深遠。

Mistral 的 Vibe 編程工具原本是一個用於互動式代理開發的本地 CLI，現在新增了**遠端代理**功能：在隔離的雲端沙盒中非同步執行的編程任務，並與 GitHub、Slack 和標準 CI/CD 流程原生整合。實際上，開發者只需下達一條指令——「修復這類 bug，開一個 PR」——然後就可以離開螢幕。任務完成後，一個完整的 Pull Request 就會出現在 GitHub 上，附帶完整的 diff、測試結果，以及每個決策的詳細說明。

任務可以從 Vibe CLI 或 Le Chat（Mistral 的消費端助理）啟動。值得一提的是，本地任務可以在執行過程中「傳送」到雲端，而不會遺失任何任務歷史或狀態——這個功能專門為常見情境設計：開發者在本地開始偵錯，發現任務比預期更長，希望繼續執行卻不想讓筆電整夜開著。

沙盒執行架構不只是方便而已，它本身就是一種安全設計。每個遠端代理任務都在一個短暫的隔離環境中執行，沒有持久的檔案系統存取權限，所有憑證都透過 Mistral 的機密管理層在執行時注入。對於擔心 AI 持久存取程式碼庫的企業來說，這個設計直接回應了真實的顧慮。

## Le Chat 推出工作模式

此次發布還預告了 Le Chat 的工作模式（Work Mode），這是一個面向非開發者企業用戶的並行代理介面。工作模式透過內建連接器將 Le Chat 直接與電子郵件、行事曆、Jira、Slack 和文件管理系統整合。模型可以同時跨這些工具執行多步驟工作流程——在單次協調執行中起草專案更新、安排審查會議、更新 Jira 票單。

Mistral 強調的差異化優勢在於：所有工具呼叫和推理步驟都會即時向使用者呈現，任何敏感操作（發送電子郵件、修改行事曆事件）都需要明確確認後才能執行。這是對那些將決策過程黑箱化的自主代理框架的刻意對照。

Le Chat 工作模式瞄準的是 Microsoft 365 Copilot 和 Google Workspace AI 正在積極角逐的同一個企業市場——但它使用的是開源模型，可以部署在私有環境，且大多數使用場景下採用 Apache 2.0 相容授權。

## 競爭格局的重新計算

這次發布的時機與包裝揭示了清晰的策略邏輯。Mistral 一直以來最強的差異化優勢是：開放性、歐洲監管定位（對 GDPR 敏感的企業至關重要），以及競爭性的效能價格比。Medium 3.5 三者兼顧。

相較於 Cursor 和 Devin，Vibe 遠端代理直接在代理編程工作流程上競爭，優勢在於是模型提供商原生的方案，而非包裝層。相較於 Anthropic 的企業產品 Claude for Work 和 Microsoft Copilot，Le Chat 工作模式提供了兩者都無法匹敵的開源部署選項。

基準測試的公信力也很重要。在 API 定價遠低於前沿層級的情況下，1280 億稠密模型拿下 77.6% 的 SWE-Bench Verified，改變了被 GPT-5.5 或 Claude 4 大規模定價排除在外的新創公司和中型企業的評估算式。

## 下一步動向

Mistral 尚未宣布 Medium 3.5 開源權重的確切時程，但從公司過往模式來看，API 發布後約四到八週就會釋出開源權重。`mistralai/Mistral-Medium-3.5-128B` 的 Hugging Face 模型庫已上線，Unsloth 的量化版本也已出現在社群中。

對開發者來說，問題已不在於 Medium 3.5 在基準測試上是否具有競爭力——答案顯然是肯定的。真正的問題是 Vibe 遠端代理的雲端執行模型能否累積出競爭工具已建立的開發者生態引力。這是一個發行通路的問題，而不是技術能力的問題，而這也正是 Mistral 歷史上比技術面更難突破的一環。

幾週後的 Google I/O，以及 Google 對 Gemini 代理開發者生態的宣示，將是這週發布的真正壓力測試。
