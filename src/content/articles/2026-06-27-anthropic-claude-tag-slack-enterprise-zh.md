---
title: "Anthropic 讓 Claude 成為企業 Slack 的永久 AI 隊友，還會主動找你說話"
summary: "Anthropic 於 6 月 23 日推出 Claude Tag 公開測試版，將 Claude 嵌入 Slack 頻道成為共享的持久 AI 隊友。團隊可以 @Claude 指派任務、非同步協作，更特別的是「環境模式」讓 Claude 不等召喚就主動介入。Anthropic 透露內部產品團隊已有 65% 的程式碼由 Claude Tag 生成。"
category: "products"
publishedAt: 2026-06-27
lang: "zh"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/23/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/"
  - name: "Fortune"
    url: "https://fortune.com/2026/06/23/anthropic-claude-tag-virtual-employee-tool-slack/"
  - name: "The Decoder"
    url: "https://the-decoder.com/claude-tag-embeds-anthropics-ai-in-slack-already-writes-65-percent-of-internal-code-company-says/"
  - name: "The New Stack"
    url: "https://thenewstack.io/anthropic-claude-tag-slack/"
tags:
  - "anthropic"
  - "claude"
  - "slack"
  - "企業 ai"
  - "ai 代理"
  - "生產力"
relatedSlugs:
  - "2026-06-25-snowflake-summit-2026-agentic-enterprise-anthropic-zh"
  - "2026-06-25-runlayer-30m-series-a-ai-agent-governance-zh"
---

2020 年代中期，Slack 整合市場充斥著各種 AI 聊天機器人與斜線指令，大多數只是讓你更快寫一條站立會議更新。Anthropic 的 **Claude Tag** 從根本上不同，而這個差別正好指向企業 AI 真正的走向。

2026 年 6 月 23 日，Claude Tag 以公開測試版形式推出，面向 Claude Enterprise 與 Team 客戶開放。它不是一個住在私訊視窗裡的個人助理——而是把 Claude 安裝成一個**全頻道共享的永久成員**，整個團隊都可以看到他在做什麼、指派任務給他、或中途接手改變方向。更特別的是，他可以主動找你說話，不需要你先開口。

## Claude Tag 如何運作

系統管理員在頻道層級進行設定，精細控制 Claude 能存取哪些工具（網路搜尋、程式執行、文件庫、內部 API）以及哪些頻道可以讀取。工程團隊的 Claude 可能有 GitHub 與 Jira 的存取權；法務團隊的 Claude 只能讀合約資料庫，其他一概不行。不同部門有各自的 Claude、各自的權限範圍，避免敏感資訊的跨部門洩漏。

有人在頻道輸入 **@Claude** 後，模型接收請求、必要時拆解任務，然後在所有人可見的討論串中執行工作。這種公開性是產品的核心設計選擇：不像個人 AI 助理的輸出只有自己看得到，Claude Tag 的工作過程對整個團隊透明，任何成員都可以即時插手、調整方向或增加新任務。

因為 Claude Tag 會從頻道歷史記錄中積累脈絡，它對組織的理解遠超過一個每次從零開始的對話 AI：哪些專案正在進行中、哪些決策已經確定、誰負責哪個領域、組織內部有哪些慣用術語——這些隱性知識，正是它與一般 Claude API 整合最大的差異所在。

## 環境模式：不等你問，自己開口

Claude Tag 最獨特的能力，是 Anthropic 所稱的**環境模式（Ambient Mode）**。開啟後，Claude 不需要被 @提及，而是持續監測頻道動態，主動浮現更新、標記問題、追蹤久無回應的討論串。

如果團隊兩天前討論了一個重要的部署決策，之後頻道陷入沉默，Claude 可能會出聲：「你們週四討論的認證架構重構沒有後續更新，需要我查一下目前 CI 狀態嗎？」如果某個決策討論串看似有了結論但沒人整理成行動項目，Claude 可以起草一份結構化摘要，確認後發給整個團隊。

這是 AI 工具運作方式的根本轉變。從「你呼叫它才動」，到「它有組織情境意識、主動找你確認要不要動」。Anthropic 明確把 Claude Tag 定位為擁有團隊角色的 AI 代理，而不是掛了個 Slack 介面的聊天機器人。

## 65% 的代碼是 Claude 寫的

Claude Tag 發布材料中最令人矚目的數字，是一個內部數據：Anthropic 自家產品團隊，現在有 **65% 的程式碼**透過 Claude Tag 生成。

若此數字屬實，意義深遠——構建 Claude 的工程師，有將近三分之二的程式碼是 Claude 自己寫的，這是一個遞歸式的能力自我證明。

當然，這個數字有未揭露的前提：不清楚 65% 是否包含了樣板程式碼、測試架構、文件生成等佔比較大的類別，還是只計算新功能邏輯。而 Anthropic 工程團隊本身就是全球最精通 AI 協作的一批人，其使用效率恐怕遠超一般企業軟體團隊。

但即便打折扣，65% 仍是一個值得認真看待的訊號：對於能夠原生融入 AI 工作流的團隊而言，嵌入溝通基礎設施的環境式 AI 協作，能帶來的生產力提升，可能遠遠超過獨立 AI 程式設計助理所能達到的上限。

## 企業戰略佈局

Claude Tag 是 Anthropic 2026 年企業策略的縮影。面對市場廣泛預期的 IPO 時程，Anthropic 正在構建的，是能深度嵌入組織工作流、製造高度切換成本的企業護城河——而非只停在 API 存取層。

競爭格局清晰：Microsoft Copilot 透過 Microsoft Graph 跨 Teams、Word、Outlook 整合，從系統層滲透；Google Gemini for Workspace 同樣基於 Google 生產力套件。Glean 則從知識圖譜切入，以檢索為核心。

Claude Tag 押注的方向不同：溝通層——決策在這裡形成、脈絡在這裡流動、工作在這裡協調——才是環境 AI 最有價值的落點。Claude 的對話與推理能力，最適合在真實團隊的 Slack 頻道那種雜亂、有脈絡、非同步的環境中發揮。

## 從工具到代理人

Claude Tag 代表了一個對職場 AI 走向的具體押注：從「你操作的工具」，演化為「你管理的代理人」。工具等待你的指令。代理人在授權範圍內持續運作，自主監測環境、主動浮現相關行動——更像在管理一位能幹的團隊成員，而不是在操作一款軟體介面。

如果環境 AI 隊友成為企業溝通平台的標準配置，組織的運作邏輯將隨之改變。更少的「請問這件事到哪了」；更完整的決策脈絡被即時記錄下來；更少的重要事項在人與人之間流轉時悄悄消失。

那個 65% 的數字，不只是行銷素材。它是一個預告，讓我們看見當 AI 從少數人主動選用的生產力工具，變成整個組織預設部署的基礎設施時，工作究竟會長成什麼樣子。
