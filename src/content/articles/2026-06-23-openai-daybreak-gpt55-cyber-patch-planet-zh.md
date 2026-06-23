---
title: "OpenAI 擴大 Daybreak 計畫：GPT-5.5-Cyber 在 Linux、Chrome 和 Safari 找到漏洞並修補"
summary: "OpenAI 大幅擴展了 Daybreak 資安計畫，發布改良版 GPT-5.5-Cyber（CyberGym 評測得分 85.6%）、Codex Security 外掛重大更新（已掃描 3000 萬次提交、超 50 萬項問題自動修復），並推出「Patch the Planet」開源聯盟，與 Trail of Bits、HackerOne 合作，夥伴名單涵蓋 cURL、Python、Go 等重量級開源專案。"
category: "developer-tools"
publishedAt: 2026-06-23
lang: "zh"
featured: false
trending: true
sources:
  - name: "Help Net Security — OpenAI expanded Daybreak cybersecurity initiative"
    url: "https://www.helpnetsecurity.com/2026/06/23/openai-expanded-daybreak-cybersecurity-initiative/"
  - name: "The Hacker News — OpenAI Expands Daybreak with GPT-5.5-Cyber"
    url: "https://thehackernews.com/2026/06/openai-expands-daybreak-with-gpt-55.html"
  - name: "SiliconANGLE — OpenAI expands Daybreak with Patch the Planet"
    url: "https://siliconangle.com/2026/06/22/openai-expands-daybreak-patch-planet-full-gpt-5-5-cyber-release/"
  - name: "OpenAI Daybreak — Securing Every Organization"
    url: "https://openai.com/index/daybreak-securing-the-world/"
tags:
  - "openai"
  - "資訊安全"
  - "daybreak"
  - "gpt-5-5-cyber"
  - "codex-security"
  - "開源"
  - "漏洞"
relatedSlugs:
  - "2026-05-14-openai-daybreak-cybersecurity-gpt55-zh"
  - "2026-06-23-agentjacking-sentry-mcp-ai-coding-attack-zh"
  - "2026-06-23-openai-codex-record-replay-workflow-automation-zh"
---

OpenAI 的 Daybreak 資安計畫在五月以雄心勃勃的姿態登場，本週的重大擴展讓外界見識到這份雄心究竟有多大。

公司推出大幅強化的 GPT-5.5-Cyber 模型、釋出功能更強大的 Codex Security 外掛更新，並啟動名為「**Patch the Planet**」的開源安全聯盟——與 Trail of Bits、HackerOne 及 CALIF 合作，致力於清理支撐全球基礎設施的軟體中長期積累的漏洞缺口。從 Daybreak 系統迄今已發現的漏洞清單來看——Linux、FreeBSD、Chrome、Safari、NGINX、Apache、Python 悉數在列——前沿 AI 模型作為防禦性資安工具的實際價值，正在用具體數字替代口號。

## GPT-5.5-Cyber：基準測試說明問題

OpenAI 發布的 GPT-5.5-Cyber 更新版是其迄今最專業化的資安模型。在 **CyberGym**（涵蓋各類程式碼庫和系統配置的漏洞識別基準）上，它得分 **85.6%**，而通用版 GPT-5.5 為 81.8%。在測試模型能否開發可運行漏洞利用程式（PoC）的 **ExploitGym** 上，它達到 **39.5%**（通用版 GPT-5.5 為 25.95%）。在評估真實世界資安工程任務——包括威脅建模和修補驗證——的 **SEC-bench Pro** 上，得分為 **69.8%**。

ExploitGym 的數字值得深思。一個能為將近四成基準測試挑戰開發可運行漏洞利用程式的模型，其威力足以要求嚴格的存取控制。OpenAI 在 GPT-5.5-Cyber 前設置了驗證機制：存取需要證明防禦性使命，符合資格的對象包括資安廠商、有實際業務的滲透測試公司，以及具備可驗證內部安全職能的組織。獨立研究人員可以申請，但須接受額外審查。

雙重用途風險是真實存在的。同一種模型能力，在協助防禦方定位和修補 SQL 注入漏洞的同時，理論上也能被取得帳號存取的惡意行為者利用。OpenAI 沒有公開其驗證流程的細節，這種不透明性將持續受到資安社群的質疑。

## Codex Security：從掃描器進化為修補智能體

今年三月以雲端研究預覽形式推出的 Codex Security 外掛，在此次更新後升級為功能遠超靜態分析工具的存在。

