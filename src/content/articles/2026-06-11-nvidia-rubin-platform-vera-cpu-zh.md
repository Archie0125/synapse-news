---
title: "NVIDIA 發布 Rubin 平台：六款新晶片、推論成本降低十倍"
summary: "NVIDIA 公布完整的 Rubin 平台規格，包含 Vera CPU 與 Rubin GPU 在內共六款晶片，預計 2026 年下半年上市。NVIDIA 宣稱相較現行 Blackwell 世代，推論 token 成本可降低十倍、訓練混合專家模型所需 GPU 數量減少四倍，若規格屬實，這將大幅重塑大規模 AI 部署的經濟模式。"
category: "hardware"
publishedAt: 2026-06-11
lang: "zh"
featured: false
trending: true
sources:
  - name: "NVIDIA 新聞室"
    url: "https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer"
tags:
  - "NVIDIA"
  - "Rubin"
  - "Vera CPU"
  - "AI晶片"
  - "資料中心"
  - "硬體"
relatedSlugs:
  - "2026-06-03-nvidia-rtx-spark-superchip-computex-zh"
  - "2026-06-10-tensorwave-amd-350m-series-b-anti-nvidia-zh"
  - "2026-06-10-china-295b-ai-data-center-buildout-zh"
---

NVIDIA 正式揭開 Rubin 的面紗——這是繼 Blackwell 之後的下一代資料中心平台，也是迄今為止規格最全面的 AI 超算系統發表。Rubin 並非單一顆 GPU 的更新，而是一套涵蓋六款晶片的整合方案，從運算核心、記憶體互連、到網路交換器，全面重新設計了 AI 超算叢集的每一個矽元件。

時機選擇深具用意。Blackwell 出貨正在全球各大超大規模雲端業者逐步放量，而競爭對手——AMD 的 MI400、Intel 的 Falcon Shores，以及 Google、微軟、亞馬遜各自推進的自製晶片——正在持續縮小差距。Rubin 是 NVIDIA 對外展示其技術路線圖仍保有領先優勢的關鍵宣示。

## Rubin 平台的六款晶片

Rubin 由六款各司其職的晶片組成，分別替換現有 Hopper/Blackwell 架構中的對應元件：

**Vera CPU**：NVIDIA 史上首款量產自製 CPU，基於 Armv9.2 架構，搭載 88 顆自研 Olympus 核心。它取代了目前與 NVIDIA GPU 搭配的主機 CPU（通常是 Grace 或 x86）。Olympus 核心與 Rubin GPU 的記憶體子系統協同設計，目標是最小化 CPU 到 GPU 的資料傳輸延遲——這是大型語言模型工作負載長期存在的效能瓶頸。

**Rubin GPU**：搭載第三代 Transformer Engine，針對現代 Transformer 架構的注意力機制與前饋計算模式深度優化。原生支援 FP4 與 FP6 資料格式，讓積極量化成為可能，同時不必承受早期低精度方案帶來的準確率損失。NVIDIA 宣稱對混合專家（MoE）架構（如 DeepSeek-V3、GPT-5）的訓練吞吐量，是 H100 的四倍。

**NVLink 6 交換器**：每顆 GPU 的頻寬達到 3.6 TB/s，幾乎是 NVLink 4 的兩倍。在機架層級，Vera Rubin NVL72 配置可容納 72 顆 Rubin GPU 與 36 顆 Vera CPU，機架內聚合頻寬達 260 TB/s，頻寬密度約為現行 Blackwell NVL72 機架的三倍。

**ConnectX-9 SuperNIC**：負責機架間的 InfiniBand 與乙太網路連線，確保機架間互連不成為整體系統的效能瓶頸。這是 NVIDIA 自 2020 年收購 Mellanox 以來，GPU 與網路路線圖全面整合的成果。

**BlueField-4 DPU** 與 **Spectrum-6 乙太網路交換器**則分別處理儲存卸載與叢集間的網路交換，完成六件套的完整閉環。

## 推論成本降低十倍的底氣

NVIDIA 用來宣傳 Rubin 的核心數字，是相較 Blackwell 每推論 token 成本降低十倍。這個數字是一個複合性的效益估算，包含更高的 GPU 運算密度、更佳的記憶體頻寬、硬體層面更好的量化支援，以及同等推論容量所需機架數量的減少。

對照一下背景：推論成本在過去 18 個月是 AI 基礎設施最激烈的競爭戰場。OpenAI 2024 年初以每千個 input token $0.03 的定價推出 GPT-4，背後仰賴的是積極的批次處理與軟體優化；如今前沿模型的推論成本已降至當時的約十分之一，主要來自連續幾代硬體與軟體的迭代。如果 Rubin 再帶來十倍的降幅，運行 GPT-5 等級模型的成本將進入低於每次查詢一美分的範圍，有機會啟動目前因成本而受限的消費者應用場景。

確認採購 Rubin 的客戶名單幾乎涵蓋了全球所有主要的 GPU 採購方：AWS、Google Cloud、Microsoft Azure、Oracle Cloud、Meta、OpenAI、Anthropic、xAI 以及 CoreWeave。NVIDIA 尚未公布定價，但業界分析師預期 NVL72 機架單價將高於 Blackwell，同時提供顯著更低的每單位算力總擁有成本。

## Vera CPU：NVIDIA 向 Intel 與 AMD 宣戰

Vera CPU 的發表，或許與 GPU 規格同等重要，只是在 AI 媒體的報導中相對低調。NVIDIA 過去對主機 CPU 保持中立態度，支援 Grace（自家 Arm CPU）、Intel Xeon 與 AMD EPYC。Vera 的推出代表了明確的架構押注：GPU 與 CPU 的最緊密整合，將為 AI 工作負載帶來任何第三方 CPU 都無法複製的優勢。

88 核心的 Olympus 設計鎖定大型語言模型推論中的具體瓶頸：上下文管理、KV 快取處理，以及自回歸生成解碼階段的記憶體頻寬密集運算。AMD EPYC Venice（採用台積電 2nm 製程、現已量產）提供更高的通用計算吞吐量，但 NVIDIA 押注的是專一化勝過核心數的策略。

對 Intel 而言，挑戰更具存亡意義。若 Vera 取代 x86 成為 NVIDIA GPU 叢集的標準配套 CPU，Intel 將痛失一大塊利潤率最高的伺服器 CPU 市場。

## 上市時程與競爭格局

NVIDIA 承諾在 2026 年下半年正式上市，超大規模雲端業者的部署預計於第三季啟動。製造分工上，Vera CPU 採用台積電 N3 製程，Rubin GPU 採用 N2 製程，是 NVIDIA 首次同步在兩家晶圓廠最先進製程上量產的產品。

從現在到 Rubin 正式上市的這段窗口期，是 NVIDIA 多年來面對最激烈競爭的時期。AMD MI300X 在推論工作負載上已取得真實的市場份額；Google TPU v6 在 Google Cloud 上執行 Gemini 等級模型時，已消除每次查詢成本的差距。本週稍早宣布完成 3.5 億美元 B 輪融資的 TensorWave，就是明確針對那些對 NVIDIA 定價與出貨等待期感到不滿的企業而生。

Rubin 的效能宣稱能否在量產規模下兌現，以及客戶能否真正取得貨源而不必再經歷 Blackwell 時代的排隊煎熬，將決定 NVIDIA 是否能在邁入 2027 年之際繼續擴大領先，還是只是維持現狀。
