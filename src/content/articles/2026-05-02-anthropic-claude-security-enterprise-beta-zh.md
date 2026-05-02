---
title: "Anthropic 推出 Claude Security 公開測試版，聯手 CrowdStrike 等六大資安巨頭"
summary: "Anthropic 正式將 Claude Security 開放給企業客戶公開測試，這款 AI 工具能像資深資安工程師一樣推理整個程式碼庫，自動發現漏洞並生成修補程式。此次發布背後有 CrowdStrike、Palo Alto Networks 等六大資安平台合作，標誌著 Anthropic 正式進軍企業資安市場——一個因 AI 生成程式碼爆炸性成長而誕生的全新戰場。"
category: "products"
publishedAt: 2026-05-02
lang: "zh"
featured: true
trending: true
sources:
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/04/30/anthropic-announces-claude-security-public-beta-find-fix-software-vulnerabilities/"
  - name: "Business Standard"
    url: "https://www.business-standard.com/technology/tech-news/anthropic-announces-claude-security-beta-for-enterprise-customers-126050100019_1.html"
  - name: "SecurityWeek"
    url: "https://www.securityweek.com/anthropic-unveils-claude-security-to-counter-ai-powered-exploit-surge/"
  - name: "CrowdStrike"
    url: "https://www.crowdstrike.com/en-us/press-releases/crowdstrike-puts-claude-opus-4-7-to-work-across-falcon-platform-project-quiltworks/"
tags:
  - "anthropic"
  - "claude"
  - "資安"
  - "企業"
  - "漏洞"
  - "AI安全"
relatedSlugs:
  - "2026-04-24-anthropic-19b-arr-claude-code-growth-zh"
  - "2026-04-17-claude-opus-47-release-zh"
  - "2026-04-12-anthropic-mythos-cybersecurity-model-zh"
---

幾個月來，資安研究人員一直在敲響同一記警鐘：AI 程式碼輔助工具讓程式碼的產出速度遠超人工稽核的能力，結果是愈來愈多的漏洞被直接埋進正式上線的系統裡。4 月 30 日，Anthropic 正式公布了它對這個問題的回應——Claude Security 現已向 Claude Enterprise 客戶開放公開測試，而且公司帶著一份令人印象深刻的合作夥伴名單一同亮相。

## 從研究預覽到企業產品

Claude Security 並非全新問世。Anthropic 最早在 2026 年 2 月以「Claude Code Security」為名，以限量研究預覽的形式提供給少數企業開發者試用。此次公開測試代表著重要的規模躍升：所有 Claude Enterprise 方案的企業現在都可以申請使用，Anthropic 表示將在未來數週內逐步擴大開放範圍。

產品的核心定位很清楚：Claude Security 的目標是發現傳統靜態分析工具看不到的東西。一般的漏洞掃描器是透過比對已知的漏洞特徵來運作——找 SQL 注入的樣板、緩衝區溢位的模式，或已知的 CVE。但 Claude Security 的做法不同，它像一位資深資安工程師一樣，對整個程式碼庫進行推理：跨檔案追蹤資料流向、檢查各元件在執行時的互動方式，最後綜合出一張攻擊者如何把多個低嚴重性問題串連成重大漏洞路徑的完整圖像。

在任何發現結果送到分析師面前之前，模型會為自己的推理過程賦予一個可信度評分，等於是在自我稽核。Anthropic 表示，這個過濾步驟是讓系統在企業規模下真正可用的關鍵——目標是打造一個資安團隊真正信賴的工具，而不是一個把警報通知塞爆的噪音機器。

## 六大合作夥伴加持，CrowdStrike 另組行業聯盟

這次合作夥伴陣容的公布，或許是整個發布中最具策略意義的部分。Anthropic 簽下了與 CrowdStrike、Microsoft Security、Palo Alto Networks、SentinelOne、TrendAI 以及 Wiz 的整合合作。每一家都將 Anthropic 的旗艦模型 Claude Opus 4.7 直接嵌入自家既有的資安平台。

