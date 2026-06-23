---
title: "Fable 5 禁令解密：SK 電訊、越獄漏洞，與一份被拒絕的最後通牒"
summary: "最新報導揭示，SK 電訊涉嫌與中國存在關聯，觸發白宮對 Anthropic Glasswing 計畫的安全審查；同日，Amazon 執行長傑西（Andy Jassy）也向川普政府通報 Fable 5 越獄漏洞。據悉，Anthropic 執行長 Dario Amodei 被給予修補漏洞或主動下架模型兩個選項，他兩者皆拒絕，出口禁令隨即於 6 月 12 日落地。"
category: "policy"
publishedAt: 2026-06-19
lang: "zh"
featured: false
trending: true
sources:
  - name: "Korea JoongAng Daily"
    url: "https://www.koreajoongangdaily.com/business/white-house-officials-pin-anthropic-ai-export-block-on-korean-telecom-report/12726842"
  - name: "Fortune"
    url: "https://fortune.com/2026/06/14/how-a-warning-from-amazon-led-the-white-house-to-shut-down-anthropics-mythos-model/"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/trump-adviser-david-sacks-says-anthropic-refused-to-fix-fable-5-jailbreak-before-us-export-controls"
  - name: "MSN/Technology"
    url: "https://www.msn.com/en-us/news/technology/us-warned-anthropic-of-china-breach-but-firm-refused-to-fix-fable-5-jailbreak-says-david-sacks/ar-AA25BWh2"
tags:
  - "AI政策"
  - "出口管制"
  - "Anthropic"
  - "SK電訊"
  - "Fable 5"
  - "國家安全"
  - "越獄"
  - "白宮"
relatedSlugs:
  - "2026-06-16-claude-fable-5-mythos-5-us-government-shutdown-zh"
  - "2026-06-17-anthropic-project-glasswing-150-orgs-critical-infrastructure-zh"
  - "2026-06-19-anthropic-seoul-office-korea-ai-partnerships-zh"
---

這場長達一週的 Anthropic 旗艦模型停機，起點並非一紙政策文件或一場立法聽證。根據最新報導，它源自幾乎同一時間抵達白宮的兩條警示線——一條關於誰能存取這些模型，另一條關於這些模型能被迫做些什麼。

兩條線交匯的結果，是 6 月 12 日那份暫停所有外國公民存取 Fable 5 和 Mythos 5 的出口管制指令——截至 6 月 19 日，禁令仍然有效。這也是自川普政府開始強力介入前沿 AI 模型存取以來，最重大的一次政府干預行動。

## SK 電訊如何成為導火線

第一條線通往南韓。Anthropic 於 2026 年 4 月啟動 Glasswing 計畫，最初約 50 個美國夥伴組織獲得 Mythos 5——Anthropic 功能最強、限制最少的模型——的管控存取權限。到 6 月初，Glasswing 已擴展至全球約 150 個組織，其中包括來自韓國的三星電子、SK 海力士，以及 SK 電訊。

SK 電訊是韓國最大的行動通訊業者，也是 Anthropic 早期融資輪中出資 1 億美元的投資者。白宮官員在審查 Glasswing 的擴展名單時，發現其中有一家韓國電信公司「被懷疑與中國存在關聯」。雖然 SK 電訊未被官方點名，公司也拒絕就相關報導置評，但它是 Glasswing 計畫中唯一的韓國電信業者，多份報導均指向其為當事方。

值得強調的是，質疑的核心並非 SK 電訊做了什麼——而在於它的存取本身。Glasswing 設計的初衷，正是讓受信任的組織取得 Anthropic 最強大 AI 的存取權，尤其針對網路安全應用場景。將這種存取權授予一家疑似對中國存在曝露的實體，從出口管制的邏輯來看，恰恰是該制度試圖防範的情境。

事發背景是：Anthropic 最初向政府提交了一份含 111 個組織的審核名單，獲得批准；此後擴增名單中加入了那家韓國電信業者，而正是這份更新名單觸發了審查機制。

## Amazon 的警告

第二條線則獨立而至，但時間點幾乎重疊。Amazon 執行長傑西（Andy Jassy）——其公司是 Anthropic 最大的雲端服務提供商，也是重要投資方——在 6 月 12 日當天，直接向川普政府高層官員提出了安全顧慮。

