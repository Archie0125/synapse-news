---
title: "Nvidia 砸 20 億入股 Marvell：NVLink 互連網路才是真正護城河"
summary: "Nvidia 宣布以 20 億美元入股 Marvell Technology，並推出 NVLink Fusion 平台，讓第三方客製 AI 加速器能直接接入 Nvidia 的高速互連架構。此舉揭示 Nvidia 的策略轉向：未來的主導地位或許不在 GPU 壟斷，而在掌控整個業界的網路層。"
category: "hardware"
publishedAt: 2026-04-05T10:05:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "The Next Platform"
    url: "https://www.nextplatform.com/connect/2026/03/31/the-2-billion-nvidia-deal-with-marvell-is-about-a-lot-more-than-nvlink-fusion/5213790"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-03-31/nvidia-invests-2-billion-in-marvell-announces-partnership"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/03/31/marvell-nvidia-stock-stake.html"
tags:
  - "nvidia"
  - "marvell"
  - "nvlink"
  - "客製晶片"
  - "ai加速器"
  - "超大規模雲端"
  - "asic"
relatedSlugs:
  - "2026-04-05-openai-gpt-oss-open-weight-zh"
  - "2026-04-05-google-turboquant-kv-cache-zh"
---

2026 年 3 月 31 日，Nvidia 宣布以 20 億美元入股 Marvell Technology，半導體業界的第一反應是防禦性操作——一家晶片巨頭花錢留住關鍵夥伴。這個解讀不算錯，但遠遠不夠完整。更深層的故事，是 Nvidia 如何在 AI 時代重新設計自己的競爭護城河。

## NVLink Fusion：把互連網路變成基礎設施

這筆交易的核心是全新平台 **NVLink Fusion**。在標準 Nvidia 架構中，NVLink 是專有高頻寬互連技術，負責在伺服器內部串聯 Nvidia GPU。NVLink Fusion 將這套架構向外延伸：允許第三方客製 AI 加速器——ASIC、XPU、領域專用晶片——以平等身份接入 NVLink 架構。

具體運作方式如下：Marvell 提供超大規模雲端業者（Google、Amazon、Microsoft）的客製 AI ASIC 設計（XPU）及 NVLink 相容的擴展網路矽片；Nvidia 提供 Vera CPU、ConnectX NIC、BlueField DPU 及 NVLink 交換架構。在 NVLink Fusion 框架下，Marvell 的運算晶片與 Nvidia 的網路暨 CPU 元件原生互通，大幅降低雲端業者的工程整合負擔，實現比現有任何開放標準都更緊密的系統整合。

消息公布後，Marvell 股價單日飆升 11 至 13%，逼近 52 週高點。

## 為何重要：客製晶片的威脅

過去三年，超大規模雲端業者大舉投資客製 AI 晶片，目的正是降低對 Nvidia 的依賴。Google TPU v5 系列、Amazon Trainium 2、Microsoft Maia 100、Meta MTIA——這些專用 AI 加速器都是為特定工作負載量身打造，設計目標是比 Nvidia GPU 更高效、成本更低。

這一趨勢對 Nvidia 的營收結構構成實質威脅。Nvidia 資料中心業務約六成收入來自四大超大規模雲端業者：Google、Amazon、Microsoft 及 Meta。若其中兩家將相當比例的 AI 訓練與推論工作負載遷移至自研晶片，Nvidia 的成長軌跡將發生重大改變。

Nvidia 過去的慣常應對是以超越取勝：更快的 GPU、更好的軟體（CUDA、cuDNN）、更完整的系統整合（DGX Superpod、GB200 NVL72 機架）。與 Marvell 的 NVLink Fusion 合作，則代表另一種策略——與其正面對抗客製晶片趨勢，不如將自己定位成讓客製晶片運作更好的「連接組織」。

## 策略算盤

若 NVLink 成為 AI 叢集的事實標準互連——就像乙太網路成為資料中心網路的預設選擇——那麼每一家為超大規模業者打造 ASIC 的廠商，都自然成為 Nvidia 網路產品組合的客戶。Nvidia 的營收不再因客製晶片趨勢受損，反而能從中獲益。

這是經典的平台策略。微軟在 1990 年代的企業軟體市場有過類似操作：與其爭奪每個應用類別，不如擁有所有應用都在其上運行的作業系統。Intel 也曾試圖讓 Xeon 處理器成為所有工作負載的 CPU 基礎。Nvidia 現在的目標，是讓自己的互連架構成為所有 AI 加速器之下的基礎層，無論誰製造了運算晶片。

Marvell 夥伴關係正是這一策略的概念驗證。Marvell 與四大超大規模業者都有深厚合作關係，為它們設計客製網路矽片。讓 Marvell 打造原生 NVLink 產品，等同於讓主要 OEM 廠商預裝特定作業系統——大幅提高超大規模業者轉用競爭互連方案的代價。

## 入股背後的真實意圖

這 20 億美元投資不純然是財務部位，Nvidia 買到的是策略對齊：

1. **提早掌握 Marvell 產品藍圖**——了解超大規模業者正在設計什麼客製晶片，有助於 Nvidia 規劃 NVLink 需要支援的能力。
2. **工程共同開發槓桿**——負責 NVLink 相容晶片的 Marvell 工程師，自然會針對 Nvidia 網路矽片進行最佳化。
3. **董事會層級的市場洞察**——20 億美元入股很可能附帶觀察員席位或董事會代表席位，讓 Nvidia 即時掌握客製晶片需求走向。

對 Marvell 而言，這筆交易是對其戰略轉型的認可。該公司多年來一直從商品化網路晶片轉向高價值客製矽片，而 Nvidia 作為策略投資方的加入，向超大規模業者客戶傳遞明確信號：Marvell 的客製 ASIC 組合深度整合於 AI 基礎設施堆疊，不再只是邊緣選項。

## 對業界的深遠影響

互連領域的競爭對手——Broadcom、Intel（Gaudi 3）及新興互連新創——如今面對的整合門檻大幅提高。若 Nvidia 與 Marvell 能證明 NVLink Fusion 叢集在頻寬利用率與晶片間延遲上明顯優於競爭方案，AI 叢集設計的經濟性將向 Nvidia 互連標準傾斜。

AMD 近期積極推廣 MI300X 於企業 AI 推論市場，並宣布延伸 Infinity Fabric 以競爭 NVLink 的擴展頻寬。AMD 能否與網路矽片廠商達成類似合作，或者 NVLink Fusion 的先行優勢已難以追趕，將是 2026 至 2027 年硬體領域最值得關注的競爭態勢。

對台灣 AI 基礎設施開發者與採購團隊而言，近期訊號明確：Nvidia 生態系正在擴大覆蓋面。即使未來的叢集採用客製晶片作為運算核心，如今已有一條清晰路徑，讓這些晶片運行在 Nvidia 品牌的網路架構之上。這將改變採購對話、廠商談判，以及整個業界的長期架構規劃。
