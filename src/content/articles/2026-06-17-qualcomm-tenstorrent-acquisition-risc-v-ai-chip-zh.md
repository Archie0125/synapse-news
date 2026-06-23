---
title: "高通傳出洽談以最高百億美元收購 AI 晶片新創 Tenstorrent"
summary: "高通據報正與由傳奇晶片設計師 Jim Keller 領導的 AI 晶片新創 Tenstorrent 進行深入收購談判，交易估值介於 80 至 100 億美元之間。此案若成局，將是高通迄今最大膽的資料中心 AI 加速晶片布局，同時也將成為 RISC-V 生態系的歷史性里程碑。"
category: "hardware"
publishedAt: 2026-06-17
lang: "zh"
featured: true
trending: true
sources:
  - name: "The Register"
    url: "https://www.theregister.com/systems/2026/06/16/qualcomm-said-to-be-circling-ai-chip-biz-tenstorrent-in-10b-risc-v-power-play/5256084"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/qualcomm-mulls-taking-over-jim-kellers-tenstorrent-report-claims-deal-for-ai-chipmaker-would-value-the-company-at-between-usd8-billion-and-usd10-billion"
  - name: "GuruFocus"
    url: "https://www.gurufocus.com/news/8918836/qualcomm-qcom-explores-8b10b-acquisition-of-ai-chip-startup-tenstorrent"
tags:
  - "高通"
  - "Tenstorrent"
  - "Jim Keller"
  - "RISC-V"
  - "AI 晶片"
  - "半導體"
  - "資料中心"
  - "NVIDIA 替代方案"
relatedSlugs:
  - "2026-06-14-nvidia-sk-hynix-ai-memory-partnership-zh"
  - "2026-04-03-riscv-ai-accelerators-zh"
  - "2026-04-03-nvidia-blackwell-supply-zh"
---

週一盤前，高通股價一度勁漲逾四個百分點，市場隨即傳出震撼消息：這家總部位於聖地牙哥的晶片巨頭，正與加拿大 AI 晶片新創 Tenstorrent 進行深入收購談判。消息由《The Information》率先披露，交易估值介於 80 至 100 億美元，若成交將成為半導體史上規模最大的 AI 晶片收購案之一。

兩家公司迄今均未公開確認。高通下一個重大公開場合是 6 月 24 日的投資人日，外界普遍認為，若談判順利，正式宣布極可能在該場合登場。

## Tenstorrent 是誰？

Tenstorrent 成立於 2016 年，總部位於矽谷，主要工程據點在多倫多，花了近十年時間默默打造一套截然不同的 AI 運算架構。有別於 NVIDIA 的 GPU 路線或 Google 的 TPU 方案，Tenstorrent 的加速器完全建構在 RISC-V 指令集架構上——這是一套開放授權、任何公司皆可免費使用的標準，無需支付專利授權費。

公司旗艦產品 Galaxy Blackhole AI 運算平台，將 32 顆加速器塞進一個 6U 機架空間，每顆加速器內建 768 個 RISC-V 核心。這套設計哲學強調彈性與可程式化，而非單純的運算吞吐量——本質上是一場賭注：押注下一代 AI 工作負載需要的是更精細、更具任務針對性的運算，而非矩陣乘法的暴力堆疊。

Tenstorrent 在擁擠的 AI 晶片市場中最獨特的地方，在於其軟體堆疊。公司在編譯器與開發工具上深度投資，讓自家硬體得以在不依賴 CUDA 生態系的情況下執行 AI 模型——而 CUDA 正是目前將絕大多數 AI 從業者牢牢鎖定在 NVIDIA 平台的關鍵。這一差異化優勢吸引了多家超大規模雲端業者與國防承包商實際測試 Tenstorrent 系統，正因為他們希望找到一條擺脫 NVIDIA 依賴的可信出路。

## Jim Keller 的份量

Jim Keller 的工程資歷，在業界幾乎無人能及。他主導設計了 AMD K7 與 K8 處理器架構，也就是讓 AMD 在 2000 年代初期短暫超越英特爾的關鍵產品。之後他加入蘋果，帶領團隊打造出搭載於初代 iPhone 與 iPad 的 A4 及 A5 晶片。2016 至 2018 年，他在特斯拉主導 Autopilot 硬體開發，隨後在英特爾擔任資深副總裁主管矽工程，最終以執行長身分加入 Tenstorrent。