Amazon 研究人員發現，透過「一系列特定提示詞」，可以讓 Mythos 級別的模型「提供原本應受限制的網路攻擊資訊」，亦即一種越獄（jailbreak）。這段提示序列能繞過 Fable 5 消費者功能與 Mythos 5 不受限制的網路輔助能力之間的安全護欄。

白宮 AI 暨加密政策顧問、總統科學技術諮詢委員會（PCAST）共同主席大衛・薩克斯（David Sacks）將消息來源稱為「極具公信力的可信夥伴」——這一描述與 Amazon 作為雲端夥伴兼重大投資方的身份高度吻合。

## 被拒絕的最後通牒

在正式發出出口管制指令之前，白宮給了 Anthropic 兩個選項：修補越獄漏洞，或主動下架 Fable 5 的外國公民存取權。薩克斯表示，執行長 Dario Amodei 兩者皆拒絕。

Anthropic 的立場是：這個越獄屬於「有限範圍的繞過，而非全面越獄」——Amodei 的措辭顯示，公司認為這只是一個定向的提示技巧，而非根本性的安全漏洞，風險程度遭到高估。

薩克斯的回應則毫不留情。他在 X 上公開表示，政府「坦率地說，對 Anthropic 不願配合其自稱最優先重視的安全要求感到困惑」，並強調禁令是「不得已而為之」，且模型的恢復「僅取決於 Anthropic 修補漏洞」。

白宮隨後對 WIRED 表示，Anthropic 必須消除 Fable 5 的「所有越獄」，才能為外國用戶恢復存取——這個要求隨即在 AI 安全研究界引發強烈質疑。

## 「零越獄」是不可能的標準

「越獄防護是縱深防禦，不是一個已解決的問題，」一位 AI 安全研究人員對 The New Stack 表示。迄今為止，沒有任何一款前沿 AI 模型曾被認證為完全免疫越獄攻擊，因為對抗性提示詞的空間在實踐上是無窮的。若嚴格照字面執行「消除所有越獄」的要求，模型可能永遠無法恢復上線。

Anthropic 至今尚未公開回應這個矛盾。公司國際業務總監 Chris Ciauri 在首爾辦公室開幕場合向記者表示，他「非常有信心」模型將「在未來幾天內恢復」——這個措辭暗示，白宮或許正以比公開聲明更靈活的方式解讀其要求，雙方正在進行實質性談判。

## 受益者是誰？

在現有 AI 廠商忙於應對風波之際，至少有一家公司看到了機會。中國 AI 新創 MiniMax 主動推廣旗下新發布的前沿級開放權重模型 M3，特別強調開放權重模型「無法被政府指令在全球範圍內強制下架」——其言外之意再清楚不過：Fable 5 對 Anthropic 伺服器的依賴，正是讓出口禁令得以生效的根本原因。

這場風波也重新點燃了對 AI 存取計畫安全審查機制的討論。Glasswing 在不到兩個月內從 50 個擴展到 150 個合作組織，其速度似乎超過了應有的安全核查流程。Anthropic 內部管控與政府審批程序究竟誰的疏失更為嚴重，雙方至今都在迴避直接回答。

## 後續走向

截至 6 月 19 日，針對外國公民的存取禁令仍然有效，未設具體恢復日期。Anthropic 目前以較舊的 Claude 3 系列服務國際用戶，美國用戶則仍可存取 Fable 5 和 Mythos 5。

解禁路徑看來需要 Anthropic 向政府展示對越獄漏洞的實質性修補——至於「實質性」的定義，將由談判決定。鑑於 Amodei 最初的拒絕和薩克斯的公開批評都已是公開紀錄，任何解決方案都需要讓雙方都能宣稱實現了各自的目標。

這整件事或許揭示了一個更深層的道理：當 AI 模型被整合進國家安全計畫、被賦予不受限制的網路作戰輔助能力，管控其部署的政治與法規約束，就與技術約束本身沒有了本質區別。Anthropic 打造了一款強大到足以讓其存取名單成為國家級關切事務的模型。而這種能力，事實證明，是有代價的。
