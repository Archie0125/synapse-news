---
title: "Odyssey完成3.1億美元B輪融資、估值14.5億：讓AI學會物理學和因果關係"
summary: "世界模型新創Odyssey完成由Natural Capital領投、Amazon、AMD Ventures與Google Ventures跟投的3.1億美元B輪融資，估值達14.5億美元，累計融資3.37億美元。由自動駕駛老將創立的Odyssey押注AI的下一個前沿不是語言，而是物理——能夠以準確因果關係模擬現實世界的AI，為機器人、互動影片和遊戲創作帶來突破。"
category: "startups"
publishedAt: 2026-06-24
lang: "zh"
featured: false
trending: false
sources:
  - name: "TechCrunch: World model maker Odyssey nabs $1.45B valuation backed by Amazon"
    url: "https://techcrunch.com/2026/06/17/world-model-maker-odyssey-nabs-1-45b-valuation-backed-by-amazon-and-other-big-names/"
  - name: "HPCwire: Odyssey Raises $310M Series B to Advance AI World Models"
    url: "https://www.hpcwire.com/off-the-wire/odyssey-raises-310m-series-b-to-advance-ai-world-models/"
  - name: "Unite.AI: Odyssey Raises $310 Million Series B at $1.45 Billion Valuation"
    url: "https://www.unite.ai/odyssey-raises-310-million-series-b-at-1-45-billion-valuation-to-advance-ai-world-models/"
tags:
  - "世界模型"
  - "新創融資"
  - "機器人"
  - "Amazon"
  - "AWS"
  - "物理AI"
  - "互動影片"
relatedSlugs:
  - "2026-06-09-generalist-ai-400m-robot-foundation-model-zh"
  - "2026-06-08-physicsx-300m-series-c-industrial-ai-zh"
  - "2026-06-07-flourish-ai-500m-bezos-neuromorphic-zh"
---

如果人工智慧的下一次重大躍升，不是更大的語言模型，而是一個真正理解物理學的模型呢？這正是Odyssey這家成立三年的AI實驗室的核心命題。2026年6月17日，這家公司宣布完成**3.1億美元B輪融資**，估值達**14.5億美元**，累計融資金額升至3.37億美元。本輪由Natural Capital領投，Amazon、AMD Ventures、Google Ventures跟投，天使投資人名單包含Google首席科學家傑夫·迪恩（Jeff Dean）、投資人Elad Gil、Y Combinator總裁Gary Tan、Vercel創始人Guillermo Rauch，以及Cruise創始人Kyle Vogt。

Odyssey正在建立研究者稱為「世界模型」（world models）的AI系統——這種系統的設計目標不是預測文本序列中的下一個詞元（token），而是預測物理或互動環境的下一個狀態。與其說是ChatGPT，不如說更像一個看過足夠多現實世界之後能夠精確模擬它的物理引擎。

## 世界模型究竟是什麼

「世界模型」這個詞在AI圈被寬泛使用了多年，但Odyssey有一個具體的技術定義作為核心：它的模型被訓練「從物理世界收集資料並以準確的物理學模擬它」，學習行動與結果之間的因果關係，而非詞元之間的統計相關性。

這一區別對應用至關重要。語言模型可以描述「扔下一個玻璃杯會發生什麼」；世界模型可以模擬它的飛行軌跡、破碎模式和碎片分布——並將這種理解推廣到從未見過的新型物體和地面材質。這種因果結構使得統計模式匹配無法可靠生成的那一類預測成為可能。

Odyssey的資料收集方法論反映了這種物理聚焦。這家公司確實是「派人背著攝影機出門」，從主體（agent）穿越環境時的第一人稱視角捕捉世界影片。這種具身視角的資料是刻意的設計選擇：它教導模型從一個在世界中行動（而非僅僅觀察）的系統的視角來表徵世界。

## 創辦人背景

Odyssey的CEO奧利弗·卡梅隆（Oliver Cameron）曾是自動駕駛卡車公司Voyage的共同創辦人，後在Cruise擔任產品副總，是打造第一批大規模自動駕駛車隊的核心成員之一。CTO傑夫·霍克（Jeff Hawke）曾是倫敦自動駕駛新創Wayve的資深工程師，而Wayve也一直在探索神經世界模型作為機器人感知的基礎。

