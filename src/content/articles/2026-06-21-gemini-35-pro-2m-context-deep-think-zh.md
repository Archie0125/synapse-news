---
title: "200 萬 Token 的承諾：Gemini 3.5 Pro 遲遲未到，揭示 AI 前沿模型發布的困境"
summary: "Google 在五月十九日的 I/O 大會上承諾 Gemini 3.5 Pro 將於六月底上線，主打 200 萬 token 超長上下文視窗與全新「Deep Think」延伸推理模式，但截至六月下旬仍僅開放給部分企業客戶試用。這場延遲揭示了 2026 年前沿 AI 模型開發的一個結構性困境：建造最強大的模型，與準時交付，在實務上幾乎難以兩全。"
category: "ai-ml"
publishedAt: 2026-06-21
lang: "zh"
featured: false
trending: false
sources:
  - name: "TechTimes — Google Gemini 3.5 Pro 六月發布在即"
    url: "https://www.techtimes.com/articles/317919/20260606/google-gemini-35-pro-nears-june-launch-2-million-token-context-deep-think-reasoning.htm"
  - name: "WaveSpeed — Gemini 3.5 Pro 下個月來了"
    url: "https://wavespeed.ai/blog/posts/gemini-3-5-pro-coming-next-month/"
  - name: "FindSkill AI — Gemini 3.5 Pro 發布日期"
    url: "https://findskill.ai/blog/gemini-3-5-pro-release-date/"
tags:
  - "google"
  - "gemini"
  - "gemini-3-5-pro"
  - "AI模型"
  - "上下文視窗"
  - "deep-think"
  - "前沿模型"
  - "大型語言模型"
relatedSlugs:
  - "2026-04-04-google-gemini-everywhere-zh"
  - "2026-06-18-openai-gpt56-imminent-june-launch-zh"
---

五月十九日的 Google I/O 大會上，桑達·皮查伊做出了一個讓在場開發者發出一聲嘆息的承諾：Gemini 3.5 Pro 及其 200 萬 token 超長上下文視窗與全新「Deep Think」延伸推理模式，將在下個月前上線。「給我們到下個月，」他說。

下個月就快結束了，Gemini 3.5 Pro 仍只開放給部分 Vertex AI 企業客戶試用。預測市場給出在六月三十日前正式上線的概率約為 50 至 55%——這個數字，揭示了 2026 年年中前沿模型開發的一個重要現實：打造最強大的 AI 系統，和按時交付它，在實務上幾乎是互斥的目標。

## Gemini 3.5 Pro 究竟是什麼？

這款模型的核心賣點是其上下文視窗：200 萬 token，目前已知生產級前沿模型中最大的規格。具體而言，200 萬 token 大約等於 150 萬個英文字，相當於五到八本長篇小說的文字量。對開發者和企業而言，這意味著可以在單一工作階段中輸入整個大型程式碼庫、完整的年度郵件往來記錄，或龐大的法律文件集，而無需截斷或拆分。

已在五月十九日正式發布的 Gemini 3.5 Flash，在 Terminal-Bench 2.1 上取得 76.2%、在 MCP Atlas 上取得 83.6% 的成績，超越了上一代 Gemini Pro 系列。3.5 Pro 預計在 Flash 仍力有未逮的領域取得更大突破，尤其是高難度數學推理、多步驟科學問題求解，以及在超大文件集上的長程資訊提取。

## Deep Think：Google 的延伸推理賭注

第二個核心功能 Deep Think，是 Google 對 OpenAI o 系列模型引入的延伸推理能力的正面回應。概念上並不複雜：模型不再只做一次前向傳播就輸出答案，而是被允許花費更多算力評估問題、檢查中間推理過程，並在生成最終答案前進行修正。

在延伸推理真正發揮作用的那類問題上，這種方法帶來的提升是顯著的——數學競賽題、多步邏輯謎題、複雜科學推導。Google 宣稱 Deep Think 將讓 Gemini 3.5 Pro 在 ARC-AGI-3 等高難度推理評測上達到前沿表現。

然而有一個重要限制：Deep Think 功能僅限月費 250 美元的 Ultra 訂閱方案使用。月費 20 美元的標準 Pro 訂閱用戶雖然能使用 200 萬 token 上下文視窗，但無法存取延伸推理模式。這種分層存取策略已引發開發者批評——許多人認為，延伸推理本質上是算力的多寡問題，而非功能的本質差異，人為設限顯得過於粗暴。

