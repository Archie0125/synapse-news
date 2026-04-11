---
title: "韓國AI晶片商Rebellions獲4億美元融資，推出RebelRack挑戰輝達推論霸主地位"
summary: "南韓AI晶片新創Rebellions完成4億美元Pre-IPO融資，估值達23.4億美元，股東包含三星、SK海力士與沙烏地阿美。同步發表RebelRack與RebelPOD推論系統，其核心Rebel100 NPU據稱以3.2倍的功耗效率達到與輝達H200相當的效能。最新與SK電信及Arm的合作更將版圖延伸至主權AI與電信基礎設施市場。"
category: "hardware"
publishedAt: 2026-04-11
lang: "zh"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/03/30/ai-chip-startup-rebellions-raises-400-million-at-2-3b-valuation-in-pre-ipo-round/"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/03/30/ai-chip-startup-rebellions-raises-400-million-ipo.html"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/semiconductors/isscc-2026-rebellions-ucie-rebel-100"
  - name: "Telecom Reseller"
    url: "https://telecomreseller.com/2026/04/10/rebellions-collaborates-with-sk-telecom-and-arm-targeting-sovereign-ai-and-telecom-infrastructure/"
tags:
  - "Rebellions"
  - "AI晶片"
  - "推論"
  - "輝達"
  - "硬體"
  - "南韓"
  - "IPO"
relatedSlugs:
  - "2026-04-03-nvidia-blackwell-supply-zh"
  - "2026-04-05-cognichip-ai-chip-design-zh"
  - "2026-04-08-semiconductor-sales-record-2026-zh"
---

多年來，AI加速器的市場敘事幾乎是一場獨角戲：輝達（Nvidia）設計晶片、輝達制定價格，其他人只能付帳。這個故事如今有了可信的對手。南韓AI晶片商Rebellions在ISSCC 2026以其Rebel100 NPU引發廣泛關注後，又宣布完成4億美元Pre-IPO融資，並同步推出兩款量產推論平台——向外界明確宣告：在利潤豐厚的AI推論市場上，逐走輝達H系列GPU的競賽已進入最激烈的階段。

## 8.5億美元融資，瞄準十億規模IPO

本輪融資由未來資產金融集團（Mirae Asset Financial Group）與韓國國家成長基金聯合領投，Rebellions估值定於23.4億美元。這筆4億美元的Pre-IPO資金，讓公司累計融資額達到8.5億美元，其中6.5億更是在過去短短六個月內到位。融資速度之快，反映出企業市場對推論最佳化替代方案的迫切需求——輝達資料中心GPU至今仍供不應求，且價格居高不下。

策略投資人的組成透露出更深遠的布局野心。三星（Samsung）與SK海力士（SK Hynix）——兩家控制HBM記憶體供應鏈的巨頭——雙雙列名股東，讓Rebellions在高頻寬記憶體的取得上擁有近水樓台的優勢。沙烏地阿美（Saudi Aramco）的入股同樣意味深長：這家能源巨頭正在波灣地區大力建設主權AI基礎設施，迫切需要能繞過美中出口管制戰場的晶片來源。

Rebellions表示將用這筆資金加速美國市場布局，並為預計在2026年下半年的公開上市做好準備。

## Rebel100：從推論需求出發的原生設計

Rebellions競爭力的核心，在於一套從零開始為推論而生的架構，而非訓練導向GPU的二次改造。Rebel100 NPU是一款四晶片（quad-chiplet）系統級封裝，由四顆320mm²神經處理晶片組成，每顆搭載12層堆疊HBM3E記憶體，單封裝共144 GB容量。晶片間採用UCIe-A互連——這是業界最早規模量產此技術的產品之一——提供的晶片間頻寬，有效解決了訓練時代GPU挪作推論用途時的記憶體瓶頸問題。

