---
title: "OpenAI 推出 GPT-5.4-Cyber：專為通過身份驗證的資安專家設計的 AI 模型"
summary: "OpenAI 發布 GPT-5.4-Cyber，這是其旗艦模型的資安專用變體，僅開放給通過「可信存取計畫」審核的資安專業人員使用。此次發布恰好在 Anthropic 公布 Mythos 模型一週後，標誌著 AI 輔助資安防禦領域的新一輪競賽正式開打。"
category: "ai-ml"
publishedAt: 2026-04-15
lang: "zh"
featured: false
trending: true
sources:
  - name: "OpenAI — 可信存取計畫"
    url: "https://openai.com/index/scaling-trusted-access-for-cyber-defense/"
  - name: "Axios — OpenAI 推出分級存取制度"
    url: "https://www.axios.com/2026/04/14/openai-model-cyber-program-release"
  - name: "Bloomberg — OpenAI 向有限群體發布網路模型"
    url: "https://www.bloomberg.com/news/articles/2026-04-14/openai-releases-cyber-model-to-limited-group-in-race-with-mythos"
  - name: "SiliconANGLE — OpenAI 為通過審核的資安專業人員推出 GPT-5.4-Cyber"
    url: "https://siliconangle.com/2026/04/14/openai-launches-gpt-5-4-cyber-model-vetted-security-professionals/"
tags:
  - "OpenAI"
  - "GPT-5.4"
  - "資安"
  - "AI安全"
  - "企業AI"
relatedSlugs:
  - "2026-04-15-anthropic-mythos-glasswing-zh"
---

OpenAI 週一正式發布 GPT-5.4-Cyber，這是目前旗艦模型的資安專用微調版本，專為防禦性資安工作而生，且僅開放給通過嚴格審核的資安專業人員使用。這次發布距 Anthropic 披露自家雙用途資安模型「Claude Mythos Preview」恰好整整七天。

時間點的巧合絕非偶然。兩家公司的接連發布，標誌著一個關鍵轉折點：前沿 AI 模型已跨越某個能力門檻，足以從根本上影響全球最關鍵軟體基礎設施的安全態勢。這個門檻要如何被妥善管理，恐怕將深刻影響未來多年的資安格局。

## GPT-5.4-Cyber 能做什麼

GPT-5.4-Cyber 並非全新架構，而是在現行 GPT-5.4 基礎上進行微調的「寬鬆資安版」——與消費端及企業端產品使用相同底層架構，但針對一般聊天機器人通常會拒絕的資安任務，刻意降低了拒絕門檻。

最具代表性的解鎖能力是**二進位逆向工程**：在無需取得原始碼的情況下，分析編譯後的軟體，找出惡意程式、潛在漏洞與安全弱點。對資安研究人員來說，這是革命性的進步。過去，逆向分析編譯後的二進位檔案需要多年的專業訓練；GPT-5.4-Cyber 大幅壓縮了這道學習曲線。

此外，模型還支援弱點報告自動分類、威脅模型生成、攻擊鏈分析，以及將自然語言需求轉化為防禦腳本和偵測規則。OpenAI 將這些功能定位為「進階防禦工作流程」，遠超過過去任何版本 GPT 在標準安全限制下所能處理的範疇。

值得注意的是，模型仍保留了防範攻擊性用途的護欄，不會生成針對關鍵基礎設施的攻擊指令或完整 exploit 代碼。OpenAI 資安長 Dane Stuckey 坦承，提示詞注入攻擊（prompt injection）仍是「前沿、尚未解決的安全問題」，公司正「審慎研究並積極緩解」寬鬆版模型遭濫用的風險。

## 三層存取架構

GPT-5.4-Cyber 的存取管道建立在 OpenAI 2026 年初推出的「可信存取計畫」（Trusted Access for Cyber）之上，新版本在原有基礎上增加了更多層級，形成金字塔式的信任與能力梯度：

- **標準層**：一般 ChatGPT 消費端及商業用戶，無須額外驗證，使用標準安全政策下的 GPT-5.4。
- **中級層**：已在 `chatgpt.com/cyber` 完成身份驗證的資安專業人員，解鎖部分擴展能力。
- **最高層**：通過深度審核的資安廠商、企業組織與個人研究員，需提供合法資安職業或研究機構隸屬的證明，唯有此層級才能申請 GPT-5.4-Cyber 的使用權限。

