---
title: "美國政府下令封禁 Fable 5：Anthropic 被迫向全球所有外國公民停服，同時公開反駁"
summary: "6 月 12 日，美國政府援引國家安全權力，發出緊急出口管制指令，要求 Anthropic 立即停止向全球所有外國公民提供 Claude Fable 5 與 Mythos 5 的存取權。Anthropic 為確保合規，被迫對所有用戶全面下線這兩款模型，同時公開表示不認同政府的決定，並警告此舉可能對整個 AI 產業造成危險先例。"
category: "policy"
publishedAt: 2026-06-29
lang: "zh"
featured: true
trending: true
sources:
  - name: "Anthropic — Fable 5 與 Mythos 5 停服聲明"
    url: "https://www.anthropic.com/news/fable-mythos-access"
  - name: "Fortune — Anthropic 在美國政府命令後關閉 Fable 和 Mythos"
    url: "https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/"
  - name: "National Law Review — Anthropic 停用 Claude Fable 5"
    url: "https://natlawreview.com/article/ai-company-anthropic-suspends-access-claude-fable-5-claude-mythos-5-following-us-export-control-directive"
  - name: "Al Jazeera — 美國命令 Anthropic 向外國公民停用 AI 模型"
    url: "https://www.aljazeera.com/news/2026/6/13/us-orders-anthropic-to-disable-ai-models-for-all-foreign-nationals"
  - name: "Cybersecurity Dive — 資安專家批評美國政府限制 Anthropic 模型"
    url: "https://www.cybersecuritydive.com/news/anthropic-us-government-export-ban-mythos-fable/822909/"
tags:
  - "anthropic"
  - "出口管制"
  - "AI政策"
  - "國家安全"
  - "claude"
  - "fable-5"
  - "mythos-5"
  - "川普政府"
  - "越獄"
relatedSlugs:
  - "2026-06-28-openai-gpt56-us-government-security-review-zh"
  - "2026-06-27-trump-nspm11-ai-national-security-enterprise-zh"
  - "2026-06-28-eu-cada-cloud-ai-development-act-zh"
---

2026 年 6 月 12 日東部時間下午 5 時 21 分，Anthropic 收到了一封來自美國政府的信函。

這份援引國家安全法律的指令，要求 Anthropic 立即停止向地球上所有外國公民提供 Claude Fable 5 與 Claude Mythos 5 的存取——無論他們身在哪個國家、持有何種工作簽證在美任職，甚至包括 Anthropic 內部的外籍員工。

6 月 13 日，全球大多數地區的用戶早晨醒來時，Anthropic 最強大的兩款模型已全面停服。

## 政府指令與越獄事件

政府的核心理由是一個據報的「越獄」漏洞。根據 Anthropic 的說法，官員告知公司，Amazon 旗下的研究人員發現了一種繞過 Fable 5 資安防護機制的方法。

這個所謂的越獄手法，從 Anthropic 的描述來看，平凡得令人訝異：向模型要求「閱讀特定程式碼庫並修復軟體漏洞」。在特定的指令序列下，此操作讓 Fable 5 顯示出其安全過濾器原本應攔截的漏洞資訊。

Anthropic 工程師審查後得出了不同結論。他們認定這是一個「窄域、非通用型越獄」，曝露的是「少數已知的輕微漏洞」。更值得關注的是，公司指出，相同的底層能力同樣存在於 OpenAI 的 GPT-5.5 中——一款全球數億用戶可存取的模型，卻沒有任何類似限制。

Anthropic 在公開聲明中直指矛盾所在：「發現一個窄域的潛在越獄，應該是召回已部署給數億用戶的商業模型的理由」——言下之意，若此漏洞等級足以封禁 Fable 5，那整個業界大多數前沿模型都應一視同仁。

## 為何是全球停服，而非地理封鎖

這道指令的措辭製造了一個罕見的合規難題。「停止向所有外國公民提供服務」聽起來像是 IP 地理封鎖的問題，但法律現實更加複雜。

