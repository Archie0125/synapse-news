---
title: "OpenAI 加碼 Cerebras：逾 200 億美元晶片合約，押注推論速度而非規模"
summary: "OpenAI 已同意在未來三年內向 Cerebras Systems 支付逾 200 億美元採購其晶片算力，金額約為今年一月簽訂的百億美元協議的兩倍。擴大後的合約還包含 OpenAI 可透過認股權證取得 Cerebras 股權的條款，是迄今為止大型 AI 實驗室擺脫 Nvidia GPU 主導地位最果決的一步。"
category: "ai-ml"
publishedAt: 2026-04-17
lang: "zh"
featured: false
trending: true
sources:
  - name: "The Information"
    url: "https://www.theinformation.com/articles/openai-spend-20-billion-cerebras-chips-receive-equity-stake"
  - name: "Reuters / TradingView"
    url: "https://www.tradingview.com/news/reuters.com,2026:newsml_L4N41002Q:0-openai-to-spend-more-than-20-billion-on-cerebras-chips-receive-stake-the-information-reports/"
  - name: "Digitimes"
    url: "https://www.digitimes.com/news/a20260417VL213/openai-cerebras-ai-server-capacity-nvidia.html"
  - name: "OpenAI"
    url: "https://openai.com/index/cerebras-partnership/"
tags:
  - "OpenAI"
  - "Cerebras"
  - "AI 基礎設施"
  - "晶片"
  - "推論"
  - "Nvidia"
relatedSlugs:
  - "2026-04-17-claude-opus-47-release-zh"
  - "2026-04-17-manycore-tech-hkex-ipo-zh"
  - "2026-04-11-rebellions-400m-rebelrack-nvidia-inference-zh"
---

# OpenAI 加碼 Cerebras：逾 200 億美元晶片合約，押注推論速度而非規模

OpenAI 已同意在未來三年內向晶片新創公司 Cerebras Systems 支付逾 200 億美元，採購其晶圓規模引擎（Wafer-Scale Engine）提供的推論算力，金額約為今年一月協議的兩倍。擴大後的合約同時附帶股權條款：OpenAI 可透過與累計消費金額掛鉤的認股權證，取得 Cerebras 的股份。《The Information》週四率先披露這項協議，業界普遍認為這是 AI 基礎設施史上規模最大的單一採購承諾，其影響範圍遠超這兩家公司本身。

這筆合約落在 AI 算力軍備競賽最激烈的節點。隨著 GPT-5.5「Spud」的預訓練上週確認完成，以及推論需求的成長速度遠超任何內部預測，OpenAI 必須採取行動。它選擇了速度。

## 九十天內從百億翻倍至二百億

合約擴大的速度令人驚訝。今年一月，Cerebras 與 OpenAI 宣布合作時，條件已屬空前：Cerebras 承諾在 2028 年前提供最多 750 兆瓦（MW）算力給 OpenAI，合約金額超過百億美元。Cerebras 當時稱之為「全球規模最大的高速 AI 推論部署」。

九十天後，OpenAI 大幅加碼。新條款將算力上限遠超過原先的 750 MW，惟具體新門檻尚未公開。已獲確認的是股權條款：OpenAI 可透過與消費里程碑掛鉤的認股權證，取得去年底已在那斯達克上市之 Cerebras 的股份。這種架構與 AWS 和 Azure 過去對基礎設施夥伴所採用的長期供應合約相仿——讓客戶在供應商估值上漲時也能分享利益。

## 晶圓規模引擎的速度優勢

要理解 OpenAI 為何押注於此，必須先了解 Cerebras 的技術本質。該公司的旗艦產品晶圓規模引擎（WSE）徹底拋棄了傳統做法——不再把多顆小晶片拼接在電路板上，而是將整片矽晶圓刻製成一塊連續的處理器。目前採用台積電 5 奈米製程的 WSE-3 擁有 4 兆個電晶體，以及 44 GB 的片上 SRAM——足以將大部分模型權重就近存放於運算核心旁，無需頻繁存取較慢的 HBM 記憶體。

