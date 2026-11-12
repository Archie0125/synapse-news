---
category: ai-ml
featured: true
lang: zh
publishedAt: '2026-11-12T06:28:32.843094+00:00'
relatedSlugs: []
sources:
- name: 9to5Google
  url: https://9to5google.com/2026/11/11/android-auto-gemini-intelligence-pixel/
- name: 9to5Mac
  url: https://9to5mac.com/2026/11/11/google-confirms-gemini-app-coming-to-apple-carplay/
- name: Engadget
  url: https://www.engadget.com/2314093/google-brings-the-gemini-app-to-apple-carplay/
- name: Google AI Blog
  url: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/
- name: 9to5Google
  url: https://9to5google.com/2026/11/11/gemini-app-carplay/
summary: 當各家模型的跑分領先只撐得了六週，Google 改賣「到處都有、而且便宜」，從你的車到你的信箱全包。
tags: []
title: Gemini 不必最聰明，只要你躲不掉：Google 的 AI 圍城戰
trending: true
type: analysis
---

先講結論：Google 看起來已經不打算追「全世界最聰明的模型」這個頭銜了。

這不代表 Google 認輸，而是它看懂了一件事：前沿模型的跑分領先，大概撐六週就會被別家追上。所以它把力氣轉向兩個對手很難複製的東西：價格，以及無所不在的通路。這個月一連串的發表都在講同一件事：Gemini 4 Carbon 主打 agent swarm（代理群）和更低的單任務成本，Gemini 上了 Apple CarPlay，Android Auto 加入 Pixel 限定的主動建議，加上新一波 Pixel Drop，以及醫療、Adobe 的整合。拆開看都是小新聞，合起來看，Google 正在用 AI 業界最大的通路網把對手圍起來。

這套打法很聰明，但也有幾個 Google 新聞稿不會提的破口。

## 最後一個進場的，偏偏是 Google

先看 CarPlay 的時間軸，很有意思。ChatGPT 在 2026 年 3 月 31 日隨 iOS 26.4 登上 CarPlay，Perplexity 4 月跟進，Grok 5 月，到 9 月 4 日 Claude、Copilot、Meta AI 也全部上架。Android Auto 的老闆 Google 反而是**最後一個**推出獨立 CarPlay App 的主流 AI 助理。在這之前，iPhone 用戶只能透過 Google 地圖間接用到 Gemini。

11 月 11 日起，完整的 Gemini Live 開始在全球 CarPlay 推出，所有支援 Gemini Live 的語言都能用。對話可以隨時插話打斷，紀錄和 iPhone App 同步。Google 自己舉的使用範例很說明問題：「幫我整理未讀信件，摘要 Sarah 那串 Q4 預算討論」、「幫我準備十點跟設計團隊的會」。

這些例子跟開車都沒什麼關係，全是 Gmail、日曆這類 Workspace 的使用情境，車只是換了個地方用而已。ChatGPT 在車上也能陪你聊，Claude 也行，但它們沒辦法直接打開你的 Gmail、查你的 Google 日曆、翻出你上週二收到的訂位確認信。這是 Gemini 的優勢：資料本來就在 Google 手上。當中控螢幕上同時有八個 AI 圖示時，能直接讀你信箱的那一個最有機會被點開。

台灣讀者對這點應該很有感。iPhone 在台灣的市占長期接近一半，CarPlay 幾乎是新車標配，從 Toyota、Honda 到 Luxgen 都有。另一方面，很多台灣上班族公司用 Outlook、私人用 Gmail，行事曆散在兩邊。Gemini 在車上能幫上多少忙，取決於你的生活有多少放在 Google 帳號裡。

## Pixel 限定：同一家公司的兩副面孔

再看 Google 在自家平台上怎麼做。同一天，Google 宣布 Android Auto 上的 Gemini Intelligence 主動建議**只開放給 Pixel 10 和 Pixel 11**。官方情境是：朋友傳訊息問皮拉提斯課在哪裡上，Gemini 自動找出確認信，建議你一鍵把地址傳過去。

所以在蘋果的平台上，Google 是開放、中立、誰都能用的好鄰居；回到自己的平台，最好的功能卻只留給自家手機。這不算矛盾，而是兩套劇本同時進行：在 iOS 上 Gemini 要搶使用者注意力，在 Android 上 Gemini 是用來賣 Pixel 的。

接下來的影響是：Android Auto 過去十年最大的價值，就是不管你用三星、小米還是 OPPO，體驗都差不多。一旦最好用的車用功能要看手機品牌，Android Auto 就會變得跟 Android 平板一樣破碎。台灣的情況更明顯：Pixel 在台灣的市占很小，路上開車的 Android 用戶大多拿三星。說來諷刺，Pixel 的硬體研發有一大塊在新北板橋，就是 2018 年 Google 用 11 億美元從 HTC 買下的那支團隊。台灣人設計的手機，在台灣卻沒多少人用。我的判斷是，12 個月內三星旗艦機會透過談判拿到這個功能，而在那之前，三星會加碼推自家的 Galaxy AI 車用功能。

## 沒人在聊的重點：每百萬 token 0.10 美元的「決策器」

這個月最重要的發表反而最少人注意：**Gemini Decisions API**，背後是新模型 Gemini Decision 1。

