---
title: "Nvidia 發布 Nemotron 3 Nano Omni：視覺、語音、語言三合一的開放多模態模型"
summary: "Nvidia 於 4 月 28 日發布 Nemotron 3 Nano Omni——一個 300 億參數的開放多模態模型，運行僅需 25GB 記憶體，吞吐量最高可達同類開放模型的 9 倍。透過混合 MoE 架構將視覺、音訊、影片與語言融合為單一模型，為邊緣 AI 代理樹立了全新的效率標竿。"
category: "ai-ml"
publishedAt: 2026-05-08
lang: "zh"
featured: false
trending: false
sources:
  - name: "Nvidia Blog"
    url: "https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/"
  - name: "Nvidia 技術部落格"
    url: "https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/"
  - name: "Hugging Face Blog"
    url: "https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/nvidia-nemotron-nano-omni-multimodal-agent-edge"
tags:
  - "Nvidia"
  - "開源模型"
  - "多模態"
  - "AI模型"
  - "邊緣AI"
  - "MoE"
relatedSlugs:
  - "2026-04-10-nvidia-cosmos-reason2-groot-physical-ai-zh"
  - "2026-05-04-kimi-k26-open-source-coding-benchmark-zh"
  - "2026-04-04-open-source-llm-race-zh"
---

長久以來，AI 模型的主流部署方式是將多個專用模型拼接在一起：一個處理視覺，一個處理語音辨識，一個處理語言，再加上一層編排邏輯讓它們協同運作。Nvidia 於 4 月 28 日發布的 Nemotron 3 Nano Omni，正是對這種架構的直接挑戰——它在單一 300 億參數模型中同時處理音訊、影片、圖像與文字，且僅需 25GB 記憶體即可運行。

這個模型完全開放，已可透過 Hugging Face、OpenRouter、build.nvidia.com 及逾 25 個合作夥伴平台立即下載使用。此次發布，是 Nvidia 在開放權重模型領域持續發力的最新動作——透過加速開發者對 Nvidia 軟體生態系統的採用，為其硬體業務提供戰略支撐。

## 架構：300 億總參數，推理時僅啟動 30 億

Nemotron 3 Nano Omni 採用混合 Mamba-Transformer 混合專家（MoE）架構。300 億的參數總量，是整個模型的規模；但在任何一次推理步驟中，僅有約 30 億參數處於激活狀態。這種稀疏激活的機制——模型的大部分在每次計算中保持靜默——正是其驚人效率數字背後的根本原因。

混合 Mamba-Transformer 骨幹架構值得特別說明。Mamba 是一種狀態空間模型（state-space model）方案，相較於純 Transformer 架構，在長上下文處理上效率顯著更高。將其與 Transformer 組件以及混合專家路由層結合，使模型同時具備 Mamba 在長程序列建模上的優勢，以及根據輸入類型激活不同專屬子網路所帶來的能力提升。

實際意義：一個 300 億參數的多模態模型，可以在工作站 GPU 上運行，而非依賴資料中心叢集。對於有真實算力限制和低延遲需求的邊緣 AI 應用開發者，這是一個值得關注的轉變。

## 基準測試：效率帕累托前沿

Nvidia 引用的基準測試成績在多個領域表現強勁。

在文件智慧領域，Nemotron 3 Nano Omni 在 MMlongbench-Doc 和 OCRBenchV2 排行榜上位居榜首——這兩個排行榜衡量的是對包含混合文字、表格與視覺元素的長文件進行複雜理解的能力。這使其在企業文件處理場景中具備強大競爭力：合約分析、財報資料提取、研究論文摘要等。

在影片理解領域，模型在 WorldSense 和 DailyOmni 基準測試中位居前列，並在 MediaPerf 的影片標注任務上取得最佳性價比——每小時可處理 9.91 小時的影片，推理成本僅需 14.27 美元。這個數字令人印象深刻，因為影片處理歷來是計算密集型任務；以全開放模型達到如此吞吐量和成本效率，實際上改變了影片智慧應用的經濟模型。

