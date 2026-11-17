---
category: ai-ml
featured: true
lang: zh
publishedAt: '2026-11-11T18:36:32.426880+00:00'
relatedSlugs: []
sources:
- name: Dev.to
  url: https://dev.to/tarikmostafa/why-standing-api-tokens-are-architectural-malpractice-the-case-for-ephemeral-single-action-15me
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/github-agentic-workflows-ga/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- name: TechCrunch
  url: https://techcrunch.com/2026/11/11/plurai-wants-to-help-ai-agents-work-better-using-the-same-approach-that-helped-get-self-driving-cars-to-roads/
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/qcon-ai-newyork-2026-program/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- name: The Verge
  url: https://www.theverge.com/tech/1030838/ebay-ai-agents-meta-muse-agentic-shopping
summary: 模型已經夠聰明，真正卡關的是權限、身分和平台的門票。eBay 剛示範了誰才能決定代理能走多遠。
tags: []
title: AI 代理上線了，卻沒人敢把鑰匙交給它
trending: true
type: analysis
---

GitHub 這次把 Agentic Workflows 推到正式版，最值得注意的不是代理能做什麼，而是它被刻意設計成**做不到**一件事：直接寫進你的 repo。

10 月 28 日 GA，距離 6 月公開預覽只隔四個月。全球最大的開發者平台推出旗艦級代理產品，結果代理預設只有唯讀權限。它提出的修改要先經過一個威脅偵測 job 掃描，再交給另一個持有自己寫入 token 的 job 執行。代理本身關在沙箱容器裡，外面還有一層 GitHub 稱為 Agent Workflow Firewall 的防火牆。

這是今年最誠實的產品設計，也說明了「AI 代理正式上線」目前真正的狀態。2025 年大家在問代理夠不夠聰明，到了 2026 年底，問題變成：你敢不敢把憑證交給它？多數正式環境的答案是不敢，所以代理的產出一律先經過一道閘門才會生效。

## 能力的落差，遠小於信任的落差

先看數字。LiveBench 2.0 的長流程代理任務中，Claude Fable 5.2 完成 82.9 題（滿分 100），ChatGPT-6 Astra 是 75.6。AI 基礎設施公司 EON 在模擬企業環境裡測試，表現最好的 Claude Opus 4.8 準確率 76.8%。

八成多聽起來不錯，但正確率會連乘。一個流程串五個步驟，每步 83%，整條流程跑完只剩約 39%。所以 GitHub、Figma、LinkedIn、DoorDash 這些認真上線的團隊，都把代理定位成**提案者**而不是**執行者**。修正、標籤、退款都由代理起草，真正按下執行鍵的是一段可預測的程式碼。

這樣設計是對的。ChatGPT Business Agents、Adobe 的 MCP server、Meta 的 Muse Ember 都在推「代理就是新介面」，但一個五次錯一次的介面，需要的是確認按鈕，而不是更多自信。這就像網銀轉帳：你很信任自己，銀行還是要你輸入 OTP。

## GitHub 的護欄，告訴你風險在哪

GitHub 的計費設計把代理的成本攤開來看。AI Credits 一點 0.01 美元，每次執行預設上限 1,000 點（10 美元），每個 workflow 每天 5,000 點（50 美元），威脅偵測每次 400 點，代理步驟 20 分鐘就逾時。`gh aw forecast` 指令已經脫離實驗階段，可以預估每月花費。說白了，GitHub 把代理當成按時計費的外包，人不在旁邊就不能拿公司卡。這樣的定位很準確。

但 GitHub 自己也承認了幾件事。官方 FAQ 寫明，唯讀和寫入分離的保護**不會自動套用**到直接賦予的寫入權限，也不會套用到作者自己加的 custom job。預覽期之後新增的 Actions Runner Controller（ARC）搭配 Docker-in-Docker，DinD sidecar **預設以特權容器執行**。也就是說，一個照最小權限原則設計的代理，旁邊就坐著整個 pod 權限最高的元件。

再看發表會的推薦語。Accenture 的 Ben Alton 說，有位主管「估計每週省下 29 小時」。GitHub 沒說這個數字怎麼量出來的，沒有方法的數字只是說法，不是數據。

歷史上有前例。2021 年 Codecov 的 Bash uploader 被竄改，攻擊者從數千條 CI pipeline 偷走環境變數。2023 年 1 月，CircleCI 要求所有客戶輪換全部 secrets。這兩起事件裡的 pipeline 都是人寫的、行為可預測。現在 pipeline 裡多了一個語言模型，而它在 issue triage 的工作就是讀陌生人寫的文字，本質上就是在處理不可信的輸入。如果跟它跑在同一台機器上的是一把全組織通用的 token，下一個 Codecov 事件只是早晚的事。

## 長效 token 才是定時炸彈

Dev.to 這週有篇文章說得很直接：寫在 prompt 裡的規則不是資安邊界。很多台灣團隊的做法跟 2016 年寫 cron job 一模一樣：`.env` 塞一把 `STRIPE_SECRET_KEY` 或 org 等級的 `GITHUB_TOKEN`，system prompt 寫「只能動 staging」，然後就上線了。只要出現一次 prompt injection、一份外洩的 stack dump 或一個失控的重試迴圈，那把 token 能做的事，代理全都能做。

