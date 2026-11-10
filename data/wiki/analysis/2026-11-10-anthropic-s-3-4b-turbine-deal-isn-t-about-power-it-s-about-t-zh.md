---
category: industry
lang: zh
published: '2026-11-10T06:29:52.070084+00:00'
sources:
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/data-centers/china-builds-massive-800-megawatt-ai-data-center-campus-to-rival-us-stargate-project-galaxy-campus-delivers-first-120-megawatts-in-a-year-at-one-fifth-the-cost
- name: TechCrunch
  url: https://techcrunch.com/2026/11/09/fervo-now-has-12b-in-orders-for-its-geothermal-power-tech/
- name: Dev.to
  url: https://dev.to/frankchu/34b-bought-anthropic-17-gw-of-gas-turbines-2ce2
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/data-centers/anthropic-skips-six-year-waitlist-with-massive-usd3-4-billion-gas-turbine-generator-deal-firm-takes-over-onepwrs-orders-secures-1-7gw-of-capacity-to-power-ai-data-centers
- name: Dev.to
  url: https://dev.to/delimitter/anthropic-secures-17-gw-of-gas-generators-in-a-34-billion-dollar-deal-23h4
summary: AI 現在最缺的不是 GPU，也不是電，而是一個排到 2031 年的工廠交貨位置。
title: Anthropic 砸 34 億美元買渦輪機：AI 下一場戰爭，比的是誰先插上插座
trending_theme: 電力成為 AI 的最大瓶頸
type: analysis
---

如果你以為 Anthropic 這筆 34 億美元的交易是在「買電」，那就看錯了。它買的是時間，大概六年那麼多。

根據《金融時報》11 月 8 日的報導，Anthropic 在 9 月底同意花約 34 億美元，取得 1.7GW 的 Caterpillar 重型燃氣發電機組。重點在交易結構：這些機組原本是德州聖安東尼奧的設備商 OnePWR Solutions 兩年前下的訂單，後來 OnePWR 籌不到資金，Anthropic 就直接接手。它沒有收購 OnePWR，也沒挖走任何員工，只接下了「排隊位置」，加上安裝所需的工程與施工能力。

先講清楚可信度：雙方都沒回應，路透也說無法獨立證實。不過擔任 OnePWR 財務顧問的 Piper Sandler，在自家官網列出一筆 34 億美元的賣方交易，內容是把「發電平台出售給一家前沿 AI 實驗室」。在這個圈子，這已經算很接近官方證實了。

很多報導的結論是「AI 公司開始買電了」。這句話沒錯，但沒說到重點。更準確的說法是：**AI 的瓶頸已經從晶片變成重工業設備的交期，而且這種交期不是多付錢就能縮短的。** 你沒辦法加價插隊，只能把別人的位置買下來。

## 一個全部賣光的市場

先看供給。全球渦輪機訂單據報已超過 100GW，但年產能只有約 60 到 70GW。美國平均交期已經拉長到六年，新訂單甚至排到 2030、2031 年，而電網併網的排隊時間也差不多長。Caterpillar 第三季發電事業營收年增 30%，達 34.21 億美元，主要來自資料中心。執行長 Joe Creed 說公司在手訂單創下 780 億美元的紀錄。一家百年重工業公司的訂單簿看起來像 2023 年的 NVIDIA，代表遊戲規則已經變了。

再拿 Anthropic 自己的財報來比。根據 11 月 2 日修訂的 S-1，它的採購與租賃承諾總額約 8,954 億美元，其中未來 12 個月要付 698 億。第三季營收 170 億美元，算力與基礎設施支出約 98.6 億，占營收 58%。S-1 還揭露一件事：Anthropic 到 2029 年 5 月前，每個月要付 xAI 12.5 億美元的算力費用。

這是我覺得最沒人討論、卻最關鍵的一點：**Anthropic 每年付超過 150 億美元給頭號競爭對手 Musk 租算力。** 這批渦輪機的價錢還不到三個月的租金，而且買到的是自己的資產。所以自建電力不只是為了讓機房有電，更是為了不再把公司的命脈交給一個巴不得你倒的對手。xAI 很早就懂這件事：今年花了約 20 億美元買移動式燃氣渦輪機，還在密西西比裝了 8 台改裝自 GE 噴射引擎的發電機，合計最高 400MW。Anthropic 等於照著這套劇本走，只是沒用噴射引擎。

## 三種解法，三種世界觀

把這週的三則新聞放在一起，可以看到三種替 AI 供電的路線。

**燃氣：建得快、前期便宜，但燃料錢要付一輩子。** 每 kW 2,000 美元是這三種裡資本支出最低的，有天然氣管線的地方幾乎都能裝。代價是燃料費永遠付不完，還有環保官司。南方環境法律中心（SELC）已經對 xAI 密西西比廠的排放許可提出挑戰。Transformer 創辦人 Shakeel Hashim 直接評論 Anthropic 這筆交易「相當糟糕」（pretty grim）。對一家主打「安全第一」的 AI 公司來說，這種批評的殺傷力比對 Musk 大得多。