Anthropic 的系統從未設計用來即時驗證美國境內用戶的公民身份。在缺乏覆蓋全體用戶、同時又不侵犯隱私的實時國籍核查機制下，確保合規的唯一可行途徑，就是對所有用戶、在全球範圍內關閉 Fable 5 和 Mythos 5。

其他 Claude 模型——Opus 4.8、Sonnet、Haiku 及早期版本——並未受到影響。但 Fable 5，距其正式上線僅僅三天，就從全面開放變成了徹底停服。

## Mythos 5 是什麼？它為何也被波及？

Claude Mythos 5 是 Fable 5 的姊妹模型，兩者共用相同的底層架構，但 Mythos 5 針對特定受審核的用戶群體——政府核可的網路防禦者、關鍵基礎設施業者及安全研究人員——解除了部分資安領域的安全限制。Anthropic 形容它是「全球所有模型中網路安全能力最強的」。

正因如此，Mythos 5 的停服或許不那麼令人意外——其明確面向攻擊性與防禦性網路安全工作的設計，恰好落在政府指令的核心打擊範圍內。但諷刺的是，停服同時清除了美國政府核可的安全團隊原本用於國家防禦工作的工具，這一矛盾在資安圈引發了廣泛關注。

## 對整個產業的衝擊

這道指令引發了資安研究人員與 AI 治理專家的強烈批評。核心論點是：若一個同樣存在於 GPT-5.5 中的越獄手法，就能以國家安全為由對 Claude Fable 5 啟動緊急限制，那相同邏輯可以在任何時間應用於任何前沿模型——等同於賦予行政機關單方面、幾乎不受程序約束地將 AI 產品下架的權力。

接受業界媒體採訪的資安專業人士指出，指令中描述的越獄手法——讓模型分析程式碼並找出漏洞——在功能上與靜態分析器、模糊測試工具等開源資安工具已做了數十年的事高度相似。區別在於 Fable 5 做得更好、更快，而這恰恰引出了一個尚無定論的問題：「強大的資安工具」與「危險的 AI 能力」之間的邊界，究竟在哪裡？

Anthropic 在聲明中謹慎地將其合規定性為法律義務，而非認同政府立場。公司表示「相信這是一個誤解，並正積極努力儘快恢復服務」，同時警告：若以相同標準對待整個業界，「實際上將使所有前沿模型供應商的所有新模型部署停擺」。

## 一個正在成形的先例

Fable 5 停服發生的這一週，美國政府對先進 AI 模型的整體態度正在多個層面同步收緊。OpenAI 最強模型 GPT-5.6 同期正在接受美國政府安全審查，在獲准更廣泛商業部署之前，須完成 AI 安全研究院主導的審核程序——但那是一個更具協作性的流程，而非緊急指令。

兩者的處理方式形成鮮明對比，在業界引發了一場辯論：Fable 5 事件是否反映了政府對 Mythos 級別能力——即解除資安限制的模型——的特定憂慮？還是一個更廣泛的監管態勢的開端：行政機關可以在缺乏一般監管程序保護機制的情況下，援引國家安全名義暫停商業 AI 產品？

截至本文發稿，Anthropic 尚未收到恢復 Fable 5 服務的許可。6 月 1 日向美國證管會秘密提交的 IPO 申請，如今面臨一個全新的重大風險因素：一個願意在一夜之間切斷其最重要商業模型的政府所帶來的監管不確定性。

對全球 AI 社群而言，Fable 5 停服事件提出的問題，其影響將遠超這一具體案例的解決：在 AI 能力被視為國家安全議題的世界裡，為全球市場打造產品意味著什麼？而誰，終究有權決定一個模型是否強大到不能運行？

---

*截至本文發布，Claude Fable 5 與 Mythos 5 仍處於停服狀態。Anthropic 表示正積極與政府官員溝通，努力恢復服務。*
