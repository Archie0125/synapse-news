---
title: "Anthropic隱藏間諜程式碼、阿里巴巴禁用令：Claude-中國危機全解析"
summary: "Anthropic在Claude Code中嵌入隱藏的隱寫術程式碼，標記與中國有關聯的用戶，阿里巴巴隨後禁用該工具，而Anthropic正著手封堵中國企業使用的境外及VPN繞道存取管道。Anthropic團隊表示，移除該程式碼的拉取請求已被合併，但這場存取戰爭遠未結束。"
category: "ai-ml"
publishedAt: 2026-07-05
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: true
trending: true
sources:
  - name: "The Register"
    url: "https://www.theregister.com/ai-and-ml/2026/07/01/anthropic-is-removing-its-covert-code-for-catching-chinese-competitors/5265366"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/alibaba-bans-claude-code-anthropic-tracking-chinese-users"
  - name: "BanklessTimes"
    url: "https://www.banklesstimes.com/articles/2026/07/03/anthropic-moves-to-block-chinese-firms-using-claude-via-offshore-workarounds/"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/319415/20260701/claude-code-hid-proxy-fingerprints-system-prompts-anthropic-promises-fix.htm"
tags:
  - "Anthropic"
  - "Claude"
  - "中國"
  - "開發工具"
  - "AI政策"
  - "阿里巴巴"
relatedSlugs:
  - "2026-07-05-anthropic-claude-code-china-detection-alibaba-ban-en"
  - "2026-07-05-anthropic-samsung-custom-ai-chip-talks-zh"
  - "2026-06-29-us-export-control-claude-fable5-foreign-ban-zh"
---

6月30日，一名開發者對Claude Code進行逆向工程，發現工具的系統提示中藏有一套以隱寫術為基礎的秘密追蹤機制，設計目的是辨識位於中國或經由與中國有關聯的代理連線的用戶。

這起事件之後，阿里巴巴禁用了Claude Code，Anthropic也採取行動封堵中國的境外繞道存取管道。它像一扇窗，讓外界得以窺見美中AI技術戰的混亂與隱密的前線。

## 隱藏的程式碼

6月30日，一名對Claude Code進行逆向工程的開發者發現：當系統時區設定為Asia/Shanghai或Asia/Urumqi時，系統提示中的日期分隔符號會從標準連字號格式（`2026-06-30`）切換為斜線格式（`2026/06/30`）。「Today's」中的單引號也會在視覺上相同的Unicode字符之間切換，藉此編碼代理主機名稱是否符合中國網域清單、AI實驗室關鍵字清單、兩者皆符合或皆不符合。

邏輯很簡單：若系統時區設定為`Asia/Shanghai`或`Asia/Urumqi`，輸出就會不同。日期分隔符號的切換，加上Unicode單引號的編碼方式，共同構成一種輕量級的隱寫術指紋——以明文方式隱藏在文字回應之中。

部分偵測程式碼以金鑰`91`進行XOR混淆，這是一種防止邏輯在純文字字串搜尋中浮現的輕量手法。程式碼還會將主機名稱與一份已知的中國AI實驗室、帳號轉售商及代理閘道網域清單進行比對——也就是業界俗稱的「中轉站」。

「實作方式不應如此隱蔽，」一位分析此程式碼的安全研究員寫道，「即便目的——偵測代理濫用——是站得住腳的，隱藏偵測邏輯已越過了信任的重要界線。」

## Anthropic的回應

Anthropic一名工程師於7月1日確認偵測系統的存在，並表示移除該程式碼的拉取請求已於7月1日合併。

Anthropic表示，這項自2026年3月啟動的實驗，旨在防止未授權轉售商的帳號濫用，並防範模型蒸餾——即利用他人AI輸出來訓練競爭模型的做法。公司並未直接道歉，僅稱其為一項「未經適當審查」的「內部實驗」。

但損害已經造成。

## 阿里巴巴宣布禁用

阿里巴巴發出內部通知，禁止員工使用Claude Code，自7月10日起生效。通知稱，Claude Code近期被發現存在後門風險，已被列入具有安全漏洞的高風險軟體清單。

阿里巴巴力推其內部替代方案**通義靈碼（Qoder）**，該工具基於自家千問（Qwen）模型系列打造，已成長為領先的開源權重模型，且與阿里巴巴內部開發基礎設施深度整合。

阿里巴巴的禁用令絕非僅具象徵意義。阿里雲是亞洲最大的企業級平台之一，其對AI工具的內部立場，對整個跟隨其標準的中國企業與新創生態系統影響深遠。

## 更大規模的封鎖行動

隱藏程式碼事件只是Anthropic全面封堵中國未授權存取Claude更大行動的一部分。根據《金融時報》的深度報導，中國企業已建立起一套完整的繞道存取基礎設施：

- **企業子公司管道**：螞蟻集團等公司為員工提供與新加坡子公司掛鉤的Claude帳號，在中國大陸開發者與Anthropic服務條款之間保持一層地理隔離。
- **個人VPN訂閱**：字節跳動程式設計師透過VPN使用個人Claude訂閱，費用由公司報銷——帳號名義上是個人的，但使用顯然屬於企業行為。
- **雲端路由**：部分組織透過境外公司在Azure上註冊的帳號進行存取，讓大陸開發者得以透過技術合規的中間層查詢Claude。
- **中轉站服務**：數十家中介轉發服務公開列於中文網站和GitHub頁面，接受微信支付和支付寶，透過信譽良好的境外帳號代為轉發查詢。

Anthropic現計畫監控帳號的電腦時區及使用模式等訊號，以偵測充當中國關聯企業中轉站的帳號。

## 治理困境

此事件清楚呈現了在出口管制後時代，AI公司所面臨的核心張力。

6月中旬，在亞馬遜研究人員發現越獄漏洞後，商務部命令Anthropic對所有外國公民停用Fable 5和Mythos 5；出口管制於6月30日解除，Anthropic於7月2日恢復存取。但技術上的存取限制難以執行：Claude是軟體服務，不是實體硬體，而全球互聯網為有動機的用戶提供了充裕的路由選項。

Anthropic選擇的隱密偵測方式——在工具本身中嵌入隱藏追蹤邏輯——跨越了開發者社群認為至關重要的一條線：工具不應在用戶無從知曉或同意的情況下對其進行監控。

阿里巴巴的禁用令或許預示著，中國大型科技公司正在重新思考對美國原生開發工具的依賴，無論這些工具是否在形式上可存取。對於Anthropic而言，此事件是一場信任危機，即便程式碼已被移除，修復仍需時間。

美國AI公司與中國用戶之間的存取戰爭，很可能繼續升級，雙方都在開發更精密的偵測與規避技術。Anthropic的這次實驗揭示的是：在這場衝突中，工具本身已成為戰場的一部分。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 11 處。*
