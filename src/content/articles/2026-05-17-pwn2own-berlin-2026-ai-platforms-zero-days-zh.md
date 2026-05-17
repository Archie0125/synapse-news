---
title: "Pwn2Own柏林2026：AI平台首度成為駭客競賽主角，39個零時差漏洞入袋逾90萬美元"
summary: "頂尖資安研究員在Pwn2Own柏林2026賽事中，發現39個獨特的零時差漏洞並獲得超過90萬美元獎金，AI調度工具LiteLLM與AI程式編輯器Cursor首度列入競賽目標。賽事報名首次額滿、逾150名研究員遭拒門外，顯示安全社群對AI系統攻擊面的研究熱情已全面引爆。"
category: "developer-tools"
publishedAt: 2026-05-17
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

Pwn2Own已是全球最具聲望的駭客競賽，走過19年歷史，向來以挑戰世界上防護最嚴密的軟體為己任。今年的柏林場，賽事加入了一個兩年前聽起來幾乎是科幻的新類別：AI平台。

結果令人警醒。

5月13至14日的兩天賽程結束後，研究員們共獲得908,750美元獎金，代價是39個全新零時差漏洞。Windows 11三度淪陷。Microsoft Edge被一套多漏洞組合攻破沙盒，獎金高達17.5萬美元。更值得注目的是：LiteLLM——一款廣受企業採用的開源AI模型路由框架，用於管理對OpenAI、Anthropic等數十家供應商模型的呼叫——被研究員以伺服器端請求偽造（SSRF）結合程式碼注入的組合攻擊完全攻陷。

更是史上首次，主辦單位因名額已滿而必須婉拒超過150名研究員報名。這個溢出現象，說明了整個資安研究社群的注意力正在往哪裡集中。

## 第一天：52.3萬美元，24個零時差

首日本身就創下紀錄。24個獨特漏洞被現場示範，研究員合計領取52.3萬美元獎金，平均每個漏洞約2.2萬美元。

單場最耀眼的演出來自DEVCORE研究團隊的Orange Tsai，他以串連四個邏輯漏洞的方式突破Microsoft Edge沙盒，獨斬17.5萬美元。組合多個看似無害的漏洞打造致命攻擊鏈，是DEVCORE多年來的招牌戰術。

Windows 11則成為首日最熱門的攻擊目標，三支來自不同機構的研究團隊各自找到不同路徑完成提權攻擊，每隊獲得3萬美元。三組人馬獨立挖到同類漏洞，意味著可攻擊的面積遠超微軟內部安全團隊所掌握的範圍。

第二天繼續延燒。Microsoft Exchange再度中箭，這是企業攻擊研究的長青目標。更引起AI產業關注的是：Cursor——目前全球用戶規模估計達數百萬人的AI原生程式碼編輯器——也被研究員透過未知漏洞成功攻破。

## AI安全的警鐘

LiteLLM與Cursor遭攻破，是本次賽事戰略意義最重大的發現，即便獎金金額不如Edge那麼顯眼。

LiteLLM是基礎設施層的軟體。它夾在企業內部系統與外部AI模型之間，負責認證、路由、速率限制和日誌記錄。對LiteLLM的成功攻擊，影響範圍不只是單一應用程式——攻擊者可能取得企業所有AI互動的存取權限。Pwn2Own展示的攻擊手法是：利用SSRF讓LiteLLM向內部網路服務發起請求，再透過程式碼注入漏洞取得系統完整控制權。

Cursor的問題則是另一類威脅。具備AI功能的程式碼編輯器，能看到開發者工作流程中極為敏感的內容：原始碼、設定檔中的認證金鑰、環境變數，且往往直接與雲端部署管線整合。Cursor的零時差漏洞，在理論上可被用來靜默竊取企業核心程式碼，或在開發者毫無察覺的情況下植入惡意邏輯。

主辦Pwn2Own的趨勢科技Zero Day Initiative（ZDI）今年正式將AI平台列為獨立競賽類別，背後原因是企業資安團隊持續倡議：AI專用工具鏈已足夠成熟，其漏洞面理應受到系統性研究的關注。

「AI生態系與核心企業技術，正日益暴露於複雜的串連攻擊之下，」ZDI在賽後總結中寫道。這句話的分量，在你想到LiteLLM等框架如今已深入銀行、律師事務所、醫療系統乃至政府機構的工作流程之後，會有截然不同的感受。

## 為什麼今年感覺不一樣

Pwn2Own柏林2026額滿了。這是19年來的頭一次。

逾150名研究員在名額截止後遭拒，反映的是資安社群整體焦點的結構性移位。AI工具鏈是新興產物，部署快速，往往未經過與傳統企業軟體同等嚴格的安全審核，卻已在帶著高度特權的情況下操作敏感系統。

與此同時，傳統目標依舊漏洞不絕。Windows 11、Edge、Exchange歷經多年研究員攻打與微軟大手筆的安全投資，仍在首日連續淪陷。成熟攻擊面持續出洞、全新AI攻擊面幾乎尚未被系統性審視——這個雙重組合，讓本屆柏林賽事成為近年影響最廣泛的一屆。

## 對企業的警示

Pwn2Own發現的漏洞遵循「負責任揭露」原則：廠商收到私下通知後，通常有90天時間修補後才公開揭露。微軟、LiteLLM維護者、Cursor開發商Anysphere等受影響方均已收到通知，正在趕製修補程式。

但負責任揭露不代表這些發現在修補前毫無意義。Pwn2Own示範的每一個零時差漏洞，都代表一個威脅行為者可能早已發現並悄悄利用中的漏洞類別。賽事不製造風險，只是讓既有的風險現形。

對企業資安團隊而言，柏林的賽果帶來幾個具體行動項目：LiteLLM及類似AI代理框架的部署，應重新審視網路隔離與輸入驗證控制；具備AI功能的程式碼編輯器應納入與其他開發工具相同的端點安全審查；更根本地，AI軟體必須被視為安全關鍵基礎設施，而非一般生產力工具，這個認知需要更快速地進入採購與治理流程。

AI產業過去三年大量辯論模型安全。Pwn2Own柏林2026提醒我們：模型以下的整個技術堆疊——API、代理、編輯器、調度層——同樣值得至少相等的關注。
