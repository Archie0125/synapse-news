---
title: "高通傳出以最高 100 億美元收購 Jim Keller 旗下 Tenstorrent，挑戰輝達 AI 晶片霸主地位"
summary: "高通據報正與 RISC-V AI 晶片新創 Tenstorrent 進行進階收購談判，估值 80 至 100 億美元——約為一年前的三倍。若成交，高通將獲得由傳奇晶片架構師 Jim Keller 打造的技術堆疊，並在 AI 加速器市場正面對決輝達的 CUDA 生態系。"
category: "hardware"
publishedAt: 2026-07-04
lang: "zh"
featured: false
trending: true
sources:
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/qualcomm-mulls-taking-over-jim-kellers-tenstorrent-report-claims-deal-for-ai-chipmaker-would-value-the-company-at-between-usd8-billion-and-usd10-billion"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/318559/20260617/qualcomm-pursues-tenstorrent-10-billion-risc-v-bet-nvidias-blind-spot.htm"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/tenstorrent-intel-qualcomm-takeover-jim-keller-risc-v"
  - name: "AI Unfiltered"
    url: "https://www.arturmarkus.com/qualcomm-in-talks-to-acquire-tenstorrent-for-8-10-billion-jim-kellers-risc-v-ai-chip-startup-valuation-triples-in-one-year/"
tags:
  - "高通"
  - "Tenstorrent"
  - "Jim Keller"
  - "RISC-V"
  - "AI晶片"
  - "輝達"
  - "半導體"
  - "併購"
relatedSlugs:
  - "2026-07-01-etched-5b-valuation-1b-sales-inference-chip-zh"
  - "2026-04-03-riscv-ai-accelerators-zh"
  - "2026-04-03-nvidia-blackwell-supply-zh"
---

根據《資訊》雜誌 6 月 15 日的獨家報導（並獲路透社獨立確認），高通（Qualcomm）正與 RISC-V AI 晶片新創公司 Tenstorrent 進行進階收購談判，收購金額預計落在 80 億至 100 億美元之間。Tenstorrent 由傳奇晶片架構師 Jim Keller 領軍。目前兩家公司均未公開置評，談判仍有破局可能——但這筆交易的規模與背後的戰略邏輯，代表半導體產業在挑戰輝達（Nvidia）對 AI 加速器市場近乎壟斷地位方面，正在發生根本性的轉變。

若交易成真，Tenstorrent 的估值將達到約一年前的 2.5 至 3 倍。大約一年前，該公司正以 32 億美元估值尋求 8 億美元融資。估值在一年內暴漲至三倍，不僅反映了 AI 晶片市場的高溫，更揭示了 Tenstorrent 的特殊性：它是目前在架構上最具說服力、且能真正挑戰輝達花了二十年建構的 CUDA 生態系的替代方案之一。

## 高通究竟在買什麼

Tenstorrent 的核心資產不是某一款特定晶片，而是一套技術堆疊。核心是 Jim Keller 和團隊多年打造的 RISC-V 處理器架構，輔以一套編譯器與軟體框架，原則上可在不依賴輝達專有 CUDA 堆疊的情況下執行 AI 工作負載。

這在戰略上的重要性，比表面看起來更深刻。任何試圖在 AI 加速器市場挑戰輝達的玩家，真正的問題不在硬體，而在軟體鎖定。建立在 CUDA 之上、價值數千億美元的模型訓練與推理基礎設施，其遷移成本之高，實際上已讓英特爾、AMD 和多家新創的技術上相當出色的競爭硬體相形見絀。一款跑得快但無法輕鬆運行現有軟體堆疊的晶片，從實際採購者的角度看，遠不如基準測試所呈現的那麼有價值。

Tenstorrent 的賭注——部分已被其持續成長的客戶管線所驗證——是透過目的性設計的開放編譯器基礎設施，為開發者提供一條以可控的遷移成本在非輝達硬體上運行既有程式碼的路徑，從而打破鎖定效應。這個論點在架構邏輯上是成立的。執行品質是否已達到企業客戶在規模化部署時的要求，則是一個更難回答的問題——而高通的收購，一方面可透過資源投入加速這一進程，另一方面透過成為一家市值逾 1,500 億美元公司旗下業務的信譽光環來提升客戶信心。