**地熱：前期很貴，之後幾乎不花燃料錢。** Fervo 的已簽約營收一季內從 72 億美元跳到 119 億。猶他州 Cape Station 的第一座 100MW 電廠已經併網，替 Google 蓋的 396MW「Cape Google 400」預計 2028 年底完工。成本從第一期每 kW 7,000 美元降到 Google 案的 5,500 美元，還是燃氣的將近三倍，但不需要燃料。Fervo 真正適合 AI 的地方在於模組化：每口新井毛發電量 15MW，幾口井組成一個「GeoBlock」，從最早的 33MW 做到現在的 50MW，剛好對應一個資料中心機房的用電量。蓋好一塊電、開一間機房，電力和算力可以同步擴充。

**中國：自己蓋電網，直接蓋在伺服器旁邊。** 遠景（Envision）在內蒙古烏蘭察布的 Galaxy 園區，不到一年就交付第一個 120MW，SemiAnalysis 估計成本只有美國同級專案的五分之一。整個園區目標在 2027 年底達到 800MW IT 容量，和 Stargate 德州 Abilene 園區的約 820MW 差不多。遠景用自家 420MW 風場搭配四小時儲能，供應前兩期 240MW 負載六成以上的用電。機房內用固態變壓器把 10kV 交流電直接轉成機櫃用的 800V 直流電。美國業者還在搶 Caterpillar 的交貨位置時，一家累計裝了超過 100GW 風機的中國公司，直接用自己的供應鏈解決了問題。

這個對比應該比任何 benchmark 都讓華府緊張。美國在晶片上領先，中國在「把鋼鐵、銅和風快速變成能用的電」這件事上領先。出口管制可以拖慢前者，但美國沒有任何工具能拖慢後者。

## 台灣讀者該想的事

這件事跟台灣的關係比想像中近。

第一，**台灣本身就是電力瓶頸的實際案例。** 經濟部 2024 年就表態，桃園以北 5MW 以上的新資料中心原則上不再供電；核三廠 2025 年 5 月停機後，基載電力更吃緊。當美國 AI 公司都得自己買發電機，台灣想發展主權 AI、吸引國際雲端業者設大型機房，先要回答的不是「有沒有 GPU」，而是「電從哪裡來」。

第二，**這波需求對台灣供應鏈是一大商機。** Galaxy 園區採用的 800V 直流架構，正是台達電這幾年力推的方向。變壓器、配電盤、重電設備的全球短缺，也讓華城、士電、中興電這些重電廠的訂單一路排到好幾年後。過去大家看 AI 概念股只看 NVIDIA 供應鏈，接下來電力設備會是另一條主線。

## 二階效應：AI 公司正在變成電力交易商

Fervo 執行長 Tim Latimer 解釋 Cape Google 400 為什麼要併網：Google 的資料中心還沒準備好時，可以把電賣給其他用戶。「誰都不用等誰。」換句話說，hyperscaler 手上握的已經不是專用電源，而是可以交易的能源部位。Alphabet 在 2025 年底收購能源開發商 Intersect，也是同一個方向。我預估五年內，至少會有一家前沿 AI 實驗室在財報上出現可觀的售電收入。

更深一層看，護城河正在轉移。頂尖模型之間的差距常常只有幾個月，權重會外流，也會被蒸餾，但 1.7GW 的排隊位置沒辦法被抄走。誰能最快啟動下一個 GW，誰就贏。

## 空頭論點

當然也有人說 Anthropic 買在高點。燃氣機組壽命 25 到 30 年，如果推論效率繼續以每年、兩年降一個數量級的速度改善，今天的電力恐慌可能變成 2029 年的閒置資產。Fervo 也還在虧錢，上季營業虧損 4,370 萬美元（但現金有 19 億），補貼後的電價仍約是天然氣的兩倍。

我不買單，至少未來三年不會。到目前為止，每一次效率提升都被用量吃掉了：token 變便宜，Agent 就變多，context 變長，推理迴圈也變深。這回合是 Jevons 悖論勝出。但風險確實存在，只是最後被套住的，不會是現在搶先下單的人。

## 值得關注

1. **2027 年中前，至少再有一家前沿實驗室宣布自有發電 1GW 以上。** 以 Stargate 的規模來看 OpenAI 機率最高，Meta 其次。
2. **渦輪機交貨位置的二手市場浮上檯面。** OnePWR 案是早期案例，接下來會出現專門仲介、甚至專門基金，每 kW 價格明顯突破 2,000 美元。
3. **Anthropic 的碳排會變成 IPO 議題。** 我預期在後續 S-1 修訂或路演中，看到它明確承諾碳抵換，或搭配地熱、核能。「安全實驗室」的品牌扛不住 1.7GW 毫無配套的燃氣。
4. **Fervo 12 個月內簽約營收突破 200 億美元**，並宣布第二個 Cape 等級的場址。Cape Station 資源量從 4GW 上修到 8.4GW，買家只會更多。
5. **Galaxy 如期在 2027 年達標。** 如果真的做到，「五分之一成本」會成為美國 AI 政策圈最難面對的數字，800V 直流架構也會在 2028 年成為業界標準，而台灣電源廠會是最直接的受益者。

GPU 短缺讓 NVIDIA 成為全球市值最高的公司。電力短缺也會造就自己的贏家，而且它們很多長得會更像 Caterpillar。