文章提出的解法是在代理的程序之外放一個 broker。每次只核發一張針對單一動作、單一目標的短效簽章授權，執行前先消耗 nonce，代理程序從頭到尾碰不到真正的上游密鑰。GitHub 的唯讀代理加寫入 job，就是這套概念的粗略版本。

這裡有個很少人討論的角度：**代理身分會是下一個大型企業資安市場，大廠都已經看到了。** 12 月 15 日 QCon AI New York 第一天的開場主講人，是 1Password 的 CTO Nancy Wang，題目是當軟體變成使用者時，身分和授權該怎麼做。她的論點是：現有身分系統都假設憑證背後有一個人，這個人有固定角色、有範圍明確的 session、事後有人負責，而代理一樣都沒有。OAuth 2.0 在 2012 年標準化，是為了讓 app 代替人存取資料，scope 很粗，一給就是好幾週。代理需要的是每個動作各自授權、毫秒內核准、用完自動失效。最後誰做出這一層 broker，不管是 1Password、Okta、CyberArk，還是一家還沒人聽過的新創，就會變成代理時代的 Okta。

## eBay 擋的不是機器人，是在守自己的店面

另一個難題是平台准不准代理進門，而這完全不是技術問題。

The Verge 的一位讀者連續幾週用 Meta 的 Muse 整理 eBay 上的手錶清單，每天一份摘要，有連結、價格、運費和成色說明。某個週末開始，Muse 說它被 eBay 擋了。eBay 在 2026 年 1 月就已經修改使用者條款，禁止「buy-for-me 代理」和「LLM 驅動的機器人」未經人工確認就下單。現在連瀏覽似乎都被擋。Amazon 完全封鎖外部代理，Target 則是有時能進、有時被擋。eBay 發言人的說法是對第三方採取「選擇性的做法」，而且「正在和潛在合作夥伴討論」。

這句話要當成談判訊號來讀。電商平台靠人的注意力賺錢，廣告版位、推薦商品、加購都是。代理直接回答「500 美元以下最值得買的三支錶」，這些營收全部被跳過。eBay 並不反 AI，它自己在搜尋、推薦和賣家工具裡大量導入 AI。它反對的是自己控制不了的 AI。台灣讀者應該很熟悉：比價網跟電商之間一直是又需要又提防的關係，代理只是一個更聰明、更難擋的比價網。蝦皮、momo、PChome 遲早也得決定要不要讓代理進門，以及要收多少錢。

更麻煩的是後續效應。Muse 被擋之後，有時會**把使用者導到轉貼 eBay 商品的鏡像網站**。封鎖沒有讓代理停下來，只是逼它去更爛的資料來源：價格過時、賣家不明，頁面裡還可能藏著 prompt injection。使用者拿到更不可靠的資訊，eBay 自家商品的流量也被別人拿走。

這劇本以前演過。Twitter 在 2012 年限制第三方客戶端，Reddit 在 2023 年調漲 API 價格，逼停了 Apollo。平台需要成長時開放，有了籌碼就關門收費。這一輪的第三方客戶端，就是 AI 代理。

## 看空的理由，對了一半

懷疑論者說，「代理上線」大多是行銷話術。GitHub 主打的場景是 issue triage 和 CI 失敗分析，風險低、以讀取為主、出錯也能還原。訂機票的代理遇到客戶施壓，還是會無視差旅規定；客服對話一拉長，context 照樣爆掉。

這是現況的準確描述，但不能拿來預測未來。以色列創投 Team8 領投了 Plurai 1,300 萬美元的種子輪。Plurai 的創辦人來自自駕公司 Nexar，其中一位曾和 Waymo 合作做駕駛模擬。他們的做法是幫企業系統建一個數位分身，把代理所有可能走的路徑畫成圖，再逐一測試邊角案例。自駕車就是這樣，從 2005 年 DARPA 挑戰賽走到 2020 年 Waymo 在鳳凰城開出無人計程車：先在模擬裡跑上數十億英里，才上真正的馬路。營運層面也在進步，Figma 用 warm pool 把代理的啟動延遲砍了 90%，可用性從 99% 拉到 99.95%。

看空派說對的那一半是：從唯讀代理走到能交易的代理，需要的是好幾年，不是幾季，而決定速度的是身分和權限系統，不是模型。

## 值得關注

1. **2027 年年中前，eBay 或另一家美國前十大電商推出付費的認證代理存取方案。**「和潛在合作夥伴討論中」講的就是價格，代理存取會像 API 一樣計價販售。
2. **2027 年底前，出現第一起公開揭露的資安事件：issue 或 PR 裡的文字誘使代理 workflow 外洩長效 token。**受害的會是自己加了 custom write job 的團隊，正好落在 GitHub FAQ 寫明不保護的範圍。
3. **GitHub 在接下來兩個大版本內，把 ARC 的沙箱預設改成 rootless 或非特權模式。**最小權限的代理旁邊放一個特權 DinD sidecar，這個破綻太明顯，不會放太久。
4. **代理 broker 成為企業採購資安問卷的標準題目。**預期 1Password、Okta、CyberArk 會在 12 個月內推出針對代理的逐動作憑證產品。台灣金融業和大型電商的資安長，明年的預算表上會多這一行。
5. **類似 GitHub 單次 10 美元的預算上限，會成為各家代理平台的標配。**代理的花費會像雲端帳單一樣，由 FinOps 團隊盯著管。