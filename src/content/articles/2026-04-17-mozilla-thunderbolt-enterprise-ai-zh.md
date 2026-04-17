---
title: "Mozilla 推出 Thunderbolt：開源自建企業 AI 用戶端，直攻 Copilot 與 ChatGPT Enterprise"
summary: "Mozilla 的營利子公司 MZLA Technologies 於 4 月 16 日發布 Thunderbolt，一款開源、可自部署的企業 AI 用戶端，專為不願將敏感數據交由 Microsoft Copilot、ChatGPT Enterprise 或 Claude Enterprise 處理的組織而設計。由 Thunderbird 團隊以 MPL 2.0 授權打造，開箱即支援雲端與本地模型，鎖定有嚴格資料治理需求的企業。"
category: "developer-tools"
publishedAt: 2026-04-17
lang: "zh"
featured: false
trending: false
sources:
  - name: "The Register"
    url: "https://www.theregister.com/2026/04/16/mozilla_thunderbolt_enterprise_ai_client"
  - name: "HelpNet Security"
    url: "https://www.helpnetsecurity.com/2026/04/17/mozilla-thunderbolt-open-source-ai-client-enterprise-data-control/"
  - name: "GamingOnLinux"
    url: "https://www.gamingonlinux.com/2026/04/mozilla-announced-thunderbolt-their-open-source-and-self-hostable-ai-client/"
  - name: "deepset"
    url: "https://www.deepset.ai/news/sovereign-ai-stack-mozilla-thunderbolt-haystack"
tags:
  - "Mozilla"
  - "開源"
  - "企業 AI"
  - "自建 AI"
  - "開發工具"
  - "隱私"
relatedSlugs:
  - "2026-04-04-mcp-protocol-explosion-zh"
  - "2026-04-11-shopify-ai-toolkit-agentic-commerce-zh"
---

# Mozilla 推出 Thunderbolt：開源自建企業 AI 用戶端，直攻 Copilot 與 ChatGPT Enterprise

Mozilla 的營利子公司 MZLA Technologies Corporation 週三宣布推出 Thunderbolt——一款開源、可自部署的企業 AI 用戶端，直接針對那些對員工使用 Microsoft Copilot、ChatGPT Enterprise 或 Claude Enterprise 時敏感數據的流向感到不安的組織。這項專案由 Thunderbird 電子郵件用戶端團隊打造，即日起在 GitHub 上線，自我定位為「在 AI 世界架設自己郵件伺服器」的等價物：設定難度更高，但一切真正掌握在自己手中。

這次發布是互聯網最具公信力的開源機構之一發出的重要訊號。Mozilla 每次進入一個市場區隔，通常都是因為它看到了商業玩家沒有動力解決的結構性問題。這次，問題是企業 AI 的數據主權——而時機，恰逢各國政府與企業都在加強對 AI 廠商數據實踐的審視，幾乎無法更精準。

## Thunderbolt 到底是什麼

Thunderbolt 最好理解為一個主權 AI 工作空間，而非一個聊天機器人包裝。它提供統一介面，用於 AI 輔助的對話、文件搜索與研究工作流程，連接企業內部數據來源，並在組織自選的模型後端上運行。

開箱即支援四家雲端 AI 供應商：Anthropic（Claude）、OpenAI（GPT 模型）、Mistral 及 OpenRouter。對希望將推論完全保留在本地的組織，它也透過 Ollama、llama.cpp 及任何 OpenAI 相容 API 端點支援本地模型執行環境——實際上意味著可以在完全不讓數據離開組織基礎設施的情況下，運行 Llama 4、Mistral 7B、Phi-4 或自訂微調模型。

企業數據連接層是 Thunderbolt 與消費者 AI 助理最鮮明的差異所在。它整合德國 deepset 的 Haystack 平台進行 AI 編排，讓組織得以將其連接至內部文件庫、資料庫和知識管理系統。使用 Thunderbolt 的員工可以針對公司實際的內部文件進行提問——而非搜索一般互聯網——並獲得基於組織自控來源的回答。

平台支援範圍從第一天起就相當廣泛：網頁應用，加上 Linux、macOS、Windows、iOS 和 Android 的原生版本。這對企業部署至關重要——IT 團隊需要一個能在異質裝置組合上無縫運作的統一用戶端，無需為每個平台另做 MDM 設定。

## Thunderbird 的傳承

Thunderbolt 從 Thunderbird 團隊孕育而生，並非巧合。Thunderbird——Mozilla 維護逾二十年的開源電子郵件用戶端——在企業軟體中佔據獨特地位：廣泛部署、深受信任，且組織選用它，正是因為它不將用戶通訊數據貨幣化。該團隊多年來積累了建立自部署、注重隱私的通訊工作流程的深厚經驗，Thunderbolt 是這種專業能力向 AI 領域的自然延伸。

