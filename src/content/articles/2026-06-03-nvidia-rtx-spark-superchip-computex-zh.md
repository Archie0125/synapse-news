---
title: "Nvidia RTX Spark 超晶片：Arm＋Blackwell 架構，要把 Windows 變成 AI 作業系統"
summary: "Nvidia 在 Computex 2026 發表 RTX Spark 超晶片——這枚 700 億顆電晶體、台積電 3 奈米製程的 SoC，將 20 核 Grace Arm CPU、Blackwell GPU 與 128GB 統一記憶體整合於單一晶片，在筆電形態下提供 1 petaFLOP FP4 AI 運算效能。搭載 RTX Spark 的筆電將於今年秋季由戴爾、惠普、聯想、華碩、微星和微軟 Surface Laptop Ultra 陸續出貨，標誌 Nvidia 迄今最雄心勃勃的個人電腦布局。"
category: "hardware"
publishedAt: 2026-06-03
lang: "zh"
featured: false
trending: false
sources:
  - name: "Tom's Hardware — RTX Spark 發表"
    url: "https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory"
  - name: "Tom's Hardware — RTX Spark 路線圖"
    url: "https://www.tomshardware.com/pc-components/cpus/nvidia-unveils-dgx-sparrk-roadmap-for-laptops-and-desktop-pcs-at-computex-2026-three-generations-outlined-rubin-followed-by-rosa-feynman"
  - name: "Nvidia GeForce — Computex 2026"
    url: "https://www.nvidia.com/en-us/geforce/news/computex-2026-nvidia-geforce-rtx-announcements/"
  - name: "StorageReview"
    url: "https://www.storagereview.com/news/nvidia-computex-2026-keynote-the-rtx-spark-pc-family-dgx-station-and-physical-ai"
  - name: "HP Newsroom"
    url: "https://www.hp.com/us-en/newsroom/press-releases/2026/computex.html"
tags:
  - "Nvidia"
  - "RTX Spark"
  - "Computex 2026"
  - "Blackwell"
  - "Arm"
  - "筆電"
  - "AI PC"
  - "端側AI"
relatedSlugs:
  - "2026-06-01-nvidia-n1x-computex-arm-laptop-launch-zh"
  - "2026-06-02-intel-crescent-island-ai-gpu-computex-zh"
  - "2026-06-02-amd-computex-2026-x3d-rx9070gre-consumer-zh"
---

黃仁勳身穿標誌性黑色皮夾克踏上 Computex 2026 台北舞台，手中拿著 Nvidia 稱之為自 GPU 問世以來最重大 PC 架構轉變的產品。RTX Spark 超晶片正式發表——這是一枚將 20 核 Grace Arm CPU、Blackwell GPU、128GB 統一記憶體整合於單一 SoC 的高度整合晶片，提供足以在筆電上本地執行 1,200 億參數推理模型的 AI 運算能力，同時薄到可以放進公事包。

這項發表在個人電腦產業的轉折點登場。英特爾和 AMD 過去兩年都試圖透過在傳統 x86 架構上加裝 NPU 加速器，定義「AI PC」的類別。Nvidia 提出的是更激進的方案：完全拋棄 x86、在單一基板上統一 CPU 與 GPU 記憶體，打造一台將智能代理工作流程視為首要工作負載而非附加功能的機器。

## 晶片架構

RTX Spark 是一枚台積電 3 奈米製程、700 億顆電晶體的產品。架構融合兩個晶粒——20 核 Grace CPU 和具備 6,144 個 CUDA 核心的 Blackwell GPU——透過 NVLink-C2C 以 600 GB/s 的頻寬互聯，這個數字遠超傳統筆電中連接獨立 GPU 的 PCIe 通道。統一記憶體池為 128GB LPDDR5X，總頻寬達 300 GB/s。

AI 效能標題數字是 1 petaFLOP（1,000 TFLOP）的 FP4 運算。作為對比，蘋果頂級 MacBook Pro 搭載的 M4 Max 神經引擎算力約為 38 TOPS——雖是不同指標，但量級上的差距說明了專用 AI 晶片與通用加速器之間的落差。Nvidia 將 RTX Spark 定位為蘋果 Silicon 統一記憶體架構的競爭對手——這在十八個月前幾乎是無法想像的比較。

