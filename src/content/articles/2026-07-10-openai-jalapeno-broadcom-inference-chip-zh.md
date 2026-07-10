---
title: "OpenAI 發表 Jalapeño：與 Broadcom 合作、九個月內打造的首款自研推論晶片"
summary: "OpenAI 與 Broadcom 聯合揭示 Jalapeño 推論處理器，宣稱成本比 GPU 方案低約五成。從設計到流片不到九個月，這款晶片標誌著全球最有價值 AI 公司正式展開垂直整合攻勢。"
category: "hardware"
publishedAt: 2026-07-10
lang: "zh"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/"
  - name: "OpenAI"
    url: "https://openai.com/index/openai-broadcom-jalapeno-inference-chip/"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-06-24/openai-and-broadcom-unveil-ai-chip-to-run-models-faster-cheaper"
tags:
  - "OpenAI"
  - "Broadcom"
  - "Jalapeño"
  - "AI晶片"
  - "推論"
  - "硬體"
  - "半導體"
relatedSlugs:
  - "2026-07-09-apple-broadcom-30b-us-chip-deal-zh"
  - "2026-07-08-nvidia-sk-hynix-hbm4-vera-rubin-partnership-zh"
  - "2026-07-04-qualcomm-tenstorrent-acquisition-talks-zh"
---

多年來，OpenAI 一直是 GPU 產業最重要的客戶——一家大量採購 Nvidia 晶片、再以高昂成本將其轉化為 ChatGPT 智能的企業。6 月 24 日，OpenAI 開始改寫這段關係。該公司與 Broadcom 聯合發表了首款自研 AI 推論晶片 Jalapeño，並稱其為「多世代計算平台」的第一步——一個 OpenAI 打算自己掌控、而非向外租借的基礎設施。

這項公告不只是技術里程碑，更是整個 AI 基礎設施生態的戰略轉捩點。

## Jalapeño 是什麼？

Jalapeño 是一款推論處理器，專為模型訓練完成後、實際回應用戶查詢的計算階段而設計。這個區分至關重要。訓練大型語言模型需要 Nvidia H100 或 GB300 GPU 那種通用、大規模並行的浮點運算能力；而推論則是另一回事：它要求低延遲、高記憶體頻寬、以及每日承接數十億次請求的成本效益。

Nvidia 的硬體是為各種 AI 工作負載改良的通用加速器，Jalapeño 則從零開始設計，只有一個目標：以最高效率運行 OpenAI 的大型語言模型推論工作負載。OpenAI 總裁 Greg Brockman 在發表會上說：「我們對這個工作負載有深刻的理解，我們想打造能夠加速可能性邊界的東西。」

早期測試印證了這個說法。Jalapeño 的工程樣品已在實驗室以量產目標頻率和功耗運行 ML 工作負載，包含 GPT-5.3-Codex-Spark。OpenAI 表示，每瓦性能「大幅優於目前最先進的替代方案」，並有分析指出與標準 GPU 部署相比，成本節省約達五成。

## 破紀錄的開發速度

Jalapeño 最令人矚目之處，或許不在晶片本身，而在於它的誕生速度。OpenAI 與 Broadcom 的合作關係在 2025 年 10 月才正式宣布，從初始設計概念到流片（tape-out，即晶片設計提交量產的關鍵節點）僅花了不到九個月。對於高性能先進半導體而言，這可能是業界有史以來最快的 ASIC 開發週期。

這種速度來自深度的共同開發模式。Broadcom 是全球最大的 ASIC 製造商，長期為 Google、Meta 等超大規模雲端業者打造客製晶片，帶來了豐富的矽晶片實作經驗。OpenAI 則貢獻了模型實際生產運行的深度知識——注意力頭如何存取記憶體、KV 快取的存取模式在高負載下如何變化、混合專家架構中的路由決策如何流動。更值得一提的是，OpenAI 還用自家 AI 模型加速了晶片設計與最佳化的部分工作——這是半導體工程中真正前所未有的新型回饋迴路。

## 自研晶片的商業邏輯

進軍客製晶片的動機並不難理解。OpenAI 的算力成本高得驚人，且還在持續攀升。在數十萬張 GPU 上運行 ChatGPT、Codex API 及各企業產品，每年耗費數十億美元。而推論——即時回應用戶請求——在這個成本結構中佔主導地位。每提升一個百分點的效率，就直接轉化為利潤。

自己掌控推論晶片，讓 OpenAI 獲得了前所未有的議價籌碼。當 Nvidia 調漲價格或將供貨優先給其他客戶時，過度依賴單一供應商就是風險所在。客製晶片消除了這個單點失效，並讓公司能針對自家模型架構精確最佳化硬體——這是通用加速器做不到的事。

這個劇本有跡可循。Google 從 2015 年開始打造 TPU，並將其視為在 Search 和 Google Cloud AI 工作負載上的成本優勢來源。Amazon 的 Trainium 晶片為自家模型訓練提供動力，也成為 AWS 體系內 Nvidia 的重要替代選項。Apple 則在 2026 年與 Broadcom 簽署了高達三百億美元的客製組件協議，在消費裝置層採用相同邏輯。

## 垂直整合大戰略的一部分

OpenAI 將 Jalapeño 定位為「多世代計算平台」的第一步，初次量產部署預計在 2026 年底前展開，後續還會有多代架構。公司尚未透露計劃產量，但 Broadcom 作為製造關係的主要負責方，暗示著相當大的規模。

這個晶片策略契合 OpenAI 過去一年積極布局的更大藍圖：傳言中由前蘋果設計師 Jony Ive 主導的 AI 設備計畫、與軟銀和 Oracle 合作的 Stargate 資料中心建設，以及據傳提出的讓美國政府持有 5% 股權方案。掌控推論晶片，為一家越來越像垂直整合平台、而非軟體新創的公司補上了最後一塊拼圖。

值得注意的是，預訓練階段——創造新基礎模型的過程——在可預見的未來仍將仰賴 Nvidia 硬體。這個階段所需的算力規模巨大且多樣，客製 ASIC 暫時還無法比擬 Nvidia H100 叢集的靈活性。但推論恰恰是客製晶片的強項：工作負載可預測、量大、特性明確，且高度回報專業化設計。

## 對 Nvidia 的意涵

這項公告是一個向業界發出的信號，即便短期內不會動搖 Nvidia 的財務表現。OpenAI 是 Nvidia 最知名的 AI 客戶，也是其最具影響力的品牌背書者。當 OpenAI 宣布設計自家推論晶片，全球每一家主要 AI 開發商都接收到了一個清晰的訊息：產業走向已經確定。

Nvidia 在訓練領域的主導地位依然穩固，GB300 Blackwell Ultra 架構仍是前沿模型開發的黃金標準。但隨著推論工作負載的成長速度超過訓練工作負載——ChatGPT 的用量大幅攀升，每次對話產生的推論 token 遠多於訓練 token——這家 GPU 霸主在推論市場的份額，可能隨著客製矽晶片的成熟而逐步流失。

對更廣大的半導體生態而言，Jalapeño 再次印證：AI 正驅動著智慧型手機時代以來最激烈的客製晶片開發浪潮。無論哪家 AI 公司最終勝出，Broadcom、台積電等晶圓代工與設計服務業者都是這波趨勢的結構性受益者。AI 推論最高效率堆疊的競賽，才剛剛開始。

---

*OpenAI 的 Jalapeño 晶片預計在 2026 年底前進入初步量產部署，並規劃後續多代平台架構。*
