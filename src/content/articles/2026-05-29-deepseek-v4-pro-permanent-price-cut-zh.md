---
title: "DeepSeek 將 V4-Pro 價格調降 75%，全球 AI 推論定價戰正式升級"
summary: "DeepSeek 將旗艦模型 V4-Pro 的價格調降 75%，降價後快取命中價格每百萬 token 起價為 0.003625 美元，輸出每百萬 token 為 0.87 美元，這是 InfoWorld 對該公司公告的報導。"
category: "ai-ml"
publishedAt: 2026-05-29
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: false
sources:
  - name: "The Next Web"
    url: "https://thenextweb.com/news/deepseek-v4-pro-price-cut-75-percent"
  - name: "InfoWorld"
    url: "https://www.infoworld.com/article/4176709/deepseeks-steep-v4-pro-price-cut-escalates-ai-pricing-war.html"
  - name: "US News & World Report"
    url: "https://money.usnews.com/investing/news/articles/2026-05-23/chinas-deepseek-to-make-permanent-75-price-cut-on-flagship-v4-pro-ai-model"
  - name: "DeepSeek API 文件"
    url: "https://api-docs.deepseek.com/quick_start/pricing"
tags:
  - "deepseek"
  - "ai定價"
  - "大語言模型"
  - "api"
  - "中國ai"
  - "推論"
  - "開發工具"
relatedSlugs:
  - "2026-05-26-cursor-composer-25-kimi-k25-coding-agent-zh"
  - "2026-05-27-open-weight-ai-guardrails-heretic-abliteration-zh"
  - "2026-05-23-openai-q1-2026-revenue-57b-codex-losses-zh"
---

據 InfoWorld 報導，DeepSeek 在公告中宣布將旗艦模型 V4-Pro 的價格調降 75%。

新價格：輸出每百萬 token 最高 **0.87 美元**，快取命中每百萬 token 最低 **0.003625 美元**（DeepSeek 同時將整個 API 套件的快取命中價格降至原有水準的十分之一）。對照 Claude Opus 4.7 的每百萬輸入/輸出 5 美元/25 美元，這個差距不是四捨五入的誤差，而是一個數量級的分野。對於大規模、成本敏感型工作負載——法律文件審查、程式碼分析管線、企業資料萃取——開發者正在以過去 18 個月前難以想像的價格取得接近前沿等級的 AI 能力。

## V4-Pro 是什麼樣的模型

要理解降價的意義，必須先理解這個模型本身。DeepSeek-V4-Pro 採用**1.6 兆參數的混合專家（MoE）架構**，每次前向傳遞激活約 490 億個參數。這個區別在推論經濟學上至關重要：模型擁有 1.6 兆參數的知識容量，但在多數查詢中的算力消耗接近一個小得多的 490 億稠密模型。

上下文視窗預設為 **100 萬 token**——這是企業用例的關鍵差異點，適用於大型程式碼庫、大量法律合約或龐大文件資料庫。DeepSeek 透過壓縮稀疏注意力（CSA）與重度壓縮注意力（HCA）的創新組合實現了這項能力，在 100 萬 token 上下文長度下，每 token FLOPs 僅需前代 V3.2 的 27%，KV 快取記憶體僅需 10%。

在基準測試上，V4-Pro 在 **SWE-bench Verified 達 80.6%**（被廣泛視為真實世界程式設計任務最可靠的代理指標）、**LiveCodeBench 達 93.5**。在超長上下文檢索上，V4-Pro-Max 在 MRCR 1M 測試達 83.5%，超越 Gemini 3.1-Pro。美國 NIST CAISI 的獨立評估認為，V4-Pro 的能力落後前沿約 8 個月，但在 7 個評估基準中的 5 個上，比可對比的美國模型更具成本效益。

近乎前沿的編碼能力、百萬 token 上下文、MoE 推論效率——正是這個組合，讓七五折降價的意義超越了普通的價格競爭。

## 中國 AI 實驗室的競爭格局

2025 年 1 月 DeepSeek R1 的發布更像是一次奇襲，而現在的格局看起來更像是一種持續的策略：壓縮定價以驅動 API 採用。

V4-Pro 在 SWE-bench 上的 80.6%，確實低於 Claude Opus 4.7 和 GPT-5，但已足夠接近，使得對於 90% 不需要絕對最先進推理能力的真實世界編碼任務而言，成本差距比能力差距更重要。

## 對西方 AI 廠商商業模式的衝擊

這次降價在一個讓 Anthropic、OpenAI 和 Google 都感到棘手的時間點出現。三家公司都在建立收入預測，而這些預測的隱含前提是：企業 AI 定價能夠在足夠長的時間內維持現有水準，以支撐下一代模型訓練的龐大開支。DeepSeek 的動作從兩個維度挑戰了這個假設。

其一，它直接壓縮了高量、成本敏感型推論工作負載的可尋址市場，而這正是西方廠商以接近算力成本加利潤率定價的主戰場。其二，它加速了「推論商品化」的敘事——這對任何以「智能即服務」為商業模式的公司都是結構性的不舒服。

Anthropic 在這個動態中的處境相對微妙。其超過 450 億美元的年化營收表明，公司成功銷售的不僅僅是原始推論能力，而是企業整合、Constitutional AI 的信任溢價，以及受管代理編排能力——這些都能支撐高於純 API 定價比較所呈現的溢價。

## 被低估的快取定價革命

DeepSeek 公告中最被忽視的細節，是其整個 API 套件快取命中定價降至原有水準的**十分之一**。快取命中之所以重要，是因為在生產 AI 應用中——維持跨對話上下文的對話系統、反覆存取相同知識庫片段的 RAG 管線、對同一程式碼庫持續運作的程式設計助手——相當大比例的推論請求是從快取而非重新計算中服務的。

每百萬快取 token 僅 0.003625 美元，DeepSeek 等於讓快取推論幾乎免費。對於有意識設計高快取命中率的生產應用，實際每次查詢成本遠低於輸入定價的頭條數字。一個在 50 萬 token 程式碼庫上下文中運行、達到 70% 快取命中率的程式設計助手，其實際每次查詢成本在任何西方服務商的定價下都難以預算。

## 地緣政治風險不可忽視

對 DeepSeek 定價的任何分析都無法迴避監管層面。NIST CAISI 已完成 V4-Pro 的評估，目前該模型對美國開發者不受限制開放。但 2026 年 5 月浮現的中國 AI 人才出境管制，以及更廣泛的美中科技脫鉤背景，給任何在 DeepSeek API 上構建關鍵基礎設施的企業架構師帶來了長期可用性風險。

部分企業已在響應：選擇在自有基礎設施（本地或美國雲端）上運行 DeepSeek 開源權重版本，而非使用其託管 API。DeepSeek 公開發布模型權重的做法意味著，定價訊號是在託管 API 競爭層面，而技術本身無論地緣政治如何演變都可繼續取用。

對整個 AI 產業而言，這次七五折降價與其說是一個定價事件，不如說是一個市場結構事件。它確立了一條競爭對手無法忽視的新下限，且這條下限建立在足以服務相當大比例真實企業工作負載的能力水準之上。薩蒂亞·納德拉與山姆·奧特曼在過去一年各種財報電話中先後提及的定價戰，已不再是未來情境，而是當下現實。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 14 處。*
