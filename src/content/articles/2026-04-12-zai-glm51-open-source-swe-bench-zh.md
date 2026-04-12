---
title: "Z.ai 的 GLM-5.1 成為首個登頂 SWE-Bench Pro 的開源模型——全程跑在華為晶片上"
summary: "中國 AI 實驗室 Z.ai 發布 GLM-5.1，這款擁有 7,540 億參數的開源模型在 SWE-Bench Pro 上拿下 58.4% 的成績，超越 GPT-5.4 與 Claude Opus 4.6，成為首個在業界最嚴苛程式碼修復基準上擊敗所有閉源模型的開放權重系統。更引人注目的是，整個訓練流程完全在華為昇騰 910B 晶片上完成，未使用任何 Nvidia 硬體。"
category: "ai-ml"
publishedAt: 2026-04-12
lang: "zh"
featured: false
trending: true
sources:
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/04/08/z-ai-introduces-glm-5-1-an-open-weight-754b-agentic-model-that-achieves-sota-on-swe-bench-pro-and-sustains-8-hour-autonomous-execution/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/ai-joins-the-8-hour-work-day-as-glm-ships-5-1-open-source-llm-beating-opus-4"
  - name: "Hugging Face"
    url: "https://huggingface.co/zai-org/GLM-5.1"
  - name: "Winbuzzer"
    url: "https://winbuzzer.com/2026/04/09/z-ai-releases-glm-5-1-754b-model-tops-swe-bench-pro-xcxwbn/"
tags:
  - "開源"
  - "Z.ai"
  - "GLM-5.1"
  - "智譜AI"
  - "SWE-Bench"
  - "自主代理"
  - "華為昇騰"
  - "程式碼AI"
relatedSlugs:
  - "2026-04-05-google-gemma-4-apache-en"
  - "2026-04-06-deepseek-v4-huawei-chips-en"
  - "2026-04-04-open-source-llm-race-en"
---

多年來，開源 AI 社群始終在一個尷尬的處境中掙扎：在最嚴苛的軟體工程基準上，頂尖的開放模型總是能*幾乎*追上，卻從未真正超越閉源巨頭。2026 年 4 月 7 日，這個局面改變了。

Z.ai——北京清華系 AI 實驗室智譜 AI（Zhipu AI）旗下的商業平台——發布了 GLM-5.1：一個擁有 7,540 億參數的混合專家（MoE）模型，以 MIT 授權完全開放，並成為第一個在 SWE-Bench Pro 上奪冠的開源系統。

## 成績到底有多亮眼？

GLM-5.1 在 SWE-Bench Pro 上拿下 58.4% 的得分，超越了 OpenAI 的 GPT-5.4 和 Anthropic 的 Claude Opus 4.6。三天後（4 月 10 日），該模型在 Code Arena 排行榜上以 1,530 Elo 分位列全球第三，僅次於 claude-opus-4-6-thinking（1,548 分）和 claude-opus-4-6（1,542 分）——這是開源模型首次進入 Code Arena 前三名。對比上一代 GLM-5.0，單次發布 Elo 就跳升了 90 分，進步幅度驚人。

## GLM-5.1 的核心設計：為「長時間自主工作」而生

GLM-5.1 的設計目標不是通用聊天機器人，而是**代理工程（agentic engineering）**——能夠長時間、多步驟地執行複雜軟體任務，並在過程中自我規劃、執行、偵錯與迭代。

在基準演示中，模型能在無人介入的情況下持續運行長達八小時：讀取現有程式碼庫、理解問題描述、撰寫修補程式、執行測試、分析失敗原因，最終交付可通過審查的解決方案。這讓它直接與 OpenAI 的 Devin 後繼產品和 Anthropic 的 Claude Code 競爭，而非只在靜態聊天排行榜上較勁。

在架構上，GLM-5.1 採用 MoE + DSA（分解稀疏注意力）設計，搭配非同步強化學習訓練。儘管總參數量高達 7,540 億，但每個 token 只有約 370 億參數被激活，使推論成本接近同等規模的稠密模型。上下文視窗支援 200,000 tokens，最大輸出達 128,000 tokens，足以處理大型程式碼庫的完整上下文。

模型權重完整公開於 Hugging Face，支援 SGLang、vLLM、xLLM、Transformers 和 KTransformers 本地部署，並提供與 OpenAI SDK 相容的 API 存取介面。

## 真正的地緣政治炸彈：零 Nvidia 硬體

GLM-5.1 發布說明中最具衝擊力的一句話：「訓練全程使用華為昇騰 910B 晶片，未使用任何 Nvidia 硬體。」

這是迄今為止最大的、已公開確認在中國自主硬體上完成訓練的前沿等級模型。時間點尤為敏感——美國國會正在審議 MATCH 法案（Multilateral Alignment of Technology Controls on Hardware Act），擬將出口限制延伸至深紫外線（DUV）微影設備，封堵外界認為目前仍存在的最後漏洞。

但 GLM-5.1 的成果暗示：西方政策制定者所預設的「晶片封鎖可以維持技術差距」的邏輯，可能已經失效。中國 AI 實驗室已在國產算力上訓練出能夠在特定基準上超越 H100/H200 叢集產物的模型。

Z.ai 的一位工程師在發布貼文中直言：「用昇騰訓練 GLM-5.1 不是不得不為之的替代方案，這從第一天起就是我們的計畫。昇騰 910B 的算力足以支撐前沿訓練，前提是你得知道怎麼用。」

## SWE-Bench Pro 在測什麼？

SWE-Bench Pro 是 2026 年初推出的升級版，從真實 GitHub 倉庫中挑選生產級 Python 問題，要求模型讀懂現有程式碼、理解錯誤報告、撰寫修補程式，並通過既有測試套件。與合成基準不同，它難以被「刷題」——測試案例對外保密，而且問題來自具有複雜相依關係的真實專案。

58.4% 的得分意味著：在這類有明確文字描述的程式碼問題中，GLM-5.1 超過一半的時間輸出的修補品質達到資深工程師水準。這不代表它能解決所有工程問題，但對於 SWE-Bench 所選定的問題類型，它已與人類頂尖工程師難分高下。

## 對行業的三重衝擊

**開源在程式碼能力上已追平閉源。** 對於軟體工程任務，GPT 和 Claude 的付費優勢已被實質抹平。任何建構在閉源 API 上的程式碼工具公司，現在都面對一個免費、MIT 授權、效能相當甚至更優的替代選項。

**中國的 AI 自主供應鏈已成形。** GLM-5.1（昇騰 910B 訓練）加上即將推出的 DeepSeek V4（據報道使用昇騰 950PR），說明中國頂尖 AI 實驗室已建立起完全獨立於美國管制硬體之外的端到端訓練體系。

**代理基準取代靜態問答成為評估核心。** 「這個模型能自主工作多久？」正在取代「這個模型有多聰明？」成為最關鍵的問題。GLM-5.1 八小時自主運行的設計，標誌著行業評估視角的根本轉移。

## 接下來的走向

Z.ai 表示，GLM-5.1 是 2026 年底全模態代理產品的前奏，公司正在擴充開發者平台，加入工具呼叫、沙盒程式碼執行和長期記憶等功能——這些目前還只有 Claude Code 和 OpenAI Operator API 等閉源平台才有。

對開發者而言，機會已經擺在眼前：一個達到業界最頂尖水準的程式碼模型，現在可以免費取得、無使用限制，甚至能透過量化版本在消費級硬體上本地部署。

第一個真正意義上的開源前沿程式碼代理已經到來，它誕生於北京，跑在華盛頓試圖封鎖的晶片上。
