---
title: "惡意 VS Code 擴充套件入侵 GitHub：3,800 個內部儲存庫遭竊，OpenAI、Mistral 淪陷"
summary: "TeamPCP 攻擊組織僅靠 18 分鐘的上架窗口，便透過中毒的 Nx Console 18.95.0 擴充套件入侵 GitHub 員工裝置，外洩約 3,800 個內部原始碼儲存庫。下游受害者確認涵蓋 OpenAI、Grafana Labs 與 Mistral AI，事件根源可追溯至兩週前的 TanStack npm 供應鏈攻擊。"
category: "developer-tools"
publishedAt: 2026-05-25
lang: "zh"
featured: false
trending: false
sources:
  - name: "The Hacker News"
    url: "https://thehackernews.com/2026/05/github-internal-repositories-breached.html"
  - name: "Help Net Security"
    url: "https://www.helpnetsecurity.com/2026/05/20/github-breached-teampcp/"
  - name: "OX Security"
    url: "https://www.ox.security/blog/teampcp-strikes-again-how-a-trojan-vs-code-extension-brought-down-github/"
  - name: "StepSecurity"
    url: "https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised"
tags:
  - "資安"
  - "供應鏈攻擊"
  - "vscode"
  - "github"
  - "開發者工具"
  - "teampcp"
  - "nx-console"
relatedSlugs:
  - "2026-05-25-github-nx-console-teampcp-supply-chain-attack-en"
  - "2026-05-17-pwn2own-berlin-2026-ai-platforms-zero-days-zh"
  - "2026-05-13-red-hat-summit-agentic-ai-developer-tools-zh"
---

2026 年 5 月 18 日上午，一個下載量超過 220 萬次的 VS Code 擴充套件悄悄推送了一次版本更新，從而引爆了近年來波及最廣的開發者供應鏈資安事件。Nx Console 18.95.0 版本在 Visual Studio Marketplace 上架後僅 18 分鐘，即遭 Microsoft 安全團隊強制下架。然而對幕後攻擊組織 TeamPCP 而言，18 分鐘已綽綽有餘。

惡意版本下架時，損害早已造成。作為 Microsoft 旗下子公司的 GitHub 在 5 月 19 日公開披露，約 3,800 個內部原始碼儲存庫遭到外洩。隨後數日，確認的下游受害者進一步擴大至 OpenAI、Grafana Labs 與 Mistral AI。

## 多階段攻擊鏈解析

要理解 TeamPCP 的操作手法，必須回溯至兩週前的 5 月 11 日。當天，該組織對 42 個 TanStack npm 套件發動供應鏈攻擊，在 npm 上發布了 84 個含有憑證竊取 JavaScript 載荷的惡意版本。

TanStack 是一套廣泛使用的開源 JavaScript 工具庫，TanStack Query、TanStack Router 與 TanStack Form 等套件出現在全球數以萬計的生產環境中。這批惡意套件只有一個目的：透過 GitHub CLI（gh）竊取開發者儲存或使用的 GitHub 認證憑證。在此次初始攻擊的眾多受害者中，恰好有一名 Nx Console 專案的合法貢獻者。

取得憑證後，TeamPCP 開始執行第二階段。攻擊者偽裝成合法的 Nx Console 維護者，將一個 498 KB 的混淆惡意載荷藏匿在官方 nrwl/nx GitHub 儲存庫的「孤立提交」（orphan commit）中——此類提交在標準分支瀏覽介面中完全不可見。這個隱藏提交成為了遠端載荷的寄存點。5 月 18 日，攻擊者隨即在 VS Marketplace 發布了 18.95.0 版本。

## 載荷：無聲、多管道、全面收割

惡意擴充套件被設計為在工作區開啟時自動觸發。開發者一打開任何專案，擴充套件便在數秒內從隱藏的孤立提交拉取並執行混淆載荷。該載荷是一個多階段憑證竊取與供應鏈污染工具，鎖定範圍涵蓋：

- **GitHub**（個人存取 Token、SSH 金鑰）
- **npm**（發布憑證與 .npmrc Token）
- **AWS**（存取金鑰與 Session Token）
- **HashiCorp Vault**（Operator Token）
- **Kubernetes**（服務帳戶金鑰、kubeconfig 條目）
- **1Password**（密碼庫解鎖憑證）
- **AI 程式碼助理**（Copilot、Cursor、Claude 的 API 金鑰）