實際效果是：Cerebras 宣稱在特定工作負載下，推論延遲可比 GPU 架構低達 15 倍。OpenAI 算力基礎設施負責人 Sachin Katti 在今年一月協議公布時直接點出：「Cerebras 為我們的平台增加了一個專用的低延遲推論方案。更快的回應、更自然的互動，以及將即時 AI 擴展至更多人的更堅實基礎。」

在 ChatGPT 的使用規模下——每天數億活躍用戶橫跨對話、語音與代理任務——即使首字元延遲縮短 100 毫秒，也能為用戶帶來可感知的品質提升。隨著 OpenAI 深入佈局即時語音對話、多小時的代理工作流程，以及傳聞中即將推出的消費性硬體的常駐 AI 助理功能，推論延遲已成為最關鍵的瓶頸。

## 降低對 Nvidia 的依賴

這筆合約的弦外之音，是 OpenAI 降低對 Nvidia 依賴的決心。儘管 OpenAI 是 Nvidia 最大客戶之一，並從 H100、H200 GPU 叢集中獲益匪淺，但其一直看著 Nvidia 資料中心 GPU 的毛利率徘徊在 80% 附近，形成難以突破的成本天花板。

OpenAI 同步推進多條分散路線：代號 OAI-1 的自研 ASIC 推論晶片預計今年於台積電進行光罩製作（tapeout）；AMD MI400 加速器已被引入部分訓練工作負載；Cerebras 晶圓規模引擎現在將承擔相當比例的 ChatGPT 推論流量。

這些並非同一工作負載的替代方案，而是架構上截然不同的互補路徑。WSE 的速度優勢在小批次、對延遲敏感的推論場景最為突出，恰好是 ChatGPT 與語音助理、生產力工具競爭的核心戰場。Nvidia 的 H200 及即將推出的 Blackwell Ultra 在大批次高吞吐訓練和特定記憶體密集任務上仍更有效率。OpenAI 並非取代 Nvidia，而是精心將工作負載路由至最適合的硬體。

## 對 Cerebras 的意義

這份擴大後的合約徹底改變了 Cerebras 的競爭處境。在今年一月的原始協議之前，Cerebras 在 IPO 文件中揭露，阿聯酋的 G42 集團在 2024 年上半年佔其營收的 87%。單一客戶貢獻近九成營收，對任何上市公司而言都是生死攸關的集中風險。百億美元的 OpenAI 合約立即重構了這個風險敞口；將承諾加倍，更讓 OpenAI 實際上成為 Cerebras 在可預見未來的定義性客戶關係，並賦予 Cerebras 擴張資料中心版圖、向台積電鎖定長期晶圓產能所需的營收確定性。

股權認購權的部分又增添了另一個維度。若 OpenAI 按市場預期在 3,000 億美元以上的估值上市，而 Cerebras 透過認股權證持有的股份具有一定規模，這家晶片公司的資產負債表上將多出一項可能遠超任何算力合約價值的資產。

## 對整個產業的漣漪效應

這項協議將以可預期的方式撼動 AI 晶片生態。其他推論晶片公司——Groq、SambaNova、Tenstorrent、d-Matrix——都將把 Cerebras 的成功案例作為自家企業銷售的佐證。每一家主要 AI 實驗室都將面臨內部壓力，要求提出屬於自己的非 Nvidia 推論多元化策略。

對 Nvidia 而言，這筆交易並不構成生存威脅——其在訓練和大批次推論領域的主導地位依然無可撼動——但它是分析師將仔細追蹤的訊號。若推論支出大量向專用低延遲晶片遷移，Nvidia 在 AI 算力的可觸及市場雖不縮水，卻在成長最快的細分市場面臨新的競爭壓力。

2026 年迄今所呈現的更大格局是：主要 AI 實驗室的行為愈來愈像垂直整合的基礎設施營運商，而非軟體公司。OpenAI 對 Cerebras 逾 200 億美元的押注，不只是一項採購決策，更是一份聲明：推論架構已是競爭護城河，而願意投入資本掌控它的公司，將享有純軟體競爭者難以複製的結構性優勢。