## Google 正在應對的競爭壓力

Google 並不是在真空中發布 Gemini 3.5 Pro。自五月十九日以來，前沿模型市場的競爭節奏絲毫未放緩。

Anthropic 的 Claude Opus 4.8 在五月二十七日發布後，以 61.4 的評分奪下 Artificial Analysis Intelligence Index 榜首——首款突破 60 分的模型。OpenAI 的 GPT-5.5 Instant 於四月起成為 ChatGPT 的預設模型，持續定義著日常 AI 使用的實用基準。而即將上線的 GPT-5.6 據傳將把上下文視窗拓展至 150 萬 token，並強化長程程式設計能力——這直接與 Gemini 3.5 Pro 的核心賣點重疊。

如果 GPT-5.6 搶先 Gemini 3.5 Pro 公開上線，Google 可能面臨尷尬局面：自家旗艦模型的標誌性功能——200 萬 token 上下文視窗——到上線時，競爭標桿已再度移動。

## 定價與 Flash 的比較

Gemini 3.5 Flash 已在 API 中以每百萬輸入 token 1.5 美元、輸出 9 美元的定價上線，在所有中端模型中具備競爭力，且遠比 GPT-5.5 便宜。3.5 Pro 預計遵循歷史上約 10 倍 Flash 的定價比例，落在每百萬輸入 token 15 美元、輸出 60 美元附近，與 Claude Opus 4.8 和 GPT-5.5 定價相當。

企業買家面對的核心問題是：3.5 Pro 相對 Flash 的額外能力，對他們的具體工作負載而言是否值得溢價？多家企業評測方已表示，Gemini 3.5 Flash「在 10% 的成本下能處理 80% 的使用場景」。對特定企業任務——全面的程式碼審查、長文件綜合、合約分析——200 萬 token 上下文視窗的確具有決定性價值；但對主導實際部署的對話和任務執行工作負載而言，則幾乎無關緊要。

## 更廣泛的模式：前沿模型為什麼總是延期？

Gemini 3.5 Pro 的延遲並非孤例。OpenAI 的 GPT-5.6「六月會來」這個說法已流傳數週，但仍未有確定日期。Anthropic 則刻意選擇不提前公布發布時間，正是為了避免陷入這種被動。

這個模式反映了 2026 年前沿模型開發的結構性現實：安全性評估、紅隊測試和基礎設施強化等發布前審查流程，本質上難以精準預測。一個技術上已完成的模型，可能在發布前的內部審查中多花幾週。

對 Google 而言，這次延遲帶來的損失不只是競爭層面，更是聲譽層面的。Google 多年來一直試圖擺脫「AI 產品發布遲到、能力不符預告」的標籤。Gemini 1.0 在 2023 年十二月的問題重重上線、Gemini Ultra 在 2024 年初的延遲、以及現在的 3.5 Pro——這些點，外界觀察者正將它們連成一條線。

Google 的支持者則指出：Flash 在 I/O 的發布確實如期而至，能力也確實令人信服。3.5 架構本身的品質並無疑問。真正存疑的是：Google 是否已解決了讓能力提升能夠以可預期節奏傳遞給市場的組織問題——而在當前的競爭環境中，這個組織問題在戰略上與底層技術同等重要。

## 接下來的走向

未來十天存在三個情境。一：Gemini 3.5 Pro 在六月三十日前正式上線，200 萬 token 上下文、Ultra 方案的 Deep Think、API 定價均符合預期——Google I/O 的承諾兌現，在企業市場強勢應對 GPT-5.6。二：發布延至七月，附帶更新後的能力集——也許是更大的上下文視窗或新的多模態功能——以此為額外等待的時間提供正當理由。三：GPT-5.6 搶先上線，Google 的發布淪為追趕，而非引領。

對在前沿模型堆疊上建構應用的開發者，三種情境下的實務建議是一樣的：先用 Flash 評估當前工作負載，並建立好模型抽象層，讓你能在不大改程式碼的情況下切換底層模型。今天看起來最強的模型，九十天後通常早已不是。

Gemini 3.5 Pro 終將帶來的東西——在前沿表現水準下的 200 萬 token 上下文視窗——是一個真正有意義的能力提升。唯一的問題，是它究竟能否及時到場，定義市場時刻；還是在整個市場已再度向前移動後，才悄悄地上線。
