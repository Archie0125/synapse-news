---
title: "NVIDIA 的 Nemotron 3 Embed 登頂檢索基準排行榜"
summary: "NVIDIA 於 7 月 17 日發布了 Nemotron 3 Embed，這是一個包含三個開放且可商用的嵌入模型家族，旗艦 8B 版本以 78.5% 的得分登頂 RTEB 檢索排行榜。這些模型專為大規模 RAG 流程和代理記憶系統而設計，填補了封閉前沿模型與較小開放替代方案之間的空白。"
category: "developer-tools"
publishedAt: 2026-07-19
lang: "zh"
featured: false
trending: false
sources:
  - name: "Hugging Face Blog"
    url: "https://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb"
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/07/17/nvidia-ai-releases-nemotron-3-embed-an-open-embedding-collection-whose-8b-checkpoint-ranks-1-on-rteb/"
  - name: "NVIDIA Build"
    url: "https://build.nvidia.com/nvidia/nemotron-3-embed-1b"
  - name: "FriendliAI"
    url: "https://friendli.ai/blog/nvidia-nemotron-3-embed"
tags:
  - "NVIDIA"
  - "Nemotron"
  - "嵌入模型"
  - "RAG"
  - "開源"
  - "開發者工具"
  - "向量搜尋"
relatedSlugs:
  - "2026-05-08-nvidia-nemotron-3-nano-omni-multimodal-edge-zh"
  - "2026-07-08-nvidia-sk-hynix-hbm4-vera-rubin-partnership-zh"
  - "2026-07-17-prismml-bonsai-27b-iphone-on-device-zh"
---

長期以來，建構有效的檢索增強生成（RAG）系統有一個不為人知的秘密：語言模型獲得了大部分關注，但決定檢索什麼的嵌入模型同樣舉足輕重。一個平庸的嵌入模型產出平庸的檢索結果，再多的提示工程也無法彌補塞滿錯誤文件的上下文視窗。NVIDIA 於 7 月 17 日發布的 Nemotron 3 Embed 正是針對這個瓶頸的直接回應——推出的模型組合在發布當日即登上了檢索基準排行榜首位。

Nemotron 3 Embed 家族包含三個模型：一個為檢索準確度設計的旗艦 8B 參數版本、一個 BF16 精度的 1B 參數版本供一般部署，以及一個 NVFP4 精度的 1B 參數版本，專為 NVIDIA Blackwell GPU 架構優化。三者均開放且可商用，可從 Hugging Face 下載，也可通過 NVIDIA Build 作為 API 端點使用。8B 模型在發布當日以 78.5% 的得分登頂 RTEB（檢索文字嵌入基準）排行榜，並在第二個綜合多語言基準 MMTEB Retrieval 上取得 75.5% 的分數。

## 優質嵌入模型的關鍵

嵌入模型在 RAG 流程中的作用是將文字轉換為保留語義的稠密數值向量。當用戶提出問題時，查詢被轉換為向量，系統找出儲存的向量中與之幾何距離最近的結果。這種相似度搜尋決定了 LLM 在生成回應前所看到的內容，整個 RAG 系統的輸出質量都取決於嵌入模型捕捉語料庫語義結構的能力。

Nemotron 3 Embed 發布前，現有格局呈現出清晰的層級結構。頂端是 OpenAI 的 text-embedding-3-large 和 Cohere Embed v4 等大型專有模型，需要 API 呼叫且按 token 計費。中間是 BGE-M3、E5-Mistral-7B 等可自行部署的開放模型，但在最難的檢索任務上落後於專有選項。小模型端則有 all-MiniLM-L6-v2 等速度快但在垂直領域查詢上明顯較弱的選項。

Nemotron 3 Embed 的架構跨越了上述兩個層級。8B 模型在準確度排名上與專有模型競爭，同時保持可自行部署且免費商用。1B 版本為需要高吞吐量但不想負擔 8B 推理伺服器算力成本的團隊，在效率曲線上提供了一個可用的平衡點。三者共享核心架構決策：雙向注意力遮罩（而非生成式模型典型的因果遮罩）、對 token 層級表示進行平均池化以產生最終嵌入，以及 32,768 個 token 的最大序列長度——長到足以在不進行分塊的情況下嵌入大多數文件。

