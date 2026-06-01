---
title: "Amazon 自研晶片業務突破 200 億美元年收入，成為獨當一面的業務"
summary: "執行長 Andy Jassy 確認，Amazon 旗下包含 Trainium、Inferentia 與 Graviton 的自研晶片部門，年化營收已突破 200 億美元，年增超過 100%。隨著 Trainium3 開始出貨，且 OpenAI、Anthropic、Meta 與 Uber 均已簽訂多年採購承諾，Amazon 正在超大規模雲端領域對 Nvidia AI 晶片主導地位展開最具說服力的挑戰。"
category: "hardware"
publishedAt: 2026-06-01
lang: "zh"
featured: false
trending: false
sources:
  - name: "The Next Web"
    url: "https://thenextweb.com/news/amazon-custom-chips-jassy-letter-fifty-billion-trainium"
  - name: "StartupHub.ai"
    url: "https://www.startuphub.ai/ai-news/technology/2026/amazon-s-chip-business-surges-past-20b"
tags:
  - "Amazon"
  - "AWS"
  - "Trainium"
  - "Inferentia"
  - "自研晶片"
  - "AI 晶片"
  - "Nvidia"
  - "雲端運算"
relatedSlugs:
  - "2026-06-01-amazon-trainium-20b-custom-silicon-en"
  - "2026-05-30-groq-650m-raise-nvidia-20b-lpu-neocloud-zh"
---

Andy Jassy 的年度股東信通常會有一兩句話，足以讓整個產業在接下來的一年反覆解讀。今年，其中一句關於晶片。Amazon 自研晶片業務——涵蓋用於 AI 訓練的 Trainium 加速器、推論導向的 Inferentia 晶片，以及通用運算的 Graviton 處理器——已突破年化 200 億美元的收入規模，Jassy 證實，且年增率超過 100%。

放入脈絡來看：200 億美元的年收入，足以讓 Amazon 的晶片部門以獨立業務之姿站穩腳跟，規模超過許多大眾耳熟能詳的半導體公司。而這個部門在五年前根本不具備任何有意義的商業規模。

## 支撐這個數字的晶片

Trainium 與 Inferentia 是為 AI 工作負載量身打造的，其效率超越通用 CPU 所能企及，甚至在特定場景下也比 Nvidia GPU 更具優勢。這兩款晶片圍繞 Transformer 模型訓練與推論的核心矩陣乘法運算設計，記憶體架構針對大規模注意力機制計算的存取模式進行了深度優化。

2025 年全面上市的 Trainium2，在 Transformer 訓練工作負載上，比同等 Nvidia H100 配置提供了約 30% 的性價比優勢——以 Amazon 的運算規模來看，這是相當可觀的差距。長期以來的瓶頸始終在於軟體：Nvidia 的 CUDA 生態系根深柢固，遷移工作負載需要投入大量工程資源。對於有能力負擔這筆遷移成本的超大規模雲服務商而言，經濟效益完全合理；對規模較小的組織而言，CUDA 綁定依然是真實存在的阻力。

2026 年初開始向特定客戶出貨的 Trainium3，進一步帶來 30-40% 的效能提升。這款晶片採用 Chiplet 架構，讓 Amazon 能獨立擴展運算與記憶體模組——這套方法論借鑒自 AMD Zen 處理器的設計哲學，並應用到 AI 加速器上。來自客戶的早期基準測試資料顯示，Trainium3 在標準 LLM 訓練配置下效能比肩或超越 H200，同時維持 Trainium2 的成本優勢。

推論導向的 Inferentia 則在企業 AI 部署從概念驗證轉向生產環境的過程中，迎來了更陡峭的採用曲線。大規模推論本質上是成本問題，而 Inferentia 相比 A100/H100 推論基礎架構更低的每 token 成本，帶動了高流量用戶的大量採用。Graviton 則作為 Amazon 的 Arm 架構通用運算處理器，扛起了非 AI 類 AWS 工作負載的骨幹。

## 客戶名單才是真正的故事