兩位創辦人都帶來了世界模型開發所需的特定能力組合：在規模化物理世界資料收集、感測器融合方面的深厚經驗，以及那種迭代閉環訓練的實踐智慧——正是這種訓練方式，才能讓模型學會預測環境動態，而非只是預測文字。他們的自動駕駛背景並非偶然：AV開發在過去十年正是在反覆應對世界模型被設計來解決的問題：如何教一個系統預測世界的下一步，且精細到足以在其中安全行動。

## AWS為首選雲端，Trainium是那個大賭注

這次融資伴隨著一項戰略基礎設施承諾：Amazon Web Services將成為Odyssey的首選雲端供應商，公司將優化其模型以在AWS的**Trainium**晶片上運行——這是Amazon定位為挑戰Nvidia資料中心統治地位的主力自研晶片。

這在當前競爭格局下是一次有意義的押注。Trainium 2以及即將到來的Trainium 3，代表AWS在爭奪歷來由Nvidia H100和B200 GPU主導的AI訓練工作負載方面最積極的努力。Odyssey承諾進行Trainium優化，為Amazon提供了一個高知名度的前沿訓練工作負載可行性案例，同時Odyssey也可能獲得AWS算力資源的優先訪問和更優惠的費率。

Amazon作為投資者——而非僅僅雲端合作夥伴——的參與，表明這家公司視世界模型為真正的前沿領域，而非純研究好奇心。Amazon的機器人和倉儲物流業務，顯然是能在工廠和倉庫環境中進行模擬和規劃的物理AI系統的理所當然的最終客戶。

## 三個應用領域

Odyssey瞄準三個初始應用領域，每一個都因缺乏可靠的物理感知AI而受限：

**機器人領域。** 最具重要性的近期應用場景。現有機器人系統在新奇環境中表現脆弱，因為它們依賴於規則和場景解析器，這些工具在遭遇訓練分布之外的物體或配置時就會失效。能夠理解因果物理學的世界模型可以進行泛化——它知道一個箱子在缺乏支撐時會跌落，無論它是否見過那個確切的箱子。這正是阻止通用機械臂和移動機器人在精心控制的環境之外可靠運行的能力缺口。

**互動影片生成。** 現有影片生成模型（Sora、Kling、Veo）能生成視覺印象深刻的影片片段，但往往違反物理定律——物體互相穿透、重力行為不一致、陰影與光源不匹配。以物理因果關係訓練的世界模型可以生成不只視覺連貫、更是物理合理的影片，應用場景從電影前期可視化到為其他AI系統生成訓練資料皆有可能。

**電子遊戲創作。** 遊戲天然適合世界模型：它們是具有明確物理引擎的全模擬環境。Odyssey的技術可以讓開發者用自然語言描述遊戲環境，並讓AI生成物理一致的互動世界，大幅壓縮目前佔AAA遊戲開發成本大頭的場景資產創作和世界建構流程。

## 更廣泛的世界模型浪潮

Odyssey並非孤例。Google DeepMind的Genie及其後繼者、Meta的V-JEPA系列，以及一批更小的實驗室，都在向同一個洞見匯聚：AI的下一個能力前沿涉及學習物理世界的結構，而非僅是其語言表面。背後的邏輯是：語言模型已基本上榨取了文本中可用的資訊；物理世界中未被開採的資訊——因果關係、物理學、具身互動——規模遠為龐大，且潛在上更具可泛化性。

在這個背景下，Odyssey獲得的3.1億美元，是對「世界模型範式是真實的、在清晰的產品市場契合出現之前數年就值得投入規模化訓練基礎設施」這一命題的一次投票。

這是一個在AI領域熟悉的投資論題。它與ChatGPT展示大型語言模型能做什麼之前，人們對大型語言模型的同一類押注如出一轍。世界模型處於更早期，更難評估，距消費者應用更遠——但投資者名單包含Google首席科學家和Y Combinator創辦人，顯示Odyssey方法背後的技術可信度被視為真實的。

## 下一步

帶著3.1億美元的新資本，Odyssey的即期優先事項是擴大訓練規模、擴充團隊，以及深化AWS合作夥伴關係，在生產規模上部署Trainium優化的推論。公司尚未公布具體的產品上市時間線，但表示機器人應用距離商業化最近。

世界模型論題的真正考驗，將在Odyssey的系統被部署到真實機器人環境和互動應用中時到來——當問題從「你能模擬物理學嗎？」轉變為「你能把物理學模擬得足夠好，以便對真實任務有實際意義嗎？」在這個問題上，Odyssey已獲得Amazon、Google、AMD以及AI領域一些最受尊重的實踐者的關注。在市場的物理法則最終宣告裁決之前，這份信任也許正是3.1億美元最重要的購買。
