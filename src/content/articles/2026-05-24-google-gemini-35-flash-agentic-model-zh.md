---
title: "Google Gemini 3.5 Flash：為代理人工作負載而生的新一代前沿模型"
summary: "Google 在 I/O 2026 發布了 Gemini 3.5 Flash，這是 3.5 系列的首款模型，結合了前沿級別的智慧與代理人及程式碼任務所需的速度。模型在所有主要代理人基準測試上超越 Gemini 3.1 Pro，同時速度快四倍，標誌著 Google 在模型定位上從對話能力轉向代理人效能的重大轉變。"
category: "ai-ml"
publishedAt: 2026-05-24
lang: "zh"
featured: false
trending: false
sources:
  - name: "Google DeepMind"
    url: "https://deepmind.google/models/gemini/flash/"
  - name: "Google Blog"
    url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/"
tags:
  - "google"
  - "gemini"
  - "ai-model"
  - "agentic-ai"
  - "developer-tools"
relatedSlugs:
  - "2026-05-20-google-io-2026-keynote-gemini-spark-xr-glasses-zh"
  - "2026-05-19-google-io-2026-developer-tools-gemma4-gemini32-firebase-zh"
---

5 月 19 日，Google 在 I/O 2026 上發布 Gemini 3.5 Flash 時，帶來了一個不尋常的定位宣言：這不是一個主要為聊天機器人設計的模型。它是為**代理人**而生的——為程式設計、為定義下一代軟體的長期多步驟任務而生。藉此，Google 劃下了一條分界線，終結了主要以對話品質衡量模型發布的時代，並宣告了一個新的競爭維度：每美元、每秒的代理人能力。

根據 Google 的數據，這款模型在每一項主要代理人與程式碼基準測試上都超越了上一代旗艦 Pro 模型，同時速度快四倍，API 定價也顯著更低。它是 3.5 系列的第一款成員；Gemini 3.5 Pro——目前仍在 Google 內部測試——預計於 2026 年 6 月向公眾推出。

## 基準測試成績

Google 為 Gemini 3.5 Flash 公布的數字足夠具體，能夠確立模型的競爭定位。在 Terminal-Bench 2.1（評估模型在終端機環境中完成真實程式設計任務的能力的業界標準）上，3.5 Flash 得分為 **76.2%**。在 GDPval-AA（以 Elo 評分系統衡量真實世界代理人任務的表現）上，模型達到了 **1,656 分**。MCP Atlas——一個專門評估模型與模型情境協議（MCP）伺服器互動能力的基準——得到 **83.6%**。

多模態表現同樣亮眼。在 CharXiv Reasoning（評估模型理解和推理複雜科學圖表的能力）上，3.5 Flash 達到 **84.2%**，反映了 Google 在 Gemini 系列上持續投入的多模態訓練。

「速度比競爭前沿模型快四倍」這一說法，在代理人情境下意義重大。代理人工作流程對延遲的敏感程度，遠比單輪問答互動高得多。一個生成十個並行子代理人來調查程式碼庫不同部分的程式碼代理人，需要每個子代理人在幾秒鐘內返回結果——而不是幾分鐘——才能讓整體工作流程具備實用性。速度在代理人情境中不只是使用者體驗的優化，更是整個類別應用得以實現的前提條件。

## 定價與可用性

Gemini 3.5 Flash 即時可用，支援多個 Google 管道：Google AI Studio 中的 Gemini API、Google Antigravity 代理人優先開發平台、Gemini Enterprise Agent Platform、Android Studio，以及 Gemini 應用程式和 Google 搜尋的 AI Mode。

API 定價採分層結構。標準層定價為每百萬輸入 token **1.5 美元**、每百萬輸出 token **9 美元**，快取輸入 token 為每百萬 0.15 美元。思考變體（thinking variant）——啟動模型的鏈式推理能力，適合需要多步驟思考的任務——定價為每百萬輸入 token **0.5 美元**、每百萬輸出 token **3 美元**。Google 表示思考變體的定價「不到同等前沿替代品費用的一半」，這顯然是針對 OpenAI o 系列推理模型和 Anthropic 擴展思考模式的競爭定位。

