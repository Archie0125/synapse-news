---
title: "Amazon 自研晶片年化營收突破 200 億美元，Jassy：若獨立販售市值可達 500 億"
summary: "涵蓋 Graviton 處理器、Trainium AI 訓練加速器與 Nitro 網路晶片的 Amazon 自研矽晶組合，年化營收已突破 200 億美元，年增率達三位數。執行長 Andy Jassy 表示，若這項業務是獨立事業並向第三方銷售晶片，其年化營收規模將達 500 億美元。"
category: "hardware"
publishedAt: 2026-06-30
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "Let's Data Science – Amazon 自研晶片達 200 億美元年化規模"
    url: "https://letsdatascience.com/news/amazons-custom-chips-reach-a-20b-run-rate-9c98d68a"
  - name: "The Next Web – Jassy：晶片部門若對外銷售市值達 500 億"
    url: "https://thenextweb.com/news/amazon-custom-chips-jassy-letter-fifty-billion-trainium"
  - name: "TIKR – Amazon Q1 2026 財報：晶片業務是更大的故事"
    url: "https://www.tikr.com/blog/amazon-beat-q1-2026-earnings-on-every-line-the-bigger-story-is-the-chip-business-inside-aws"
tags:
  - "Amazon"
  - "AWS"
  - "Trainium"
  - "Graviton"
  - "AI 晶片"
  - "半導體"
  - "硬體"
relatedSlugs:
  - "2026-06-29-openai-jalapeno-broadcom-inference-chip-zh"
  - "2026-06-29-ai-chip-stock-selloff-june-2026-zh"
---

Andy Jassy 在 Amazon 股東信中披露，並在 2026 年第一季財報電話會議上再度提到，公司自研矽晶業務的年化營收已突破 **200 億美元**、年增率達三位數。但更大的數字緊接著出現：Jassy 說，如果 Amazon 的晶片業務是獨立事業，並像其他領先晶片公司那樣向 AWS 與其他第三方銷售晶片，年化營收規模將達到 **500 億美元**。

這個假設性估值，Jassy 在股東信和財報會議上反覆提及，映照出當今科技業最被低估的戰略資產。Amazon 已悄悄建起一套垂直整合的矽晶技術棧：從 AI 訓練加速器、推論晶片、CPU 集群，到資料平面網路晶片，全部針對驅動雲端基礎設施投資的 AI 工作負載量身打造。

## 三條產品線，一個完整戰略

Amazon 的自研晶片組合分為三個產品家族：Graviton、Trainium 與 Nitro。

**Graviton** 處理器承擔 AWS 上的 CPU 運算工作負載。AWS EC2 前 1,000 大客戶中，已有 98% 使用 Graviton。

**Trainium** 是 Amazon 的 AI 訓練與推論加速器，旨在與 Nvidia 的資料中心 GPU 競爭。Trainium3 是 Amazon 首款採用 3 奈米製程的晶片，於 2026 年初開始出貨，據 AWS 簡報形容「幾乎已被預訂一空」——亦即需求已達甚至超過產能。Trainium4 距離廣泛上市仍約有 18 個月，但已有大量產能被預訂。

**Nitro** 晶片負責支撐 AWS 虛擬化、網路與儲存系統的資料平面基礎架構。它不如 Graviton 或 Trainium 那樣廣為人知，卻是整個體系的基礎——它從每台伺服器的 CPU 卸載大量額外負荷，並支援大規模 AI 模型推論所需的高頻寬網路。

## 改變一切的兩大錨定客戶

Trainium 的轉折點，是全球最大兩家 AI 模型開發商相繼承諾將訓練工作負載部署在 Amazon 矽晶上。

**Anthropic** 在 Amazon 250 億美元投資承諾的配套框架下，承諾使用高達 **5 吉瓦**的 Trainium 算力容量。這個安排將 Trainium 從「有趣的 Nvidia 替代品」，升級為 Anthropic 訓練基礎設施的核心組成——一段鎖定算力收益與模型開發協作的長期關係。

## 500 億美元意味著什麼

Jassy 提出的假設性 500 億市場估值值得細究。500 億美元是 Jassy 對晶片業務若為獨立公司、向 AWS 與第三方銷售晶片時年化營收規模的估計，目前的年化規模則超過 200 億美元。Nvidia 資料中心 GPU 晶片在製造成本之上享有相當豐厚的毛利。若 Amazon 以類似市場定價銷售 Trainium 和 Graviton，而不是將其內化進 AWS 基礎設施成本，這門生意的帳面規模會顯著放大。

這在幾個層面上有重要意義：其一，AWS 的財報利潤率很可能大幅低估了其矽晶投資的戰略價值，因為晶片成本被算進 AWS 服務定價，而非作為獨立晶片銷售報告。其二，也是最實際的——它顯示 Jassy 已釋出這個方向的訊號，他寫道「我們未來很有可能向第三方銷售整櫃的晶片」：將 Trainium 賣給非 AWS 客戶，提供 Nvidia 近乎壟斷的 AI 訓練硬體之外的選擇。

Amazon 目前透過 EC2 執行個體將晶片變現，因此若直接對外銷售，將標誌著轉向參與晶片商用市場競爭的根本轉變。

## 更大的背景：Nvidia 護城河的裂縫

Amazon 200 億美元里程碑的意義，遠超過 Amazon 本身。它是迄今為止最清晰的數據點之一，表明 AI 矽晶市場正在逐漸從 Nvidia 的壓倒性主導地位中分化出來。

2025 年，Nvidia 囊括了約 80% 的 AI 訓練加速器市場份額。但 2026 年，剩餘 20% 的組成已大不相同。Amazon（Trainium）、Google（TPU）和微軟（驅動 Azure AI 工作負載的 Maia 2 晶片）各自運行著規模龐大的自研矽晶計劃——其量級在五年前根本難以想像。合計而言，超大規模雲端業者的內部晶片計劃，每年代表了估計 600 至 700 億美元的算力價值，而這些完全不會流入 Nvidia 的收入報表。

這個動態已在 Nvidia 的前瞻指引中有所體現。雖然該公司持續預測到 2027 年的驚人營收增長，執行長黃仁勳也坦承，超大規模業者的自研矽晶代表的是市場的結構性轉變，而非暫時性偏差。

對 Amazon 而言，200 億美元里程碑既是財報數字，也是向市場發出的信號：AWS 正在為長期矽晶競賽全力押注，Trainium 是嚴肅訓練工作負載的可信 Nvidia 替代方案，而公司有足夠的規模與客戶承諾支撐多個晶片世代的持續投資。Jassy 描述的那個假設性 500 億估值——在公開市場、以獨立業務形式——究竟何時能兌現，仍是未知數。但趨勢的方向，已無懸念。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 12 處。*
