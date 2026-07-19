---
title: "Cursor 洩露「Honeycomb」代號——Anthropic 的 Opus 5 近在眼前"
summary: "7 月 8 日，一個名為「Claude Honeycomb EAP」的神秘模型短暫出現在 Cursor 的生產環境模型選單中，揭示了百萬 token 上下文視窗與「xhigh」推理層級。隨著 Fable 5 免費訂閱期今日到期，所有跡象指向 Anthropic 下一代前沿模型即將在數日內亮相。"
category: "ai-ml"
publishedAt: 2026-07-19
lang: "zh"
featured: true
trending: true
sources:
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/320265/20260712/fable-5-free-through-july-19-anthropic-blinks-again-opus-5-leak-surfaces-cursor.htm"
  - name: "The New Stack"
    url: "https://thenewstack.io/fable-5-honeycomb-opus/"
  - name: "WinCentral"
    url: "https://thewincentral.com/claude-opus-5-leak-1m-context-window-launch/"
  - name: "Valletta Software"
    url: "https://vallettasoftware.com/blog/post/claude-opus-5-release-date"
  - name: "KuCoin"
    url: "https://www.kucoin.com/news/flash/anthropic-preparing-claude-opus-5-for-potential-release-this-week"
tags:
  - "Anthropic"
  - "Claude Opus 5"
  - "Honeycomb"
  - "AI 模型"
  - "前沿 AI"
  - "Cursor"
relatedSlugs:
  - "2026-07-07-anthropic-fable5-exits-subscriptions-billing-change-zh"
  - "2026-07-17-anthropic-blackstone-ode-ai-implementation-zh"
  - "2026-07-18-anthropic-ipo-roadshow-october-2026-zh"
---

十一天來，AI 開發者社群不斷分析一張存在不到一小時的截圖。7 月 8 日，一位 ID 為 @chetaslua 的開發者在 X 上發布了一張看似普通的 Cursor 模型選單截圖，但其中一個選項顯示為「Claude Honeycomb EAP」。數小時後，這個字串消失無蹤。Anthropic 保持沉默。然而 AI 圈子卻花了整整一週做它最擅長的事：從每個像素中提取訊號。

今天，7 月 19 日，Fable 5 的免費訂閱存取將於太平洋時間晚間 11:59 到期。無論 Anthropic 下一步是發布 Opus 5、第四次延長免費期，還是將用戶轉移至按量計費，答案都將在數小時內揭曉。Honeycomb 洩露不只透露了一個模型代號，更可能告訴我們那個模型究竟是什麼。

## Cursor 洩露揭示了什麼

關於 Honeycomb EAP 模型，有三個事實獲得多份獨立截圖與開發者陳述的佐證。第一，上下文視窗顯示為 100 萬 token，與 Anthropic 為 Fable 5 擴展上下文層級推出的 200 萬 token 相比稍低，但已屬標準層級的頂端。第二，該模型支援「xhigh」推理設定——比當前 Claude API 中可用的「high」層級再高一級，暗示思維鏈深度遠超現有 Opus 4.8 的表現。第三，當觸發安全機制時，備援模型是 Claude Opus 4.8 而非 Fable 5，這種架構選擇意味著 Honeycomb 在產品線上介於 Opus 4.8 與 Fable 5 之間，正是 Opus 5 應該落腳的位置。

「EAP」標記（早期存取計畫）與 Anthropic 在 6 月 30 日公開發布前，內部為 Claude Sonnet 5 使用的標籤相同。這個模型字串未出現在 Anthropic 任何公開 API 文件、claude.ai 界面或 Claude Code CLI 中，符合一個在部署失誤中意外進入生產端點的預發布工程預覽版的特徵。

## 三次延期與一個規律

Anthropic 對 Fable 5 訂閱期的處理方式頗為反常。6 月 9 日，Claude Fable 5 與 Claude Mythos 5 一同推出，定位為 Anthropic 有史以來最強大的公開模型，定價方案包含限時免費試用期。原訂截止日是 7 月 7 日，後延至 7 月 12 日，再延至 7 月 19 日。每次延期都只給出「社群反饋」或「過渡支援」等模糊說明，但每次也都恰好與競爭對手新模型上線或 Anthropic 自身發布時程出現變動的時機吻合。

