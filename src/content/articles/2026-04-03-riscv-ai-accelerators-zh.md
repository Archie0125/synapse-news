---
title: "RISC-V AI 加速器：沒人在關注的黑馬"
summary: "當所有人都在搶 NVIDIA 和 AMD GPU 時，一群新創正在用開源 RISC-V 架構打造 AI 晶片。離成熟還有幾年，但對 AI 主權的影響巨大。"
category: "hardware"
publishedAt: 2026-04-03
lang: "zh"
featured: false
trending: false
sources:
  - name: "Chips and Cheese"
    url: "https://chipsandcheese.com"
  - name: "ServeTheHome"
    url: "https://www.servethehome.com"
tags:
  - "risc-v"
  - "ai-chips"
  - "open-hardware"
  - "semiconductors"
relatedSlugs:
  - "2026-04-04-amd-mi300x-enterprise-zh"
---

## 你沒在關注的最重要晶片架構

RISC-V 是開源處理器架構 — 想像 Linux，但是是給晶片的。任何人都可以用 RISC-V 指令集設計處理器，不用付授權費給 ARM 或 Intel。

多年來，RISC-V 限於微控制器和嵌入式裝置。現在它正在進入 AI 加速器市場，其影響比當前晶片的能力所暗示的更大。

## 實際在出貨的東西

幾家公司正在 RISC-V 上打造 AI 加速器：

**Esperanto Technologies** 的 ET-SoC-1 是一顆 1000 多核心的 RISC-V 晶片，設計用於 AI 推理。效能不跟 NVIDIA 競爭，但每顆晶片功耗只有 20 瓦，瞄準的是邊緣推理 — 在裝置上跑模型，不是在資料中心。

**Tenstorrent**（Jim Keller 的公司）正在打造結合通用 RISC-V 核心和自訂張量處理單元的 AI 硬體。他們的 Wormhole 晶片能同時做訓練和推理。

**SiFive** 提供 RISC-V 核心給其他公司整合到 AI SoC 中。他們是 RISC-V 世界的 ARM — 他們不做最終晶片，做的是裡面的核心。

**中國公司**（阿里巴巴的玄鐵、賽昉科技、嘉楠科技）正積極為 AI 應用採用 RISC-V，部分是技術原因，部分是因為這避開了 ARM 和 x86 的授權依賴 — 那些在貿易衝突中可能被武器化。

## 為什麼這在技術之外也重要

RISC-V AI 晶片不會在明年取代 NVIDIA。也不會在後年。但三個動態讓它們在策略上很重要：

**AI 主權**：想要國產 AI 能力但缺少半導體 IP 的國家可以在 RISC-V 上建構，不用授權外國架構。印度、巴西和幾個歐盟成員國正是因為這個原因有 RISC-V 計畫。

**邊緣 AI**：AI 的未來不只是資料中心 — 是數十億裝置在本地跑推理。這些裝置需要便宜、高效、可客製化的晶片。RISC-V 的開放性質讓它非常適合邊緣的客製 AI 加速器。

**ARM 風險**：ARM 的 IPO 和後續授權變更讓一些客戶緊張。RISC-V 是對 ARM 變太貴或太嚴格的保險。NVIDIA 自己在某些產品中也在 ARM 核心旁邊使用 RISC-V 核心。

## 障礙是真的

RISC-V AI 晶片面臨真正的挑戰：

- **軟體生態不成熟**：CUDA 有 15 年的函式庫和工具。RISC-V AI 工具還在建造中
- **效能差距顯著**：當前 RISC-V AI 晶片在同等任務上比 NVIDIA 最好的慢 5-10 倍
- **製造管道**：先進晶片需要先進晶圓廠，而晶圓廠的取得是有限的且受地緣政治約束
- **碎片化風險**：沒有主導供應商的情況下，不同的 RISC-V AI 晶片可能有不相容的軟體堆疊

## 觀察重點

- Tenstorrent 的下一代晶片 — Jim Keller 有交出突破性架構的紀錄
- 中國 RISC-V AI 晶片採用率 — 量會先從這裡來
- RISC-V AI 軟體工具（編譯器、框架）能不能成熟得夠快來吸引開發者
- 歐洲和亞洲政府資助的 RISC-V 計畫 — 政策資金驅動早期採用

*RISC-V 不會在 2026 或 2027 年顛覆 AI 晶片市場。但到 2030 年，「每一顆 AI 晶片都跑在兩家美國公司授權的專有架構上」的想法會像大型主機時代一樣過時。問題是你是已經為那個轉變做好準備，還是到時候再手忙腳亂地追趕。*
