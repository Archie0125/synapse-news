---
title: "DeepSeek V4 正式發布：1.6 兆參數、每百萬 token 僅 $0.28，直接向西方叫陣"
summary: "中國 AI 新創 DeepSeek 發布迄今最強大的模型 V4，分為旗艦版 Pro（1.6 兆總參數）與輕量版 Flash（每百萬 output token 僅 0.28 美元）。這是該公司一年前震驚矽谷後的再度出擊，也再次證明中國 AI 發展的腳步從未停歇。"
category: "ai-ml"
publishedAt: 2026-04-25
lang: "zh"
featured: true
trending: true
sources:
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/04/24/deepseek-v4-llm-preview-open-source-ai-competition-china.html"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-04-24/deepseek-unveils-newest-flagship-a-year-after-ai-breakthrough"
  - name: "Fortune"
    url: "https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/"
  - name: "MIT Technology Review"
    url: "https://www.technologyreview.com/2026/04/24/1136422/why-deepseeks-v4-matters/"
  - name: "DeepSeek API Docs"
    url: "https://api-docs.deepseek.com/news/news260424"
tags:
  - "DeepSeek"
  - "大型語言模型"
  - "開源"
  - "中國 AI"
  - "混合專家架構"
  - "華為"
relatedSlugs:
  - "2026-04-25-deepseek-v4-flagship-model-release-en"
  - "2026-04-25-cohere-aleph-alpha-merger-sovereign-ai-zh"
  - "2026-04-25-openai-25b-revenue-ipo-plans-zh"
  - "2026-04-24-openai-gpt-5-5-agentic-model-zh"
---

整整一年前，DeepSeek 的 R1 推理模型在矽谷投下震撼彈——單日抹去輝達約 6,000 億美元市值——如今，這家中國 AI 新創帶著更強悍的接班人回歸。2026 年 4 月 24 日，DeepSeek V4 以預覽版形式發布，分為兩個變體，再次宣示該公司在全球大型語言模型競賽中的前沿地位。

這次發布的競爭意義遠超過跑分數字本身。在美國對中國實施大規模晶片出口管制、歐洲各國政府重新思考 AI 主權的時代背景下，DeepSeek 以遠低於西方同業的算力預算持續突破技術極限，正是對「前沿 AI 必須仰賴前沿硬體投入」這個假設的直接挑戰。

## 雙模型、同一架構

DeepSeek V4 以兩款獨立模型面世。**V4-Pro** 是旗艦版：採用混合專家（MoE）架構，總參數量達 **1.6 兆**，每次推理時啟用的參數為 **490 億**。**V4-Flash** 則是更輕、更快的版本，總參數 2,840 億、啟用參數 130 億，專為對延遲與成本敏感的應用場景設計。

兩款模型均支援 **100 萬 token 的上下文視窗**（1,048,576 tokens），允許開發者在單一提示中載入完整程式碼庫、冗長法律合約或多冊研究文獻，其規模與 OpenAI、Anthropic 目前提供的最高水準相當甚至更長。

架構層面最受矚目的創新是 DeepSeek 命名的**混合注意力架構（Hybrid Attention Architecture，HAA）**。傳統 Transformer 在極長上下文中存在眾所周知的效能衰退問題——HAA 透過在不同層次交替使用不同注意力機制來解決這個問題，使模型在整個百萬 token 上下文中保持連貫的記憶能力，同時避免純密集注意力的二次方計算成本。DeepSeek 的技術文件指出，這對需要跨越大量程式行追蹤狀態的程式代理（coding agent）與文件分析工作流程尤其有利。

## 重新定錨的定價策略

DeepSeek 再次以定價作為競爭武器。透過 DeepSeek API，V4-Pro 的 output token 售價為每百萬 **3.48 美元**，V4-Flash 僅需 **0.28 美元**。相較之下，OpenAI o3 的完整推理模式約為每百萬 60 美元，GPT-4.1 為 8 美元，Anthropic Claude Sonnet 4.6 則是 15 美元。

