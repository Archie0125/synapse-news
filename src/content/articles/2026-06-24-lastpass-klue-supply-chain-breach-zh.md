---
title: "LastPass 再遭供應鏈入侵：Icarus 駭客組織透過 Klue 竊取 CRM 資料"
summary: "LastPass 於 6 月 23 日確認，Icarus 威脅組織竊取了第三方市場情報平台 Klue 的 OAuth 憑證後，進而存取其 Salesforce 環境中的客戶資料。此次外洩涉及企業客戶的 CRM 紀錄，但密碼保險庫並未受到波及。"
category: "products"
publishedAt: 2026-06-24
lang: "zh"
featured: false
trending: false
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/23/password-manager-maker-lastpass-says-hackers-stole-customer-support-case-data-during-klue-breach/"
  - name: "BleepingComputer"
    url: "https://www.bleepingcomputer.com/news/security/lastpass-confirms-data-breach-in-klue-supply-chain-attack/"
  - name: "Help Net Security"
    url: "https://www.helpnetsecurity.com/2026/06/24/lastpass-klue-data-breach-salesforce-environment/"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/lastpass-klue-supply-chain-breach-customer-data-stolen"
tags:
  - "LastPass"
  - "Klue"
  - "供應鏈攻擊"
  - "Icarus駭客"
  - "資料外洩"
  - "Salesforce"
  - "資安"
relatedSlugs:
  - "2026-05-25-github-nx-console-teampcp-supply-chain-attack-zh"
  - "2026-04-14-rockstar-shinyhunters-breach-zh"
---

LastPass——這家自 2022 年那次指標性資安事件後接連遭遇多起高知名度安全事故的密碼管理器——於 6 月 23 日確認，攻擊者存取了其存放在 Salesforce 環境中的客戶關係管理資料。入侵途徑，是透過供應鏈攻擊入侵了第三方市場情報平台 Klue。

此次入侵由名為 Icarus 的駭客與勒索組織執行，是企業軟體供應商淪為針對客戶攻擊跳板的一系列事件中最新的一起。LastPass 堅稱，其核心產品——加密的密碼保險庫——並未受到觸及。

## 攻擊是如何發生的

6 月 12 日，LastPass 收到通知，其業務拓展團隊用於競爭情報與客戶研究的 Klue 平台已遭入侵。Icarus 組織利用一個整合服務帳戶的舊式憑證漏洞，滲透進 Klue 的基礎設施——那是一個仍持有有效存取令牌、但已長期無人主動管理的休眠技術帳號。

進入 Klue 系統後，攻擊者取得了 Klue 代表客戶（包括 LastPass）持有、用於存取 Salesforce 與 Gong 整合的 OAuth 憑證。隨後，他們使用自動化的 Python 工具，對 Salesforce 物件進行枚舉，並執行數千次 API 查詢，大規模抓取 CRM 紀錄。

這次攻擊無需破解加密，也無需繞過多因素驗證。OAuth 憑證一旦被竊，在主動撤銷之前，其行為完全等同於合法憑證。Klue 的整合服務帳戶長期未輪換憑證，使這些令牌在帳戶停止主動管理後仍持續處於暴露狀態。

## 哪些資料遭到外洩

LastPass 將外洩資料描述為「標準業務聯絡資訊及相關 CRM 資料」，包括客戶姓名、電話號碼、電子郵件地址、實體地址、客服案例資料及銷售相關紀錄。公司表示，目前尚無法精確確認受影響的客戶紀錄數量。

關鍵是，LastPass 表示此次外洩不影響其產品基礎設施或存放實際密碼的加密保險庫。涉事的 Salesforce 環境是銷售與客戶成功系統，並非密碼管理器架構的組成部分。用戶的主密碼及存儲的憑證均未受到危害。

同一次 Klue 供應鏈攻擊中，其他確認受害的組織包括 Recorded Future、Tanium、Jamf、Sprout Social、Gong 及 Insurity——其中多家本身即是資安相關公司，為這次事件增添了一絲諷刺意味。

## Icarus 駭客組織與勒索威脅

Icarus 組織於 2025 年底首次現身，運營一個洩露網站，透過公布竊取資料向受害企業勒索。6 月 22 日，疑似源自 Klue 攻擊的資料開始出現在 Icarus 洩露網站，並向多家受影響公司提出要求。

LastPass 確認正與執法機關合作，已停用員工對 Klue 的存取權限，輪換所有暴露的 API 及 OAuth 憑證，並聘請事件回應專家評估外洩範圍。公司未確認是否收到具體勒索要求，也未表示是否有意付款。

分析洩露資料樣本的資安研究人員確認，相關紀錄外觀真實，與通過市場情報整合流通的企業 CRM 紀錄類型一致。

## 供應鏈安全盲點

Klue 事件是讓資安團隊日益憂慮的一種模式中最新的案例：企業資料的攻擊面，已不再終結於目標公司的邊界防線。每一個第三方整合——每一個銷售工具、HR 平台、市場情報資訊源或分析連接器——都是潛在的入侵切入點。

就 LastPass 的案例而言，公司持有的資料從定義上就具高度價值：其客戶是將憑證管理信任給它的大型企業。即便是關於這些客戶的 CRM 後設資料——他們是誰、曾有過哪些客服案例、公司電話號碼是什麼——對攻擊者而言，均可用於精準網絡釣魚、身份冒充或發動下一輪供應鏈攻擊。

2022 年的 LastPass 資安事件奠定了一個透過多階段、橫向構建的方式攻擊高價值目標的方法論：攻擊者最終透過鎖定一名開發者的家用電腦，存取到了加密的客戶保險庫。Klue 事件遵循了相似的邏輯：不從堅固的核心攻擊 LastPass，而是從一個監控較鬆的周邊整合入手。

## LastPass 的屢次外洩記錄

對 LastPass 而言，Klue 事件在聲譽上選擇了一個特別棘手的時刻降臨。2022 年的資安事件在媒體頭條上持續逾一年，事後分析揭示攻擊者竊取了加密的保險庫資料，若客戶使用弱主密碼，資料仍處於風險之中。2023 年隨後發生了憑證填充攻擊事件。

公司於 2021 年被 Francisco Partners 收購，此後以獨立實體運營，並自 2022 年起大力投資重建安全架構。此次最新的外洩——儘管就資料類別的敏感性而言不及從前——進一步強化了安全業界對 LastPass 仍是不成比例高度被針對組織的印象。

「這不是他們保險庫架構的失敗，」一位企業資安顧問表示。「但這是一個提醒：對這個品牌而言，任何安全事件帶來的頭條風險，都高於密碼管理器市場上幾乎所有其他人。當你的核心承諾就是安全，標準就是不一樣的。」

對企業 IT 團隊而言，眼前的行動清單清晰明確：審計持有 OAuth 令牌或 API 憑證、連接到內部敏感系統的第三方整合平台；確認整合服務帳戶受到與人工用戶帳戶同等的憑證輪換與監控政策約束；並確認授予市場情報和分析工具的存取範圍，已限制在業務所需的最低程度。
