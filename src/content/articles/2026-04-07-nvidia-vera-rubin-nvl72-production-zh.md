---
title: "NVIDIA Vera Rubin NVL72正式量產：推論效能達Blackwell五倍，提前出貨"
summary: "NVIDIA最新一代AI超級電腦Vera Rubin NVL72已提前進入量產，早於原定2026年下半年時程。這套機架級系統每架可提供3.6艾次方浮點運算的推論算力，每個Token成本較Blackwell降低最多十倍，AWS、Google Cloud、微軟Azure及CoreWeave等雲端巨頭已在首波部署名單之列。"
category: "hardware"
publishedAt: 2026-04-07
lang: "zh"
featured: false
trending: true
sources:
  - name: "NVIDIA新聞室：Rubin平台AI超級電腦"
    url: "https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer"
  - name: "Microsoft Azure部落格：策略性AI資料中心規劃與NVIDIA Rubin部署"
    url: "https://azure.microsoft.com/en-us/blog/microsofts-strategic-ai-datacenter-planning-enables-seamless-large-scale-nvidia-rubin-deployments/"
  - name: "Tom's Hardware：NVIDIA Vera Rubin NVL72 AI超級電腦"
    url: "https://www.tomshardware.com/pc-components/gpus/nvidia-launches-vera-rubin-nvl72-ai-supercomputer-at-ces-promises-up-to-5x-greater-inference-performance-and-10x-lower-cost-per-token-than-blackwell-coming-2h-2026"
tags:
  - "NVIDIA"
  - "Vera Rubin"
  - "GPU"
  - "AI基礎設施"
  - "資料中心"
  - "雲端運算"
relatedSlugs:
  - "2026-04-03-nvidia-blackwell-supply-zh"
  - "2026-04-05-nvidia-marvell-nvlink-fusion-zh"
  - "2026-04-04-amd-mi300x-enterprise-zh"
---

# NVIDIA Vera Rubin NVL72正式量產：推論效能達Blackwell五倍，提前出貨

NVIDIA迄今最強大的AI超級電腦——Vera Rubin NVL72——已正式進入量產，比執行長黃仁勳在2026年CES宣布的下半年時程**提前數月**。這一消息在AI基礎設施軍備競賽持續升溫之際意義重大：雲端大廠與超大規模業者正爭相鎖定機架配額，而NVIDIA宣稱此系統每架推論效能較前代Blackwell平台提升**五倍**、每Token成本降低**十倍**。

Vera Rubin世代自發表以來便備受業界矚目。提前確認量產——恰逢AI算力需求持續超越供給之際——既是NVIDIA技術實力的體現，也是其供應鏈管理能力的重要里程碑。

## NVL72的核心規格

NVL72是機架規模的系統，部署的基本單位是整個機架，而非單一GPU或伺服器刀鋒。每個機架整合了：

- **72顆Rubin GPU**：NVIDIA新一代資料中心GPU，架構針對Transformer推論工作負載深度優化
- **36顆Vera CPU**：NVIDIA自研ARM架構處理器，使Vera Rubin成為首款不依賴AMD或Intel第三方處理器的NVIDIA機架系統
- **ConnectX-9 SuperNIC**：NVIDIA最新一代高效能網路介面卡
- **BlueField-4 DPU**：負責卸載網路、儲存與安全任務，讓GPU專注於AI運算

整套系統每架推論算力達**3.6 EFLOPS（艾次方浮點運算）**，訓練算力達**2.5 EFLOPS**——18個月前，要達到這樣的規模需要好幾個Blackwell伺服器機房才能做到。

Vera CPU的整合尤其值得關注。透過自研處理器，NVIDIA得以在CPU與GPU記憶體子系統之間實現更緊密的整合，降低異質運算架構長久以來面臨的延遲瓶頸。這也讓NVIDIA擁有了從晶片、網路到軟體的垂直整合AI算力堆疊，其策略邏輯與Apple在消費性晶片領域的路徑如出一轍。

## 推論經濟學：十倍成本優勢從何而來

「每Token成本降低十倍」的宣示需要仔細審視，NVIDIA已公布特定工作負載的數據支撐。這一優勢來自三個疊加因素：

1. **更高的算術強度**：Rubin GPU搭載新一代Tensor Core，在FP8及INT4精度格式下的每瓦浮點效能大幅提升——這正是生產環境推論的主流精度需求。
2. **NVLink頻寬擴展**：NVL72的全對全GPU互連消除了跨節點通訊瓶頸，降低了大型模型在模型平行推論時的額外開銷。
3. **記憶體層次重新設計**：Rubin引入了更大的片上L2快取與高頻寬記憶體配置，減少對較慢DRAM的存取次數，提升長上下文請求的批次處理效率。

