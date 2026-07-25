---
title: "Etched完成3億美元C輪融資，估值七個月翻倍至103億美元，SK海力士加持無GPU推論晶片"
summary: "專為Transformer模型推論設計的AI晶片新創Etched，以103億美元估值完成紅杉資本領投的3億美元C輪融資，距離上輪50億美元估值僅七個月。手握10億美元晶片訂單，加上SK海力士以策略投資人身份加入，Etched正在發起對輝達推論領域最有力的一次挑戰。"
category: "hardware"
publishedAt: 2026-07-25
lang: "zh"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/07/23/ai-chip-startup-etched-defies-skeptics-hits-10-3b-valuation-from-big-name-investors/"
  - name: "GlobeNewswire"
    url: "https://www.globenewswire.com/news-release/2026/07/23/3332366/0/en/Etched-raises-300M-at-a-10-3B-Valuation-to-Scale-Production-of-Frontier-Scale-Inference-Hardware.html"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/etched-300m-series-c-10-3b-valuation-sequoia-sk-hynix"
tags:
  - "Etched"
  - "AI晶片"
  - "推論晶片"
  - "半導體"
  - "紅杉資本"
  - "SK海力士"
  - "新創融資"
relatedSlugs:
  - "2026-07-25-intel-q2-2026-earnings-comeback-zh"
  - "2026-07-08-nvidia-sk-hynix-hbm4-vera-rubin-partnership-zh"
  - "2026-07-01-etched-5b-valuation-1b-sales-inference-chip-zh"
---

七個月前，Etched以50億美元估值完成5億美元融資，半導體業界普遍將它視為一家資金充裕的技術實驗室。2026年7月23日，這家AI推論晶片新創再度宣佈以103億美元估值完成3億美元C輪融資——估值在不到一年內翻倍——並手握10億美元的晶片訂單。紅杉資本（Sequoia Capital）領投，安德森霍洛維茲（a16z）、Jane Street、Diffusion以及記憶體巨頭SK海力士均以新投資人身份加入。

TechCrunch指出，這是紅杉有史以來領投的估值最高C輪融資。更重要的是，它為一個自Etched 2022年成立以來飽受質疑的論點背書：專為Transformer模型推論打造的ASIC晶片，是一門真實可行的生意。

## Etched究竟造的是什麼

AI晶片的討論大多聚焦於「訓練」——訓練大型模型需要龐大的GPU算力集群。輝達的H100、H200幾乎已成為AI算力的硬通貨，主導了OpenAI、Anthropic、Google DeepMind、Meta的模型研發。

但訓練只是等式的一半。模型訓練完成後，需要被「部署」——即每秒回應數百萬用戶查詢的「推論」（inference）工作。推論才是AI產品真正被用戶感知的地方，也是AI算力支出比重快速增長的領域。

Etched的核心論點是：輝達的GPU為了兼顧訓練、推論、科學計算等各種應用而設計，這種通用性帶來了多餘的成本與耗電。純推論工作根本不需要這麼「萬能」的晶片。

Etched的旗艦產品「Sohu」，被設計為只做一件事：以極高效率對Transformer模型執行推論。透過拋棄訓練所需的架構彈性，Etched宣稱Sohu在標準語言模型服務任務中，每美元可產出的tokens吞吐量比輝達H100集群高出10至20倍。

## 估值為何七個月翻倍

10億美元晶片訂單是估值快速攀升最直接的解釋。七個月前，Etched是一個技術路線可信但尚未有大量訂單的新創；如今它手握一份訂單積壓清單。

這些客戶的身份至少和金額本身一樣重要。大規模推論的主要買家是少數幾類大客戶：主要雲端服務提供商（AWS、Google Cloud、Microsoft Azure）和模型公司本身（OpenAI、Anthropic、xAI、Meta）。任何能開出10億美元晶片支票的企業，幾乎必然來自這個名單，儘管Etched至今未公開具體客戶。

