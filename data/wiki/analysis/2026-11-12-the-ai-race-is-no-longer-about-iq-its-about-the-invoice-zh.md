---
category: ai-ml
lang: zh
published: '2026-11-12T18:39:19.635640+00:00'
sources:
- name: Tom's Hardware
  url: https://www.tomshardware.com/pc-components/cpus/amd-shares-how-it-can-retain-95-percent-of-server-performance-with-just-half-the-dram-sidestepping-memory-shortages-with-mext-tech-powers-over-100-servers-already-running-with-plans-to-expand-to-2-000-servers-in-2027
- name: The Verge
  url: https://www.theverge.com/ai-artificial-intelligence/1030787/google-gemini-4-carbon-public-rollout
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/google-broadens-its-ai-hardware-portfolio-with-two-new-specialized-chips/
- name: Hacker News
  url: https://strandsagents.com/blog/amazon-saves-millions-replacing-sonnet-with-strands-decider/
- name: Hacker News
  url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/
summary: 模型分數再高，若每完成一件事都比對手貴五倍，企業只會把它留在簡報裡。
title: AI 不再比誰最聰明：真正的戰場是每張帳單
trending_theme: AI 競賽轉向效率
type: analysis
---

AI 軍備競賽最誠實的排行榜，不在研究機構，也不在模型公司的發表會，而在財務部的雲端帳單上。模型可以在測驗中多拿兩分，但若一次客服分類要多花十倍 token、回應慢三倍，還得多塞一櫃 HBM，它就不是產品，只是一場昂貴的表演。

過去幾年的敘事非常好懂：模型越大，能力越強。2017 年 Transformer 架構出現，2020 年 GPT-3 把參數量推到 1,750 億，之後每家公司都想用更大的模型證明自己站在最前面。可是 2022 年 DeepMind 的 Chinchilla 已經示範過，700 億參數、吃進更多訓練資料，可以擊敗 2,800 億參數的 Gopher。規模從來不是唯一答案，只是最容易拿來做行銷的答案。

現在，市場終於開始問比較務實的問題：同一件工作，到底要花多少錢、等多久、占多少記憶體，失敗後又要重跑幾次？

Google 推出的 Gemini 4 Carbon 正好暴露了這個轉折。Carbon 被定位成處理長時間程式設計、資安與科學研究的最強模型；但 Google 同時明講，多數軟體工程與知識工作應該繼續使用較輕的 Gemini 4 Argon。翻成白話，就是「最聰明的模型不該接每一張單」。