在音訊理解方面，VoiceBench 的結果同樣顯示該模型在開放權重替代品中領先。

這些結果的共同線索是效率而非純粹精度：Nemotron 3 Nano Omni 並不聲稱在每個類別都是最精準的模型，而是聲稱擁有最佳的「準確率/推理成本」比。對於推理成本和延遲與模型品質同樣重要的生產部署環境，這往往才是更有意義的指標。

## 統一多模態架構的意義

將視覺、音訊與語言融合進單一模型，其意義遠超基準測試表現。架構上統一的模型，可以避免拼接管道的失效模式。

當你串聯多個專用模型時，錯誤會疊加：語音辨識模型的轉錄錯誤，會以「事實」的形式流入語言模型；視覺模型的信心分數，也難以自然地向語言層傳遞不確定性。而聯合跨模態訓練的統一模型，能夠學習各模態之間的隱性相關性——說話時的語調和節奏，傳遞著能夠強化或修正語言內容的情感訊號；文件圖像的視覺上下文，有助於詮釋含糊的文字。

這對 Nvidia 明確瞄準的代理式 AI 應用場景尤為關鍵。一個 AI 代理在處理複雜業務流程時——解讀一份發票、聆聽一段客戶通話、分析一張產品圖片、生成一份回應——需要同時在工作記憶中保持所有這些模態，並跨模態進行推理。統一架構讓這種融合在根本上成為可能，而拼接管道則無法做到。

## Nvidia 的開放模型戰略

Nemotron 3 Nano Omni 是 Nemotron 家族的最新成員，整個家族在過去一年中已被下載超過 5,000 萬次。這個採用數字在戰略上意義重大：它意味著 Nemotron 架構已嵌入大量 AI 生產系統，形成向 Nvidia 軟體生態系統聚集的引力。

這是 Nvidia 歷史上熟悉的劇本。CUDA 的主導地位，並非僅靠硬體性能建立，而是依靠工具、函式庫和開發者熟悉度所構成的生態護城河——任何在 CUDA 開發上有所投入的人，切換成本都極為高昂。透過開放能在 Nvidia 硬體上表現最佳的高品質模型，Nvidia 正在將同樣的邏輯延伸到 AI 模型層。

Nano Omni 的發布，繼承了 Nemotron 3 Nano（純語言模型）和 Nemotron 3 Super（今年 3 月 GTC 上發布的更大容量版本）的工作。三款模型共同構成了一個覆蓋不同能力和效率權衡的產品系列，可適應從雲端大規模推理到高端消費硬體本機部署等不同場景。

## 對 AI 代理開發者的影響

對於正在構建 AI 代理的開發者而言，Nemotron 3 Nano Omni 的發布，在幾個具體維度上改變了成本計算方式。

首先，原本需要分別呼叫視覺和語言模型的代理，有可能整合為單次模型呼叫，降低延遲並簡化基礎設施。其次，25GB 記憶體需求意味著模型可在高端工作站和配備 Nvidia RTX GPU 的遊戲主機上本地運行，無需依賴雲端 API，直接省去對應費用。第三，開放授權意味著可以針對特定領域進行微調，不受 API 使用條款的限制。

Nvidia 正在把握的趨勢，是 AI 互動從對話式走向代理式的大轉型：AI 系統自主完成多步驟任務、監控持續進行的流程、與真實系統交互。這類應用無一例外地受益於多模態能力，因為現實世界本身就是多模態的——人類的溝通同時包含文字、語音、圖像和影片。

Nemotron 3 Nano Omni 能否成為下一代 AI 代理的骨幹模型，取決於其效率優勢在與 GPT-5.5、Gemini 3.1 等閉源替代品的生產工作負載實測中能否持續成立。但一個完全開放的模型現在已能在多模態效率基準上可信地與其競爭，同時還能在消費級硬體上運行——這本身就是開發者構建 AI 應用的可能性邊界的一次真實擴展。
