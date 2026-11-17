---
title: "Nvidia RTX Spark 超級晶片顛覆 PC 市場格局"
summary: "在 Computex 展上，黃仁勳發表與聯發科共同打造的 PC 晶片 RTX Spark，將 Blackwell GPU 與聯發科 CPU 結合。Nvidia 進軍 PC 市場，也使 Intel、AMD 與高通股價下跌。"
category: "hardware"
publishedAt: 2026-06-06
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "Tom's Hardware – Nvidia RTX Spark 超級晶片"
    url: "https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory"
  - name: "CNBC – Nvidia 新款 PC 晶片"
    url: "https://www.cnbc.com/2026/06/02/nvidias-new-pc-chips-are-ceos-bid-to-own-every-part-of-ai-stack.html"
  - name: "Nvidia GeForce – Computex 2026 發表"
    url: "https://www.nvidia.com/en-us/geforce/news/computex-2026-nvidia-geforce-rtx-announcements/"
tags:
  - "Nvidia"
  - "RTX Spark"
  - "ARM"
  - "Blackwell"
  - "Computex"
  - "AI PC"
  - "半導體"
relatedSlugs:
  - "2026-06-05-nvidia-cosmos-3-physical-ai-omnimodel-zh"
  - "2026-06-04-big-tech-725b-ai-capex-race-zh"
---

Nvidia 在週一宣布進軍 PC 市場。

在台灣 Computex 展的主題演講中，執行長黃仁勳（Jensen Huang）正式發表 **RTX Spark**——一款與聯發科共同開發、適用於 PC 的系統單晶片。這不只是一款新產品，更代表 Nvidia 意圖掌控從資料中心到終端裝置的完整 AI 運算堆疊，同時直接衝擊 Intel、AMD 與高通在消費性 PC 市場的版圖。

## RTX Spark 的技術底蘊

它將 Nvidia 先進的 **Blackwell GPU** 與 **聯發科 CPU** 整合在同一顆系統單晶片上。

128 GB 的記憶體容量格外值得關注。Apple M4 Max 的上限也是 128 GB，高通 Snapdragon X Elite 的天花板則是 64 GB。RTX Spark 一舉追平 Apple，並將高通遠拋在後。對於需要在本機執行大型 AI 模型的企業用戶而言，這個數字意味著過去只能在伺服器上跑的任務，現在在筆電上也能完成。

晶片採用 **台積電 3 奈米製程**，與 Apple M4 系列相同，在效能與功耗之間取得競爭性的平衡。

## 效能實測數字

Nvidia 公布的幾項場景測試頗具說服力。在一台 14mm 厚的輕薄筆電、不插電的情況下，RTX Spark 可以：

- 即時渲染 **90 GB 的 3D 場景**
- **12K 影片**即時剪輯
- 以 **1440p 解析度、100fps** 執行《印第安納瓊斯：大圓》

這些都是 GPU 吃重的工作負載。在 AI 推論方面，FP4 Tensor Core 搭配 128 GB 統一記憶體，讓 RTX Spark 可以在不壓縮精度的情況下，本機執行 **70B 以上參數的大型語言模型**——這是 Windows 消費性筆電的首次突破。

## 代理式 PC 的新視野

黃仁勳在發表會上將 RTX Spark 定位為「**代理式 AI 作業系統**」的基礎——一個讓 AI 代理程式能在 Windows 桌面持續運行、監控螢幕、處理音視訊，並在不需要雲端往返的情況下自主執行任務的環境。

Nvidia 與 Microsoft 已在韌體與驅動程式層面深度合作，將這些能力整合進 Windows 11。對於敏感數據處理、法規遵循要求嚴格的產業，本機 AI 代理的吸引力顯而易見——數據永不離開裝置，規避了雲端 API 帶來的資料主權疑慮。

## 上市時程與合作夥伴

RTX Spark 預計於 **今年稍後**登場，將搭載於 **微軟、Dell、HP、華碩、聯想**與 **微星（MSI）**的新款 Windows PC。

Nvidia 同時公布了三代路線圖。下一代代號 **Vera Rubin**，將採用 LPDDR6 記憶體提升頻寬；第三代 **Rosa Feynman** 同樣列在路線圖上，記憶體規格尚未揭露。

## 對 Intel、AMD、高通的直接衝擊

RTX Spark 發表後，**AMD、Intel 與高通**股價隨即應聲下跌。市場的擔憂不是短期競爭，而是結構性威脅：Nvidia 打算為 PC 打造系統單晶片，威脅到長期由 Intel 與 AMD 雙雄掌控的市場。

Intel 押注 Lunar Lake 與 Panther Lake 的 NPU 加速路線；AMD 力推 Strix Halo APU；高通以 Snapdragon X 系列定義 Windows on Arm 體驗。但 RTX Spark 的殺手鐧在於三家都缺乏的能力：一個在晶片層級與高頻寬統一記憶體深度整合的世界級顯示核心。

## Nvidia 的垂直整合佈局

拉遠視角來看，Nvidia 的策略脈絡清晰可見。資料中心端，H100 與 B200 Blackwell GPU 主宰 AI 訓練與推論市場；軟體端，CUDA 與 NIM 微服務平台構成生態護城河；工作站端，DGX Spark 桌機瞄準開發者族群；現在再加上 RTX Spark 筆電，Nvidia 的 AI 堆疊延伸至每一位終端用戶。

企業可以用相同的 CUDA 函式庫、相同的 NIM 容器、相同的模型格式，在資料中心伺服器與員工筆電上跑一致的 AI 工作流程。這種端到端的一致性，是強大的生態鎖定效應。

## 定價仍是最大變數

Computex 發表刻意略過定價細節。以 Nvidia 的定位與製造成本推算，RTX Spark 筆電的起售價可能落在新台幣 5 萬元以上。這意味著短期內 RTX Spark 可能仍是企業與專業用戶的選項，而非大眾消費市場的主流。

但無論定價如何，這場發表已確立一件更重要的事：Nvidia 要進入 PC 市場了。接下來 18 個月，PC 產業的競爭格局將圍繞這個現實重新布局。

6 月 8 日，Apple WWDC 2026 即將登場，外界預期 Apple 將以新一代 Apple Intelligence 功能正面回應。AI PC 的軍備競賽正在加速——而且幾十年來首次，最受矚目的筆電晶片，不來自 Intel、AMD 或高通。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 8 處。*
