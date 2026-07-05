---
title: "前英特爾首席架構師 Raja Koduri 的 Oxmiq Labs 完成 3500 萬美元 A 輪融資"
summary: "由前英特爾、AMD 晶片架構師 Raja Koduri 創辦的 Oxmiq Labs，完成 3500 萬美元 A 輪融資，用於擴展可授權 GPU 與 AI 架構平台 OxCore。這家公司押注的是：AI 晶片競賽的真正瓶頸不在製造產能，而在設計成本——而可授權架構能讓更多企業以負擔得起的代價打造客製化 AI 矽晶片。"
category: "hardware"
publishedAt: 2026-07-05
lang: "zh"
featured: false
trending: false
sources:
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/07/01/raja-koduris-oxmiq-labs-raises-35m-lower-design-cost-custom-ai-silicon/"
  - name: "Tech Startups"
    url: "https://techstartups.com/2026/07/01/raja-koduris-ai-startup-oxmiq-raises-35m-to-build-ai-chip-architecture-that-cuts-the-cost-of-custom-ai-silicon/"
  - name: "HPCwire"
    url: "https://www.hpcwire.com/off-the-wire/oxmiq-raises-35m-to-scale-oxcoretm-architecture/"
tags:
  - "Oxmiq"
  - "Raja Koduri"
  - "GPU 架構"
  - "客製化矽晶片"
  - "AI 晶片"
  - "A 輪融資"
  - "三星創投基金"
  - "聯發科"
  - "OxCore"
  - "台灣"
relatedSlugs:
  - "2026-07-05-anthropic-samsung-custom-ai-chip-talks-zh"
  - "2026-07-04-qualcomm-tenstorrent-acquisition-talks-zh"
  - "2026-07-01-etched-5b-valuation-1b-sales-inference-chip-zh"
---

Raja Koduri 職涯都在世界最大的晶片公司裡度過——先是在 AMD 擔任圖形晶片關鍵架構師，後來成為英特爾首席架構師兼執行副總裁，主導英特爾重返獨立顯示卡市場的野心。如今，透過他創辦的 Oxmiq Labs，他押注的是：AI 晶片產業最重要的缺口不在製造層，而在設計層——而可授權的 GPU 架構能大幅降低客製化 AI 矽晶片的門檻。

Oxmiq 於 2026 年 7 月 1 日宣布完成 3500 萬美元 A 輪融資，使公司成立以來累計融資總額達到 6000 萬美元。本輪由 Fundomo 與三星創投基金（Samsung Catalyst Fund）共同領投，聯發科（MediaTek）、AM Intelligence Labs、和碩創投（Pegatron Venture Capital）、CDIB-TEN、Darwin Ventures 和 Morgan Creek Digital 等策略性投資人跟投。

## Oxmiq 要解決的問題

從頭打造一顆客製化 AI 晶片的成本極為驚人。單是設計費用——在流片任何一片晶圓之前——在計入工程師人力成本、EDA 軟體授權費、IP 授權金，以及達到量產品質所需的多輪迭代設計週期之後，往往輕鬆超過數億美元。這就是為什麼客製化 AI 矽晶片歷來只是超大規模雲端服務商的專利：Google（TPU）、亞馬遜（Trainium/Inferentia）、微軟（Maia）乃至 OpenAI，其規模使得多年投資具備經濟合理性。

其他所有人——半導體公司、企業 AI 基礎設施供應商、國防計劃、區域雲端服務商——都面臨一個二元選擇：要麼付輝達的價格，要麼承擔代價高昂的自主設計計劃。Oxmiq 的論點是，存在第三條路：授權一個經過驗證、生產就緒的 GPU 架構，在此基礎上建構。

OxCore 正是 Oxmiq 針對這個缺口的解答。它將三個傳統上獨立的元件——GPU、中央處理器，以及針對 AI 矩陣運算優化的客製張量引擎——整合進一個可授權的智慧財產區塊。授權 OxCore 的公司可以針對其特定工作負載打造客製化晶片，無需從頭設計底層架構，大幅壓縮成本與上市時間。

## OxQuilt 與軟體層