## 代理檢索使用情境

嵌入模型的發展歷史上一直由文件搜尋和問答使用情境驅動：嵌入一批 PDF 語料庫，然後回答關於它的問題。Nemotron 3 Embed 明確以不同的目標為設計出發點：需要在執行時進行檢索的代理系統。

這一區別至關重要。傳統 RAG 系統嵌入靜態語料庫，在查詢時進行檢索。代理系統可能持續向記憶儲存中添加內容，跨越異質內容類型（程式碼、對話歷史、工具輸出、網頁內容）進行檢索，並將檢索決策作為多步驟推理鏈的組成部分而非預處理步驟。其需求——多語言覆蓋、長上下文支持、跨不同內容領域的準確性、高查詢量下的速度——比靜態文件檢索更為嚴苛。

NVIDIA 選擇在 MMTEB Retrieval 上對 Nemotron 3 Embed 進行基準測試，而非僅在傳統英語基準 MTEB 上，這一決策反映了代理框架的思考：一個在英語中檢索良好、但在西班牙語、日語或程式碼中表現不佳的系統，無法勝任全球部署的代理應用。

## 部署選項

對於構建 RAG 或代理系統的團隊，Nemotron 3 Embed 提供了三種部署路徑。模型作為標準 Transformer checkpoint 可從 Hugging Face 直接獲取，與 Sentence Transformers 庫以及任何能運行 HuggingFace 模型的推理框架相容。NVIDIA Build 為希望跳過推理基礎設施管理的團隊提供託管 API 端點。第三方推理服務商 FriendliAI 則提供在 NVIDIA Blackwell GPU 上的優化部署，1B NVFP4 版本在最新硬體上的吞吐量遠超舊版 GPU。

NVFP4 版本值得特別關注。NVIDIA 的 Blackwell GPU 系列去年開始作為 Vera Rubin 基礎設施路線圖的一部分進入生產，其中包含對 FP4 矩陣乘法的硬體支援，可大幅加速以該格式編譯的模型推理。Nemotron-3-Embed-1B-NVFP4 直接利用了這一能力，NVIDIA 稱之為在 Blackwell 基礎設施上運行的團隊的最低延遲路徑——但這需要特定硬體，與舊一代 GPU 不相容。

## 脈絡：NVIDIA 為何進入嵌入模型領域

NVIDIA 的核心業務是 GPU 硬體，其軟體工作——CUDA、cuDNN、Triton 推理伺服器，以及 Nemotron 3 Embed 所依託的 NeMo 框架——都服務於這個硬體業務。發布強大的開放嵌入模型有多重策略目的。

首先，它推動了對 NVIDIA GPU 的需求。更優秀的開放嵌入模型意味著更多組織構建 RAG 和代理系統；更多代理系統意味著更大的推理需求；更大的推理需求意味著更多的 GPU 銷售。模型本身不是產品，它所創造的需求才是。

其次，它向封閉嵌入模型市場施壓。如果 NVIDIA 的開放模型在 RTEB 上超越了 OpenAI 的 text-embedding-3-large，企業客戶就有了充分的財務理由選擇自行部署而非按 token 付費。這在 OpenAI 和 Anthropic 積極競爭企業推理收入的時刻，削弱了基於 API 的嵌入模型商業模式。

第三，它確立了 NeMo 作為可信開源 AI 開發框架的地位，與 Meta 的 PyTorch 生態系統競爭。NVIDIA 一直在 Nemotron 旗幟下穩定發布強大的開放模型——5 月發布了面向邊緣推理的 Nemotron 3 Nano，現在又發布了面向檢索的 Nemotron 3 Embed——以此在以 CUDA 為原生基礎的開發棧周圍建立開發者思維份額。

對於正在為新專案選擇嵌入模型的開發者而言，Nemotron 3 Embed 改變了決策邏輯。8B 版本提供了此前只能通過專有 API 獲得的準確度，而自行部署的費用為零。1B BF16 版本為高吞吐量應用提供了實際可行的性能點。1B NVFP4 版本則指向了在最新 NVIDIA 硬體上性能優化的未來方向。在 RAG 架構中，檢索質量是輸出質量的天花板，嵌入模型層級的這一改變絕非可以輕描淡寫的細節。
