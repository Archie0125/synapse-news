---
title: "Nvidia 發布 N1X：首款 Blackwell 筆電晶片，Windows on Arm 迎來新紀元"
summary: "黃仁勳在 6 月 1 日的 GTC 台北主題演講中正式發布 Nvidia N1 與 N1X，這是 Nvidia 有史以來首款筆電專用處理器。晶片由 MediaTek 合作開發、採用台積電 3nm 製程，搭配 20 核 Arm CPU 與 6,144 個 CUDA 核心的 Blackwell GPU，直攻年出貨量達 1.5 億台、長期由 Intel、AMD 與高通主導的筆電市場。"
category: "hardware"
publishedAt: 2026-06-01
lang: "zh"
featured: true
trending: true
sources:
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/pc-components/cpus/nvidias-long-awaited-n1-n1x-soc-specs-leak-ahead-of-computex-launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-with-12-and-10-core-configs"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/317428/20260530/nvidia-arm-laptop-chip-n1x-confirmed-computex-cuda-rtx-5070-gpu-onboard.htm"
  - name: "ChatForest"
    url: "https://chatforest.com/reviews/nvidia-gtc-taipei-2026-jensen-huang-keynote-n1x-vera-rubin-physical-ai-preview/"
tags:
  - "Nvidia"
  - "N1X"
  - "Computex"
  - "Windows on Arm"
  - "筆電晶片"
  - "Blackwell"
  - "MediaTek"
  - "AI PC"
relatedSlugs:
  - "2026-06-01-nvidia-n1x-computex-arm-laptop-launch-en"
  - "2026-06-01-microsoft-build-2026-mai-coding-models-zh"
---

黃仁勳過去三年不斷告訴全世界，運算的未來屬於加速運算。6 月 1 日，他站在台北的舞台上，在 Computex 2026 開幕前夕，將這個未來帶進了一個 Nvidia 從未涉足的形式：筆記型電腦。

GTC 台北主題演講正式揭曉 Nvidia N1 與 N1X——這是 Nvidia 有史以來第一款筆電系統單晶片（SoC），由 MediaTek 聯合開發、採用台積電 3nm 製程生產。對 Nvidia 而言，這是公司歷史上最具戰略意義的硬體公告之一，將其矽晶版圖從資料中心與桌機延伸至年出貨量約 1.5 億台的 PC 市場。

## 晶片規格全解析

旗艦版 N1X 的規格在筆電 SoC 中可謂頂尖。CPU 採用 20 核心配置，由 10 顆高效能的 Arm Cortex-X925 核心與 10 顆節能的 Cortex-A725 核心組成——架構與高通 Snapdragon X Elite 相近，但關鍵差異在於 GPU。

高通依賴自家 Adreno 圖形架構，N1X 則在相同 CPU 核心之外，搭載了一顆完整的 Blackwell 架構 GPU，擁有 48 個 SM（著色器多處理器）、共 6,144 個 CUDA 核心，效能相當於桌上型 RTX 5070，這並非行動版縮水圖形核心。記憶體方面採用統一式 LPDDR5X 架構，最高支援 128GB，功耗範圍依 OEM 配置在 45 至 80W 之間。

標準版 N1 則針對更輕薄、更省電的設計，CPU 核心數從 10 至 12 顆不等，GPU 叢集規模較小。兩款晶片均採用台積電 N3 製程，與 Apple 最新 M 系列及 Snapdragon X 處理器使用同一節點。

「這是 Grace Blackwell 架構進入 PC 的時刻，」黃仁勳在台北音樂中心向滿場觀眾表示。「每一台我們出貨的筆電，都能在本機原生執行 AI。這從根本改變了人們的工作方式。」

## Windows on Arm 的一次豪賭

Nvidia 進軍筆電並非孤注一擲。Windows on Arm 生態系已花了三年時間逐漸建立可信度。高通的 Snapdragon X Elite 在 2024 年為這個平台帶來了第一顆真正具有競爭力的晶片；Apple 更早就證明了 Arm 筆電可以是業界最佳。

過去一直缺少的，是能在創作、遊戲與 AI 推論工作負載上具備可信 GPU 效能的 Arm Windows 硬體——而這正是 Nvidia N1X 帶來的改變。Nvidia 宣稱 N1X 的 GPU 吞吐量是 Snapdragon X Elite 的兩倍以上，CPU 效能相當，但獨立基準測試要等到正式上市後才能驗證。

