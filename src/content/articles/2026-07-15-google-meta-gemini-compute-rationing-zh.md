---
title: "Google 對 Meta 限量供應 AI 算力，同時向 SpaceX 租用 GPU 自救——連最大的基礎設施巨頭也追不上自己創造的需求"
summary: "Google 告知 Meta 無法滿足其 Gemini 算力需求，迫使 Meta 限制員工 AI 使用並加速轉向自研的 Muse Spark 模型。為了填補自身缺口，Google 以每月 9.2 億美元的代價向 SpaceX 租用 11 萬張 Nvidia GPU——即便年投資額逾 1,800 億美元的基礎設施巨頭，也已無法跟上自己推動的 AI 需求。"
category: "industry"
publishedAt: 2026-07-15
lang: "zh"
featured: false
trending: true
sources:
  - name: "The Next Web"
    url: "https://thenextweb.com/news/google-caps-meta-gemini-compute-shortage"
  - name: "Forbes"
    url: "https://www.forbes.com/sites/jonmarkman/2026/06/29/google-limits-metas-gemini-usage-over-compute-shortages/"
  - name: "Quartz"
    url: "https://qz.com/google-meta-gemini-ai-compute-shortage-062926"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/319361/20260630/ai-compute-shortage-forces-google-ration-gemini-meta-despite-460b-backlog.htm"
tags:
  - "Google"
  - "Meta"
  - "Gemini"
  - "AI 基礎設施"
  - "算力短缺"
  - "SpaceX"
  - "Nvidia"
  - "資料中心"
relatedSlugs:
  - "2026-07-08-amazon-25b-bond-ai-infrastructure-debt-zh"
  - "2026-07-04-google-ai-electricity-37-percent-surge-zh"
  - "2026-07-08-nvidia-sk-hynix-hbm4-vera-rubin-partnership-zh"
---

多年來，AI 基礎設施的主流敘事一直是「無限擴張」：超大規模雲端業者將不惜一切代價擴建算力，供給遲早會追上需求。但 Google 悄悄對 Meta——世界最大科技公司之一——限量供應 Gemini AI 服務的故事，說明這套敘事需要被修正了。

根據《英國金融時報》6 月底的報導，Google 約在 2026 年 3 月告知 Meta，無法滿足後者請求的 Gemini 算力配額。Meta 一直依賴 Gemini 處理核心安全基礎設施——包括有害內容偵測、詐騙移除和防欺詐——這些應用場景中，Gemini 的表現優於 Meta 自家的開源 Llama 模型。Google 縮減供給後，Meta 指示員工更節省地使用 AI token，並加速將內部工作負載遷移至 Superintelligence Labs 團隊開發的自研模型 Muse Spark。

為了填補自身的供給缺口，Google 另與 SpaceX 簽署協議，以每月 9.2 億美元的代價租用 11 萬張 Nvidia GPU——年化費用高達 110 億美元。一家每年資本支出逾 1,800 億美元的公司，向一家火箭製造商租晶片來服務自己的客戶，堪稱本輪 AI 基礎設施競賽中最荒誕、卻也最真實的縮影。

## 短缺的規模

放在脈絡裡看，這種供給緊缺令人驚訝。Google 是全球最資深的大規模 AI 基礎設施建設者之一，早在大多數公司還搞不清楚「AI 算力」意味著什麼時，它就已部署了十年以上的 TPU（張量處理器）。其資料中心橫跨多大洲，2026 年資本支出承諾超過 1,800 億美元。

但就算如此：Gemini 算力的需求增長速度，依然超過了這個預算所能支撐的供給速度。Google 今年早些時候披露的 4,600 億美元 Gemini 企業合約積壓，不只是一個商業里程碑——它是企業買家簽約承諾 AI 服務的速度，與實體基礎設施建設速度之間結構性錯配的明證。資料中心的規劃、取得許可、建設往往需要 18 到 36 個月；Nvidia GPU 產能儘管在加速提升，仍受制於台積電和 SK 海力士的 CoWoS 先進封裝與 HBM 供應；而軟體端的需求，則是以網際網路的速度增長。

結果是：歷史上最有錢的基礎設施建設者，正在發現「有錢不一定買得到、買得夠快」。Google 對 Meta 限供，不是孤立事件——而是整個系統承壓的症狀。

## Meta 的困境