Carbon 的促銷價是每百萬輸入 token 2 美元、輸出 token 10 美元；11 月底後調成 4 美元與 20 美元。根據 [The Verge 整理的價格比較](https://www.theverge.com/ai-artificial-intelligence/1030787/google-gemini-4-carbon-public-rollout)，促銷期間約為 OpenAI GPT-6 Astra 的五分之一、Anthropic Fable 5.2 的四分之一。這個數字很吸睛，卻也很容易誤導。

因為 Carbon 本來就會比 Argon 使用更多 token。它會展開更多路徑、反覆查核，甚至執行多輪驗證。每顆 token 半價，不代表完成一件工作只要半價；如果它為了回答同一題用了四倍 token，總帳單照樣比較高。

因此真正該看的單位不是「每百萬 token 多少錢」，而是「每完成一項可交付任務多少錢」。這裡要把工具呼叫、重試、錯誤回復、人工覆核、等待時間，以及代理人跑到一半失控的成本全部算進去。企業買的不是 token，而是完成的工作。

Google 至少開始用這個語言說話。它宣稱 Carbon 在 CursorBench 4.0、Perplexity WANDR 與 Zapier AutomationBench 都排名第一，而且每項任務的成本比第二名外部模型低超過一半。這仍然是 Google 挑選並公布的成績，不能照單全收；但「每件任務成本」顯然比再貼一張模型多贏 2.3 分的長條圖有意義。

Antigravity 平台預覽的「swarm」功能，更能看出 Google 想賣的不是單一超級模型。Carbon 負責規劃、架構與稽核；便宜的小模型分頭執行；另一批驗證模型專門挑錯。這套系統比較像一間公司：昂貴的主管不負責影印，基層員工也不替公司決定十年技術路線。

問題在於，多代理人不會自動變便宜。假設一個任務原本呼叫 Carbon 一次，改成八個代理人各跑兩輪，再加兩個驗證者，token 消耗可能先膨脹十倍。所謂 swarm 若沒有預算上限、終止條件與成果驗收，只是把「模型亂講話」升級成「一群模型開會亂講話」。

Amazon 的案例更值得企業注意，因為它不是把大型模型換成另一個大型模型，而是把大型模型直接請出場。

Amazon 內部系統原本用 Claude Sonnet 4.6，把客服升級、容量需求、自動警報與資安發現等工單分進 20 個類別。工程師後來改用 Strands 決策模型。這種模型不寫文章，也不需要產生一段看起來很有道理的思考文字；它只接收工單內容、比較 20 個選項，再輸出每個分類的機率與信心分數。

根據 [Strands 公布的案例](https://strandsagents.com/blog/amazon-saves-millions-replacing-sonnet-with-strands-decider/)，新系統的表現追平甚至超過正式環境中的 Sonnet，成本卻降低 98%，一年可省下數百萬美元。團隊先測試 20 億參數的 Strands Decider，再選用表現較好的 E4B Gemma 4 版本。模型部署在 SageMaker `ml.g5.xlarge`，也就是一張 24GB 的 Nvidia A10G；實際占用約 19GiB，一次判斷約 640 毫秒。

更有意思的是周邊架構毫不神祕：SQS 收工單、Lambda 呼叫模型、SageMaker 提供推論端點、AppConfig 控制切換、CloudWatch 看指標。Amazon 沒有為工單分類蓋一座 AI 神殿，只是讓一個小模型做它擅長的事。

這對 frontier 模型公司不是好消息。多數企業工作並不是破解數學猜想，而是分類、抽取、排序、路由、風險判斷與核准。若小型決策模型能接走其中 80%，最昂貴的模型就會從預設選項變成「信心不足才升級」的二線支援。企業毛利會改善，但按 token 收費的模型供應商未必開心。

硬體也在走同一條路。Google 與 AMD 合作的 TPU 8tx，主打機密訓練與推論，讓資料和模型權重在運算中仍受到硬體隔離；它也能把訓練與推論放在更接近的位置，方便企業用自有資料即時蒸餾小模型。TPU 8i Max 則把兩顆偏重推論的 TPU 8i 整合進單一封裝，記憶體容量、運算量與頻寬都加倍。

這不是單純比誰的晶片跑分快，而是把硬體依任務切開：訓練用一種、低延遲推論用一種、機密資料用一種、大記憶體工作再用另一種。

Google 不是唯一這麼做的公司。Amazon 有 Trainium 與 Inferentia，Microsoft 發展自家 AI 加速器，OpenAI 與 Broadcom 合作客製晶片，Anthropic 也在建立晶片設計團隊。Nvidia 的 CUDA 生態與通用性依然占優勢，但雲端業者根本不需要在每一種工作上擊敗 Nvidia。只要在每天重複十億次的固定任務上便宜 20%，自研晶片就有存在價值。

記憶體則是另一筆常被忽略的 AI 稅。AMD 的 MEXT 會把冷資料頁面從 DRAM 搬到較便宜的 flash，再用預測模型提前把即將使用的頁面叫回來。AMD 表示，Synopsys PrimeTime 在只保留一半實體 DRAM 的情況下，仍能維持完整配置 95% 的效能；依工作類型不同，DRAM 用量可減少 20% 到 75%。

目前 AMD 已在 145 台內部伺服器部署 MEXT，目標是在 2027 年擴大到 2,000 台，HPE 也準備透過「MEXT Ready」EPYC 伺服器推向客戶。這些數字來自 AMD 自己，適用範圍仍窄，但方向非常明確：省下一條 DRAM 或 HBM，可能比多買一些算力更有價值。

台灣供應鏈尤其不能把「效率提升」直接解讀成「晶片需求下降」。如果一次判斷的成本降低 98%，企業不會只做原本那批判斷；它會在更多流程插入模型，讓代理人彼此檢查，甚至對同一筆交易連續跑五種風險評估。單台伺服器需要的記憶體可能下降，部署的推論節點卻會快速增加。這和頻寬、儲存空間及雲端主機過去的發展一樣：單位價格下降，總用量反而上升。

這也是很少人談的另一面：效率競賽會讓客戶更難換供應商。

單純呼叫一個模型 API，很容易搬家；但如果整套系統已經綁定 Google TPU、Gemini 分流、Antigravity 代理人、機密運算和內部監控，要改用別家就得重做整條生產線。AWS 也一樣：當 SQS、Lambda、SageMaker、Strands、Inferentia 和 CloudWatch 全部串在一起，便宜的不只是模型，而是一個很難拆開的垂直系統。低價負責拉客，整合程度才是真正的護城河。

當然，這波效率敘事也有明顯的空頭理由。Carbon 現在是促銷價，基準測試由 Google 挑選；Amazon 的案例只有 20 個已知分類，一旦分類規則變動或遇到全新資安事件，小模型可能自信滿滿地選錯；MEXT 的 95% 效能來自適合的內部工作，不等於語音或即時服務也能接受；640 毫秒拿來處理後台工單很合理，拿來做輸入法補字就慢得令人抓狂。

所以接下來的競爭，不會是誰擁有一顆無所不能的大腦，而是誰能把每個請求送到「剛好夠用」的模型、晶片與記憶體層級。訓練是一張驚人的一次性帳單，推論則是每天重複出現的營業成本。當 AI 從展示功能變成每天數百萬次的工作流程，後者才會決定誰能活著收錢。

## 值得關注

- 2027 年底前，成熟 AI 服務會開始公布「每個成功工作流程成本」、P95 延遲、重試率與人工接手率。只報 token 單價，會像汽車廣告只報引擎排氣量一樣過時。
- 大型企業的高頻 AI 系統中，最昂貴的 frontier 模型最終只會處理不到 10% 的請求；其餘工作將由分類器、決策模型、蒸餾模型與規則系統接手。
- Carbon 在 11 月底漲價後的實際 token 用量值得盯緊。若一次任務消耗的 token 抵銷牌價優勢，Google 宣稱的兩倍成本差距會很快破功。
- AMD 的 2,000 台 MEXT 部署是關鍵驗收。若至少三種正式工作能在 DRAM 減半後，把效能損失壓在 5% 以內，預測式記憶體分層將從特殊方案變成伺服器標配。
- 對台灣 ODM、散熱、封裝與網通供應鏈來說，下一波訂單不會只集中在最大顆 GPU，而會分散到推論加速器、記憶體分層設備、NIC 與大量中型節點。AI 機房將更像一支分工明確的球隊，而不是十一個位置全塞同一位巨星。