每百萬 token 0.28 美元——比寄一封信還便宜。對於正在建構高吞吐量應用的開發者而言，無論是客服機器人、文件處理流水線還是程式碼審查系統，這樣的定價在經濟層面近乎顛覆性。即便是 V4-Pro 的 3.48 美元，也比多數西方同級前沿模型便宜二到五倍。

DeepSeek 透過 MoE 架構（大幅降低每個 token 的啟用計算量）以及異常高效的訓練流程來實現這樣的定價。公司尚未公開 V4 的訓練成本，但其先前模型的訓練支出一直是美國頂尖實驗室的零頭。

## 開源發布與華為晶片整合

V4 兩款變體均以開放權重（open-weight）模型形式發布，可在 Hugging Face 上下載與微調。這延續了 DeepSeek 的開源傳統，其先前的開放發布多次在全球 AI 社群催生新研究與衍生模型。

地緣政治意涵更重的是，V4 與**華為昇騰 AI 晶片**的深度整合。美國出口管制已實際切斷中國 AI 實驗室取得 NVIDIA H100、H200 GPU 的管道。然而 DeepSeek 非但沒有停滯，反而似乎已全面適應——將 V4 深度優化以運行在華為的國產替代方案上。華為現役旗艦 AI 加速器昇騰 910C 在原始吞吐量上仍落後 NVIDIA 最強硬體，但 V4 以效率為核心的架構設計大幅縮小了這個差距。

這個細節的意義超越 DeepSeek 本身：它表明美國的晶片出口管制雖然造成了衝擊，卻未能阻止中國的前沿模型開發——反而加速了中國對國產晶片的優化投入。

## 跑分表現

DeepSeek 將 V4-Pro 定位為在程式設計、數學與推理任務上接近前沿水準。根據內部基準測試，V4-Pro 在多項程式設計評估中超越 GPT-4.1，並在多步驟推理任務上與 Gemini 3.1 Pro 相當或更優。Chatbot Arena 等平台的獨立評測者已開始將 V4-Pro 列入全球前五，但全面的第三方基準測試結果仍在陸續產出中。

V4-Flash 儘管啟用參數量大幅縮減，在多數標準評測中的表現據報與 GPT-4o-mini 及 Gemini 3.1 Flash 相當——這樣的性價比，西方廠商將很難匹敵。

## 地緣政治的弦外之音

這次發布發生在充滿張力的背景下。中國監管機構近期對 Moonshot AI、StepFun、字節跳動等國內 AI 公司的境外投資展開審查；美國政策制定者則在討論進一步收緊晶片出口管制。DeepSeek 在這個環境中顯得格外特別：一家保持相當開放姿態、可在國際市場使用、且技術可信度持續提升的中國 AI 實驗室。

一週年的時間節點選擇帶有明顯的象徵意味。當 DeepSeek R1 在 2025 年 1 月橫空出世時，西方 AI 圈最初的反應是：這不過是對既有典範的一次聰明工程創新，並非持續的技術能力躍升軌跡。V4 的到來挑戰了這個判斷——在約 18 個月內，DeepSeek 已先後推出 V2、V3、R1 與 V4，每一款都比上一款明顯更強。

## 對企業採用者的意義

對於正在評估模型供應商的技術長與 AI 負責人而言，V4 的發布帶來了切實的抉擇。V4-Flash 的定價對任何目前使用 GPT-4o-mini 或 Gemini Flash 的應用都構成強烈誘惑——成本節省的幅度難以忽視。V4-Pro 則在模型品質優先、且資料存放合規要求允許使用 DeepSeek API 的工作場景中，進入嚴肅的候選名單。

持續存在的顧慮是可靠性與企業支援。DeepSeek 的 API 基礎設施雖然比一年前穩健許多，但在尖峰需求下仍偶有可用性問題。對於任務關鍵的企業部署，許多組織可能更傾向在自有基礎設施上運行開放權重版本——而此次的開源發布使這成為可能。

來自杭州的訊號已經清晰：AI 競賽仍然勝負未定，成本曲線仍在下探，西方廠商無法對自己的領先地位高枕無憂。
