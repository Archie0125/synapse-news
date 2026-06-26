---
title: "Qualcomm 傳洽購 Tenstorrent：估值一年暴漲三倍至百億美元的 RISC-V 晶片新局"
summary: "Qualcomm 正與 Jim Keller 領導的 AI 晶片新創 Tenstorrent 進行進階收購談判，估值介於 80 至 100 億美元——較一年前暴漲三倍。若交易達成，結合其近期對 Modular 編譯器公司的收購，Qualcomm 將握有完整的 AI 矽晶片技術棧，向 NVIDIA 的主導地位發起迄今最具說服力的開放架構挑戰。"
category: "hardware"
publishedAt: 2026-06-26
lang: "zh"
featured: false
trending: true
sources:
  - name: "The Register"
    url: "https://www.theregister.com/systems/2026/06/16/qualcomm-said-to-be-circling-ai-chip-biz-tenstorrent-in-10b-risc-v-power-play/5256084"
  - name: "Data Center Dynamics"
    url: "https://www.datacenterdynamics.com/en/news/qualcomm-considers-acquiring-ai-chip-firm-tenstorrent/"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/319017/20260624/qualcomm-bets-14-billion-cracking-nvidias-ai-monopoly-risc-v-open-compiler.htm"
  - name: "AI Unfiltered"
    url: "https://www.arturmarkus.com/qualcomm-in-talks-to-acquire-tenstorrent-for-8-10-billion-jim-kellers-risc-v-ai-chip-startup-valuation-triples-in-one-year/"
tags:
  - "qualcomm"
  - "tenstorrent"
  - "RISC-V"
  - "AI 晶片"
  - "收購"
  - "jim keller"
  - "硬體"
relatedSlugs:
  - "2026-06-24-qualcomm-modular-4b-acquisition-nvidia-moat-zh"
  - "2026-06-25-nvidia-vera-rubin-nvl72-78m-rack-memory-cost-zh"
---

AI 晶片產業可能即將迎來近年來最大的一筆收購案。Qualcomm 正與半導體傳奇人物 Jim Keller 領導的 RISC-V AI 加速器新創公司 Tenstorrent，進行 80 至 100 億美元的收購洽談——估值在短短十二個月內暴漲三倍。

這項消息首先由路透社於 2026 年 6 月 15 日報導，並獲多家媒體獨立證實。若交易完成，將成為歷史上規模最大的 AI 硬體收購案之一，也標誌著 Qualcomm 迄今為止向 NVIDIA AI 基礎設施市場霸主地位發起的最積極挑戰。

## Tenstorrent 是誰？

Tenstorrent 成立於 2016 年，一直在基於 RISC-V 開源指令集架構上打造 AI 加速器硬體。RISC-V 已成為尋求 Arm 授權設計和 x86 架構之外替代方案的公司的集結號角。公司在 NVIDIA 和 AMD 爭奪專有矽晶片生態系統主導地位的市場中，押注開放架構模式——這種模式在軟體領域透過 Linux 和開源框架大獲成功——同樣能在硬體中奏效。

這場豪賭背後的人物是 Jim Keller，矽谷史上最具傳奇色彩的晶片架構師之一：

- 他設計的 AMD K8 處理器將 64 位元運算帶入 x86，在 2000 年代中期幾乎令 Intel 破產
- 他架構的 Apple A4 和 A5 處理器開啟了自研 ARM 晶片時代，令 iPhone 成為全球最具獲利能力的產品線
- 他設計的 AMD Zen 架構讓公司從瀕臨消亡中起死回生
- 他打造了 Tesla 的全自駕晶片
- 2020 年，他在擔任 Intel 矽晶片工程資深副總裁後離職，加入 Tenstorrent 擔任執行長

Tenstorrent 的旗艦產品 **Galaxy Blackhole** 平台於 2026 年初推出，在單個 6U 資料中心機箱中搭載 32 個 AI 加速器，每個加速器擁有 768 個 RISC-V 核心。這個平台為企業提供 NVIDIA H 系列 GPU 的替代方案，無需支付 NVIDIA 的高溢價或接受其專有軟體鎖定。

## 一年估值暴漲三倍

數字清楚說明了過去十二個月 AI 晶片版圖發生了多大的變化。就在一年前，Tenstorrent 正在以 32 億美元的後估值尋求約 8 億美元的融資。公司已推出硬體、吸引工程人才並建立了客戶管線——但以 AI 基礎設施標準衡量，仍是一家中期階段的新創公司。

在此期間，AI 硬體短缺加劇、RISC-V 透過重大部署獲得公信力、Galaxy Blackhole 正式出貨，市場對任何能夠替代 NVIDIA 的方案的渴求急劇擴大。現在 Qualcomm 據報願意支付最多 100 億美元——是去年融資估值的 3.1 倍，大約是 Tenstorrent 當時尋求融資金額的 12.5 倍。