原有版本可識別漏洞，並附上上下文嚴重性評等和受影響程式碼位置。新版本加入：**攻擊路徑追蹤**（跨系統依賴項追蹤漏洞的傳播路徑）、**威脅模型生成**（針對對手目標和系統暴露面生成結構化分析）、**自動化修補生成**（生成可審查的修補程式，而不僅僅是建議文字），以及**漏洞管理系統整合**（透過 SARIF 和 CodeQL 格式連接企業現有資安工具鏈）。

OpenAI 公開的規模數據才是最大亮點。自三月以來，Codex Security 已掃描超過 **3,000 萬次提交**，覆蓋 **3 萬個程式碼庫**；超過 **50 萬項發現**被自動判定為已修復——即 50 萬個案例中，程式碼在 Codex Security 發現問題後被修改，且修改內容滿足了原始漏洞條件。OpenAI 說明，這裡計算的是發現實例數，而非唯一漏洞數量；同一漏洞類別出現在多個位置，會被計為多次。

## 已披露的漏洞清單

OpenAI 公布了 Daybreak 系統迄今重大發現的摘要，受影響系統的普遍性令人警覺：

**Linux 核心**：8 個核心指標洩漏和 24 個本地提權漏洞利用程式。核心層漏洞可讓攻擊者取得對受影響系統的完全控制，從普通用戶提升到 root 是後滲透最常見的路徑。

**FreeBSD**：34 個漏洞，包含 7 個本地提權概念驗證。FreeBSD 支撐著 Netflix 的 CDN 基礎設施及索尼遊戲系統的大部分業務。

**dnsmasq**：6 個漏洞，存在於這款廣泛部署在全球數億台家用路由器和嵌入式系統中的輕量級 DNS 轉發器。

**HTTP/2 Bomb**：同時影響 **NGINX、Apache HTTP Server、微軟 IIS 和 Cloudflare Pingora** 的漏洞。NGINX 和 Apache 合計服務全球大多數公開 Web 流量；單一漏洞類別同時擊中這四款伺服器，意味著嚴重程度罕見的系統性暴露。

**Google Chrome V8**：Chrome JavaScript 引擎中的 5 個漏洞，影響範圍不只是瀏覽器本身，還涵蓋企業軟體中大量使用的 Electron 應用程式。

**Apple Safari**：10 個可利用漏洞。這些發現橫跨 iOS、macOS 和 iPadOS，組合攻擊面超過 20 億台設備。

OpenAI 表示，所有已披露漏洞均已透過協調披露機制通報各維護方，目前均已修補或正在積極修復中。

## Patch the Planet

聯盟的成立是此次公告中戰略意義最深遠的部分。Patch the Planet 將 OpenAI 的 AI 能力與 Trail of Bits（知名資安研究公司）、HackerOne（主流漏洞賞金平台）及 CALIF（專注於開源安全資助的非營利組織）結合，旨在解決開源安全生態的結構性缺口：廣泛部署的基礎設施軟體，由缺乏資安預算的小型志願者社群維護。

初始參與開源專案包括 **cURL**、**NATS Server**、**pyca/cryptography**、**Sigstore**、**aiohttp**、**Go 語言**、**freenginx**、**Python** 及 **python.org**。這份名單側重基礎設施管道而非終端用戶應用——單是 cURL 就為估計超過 100 億台設備處理 HTTP 傳輸。

公開啟動前進行的一次五天試驗衝刺「識別出數百個潛在問題，並促成數十個修補程式被合併」。受協調披露時程影響，OpenAI 未公布具體漏洞數量。

## Daybreak 資安合作夥伴計畫

在技術發布之外，OpenAI 同步宣布 Daybreak 資安合作夥伴計畫，允許資安廠商將 GPT-5.5 與「資安可信存取」框架整合進客戶產品，讓企業資安團隊得以透過現有資安工具鏈（SIEM、漏洞管理平台、應用安全工具）使用前沿 AI 漏洞掃描，而無需自建 OpenAI API 整合。

## 背景：防禦者缺口

CISA 估計全球資安人才缺口達 400 萬人。從漏洞發現到補丁部署之間的「修復速度差距」長期有利於攻擊方。如果 Codex Security 超過 50 萬項自動修復發現具有代表性，並且能持續規模化，其對這一差距的影響將在基礎設施層面產生真實意義。

Anthropic 的 Project Glasswing 雖在資安圈有傳聞，但迄今未公開披露；Google Project Zero 已將 Gemini 整合進部分研究流程，尚無類似計畫公告。OpenAI 主動披露具體漏洞發現——達到 CVE 就緒的披露標準，而非模糊的能力聲明——正在倒逼競爭對手提高透明度門檻。
