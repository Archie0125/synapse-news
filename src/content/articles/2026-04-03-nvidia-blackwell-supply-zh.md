---
title: "NVIDIA Blackwell 晶片賣到 2027 年都缺貨。這對所有人都有影響。"
summary: "GPU 短缺不只是 NVIDIA 的問題 — 它正在重塑整個 AI 產業的權力結構。提前鎖定產能的公司正在拉開差距。其他人都在搶。"
category: "hardware"
publishedAt: 2026-04-03T09:10:00Z
lang: "zh"
featured: false
trending: false
sources:
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com"
  - name: "Semianalysis"
    url: "https://www.semianalysis.com"
  - name: "The Information"
    url: "https://www.theinformation.com"
tags:
  - "nvidia"
  - "gpu"
  - "blackwell"
  - "supply-chain"
  - "hardware"
relatedSlugs:
  - "2026-04-04-openai-gpt5-leak-zh"
---

## 科技界最重要的等待名單

NVIDIA 的 Blackwell B200 和 GB200 系統已經完全售罄到 2027 年第二季。每個主要雲端服務商 — Microsoft、Google、Amazon、Meta、Oracle — 都鎖定了價值數百億美元的多年合約。其他人的等候時間以季度計算，不是週。

這不讓人意外。但二階效應正在以值得更多關注的方式重塑產業。

## 有 GPU 的人擁有權力

AI 產業有了新的階級制度，而它建立在 GPU 配額上：

**有的人**：Microsoft（OpenAI 的靠山）、Google（Gemini）、Meta（Llama）和 Amazon（Bedrock + Anthropic 合作）。這些公司各自有數十萬顆 Blackwell GPU 的存取權。他們可以訓練前沿模型、運行大規模推理叢集、自由實驗。

**沒有的人**：其他所有人。中型 AI 公司、新創、學術研究者和大部分企業。他們要嘛用上一代的 H100（仍然很棒，但開始落後），要嘛靠雲端 API，要嘛排隊等。

**有趣的中間地帶**：像 Anthropic 這樣的公司，不製造硬體但通過合作夥伴關係確保了大量配額（Amazon 的 40 億美元投資附帶算力承諾）。位置穩固但有依賴性。

## 真實數字

「售罄」在這個規模下是什麼概念：

- NVIDIA 資料中心營收上季達到 **390 億美元**（沒打錯 — 這是一個季度）
- 台積電的 CoWoS 先進封裝才是真正的瓶頸 — 不是晶片製造本身
- 2026 年 Blackwell 預估總產量：**約 300 萬顆 GPU**。聽起來很多，直到你知道 Meta 一家就要 60 萬顆

供需缺口大約是 2:1。每出貨一顆 GPU，就有一個想要但拿不到的人。

## 為什麼這不只是 AI 實驗室的事

GPU 配額正在成為地緣政治和企業策略議題：

**主權 AI**：沙烏地阿拉伯、阿聯酋、法國、日本和印度都在建國家 AI 算力基礎設施。他們在爭搶同樣有限的供應，而 NVIDIA 扮演著造王者的角色。

**新創融資**：「你有多少 GPU 存取權？」現在是 VC 盡職調查的標準問題。確保算力幾乎跟找到 PMF 一樣重要。

**雲端溢價**：AWS、Azure 和 GCP 對 Blackwell 實例比 H100 多收 30-50% 的費用。客戶照付，因為替代方案 — 等待 — 更糟。

## AMD 和 Intel 的問題

AMD 的 MI300X 和 Intel 的 Gaudi 3 在技術規格上是有競爭力的替代品。但實際上，NVIDIA 的 CUDA 生態系統和軟體工具鏈創造了大多數公司不願支付的轉換成本。

CUDA 護城河是真的。不是 AMD 的晶片不好。而是重寫你整個 ML 技術棧來使用它們是一個六個月的專案，大部分團隊在競爭對手正在出貨的時候負擔不起。

話說回來，需求驅動採用。NVIDIA 短缺持續越久，越多公司會認真評估替代方案。AMD 的 ROCm 生態已經大幅改善，而對於推理工作負載，客製化 ASIC（Google TPU、Amazon Trainium）越來越可行。

## 觀察重點

- 台積電 CoWoS 產能擴張（2026 年底新廠上線 — 夠不夠？）
- NVIDIA 下一代 Rubin 架構發表（預計 GTC 2027）
- AMD 能不能把「有興趣」轉化為真正的企業規模採用
- 主權 AI 建設 — 哪些國家拿到配額，附帶什麼地緣政治條件

*每次淘金熱，賣鏟子的人最賺。NVIDIA 不只是在賣鏟子 — 他們在賣唯一存在的鏟子。問題是這個壟斷能維持多久。*
