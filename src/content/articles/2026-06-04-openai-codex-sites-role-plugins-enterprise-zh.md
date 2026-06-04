---
title: "OpenAI Codex Sites：用一句話描述，任何員工都能部署一個上線的網頁應用"
summary: "OpenAI 在 6 月 2 日發布 Codex Sites，讓任何人只需以自然語言描述需求，Codex 即可自動建構、部署並托管一個可分享的網址應用——完全不需要工程師介入。搭配新推出的六款職能角色外掛（銷售、行銷、財務、人資、產品、營運），此次更新標誌著 OpenAI 正將 Codex 從工程師工具，打造為全企業知識工作者的 AI 作業平台。"
category: "developer-tools"
publishedAt: 2026-06-04
lang: "zh"
featured: false
trending: true
sources:
  - name: "OpenAI 官方部落格"
    url: "https://openai.com/index/codex-for-every-role-tool-workflow/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/orchestration/openais-codex-update-lets-agents-build-interactive-enterprise-workspaces-via-sites-and-role-specific-plugins"
  - name: "Build Fast With AI"
    url: "https://www.buildfastwithai.com/blogs/openai-sites-codex-launch-review-2026"
tags:
  - "OpenAI"
  - "Codex"
  - "開發者工具"
  - "企業AI"
  - "無程式碼"
  - "AI代理"
  - "ChatGPT"
relatedSlugs:
  - "2026-05-16-openai-codex-mobile-app-developer-zh"
  - "2026-05-20-openai-dell-codex-enterprise-on-premises-zh"
  - "2026-06-04-google-io-2026-search-ai-agents-overhaul-zh"
---

企業 AI 導入長期存在一個核心矛盾：工程師熱愛這些工具，但真正做決策的業務端使用者大多沒在用。OpenAI 過去半年花了大量心力解決這個問題。6 月 2 日，答案終於公開。

在「智能工作（Intelligence at Work）」發表會上，OpenAI 以預覽版形式推出了 **Codex Sites**——讓任何人用一句自然語言描述需求，Codex 就能自動建構、部署並托管一個可分享的網址應用，全程無需開啟程式碼編輯器、無需設定雲端環境、無需提票給 DevOps 團隊。幾分鐘後，一個可在瀏覽器直接使用的儀表板、進度追蹤器、KPI 檢視工具或客製工作流程，就會出現在同事眼前。

同步發布的還有六款**職能角色外掛包**，分別針對銷售、行銷、財務、人資、產品與營運，預先整合了各職能日常所需的工作流程與輸出格式。法務、企業財務及私募股權的外掛版本則正在開發中。

這兩項更新加在一起，代表 Codex 的定位出現重大轉型：它不再只是協助工程師寫程式的工具，而是要成為企業知識工作的 AI 作業層。

## Codex Sites 究竟能做什麼

Codex Sites 的訴求比傳統無程式碼（no-code）平台更乾淨。傳統無程式碼平台即使不用寫語法，仍要求使用者理解表單邏輯、條件判斷、資料庫結構。Codex Sites 把這一切壓縮成一段自然語言對話。行銷分析師可以描述「一個帶有即時資料、可按地區篩選、有分享按鈕的活動追蹤儀表板」，Codex 就會把它建出來。

身份驗證透過「以 ChatGPT 登入」處理，無需自行設定 OAuth 或建立用戶管理機制。生成的應用由 OpenAI 基礎設施托管，IT 部門不需要做任何部署設定或維運管理。

OpenAI 在發表會上展示的應用類型涵蓋：整合即時 KPI 資料的部門儀表板、專案審查工作區、內部知識庫、輕量 CRM 視圖、請款單產生器與費用審核流程。這類工具在多數企業不是散落在複雜的 Excel 試算表中，就是需要工程師花時間開發維護。Codex Sites 讓這個落差消失。

