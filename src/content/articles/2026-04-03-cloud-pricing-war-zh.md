---
title: "雲端價格戰開打：AWS vs Azure vs GCP 的 AI 時代攻防"
summary: "雲端供應商把 GPU 實例價格砍了 30-50%，同時把客戶鎖進多年的 AI 承諾合約。雲端運算的經濟正在被重寫。"
category: "industry"
publishedAt: 2026-04-03
lang: "zh"
featured: false
trending: false
sources:
  - name: "The Information"
    url: "https://www.theinformation.com"
  - name: "SemiAnalysis"
    url: "https://www.semianalysis.com"
tags:
  - "cloud"
  - "aws"
  - "azure"
  - "gcp"
  - "pricing"
relatedSlugs:
  - "2026-04-03-nvidia-blackwell-supply-zh"
---

## 價格標籤開始有趣了

AWS 上個月把 GPU 實例價格砍了 40%。Google Cloud 回應 45% 的降價加上 AI 工作負載免費出流量。Azure 在 48 小時內跟進，還附贈 AI 應用的 6 個月免費 Cosmos DB。

這不是正常的雲端定價競爭。這是對運算史上最有價值工作負載類型的搶地盤戰：AI 推理和訓練。

## 為什麼是現在？

三股力量同時交匯：

**供給追上來了**：定義了 2024-2025 的 GPU 短缺正在緩解。NVIDIA 在 2026 第一季出貨的 Blackwell GPU 比 2024 全年賣出的 H100 總和還多。雲端供應商終於有庫存可以積極賣了。

**推理是新的運算**：訓練搶了標題，但推理 — 在生產環境運行模型 — 才是產生營收的。推理工作負載年增 10 倍，因為企業正在部署 AI 應用。

**客戶鎖定才是真正的遊戲**：雲端供應商不靠 GPU 實例本身賺錢。他們靠周邊服務賺 — 儲存、網路、監控、託管資料庫。在 Azure 上跑 AI 的客戶也在 Azure 上跑其他所有東西。GPU 是虧本引客的。

## 承諾消費的陷阱

每個 CTO 都該緊張的把戲來了：雲端供應商提供 50-70% 的 GPU 運算折扣，交換條件是 3-5 年的承諾消費合約。

推銷聽起來很棒：「鎖定今天的價格三年，拿到巨大折扣。」現實是：

- GPU 成本自然每年降 30-40%，因為新晶片持續出貨
- 「今天價格打五折」的三年承諾，到第二年實際上比即時價格還貴
- 承諾涵蓋所有雲端支出，不只是 GPU — 所以你被鎖在所有東西上
- 提前解約要付剩餘合約價值的 30-50%

Microsoft 和 Google 都在積極對企業客戶推這個。AWS 比較謹慎但也在猛推 Reserved Instances。

## 真正的戰場：託管 AI 服務

原始 GPU 定價是入場券。真正的競爭在讓 AI 更容易部署的託管服務上：

- **AWS Bedrock** vs **Azure OpenAI Service** vs **Google Vertex AI** — 哪個託管模型平台會贏？
- **SageMaker** vs **Azure ML** vs **Vertex AI Training** — 哪個讓自訂模型訓練最容易？
- **Inferentia/Trainium** (AWS) vs **TPU** (Google) vs **Maia** (Microsoft) — 自研 AI 晶片 vs NVIDIA

Google 的 TPU 有真正的優勢 — 對很多推理工作負載比 NVIDIA GPU 便宜。AWS 的 Inferentia2 做推理很穩但訓練還不夠成熟。Microsoft 的 Maia 晶片還在早期。

能在自家矽晶片上提供有競爭力 AI 效能的供應商 — 不用付 NVIDIA 的溢價 — 長期在經濟面上就贏了。

## 觀察重點

- 價格戰能不能持續到第三季，還是供應商搶完市場份額就收手
- 自研晶片採用率 — TPU/Inferentia/Trainium 能不能從 NVIDIA 實例搶走有意義的份額
- 對純 GPU 雲端供應商（CoreWeave、Lambda Labs）的衝擊 — 他們無法匹敵超大規模供應商的定價
- 企業多雲策略 — 公司在分散押注還是全押一家？

*雲端價格戰不是比誰今天最便宜。是比誰擁有未來十年的 AI 工作負載關係。降價只是開局的第一步。*