核心數字同樣亮眼：每顆Rebel100晶片達到約2 PFLOPS FP8算力，每個DMA引擎提供高達2.6 TB/s的頻寬。Rebellions在ISSCC 2026上展示的設計在原始效能上與輝達H200相當，但公司反覆強調的差異化優勢是功耗——聲稱每瓦產出的tokens數（TPS/W）較輝達H100高出3.2倍。對於每天處理數百萬推論請求的超大規模雲端業者而言，電費是最主要的營運成本之一，這個數字意義重大。

軟體生態系的故事同樣關鍵。過去幾代客製AI矽晶片常常敗在軟體相容性，而非硬體效能上。Rebellions明確支援PyTorch 2.x、vLLM與Triton，且不需要分支或修補版本——這對已在這些框架上建置LLM推論技術棧的企業客戶而言，是至關重要的信任保證。

## RebelRack與RebelPOD：把推論能力規模化

兩款新產品將Rebel100轉化為可直接部署的基礎設施。**RebelRack**是基礎推論計算單元：一套量產機架系統，由16顆加速器組成，提供16 PFLOPS FP8推論算力，設計上可直接嵌入現有資料中心機房，符合標準供電與散熱規格。

**RebelPOD**則是橫向擴展方案。它將多組RebelRack（2、4、6、8或16架）叢集整合，對上層編排系統呈現統一的系統映像。最大規格的RebelPOD-16，搭載1,024顆Rebel100加速器，提供高達1,024 PFLOPS FP8推論算力。以此規格執行700億參數以上的大型語言模型，在高並發場景下完全可行，且無需承受2023年以來困擾採購部門的GPU供貨不確定性。

業務長Marshall Choy直接點出產品策略的核心邏輯：Rebellions無意與輝達在訓練市場正面交鋒——那是他們承認輝達在現有這代產品中已在結構上取勝的領域。目標是推論層：這是AI技術棧成長最快的部分，功耗效率的差異可直接換算為每token成本，而且從GPU切換到NPU的轉換成本最低，因為推論工作負載本身無狀態、易於重新部署。

## SK電信與Arm：主權AI的新戰線

4月10日，Rebellions宣布與SK電信及Arm展開三方合作，在超大規模雲端市場之外開拓第二條成長路徑。這項合作以主權AI部署與電信基礎設施為目標——政府機關與國家電信業者在這些領域需要本地製造、可掌控且不受美國出口限制的AI算力。

Arm的參與帶來CPU IP與軟體生態，讓Rebel100系統得以連結電信級網路功能與邊緣AI部署。SK電信不僅是客戶背書，更成為Rebellions進入亞洲電信業者評估算力自主化進程的重要通路。

主權AI的敘事在東南亞、中東與歐洲尤具共鳴——自2022年美國實施晶片出口管制以來，各國政府已明顯加速本土AI基礎設施的投資。Rebellions已在美國、日本、沙烏地阿拉伯與台灣設立法人實體，這個版圖清楚表明其野心遠不止於南韓本土市場。

## 全局視角：推論才是新戰場

Rebellions發表新產品的時機，與AI工作負載經濟學的結構性轉變高度契合。生成式AI時代的前三年，訓練主導了資本支出與市場目光。但隨著前沿模型趨於穩定，企業從實驗階段轉入量產部署，推論現已佔據全部AI算力支出的六至七成。這正是Rebellions搶先布局的戰場。

這條賽道並不孤寂：Groq、Cerebras與AMD MI300X系列都在搶食推論市場，輝達本身也針對推論場景推出了Blackwell架構的優化版本。但Rebellions帶著一個值得注意的差異化進場——從頭設計、以H200相當效能搭配遠低功耗的原生推論矽晶片，完整的機架級產品線，以及來自三星與SK海力士這兩家HBM供應鏈掌控者的背書。

在輝達發表下一代推論導向架構之前，Rebellions能否將技術公信力轉化為企業市場份額，仍是最關鍵的問題。預計在2026年下半年啟動的IPO，將是市場是否準備好押注挑戰者的最清楚指標。

H系列無人匹敵的時代，或許終於有了截止日期。
