---
title: "NVIDIA Vera Rubin 確認第三季出貨：效能超越 Blackwell 五倍、成本降低十倍"
summary: "NVIDIA 在創下歷史紀錄的 Q1 FY2027 財報電話會議上確認，Vera Rubin 平台將於 2026 年第三季開始出貨，第四季進入量產。這款七晶片架構每 GPU 可提供 50 petaFLOPs NVFP4 推理效能、機架層級達 3.6 exaFLOPs 吞吐量，可能是 Transformer 架構普及以來最關鍵的 AI 硬體世代交替。"
category: "hardware"
publishedAt: 2026-05-27
lang: "zh"
featured: true
trending: true
sources:
  - name: "CNBC – NVIDIA Q1 FY2027 財報直播"
    url: "https://www.cnbc.com/2026/05/20/nvidia-nvda-earnings-report-q1-2027.html"
  - name: "VideoCardz – Vera Rubin NVL72 詳細規格"
    url: "https://videocardz.com/newz/nvidia-vera-rubin-nvl72-detailed-72-gpus-36-cpus-260-tb-s-scale-up-bandwidth"
  - name: "Tom's Hardware – Vera Rubin NVL72 AI 超級電腦"
    url: "https://www.tomshardware.com/pc-components/gpus/nvidia-launches-vera-rubin-nvl72-ai-supercomputer-at-ces-promises-up-to-5x-greater-inference-performance-and-10x-lower-cost-per-token-than-blackwell-coming-2h-2026"
  - name: "Futurum Group – NVIDIA Q1 FY2027 分析"
    url: "https://futurumgroup.com/insights/nvidia-q1-fy2027-data-center-diversification-blackwell-scale-cpu-upside/"
tags:
  - "nvidia"
  - "vera-rubin"
  - "ai晶片"
  - "硬體"
  - "資料中心"
  - "黃仁勳"
relatedSlugs:
  - "2026-05-22-nvidia-q1-fy2027-earnings-china-huawei-concession-zh"
  - "2026-05-08-nvidia-iren-5gw-ai-factory-partnership-zh"
  - "2026-05-18-tsmc-n2-2nm-chip-ramp-ai-hardware-zh"
---

當 NVIDIA 公布 Q1 FY2027 營收 816 億美元、年增 85% 的亮眼成績單時，數字本身幾乎只是配角。更具深遠意義的消息來自執行長黃仁勳的開場發言：Vera Rubin——NVIDIA 下一代 AI 運算平台——確認將於 2026 年第三季開始交付雲端客戶，第四季全力量產。

對過去十八個月來一直為 Blackwell 供應短缺與高昂算力帳單所苦的業界而言，這項確認訊息影響深遠。Vera Rubin 不只是下一顆晶片，它是一個由七個元件構成、專為代理式 AI 時代而設計的全棧平台——而黃仁勳毫不保留地宣告，這個時代已然到來。

「運算需求正在指數級成長——代理式 AI 的拐點已經到來，」黃仁勳在財報電話會議上告訴分析師。「Grace Blackwell 搭配 NVLink 是當今推理領域的王者，每個 token 成本降低了一個數量級，而 Vera Rubin 將進一步延伸這份領導優勢。」

## 七晶片、一平台

Vera Rubin 是 NVIDIA 所謂「極致協同設計」的產物，橫跨整個運算堆疊。平台整合了 2026 年 CES 發表的六種晶片類型，以及三月加入陣容的第七款——Groq 3 LPX 低延遲推理加速器。七者共同構成一體化系統：Vera CPU、Rubin GPU、NVLink 6 交換器、ConnectX-9 SuperNIC、BlueField-4 DPU、Spectrum-6 乙太網路交換器，以及 LPX。

Rubin GPU 是平台核心。由兩個光罩限制晶粒組成，共 3,360 億個電晶體——較 Blackwell B200 多出約 60%——提供 50 petaFLOPs NVFP4 推理效能與 35 petaFLOPs 訓練吞吐量。記憶體升級為 HBM4，每 GPU 配備 288 GB，晶片內頻寬達到驚人的 22 TB/s。這項頻寬數字的重要性絲毫不亞於原始 FLOP 數：大型語言模型推理的瓶頸幾乎永遠在記憶體頻寬，而非算術運算能力。

Vera CPU 同樣野心十足。採用 2,270 億電晶體、基於客製化 Arm「Olympus」核心，規格為 88 核心、176 執行緒，提供 1.5 TB LPDDR5x 容量與 1.2 TB/s 記憶體頻寬。NVIDIA 數十年來一直出貨獨立 GPU 加速器；Vera CPU 宣示的是對主機-加速器邊界兩側同時奪取主控權的嚴肅企圖。

## NVL72：AI 基礎建設的新基本單位