Amazon 晶片資訊揭露中最具戰略意義的細節，不是 200 億美元這個數字，而是客戶名冊。根據 Amazon 公佈的資訊，OpenAI、Anthropic、Meta 與 Uber 均已簽訂 Trainium 基礎設施的多年承諾。

OpenAI 的參與格外引人注目。這家公司今年稍早宣佈的 500 億美元 AWS 投資承諾中，包含了大量 Trainium3 配置。OpenAI 與微軟的商業合作讓 Azure 成為其首要雲端供應商，但它同時也對 AWS Trainium 做出有意義的承諾——這反映出在當前的 AI 運算需求規模下，任何單一硬體供應商都無法作為唯一依賴。

Anthropic 對 Trainium 的承諾是其數十億美元 AWS 合作的正式組成部分，並與公司持續使用 Google Cloud 及自有基礎設施的策略並行。這種冗餘設計出於刻意選擇：對於在前沿進行模型訓練的公司而言，擁有多條硬體路徑，能降低 2023-2024 年 GPU 短缺期間讓眾多 AI 公司切身感受到的單點失效風險。

Meta 的採用或許是其中技術上最有意思的案例。Meta 的研究團隊最初在 Nvidia 硬體上建構訓練基礎架構，內部 AI 框架也針對 CUDA 優化。將相當比例的訓練工作負載遷移至 Trainium，需要大量的軟體工程投入——Meta 願意做出這項投資，恰恰反映出背後成本節省的規模之大。

## Jassy 的 500 億美元藍圖

在股東信中，Jassy 的描述不只是確認 200 億美元這個數字。他表示 Amazon 晶片業務有潛力在「幾年內」達到 500 億美元年收入，並在措辭謹慎的前提下——考量到監管敏感性——暗示 Amazon 可能開始對外銷售 Trainium 與 Inferentia，不僅作為 AWS 服務的一部分，甚至作為獨立晶片產品提供給企業自建資料中心的客戶。

最後這一點目前仍屬猜測，但戰略邏輯清晰。企業在自建 AI 資料中心時，目前 CUDA 相容 GPU 以外的選項主要是 AMD 的 MI 系列。如果 Amazon 以其在雲端規模部署中已被證實的成本優勢切入這個市場，將從根本上改變企業 AI 基礎架構的競爭格局。

Nvidia 的地位並沒有財報數字所呈現的那麼無懈可擊。H100 和 H200 晶片持續供不應求，毛利率居歷史高位，軟體生態系也確實具有真實的防禦性。但 Amazon 200 億美元的晶片業務、Groq LPU 在推論速度上的優勢，以及 AMD 積極推進的 MI350 藍圖，都指向同一個方向：超大規模雲商與專業廠商正在逐步削弱「Nvidia 是前沿 AI 運算唯一可行路徑」這一假設。

## 對 AI 運算市場的意義

200 億美元的里程碑不只是財務成就，更是一個可信、可規模化的替代 AI 晶片生態系能夠成立的明證。阻礙取代 Nvidia 的壁壘歷來在於三件事：軟體（CUDA）、供應（配額）與效能（每美元算力）。Amazon 已解決後兩個問題，並持續建構降低第一個問題阻力的工具鏈。

對正在評估 AI 基礎架構策略的企業而言，Amazon 的成績驗證了多雲、多晶片路線——這個方向理論上早有建議，實際執行上卻長期困難重重。成本節省、供應可預期性以及 AWS 生態系整合的組合，讓 Trainium 對任何在大規模運行推論工作的組織而言都值得認真評估。

對 Nvidia 而言，更迫切的隱憂或許不是失去超大規模雲商的業務——這些客戶向來會做多重佈局。真正的威脅在於對定價能力的下游影響。如果 Amazon 的晶片壓低了市場上 AI 運算的有效價格，Nvidia 維持 70% 以上毛利率的能力，將面臨光靠 CUDA 綁定在長期上無法獨自抵禦的結構性壓力。

AI 資料中心晶片市場，有史以來第一次開始呈現真正的競爭態勢。Amazon 的 200 億美元，是迄今最清晰的佐證，說明這場競爭並非虛言。
