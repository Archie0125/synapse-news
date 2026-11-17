---
title: "Kimi K3開源週日登場：2.8兆參數創開源模型歷史之最，自架部署成真正選項"
summary: "Moonshot AI預計於7月27日在Hugging Face釋出Kimi K3完整模型權重，使這個2.8兆參數的模型成為迄今規模最大的開源釋出。對於擔心敏感資料流經中國伺服器的企業而言，自架部署在技術上成為切實可行的選擇，儘管硬體需求相當嚴苛。"
category: "ai-ml"
publishedAt: 2026-07-26
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "Kimi 官方部落格"
    url: "https://www.kimi.com/blog/kimi-k3"
  - name: "Labellerr"
    url: "https://www.labellerr.com/blog/kimi-k3-world-first-open-2-8t-ai-model/"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/321551/20260725/kimi-k3-open-weights-arrive-sunday-self-hosting-cuts-china-data-risk-api-never-can.htm"
tags:
  - "Kimi K3"
  - "月之暗面"
  - "開源模型"
  - "大型語言模型"
  - "中國AI"
  - "自架部署"
  - "混合專家"
relatedSlugs:
  - "2026-07-17-moonshot-kimi-k3-open-weight-model-zh"
  - "2026-07-24-moonshot-ai-kimi-k3-treasury-sanctions-anthropic-distillation-zh"
  - "2026-07-07-chinese-ai-models-openrouter-60-percent-dominance-zh"
---

台灣時間7月27日上午8點（UTC 0點），月之暗面（Moonshot AI）將在Hugging Face公開Kimi K3的完整模型權重，讓這個2.8兆參數的模型成為有史以來規模最大的公開可下載AI模型——參數量幾乎是其前代Kimi K2.6的三倍。

這次開源釋出，是Kimi K3自7月16日透過API上線以來持續引發業界關注的最終章。K3在前端程式碼競技場（Frontend Code Arena）拿下1,679分奪冠，超越Claude Fable 5（1,631分）、GPT-5.6 Sol（1,618分）和智譜GLM-5.2（1,587分）。在研究生程度科學推理基準GPQA Diamond上，K3以93.5%拿下開源模型最強成績；在測試網路研究能力的BrowseComp上以91.2%，成為發布時某個追蹤榜單上已公布的最高分。

但基準測試只是故事的一部分。開源釋出為所有曾使用K3 API、卻暗自擔憂資料流向的企業，帶來了截然不同的部署邏輯。

## K3架構的三大創新

K3採用混合專家（MoE）架構，但並非傳統設計。在896位專家中，每個Token只激活16位——激活率僅1.8%，使每個Token的運算量維持在可接受範圍內，儘管總參數量已達兆級規模。三項架構創新讓K3有別於以往的大型MoE模型：

**Kimi Delta Attention（KDA）**：混合線性注意力機制，在百萬Token長文本場景下可實現最高6.3倍的解碼加速。長上下文處理過去需要龐大算力支撐，KDA使其在推論層面具備實際競爭力。

**Attention Residuals（AttnRes）**：在不到2%的額外計算開銷下，將訓練效率提升約25%。這主要是訓練效率的突破，讓Moonshot能在相同算力預算內注入更多訓練信號。

**Stable LatentMoE**：實現1.8%激活率的專家路由機制，並宣稱解決了大型MoE模型長期存在的路由崩潰問題。此外，模型原生支援視覺輸入，並提供100萬Token的上下文窗口，對企業文件處理與程式碼庫分析工作流程具有實際意義。

## 自架部署的核心價值與硬體現實

自架K3最直接的理由是資料主權。呼叫Kimi API時，提示詞——可能包含專有程式碼、內部文件或敏感客戶資料——會路由至Moonshot在中國的基礎設施。對許多使用情境來說，這種曝露是可以接受的；但對受監管行業、政府承包商、國防相關應用，或任何已徵詢中國資料處理法律意見的組織而言，則是難以接受的風險。

自架K3徹底消除這種路由。權重歸使用者所有，可在自有算力上執行、審視修改，並進行稽核。截至7月25日，K3的具體授權條款尚未公布，因此部署前應先從K3儲存庫確認其商業使用條款。

然而硬體現實並不輕鬆。Moonshot建議以64塊以上加速器的「超節點」配置進行生產部署。據第三方分析，採用MXFP4四位元精度時，K3的權重在計入執行時緩衝區與鍵值快取之前，就需要約1.4TB的高速記憶體。

對多數團隊而言，這排除了在地端自架的可能。實際可行的中間路線，是透過Fireworks AI、Together AI、Baseten等託管推論服務提供商部署K3——在美國或歐盟法律框架下取得合約性的資料主權保障，同時免於硬體自購負擔。多家服務商已確認將於7月底前提供K3託管服務。

## 中國開源模型的戰略邏輯

K3的釋出時機經過精心計算。月之暗面正在籌備以500億美元估值赴港上市，開源釋出旨在上市路演前最大化社群聲量與基準排名能見度。DeepSeek則另謀以710億美元估值在上海掛牌；開源模型的競賽，已與中國AI企業的資本市場雄心深度交織。

地緣政治面向同樣不可忽視。另有地緣政治面向：白宮指控月之暗面蒸餾Anthropic的Fable模型來打造K3，財政部長貝森特（Scott Bessent）也威脅實施制裁，不過截至7月25日，尚未宣布任何針對K3的執法行動。

## K3在開源生態系的定位

在K3之前，規模最大的開源模型擁有一兆參數。K3的2.8兆總參數（每個Token激活490億）堪稱另一個重量級別。在基準表現上最接近的競爭者，是Mistral的LeanStral 1.5與Meta的Watermelon模型，但兩者在程式設計與研究任務上均落後K3。

對於需要接近前沿性能且不願被商業API綁定的開發者而言，K3是目前最清晰的選擇。DeepSeek V4-Flash以每百萬Token 0.14美元輸入、0.28美元輸出持續壓低價格，但K3在長上下文與程式設計任務上的架構優勢，足以支撐其較高API定價（每百萬Token輸入3美元、輸出15美元）在生產環境中的合理性。

## 開源後的觀察重點

權重釋出後，社群反應將立即展開。針對程式設計、數學和指令遵循的微調實驗，預計在數小時內啟動。幻覺率是值得關注的一點：Artificial Analysis在AA-Omniscience上測得K3的幻覺率約為51%，高於Kimi K2.6的39%，而Moonshot自家圖表並未包含這項數字。

截至7月25日，K3的授權條款尚未公布，因此商業微調版本和衍生模型能被自由打造到什麼程度，仍待確認。

K3的釋出，恰好發生在開源AI生態系正歷經結構性轉變的時刻。市場正在觀察：一個2.8兆參數的模型，究竟能否在真實的前沿部署場景中被實際使用——還是僅僅刷新了一項參數量紀錄，而對多數使用場景仍不切實際？

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 9 處。*