它不寫文章，只做選擇題。你丟一份多模態輸入（文字、圖片、音訊、影片、PDF，最多 256K token），再附上最多 1,000 個獨立問題，題型可以是是非題、2 到 255 個選項的選擇題，或評分量表。它用一次前向運算替所有選項打分，回傳經過校準的機率和 0 到 1 的信心分數，端到端延遲 150 到 250 毫秒。價格是**每百萬輸入 token 0.10 美元，輸出 token 完全不收費**。Google 說在同一套測試裡，成本比用 Gemini 3.5 Flash-Lite 做同樣的事便宜將近 5 倍。

這件事為什麼重要？要先看懂 AI agent 系統實際上把錢花在哪裡，包括 Gemini 4 Carbon 主打的代理群。大部分運算不是在生成漂亮的文字，而是在做大量的小判斷：要呼叫哪個工具、這個任務交給哪個子代理、這份結果有沒有違反政策、撈回來的文件相不相關、這個案例信心不夠要不要轉給真人。這些本質上都是分類題。但現在多數公司的做法，是叫一個完整的生成式模型「想一想，然後輸出『是』或『否』」，為了一個位元的答案付整段推理加輸出的錢。

Google 要把這一層變成跟水電一樣便宜的基礎設施。拿保險理賠來說，一份掃描的理賠 PDF 配上車損照片，一次問 40 個問題，成本不到一美分，四分之一秒內回覆。Google 自己舉的例子是把客服通話錄音和帳戶資料放在一起判斷，目標顯然是企業客服市場。台灣的保險業、銀行客服、電商退貨審核，都是這類 API 的潛在大客戶。

Gemini 4 Carbon 敢主打「單任務成本更低」，關鍵就在這裡。路由幾乎不用錢，同一個任務就能開更多代理，帳單也不會爆掉。OpenAI 和 Anthropic 的前沿模型很強，但都是按生成的 token 計費；Google 打的是那次昂貴呼叫周邊的所有成本。AWS 當年就是這樣贏下雲端：不是靠最強的伺服器，而是把周邊服務做得夠便宜，便宜到搬走比留下來還貴。

## 唱反調：通路救不了 Google 的前例多得是

公平起見，無所不在不代表會被選上，Google 自己就證明過好幾次。

Google Assistant 2016 年推出，裝在幾十億台 Android 手機、智慧音箱和車上，最後還是沒變成一門好生意，現在正被 Gemini 取代。Allo、Duo、Google+、Stadia 背後都有龐大的通路，全都收掉了。Bard 在 2023 年 2 月推出時有 Google 搜尋撐腰，消費者心中的位置還是輸給完全沒有通路的 ChatGPT。

在 CarPlay 上，Gemini 只是八個圖示裡的一個，蘋果自己的 Siri 在 iOS 27 已經獨立成 App，而且是系統層級的預設。被放上螢幕不等於有人用。ChatGPT 的消費者品牌還是比較強，大多數人通勤時會打開的，是在辦公桌上已經習慣用的那一個。

還有一個結構性的問題：Apple 已經跟 Google 合作，用 Gemini 模型驅動新版 Siri。如果車上的 Siri 底層其實就是 Gemini，那 CarPlay 上的 Gemini App 等於在跟系統內建的 Gemini 搶用戶。Google 兩邊都有錢賺，但 Gemini 這個品牌是在跟自己打。

## 車廂裡的隱私問題

這是整套戰略最脆弱的地方。Gemini 在車上的價值，建立在讀取你的信件、日曆、訊息，以及在密閉車廂裡聽你說話。很多人會在車上講薪水、健檢報告，甚至跟另一半吵架。Google 的隱私說明一直寫得很清楚：會有真人審查員抽樣閱讀 Gemini 對話，被審查過的對話最多可保留三年，並建議用戶不要輸入不想讓審查員看到的內容。

這個提醒在手機上還說得過去，因為打字是有意識的。到了車上就很難成立：你會自言自語，Google 的行銷文案還鼓勵你「模擬一下 Q4 提案，你扮演難搞的副總」、「幫我準備一場困難的對話」。再加上醫療整合，「使用情境感覺很私密」和「資料其實有人在看」之間的落差，大到監管單位很難不注意。Gemini 出現在愈多地方，這個問題就跟著出現在愈多地方。

## 值得關注

- **2027 年第四季前，三星旗艦機會拿到 Android Auto 的 Gemini Intelligence。** 在三星的手機出貨量面前，Pixel 獨佔撐不了太久。
- **OpenAI 會在半年內推出對打的分類或決策端點**，定價壓到每百萬 token 0.10 美元以下。AI 的低價路由之戰即將開打。
- **2027 年會有歐洲資料保護機關對 Gemini 的真人審查機制展開調查**，焦點是車內語音和醫療資料，愛爾蘭 DPC 最有可能。
- **未來兩季財報內，Gemini App 月活躍用戶會突破 10 億**，而且 Google 會把成長主要歸功於 Android 和 Workspace 的整合，而不是 App 下載。
- **車上最常被使用的 AI，會是本來就連著你信箱的那一個。** 這對 Google 有利，除非 OpenAI 自己做出一套像樣的郵件加行事曆產品。