業界觀察人士指出，這些延期看起來與其說是慷慨，不如說是時程管理。7 月 9 日 OpenAI 的 GPT-5.6 Sol 上線後，Fable 5 的免費期隨即延長，似乎是直接應對競爭壓力的舉措。7 月 19 日是最後的硬性截止日，而 Anthropic 已無路可退：要麼推出下一個模型，要麼讓訂閱者接受隨後的按量計費。

Metaculus 與 Manifold 等預測市場截至 7 月 17 日的資料，將七月下旬至八月初列為 Anthropic 新前沿模型最可能的發布視窗，且不是 Fable 5 等級，而是更高一層。Honeycomb 這個代號未出現在任何過去的 Anthropic 溝通中，與該公司在開發期間使用有機感代號、正式發布時改用「Claude [層級] [版本]」命名規則的一貫做法吻合。

## Opus 5 為何舉足輕重

7 月以來的一系列發布讓前沿模型競爭格局空前擁擠。OpenAI 的 GPT-5.6 Sol 於 7 月 9 日全面上線，在長程代理任務基準上表現出色，且基礎層定價僅為每百萬輸入 token 1 美元，攻擊性十足。xAI 的 Grok 4.5 同期推出，在程式碼生成上尤為突出。Moonshot AI 的 Kimi K3 是一個開放權重模型，於 7 月 17 日發布後數小時內登頂前端程式碼競技場排行榜，這對開放權重模型而言是一個里程碑式的時刻。

在這樣的背景下，Anthropic 以「迄今最強公開模型」身份推出的 Claude Fable 5，正面臨一種微妙的處境：它在多項基準上仍屬一流，尤其是長篇推理與安全對齊，但競爭差距在不到六週內已明顯縮小。Opus 5 的發布將重新拉開這一差距，至少在基準測試上如此，並向許多基於 Anthropic 路線圖簽署合約的企業客戶傳遞出一個訊號：Anthropic 的研究速度仍在軌道上。

更重要的是，洩露的 xhigh 推理層暗示 Opus 5 可能是 Anthropic 對 OpenAI o 系列與 Google Deep Think 模式所引領的「延伸思維」趨勢的回應。Fable 5 的並行推理是重大的架構創新，但若 Honeycomb 在現有 Fable 5 基礎上新增持續多步驟深度推理模式，Claude 在複雜、長週期代理任務上與競爭對手之間的差距可能將再度顯著拉大。

## 值得關注的重點

Anthropic 對 Honeycomb 至今沒有任何公開回應。該公司的慣例是在新聞室公告與 API 文件同步更新的同一時刻發布模型，不設預告期——這使任何時間線預測本質上都帶有不確定性。可以確定的是產品日曆：Fable 5 免費存取今日到期，接下來的一切從今晚開始。

對開發者而言，最關鍵的問題在於 Honeycomb 將以有限 EAP 形式亮相，還是直接以完整 API 釋出。7 月 8 日出現在 Cursor 生產環境選單——這是一個合作夥伴整合，而非 Anthropic 自身的介面——暗示這個模型在外部測試上的進展可能遠比 Anthropic 在發布前通常承認的程度更為成熟。Cursor 基於其與 Anthropic 的密切整合關係，在獲得 Sonnet 5 擴展容量合作協議後，自然成為 EAP 洩露最合理的第一個出口。

如果 Honeycomb 確實在本週上線，它將進入一個自 Anthropic 上次主要前沿發布以來已大幅改變的市場。Kimi K3 的開放權重衝擊，以及 7 月 24 日即將到來的 DeepSeek V4 權重釋出，意味著封閉式前沿模型如今不僅需要在基準上勝出，還必須展現用戶無法透過本地模型獲得的實際價值主張。Anthropic 的賭注——隱含於 Fable 5 架構中，可能在 Opus 5 中進一步放大——是對齊品質、長上下文連貫性與代理可靠性才是企業買家最在乎的維度。在每月零成本的開放權重模型登頂程式碼競技場的世界裡，這個賭注是否站得住腳，未來數天或許將開始給出答案。