外洩行動透過三個獨立管道進行：HTTPS 連往攻擊者控制的端點、偽裝成儲存庫活動的 GitHub API 呼叫，以及作為備用管道的 DNS 通道。這種三重冗餘架構大幅降低了邊界防禦設備的偵測能力。

Nx Console 事件前擁有超過 220 萬次安裝。惡意版本在 VS Marketplace 上架僅 18 分鐘（OpenVSX 上則為 36 分鐘），Nx Console 開發團隊仍估計逾 6,000 名開啟自動更新的開發者受到感染。

## GitHub 內部儲存庫遭洗劫

GitHub 於 5 月 19 日公開確認，一名員工裝置遭惡意擴充套件感染，攻擊者隨即利用取得的存取權限外洩約 3,800 個內部儲存庫。GitHub 資安長（CISO）指認 Nx Console 為事件根本原因，並表示 3,800 個的規模與其調查結論「方向一致」。

遭洩儲存庫涵蓋內部工具程式碼、配置管理腳本與基礎設施自動化檔案。GitHub 強調此次入侵並未直接影響公開平台或客戶資料，但潛在連鎖風險不容忽視——任何嵌入這些內部儲存庫的機密或 API 金鑰，都可能成為攻擊者滲透更多系統的跳板。

已確認的下游受害名單清楚呈現了現代供應鏈攻擊的連鎖效應。在 OpenAI、Grafana Labs 與 Mistral AI 工作且啟用自動更新的開發者，在毫不知情的情況下接收了惡意版本。這些開發者機器上存放的機密——連通 AI 訓練基礎設施、可觀測性平台與雲端服務的憑證——均面臨外洩風險。

## TeamPCP 的操作指紋

TeamPCP 在暗網論壇上主動宣稱對此次行動負責，將其定性為「現代開發者供應鏈內在脆弱性的一次示範」。率先發布技術分析的 OX Security 研究人員識別出 TeamPCP 多次以開發者工具為目標的歷史攻擊，並指出該組織擅長「耐心等待」——通常在初始憑證竊取後靜候數週再行利用。TanStack 攻擊（5 月 11 日）與 Nx Console 惡意版本發布（5 月 18 日）之間的七天間隔，完全符合這一作案模式。

發布獨立資安通告的 StepSecurity 則指出，此次攻擊代表針對開發者的戰術升級。以往的供應鏈攻擊多針對生產部署使用的程式庫；本次攻擊鎖定的目標卻是開發環境本身——以開發者級別權限運行、並可存取開發者所觸及之所有系統憑證的 VS Code 擴充套件。

## 修補措施與後續衝擊

Nx Console 在惡意版本下架後隨即發布 18.95.1，官方團隊緊急建議所有開發者立即輪換憑證、檢查裝置是否出現入侵跡象，並審查近期部署紀錄與 CI/CD 流水線輸出是否存在異常。

Microsoft 已宣布計畫為 VS Code Marketplace 引入針對擴充套件更新的即時行為分析機制。若此機制早已部署，本次惡意載荷極可能在分發前便遭攔截。Marketplace 先前主要依賴靜態分析與發布者信譽評分，這套防禦體系在面對已遭入侵的合法維護者帳號時，顯然力有未逮。

對企業而言，此事件帶出一個嚴峻問題：開發者機器上的憑證安全歷來受到忽視，但 TeamPCP 竊取的 AWS Token、Kubernetes 服務帳戶金鑰、CI/CD 機密，正是足以讓攻擊者從一台受感染的開發者筆電橫向移動至生產基礎設施的關鍵憑證。開發者端點的終端防護（EDR）覆蓋率，已成為許多企業亟需補強的優先事項。

## 開發者生態系統長期被忽視的系統性風險

Nx Console 事件印證了資安研究人員多年來的警告：現代開發者工具鏈所形成的攻擊面廣大且長期被低估。開發者在 VS Code 中安裝數十個擴充套件、使用 npm 全域套件、執行 GitHub Actions 工作流與各種 CLI 工具——每一個都是潛在的信任邊界。一旦任何環節遭到入侵，攻擊者獲得的不只是單一系統的存取權，而是該開發者所能觸及之所有系統的進入許可。

一個擁有 220 萬次安裝量的擴充套件能在 18 分鐘內被武器化並入侵 GitHub 內部程式碼庫，這一事實為整個業界提供了一次清醒的警示。

GitHub 至今未公開表示，外洩的內部儲存庫內容是否已在外部被觀察到流通。對於仍在評估自身曝險的企業而言，這份沉默帶來的是更深的隱憂。
