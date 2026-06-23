---
title: "Fable 5 免費時代結束：Anthropic 將旗艦模型移至使用點數制"
summary: "從 2026 年 6 月 23 日起，Claude Fable 5 不再納入 Pro、Max、Team 及 Enterprise 訂閱方案。用戶現需購買使用點數，費率為每百萬輸入 Token $10、每百萬輸出 Token $50，是 Opus 4.8 的兩倍。原定 13 天免費試用期因美國出口管制暫停，實際可用天數僅約 4-5 天，大量用戶表達不滿，但 Anthropic 迄今未回應補償問題。"
category: "ai-ml"
publishedAt: 2026-06-23
lang: "zh"
featured: false
trending: true
sources:
  - name: "TechCrunch — Anthropic releases Claude Fable 5"
    url: "https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/"
  - name: "Claude Fable 5 Free Access Window: June 9–22"
    url: "https://claude5.ai/en/news/claude-fable-5-free-access-june-9-22-pro-max-team-enterprise"
  - name: "MindStudio — Claude Fable 5 Pricing, Access, and Usage Limits"
    url: "https://www.mindstudio.ai/blog/claude-fable-5-pricing-access-usage-limits"
  - name: "Hacker News Discussion — Fable 5 Usage Credits"
    url: "https://news.ycombinator.com/item?id=48463982"
tags:
  - "anthropic"
  - "claude"
  - "fable-5"
  - "定價"
  - "使用點數"
  - "AI模型"
  - "訂閱"
relatedSlugs:
  - "2026-06-10-anthropic-claude-fable-5-public-release-zh"
  - "2026-06-16-claude-fable-5-mythos-5-us-government-shutdown-zh"
  - "2026-06-22-freefable-400-experts-challenge-us-fable-mythos-ban-zh"
---

免費窗口關閉，Fable 5 正式進入付費時代。從 2026 年 6 月 23 日起，Anthropic 迄今為止最強大的公開 AI 模型不再包含在標準訂閱方案內。使用 Claude Fable 5，需要另行購買使用點數，計費方式與 API 開發者定價相同。

費率清楚但不便宜：**每百萬輸入 Token $10，每百萬輸出 Token $50**——恰好是 Claude Opus 4.8 的兩倍。對於有大量重複上下文的應用場景，快取輸入可享 90% 折扣（每百萬 Token 降至 $1），但對一般對話場景而言，成本差距是直接且明顯的。Anthropic 表示計畫「盡快」將 Fable 5 恢復為標準方案功能，但沒有給出時間表。

## 名存實亡的 13 天免費期

這次轉換之所以讓人不滿，是因為原本宣傳的 13 天免費窗口，實際上縮水得相當嚴重。Fable 5 於 6 月 9 日正式推出。四天後，也就是 6 月 12 日，美國政府的出口管制令將 Fable 模型全線下架——這是一項針對性措施，目的是防止 Fable 的先進科學推理能力流入敵對國家，但命令範圍涵蓋了所有地區，包括美國本土用戶。直到約 6 月 18 日模型才恢復上線，這意味著訂閱用戶在承諾的近兩週免費期內，實際僅享有約**四到五天**的可用時間。

這一落差在開發者社群中引發強烈反彈。Hacker News 和 Reddit 的 r/LocalLLaMA 討論串中，不少人批評 Anthropic 的溝通方式不夠透明：沒有按比例退款、沒有延長免費期、也沒有公開承認用戶實際獲得的存取遠少於原始承諾。部分企業團隊已將 Fable 5 整合進內部工作流程，卻在衝刺週期中被迫臨時切換替代方案。

Anthropic 的公開回應十分有限。狀態頁面記錄了暫停及恢復的時間點，但公司對於是否認為用戶已獲得充分補償，始終未有正面表態——而這個問題在 Anthropic 準備赴美上市的節骨眼上，格外引人關注。

## Fable 5 是什麼，不是什麼

Fable 5 是 Anthropic Mythos 模型系列的消費者版本。完整的 Mythos 5 仍保留在更高的存取層級，Anthropic 內部描述其接近現有安全框架在大規模部署下所能可靠治理的邊界。Fable 5 是為廣泛部署設計的受約束版本，搭載一套特定的安全回退機制：在高風險領域——包括資安、生物、化學和模型能力萃取——它會悄悄切換到 Claude Opus 4.8，而非以完整能力作答。根據 Anthropic 的數據，這一回退在不足 5% 的真實對話中被觸發。

