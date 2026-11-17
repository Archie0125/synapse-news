---
title: "Claude Fable 5 重返全球市場，美國解除出口管制"
summary: "美國商務部解除對 Anthropic Claude Fable 5 及 Mythos 5 的出口管制，Anthropic 在 6 月中旬開始的停用後恢復存取。Fable 5 重返時，部分方案適用暫時性的用量限制條款。"
category: "policy"
publishedAt: 2026-07-02
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "Anthropic"
    url: "https://www.anthropic.com/news/fable-mythos-access"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/anthropic-is-bringing-back-claude-fable-5-globally-after-us-lifts-export-control-order-where-can-enterprises-access-it"
  - name: "Euronews"
    url: "https://www.euronews.com/2026/07/01/us-lifts-export-controls-on-powerful-ai-models-anthropic-says"
tags:
  - "anthropic"
  - "claude"
  - "fable-5"
  - "export-controls"
  - "ai-policy"
  - "cybersecurity"
  - "us-government"
relatedSlugs:
  - "2026-07-02-claude-fable5-export-ban-lifted-global-return-en"
  - "2026-07-01-anthropic-claude-sonnet-5-agentic-launch-zh"
  - "2026-06-29-us-export-control-claude-fable5-foreign-ban-zh"
---

Anthropic 的 Claude Fable 5 預計自週三起重新開放給全球用戶，出口管制解除一事已於週二宣布。美國政府 6 月 12 日發出出口管制指令，禁止任何外國人存取後，Claude Fable 5 與 Mythos 5 已對所有客戶停用；Anthropic 表示，商務部解除管制後將恢復存取。這場由政府下令的商用 AI 模型停用，在 Anthropic 與美國政府合作後，隨出口管制解除而結束。

這在商業 AI 發展史上毫無先例，而其解決過程所留下的問題，不亞於封鎖本身。

## 封鎖的起點

Fable 5 在 6 月 9 日正式上線，是 Anthropic 迄今最強大的模型，在多數基準測試上持平或超越 GPT-5.5，並引入能自主處理長期任務的 agentic 能力。同日，Mythos 5 也在 Anthropic「Project Glasswing」計畫下，向一小群受信任的資安合作夥伴限量部署。

然而幾天後，一份亞馬遜網路服務的內部研究報告在政府圈內流傳。據 Anthropic 表示，政府認為已發現一種繞過（越獄）Fable 5 的方法；Anthropic 形容那是狹窄、非通用的越獄，內容是要求模型讀取特定程式碼庫並修復軟體缺陷。Anthropic 表示，該技術所找出的漏洞相對簡單，其他公開可用的模型不需繞過防護也能發現。

Anthropic 於 6 月 12 日收到該指令，要求其暫停任何外國人對 Fable 5 和 Mythos 5 的所有存取，不論身在美國境內或境外，包括 Anthropic 的外籍員工。由於 Anthropic 沒有即時驗證帳號國籍的機制，公司選擇全球下架兩款模型，而非嘗試可能面臨法律挑戰的局部合規方案。

結果是 Anthropic 為遵守該指令，在 6 月中旬對所有客戶停用 Fable 5 和 Mythos 5。

## 修補方案與監控框架

6 月 12 日的指令之後，Anthropic 為遵守規定對所有客戶停用 Fable 5 和 Mythos 5，並表示管制解除後將開始恢復存取。Anthropic 聯合亞馬遜安全團隊與政府，針對允許繞過防護的特定漏洞，以調整微調參數、部署執行期過濾器攔截相關提示模式、以及建立異常用量即時通報政府儀表板等方式，進行多層次修補。

更廣泛地說，Anthropic 同意了一套持續監控框架：若生產部署中的安全行為與基準線出現統計顯著的偏差，自動通知商務部。這代表一種全新的 AI 合規基礎設施類型——不是上市前的能力揭露，而是部署期間的持續行為驗證。

這套框架顯然讓政府滿意。6 月 30 日，商務部通知 Anthropic 解除出口管制。據 Anthropic 表示，Fable 5 將自週三起，於 Claude 平台、Claude.ai 及 Claude Code 重新開放給全球用戶。

## 分階段限制存取

解封並非無條件恢復。Anthropic 實施了分階段的用量限制，讓基礎設施團隊在恢復負載前能在監控下觀察部署狀況。7 月 7 日後，模型轉為依用量計費的信用點數制——這也是 Anthropic 對旗艦模型早已規劃的定價方向。

Anthropic 表示，將盡快在 Amazon Web Services、Google Cloud 及 Microsoft Foundry 重新啟用 Fable 5。

對於在封鎖前已將 Fable 5 整合進正式工作流程的企業客戶來說，分階段限制是在停用之後的又一次衝擊。據悉，部分大型企業客戶的法務團隊正在評估此次斷線是否構成針對 Anthropic 的合約索賠依據——Anthropic 的服務條款中，並未包含政府強制暫停存取的 SLA 條款。

## 台灣的處境

對台灣企業和開發者而言，這段停用期來得格外不是時候。多家科技公司在 Fable 5 上線後迅速將其導入正式環境，尤其是在程式審查、文件摘要及長期 Agent 任務方面。封鎖期間，企業被迫緊急降回 Claude Sonnet 4.6 或其他替代方案，雖然仍能運作，但造成了相當程度的作業中斷。

全球存取恢復後，台灣用戶再度受到 Anthropic 標準服務條款的保障。現行監控框架不設地理限制，所有用戶在同一套行為驗證體系下運作，政府儀表板呈現的是整體用量模式，而非個別帳號資訊。

## 這個先例意味著什麼

這起事件的深遠意義，在於它對前沿 AI 監管格局的示範效應：在政府指令下，Anthropic 對所有客戶停用了 Fable 5 和 Mythos 5，並在管制解除後開始恢復存取。

這開創了一種新的部署風險類型。依賴美國前沿模型建構國際 AI 部署的企業，現在必須在架構決策中為「監管中斷風險」定價——這是一種既有商業條款中不存在的風險維度。

對產業而言，最迫切的懸念是：這套快速合規框架是否將成為未來能力監管的標準模板？川普的行政命令仍然有效，而「政府可在發現安全疑慮後快速觸發全球封鎖」的先例，已然確立。問題是這個機制將以多高的頻率被啟用。

Mythos 5 已在 6 月 26 日獲政府核准後，對部分美國機構恢復存取，Anthropic 表示將持續與美國政府合作，透過 Glasswing 計畫向更多國內外夥伴擴大 Mythos 5 的存取。隨著 GPT-5.6 Sol 也進入類似的政府預覽審查程序，一個模型必須通過持續安全認證才能在全球部署的時代，似乎已經正式開始。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 18 處。*
