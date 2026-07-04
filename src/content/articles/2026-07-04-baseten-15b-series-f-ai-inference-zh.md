---
title: "Baseten完成15億美元F輪融資，估值達130億美元，AI推論基礎設施競爭白熱化"
summary: "AI推論基礎設施新創Baseten完成15億美元F輪融資，估值在不到五個月內從50億美元躍升至130億美元。該公司現每日處理超過10億次AI推論請求，橫跨18個雲端供應商的87個叢集，年收入成長20倍，企業客戶正將30至50%的模型支出轉向客製化後訓練模型。"
category: "startups"
publishedAt: 2026-07-04
lang: "zh"
featured: false
trending: true
sources:
  - name: "Business Wire"
    url: "https://www.businesswire.com/news/home/20260622645563/en/Baseten-Raises-%241.5-Billion-to-Power-the-Next-Era-of-AI-Inference"
  - name: "Startup Fortune"
    url: "https://startupfortune.com/baseten-raises-15-billion-at-a-13-billion-valuation-as-inference-becomes-ais-most-contested-infrastructure-layer/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/18/ai-inference-startup-baseten-reportedly-raising-1-5b-months-after-its-last-mega-round/"
tags:
  - "Baseten"
  - "AI推論"
  - "F輪融資"
  - "基礎設施"
  - "後訓練"
  - "開發者工具"
relatedSlugs:
  - "2026-07-01-etched-5b-valuation-1b-sales-inference-chip-zh"
  - "2026-07-03-together-ai-800m-series-c-open-source-cloud-zh"
---

Baseten宣布完成15億美元F輪融資，估值達130億美元，相較五個月前E輪的50億美元估值，漲幅高達160%。本輪由Altimeter Capital、Conviction與Spark Capital領投，Sands Capital與Wellington Management共同領投，IVP、Greylock、01A、Blackbird、Durable Capital Partners、Verified Capital、Battery Ventures及D. E. Shaw Ventures等機構也參與其中。Baseten累計募資金額現已突破20億美元。

支撐這輪融資的數字相當亮眼：該公司每日處理超過10億次AI推論請求，在全球18個雲端供應商上運行87個叢集，年收入成長約20倍。其年化收入從2025年12月的約2億美元，在2026年3月已攀升至約6億美元——這樣的增速，在風險投資支持的軟體業中幾乎只存在於試算表裡。

## 為何推論成了獨立的基礎設施戰場

AI商業化歷史的大部分時間裡，業界普遍認為推論是已解決的問題：買算力、選模型、跑就對了。訓練才是技術與資本挑戰的重心。這個觀點正在快速過時。

隨著AI工作負載從內部工具與概念驗證轉向面向客戶、對延遲敏感的生產系統，推論的運維複雜度已急劇攀升。在單一地區以可預期的流量運行單一前沿模型的公司，用通用雲端基礎設施還撐得住。但若一家公司需要在多個地區同時管理十個模型、應對每分鐘數百萬請求的流量峰值、在GPU叢集的冷啟動限制下協調多個微調版本——這樣的公司需要的是專用基礎設施軟體，而非通用雲端控制台。

Baseten執行長Tuhin Srivastava對驅動業務的核心洞察直言不諱：「對於以自有資料建構產品的公司而言，後訓練已成為生死攸關的事。」這句話指向一個事實：基礎模型商品化的時代比多數人預期的來得更快。針對特定領域後訓練、精調的開源模型，如今在許多商業任務上已能以極低成本達到前沿水準。應用層的領先企業，正將30至50%的模型預算轉向客製化與後訓練模型，而非繼續為前沿模型API的高額單價買單。

這一轉變創造了對Baseten所提供服務的結構性需求。在生產規模上運行後訓練或微調模型，需要GPU生命週期管理、跨異質硬體的自動擴縮容、可觀測性管道、計費整合，以及開發者工具——這些都是Baseten多年來精心打磨的能力。推論服務有十幾家可選，但生產級推論基礎設施的供應商屈指可數。

## 客戶名單就是市場地圖

Baseten的客戶名單，讀起來像是AI應用層技術需求最高的企業目錄。AI程式碼編輯器Cursor——已成為軟體工程師的默認生產力工具——在Baseten上運行推論；為醫療系統打造AI臨床文件工具的Abridge亦然；AI原生招募平台Mercor也不例外。AI銷售情報工具Clay、AI網頁開發工具Lovable，以及將大型語言模型應用於醫學研究彙整的OpenEvidence，共同構成了一份橫跨醫療、開發者工具、銷售情報與軟體創作的客戶陣容。

這些客戶的共通點不在於所屬產業或收入規模，而在於他們都需要在生產環境中以高速運行多模型推論——可靠性與延遲直接決定了產品能否正常運作。這些公司的推論不是背景任務，而是產品的關鍵路徑。

## 融資速度本身就是一種信號

資本投入的軌跡值得單獨分析：1.5億美元D輪、九個月後以50億估值完成3億美元E輪、再過五個月以130億估值完成15億美元F輪。短短約十四個月內，流入這家公司的資本總額接近20億美元。

這種速度並非只是投資人對AI概念的盲目追捧。這是對結構性供給限制的理性回應：打造生產級AI推論基礎設施，需要提前承諾GPU產能——在供給緊俏的市場中，要幾個月前就簽合約。想保障未來一年所需算力的公司，必須現在就付錢，即使需求還不確定。Baseten一輪接一輪的大額融資，部分是為了支撐業務成長，部分是為了鎖定服務那些尚未提交承諾的客戶所需的實體基礎設施管道。

領投方Altimeter Capital長期是上市雲端基礎設施公司的重量級投資人，其領投這輪意味著Baseten被定位為擁有穩健收入特性的基礎設施企業，而非純粹的AI風投賭注。

## 推論基礎設施的競爭格局

Baseten並非孤軍奮戰。推論基礎設施市場包含本週宣布以83億美元估值完成8億美元C輪融資的Together AI，主打開源模型托管與GPU雲端；也包含Fireworks AI、Replicate和Modal，三者均瞄準開發者與企業推論市場的重疊需求；當然還有AWS、Azure和Google Cloud等超大規模雲端供應商，它們的AI平台組合中也提供托管推論服務。

Baseten的差異化，在於其對算力之上系統軟體層的專注。該公司賣的不主要是GPU-小時，而是讓GPU-小時在生產環境中可用的運維基礎設施。隨著市場成熟，這個區別日益關鍵。早期雲端運算時代，買算力就是目的；待雲端成熟，價值遷移到了託管服務、資料庫、佇列與可觀測性工具——那些讓算力可靠、可大規模運維的軟體。推論基礎設施市場似乎正在走一條相似的路，只是時間軸被壓縮了許多。

以130億美元估值、6億美元年化收入計，Baseten的市銷率約達22倍——這個溢價倍數意味著投資人預期公司要麼維持非凡的成長率，要麼隨著推論基礎設施層整合而進入毗鄰市場。兩條路都需要強大的執行力，而Baseten迄今已證明了這一點。
