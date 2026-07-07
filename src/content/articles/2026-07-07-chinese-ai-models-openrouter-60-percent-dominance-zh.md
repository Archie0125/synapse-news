---
title: "中國 AI 模型掌控全球 API 流量六成，美國份額從七成崩跌至三成"
summary: "中國 AI 服務商已奪得最大公開 AI 路由平台 OpenRouter 超過六成的 Token 消耗量，相較 18 個月前的不足 2% 出現結構性逆轉。DeepSeek、MiniMax、Kimi、小米等四大中國廠商的流量，已集體遠超 Google、OpenAI 和 Anthropic。低至十至二十倍的定價、開放權重可自架，以及媲美美國閉源模型的 coding 評測成績，是這場逆轉的三大驅動力。"
category: "industry"
publishedAt: 2026-07-07
lang: "zh"
featured: false
trending: false
sources:
  - name: "ChatForest — Chinese AI Models Now Own 60% of Global API Traffic"
    url: "https://chatforest.com/reviews/chinese-ai-models-openrouter-dominance-deepseek-kimi-minimax-glm-2026/"
  - name: "TechTimes — DeepSeek Hits 541 Million Visits, Fifth Worldwide"
    url: "https://www.techtimes.com/articles/318181/20260610/deepseek-hits-541-million-visits-fifth-worldwidechina-ai-price-war-tests-us-bills-data.htm"
  - name: "OfficeChai — Share Of US Models Being Used On OpenRouter Has Collapsed From 70% To 30%"
    url: "https://officechai.com/ai/share-of-us-models-being-used-on-openrouter-has-collapsed-from-70-to-30-over-the-past-year/"
  - name: "Data Gravity — China's Open-Weight Takeover"
    url: "https://www.datagravity.dev/p/chinas-open-weight-takeover"
tags:
  - "中國AI"
  - "DeepSeek"
  - "OpenRouter"
  - "AI市場份額"
  - "地緣政治"
  - "開源模型"
relatedSlugs:
  - "2026-07-05-meituan-longcat-2-china-domestic-chips-zh"
  - "2026-07-02-taiwan-super-micro-nvidia-chip-smuggling-probe-zh"
---

2025 年 6 月，美國 AI 服務商——Google、OpenAI 和 Anthropic——在 OpenRouter（全球最大的公開 AI 路由平台）上合計佔有約七成的 Token 消耗量。一年後，這個數字已跌至三成。

反向奪走這份流量的，是中國廠商。根據平台流量數據，截至 2026 年年中，DeepSeek、MiniMax、月之暗面（Kimi）、智譜 AI（GLM）和小米的模型，已合計佔據 OpenRouter 總 Token 消耗量的六成以上。而 18 個月前，這個數字還不到 2%。這是一場以驚人速度完成的結構性市場逆轉。

## 量化這場逆轉

中國廠商在平台上的體量令人咋舌。MiniMax 的 M2.5 模型每月透過 OpenRouter 處理 4.55 兆個 Token；月之暗面的 Kimi K2.6 每月處理 4.02 兆個 Token；小米——相對晚近才進入 AI 模型市場的玩家——每週的處理量高達 4.21 兆個 Token，折算成月度體量已超越前兩者。

截至 2026 年 6 月，DeepSeek V3.2 和 V4 合計佔據約 17.6% 的平台份額。作為對比：DeepSeek 在 OpenRouter 上的 Token 體量，超過了 Google（12.5%）和 OpenAI（8.4%）兩者加總。智譜 AI 的 GLM-5.1 則坐穩第一梯隊的最後一席。

使用結構同樣值得關注。程式碼相關任務目前佔 OpenRouter 總流量的逾五成，而 2025 年初這個比例僅有 11%。中國模型在這一使用場景上進行了針對性優化，其軟體工程任務評測表現已與美國閉源旗艦模型不相上下，定價卻低出數倍乃至十數倍。

## 中國模型為何取得優勢

中國 AI 服務商的競爭邏輯建立在四個相互強化的優勢之上。

**定價**是最直觀的驅動力。中國模型，尤其是可自架的開放權重版本，在同等任務上的定價比美國服務商低 10 至 20 倍。DeepSeek V4 提供的上下文視窗和 coding 能力在評測上可對標美國中階模型，定價卻是其一個零頭。對於正在建構高流量應用的成本敏感開發者而言，這筆帳並不難算。