時機掌握精準：Intel Lunar Lake 與 Arrow Lake 筆電平台始終未能縮短與 Arm 競爭對手之間的效率差距，AMD 搭載 RDNA 4 架構的行動版晶片也要再等幾個月才上市。Nvidia 正在走進一個絕佳時間窗口。

## 首發 OEM 夥伴陣容完整

與許多晶片發表後硬體還要等好幾個月的情況不同，Nvidia 此次公告已有完整的合作夥伴生態系就位。Dell、Lenovo、Asus 與 MSI 均已確認推出搭載 N1X 的設計，其中 Asus 承諾將在多款 ZenBook 及 ProArt 系列中採用此晶片。

長期被視為 Windows 筆電設計標竿的 Dell XPS 系列，將是最早採用 N1X 的機型之一。Lenovo 計畫在 ThinkBook 與 Yoga 系列中導入，MSI 則鎖定創作者與遊戲相鄰的應用場景，Blackwell GPU 在本機 AI 推論方面的優勢在此處有實質意義。

首批商業產品預計在 2026 年假期購物季前上市，2027 年初起將有更多 SKU 全面普及。開發者與媒體評測用的預量產機台本週將在 Computex 現場展示。

## 對在地 AI 的深遠意義

N1X 內建的 GPU 不只是效能差異化工具，從根本上說，它是一顆本機 AI 運算引擎。6,144 個 CUDA 核心支援 FP8、INT8 與 INT4 精度的 Tensor Core 運算，直接對應在裝置端執行大型語言模型的能力，無需雲端連線。

在 45W 持續功耗下，Nvidia 宣稱 N1X 可以以實用速度——約每秒 15 至 20 個 token——在本機執行 700 億參數的量化模型。達到 80W 上限時，可支援更大的上下文視窗與更快的推論速度。對於重視隱私的使用者、受監管產業、或網路連線不穩定地區的用戶而言，這從根本上改變了 AI 輔助軟體的經濟模型。

微軟作為共同發表者登台，Windows 事業部長 Panos Panay 形容 N1X 是「讓每一款 Windows 應用程式都成為 AI 原生」的平台。Arm Holdings 執行長 Rene Haas 則透過視訊出席，稱此晶片是對 Arm 架構運算長期押注的最佳印證。

## 對競爭格局的衝擊

高通股價在發表後的早盤交易中下跌約 4%，反映出投資人將 N1X 視為對 Snapdragon Windows on Arm 主導地位的直接威脅。高通多年來深耕生態系建立與微軟合作夥伴關係，傾力使 Snapdragon 成為 AI PC 首選平台，如今面臨一個擁有更強 GPU 實力與 Nvidia 品牌加持的競爭者。

Apple 的比較則更為複雜。Apple Silicon 在 Arm 筆電的每瓦效能方面仍是業界翹楚，M4 世代的神經引擎在 Apple 封閉軟體生態中的在地 AI 推論仍具優勢。但 Apple 既不對外銷售晶片也不授權平台，這意味著每一位需要搭載 Windows 的 Arm 筆電的企業 IT 買家，如今都多了一個強大的新選擇。

對 Intel 而言，這個時機相當難堪。Meteor Lake 與 Arrow Lake 未能兌現承諾的世代性躍升，Arrow Lake 的遊戲效能表現更是令人難堪。Nvidia 以 GPU 實力從意想不到的方向切入市場，給 Intel 帶來了全新的壓力。

## 接下來的動向

Computex 本週從 6 月 2 日正式開幕，Nvidia 將在各合作夥伴展區進行 N1X 的實機展示。黃仁勳的主題演講也預告了下一代資料中心 GPU 平台 Vera Rubin 的進展，並觸及 Nvidia 的具身 AI（Physical AI）藍圖——但對消費市場而言，N1X 無疑才是這場發表的最大焦點。

筆電晶片市場不會在一夜之間被重塑。高通在 OEM 關係與 Windows 整合方面的深厚積累仍在，Intel 的製造協議與產品藍圖也提供了緩衝空間。但自 Arm 正式切入 Windows 筆電市場以來，這是頭一次出現一個以 GPU 為核心競爭力、能夠在創作者與開發者最在乎的規格上正面對抗的強勁競爭者。光是這一點，就已經是一場地殼變動。
