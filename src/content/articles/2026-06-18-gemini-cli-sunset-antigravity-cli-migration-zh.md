---
title: "Google今日正式關閉Gemini CLI：強制遷移Antigravity CLI引爆開發者怒火"
summary: "2026年6月18日起，Google正式停止Gemini CLI服務——這個擁有十萬GitHub星標的開源AI程式工具，宣告終結。繼任者Antigravity CLI在I/O上只給了開發者30天的遷移時間，且是非開源工具，原有自動化腳本全面失效，眾多開發者已開始轉向競爭平台。"
category: "developer-tools"
publishedAt: 2026-06-18
lang: "zh"
featured: false
trending: true
sources:
  - name: "Google Developers Blog"
    url: "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
  - name: "The Register"
    url: "https://www.theregister.com/ai-ml/2026/05/20/bye-bye-gemini-cli-google-nudges-devs-toward-antigravity/5243605"
  - name: "Groundy"
    url: "https://groundy.com/articles/google-sunsets-gemini-cli-on-june-18-forced-migration-to-antigravity-cli-breaks/"
tags:
  - "Google"
  - "Gemini CLI"
  - "Antigravity CLI"
  - "開發者工具"
  - "開源"
  - "AI程式輔助"
  - "開發者體驗"
relatedSlugs:
  - "2026-06-16-github-copilot-metered-billing-backlash-zh"
  - "2026-06-16-spacex-acquires-cursor-60-billion-zh"
  - "2026-04-04-cursor-devin-war-zh"
---

今天，Gemini CLI正式停止服務。

2026年6月18日起，這個累積超過十萬個GitHub星標、收到超過六千個社群Pull Request的命令列AI工具，走入歷史——由一個叫做Antigravity CLI的新工具取代。距離Google在5月19日Google I/O上宣布這件事，只有整整三十天。

反彈來得迅速、激烈，且耐人尋味。問題不只是新工具好不好——Antigravity CLI確實有真正的改進。問題在於遷移方式。開發者在CI流水線、shell腳本與自動化工作流中嵌入了Gemini CLI，如今被告知要在一個月內全部重寫，沒有相容層，截止日期還壓在兩週衝刺週期的中間。

## Gemini CLI曾是什麼

2025年初，Gemini CLI以Apache 2.0開源授權亮相，是Google針對AI程式輔助熱潮推出的命令列工具：終端機原生、開源、可讓開發者不離開命令列就使用Gemini的能力。它的增長迅速——十萬顆星是有機採用的具體證明——並透過社群貢獻積累了六千個已合併的Pull Request。

對許多組織而言，Gemini CLI成為承重的基礎設施。CI流水線用它做自動化程式審查，shell腳本用它生成文件，個人開發者把它編進每天的工作流。這個工具存在了大約一年，讓人感覺——事後看來是錯誤的感覺——Google會持續維護它。

## Antigravity CLI是什麼（不是什麼）

Antigravity CLI以`agy`指令呼叫，是用Go語言從頭重寫的工具，專為多代理工作流設計——處理2026年AI工具日常使用中的核心需求：多個代理並行運作、非同步任務執行、長時間在背景運行的操作。

功能集確實有所擴展。Antigravity CLI不只支援Gemini模型，還支援Claude與GPT-OSS-120B，讓它從單一廠商工具變成多模型平台，直接對標Claude Code與OpenCode等工具。

但有兩個關鍵問題。第一，Antigravity CLI**不是開源工具**。不同於Apache 2.0授權的Gemini CLI，Antigravity CLI以封閉二進位檔形式發布。其GitHub儲存庫只有更新日誌、README和一個展示介面外觀的GIF。對有開源要求或安全稽核需求的組織而言，這是一個根本性的改變。第二，Google明確表示，**新工具在發布時不會具備完整的功能對等性**——開發者在三十天的期限內，必須遷移到一個還不完整的工具。

## 遷移現場：實際會壞掉什麼

從`gemini`到`agy`的強制遷移，在三十天內究竟會碰到哪些問題？

所有假設指令名稱的地方都需要更新：shell別名、CI設定、shebang行、PATH引用，一個也跑不掉。但這只是容易的部分。兩個工具的認證機制不同，需要重新生成憑證。外掛系統（Extensions）被更名為「Antigravity plugins」並改變了API——自製外掛的團隊必須重新移植。

時間問題讓情況更糟。大多數工程團隊跑兩週衝刺。三十天的遷移窗口意味著一個衝刺用來規劃、一個衝刺用來執行，完全沒有測試、審批或除錯的緩衝時間。對那些將Gemini CLI嵌入生產自動化的組織來說，尤其艱難。

Google在遷移文件中承認了這場混亂，說「不會是完美的過渡」。這是事實，但遠遠不夠。

## 誰還能繼續使用

這次下線並不平等地影響所有用戶。免費用戶、Google AI Pro訂閱者、Google AI Ultra訂閱者今天起失去存取權。但透過Gemini Code Assist**標準版**或**企業版**授權使用的組織，或透過付費Gemini API金鑰使用的用戶，仍可繼續存取並獲得模型更新。

結果是兩層制：個人開發者和小型團隊——正是讓Gemini CLI在GitHub取得十萬顆星的社群——率先被切斷，而企業合約提供了緩衝。這是合理的商業決策，但在開源社群眼中，滋味相當難受。

## 信任的代價

真正的損害，不在任何一條流水線或工作流。它在於開發者在評估要不要把基礎設施建在某個工具上時，所用的信任算法。

Gemini CLI於2025年初推出，2026年6月下線，壽命大約十五個月。對今天正在評估AI工具的開發者而言，這個時程是一筆數據。問題不是Antigravity CLI好不好。問題是：十五個月後，Antigravity CLI會是什麼結局？

開發者社群的討論串已出現明確的比較：Claude Code和OpenAI的程式工具，都沒有做過類似的強制遷移。擁有十六萬GitHub星標、750萬月活躍用戶的開源程式代理OpenCode，可以跑在任意模型上，不受單一廠商控制。這些替代品正在因為Gemini CLI的遷移事件而受益——許多團隊把這次混亂當作一個觸發點，重新審視整個工具鏈的選擇。

## Antigravity CLI做對了什麼

公允地說：Antigravity CLI的多模型支援解決了一個真實的問題。因為CLI工具被迫只能用Gemini模型的開發者，現在可以透過同一個介面使用Claude或其他供應商。非同步工作流架構也反映了AI開發的實際演進——順序式、單模型提示，愈來愈難以應付複雜的開發任務。

Go語言重寫帶來了更快的二進位檔、更低的延遲。在每天觸發數百次呼叫的CI環境中，這是有意義的改進。成熟後的多代理編排能力，也可能比Gemini CLI強大許多。

但功能上的進步，無法掩蓋流程上的失敗。以三十天的通知強制棄用一個開源社群工具、推出缺乏功能對等性的封閉原始碼替代品、率先切斷免費和個人用戶——這些決策，會在開發者評估Google下一款開發工具時，被清楚地記起。

今天傳達給市場的信號，不是關於Antigravity CLI的優劣。而是關於「建立在Google開發者基礎設施上」這件事，究竟意味著什麼。