交易結構據報包含與路線圖執行掛鉤的里程碑績效付款——這是晶片新創收購的標準機制，技術承諾最終必須轉化為實際出貨的部署矽晶片。

## Qualcomm 的兩步棋

將此次 Tenstorrent 收購與 Qualcomm 近期其他動作放在一起觀察，戰略邏輯就清晰得多了。

2026 年 6 月，Qualcomm 宣布以 **40 億美元收購 Modular Inc.**，一家持有基於 MLIR 工具鏈基礎設施關鍵資產的編譯器技術公司，該工具鏈位於 AI 框架（PyTorch、JAX）和晶片硬體之間。Modular 的編譯器技術使開發者能夠從單一程式碼庫針對多種硬體後端——這是任何希望取代 NVIDIA CUDA 的生態系統的關鍵基礎設施。

Tenstorrent 則能給 Qualcomm 帶來晶片本身。擁有 Modular 和 Tenstorrent 的 Qualcomm，將掌握一個端到端的 AI 矽晶片技術棧：從將模型轉換為硬體指令的編譯器，到執行這些指令的加速器。這與讓 NVIDIA 如此難以取代的垂直整合戰略如出一轍——CUDA、cuDNN、TensorRT 和 GPU 硬體協同開發。

「RISC-V 是 NVIDIA 的盲點，」一位分析師告訴 The Register。「他們在專有技術上建立了護城河——CUDA、NVLink、記憶體子系統。RISC-V 從定義上就無法被專有化，Qualcomm 這樣的公司把這視為構建生態系統而非僅僅一個產品的機會。」

RISC-V 路線同樣具有地緣政治意義。由於 RISC-V 是一個開放標準，在美國出口許可要求方面與 Arm 授權設計有所不同，RISC-V 加速器在非美國市場越來越具吸引力——尤其是中國，阿里巴巴、華為及各國家支持的機構一直在積極培育 RISC-V 能力。台灣的晶片設計業者也對此高度關注，RISC-V 架構的開放性可能帶來更多本土 AI 晶片設計的商機。

## Intel 虎視眈眈

收購談判並非單純的雙邊交易。彭博社在 2026 年 5 月報導 Intel 曾單獨接觸 Tenstorrent 洽談收購，形成競價局面，幾乎可以肯定這幫助將要求價格推向 100 億美元。

對 Intel 而言，收購 Tenstorrent 有不同的戰略意義：公司正在進行昂貴的晶圓代工業務重組，收購一家知名 RISC-V AI 晶片新創公司，將有助於展示其製程節點能吸引高知名度的客製化晶片設計客戶。但 Intel 目前的資產負債表遠比 Qualcomm 受限，正管理著數十億美元的重組成本，百億美元的收購將面臨董事會和投資者的嚴格審查。

## Jim Keller 的去留之謎

或許最耐人尋味的問題，是收購對 Keller 本人意味著什麼。他在各公司的任期往往遵循一個可辨識的規律：設計架構、監督關鍵里程碑、然後繼續前行。他在 Apple 待到 A5 之後離開。他在 AMD 的 Zen 架構推出後離職。他在 Intel 待了不到兩年。

Keller 尚未公開評論此次收購洽談。創辦人主導的科技公司交易結構通常包含承諾關鍵技術領導層留任 2 至 4 年的協議——但這些「黃金手銬」能否留住擁有 Keller 這般履歷和選擇空間的人，又是另一個問題了。

若他留下，Qualcomm 就能在其最重要的新業務前沿，擁有當今最高效的晶片架構師之一。若他離開，公司繼承了一個強大的團隊、連貫的路線圖和客戶管線——但失去了締造者的遠見。

## 對 NVIDIA 意味著什麼？

Qualcomm 和 Tenstorrent 均未確認此交易，這個階段的收購談判也頻繁破局。但半導體業界都在密切關注，因為若交易完成，其影響將是深遠的。

NVIDIA 在 AI 算力上的主導地位建立在三個相互強化的因素上：硬體效能、軟體生態系統（CUDA），以及歷經二十年建立的供應鏈關係。這些優勢各自並非永久性的，但組合在一起，卻幾乎令人難以攻克。

一個同時擁有最佳開放架構 AI 晶片公司（Tenstorrent）和最佳跨平台 AI 編譯器堆疊（Modular）的 Qualcomm，將同時向這三個因素發起攻勢：在硬體效能上競爭、提供 CUDA 鎖定的軟體定義替代方案，並借助 Qualcomm 與超大規模廠商、OEM 廠商和電信客戶的既有關係，建立 NVIDIA 天然不具備的銷售通路。

這是一個合理的戰略。至於是否是制勝戰略，取決於執行力——以及 Jim Keller 有多少才華會隨著這筆交易一同留下。
