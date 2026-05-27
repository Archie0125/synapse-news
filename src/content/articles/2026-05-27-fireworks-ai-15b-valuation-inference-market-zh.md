---
title: "Fireworks AI 洽談 150 億美元估值新融資，AI 推論服務市場競爭白熱化"
summary: "專門為企業提供大型語言模型推論服務的新創公司 Fireworks AI，正在以約 150 億美元估值洽談新一輪融資，不到八個月估值翻近四倍。截至 2026 年 2 月，公司年化營收已達 3.15 億美元，本輪由 Index Ventures 共同領投，將成為今年 AI 基礎設施領域規模最大的融資案之一。"
category: "startups"
publishedAt: 2026-05-27
lang: "zh"
featured: true
trending: true
sources:
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-05-27/fireworks-ai-in-talks-for-funding-at-15-billion-valuation"
  - name: "CryptoBriefing"
    url: "https://cryptobriefing.com/fireworks-ai-funding-15-billion-valuation/"
  - name: "Fireworks AI Blog"
    url: "https://fireworks.ai/blog/series-c"
tags:
  - "AI 推論"
  - "新創公司"
  - "融資"
  - "Fireworks AI"
  - "Index Ventures"
relatedSlugs:
  - "2026-05-05-cerebras-ipo-40b-nasdaq-zh"
  - "2026-05-23-modal-labs-355m-series-c-ai-compute-zh"
  - "2026-05-03-ai-api-pricing-war-token-collapse-zh"
---

在 AI 基礎設施投資依然火熱的市場中，專門為企業客戶提供高速、低成本開源模型推論服務的新創公司 Fireworks AI，正在洽談以約 150 億美元估值完成新一輪融資。這項消息由 Bloomberg 在週二率先披露，知情人士透露，先前已投資 Fireworks 的 Index Ventures 將共同領投本輪。

這個數字之所以引人矚目，不只是因為金額龐大，更因為它的速度之快令人咋舌。不到八個月前，Fireworks 在 2025 年 10 月剛以 40 億美元估值完成了 2.5 億美元的 C 輪融資。若本輪以接近傳聞的估值成交，公司估值將在短短一年內翻近四倍——成為本輪 AI 融資週期中估值躍升最為凌厲的案例之一。

Fireworks 與 Index Ventures 的發言人均婉拒置評，條件仍有可能變動。

## 推論即服務：一個被忽視的關鍵市場

Fireworks AI 佔據的，是 AI 經濟中一個特定卻愈發重要的利基位置：推論即服務（inference-as-a-service）。當外界目光總是聚焦在 GPT-5、Gemini 3、Claude 4 等前沿模型的訓練突破時，真正讓這些模型以生產規模服務終端用戶和應用程式的「最後一哩路」工程，既艱深又有利可圖。

所謂推論，就是讓已訓練完畢的模型對外部請求產生回應——補全文字、生成嵌入向量、執行函數呼叫。對於打造 AI 原生產品的公司來說，推論成本的高低攸關生死：規模一大，推論費用往往吃掉 30% 到 60% 的營收；延遲高低更直接決定產品體驗，而非只是工程問題。

Fireworks 在 AWS Bedrock、Google Vertex AI 等雲端巨頭與 Groq、Cerebras 等客製矽片新創之間找到了自己的定位。公司的核心優勢是速度與彈性：在商用 GPU 叢集上運行深度優化的服務基礎設施，以 token 計費，支援種類繁多的開源模型——Llama 4、Qwen 3、Mistral 等數十款——讓客戶不用被綁死在單一供應商。

公司自研的 FireAttention 推論引擎，據稱在每 GPU 每秒請求量（RPS/GPU）的第三方評測中屢居前列，吞吐量比標準實作高出 2 至 4 倍。

## 支撐高估值的真實業績

150 億美元的估值並非空中樓閣，背後有真實的業績做支撐。Fireworks 在 2026 年 2 月的年化重複性營收（ARR）達到 3.15 億美元，較前一年同期成長 416%，高於 C 輪融資時公告的 2.8 億美元。公司客戶數量從 B 輪時的約 1,000 家，擴張至 2025 年底的逾萬家。

客戶名單涵蓋當前成長最快的一批 AI 原生公司：Cursor、Perplexity、Notion、Sourcegraph、Uber、DoorDash、Shopify、Upwork。這些不是試玩性質的帳號，而是每天可能需要處理數百萬次 API 請求、對延遲和成本都極為敏感的生產級部署。

以 3.15 億美元 ARR 計算，150 億美元估值對應約 47 倍的本益比——以傳統軟體標準來看偏高，但在本輪 AI 基礎設施投資週期中並不罕見。今年 5 月剛在 Nasdaq 上市、估值逾 400 億美元的 Cerebras，以更薄的營收支撐著相近的倍數。

## 競爭激烈的推論服務市場

過去一年，推論基礎設施賽道迅速升溫。Groq 靠自研語言處理器（LPU）主打超低延遲，與多家超大規模雲端服務商簽署了多年期合約；已上市的 Cerebras 以晶圓級運算攻大型模型推論市場；SambaNova 以私有化部署瞄準企業客戶；Together AI 則提供類似定位的推論服務，估值超過 12 億美元。

最直接的競爭對標可能是 Baseten——這家公司在 2026 年 2 月以 50 億美元估值完成了 3 億美元的 E 輪融資，強調企業銷售與生產級容量承諾。

讓 Fireworks 有所區隔的，據熟悉該公司的投資人說，是模型支援的廣度、持續領先的推論引擎，以及不斷擴充的周邊產品線——包括微調基礎設施、專屬部署選項，以及多家頭部智慧代理（agentic）應用開發者已採用的函數呼叫 API。

## 基礎設施能否守住長期價值？

圍繞 Fireworks 的估值討論，其實折射出 AI 投資圈一個懸而未決的核心問題：基礎設施服務商能否長期積累可觀的護城河，還是終將在超大型雲端服務商的定價補貼下邊際壓縮？

悲觀論點在於：AWS、Google、Microsoft 都有自己的推論服務，擁有更強的企業銷售能力，且願意在推論費率上補貼以換取更大的雲端綁定。隨著 Llama 4 Maverick、Qwen 3-235B 等開源模型在 2026 年的能力逼近閉源前沿，企業更換服務商的轉換成本正在降低。

樂觀論點則是：在大規模情況下高速、高效地服務模型，是一項有深度護城河的工程能力，而超大型業者在開源模型的優化部署上行動遲緩。加上模型上下文長度持續擴張——從 128K、1M 到如今開始支援數百萬 token 的視窗——高效服務長上下文請求的能力，與標準吞吐量優化是截然不同的技術挑戰。

Fireworks 的成長曲線暗示，目前客戶正在以行動投票支持樂觀論點。

## 150 億融資的市場意義

若本輪交易以傳聞估值成交，Fireworks 將躋身 2026 年最大規模私人 AI 基礎設施融資之列，與 Anthropic 的 300 億美元超大輪、Runway 的 50 億美元融資、Modal Labs 的 3.55 億美元 C 輪，共同描繪出前沿 AI 應用底層基礎設施仍在持續吸引資本的圖景。

對整個 AI 推論服務市場而言，這筆融資所傳遞的訊號是：投資人相信，在雲端服務商的商品化完全壓縮利潤空間之前，專業推論平台仍有數年的機會視窗——而那些已建立可觀營收與客戶集中度的公司，值得以積極的估值支持。

Fireworks 的賭注，是要在推論服務層做到 Snowflake 當年在雲端資料倉儲做到的事。150 億美元的籌碼是否下得恰當，等本輪融資正式落地後才能見真章。