Oxmiq 的做法不止於核心架構。公司還開發了 OxQuilt——一種將異質計算小晶片（chiplet）與記憶體整合進單一封裝的計算互連架構，附帶設定工具，讓設計人員能針對不同供應鏈和製造限制調整設計。在供應鏈韌性已成為設計硬性需求的當下，這一特性尤其重要。

軟體層面的故事同樣關鍵。輝達在過去十年裡建立的最深護城河，不是硬體本身，而是 CUDA——那個吸引了數百萬開發者、並讓大量 AI 工作負載程式碼緊緊綁定在輝達生態系的程式設計模型。Oxmiq 的 OxPython 是對這一鎖定的直接回應：它讓現有的 CUDA 和 PyTorch 程式碼無需修改，即可在 OxCore 硬體上運行，大幅降低潛在客戶的遷移門檻。

OxCapsule 負責跨分散式 OxCore 叢集的部署與管理，提供企業客戶在務實評估轉換平台之前所需的基礎設施配管工程。

## 投資人組合背後的戰略邏輯

Oxmiq A 輪投資人陣容的構成，本身就是一個戰略故事。三星創投基金是領投方，而三星的晶圓代工業務是授權 OxCore 的公司在量產時的天然製造夥伴。聯發科是台灣半導體公司，為智慧型手機、汽車及日益增多的 AI 邊緣應用生產晶片，既是潛在客戶，也帶來了對可授權架構商業模式的實戰洞察。

和碩創投直接代表了台灣硬體製造生態系。和碩作為代工廠，負責組裝全球大量消費電子產品，近年來積極投資 AI 晶片基礎設施，作為從組裝向元件端移動的戰略舉措。對 Oxmiq 而言，和碩的加入打開了通往亞洲硬體供應鏈各環客戶的潛在通道。

三星（晶圓代工夥伴）、聯發科（邏輯晶片客戶）、和碩（代工廠）的組合，暗示 Oxmiq 正在構建一個生態系，而不只是一個產品。其戰略目標似乎是將 OxCore 定位為 AI 矽晶片領域的 ARM——一個坐落在眾多不同終端產品之下的可授權架構，而非直接與任何一者競爭。

## Koduri 押注的打破 GPU 壟斷之路

Raja Koduri 對這個市場的思考已持續多年。在 AMD，他領導的團隊讓 Radeon 圖形晶片跨越多個世代追上輝達的競爭力。在英特爾，他獲得了龐大資源來打造 Arc GPU 系列，任務是打破輝達在專業圖形和 AI 計算上的壟斷。兩次努力都沒有完全達到預期——Koduri 在 2023 年底離開英特爾，對輝達的地位為何如此難以撼動有了清醒的認識。

他的結論似乎是：正面與輝達在高端市場競爭，對大多數玩家而言是一場必輸的賭局。更好的選項是擴大市場——讓那些目前除了付錢給輝達別無選擇的公司，也能獲得客製化 AI 矽晶片的途徑——並將 Oxmiq 的智慧財產置於這場擴展的核心。

「降低這個成本，你就拓寬了誰能用它來建構的範圍，」Koduri 在宣布融資時說。野心不是取代輝達，而是建立讓下一代競爭者得以存在的基礎設施。

## 市場時機

Oxmiq 的 A 輪融資，在客製化 AI 矽晶片市場以前所未有的速度移動的時刻落地。Anthropic 剛剛與三星啟動了初步的晶片洽談。另一家 AI 晶片新創 Etched 最近以 10 億美元銷售額達到 50 億美元估值。高通據報正在商討以最高 100 億美元收購 RISC-V 晶片新創 Tenstorrent。

在這個背景下，一家可授權架構公司的 3500 萬美元 A 輪，是一個相對謙遜但上行空間高度不對稱的賭注。如果 OxCore 在當前規劃客製化 AI 晶片的公司中，哪怕只取得一小部分的採用，授權收入在規模下可能相當可觀——而 Koduri 在晶片架構技術與商業兩個面向的深厚積累，賦予 Oxmiq 大多數早期硬體新創根本無法宣稱的公信力。

AI 晶片戰爭正在擴大戰線。Oxmiq 押注的是：讓晶片設計民主化，最終將比贏得任何一場單一設計競賽更為持久。