平台旗艦配置 NVL72 將 72 顆 Rubin GPU 與 36 顆 Vera CPU 透過 NVLink 6 連接——單 GPU 交換器頻寬較 NVLink 5 提升三倍。由此產生的數字難以直覺理解：每機架 3.6 exaFLOPs NVFP4 推理吞吐量、2.5 exaFLOPs 訓練吞吐量、20.7 TB HBM4 容量、54 TB LPDDR5x，以及 260 TB/s 的橫向擴展頻寬。

相較於 Blackwell NVL72，NVIDIA 預測推理效能提升 5 倍、每 token 成本降低 10 倍（相同工作負載規模下）。這些不是可以隨手歸檔的規格——它們代表著截然不同的經濟學模式。目前以 Blackwell 速度需要耗資 1 億美元的部署，在理論上可透過 Vera Rubin 基礎建設以約 1,000 萬美元達到相同吞吐量。這些預測是否能在真實世界混合專家模型規模下成立仍待觀察，但方向性趨勢已無庸置疑。

## 供給現實的冷靜審視

對 Vera Rubin 規格的期待，需要用生產現實來節制。NVIDIA 預測 Q2 FY2027 營收約 910 億美元——仍主要由 Blackwell 驅動。按慣例，公司在新 GPU 上市第一年將 60% 至 70% 的產能分配給超大規模雲端業者，其餘部分由企業、政府和雲端新創競搶。

分析師估計 2026 年 Vera Rubin GPU 總產量介於 20 萬至 30 萬顆之間——僅是已安裝 Blackwell 基礎的一小部分。首批客戶預計涵蓋 AWS、Google Cloud、Microsoft Azure、Oracle Cloud Infrastructure 與 CoreWeave，大致依此優先順序分配。

這種供給約束弔詭地解釋了為何 NVIDIA 將 Blackwell 加上 Rubin 合計平台展望至 2027 年累積營收 1 兆美元。Blackwell 仍以產多少賣多少的速度持續出貨；Rubin 新增的是高端層級而非取代前代。隨財報一同宣布的 800 億美元股票回購與 25 倍股息增加，反映管理層對需求跑道遠超任何近期供給上限的強烈信心。

## Groq 3 LPX：低延遲的新維度

第七顆晶片值得單獨討論。Groq 3 LPX——NVIDIA 今年初收購了 Groq 的團隊與智慧財產權——是針對對話式 AI 與代理即時任務所需百毫秒以下響應時間優化的低延遲推理加速器。傳統 GPU 推理是吞吐量優先的；LPX 解決的是一個截然不同的問題維度。

LPX 被納入 Vera Rubin 平台，標誌著 NVIDIA 正在為推理請求以快速突發方式而非批次作業到來的 AI 部署模式而建造——這正是 AI 代理每項任務進行數十次工具呼叫的自然模式。結合 Rubin GPU 處理大量工作負載與 LPX 加速器處理互動延遲，是需要數年才能複製的架構精密度。

## 中國：讓出市場，鞏固焦點

形塑本次財報敘事的一個插曲，是黃仁勳坦率承認 NVIDIA 已「大致放棄」中國先進 AI 晶片市場給華為。禁止 NVIDIA 在中國銷售高端 H100 和 H200 型號的地緣政治限制，使華為昇騰 910C 成為中國超大規模雲端業者與 AI 實驗室的預設選擇。

這項讓步消除了供給預測中的一個潛在變數。NVIDIA 的中國合規版 H20 晶片持續以有限數量出貨，但公司已不再角逐旗艦中國市場。從競爭動態角度看，這意味著 AI 基礎建設霸權之爭現在比以往任何時候都更是 NVIDIA 與雲端業者自製矽片計畫——Google TPU、Amazon Trainium、Microsoft Maia——之間的對決。

## Vera Rubin 對未來兩年的意義

嵌入 Vera Rubin 的架構決策，清晰地反映了對 AI 運算走向的深刻判讀。多步驟代理工作流程、長上下文推理模型與混合專家架構，對記憶體容量和頻寬的壓力遠大於原始算術吞吐量。HBM4 的 22 TB/s 頻寬、260 TB/s NVLink-6 橫向擴展，以及 LPX 的延遲優化，都是針對這些特定需求的解答。

更廣泛的含義是，推理的經濟學即將再次轉變。自 2022 年 ChatGPT 時刻以來每一年，百萬 token 的成本下降了約 80%——不是因為 OpenAI 或 Anthropic 變得更有效率，而是因為他們運行的硬體在固定功耗下變得大幅更快。Vera Rubin 若能實現相對 Blackwell 10 倍的每 token 成本改善，將加速這一趨勢，並擴大部署 AI 代理在經濟上合理的任務範圍。

對在 NVIDIA 分配隊列另一端等待的企業、開發者與研究人員而言，2026 年第三季的到來再怎麼快都不夠快。
