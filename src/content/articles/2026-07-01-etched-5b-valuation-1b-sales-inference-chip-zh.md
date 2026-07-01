---
title: "專為 Transformer 打造的 AI 晶片新創 Etched 估值達 50 億美元、訂單破 10 億"
summary: "由哈佛輟學生創立的 AI 晶片新創 Etched，旗下專為 Transformer 架構設計的推論晶片已取得超過 10 億美元客戶合約，最新估值達 50 億美元，累計融資 8 億美元。公司正與早期客戶展開測試，矛頭直指輝達在 AI 推論市場的壟斷地位。"
category: "hardware"
publishedAt: 2026-07-01
lang: "zh"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/30/nvidia-competitor-etched-hits-5b-valuation-1b-in-sales-for-ai-chip/"
  - name: "Yahoo Finance"
    url: "https://finance.yahoo.com/technology/ai/articles/etched-emerges-stealth-working-chip-150000905.html"
  - name: "DataCenterDynamics"
    url: "https://www.datacenterdynamics.com/en/news/etchedai-raises-500m-for-a-5bn-valuation-report/"
tags:
  - "硬體"
  - "ai晶片"
  - "推論"
  - "輝達"
  - "新創"
  - "半導體"
relatedSlugs:
  - "2026-07-01-etched-5b-valuation-1b-sales-inference-chip-en"
  - "2026-06-29-openai-jalapeno-broadcom-inference-chip-zh"
  - "2026-06-30-amazon-custom-silicon-20b-run-rate-zh"
---

AI 晶片新創 Etched 專門打造只為 Transformer 架構服務的晶片，如今客戶簽約金額已突破 10 億美元、最新估值達 50 億美元（投後）——讓這家公司成為競爭激烈的 AI 推論硬體市場中，挑戰輝達最引人注目的押注之一。

Etched 同時宣布晶片實物已完成製造、客戶訂單同步開放，這樣的組合讓它有別於那些只交出規格書、從未搬出真實矽晶片的 AI 晶片新創墓地。公司迄今已在多輪融資中籌得 8 億美元，其中包括去年 12 月由 Stripes 領投的 5 億美元新輪——如今正將投資人的信任轉化為真實客戶的採購承諾。

## 一顆只跑 Transformer 的晶片，賭的是架構霸主地位

Etched 的核心策略在半導體業界堪稱激進：他們沒有選擇打造通用 GPU 或可程式化加速器，而是將 Transformer 架構直接固化進硬體電路。這顆名為 Sohu 的晶片無法執行任意運算，只能跑 Transformer——但跑起來極快，推論成本與功耗都遠低於競爭方案。

這個賭局的前提是：Transformer 架構已經贏了。主流前沿模型——GPT、Gemini、Claude、Llama——全都跑在 Transformer 上。若這種架構主導地位持續下去，專為 Transformer 打造的晶片就不是限制，而是優勢。Etched 聲稱其在等效工作負載下的每瓦吞吐量與每次推論成本上，都優於輝達 H200 叢集，但大規模的獨立驗證尚未完成。

公司出售的是「前沿推論叢集」——將 Sohu 晶片、客製化機架與專有軟體打包的完整整合系統，而非裸矽晶片。這種全棧策略與輝達的成功路徑如出一轍：硬軟體協同設計製造高轉換成本，讓先發優勢難以撼動。

## 創辦人、投資人，以及和史丹佛的類比

Etched 於 2022 年由 Gavin Uberti（執行長）和 Robert Wachen（總裁）共同創立，兩人都是哈佛大學的 Thiel Fellow，為了這家公司雙雙輟學。這個創業故事幾乎就是矽谷原型的翻版——年輕、頂尖學府出身的創辦人，在對的歷史時機離開象牙塔，去解決一個具體的技術問題。