晶片可在本地（無需網路連線）執行最多 1,200 億參數、上下文窗口長達 100 萬 token 的模型。這意味著開發者或研究員可以在筆電上把相當於 GPT-4 參數量規模的模型作為背景程式執行——目前這種能力只存在於雲端基礎設施，或售價超過新台幣三十萬元的專用工作站上。

## 生態系陣容

Nvidia 已鎖定跨越所有價位帶的首發合作夥伴。戴爾、惠普、聯想、華碩和微星均將於今年秋季推出搭載 RTX Spark 的筆電。最受矚目的是微軟 Surface Laptop Ultra——這項合作凸顯了微軟 Windows AI 戰略對 Nvidia 布局的核心地位。Surface Ultra 搭載完整 128GB 記憶體配置，採用 Nvidia 形容能實現「持續 AI 工作負載」（而非瞬間爆發後降頻）的協同設計散熱方案。

華碩 ProArt P14 和 P16 鎖定創意專業人士與 AI 研究員，讓他們能在本地執行圖像生成、音訊處理和文件理解的推理工作，無需將資料送往雲端。惠普的配置偏向企業部署，適用於資料主權和合規要求使雲端 AI 在法律或合約上成問題的場景。

遊戲工作負載的 GPU 效能據稱等同於獨立顯卡 RTX 5070，目前售價約 599 美元，代表 Nvidia GPU 產品線中的主流發燒友定位。若效能對等屬實，RTX Spark 筆電將在與傳統遊戲筆電競爭的同時，增添後者無法比擬的本地 AI 能力。

## 平台野心

RTX Spark 不只是一顆晶片，而是一個平台，Nvidia 的野心是架構層面的。公司正與微軟合作，將 Windows 定位為黃仁勳口中的「智能代理 AI 作業系統」：一個本地 AI 模型可以在無需雲端依賴的情況下，協調檔案管理、應用程式控制、背景調研和多代理任務委派的作業系統。

這個願景與微軟在 Build 2026 發表的 Aion 1.0 高度契合——後者將一個 140 億參數的推理模型內建於 Windows 中，在相容裝置上開箱即用。Aion 1.0 運行在 RTX Spark 硬體上，理論上可創造一台能夠僅靠本地算力，自主規劃並執行多步驟任務的裝置。軟體生態——能為本地模型暴露正確工具介面的應用程式——是否能夠及時成熟以實現這個願景，則是另一個問題。

Nvidia 同時發表 DLSS 4.5，最新一代 AI 超解析度技術，在 RTX Spark 上運行可提供接近原生畫質的視覺效果，同時大幅降低渲染成本。

## 三代路線圖

在產品發表時公布三代路線圖，是 Nvidia 向 OEM 夥伴和企業採購方傳遞長期承諾的刻意信號：

**Grace Blackwell（現行世代）** — Computex 發表的晶片，配備 LPDDR5X 記憶體，2026 年秋季出貨。

**Vera Rubin Spark（第二世代）** — 全新設計的 Vera CPU 搭配 Rubin 世代 GPU 與 LPDDR6 記憶體，預計 AI 運算效能翻倍以上。未宣布上市時程。

**Rosa Feynman Spark（第三世代）** — Rosa CPU 搭配採用垂直 3D 堆疊 GPU 晶粒的 Feynman 架構，允許記憶體頻寬突破平面架構的物理限制。

## 競爭格局

RTX Spark 進入的市場，蘋果 Silicon 已在效能功耗比上保持五年無可撼動的領先地位。M4 Ultra 已充分展示統一記憶體架構對 AI 推理的威力，蘋果的開發者生態系也針對此架構優化多年。Nvidia 的優勢在於龐大的 CUDA 軟體安裝基礎、遊戲生態系的深度，以及關鍵的 Windows——一個佔全球 PC 出貨量約九成、對蘋果硬體市佔率幾乎為零的平台。

高通的 Snapdragon X Elite 將 Windows on Arm 定位為效能故事；RTX Spark 則試圖將其重新定位為極致效能故事。這個差異能否轉化為商業成功，取決於 Windows on Arm 的生產力與 AI 軟體生態是否能填補對舊有 x86 應用程式的相容性缺口——這是從初代 Surface RT 到高通早期 Snapdragon 筆電，每次 Windows on Arm 嘗試都未能克服的痼疾。

Nvidia 的賭注是：這一次，AI 工作負載的吸引力足以讓開發者跟著硬體走，而不必等硬體追上軟體。

產品於 2026 年秋季出貨，售價尚未公布。