**開放權重**帶來的是另一層競爭優勢。多款主流中國模型以開放權重形式發布，任何組織都可以下載後在自己的基礎設施上運行，無需按 Token 付費。這不僅吸引了預算有限的新創公司，也讓有資料主權要求的企業、需要大量批次處理的場景，以及偏好基礎設施自主性的組織找到了選擇。自架選項從根本上消除了每次查詢的成本上限。

**超長上下文工程**是另一個重要籌碼。中國 AI 研發投入了大量資源在拉長上下文視窗上。MiniMax M2.5 提供以百萬計 Token 的上下文視窗——這對程式庫級程式碼分析、法律文件審閱和科學文獻綜合尤為有力。

**Coding 專精化**恰好契合了 OpenRouter 流量的轉型方向。在 SWE-Bench、HumanEval 以及各大 AI IDE 的內部評測中，中國模型在 coding 場景上已能與最強的美國 coding 模型在極窄的差距內競爭，且成本為後者的一個零頭。

## 監管與安全的維度

OpenRouter 的數據揭示的是市場故事，但它落在一個讓其含義遠比純粹競爭分析複雜的地緣政治語境中。

將生產流量導向中國控制的 AI 服務商，引發的問題不只是成本優化。中國 AI 模型處理的資料——包括潛在的商業機密、原始碼、客戶資料和戰略通訊——可能受到要求與政府部門配合的中國資料治理法律的管轄。中國科技企業的資料處理法律義務框架，與美國或歐盟的標準存在實質差異。

美國立法者已注意到這一轉變。2026 年已有多項法案被提出，建議限制中國 AI 模型在政府和關鍵基礎設施中的使用。川普政府在 2026 年 5 月推遲了一項原定的 AI 監管框架，使各司法管轄區的前沿模型在敏感場景部署前均缺乏正式的美國評估標準。這個監管空白，實際上讓市場力量在具有國家安全含意的採購決策中主導了走向。

對商業企業而言，建議相對清晰：資料可以分類管理，路由決策可以按任務執行，混合部署可以讓中國模型只處理非敏感的批次任務，敏感資訊則保留給美國模型。

## 對美國 AI 巨頭的意義

OpenRouter 並非整個 AI 市場——它是一個主要由開發者、AI 新創公司和技術型企業使用的路由層。以合規要求、既有廠商關係和風險容忍度為考量的企業採購市場，仍然偏向美國服務商。

但 OpenRouter 是領先指標。推動企業採購轉型的開發者社群，會優先選用最便宜、最有能力的工具，然後向組織推薦。如果一個開發者社群有六成已在使用中國模型，當他們被問及公司應選用哪家 AI 基礎設施時，他們的答案往往也會指向中國廠商。

OpenAI 和 Anthropic 試圖以定價回應——雙方都推出了針對效率層的低成本模型，直接面對中國廠商最強的區間競爭。但這個定價不對稱是結構性的，而非邊際性的：中國實驗室的成本結構更低，以多種形式獲得國家支持，而開放權重模型更是從根本上切斷了開發成本與每 Token 收入之間的連結。

美國廠商更深層的回應方式是差異化：投入在中國實驗室較少聚焦的能力——長程自主任務、前沿推理評測、超越文字與程式碼的多模態能力，以及企業整合深度。這個論點站得住腳，但對於構成 OpenRouter 流量主體的成本敏感開發者而言，說服力有限。

## 台灣開發者的視角

對台灣和亞太地區的讀者而言，OpenRouter 的數據具有特別切身的參考價值。台灣位處美中科技分歧的核心交叉點：台積電同時為美國 AI 實驗室和（在出口管制範圍內的）中國 AI 服務商製造晶片；台灣科技業的開發者社群，對美國和中國 AI 服務都有機會存取，且正在積極使用。

在這樣的情境下，台灣企業和開發者面對的是一個沒有簡單答案的選擇。中國 AI 模型提供的成本效益和能力輪廓極具吸引力；美國 AI 模型提供的是更可預測的合規性，以及與台灣戰略關係的一致性。對多數組織而言，合理的答案不是一刀切向任何一方，而是基於任務分類和資料敏感度的刻意混合策略。

OpenRouter 的數據，呈現的是全球開發者社群在不受合規要求約束時，基於純粹經濟理性所做的選擇。對台灣和世界各地的組織而言，問題在於：這種理性中，有多少能夠在自身的風險邊界內被付諸實踐，又在哪些地方，美國模型的溢價是值得為之付出的代價。