投資人名單具有強烈的信號意義。天使投資人包括 AI 界重量級人物 Andrej Karpathy、Geoffrey Hinton 和李飛飛，以及億萬富翁 Stanley Druckenmiller 與 Peter Thiel。Hinton 的參與尤為矚目——這位獲得 2024 年諾貝爾物理學獎的神經網路奠基人背書，意味著對 Transformer 架構押注的深刻技術信心。

去年 12 月由 Stripes 領投的 5 億美元融資，讓 Etched 的估值與 AI 推論晶片生態中的 Groq（已完成 6.5 億美元融資）和 Cerebras（近期已 IPO）比肩。差異在於 Etched 比兩者走得更極端——後兩者為了擴大可尋址市場仍保留一定程度的可程式化彈性，而 Etched 則全押 Transformer 專用路線。

## 推論瓶頸是真實存在的結構性問題

Etched 的時機點契合了 AI 算力市場真實的結構轉變。訓練曾是 GPU 使用的主要場景，但如今推論——也就是實際執行模型來回答使用者查詢、驅動 AI Agent 或處理企業資料——在 AI 基礎設施開支中的占比正快速超越訓練。高盛分析師估計，到 2027 年推論將佔 AI 基礎設施支出的 60% 以上。

輝達的 GPU 極為靈活，其 CUDA 軟體生態更有長達 18 年的先發優勢。但這種靈活性有其代價：在 H100 或 H200 上執行 Transformer 推論，動用的是為更廣泛運算設計的電路，大量電路在典型推論工作負載下處於閒置狀態。

Etched 的論點是：一顆為這項單一任務打造的 ASIC（特定應用積體電路），能以更低的能耗和矽面積達到相同的輸出，大規模推論叢集的整體擁有成本大幅降低。10 億美元的簽約金額顯示，至少有一批重要客戶對這個論點信服到願意付真金白銀。

## 競爭版圖

Etched 所處的市場已迅速變得擁擠。Cerebras 以其晶圓級晶片於 2025 年上市，同時布局訓練與推論市場。Groq 以其語言處理單元（LPU）主打快速推論，已進入商業部署。兩者都保留了一定可程式化彈性，瞄準比 Etched 更廣泛的市場。

大型雲端服務商也在大規模打造自有矽晶片：亞馬遜的 Trainium 與 Inferentia 系列剛突破年化營收 200 億美元；Google 的 TPU 支撐其自有模型服務；OpenAI 與 Broadcom 合作的 Jalapeño 晶片正式入局；微軟的 Maia 加速器也已進入量產；輝達自身也推出了推論優化的 NVL 系列來回應市場。

在這個背景下，Etched 的差異化不只是技術層面，更是策略層面：它把自己定位為 AI 實驗室與企業的推論硬體夥伴，專注於 Transformer 推論的最高效率，而非成為通用算力供應商。

## 10 億訂單的真實意涵

簽約合同不等於已交付的營收。從承諾到系統出貨的這段路，正是 AI 硬體新創最常摔跤的地方——晶片設計定案成本高、良率難以預測、交期容易延誤。Etched 也坦承，其晶片目前還在早期客戶測試階段，尚未進入量產。

但在正式上市前就拿到 10 億美元訂單，是個不尋常的位置。這意味著一批主要機構——Etched 尚未公開名稱——已對早期矽晶片的表現足夠信服，願意為採購先行付款。對一家 2022 年成立、此前從未公開亮相的公司而言，這樣的商業牽引力著實罕見。

下一個關鍵里程碑：Etched 能否如期將這些承諾轉化為實際出貨，以及生產規模下的效能宣稱是否成立。若成功，50 億美元估值或許只是起點；若失敗，即便 Transformer 押注在智識上完全正確，也難逃 AI 硬體新創屢見不鮮的執行力陷阱。

無論如何，Etched 已清楚示範：專用 AI 推論矽晶片市場是真實的、競爭激烈的、且正在快速擴張。懸念只剩一個：誰能最終收割它？
