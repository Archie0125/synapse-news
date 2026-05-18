---
title: "OpenAI 以 GPT-5.5 Instant 取代 ChatGPT 預設模型，幻覺率降低逾五成"
summary: "OpenAI 於 5 月 5 日靜悄悄地將 ChatGPT 預設模型從 GPT-5.3 Instant 升級至 GPT-5.5 Instant，錯誤陳述（幻覺）率降低 52.5%，AIME 數學評測成績從 65.4 提升至 81.2，並推出「記憶來源」功能，讓模型可調閱過往對話、上傳檔案及 Gmail 來客製化回應。"
category: "ai-ml"
publishedAt: 2026-05-18
lang: "zh"
featured: false
trending: false
sources:
  - name: "OpenAI"
    url: "https://openai.com/index/gpt-5-5-instant/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/"
  - name: "eWeek"
    url: "https://www.eweek.com/news/openai-gpt-55-instant-chatgpt-default-model/"
tags:
  - "OpenAI"
  - "GPT-5.5"
  - "ChatGPT"
  - "AI 模型"
  - "幻覺"
  - "記憶功能"
relatedSlugs:
  - "2026-05-18-openai-chatgpt-ads-manager-self-serve-zh"
  - "2026-05-15-openai-gpt-realtime-2-voice-models-zh"
  - "2026-05-14-openai-daybreak-cybersecurity-gpt55-zh"
---

2026 年 5 月 5 日，OpenAI 悄悄完成了 ChatGPT 數月來最重要的底層升級：將所有用戶層級（免費、Plus、Pro、Business、Enterprise）的預設模型從 GPT-5.3 Instant 換成 GPT-5.5 Instant。這次更新並未舉辦大型發布活動，卻在準確性、對話品質與個人化三個維度上帶來明顯進步，同時為更完整的記憶架構打下基礎——而這個架構將決定 AI 助理如何與用戶建立長期關係。

## 幻覺率大幅下降

最受矚目的數據是：在醫療、法律、金融等高風險領域的高要求提示測試中，GPT-5.5 Instant 的「幻覺陳述」（hallucinated claims）比 GPT-5.3 Instant 減少了 52.5%。幻覺率的測量向來不易標準化，因為評判正確與否取決於參考來源的定義，但 OpenAI 使用了結構化評估集，讓事實主張可對照權威參考資料加以核實。

對一般用戶而言，差異是切身可感的。GPT-5.5 Instant 在缺乏把握的領域更傾向回答「我不確定」，而非用同樣有自信的語氣生成聽起來合理但實際錯誤的資訊。模型的表達方式也更精簡——不再動輒列出一大堆項目符號、不必要的結構，以及那些增加摩擦感但沒有實質意義的追問。

## 評測成績提升

在 AIME 2025 數學競賽資料集上，GPT-5.5 Instant 拿下 81.2 分，較前代的 65.4 分提升約 24%——這個測試針對的是多步驟符號推理，而非表面的模式比對。在融合視覺與文字資訊的多模態推理評測 MMMU-Pro 上，成績則從 69.2 提升至 76。

這些進步讓 GPT-5.5 Instant 在部分評測中可與 Claude Mythos 相抗衡，雖然 Anthropic 的旗艦模型在多步驟代理任務和延伸推理評測上仍保有優勢。對絕大多數用戶而言，AIME 和 MMMU-Pro 的分數更像是指標意義大於實用意義——他們在乎的是模型能不能精確、清楚地回答眼前那個具體問題，而這種品質很難被一個數字完整代表。

## 記憶來源：更深遠的架構意義

這次 5 月 5 日更新中，技術層面更值得關注的，不是模型本身，而是同步推出的「記憶來源」（memory sources）功能。當 GPT-5.5 Instant 客製化某個回應時——例如引用了三次對話前用戶說過的話、參照了上傳的文件，或從連結的 Gmail 中提取了相關脈絡——系統現在會顯示透明層：具體調閱了哪些資訊、來源是什麼。

對 Plus 和 Pro 用戶來說，模型現在可以主動查詢過往對話、上傳檔案及連結的 Gmail 來建構個人化回應。一個問「我之前決定 Q3 預算怎麼處理？」的用戶，可能會得到引用自己上傳的試算表或某次過往對話的具體答案。記憶不是被動存在的，而是即時檢索、即時應用的。

關鍵在於：這一切都是可選擇且可審查的。用戶可以看到每次回應中具體使用了哪些記憶，並可刪除或修正個別記憶條目。OpenAI 的設計理念是把透明度當作功能，而非合規打卡——直接回應過去外界對「AI 個人化是黑盒子」的批評。

此功能目前優先向 Plus 和 Pro 網頁版用戶開放，行動端與 Free/Go/Business/Enterprise 用戶將於後續數週陸續跟進。路線圖還暗示了針對程式開發專案與長期研究任務的跨對話記憶功能，這將讓 GPT-5.5 Instant 成為迭代工作流中更得力的長期夥伴。

## API 存取與開發者影響

對開發者而言，GPT-5.5 Instant 可透過 API 以 `chat-latest` 存取，這個指向現已更新為新模型。OpenAI 確認，GPT-5.3 Instant 仍可作為付費 API 用戶的明確選項使用約三個月，讓開發團隊有時間在完全遷移前測試迴歸情況。

模型在事實準確性和簡潔性上的改善，對生產環境應用的影響可能比實驗性用途更顯著。基於 ChatGPT 建構的客服、文件分析或專業研究應用，向來最難應對幻覺問題——而 GPT-5.5 Instant 的進步恰好最集中在這些領域。若開發者過去為了補償 GPT-5.3 的錯誤率而建置了複雜的後處理過濾或事實核查層，這次升級或許讓部分防禦性工程有機會簡化。

## GPT-5.5 Instant 不是什麼

有幾點需要精確說明。GPT-5.5 Instant 是漸進式升級，不是前沿模型發布。它不是 Claude Mythos，後者在延伸推理與代理評測上推動著技術前沿。它也不是 o 系列推理模型的替代品，後者仍針對需要深度思維鏈的任務提供服務。

OpenAI 的模型陣容已刻意形成分層：Instant 系列負責快速、對話式、低成本的回應；推理模型針對結構化問題求解；語音、圖像生成與程式碼則有各自的專用模型。GPT-5.5 Instant 位於推理速度堆疊的底層，也是處理全球絕大多數 ChatGPT 互動的模型。光憑這個交互量，改善它對整體用戶體驗的意義，就超過任何一次前沿模型的發布。

## 競爭格局的背景

5 月 5 日的推出時機，絕非碰巧。Anthropic 於 5 月 13 日推出面向小型企業的 Claude for Small Business，整合了 QuickBooks、HubSpot、Canva 等工具。Google 則將在 24 小時後舉行 Google I/O 2026 主題演講，分析師預測 Gemini 的模型升級將與 GPT-5.5 Instant 處於同一競爭水準。模型品質競賽已從一年一度的史詩對決，演變為每隔數週就有增量進步的持續角力。

對用戶而言，好處是直觀的：ChatGPT 在最昂貴的失誤領域變得更可靠了。對 OpenAI 而言，更好的預設模型可降低流失率、強化訂閱的價值主張，同時為廣告、記憶與企業功能的分層疊加打下更穩固的基礎——而那些功能將定義其未來兩年的商業模式。