在 Antigravity 上的可用性尤其值得關注。Google 新發布的 Antigravity 2.0 平台以 3.5 Flash 為主力模型，當代理人使用新版 Antigravity 框架運行 3.5 Flash 時，可以在單次執行中生成多個並行子代理人——實現分散式任務執行，這在更慢、更昂貴的模型上根本不具備經濟可行性。

## 3.5 Flash 與前幾代有何不同

Gemini 模型的命名規則過去並不直覺。Flash 版本以往被定位為 Pro 模型的精簡替代品——更快但能力更弱。Gemini 3.5 Flash 打破了這種取捨：它在代理人和開發者最重視的基準上超越了上一代 Pro，同時維持了 Flash 級別的速度和定價。

Google 將 3.5 系列的設計哲學描述為「將前沿智慧與行動力相結合」——這個措辭標誌著與「模型即神諭」範式的刻意告別。前幾代 Gemini 針對知識檢索和問答進行優化；3.5 則明確針對**跨多個步驟、工具調用和環境互動展開的任務**進行優化。模型在指令遵循、工具使用和執行錯誤恢復上投入了大量訓練——這些能力在模型不只是生成文字、而是作為軟體環境中的自主執行者時至關重要。

在技術層面，Gemini 3.5 Flash 原生支援模型情境協議（MCP），能夠與 MCP 伺服器——數據連接器、代碼執行環境、API 包裝器——直接交互，無需額外配置。鑑於 MCP 已成為代理人工具整合的主導標準（獲 Anthropic、OpenAI 及日益壯大的第三方工具生態系統支持），3.5 Flash 的原生 MCP 支援讓它與大多數現代代理人架構即插即用。

## Pro 版即將到來，且已在 Google 內部使用

Google 在 I/O 上確認，Gemini 3.5 Pro——系列中更大、能力更強的模型——已在 Google 內部生產環境中投入使用，用於複雜推理任務、文件分析和研究輔助，公開性能被描述為「在開放式推理基準上顯著強於」3.5 Flash。公開推出計劃在 2026 年 6 月。

3.5 系列中 Pro 與 Flash 之間的差距，預計將窄於前幾代，反映了讓兩個層級保持在具競爭力的性能範圍內的刻意策略。Google 的定位邏輯是：3.5 Flash 展示前沿性能可以用一個讓大規模代理人部署具備經濟可行性的價格點獲得，而 Pro 服務的是那些無論成本如何都需要最大可用能力的用戶和企業。

## 競爭格局

此次發布正值 AI 模型市場在代理人前線競爭最激烈的時刻。Anthropic 的 Claude Sonnet 4.6 已成為許多程式碼代理人部署的預設模型。OpenAI 的 o3 和 GPT-5.5 佔據推理和通用場景。Meta 的 Llama 4 Maverick 主導開放權重部署。

Google 以 Gemini 3.5 Flash 的策略，是將自己定位為在託管基礎設施上實現前沿代理人性能最快、最經濟的路徑。強勁的基準數字、具競爭力的定價（尤其是思考變體），加上與 Google 開發者技術棧的深度整合——Antigravity、AI Studio、Firebase、Android Studio——為已在 Google 生態系統中的開發者提供了引人注目的選擇。

對更廣泛的市場而言，3.5 Flash 的意義在於它對模型發展方向的預示。下一個競爭前沿不以參數量或單輪推理測試衡量，而是以模型能以多可靠、多快速、多低廉的方式，在真實環境中完成真實任務來衡量——而 Gemini 3.5 Flash 是 Google 迄今為止，在這個維度上認真競爭的最直接宣言。