隨同上線的 **Codex Annotations**，則允許對文件特定段落、試算表儲存格、投影片、圖像或網頁應用進行精準編輯，而非重新生成整份內容——解決了 AI 文件協作的一大痛點：「叫 AI 改第四段，結果第一到第三段也一起亂掉」的問題。

## 那個最關鍵的企業用戶數字

OpenAI 披露 Codex 每週活躍用戶已突破 500 萬，高於五月中推出行動版時揭露的 400 萬。絕對數字的意義，不如其背後的結構來得重要。

在 Codex 用戶中，約 20% 是知識工作者：分析師、行銷人員、業務主管、設計師、研究員、投資人與銀行從業者，他們不親自寫程式，但用 Codex 強化自己的工作流程。這個 20% 的族群，成長速度是工程師族群的三倍。如果這個趨勢持續，不到一年，非工程師用戶將成為 Codex 的最大用戶群體。

這絕非偶然。OpenAI 刻意以此為軸，調整行銷策略、產品路徑圖與外掛架構。Codex Sites 的發布是這個策略的頂點：它移除了最後一道門檻——你不再需要以技術語言描述你要什麼，只需說你希望達成什麼結果。

## 職能角色外掛：讓 Codex 學會你的工作

六款外掛包的設計邏輯，是讓 Codex 擁有各職能場景所需的上下文能力，而非要求使用者自行以提示詞工程導出專業輸出。

財務外掛整合了常用金融資料來源，內建預算差異分析、財報摘要與情境模擬的模板。銷售外掛連接 CRM 資料，優化漏斗審查與客戶研究流程。行銷外掛聚焦成效分析、內容規劃與活動追蹤。人資、產品與營運外掛依循相同邏輯，各自預載對應職能的工作慣例與輸出格式。

對企業採購決策者而言，商業邏輯相當直白：Codex Business 訂閱預設包含 Sites，無需額外付費；Enterprise 管理員可透過角色存取控制（RBAC）開放 Sites 使用權限。讓財務團隊成員使用預設好的 Codex 職能外掛，幾乎是零邊際成本，而哪怕是保守估計，生產力提升幅度也相當可觀。

## AWS 整合：企業基礎設施的必要一步

另一項值得關注的動態，是 OpenAI 正式確認 Codex 透過 Amazon Bedrock 在 AWS 上線，讓企業客戶可在既有雲端架構內運行 Codex，而無需將工作負載路由至 OpenAI 直接 API。對金融服務、醫療、政府等受監管行業而言，資料駐留（data residency）與供應商合規往往是硬性要求，AWS 原生整合移除了這道障礙。

OpenAI 表示，透過 Codex 完成程式碼審查、除錯與應用現代化的用戶已超過五百萬。目前已對特定用戶開放的 Computer Use 功能，讓 Codex 可直接操作 Windows 應用程式——透過截圖解讀畫面內容並發出滑鼠與鍵盤指令，將 Codex 的能力範圍從文字生成延伸至真正的自主工作流執行。

## 競爭格局：分發即護城河

Codex Sites 進入的是一個競爭激烈的市場。微軟 Copilot Studio 讓非工程師建構代理的功能已推出數月；Google 在 I/O 2026 發表的 Antigravity 平台也包含應用生成能力；GitHub Copilot Workspace 針對工程師用戶；Replit、Vercel 等平台也都在 AI 生成程式碼上持續精進。

OpenAI 的獨特優勢在於分發基礎。ChatGPT 每週活躍用戶超過八億，意味著 Codex Sites 不需要從零開始獲取用戶，而是要把已存在、已活躍的用戶群，從「對話」轉化為「建構」。此次 Sites 發布，本質上是一個押注：相當比例的 ChatGPT Business 和 Enterprise 用戶，將自行發現他們其實能夠建置以前做不到的內部工具——而這個「發現」會比任何銷售動作更有效地深化留存率並拓展訂閱席次。

如果這個轉化在規模上真的發生，「AI 助理」與「應用平台」之間的邊界，將在 ChatGPT 界面內有效消融——企業軟體市場的面貌也將隨之改變。
