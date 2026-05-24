---
title: "Anthropic 以逾 3 億美元收購 Stainless，切斷 OpenAI 與 Google 共用的 SDK 核心工具"
summary: "Anthropic 宣布收購紐約新創公司 Stainless，這家公司的 SDK 自動生成平台廣泛被 OpenAI、Google 與 Cloudflare 等競爭對手使用。這筆逾 3 億美元的交易背後，Anthropic 計畫關閉 Stainless 的所有託管服務，讓競爭者不得不重建或遷移其開發者基礎設施中的關鍵一環。"
category: "developer-tools"
publishedAt: 2026-05-24
lang: "zh"
featured: false
trending: false
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/18/anthropic-has-acquired-the-dev-tools-startup-used-by-openai-google-and-cloudflare/"
  - name: "Anthropic 官方部落格"
    url: "https://www.anthropic.com/news/anthropic-acquires-stainless"
  - name: "The AI Insider"
    url: "https://theaiinsider.tech/2026/05/19/anthropic-acquires-sdk-startup-stainless-for-over-300m-cutting-off-key-tool-used-by-openai-and-google/"
tags:
  - "Anthropic"
  - "Stainless"
  - "開發者工具"
  - "SDK"
  - "收購"
  - "OpenAI"
  - "Google"
relatedSlugs:
  - "2026-05-23-karpathy-anthropic-pretraining-claude-zh"
  - "2026-05-23-anthropic-milan-emea-expansion-9x-revenue-zh"
  - "2026-05-22-anthropic-first-profit-q2-revenue-109b-zh"
---

Anthropic 於 5 月 18 日宣布收購紐約新創公司 Stainless——一家專門自動化生成和維護 API 軟體開發套件（SDK）的公司。據《The Information》報導，這筆交易金額逾 3 億美元。然而，讓這起收購引發廣泛關注的，不只是價格，而是一個更微妙的事實：Stainless 長期以來是 AI 產業的共用基礎設施，其最大客戶包括 OpenAI、Google、Cloudflare 和 Merge——換言之，Anthropic 剛剛買下了讓競爭對手開發者生態系得以運作的關鍵管道。

這個事實的競爭意涵，正在整個開發者工具社群中發酵。

## Stainless 究竟做什麼

Stainless 由前 Stripe 工程師 Alex Rattray 於 2022 年在紐約創辦，解決的是一個既枯燥又至關重要的問題：讓 SDK 函式庫隨時跟上快速演進的 API。

當一家 AI 公司推出新模型、端點或參數時，開發者用來呼叫該 API 的每一個 SDK——Python、TypeScript、Go、Kotlin、Java——都必須同步更新。手動維護這些 SDK 既費時又容易出錯。Rattray 的核心洞見是：以 API 規格作為唯一的事實來源，其餘一切交給自動化。Stainless 接受 OpenAPI 規格後，可自動生成跨語言的生產級 SDK，並在規格更新時持續同步再生成。

這個平台大幅降低了任何擁有公開 API 的公司的維護負擔。對於每幾週就推出新模型版本的 AI 公司來說，這個功能尤其珍貴。OpenAI 的 Python 與 TypeScript 客戶端函式庫——AI 生態系中下載量最高的函式庫之——就是透過 Stainless 建立並維護的；Google 的 AI SDK 基礎設施和 Cloudflare 的開發者產品同樣依賴這個平台。

## 競爭上的連帶效應

Anthropic 的聲明相當直接：公司計畫關閉 Stainless 所有託管產品，包括 SDK 生成器。現有客戶仍保有對其已生成 SDK 的完整所有權與修改權，但自動維護這些 SDK 的管道將就此終止。

對 OpenAI 和 Google 而言，這帶來一個真實但尚可處理的運營挑戰：兩家公司必須選擇自建 SDK 生成基礎設施、尋找新的服務商，或是將手動維護工作移至內部承擔。以這些公司的工程資源來說，以上選項都不是致命打擊，但都需要時間和金錢，而這些資源原本可以投入產品開發。

對整個生態系更具意義的衝擊，在於那些中小型 AI 新創公司。這些公司選擇 Stainless，正是因為沒有資源自建工具。在開發者體驗往往決定 API 採用率的市場中，在關鍵成長階段失去可靠的 SDK 維護平台，是切實的挫折。

## Anthropic 為何願意花逾 3 億買一個 B2B 工具新創

初看之下，逾 3 億美元收購一家開發者生產力工具公司確實昂貴。Stainless 並不是一個驚人的營收機器。但 Anthropic 顯然在買的，是技術以外的戰略優勢。

最直接的理由是防禦性整合。隨著 Anthropic 的 API 業務快速擴張——公司剛剛完成史上首個盈利季度，Q2 營收達 109 億美元——Claude API 周邊的開發者工具品質，已成為具體的競爭因素。將 Stainless 收入麾下，讓 Anthropic 能將這個平台的全部能力導向自家 SDK 生態系：更快的更新、更完整的語言支援、與 Claude 功能集更緊密的整合。

人才面向同樣不可忽視。Rattray 與 Stainless 團隊建造了業界最成熟的 API SDK 生成平台，這樣的技術積累本身就是資產，獨立於產品之外。

第三個理由——也是讓競爭對手最不安的——是競爭干擾。無論 Anthropic 是否以此為主要意圖，收購並關閉一個 OpenAI 和 Google 仰賴的平台，就是對其開發者生態系的一次真實打擊。在開發者心智份額隨時間複利累積的市場中，讓競爭對手的 SDK 工作流程多出每一個摩擦點，都是 Anthropic 的微小優勢。

## 開發者生態系作為護城河

這起收購反映了 AI 產業當前階段更廣泛的規律：前沿模型的性能正以足夠快的速度收斂，輔助性的開發者體驗因此成為主要競爭場域。當 GPT-5、Gemini 3.5 Flash 和 Claude 4 都能處理相同的企業任務時，決定開發者選擇哪個 API 的，越來越是文件品質、SDK 可靠性、技術支援響應速度和生態系深度。

Anthropic 在這個維度上的投資已持續約 18 個月：推出大幅改版的開發者平台、發布 Model Context Protocol（MCP）並催生了大量第三方整合生態，以及近期延攬 Andrej Karpathy 擔任研究顧問。Stainless 的收購符合這個脈絡：有系統地強化開發者體驗堆疊的每一個層次。

這起消息傳出之際，Anthropic 據報正在接近一輪可能讓公司估值達 9000 億美元的新融資——若成真，將使其成為史上估值最高的非上市公司。以這樣的規模，Anthropic 有能力花 3 億美元掌控競爭對手無法輕易取代的基礎設施。

## 接下來會怎樣

據熟悉交易條款的消息人士透露，非 Anthropic 的 Stainless 客戶有 90 天時間為服務終止做準備。大多數客戶預計將遷移至內部解決方案或其他新興替代服務——業界已有多家廠商表示有意填補這個空缺。

對更廣泛的開發者生態系而言，這個事件是一個警示：競爭激烈的市場中，共用基礎設施背負著隱性風險。一個因多家競爭公司同時使用而顯得「中立」的工具，一旦被其中某家收購，就可能立刻成為武器。

Rattray 與 Stainless 核心團隊將加入 Anthropic 的開發者體驗部門。SDK 生成器技術在去除託管服務後，將被改造為 Anthropic 維護自家客戶端函式庫的內部工具，暫無重新對外開放的計畫。

Stainless 作為 AI 基礎設施公共財的一頁，就此翻過。下一章，由 Anthropic 執筆。
