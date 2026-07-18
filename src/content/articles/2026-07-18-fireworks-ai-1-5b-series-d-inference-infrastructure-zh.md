---
title: "Fireworks AI 完成 15 億美元 D 輪融資，估值達 175 億美元，每日處理 40 兆 Token"
summary: "由 Nvidia 支持的 Fireworks AI 以 175 億美元估值完成 15 億美元 D 輪融資，鞏固其在企業 AI 模型部署市場的領導地位。該公司年化營收已突破 10 億美元，每日處理逾 40 兆 Token。"
category: "startups"
publishedAt: 2026-07-18
lang: "zh"
featured: false
trending: true
sources:
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/07/16/ai-infrastructure-startup-fireworks-closes-1-5b-round-17-5b-valuation/"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/07/16/fireworks-nvidia-cloud-ai-startup-value.html"
  - name: "Fireworks AI Blog"
    url: "https://fireworks.ai/blog/series-d-announcement"
tags:
  - "Fireworks AI"
  - "AI 基礎設施"
  - "推理運算"
  - "融資"
  - "Nvidia"
  - "開源"
relatedSlugs:
  - "2026-07-01-etched-5b-valuation-1b-sales-inference-chip-en"
  - "2026-07-11-sambanova-1b-series-f-ai-chip-en"
  - "2026-07-04-baseten-15b-series-f-ai-inference-en"
---

AI 推理層的競爭剛剛進入了一個全新的量級。Fireworks AI 於 7 月 16 日宣布完成 15 億美元 D 輪融資，融資後估值達到 175 億美元。本輪由 Atreides Management、Index Ventures 和 TCV 聯合領投，Nvidia 等六家以上機構跟投。這筆融資讓 Fireworks 成為企業開源 AI 模型部署領域最強大的獨立平台之一，直接挑戰 OpenAI 和 Anthropic 等封閉生態系。

公司的業務規模令人矚目。Fireworks 目前每日在其基礎設施上處理超過 40 兆個 Token，這些算力承載著大量基於 Meta Llama 家族、Mistral 及 DeepSeek 衍生版本等開源模型運行的企業應用。融資前，公司年化營收已突破 10 億美元——這個里程碑，直到不久前還被視為只有前沿模型實驗室才能達到，而非基礎設施層的玩家。

## Fireworks 到底做什麼

Fireworks 的雲端平台主要解決兩個問題：一是讓企業能在管理式 GPU 叢集上以按使用量計費的方式微調開源模型；二是提供規模化的推理服務，分為無伺服器和專屬部署兩種選項。

在模型微調方面，平台內建了一個 AI 自動化代理，能識別最佳超參數，並在需要時以 DPO（直接偏好優化）檔案擴充訓練資料集，大幅降低了企業構建領域專屬模型的門檻。Fireworks 支援四種不同的訓練並行化技術，針對不同架構和規模的模型各有優化。

推理服務方面，客戶可以選擇幾乎零配置的無伺服器環境，或選擇提供自動擴縮容、模型量化等更深度自訂功能的「Deployments」專屬 GPU 叢集方案。三星電子（Samsung Electronics）和 GitLab 是其主要企業客戶——這些公司的 AI 工作負載規模龐大且對延遲敏感，一個穩定的推理夥伴和一個廉價供應商之間的差異，往往以生產事故的頻率來衡量。

## 基礎設施投資的底層邏輯

這輪融資恰逢「推理經濟」的關鍵轉折點。隨著基礎模型能力趨於收斂——Anthropic、Google、Meta 以及各路開源貢獻者的模型在多數任務上都表現得可圈可點——企業開始不再只關心「用哪個模型」，而是更在意「如何更便宜、更穩定地部署它」。

Fireworks 正好卡位在這個轉變上。透過將 GPU 排程、記憶體頻寬優化和批次處理策略的複雜性抽象化，公司把一個深度技術問題變成了一項託管服務。Nvidia 作為跟投方的角色頗具深意：任何能推動更多算力消耗的平台，Nvidia 都是直接受益者，而 Fireworks 每日 40 兆 Token 的處理量，正是 Nvidia 希望加速的需求乘數。

## 競爭格局

這輪融資進一步加劇了企業 AI 基礎設施市場的競爭烈度。Baseten 在七月初以 150 億美元估值完成了 15 億美元融資，SambaNova 則在其 F 輪融資 10 億美元。Fireworks 聲稱的核心差異化優勢在於自訂化深度——不僅是提供模型服務，而是能夠針對特定企業場景實質性地改變模型的行為。

這個差異化在受監管行業中尤為關鍵。三星或金融機構不可能將敏感工作負載直接路由到共用的 OpenAI 端點，他們需要的是在可信基礎設施上運行的微調模型，配備符合企業採購要求的審計追蹤和 SLA 保障。這正是 Fireworks 在解決的問題。

## 下一步計畫

公司計畫將這筆資金用於擴充工程團隊和全球算力容量。策略層面，這很可能意味著與雲端超大規模服務商的更深度整合——與微軟和 Nvidia 的合作夥伴關係已經到位——同時也會向資料主權法規讓在美國雲端基礎設施上運行工作負載存在法律顧慮的地區拓展業務。

在 175 億美元的估值水位上，Fireworks 的市值已超過多數同等營收規模的傳統企業軟體公司。這個溢價反映了市場對一個判斷的信念：隨著 AI 採用從試點走向全面生產部署，推理基礎設施層將持續累積不成比例的價值。每日 40 兆 Token 不只是一個數字——它是這個轉變已經開始的明證。

對於整個 AI 生態系而言，一個達到如此規模的 Fireworks，代表著一件重要的事：在那些吸引最多關注的明星模型之下，基礎設施層正在積累可觀的價值。AI 的下一個前沿，有時並不在於誰能訓練出最好的模型，而在於誰能最有效率地為其他人運行它。