MZLA Technologies 於 2020 年作為獨立法人成立，讓 Thunderbird 得以追求商業收入，同時不危及 Mozilla 基金會的非營利地位。這次的組織架構是刻意的鏡像——以營利載體推進商業 AI 產品，同時以開源核心確保更廣大的社群能夠稽核、擴展和自行部署。

程式碼以 Mozilla Public License 2.0 發布，這是一種著佐權授權，要求對 MPL 授權檔案的修改必須以同樣授權釋出，但允許在同一專案中將 MPL 程式碼與專有程式碼結合使用。相較於 GPL 更有利於商業使用，也顯示 MZLA 希望吸引企業貢獻和整合，同時不要求採用者公開其內部客製化內容。

## 主權論據

Thunderbolt 的發布時機，反映了企業 AI 採購兩年來正在醞釀的轉變。2024 年和 2025 年初，多數企業以極少的審查採用雲端 AI 工具——接受 Microsoft、Google 和 OpenAI 的標準數據處理協議後就繼續前行。進入 2026 年，情況已截然不同。

在 GDPR 下運營的歐洲企業面臨日益明確的法規（及執法）要求，涉及 AI 數據處理。美國醫療和金融服務公司眼見同業因透過商業 AI 服務處理病患和客戶數據而受到監管調查。多個國家的公共部門組織要麼直接禁止商業 AI 工具用於敏感工作負載，要麼正積極尋求替代方案。

對所有這些組織，Thunderbolt 提供的是主要雲端 AI 廠商無法真正給出的路徑：一個企業在字面意義上掌控整個技術堆疊每個環節的系統。模型權重可以在本地。推論可以在本地。對話記錄永遠不會離開組織自有的基礎設施。稽核人員問「這份數據去了哪裡？」能得到直接的答案。

MZLA 押注的是：這個細分市場——有真實主權需求、而非只是作秀式隱私偏好的企業——規模足夠大，且願意為企業支援和部署服務支付足夠多，以建立可持續的商業模式。該公司表示計劃透過企業部署取得收入，提供設定協助和託管支援，同時讓核心產品保持免費取用。

## 值得注意的限制

Thunderbolt 的公告附帶了誠實的注意事項，這在企業軟體發布中並不多見。產品仍在積極開發中，正在進行安全稽核，MZLA 明確表示尚未達到企業生產就緒狀態。今天就想部署的組織可以嘗試，但應預期仍有粗糙之處，且在安全稽核完成並標記企業穩定版本之前，不應用於高度敏感的生產工作負載。

這種透明度在企業軟體市場實屬罕見——廠商通常誇大成熟度以促成早期交易。Mozilla 選擇在生產就緒之前公告，很可能是務實之舉：趁資金充裕的競爭者（Slack、Notion 及多家新創據報正在打造類似產品）推出自家企業 AI 用戶端替代方案之前，先建立社群、吸引貢獻者、確立專案身份。

競爭格局是真實存在的。Microsoft Copilot 有 2.3 億企業用戶，ChatGPT Enterprise 已簽下數千家組織，Claude Enterprise 乘著 Anthropic 三百億美元年化營收的東風快速成長。Thunderbolt 正在進入一個與擁有巨大發行優勢、深度整合現有生產力套件、且搶先多年的在位者競爭的市場。

Thunderbolt 擁有那些在位者無法真正複製的東西：Mozilla 品牌與開放標準、用戶權利和長期維護開放基礎設施的關聯。對愈來愈多做出 AI 採購決策的資安長（CISO）、隱私主任和法遵團隊而言，這種品牌信任是任何行銷預算都無法製造的。

## 後續觀察重點

未來六個月將決定 Thunderbolt 能否找到真正的產品市場契合點，還是淪為一個技術上稱職、卻難以轉換開源信仰者以外用戶的專案。三個訊號值得關注：GitHub 上社群貢獻的速度與品質；是否有重量級企業——歐洲銀行、政府機關、醫療系統——公開宣布採用；以及 MZLA 能否在安全稽核完成、專案達到官方生產就緒狀態之前，先完成第一批企業支援合約的簽署。

Mozilla 曾打造過歷久彌新的產品。Thunderbird 至今仍有數百萬活躍用戶，Firefox 依然舉足輕重。若 Thunderbolt 能在企業 AI 用戶端市場達到類似的長期生命力，它將完成商業在位者永遠無法完美複製的一件事：讓 AI 技術堆疊的一個環節，真正掌握在使用它的組織手中。