Meta 選擇以外部廠商的 AI 處理內部關鍵安全基礎設施——審核、詐騙偵測、防欺詐——這個決策因供給緊縮而被迫曝光。依賴外部模型做核心業務，等同於把命脈交在別人手上，Google 的算力收縮，不管出於什麼原因，都驗證了這個風險。

Meta 相關部門收到了「提升效率、節約用量」的指示——企業語言轉譯成白話，就是「能做的 AI 事情比原本計劃的少」。《金融時報》援引消息人士稱，限制措施打亂並推遲了 Meta 多個內部 AI 專案的時程。

這一插曲此後加速了 Meta 去外部依賴的既有進程。由前 Google Brain 研究員團隊領銜、在 Meta Superintelligence Labs 孵化的 Muse Spark，已接手此前由 Gemini 承接的安全審核工作負載。Meta 同時公布了 2026 年 1,150 至 1,350 億美元的 AI 資本支出指引，表明即便短期無法完全自給，公司也在全力向算力自主邁進。

## SpaceX 的 GPU 租約說明了什麼

讓整個局面清晰起來的，是 Google 與 SpaceX 簽訂的 GPU 租約細節：每月 9.2 億美元，換取 11 萬張 Nvidia GPU 的使用權。說白了：一家已擁有全球最龐大 AI 基礎設施版圖之一的公司，以每年 110 億美元的代價向一家火箭公司租芯片，因為它自建的算力已無法服務所有客戶。

SpaceX 的 GPU 算力叢集坐落於田納西州孟菲斯的 Colossus 資料中心，最初為 xAI 開發 Grok 而建，是目前全球最大的單一 GPU 叢集之一，其建設速度創下紀錄。如今它把多餘容量租給 Google——這個直接競爭對手的基礎設施，正在服務另一個競爭對手的客戶——清晰地反映出，算力短缺已促成了整個行業多麼不尋常的商業組合。

對 SpaceX 和 xAI 而言，GPU 租金收入不容小覷：每月 9.2 億美元是相當可觀的額外現金流，且不需要再發射任何火箭。對 Google 而言，這筆費用等於承認：即便投資力度如此之大，短期內仍必須向任何有空閒算力的地方租用，不管戰略關係如何。

## 更深層的啟示

這一算力限供事件，至少傳遞了三層超越 Google-Meta 雙邊關係的訊號。

第一，AI 基礎設施稀缺是真實存在的，且在未來 24 到 36 個月資料中心管線建設完工之前，這個狀況不會消失。任何計劃在此期間大規模部署 AI 的公司，都應將「過度依賴單一基礎設施供應商」列為重大風險加以建模。

第二，「AI 基礎設施就是競爭護城河」的命題，比表面看起來更複雜。Google 在 AI 基礎設施上的投入幾乎超過任何一家公司，卻依然在最重要的客戶面前耗盡了供給。制約因素不是資金或意願，而是物理規律和供應鏈：晶圓代工產能、先進封裝、電力配送和散熱。

第三，AI 算力自主不再只是長遠願景，而是迫切的戰略課題。Meta 在外部算力被削減時，恰好最依賴這算力維持安全業務——這個現實提供了一堂具體而言的課：能夠掌控自身 AI 基礎設施的公司，與租用算力的公司，面對的風險敞口根本不在同一個量級，尤其是在需求持續超過供給的今天。

## 失衡的市場

Google 對 Meta 限供、同時向 SpaceX 租用 GPU 這兩件事並置在一起，呈現出的是一個深度失衡的 AI 基礎設施市場：最大的買家、建設者和部署者，正在同時對客戶限量、向競爭對手租算力、並加速自建——所有事情同步發生。

這不是一個供應鏈清晰、產能規劃可預期的成熟市場的圖景。這是一場技術轉型比任何單一參與者、無論多麼財力雄厚、都快得來不及完全消化的圖景。AI 基礎設施競賽的贏家，將是那些找到辦法在需求爆發之前搶先建好、搶先鎖定算力的人——而這一挑戰，比看上去要難得多。

眼下的混亂是否會隨著資料中心管線的交付而趨於平靜，或者更高層級的新瓶頸是否即將浮現，仍有待觀察。但 Google-Meta 這一插曲讓一件事無可置疑：在 AI 部署的前沿，算力是真正的制約，而這個制約是貨真價實的。
