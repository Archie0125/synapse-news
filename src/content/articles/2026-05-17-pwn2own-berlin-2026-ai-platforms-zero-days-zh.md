---
title: "Pwn2Own柏林2026：AI平台首度成為駭客競賽主角，39個零時差漏洞入袋逾90萬美元"
summary: "資安研究員在Pwn2Own柏林2026前兩天賽程中，以39個獨特的零時差漏洞獲得908,750美元獎金，LiteLLM與Cursor等AI目標也在遭攻破之列。"
category: "developer-tools"
publishedAt: 2026-05-17
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: false
sources:
  - name: "Security Affairs"
    url: "https://securityaffairs.com/192183/hacking/pwn2own-berlin-2026-day-one-523000-paid-out-ai-products-fall.html"
  - name: "Zero Day Initiative"
    url: "https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results"
  - name: "BleepingComputer"
    url: "https://www.bleepingcomputer.com/news/security/windows-11-and-microsoft-edge-hacked-on-first-day-of-pwn2own-berlin-2026/"
  - name: "CybersecurityNews"
    url: "https://cybersecuritynews.com/microsoft-exchange-windows-11-and-cursor-zero-days-exploited-pwn2own/"
tags:
  - "資安"
  - "Pwn2Own"
  - "零時差漏洞"
  - "LiteLLM"
  - "Cursor"
  - "AI安全"
  - "Windows 11"
  - "Microsoft Edge"
relatedSlugs:
  - "2026-05-17-pwn2own-berlin-2026-ai-platforms-zero-days-en"
  - "2026-05-13-anthropic-mythos-autonomous-exploit-zh"
---

Pwn2Own是一項駭客競賽，研究員在其中展示完整修補軟體中前所未知的漏洞。今年的柏林場聚焦企業技術與人工智慧，目標包括AI資料庫、程式碼代理與本地推論。

結果令人警醒。

賽事前兩天結束後（仍剩一天），研究員們共獲得908,750美元獎金，代價是39個全新零時差漏洞。Windows 11三度淪陷。Microsoft Edge被一套多漏洞組合攻破沙盒，獎金高達17.5萬美元。更值得注目的是：LiteLLM被研究員k3vg3n串連三個漏洞（包括伺服器端請求偽造與程式碼注入）完全攻陷。

## 第一天：52.3萬美元，24個零時差

24個獨特漏洞被現場示範，研究員合計領取52.3萬美元獎金，平均每個漏洞約2.2萬美元。

單場最耀眼的演出來自DEVCORE研究團隊的Orange Tsai，他以串連四個邏輯漏洞的方式突破Microsoft Edge沙盒，獨斬17.5萬美元。

Windows 11在首日三度被不同研究員以提權零時差漏洞攻破，兩個消息來源指稱三組各獲得3萬美元，但Zero Day Initiative自身的列表顯示第一組為3萬美元，另外兩組各為1.5萬美元。三組人馬獨立挖到同類漏洞，意味著可攻擊的面積遠超微軟內部安全團隊所掌握的範圍。

第二天延續了成果。Microsoft Exchange再度中箭，這是企業攻擊研究的長青目標。更引起AI產業關注的是：Cursor程式碼編輯器在第二天被不同團隊成功攻破兩次。

## AI安全的警鐘

LiteLLM與Cursor遭攻破，是本次賽事戰略意義最重大的發現，即便獎金金額不如Edge那麼顯眼。

LiteLLM是基礎設施層的軟體。對LiteLLM的成功攻擊，影響範圍不只是單一應用程式——攻擊者可能取得企業所有AI互動的存取權限。Pwn2Own展示的攻擊手法串連了三個漏洞（包括SSRF與程式碼注入），攻陷LiteLLM。

Cursor的問題則是另一類威脅。具備AI功能的程式碼編輯器，能看到開發者工作流程中極為敏感的內容：原始碼、設定檔中的認證金鑰、環境變數，且往往直接與雲端部署管線整合。Cursor的零時差漏洞，在理論上可被用來靜默竊取企業核心程式碼，或在開發者毫無察覺的情況下植入惡意邏輯。

## 為什麼今年感覺不一樣

AI工具鏈是新興產物，部署快速，往往未經過與傳統企業軟體同等嚴格的安全審核，卻已在帶著高度特權的情況下操作敏感系統。

與此同時，傳統目標依舊漏洞不絕。Windows 11、Edge、Exchange歷經多年研究員攻打與微軟大手筆的安全投資，其中Windows 11與Edge在首日淪陷，Exchange也在第二天跟進。成熟攻擊面持續出洞、全新AI攻擊面幾乎尚未被系統性審視——這個雙重組合，讓本屆柏林賽事成為近年影響最廣泛的一屆。

## 對企業的警示

廠商有90天時間，針對賽事中示範的零時差漏洞發布修補程式。

但負責任揭露不代表這些發現在修補前毫無意義。Pwn2Own示範的每一個零時差漏洞，都代表一個威脅行為者可能早已發現並悄悄利用中的漏洞類別。賽事不製造風險，只是讓既有的風險現形。

對企業資安團隊而言，柏林的賽果帶來幾個具體行動項目：LiteLLM及類似AI代理框架的部署，應重新審視網路隔離與輸入驗證控制；具備AI功能的程式碼編輯器應納入與其他開發工具相同的端點安全審查；更根本地，AI軟體必須被視為安全關鍵基礎設施，而非一般生產力工具，這個認知需要更快速地進入採購與治理流程。

AI產業過去三年大量辯論模型安全。Pwn2Own柏林2026提醒我們：模型以下的整個技術堆疊——API、代理、編輯器、調度層——同樣值得至少相等的關注。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 22 處。*
