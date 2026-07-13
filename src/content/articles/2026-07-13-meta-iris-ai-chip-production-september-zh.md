---
title: "Meta 自研 Iris AI 晶片通過測試，九月啟動量產"
summary: "Meta 第四代 MTIA 晶片「Iris」僅用六週完成除錯測試，預計今年九月正式量產。該晶片由 Broadcom 協助設計、台積電代工生產，是 Meta 斥資 1,250 至 1,450 億美元資本支出計畫的核心，目標是在 2027 年前將 AI 運算容量倍增至 14 吉瓦。"
category: "hardware"
publishedAt: 2026-07-13
lang: "zh"
featured: false
trending: true
sources:
  - name: "Reuters / US News"
    url: "https://money.usnews.com/investing/news/articles/2026-07-09/exclusive-meta-to-put-ai-chip-into-production-in-september-as-it-looks-to-double-computing-capacity-memo-shows"
  - name: "MLQ News"
    url: "https://mlq.ai/news/meta-to-begin-manufacturing-in-house-iris-ai-chip-in-september/"
  - name: "Data Center Dynamics"
    url: "https://www.datacenterdynamics.com/en/news/meta-could-start-production-of-iris-ai-chip-in-september-report/"
tags:
  - "Meta"
  - "AI晶片"
  - "MTIA"
  - "硬體"
  - "博通"
  - "台積電"
  - "客製矽晶片"
relatedSlugs:
  - "2026-07-08-nvidia-sk-hynix-hbm4-vera-rubin-partnership-zh"
  - "2026-07-04-qualcomm-tenstorrent-acquisition-talks-zh"
  - "2026-07-11-sambanova-1b-series-f-ai-chip-zh"
---

Meta 正在從依賴 GPU 採購，大步邁向自研晶片的垂直整合策略。路透社取得的一份公司內部備忘錄顯示，Meta 第四代 MTIA（Meta Training and Inference Accelerators，Meta 訓練與推論加速器）計畫的晶片「Iris」，在短短六週的除錯測試中未發現重大問題，預計今年九月正式量產。這項里程碑標誌著科技巨頭爭相掌控 AI 完整技術棧的競賽進入新階段。

## Iris 是什麼？它的定位在哪裡？

Iris 並非 Google TPU 或 Amazon Trainium 那種訓練用 GPU 的替代品，而是針對 Meta 生產環境中佔大宗的「推論工作負載」量身打造：包括 Facebook 與 Instagram 的排名推薦演算法、生成式圖像與影片的推論任務，以及日益普及的平台內 AI 功能（如由 Llama 驅動的聊天助手）。

MTIA 產品線目前涵蓋四個版本，發布週期約六個月——大約是業界同類計畫的兩倍速度：

- **MTIA 300**：已量產，負責 Meta 社群平台的推薦與排名任務
- **Iris（MTIA 400 系列）**：2026 年 9 月投產，主攻生成式 AI 推論
- **MTIA 450 與 500**：規劃至 2027 年，鎖定更複雜的生成式圖像與影片工作負載

新一代 MTIA 晶片預計採用台積電 2 奈米製程，在能耗效率上較現行製程有顯著提升。博通（Broadcom）則是設計合作夥伴，雙方合約延伸至 2029 年，涵蓋多個晶片世代。

## 策略核心：打破對輝達的依賴

Meta 2026 年的資本支出預算高達 1,250 至 1,450 億美元，幾乎全數投入資料中心、GPU 採購與自研晶片。這個數字超過全球約 100 個國家的 GDP。如此龐大的規模，反映出 Meta 亟欲解決的核心矛盾：AI 擴張的速度，遠超過輝達能以合理成本供貨的能力。

備忘錄指出：「我們需要的運算資源，已超過市場能以合理成本提供的規模。」Iris 正是為此而生。雖然該晶片並不會全面取代第三方 GPU——業界分析師預期它將吸收推論工作負載的增量，而非取代現有輝達訓練叢集——但它賦予了 Meta 在供應商談判中的議價籌碼，也從輝達的利潤結構中，剝離了一大塊推論成本。

量化目標如下：
- **7 吉瓦**：2026 年底前達成的總運算容量
- **14 吉瓦**：2027 年底目標——十二個月內翻倍

以具體比例理解，14 吉瓦相當於十二座大型核電廠全力運轉的總發電量。

## Iris 在自研晶片大潮中的位置

Meta 加入了一個日益壯大的超大規模雲端業者陣營，皆在積極開發推論專用晶片，以對沖業界所稱「晶片通膨」（chipflation）的風險——訓練與推論工作負載的成長速度，持續超越 GPU 供給能力。Google 的 TPU 計畫從 2016 年即已運行；亞馬遜的 Trainium 與 Inferentia 晶片承擔 AWS AI 服務的核心推論任務；微軟正在研發 Maia AI 加速器；Apple 的神經引擎則深度整合於裝置端推論。

Meta 策略的獨特之處，在於它所要解決的推論規模問題之龐大。Facebook、Instagram、WhatsApp 與 Threads 合計每日活躍用戶逾 33 億，Meta 維運的推薦與排名模型是全球運算需求最密集的系統之一，且必須全天候不間斷運行。即便是微小的推論效率提升，每年也能轉化為數億美元的節省。

Iris 的供應鏈深度也令同業側目。Meta 已確保與三星的記憶體供應協議、與 SanDisk 的快閃儲存合作，以及與住友電工（Sumitomo Electric）的光纖互連設備採購——這種多層次供應鏈管理能力，過去幾乎只有輝達與英特爾才具備。

## 對市場競爭格局的影響

對輝達而言，Iris 的問世並非生存威脅，但確實帶來有感的營收阻力。Meta 目前是輝達最大客戶之一，若 Iris 成功承擔 Meta 推論需求的 15 至 20%，年度 GPU 採購金額將縮減數十億美元。再加上 Google、亞馬遜、微軟、Apple 各自推進的類似計畫，對輝達資料中心業務成長軌跡的合計影響，不可小覷。

對台積電與博通而言，這是明確的利多消息：台積電承攬 Iris 代工合約，進一步鞏固其在尖端客製晶片市場的領導地位；博通則透過與 Meta 延伸至 2029 年的設計合作，在 ASIC 客製市場取得可預期的穩定收入流——此外它也與 Google（TPU 供應合作）及字節跳動維持類似關係。

就整體 AI 生態系而言，Iris 宣告推論基礎設施層正成為繼訓練層之後，下一個被激烈競爭的戰場。能以低成本、大規模執行推論的公司，將在跨產品部署 AI 功能上擁有結構性成本優勢，而這種優勢會隨著模型複雜度的增長而持續複利。

## 後續觀察重點

九月量產意味著 Iris 晶片最快將在 2026 年底前出現在 Meta 的資料中心。公司預計在部署規模達到足夠可信度後，才會公布效能基準與部署指標——時間點可能落在 2026 年第四季或第四季財報發布時。

對開發者與研究社群而言，MTIA 計畫的快速迭代節奏顯示，Meta 對追趕 Google TPU 的成熟度是認真的。Iris 能否在生產環境中交出足以證明龐大資本投入的成績，以及 2027 年 14 吉瓦的宏大目標在全球電網限制下是否可行，將決定這究竟是一場 AI 基礎設施的真正轉型，還是一場昂貴的硬體主權實驗。