CrowdStrike 的合作關係更進一步超越了一般的功能整合。就在 Claude Security 公告的同時，CrowdStrike 宣布啟動 **Project QuiltWorks**——一個由它主導召集的行業聯盟，專門應對該公司所稱的「AI 漏洞浪潮」。這個聯盟同時引入 Anthropic 與 OpenAI 的前沿模型，其宣示的使命是建立共用工具和最佳實踐，持續發現並修補 AI 生成程式碼帶來的安全漏洞。

這背後的語境意涵值得深思。CrowdStrike 不只是在 Falcon 平台上加一個新功能——它在把自己定位成一個全新子產業的核心，而這個子產業的存在，完全是因為 AI 程式碼工具改變了軟體開發的經濟邏輯。CrowdStrike 執行長 George Kurtz 稱 AI 生成的程式碼是「十年來企業攻擊面最大規模的擴張」，直接承認了企業為了提升開發速度而採用的那些工具，同時也在以傳統方法追不上的速度製造技術安全負債。

## Claude Security 要解決的市場問題

要理解 Anthropic 為何在此時推出這個產品，需要先看清 2026 年中的資安大環境。Anthropic 引用的數據顯示，過去 18 個月，AI 輔助開發程式碼庫中新發現漏洞的數量，比前三年的增速快了約三倍。但資安團隊的規模並沒有等比例成長。

直接原因顯而易見：當開發者可以從一個粗略的提示詞在幾分鐘內完成一個拉取請求，程式碼進入程式碼庫的速度自然大幅加快。不那麼明顯的是，AI 生成的程式碼往往以不同於人類撰寫程式碼的方式出錯。它經常產出看起來合理、語法正確、能通過基本測試的程式碼，卻帶有細微的邏輯錯誤——對驗證狀態的錯誤假設、信任邊界的不當處理、或只在特定條件或高負載下才會觸發的競態條件。

傳統靜態分析工具是為人類程式設計師的寫作模式而訓練的，對於這類新型漏洞的校準能力先天不足。Claude Security 的賭注是：一個能對整個程式庫進行上下文推理的大型語言模型，比基於特徵比對的掃描器更適合捕捉這些「AI 原生」漏洞。

## 定價與使用門檻

Anthropic 目前尚未公布細部定價，僅確認 Claude Security 向現有 Claude Enterprise 訂閱用戶開放。根據定位，它似乎是作為附加功能而非獨立產品推出，這與各家合作夥伴（CrowdStrike Falcon、Wiz Cloud Security、Microsoft Defender）各自以企業合約計費的方式相符。

對已使用 Claude Enterprise 方案的資安導向團隊而言，進入途徑是填寫一份申請表，Anthropic 表示將在整個 5 月以滾動方式審核。

## Anthropic 的企業版圖持續擴大

Claude Security 的發布是 Anthropic 有意識地擴展企業產品矩陣的最新例證。過去六個月，該公司陸續推出了 Claude for Word（整合 Microsoft Office 工作流程）、面向開發者的 Claude Code，現在又有了面向資安作戰中心的 Claude Security。每款產品都針對一個特定的專業工作流程，且都搭配夥伴合作，把 Anthropic 的模型嵌入客戶早已在付費使用的平台之中。

這套分發策略折射出企業軟體市場的殘酷現實：企業很少會捨棄已有的工具堆疊。要贏得企業客戶，就必須出現在那些已經分配到預算、已經獲得組織認可的工具裡——這正是 CrowdStrike、Palo Alto 和 Wiz 合作所帶來的價值。

## 下一步會怎麼走

以 2026 年 4 月底的數字計算，Anthropic 的年化收入已接近 190 億美元，足夠支撐公司以穩健的步調打造完整的企業產品組合。Claude Security 的加入，讓人愈來愈難用「只是一家 AI 模型公司」來定義 Anthropic。

更深層的問題在於：AI 驅動的資安工具，能否跟上 AI 驅動的威脅的腳步？CrowdStrike 的 Project QuiltWorks 已隱含地承認這是一場軍備競賽——幫助開發者更快寫程式碼的同一批模型，同樣可以幫助攻擊者更快找到並利用那些程式碼中的漏洞。從本質上說，Claude Security 就是 Anthropic 表態要站在這場競賽正確那一側的宣言。

對於正在努力消化自身 AI 輔助開發工作流程所帶來資安隱憂的企業而言，公開測試在此時此刻落地，既是一種解脫，也是對這片地基已變化多快的一份清醒認知。