對於大規模運行前沿語言模型的雲端業者而言，每美元Token數提升兩至三倍就已是翻天覆地的變化——若十倍優勢在生產環境中獲得驗證，則意味著業者可以大幅降低API定價同時改善利潤，或在相同資本支出下運行規模大得多的模型。

## 首批機架的去向

NVIDIA已確認首批量產機架將優先分配給以下合作夥伴：

- **Microsoft Azure**：已將Rubin NVL72整合進威斯康辛州、亞特蘭大及規劃中的Fairwater園區等AI超級工廠建設計畫
- **Amazon Web Services**：列入首波部署名單，上線時程與2026年下半年計畫對齊
- **Google Cloud**：重要早期客戶，但具體部署地區細節尚處保密狀態
- **Oracle Cloud Infrastructure（OCI）**：擴大與NVIDIA的AI基礎設施合作
- **CoreWeave**：這家專注AI運算的雲端業者一直是NVIDIA最積極的早期採購方，已列入首波名單
- **Lambda Labs、Nebius及Nscale**：專注AI算力的新興雲端業者也在首批確認名單中

這樣的分配名單既反映財務承諾，也折射出策略夥伴關係的深度。微軟與NVIDIA的合作已深度延伸至Azure整體技術堆疊，而CoreWeave的整個商業模式就建立在比競爭對手更早獲得最新NVIDIA晶片的基礎上。

## 更大的基礎設施背景

Vera Rubin NVL72正式量產，恰逢AI基礎設施資本支出創歷史紀錄之際。OpenAI正在德克薩斯州阿比林建設一座**1.2 GW的資料中心**——據悉與微軟合作——預計今年完工。這座設施被廣泛認為是Rubin等級硬體的主要目的地之一。

NVIDIA在Rubin世代的供應鏈經過重組，吸取了Blackwell量產期間的教訓——當時因高密度機架配置的散熱管理問題導致交期延誤。此次，NVIDIA與台灣製造夥伴——台積電負責晶片，鴻海（富士康）負責機架組裝——在量產前進行了嚴格的熱管理與電力供應系統驗證。

Rubin GPU採用台積電**N3製程**，並以CoWoS（晶片堆疊封裝）先進封裝技術將GPU晶粒與高頻寬記憶體堆疊配對。台積電的CoWoS產能在Hopper至Blackwell世代交替期間曾是重大瓶頸，目前已透過2025年在新竹與台中廠區的大規模投資獲得顯著提升。

## 對競爭格局的影響

AMD的MI350X加速器與Intel的Gaudi 4均預計在2026年下半年量產，但在前沿推論工作負載的效能基準上，兩者都未能宣稱達到與Rubin NVL72相同的水準。差距或許正在縮小——AMD已在歷代產品中實現顯著的架構改進——但NVIDIA結合硬體領先地位與CUDA生態系統鎖定效應的組合優勢依然強大。

更有趣的競爭動態發生在系統層面：Google的TPU v7與亞馬遜的Trainium 3晶片都旨在降低內部工作負載對NVIDIA的依賴，同時這兩家公司在面向客戶的雲端服務中仍繼續部署NVIDIA硬體。自有晶片是大規模的成本優化，而非完全替代——目前看來，Google與亞馬遜都沒有退出NVIDIA供應鏈的跡象。

對於當下正在做基礎設施決策的新創公司與企業用戶而言，Rubin NVL72的量產改變了算盤。以現行市場價格租用Blackwell算力，如今更像是短期避險，市場普遍預期Rubin等級硬體將在12至18個月內重置定價體系。買方面臨的問題是：現在鎖定多年期Blackwell合約，還是等待Rubin供貨放量？這是對NVIDIA量產爬坡速度的一場押注。

## 黃仁勳對「整架賭局」的押注

Vera Rubin NVL72體現了黃仁勳數年前的一個關鍵策略賭注：NVIDIA必須擁有整個機架——晶片、網路、散熱與軟體——而非只是向ODM廠商出售元件。這一押注如今似乎正在兌現：NVL72是競爭對手單靠授權NVIDIA晶片設計無法複製的產品，因為競爭優勢就在系統整合之中。

十倍Token成本優勢的宣示能否在生產環境中禁得起考驗，尚待時間驗證。但Vera Rubin提前量產的訊號清晰表明：NVIDIA的工程與供應鏈組織正在全速運轉，而AI基礎設施週期正在加速——而非放緩。對台灣的半導體供應鏈而言，從台積電的N3先進製程到鴻海的機架組裝，這一波Rubin訂單潮將是2026年下半年最重要的業務驅動力之一。