即使如此，Fable 5 的實際效能仍顯著超越訂閱方案中以往提供的任何模型。它在 **SWE-bench Pro**（倉庫級軟體工程基準測試）上得分 80.3%，高於 GPT-5.5 的 74.1% 和 Gemini 3.5 Pro 的 72.8%。在數學推理任務上，其領先 Opus 4.8 的幅度約達 18 個百分點。在長篇文本分析與綜合——最能體現知識工作者每次對話價值的場景——人類評估者一致認為其輸出更準確、結構更嚴謹。

## Anthropic 為何計量收費

Anthropic 的算力現況比任何商業考量都更能解釋這次付費牆的設立。Fable 5 每個輸出 Token 消耗的算力估計約是 Opus 4.8 的兩倍。在用戶量爆炸成長的時期，對數百萬 Pro 訂閱用戶免費提供這樣一個模型，造成了公司顯然無法長期承受的供需失衡。

Anthropic 的基礎設施擴充正在推進，但需要時間。公司已簽署超過 12 份美國數據中心直租意向書，總容量超過 1 吉瓦，Alphabet 透過與 Anthropic 合作設計部分晶片的結構為此提供財務擔保。但已簽約的容量與可用容量不是同一回事——這批算力要真正上線，還需要數個月。

## 競爭格局的脆弱點

付費牆讓 Anthropic 在競爭中處於結構性不利位置。OpenAI 的 **GPT-5.5** 仍包含在每月 $200 的 ChatGPT Pro 訂閱中，沒有額外計量費用。本週進入正式開放窗口的 Google **Gemini 3.5 Pro**，則隨 $250/月的 Ultra 方案附上 200 萬 Token 的上下文窗口——這是 Fable 5 目前無法匹配的規格。兩家競爭對手都比使用點數計費更具預算可預測性，這對多數中型企業團隊而言是關鍵優勢。

開源生態系已在吸收部分被轉移的需求。本週稍早推出的 **智譜 GLM-5.2**，在多項標準評測上的得分據稱與 GPT-5.5 相近，且以更低的算力成本運行。六月的 Fable 5 政府暫停，已驅動企業對開源權重模型的評估量明顯增加——單靠恢復供應並不能完全逆轉這一趨勢。

## IPO 前的揭露義務

在用戶體驗不滿之外，還有一個更深層的問題。Anthropic 於 6 月 1 日秘密向 SEC 提交 S-1 草稿，目標是在 10 月以 9650 億美元後估值完成上市，年化營收約為 470 億美元。Fable 5 的出口管制暫停事件——以及 Anthropic 在處理訂閱用戶期望時的方式——屬於 S-1 起草方必須揭露的重大風險因素。

審視 Anthropic 招股說明書的投資人將會追問：政府 AI 出口管制未來可能再度限制部署的情境有多大、此類限制的頻率和範圍作為一類風險應如何評估，以及 Anthropic 的訂閱營收是否結構性地易受政府強制下架的影響。六月暫停期間公司的溝通處理，將是任何此類分析的核心案例。

## 現在該怎麼辦

對於現有訂閱用戶，今天的變更不需要任何主動操作——沒有點數餘額時，Fable 5 選項將不再顯示。Anthropic 控制台支援從 $10 起步的點數儲值。Fable 5 的 API 端點保持不變；呼叫照常進行，只是從訂閱配額改為扣除點數餘額。

對於已將 Fable 5 整合進生產工作流程的開發團隊而言，成本變化才是核心運營課題。處理大量 Fable 5 工作負載的團隊——長上下文文件處理、密集程式設計任務、多輪推理鏈——在決定是否繼續使用之前，需要對照新的 Token 費率測算實際消耗。

Anthropic 尚未表明 Fable 5 是否或何時會永久回歸方案內功能。最可能的觸發條件是其數據中心建設完工——當 Anthropic 自有算力能夠在不受基礎設施瓶頸制約的情況下承載旗艦模型需求，計量計費的必要性才會消失。

在那之前，Fable 5 是一項溢價選擇，具體代價取決於你如何使用它。