企業用戶可透過 OpenAI 帳戶代表申請最高層級；個人研究員則需透過 chatgpt.com/cyber 入口提交申請。

OpenAI 在擴大最高層規模方面態度審慎。初期僅向少數通過審核的資安公司和研究機構開放，並計畫在未來數月陸續擴展至「數千名個人用戶與數百支資安團隊」，同步精進驗證流程並監控潛在濫用模式。

## 與 Anthropic Mythos 的競速賽

在時間點上，此次發布與 Anthropic Mythos 的關係是這個故事的核心。4 月 7 日，Anthropic 披露 Claude Mythos Preview 已自主識別出各大作業系統與瀏覽器中數千個零時差漏洞（zero-day），包括一個潛伏長達 27 年的 OpenBSD 漏洞，以及一個存在 16 年的 FFmpeg 安全缺陷。Anthropic 選擇不公開發布模型，而是透過「玻璃翼計畫」（Project Glasswing）將其能力導入由 Apple、Microsoft、Google、NVIDIA 等 11 家業界夥伴組成的防禦聯盟，並承諾提供 1 億美元的使用點數。

OpenAI 的回應策略截然不同。Anthropic 選擇完全封鎖公眾存取，僅透過受控聯盟對外釋放能力；OpenAI 則是建立一個以信任為基礎的分級市場：只要通過愈來愈嚴格的身份驗證，使用者就能存取愈來愈強大的工具。

這兩種哲學之間的辯論——「受控聯盟」對「身份驗證市場」——很可能成為未來幾年 AI 與資安政策論戰的核心議題。兩者各有取捨：Anthropic 的模式控制力最強，但將權力集中在少數科技巨頭手中；OpenAI 的模式更具民主化精神，但驗證流程本身可能成為社會工程攻擊的新目標。

## 對資安產業的意義

資安業界正密切觀察這兩次發布，其影響遠不止於哪家公司贏得企業資安市場份額。

傳統資安工具——SIEM 平台、弱點掃描器、滲透測試框架——歷來都需要具備深厚專業知識的人類操作員，才能將原始資料轉化為可行動的威脅情報。能夠在規模化場景下執行二進位逆向工程、生成偵測規則、推理攻擊鏈的 AI 模型，代表著資安防禦人員生產力的潛在跨越式躍升——而這個職場長期面臨嚴重人力短缺的問題。

美國網路安全暨基礎設施安全局（CISA）據報正與 OpenAI 及 Anthropic 分別洽談正式的政府存取管道；美國國家安全局（NSA）也已表示有意將 GPT-5.4-Cyber 與 Mythos Preview 納入其「網路安全協作中心」的應用範疇。

對企業資安團隊而言，最迫切的問題十分實際：誰有資格申請最高層、審核需要多長時間、附帶哪些法律條款？OpenAI 目前尚未公布具體審核時程與詳細合約條款，而這些細節將是資安運營中心（SOC）在評估是否採用這套平台時的關鍵決策依據。

## 競爭格局

GPT-5.4-Cyber 進入的市場已有眾多 AI 資安工具競爭，包括 CrowdStrike、Palo Alto Networks 以及微軟 Security Copilot，這些產品已深耕近兩年。OpenAI 的差異化主張在於底層模型能力：以超大規模訓練的 GPT-5.4-Cyber，在面對開放性、新穎威脅場景時，理論上能超越為特定資安場景客製化的專用模型。

這個論點需要在實戰中接受驗證。資安團隊以高度懷疑的態度著稱，在做出採購決策前必然會進行嚴格的自有基準測試。OpenAI 已宣布為完成層級驗證的組織提供一個受限的公開評估計畫，讓他們能在正式採用前，以內部紅隊資料集測試模型表現。

有一點已十分清晰：前沿 AI 實驗室已正式將資安列為一流產品優先項，而非僅僅是倫理與安全的附帶考量。AI 驅動的攻防競賽，已從理論層面的隱憂，演變為真實存在的產品賽道——而起跑槍聲，就在本週響起。