Jim Keller 本人是業界有史以來最傑出的處理器架構師之一。他設計了讓 AMD 在 2000 年代中期挑戰英特爾霸主地位的 K8 架構，對 Apple Silicon 的發展軌跡有重要貢獻，並在創辦 Tenstorrent 之前在英特爾主導 CPU 核心開發。他的參與不是象徵性的——他在硬體決策中所嵌入的架構直覺，將直接決定 Tenstorrent 的晶片能否真正達到超大規模運算客戶所需的每瓦效能。

## 高通面臨的戰略困局

對高通而言，收購邏輯源於一個無法迴避的商業現實：無論其智慧型手機晶片業務多麼有利可圖，都面臨結構性的增長天花板。全球手機出貨量預計在可見未來維持低個位數增長，而 AI 加速器市場——目前年規模估計超過 1,000 億美元，年增率超過 50%——才是半導體行業中最具吸引力的利潤正在集中的地方。

高通此前多次嘗試以自研晶片進入 AI 加速器和資料中心市場。其 Oryon CPU 在微軟 Copilot+ PC 產品線中取得了令人印象深刻的效能成績，在邊緣 AI 運算市場建立了灘頭陣地。但真正的 AI 大錢所在——資料中心規模的推理與訓練——至今仍難以突破。收購 Tenstorrent 將一次性給予高通團隊、架構、編譯器堆疊和客戶群，以及由少數能成功顛覆既有運算正規的晶片設計師之一所塑造的研究文化。

英特爾也對 Tenstorrent 表達了收購意向，據悉這在一定程度上加快了高通談判的進程。英特爾的晶圓廠業務和現有資料中心客戶關係，在不同層面上也具備收購邏輯；但英特爾的財務狀況和內部動盪，在 Tenstorrent 的投資人和團隊眼中，使其成為說服力較弱的買家。

## RISC-V 的地緣政治維度

若交易成交，這將是史上最大規模的 RISC-V 公司收購案，其意義遠超當事雙方本身。RISC-V 是一種開放、免版稅的指令集架構，近年在嵌入式系統、汽車和 AI 工作負載中持續擴大影響力，但一直受到商業模式依賴專有架構的既有晶片企業的警惕與抵制。以 100 億美元規模收購最具代表性的 RISC-V AI 晶片新創，將是這一開放指令集在高端運算市場商業可行性的里程碑式驗證。

這也會讓 AI 晶片的地緣政治圖景更加複雜。RISC-V 在美中晶片競爭中已具有特殊地位——被出口管制封鎖在先進製程技術之外的中國企業，已大量投入 RISC-V 架構設計，視之為國產 AI 晶片的突破路徑。一家美國大廠大規模收購 RISC-V AI 晶片企業，將使這一架構更直接地進入國家安全討論，也可能加速國會和行政部門對 RISC-V 工具鏈和 IP 實施出口管制的壓力——而這是開源社群和國際學術界一直強烈反對的方向。

## 對 AI 晶片生態的深遠影響

若高通-Tenstorrent 交易最終完成，將以超越即時競爭格局的方式重塑 AI 晶片競爭地圖。對高通，提供了進入資料中心的可信路徑；對 Tenstorrent，提供了縮短與 CUDA 軟體成熟度差距的資源；而對 Keller——這位在半導體市場以絕對劣勢者身份入局、卻屢屢取勝的架構師——則提供了又一次非對稱的機會。

對輝達而言，可能的回應是繼續投入架構創新以拓寬 CUDA 護城河，並在推理優化硬體上採取更積極的定價策略。而對那些一直在悄悄為「後輝達壟斷時代」的運算未來制定備案計畫的雲端業者和企業客戶而言，一個資金更為充裕的 Tenstorrent，不論支票由誰開出，都是值得歡迎的進展。

交易尚未敲定。但談判已深入到足以讓整個 AI 硬體市場開始給這件事定價的程度：Jim Keller 的下一個重大架構賭注，很可能即將獲得世界最大晶片公司之一的背書。