SK海力士以策略投資人身份加入，同樣意義重大。SK海力士是全球兩大高頻寬記憶體（HBM）供應商之一，HBM是現代AI晶片維持算力利用率的關鍵記憶體架構。輝達的AI晶片領導地位，在很大程度上建立在其優先獲得HBM供貨的能力上。Etched有SK海力士作為策略夥伴，等同於在供應鏈層面取得了光靠燒錢買不到的優勢。

紅杉選擇在這個時間點以103億美元估值領投C輪，代表的不只是財務判斷，更是對Etched技術路線和市場動態的深度認可。紅杉的半導體投資組合涵蓋過去20年最具影響力的晶片公司，這樣規模的押注絕非輕率決定。

## 專一化的底氣

半導體業界歷來重視通用性。通用晶片適用於廣泛應用場景，可降低客戶集中風險；而特製晶片提供性能優勢，卻建立了對特定技術路線的依賴。

Etched的賭注是：Transformer架構已如此主流，「針對它設計」不是冒險，而是準確預判未來。自2017年「Attention is All You Need」論文問世以來，Transformer幾乎成為所有前沿AI系統的底層架構——無論是語言模型、圖像生成、影片創作還是機器人控制。

若Transformer在未來五到十年持續主導AI架構，那麼專為Transformer優化的晶片就不是窄化，而是切中要害。

質疑者認為，混合專家模型（MoE）、狀態空間模型（Mamba）等新架構正在複雜化這個論點。若AI產業偏離純Transformer路線，Etched的單一用途晶片便面臨挑戰。Etched表示其架構可以適應這些變體，但這場爭論仍未塵埃落定。

## 在現實世界中挑戰輝達

做出性能超越輝達的晶片是可能的；做出能搶走輝達訂單的生意則困難得多。

輝達在推論市場的優勢遠超晶片本身。其CUDA軟體生態歷經二十年打磨，讓開發者可以一次編寫推論代碼，在所有輝達硬體上運行。遷移至非輝達晶片的轉換成本，不只是晶片價格，還包括重寫軟體堆疊、重新培訓運維團隊、接受生產系統的新風險。

Etched的應對策略是直接鎖定超大規模雲端業者和模型公司——而非廣泛的企業客戶。這些大型買家有能力調配工程師適配新硬體，有強烈動機壓低推論成本（規模化後每年數十億美元的開銷），也有足夠採購量讓大型客製化晶片協議具備經濟效益。

10億美元訂單意味著這個策略在早期採用者身上已開始奏效。接下來12至18個月的關鍵驗證，是這些訂單能否轉換為成功的部署案例，進而擴大安裝基礎——還是供應鏈挑戰、軟體整合摩擦、或輝達的競爭反制讓勢頭放緩。

## 更大的推論晶片戰局

Etched並非孤軍。Groq以低延遲語言處理單元（LPU）競逐類似市場，Cerebras用晶圓級晶片提供龐大記憶體頻寬，Tenstorrent由前AMD首席架構師Jim Keller打造更通用的AI晶片，高通也持續擴大雲端端側推論佈局。

紅杉、a16z和SK海力士願意同時在這個時間點押注Etched，反映出精明投資人相信推論晶片市場夠大，可以孕育多個成功企業——即便輝達維持多數市佔。全球規模前沿AI模型的年化推論成本已達數千億美元規模，足以支撐多家晶片公司共存。

對台灣半導體生態而言，Etched的崛起值得高度關注。Etched的Sohu晶片由台積電代工，其成長直接帶動台積電先進製程的需求；而SK海力士的戰略投資，也意味著這場推論晶片競賽在記憶體端進一步牽動台灣供應鏈的布局。

三位哈佛輟學生在2022年創辦一家晶片公司，四年不到便以103億美元估值、10億美元訂單站上舞台——這要麼是應用特定AI晶片將成為下一波半導體價值創造浪潮的最佳佐證，要麼是矽谷這輪AI熱潮中最昂貴的一場賭注。現有的訂單積壓，讓前者的機率看起來越來越高。
