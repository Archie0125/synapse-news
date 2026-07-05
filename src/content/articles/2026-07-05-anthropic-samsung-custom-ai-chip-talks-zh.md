---
title: "Anthropic 洽談與三星合作打造首款自製 AI 晶片"
summary: "Anthropic 已與三星電子展開初步討論，探索合作製造自訂 AI 加速器的可能性，成為最新一家尋求擺脫對輝達依賴的前沿 AI 實驗室。此舉發生在 OpenAI 與博通合作推出 Jalapeño 晶片之後，標誌著整個產業正朝向客製化矽晶片轉型，以應對大規模推論的經濟壓力。"
category: "hardware"
publishedAt: 2026-07-05
lang: "zh"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/"
  - name: "The Information"
    url: "https://www.theinformation.com/articles/anthropic-talks-samsung-manufacture-custom-ai-chip"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-07-02/anthropic-in-talks-with-samsung-for-custom-ai-chip-information-mr3l34t4"
tags:
  - "Anthropic"
  - "三星"
  - "客製化 AI 晶片"
  - "硬體"
  - "ASIC"
  - "輝達"
  - "AI 基礎設施"
  - "推論晶片"
relatedSlugs:
  - "2026-06-29-openai-jalapeno-broadcom-inference-chip-zh"
  - "2026-07-04-qualcomm-tenstorrent-acquisition-talks-zh"
  - "2026-07-01-etched-5b-valuation-1b-sales-inference-chip-zh"
---

Anthropic 已與三星電子展開初步洽談，探索合作開發客製化 AI 晶片的可能性。此消息首先由《The Information》披露，隨後多家媒體跟進確認，使 Anthropic 成為最新，也可能是最令人意外的，開始追求自有矽晶片策略的前沿 AI 實驗室。畢竟這家公司早期以模型研究著稱，而非硬體野心。

目前談判仍處於早期階段。Anthropic 尚未確定這顆晶片的用途、效能規格，或它將如何整合進伺服器基礎架構。可以確定的是，公司正在評估三星的 2 奈米製程及其先進封裝設施，並已於 2026 年 6 月初從 OpenAI 晶片團隊挖角 Clive Chan，主導這個剛起步的硬體部門。

## 為何選擇三星？

選擇三星作為製造夥伴並非偶然。2026 年 5 月，三星以戰略基礎設施夥伴身份參與了 Anthropic 規模達 650 億美元的 H 輪融資——當時分析師普遍認為這是一個供應鏈深度整合的籌碼，而非單純的財務投資。如果 Anthropic 首款客製化晶片的製造合作確定由三星承接，將是這場戰略投資的合理下游結果，在 AI 實驗室與頂尖半導體製造商之間建立更緊密的一體化關係。

三星在這個領域擁有幾項關鍵優勢。其 2 奈米製程是目前量產中最先進的節點之一，僅次於台積電；其先進封裝技術——對於大型語言模型推論所需的高頻寬記憶體配置至關重要——也達到業界領先水準。三星同時與輝達（生產現行 GPU 系列元件）和 Google（合作開發客製化晶片）保持既有合作，對 AI 矽晶片的工作負載特性已有深厚的實作經驗。

## 推論經濟學的根本問題

要理解 Anthropic 為何如今走到這一步，必須先理解大規模運行前沿 AI 模型的經濟邏輯。

Anthropic 每天在 Claude 的消費端、開發者端和企業端處理龐大數量的推論請求。每一個請求都需要硬體支撐——絕大多數是輝達 GPU，加上透過雲端合作夥伴使用的 Google TPU 和亞馬遜晶片。輝達的硬體在通用 AI 工作負載上表現出色，但「通用」本身就帶有額外成本。一顆設計用來支援遊戲、科學運算與 AI 推論的 GPU，對任何單一任務而言都不是最佳選擇。

客製化推論晶片能消除這種冗餘。它可以精確針對特定模型架構的記憶體存取模式、浮點精度需求和批次處理特性進行調優。OpenAI 與博通合作、於 2026 年 6 月底宣布的 Jalapeño 晶片，早期測試中據報相較標準 GPU 推論可節省約 50% 成本。對一家每天處理數十億個 token 的公司而言，這樣的效率提升不只是邊際改善——而是單位經濟學的根本改變。

Anthropic 的動機很可能相同。公司一直公開表示其計算策略是刻意多元化的——Google、亞馬遜和輝達都扮演重要角色——但多元化與最佳化是兩回事。一顆針對 Claude 架構調優的客製化晶片，能夠大幅降低 Anthropic 每個 token 的交付成本，在公司朝向潛在 IPO 的關鍵時期改善獲利結構。

## 正在形成的產業模式

這個發展的意義，不只在於 Anthropic 的個別處境，更在於它所代表的產業趨勢。在大約 18 個月的時間裡，每一家主要的前沿 AI 實驗室，要麼已開發客製化矽晶片，要麼宣布了計劃，要麼與有能力建造的晶片製造商建立了合作。

OpenAI 與博通宣布 Jalapeño 晶片。Google 長期運營自有 TPU 系列，目前已進入第七代。亞馬遜的 Trainium 和 Inferentia 晶片已從內部工具成長為重要的外部產品，公司最近披露年收入已達 200 億美元規模。Meta 多年來一直為推薦系統設計客製化 AI 晶片，現在正將這一能力延伸至語言模型訓練。微軟透過 Azure 內部矽晶片團隊的 Maia 推論晶片已在生產環境中測試。

Anthropic 的行動若最終產出一顆量產晶片，將完成這個行業版圖的最後拼圖。唯一一家公開堅持「硬體不可知論」、只使用 GPU 的主要 AI 實驗室，現在也開始洽談打造自己的矽晶片。

## 改變的與不改變的

這個消息不應被解讀為 Anthropic 準備放棄現有的雲端合作關係。公司一再強調與 Google、亞馬遜和輝達的長期戰略合作關係。一顆仍在設計討論階段的客製化晶片，不會取代這些合作——而是補充它們，在特定推論工作負載中，客製化加速器能提供有意義的效率優勢。

任何晶片走向量產的時間線都以「年」計，而非「月」。從初步設計討論到流片、首批矽晶片、認證和量產，這一層級的客製化晶片開發，在最理想的條件下通常需要兩到三年。Anthropic 並不會在明天取得硬體優勢。但它正在啟動一項戰略能力的倒數計時——若成功，將在 AI 市場預期進入激烈利潤壓縮期之前，賦予公司有意義的成本槓桿。

對 Anthropic 而言，正如對每家追求客製矽晶片的 AI 實驗室一樣，真正的問題是：打造和驗證一顆全新晶片所需的數年工程投資與資本支出，是否能在競爭格局再次轉變之前回收？歷史告訴我們，對規模足夠大的公司而言，答案通常是肯定的。Anthropic 現在夠大了，有資格提出這個問題。

---

*Anthropic 與三星之間的洽談，由《The Information》於 2026 年 7 月 2 日率先報導。*