在晶片業，Keller 享有的地位如同樂壇傳奇或體育明星：那種真正能改變公司產品走向的稀有設計師。企業只有在需要破局性變革、而非漸進改良時，才會延攬他。

這樣的光環，是高通願意付出高額溢價的重要原因之一。Tenstorrent 的專利組合，加上從 AMD、蘋果、英特爾、特斯拉等公司挖角而來的菁英工程團隊，是任何金錢都難以在公開市場複製的資產。

## 高通的戰略邏輯

高通目前絕大部分營收來自 Snapdragon 行動與 PC 處理器。這個市場已趨成熟，高端受蘋果 M 系列晶片夾擊，低端則面臨同質化 ARM 設計競爭，AI PC 風潮雖帶來喘息空間，但並不足以為一筆百億美元的收購提供充分依據。

高通真正想要的，是在資料中心 AI 加速晶片市場取得一個可信的立足點。這個市場目前由 NVIDIA 以逾八成市佔率宰制，全球前七大超大規模業者今年在 AI 基礎設施的合計支出超過 2,000 億美元。高通執行長 Cristiano Amon 公開看好 AI 矽晶圓已有兩年，但公司始終缺乏一款具競爭力的資料中心產品。

Tenstorrent 提供了這款產品。更重要的是，它建構在 RISC-V 上，契合高通另一個關鍵戰略目標：降低對 ARM Holdings 的依賴。高通與 ARM 在授權糾紛上已纏訟多時，為高通的架構藍圖帶來不確定性。收購 Tenstorrent，將加速高通轉向一個掌控自身指令集命脈的開放架構未來。

另有一個市場時機因素。AI 晶片市場正進入分析師所稱的「NVIDIA 替代交易」階段——超大規模業者、各國政府與大型企業正積極尋求供應鏈多元化，不願再押注單一主導廠商。高通憑藉其製造合作關係、全球銷售基礎建設與品牌知名度，是最有能力接收這股需求的非 NVIDIA 廠商之一——前提是要有夠有力的矽晶圓拿出來說話。

## RISC-V 生態系的歷史性契機

若此次收購成局，最具結構性意義的影響，恐怕不在高通本身，而在於整個 RISC-V 生態系。

RISC-V 近年作為指令集架構成長迅速，在嵌入式系統、邊緣裝置與主權運算領域（中國的自研晶片計畫、印度國家半導體計畫、歐盟晶片雄心皆有重大 RISC-V 成分）已佔有一席之地。但它始終缺少一個在高效能 AI 運算的旗艦成功案例。

若有高通撐腰的 Tenstorrent，能取得全球頂尖半導體晶圓廠的製造資源與企業銷售網路，這將成為 RISC-V 生態系最有力的商業驗證：清楚表明 RISC-V 不只能在邊緣裝置發光，更能在 AI 推論市場頂端與 NVIDIA 一較高下。

《The Register》以「百億美元 RISC-V 權力棋局」定性此案，這個框架在長遠看來，或許比「高通進軍資料中心」的表面敘事更為精準。

## 後續發展

目前談判被描述為「深入但尚未定案」。此規模與複雜度的交易，常因估值歧見、監管顧慮，或兩組織文化磨合難度而告吹。高通本身也有雄心壯志收購最終落空的前例——最著名的是 2018 年以 440 億美元出價收購恩智浦半導體，最終在監管壓力下放棄。

反壟斷審查同樣是真實的變數。雖然 Tenstorrent 目前尚未在任何市場佔有主導地位，但美國監管機構對半導體業整合的審視態度向來嚴格，加上當前地緣政治的不確定性，任何時間表都難以確定。

若交易成局，正式宣布最可能出現在 6 月 24 日的投資人日。屆時市場將密切觀察高通如何定位 Tenstorrent——是資料中心佈局、是 RISC-V 平台，還是兩者兼具。百億美元的代價，意味高通押注的答案是後者。

對一個眼看 NVIDIA H100 與 B200 訂單已排到 2027 年的市場而言，一家由百億美元支撐、技術成熟、生態開放的 RISC-V AI 加速器廠商的出現，絕非邊緣故事——它或許是這個十年最關鍵的晶片交易。
