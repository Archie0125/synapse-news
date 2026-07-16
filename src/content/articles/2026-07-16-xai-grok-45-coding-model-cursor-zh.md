---
title: "xAI 發布 Grok 4.5：與 Cursor 共同訓練的程式碼模型，劍指前沿市場定價"
summary: "xAI 於 7 月 8 日推出 Grok 4.5，這是其迄今速度最快、成本效益最高的模型，與程式碼編輯器 Cursor 聯合開發，搭載 50 萬 token 上下文視窗。每百萬輸入 token 僅需 2 美元，效能卻聲稱接近 Claude Opus 4.8。"
category: "developer-tools"
publishedAt: 2026-07-16
lang: "zh"
featured: false
trending: true
sources:
  - name: "xAI — 發布 Grok 4.5"
    url: "https://x.ai/news/grok-4-5"
  - name: "Axios — Grok 4.5 發布報導"
    url: "https://www.axios.com/2026/07/08/spacexai-grok-new-model"
  - name: "TechCrunch — Grok 4.5"
    url: "https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/"
  - name: "Fullstack — Grok 4.5 深度解析"
    url: "https://www.fullstack.com/labs/resources/blog/grok-4-5-a-closer-look-at-xais-latest-model"
  - name: "DataNorth — Grok 4.5 發布"
    url: "https://datanorth.ai/news/xai-releases-grok-4-5-coding-focused-model"
tags:
  - "xAI"
  - "Grok"
  - "程式碼 AI"
  - "Cursor"
  - "開發者工具"
  - "大型語言模型"
relatedSlugs:
  - "2026-07-16-openai-gpt56-sol-terra-luna-general-availability-zh"
  - "2026-07-15-gemini-35-pro-pricing-deepseek-competition-zh"
---

在 OpenAI 向全球開放 GPT-5.6 的前一天，xAI 搶先出手。7 月 8 日，伊隆·馬斯克掌控的 AI 公司發布了 Grok 4.5——一款以程式碼為核心、與 AI 原生程式碼編輯器 Cursor 聯合開發的模型。這次發布是 xAI 迄今最清晰的競爭宣示：它不只想在原始能力上較勁，更要在成本效益的曲線上贏得開發者與企業的採用。

## Grok 4.5 的核心規格

Grok 4.5 是文字與圖片輸入、文字輸出的模型，圍繞四個核心指標打造：

**上下文視窗：50 萬 token。**這是目前商業可用的最大上下文視窗之一，明顯超越 GPT-5.6 Sol，與 Gemini Omni Ultra 延伸上下文配置大致相當。對程式碼任務而言，50 萬 token 意味著 Grok 4.5 可以一次性讀入整個中型程式碼庫——包含測試套件、設定檔與建構腳本——無需仰賴分段處理與向量檢索的繁瑣流程。

**速度：每秒 80 個 token。**xAI 將此定義為「快速模型級別」的吞吐量。公司表示，這個速度得益於與 Cursor 工程團隊協作開發的自訂推理核心（inference kernel）。

**定價：每百萬 token 輸入 2 美元、輸出 6 美元。**這個定價讓 Grok 4.5 直接與 GPT-5.6 Terra 和 Gemini Omni Flash Pro 正面交鋒。伊隆·馬斯克形容這款模型「效能大致相當於 Opus 4.7，但速度更快、token 效率更高」——若此說法能通過獨立基準測試的驗證，那將是異常出色的性價比：以中階價位換來接近前沿等級的智慧。

**函式呼叫與結構化輸出。**Grok 4.5 全面支援現代代理框架所需的程式化介面：函式呼叫、結構化 JSON 輸出、網路搜尋、X（Twitter）搜尋以及程式碼執行。其中 X 搜尋整合是真正的差異化特性——開發者可以直接透過模型查詢 X 的即時公開資料流，無需另行整合獨立 API。

## Cursor 聯合訓練的深遠意義

Grok 4.5 的獨特之處，在於它是與 Cursor **共同訓練**而成，而非事後整合。Cursor 工程團隊深度參與了模型的訓練資料篩選與微調流程，重點聚焦在多檔案程式碼理解、差異（diff）生成以及內嵌編輯品質的提升。

這帶來實際可見的成果：Grok 4.5 在 Cursor 用戶最常處理的任務上表現亮眼——不僅是從規格書生成程式碼，更能處理重構現有程式碼、修復跨模組邊界的型別錯誤，以及推理一個 diff 對正在運行的系統會產生什麼實際影響。50 萬 token 的上下文在此尤為關鍵：Cursor 可以將整個功能分支的完整內容傳給模型，讓它從全局角度評估程式碼的正確性。

從第一天起，Grok 4.5 就作為 Cursor 所有訂閱方案（包含免費方案）的一流模型正式上線。這個分發渠道至關重要：Cursor 在過去 18 個月已成為職業開發者使用最廣泛的程式碼環境之一，免費方案的嵌入讓 xAI 無需另外贏得採購決策，便能直接觸及龐大的開發者群體。

## 基準測試定位

xAI 宣稱 Grok 4.5 在 Artificial Analysis Intelligence Index 上排名第四，超越所有現行開源模型以及整個 Gemini 家族。在備受開發者關注的 SWE-bench Verified 基準（衡量真實軟體工程能力的標準測試）方面，xAI 尚未公布官方分數，這將是下一個重要觀察指標。

## 上市限制與歐盟空缺

Grok 4.5 目前可在 Grok Build、Cursor 所有方案以及 xAI API 控制台使用，但**尚未在歐盟地區上線**，仍需完成《歐盟人工智慧法》的透明度與資料治理合規程序。xAI 表示預計 7 月中旬開放歐盟市場——這個時間窗口如今已到，意味著監管審查應已接近尾聲。

歐盟市場的缺席對 xAI 的企業客戶拓展形成持續阻力：歐洲企業佔全球 AI API 支出的相當比重，每晚一週開放，就多損失一週的市場份額給合規競爭對手。

## 搶先佈局的競爭邏輯

在 OpenAI GPT-5.6 全面開放的前一天發布，絕非巧合。xAI 試圖在 OpenAI 的新聞浪潮席捲之前，先建立自己的話語權。這個策略部分奏效——Grok 4.5 在開發者社群引發了一波討論，隨即被 GPT-5.6 的報導所淡化。但模型的長期價值，將取決於 Cursor 整合能否帶動持久的日活躍用戶成長。

對開發者而言，xAI 的市場地位頗具意思：Anthropic 深耕 Claude API 開發者生態；OpenAI 透過微軟控制 GitHub Copilot；Google 的 Gemini 深度整合於 Android Studio 和 Firebase；而 xAI 擁有的是 Cursor——以及透過 Cursor 觸達的，日益龐大的開發者群體。

## 開發者的評估要點

對正在評估 Grok 4.5 的團隊而言，關鍵的未知數包括：SWE-bench Verified 的實際成績、生產負載下的延遲穩定性（80 TPS 是標稱值，p95 延遲更能反映真實體驗），以及 X 搜尋整合在依賴即時資料的應用中的穩定性。50 萬 token 上下文視窗對大型程式庫分析極具價值；在接近上限時的效能表現，則需要獨立測試來驗證。

Grok 4.5 的出現意味著，程式碼模型賽道——曾是 GitHub Copilot 一家獨大的相對平靜市場——正在成為真正意義上的激烈競爭場域，模型架構、訓練合作關係與分發渠道，都在以過去難以想像的方式影響最終格局。
