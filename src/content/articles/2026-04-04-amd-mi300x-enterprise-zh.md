---
title: "AMD MI300X 終於在拿下企業訂單了。到底什麼變了？"
summary: "在當了 NVIDIA 配角多年之後，AMD 的 AI GPU 正在拿到真正的企業合約。CUDA 護城河是真的但正在侵蝕，而價差已經大到無法忽視。"
category: "hardware"
publishedAt: 2026-04-04
lang: "zh"
featured: false
trending: false
sources:
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com"
  - name: "ServeTheHome"
    url: "https://www.servethehome.com"
tags:
  - "amd"
  - "mi300x"
  - "gpu"
  - "nvidia"
  - "inference"
relatedSlugs:
  - "2026-04-03-nvidia-blackwell-supply-zh"
---

## NVIDIA 稅越來越貴了

多年來，企業 AI 的對話很簡單：買 NVIDIA。CUDA 是標準，軟體生態無人能及，選市場領導者不會被炒魷魚。

2026 年，這個等式在改變。AMD 的 MI300X 正在 Oracle、Microsoft Azure、Meta 和幾家中型雲端供應商拿下訂單。不是因為它比 NVIDIA 最好的更強 — 它不是。而是因為它便宜 30-40%，對一個日益重要的工作負載來說夠好：推理。

## 訓練 vs 推理：關鍵的分裂

NVIDIA 的主導地位在訓練上最強 — 從頭建構模型的過程。訓練需要絕對最好的硬體，因為一萬顆 GPU 叢集上 10% 的效能差異等於數百萬美元的時間和電費節省。

但推理 — 在生產環境運行已訓練好的模型 — 有不同的經濟學：

- **價格敏感度更高**：當你處理數百萬請求時，每一塊錢的查詢成本都重要
- **效能要求更低**：推理不需要峰值吞吐量，需要的是穩定的低延遲
- **軟體堆疊更簡單**：推理框架（vLLM、TensorRT-LLM、SGLang）越來越不挑硬體

MI300X 的 192GB HBM3 記憶體（對比 NVIDIA H100 的 80GB）在推理上是真正的優勢。更大的模型塞在更少的 GPU 上。更少 GPU 意味更低成本。數學很直接。

## 到底什麼變了

AMD 試著在 AI 上跟 NVIDIA 競爭好幾年了。為什麼現在有效？

**ROCm 長大了。** AMD 的軟體堆疊（CUDA 的競爭者）在 2023 年真的很爛。到 2026 年，它...堪用了。沒有 CUDA 精緻，但功能足夠讓價格折扣合理化摩擦。

**vLLM 搭起了橋。** 開源推理引擎 vLLM 在 NVIDIA 和 AMD GPU 上都能跑，效能幾乎一樣。這單一個專案可能比 AMD 內部做的任何東西都更推動了 AMD 的 AI 採用。

**NVIDIA 缺貨幫了忙。** 當你買不到你想要的晶片，你就會評估替代品。幾家在 Blackwell 缺貨期測試 MI300X 的公司發現它滿足需求，之後就沒有換回去。

**來自客戶的價格壓力。** 當推理成本在規模上衝擊企業預算時，CFO 開始問：「為什麼我們在推理上付 NVIDIA 溢價，AMD 便宜 40%？」

## AMD 時刻的極限

說清楚 AMD 沒有贏的地方：

- **前沿模型訓練**：仍然是 NVIDIA 的領地。沒有人在 AMD 硬體上訓練 GPT-5。
- **CUDA 生態系**：數千個程式庫、工具和學術程式碼庫都假設是 NVIDIA。切換不是免費的。
- **企業支援**：NVIDIA 的企業支援和合作夥伴生態領先好幾年。對任務關鍵的部署來說，這很重要。

AMD 實際可觸及的市場是推理和微調工作負載 — 價格比峰值效能更重要的場景。那是一個大市場 — 可能佔 AI 總運算支出的 40% — 但那不是「取代 NVIDIA」。

## 觀察重點

- AMD 的 MI400（預計 2026 年底）— 如果縮小訓練差距，故事會根本改變
- Google 的 TPU 和 AWS 的 Trainium 更多是跟 AMD 還是 NVIDIA 競爭
- ROCm 的開發速度 — AMD 能維持追上 CUDA 所需的投資嗎？
- 企業採用指標 — 早期勝利需要轉化為持續的市場份額

*AMD 不會殺死 NVIDIA。但一個企業常態性地用 60% NVIDIA 做訓練、40% AMD 做推理的世界，是一個 NVIDIA 定價權顯著侵蝕的世界。那個世界來的速度比黃仁勳想的更快。*
