---
title: "微軟一口氣發布七款自研AI模型，宣示脫離OpenAI依賴"
summary: "在舊金山舉辦的Build 2026大會上，微軟發布七款自主研發的MAI系列AI模型，涵蓋推理、程式碼生成、語音、轉錄及圖像等領域，全部從頭訓練，不使用OpenAI或任何第三方蒸餾技術。這是微軟AI主管Mustafa Suleiman口中「長期自給自足」戰略的最清晰宣示，標誌著這家OpenAI最大金主的AI戰略正式轉向。"
category: "ai-ml"
publishedAt: 2026-06-17
lang: "zh"
featured: false
trending: true
sources:
  - name: "Microsoft AI Blog"
    url: "https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html"
  - name: "GeekWire"
    url: "https://www.geekwire.com/2026/microsoft-unveils-seven-homegrown-ai-models-in-bid-for-long-term-self-sufficiency/"
  - name: "Windows Central"
    url: "https://www.windowscentral.com/software-apps/microsoft-launches-seven-in-house-ai-models-to-cut-developer-costs-and-reduce-reliance-on-openai"
tags:
  - "微軟"
  - "MAI模型"
  - "OpenAI"
  - "推理模型"
  - "程式碼生成AI"
  - "Build 2026"
  - "Mustafa Suleiman"
  - "AI自給自足"
relatedSlugs:
  - "2026-06-16-github-copilot-metered-billing-backlash-zh"
  - "2026-04-04-cursor-devin-war-zh"
---

過去四年，微軟的AI策略可以用一句話概括：相信OpenAI就對了。微軟向ChatGPT的母公司砸下逾130億美元，把OpenAI的模型深度嵌入Azure、Office、Windows和GitHub Copilot，整個AI商業敘事都建立在Sam Altman的模型之上。

這個時代，正在走向終結。

6月2日，在舊金山的Build 2026大會上，微軟AI事業執行長Mustafa Suleiman（2024年從DeepMind挖角而來）公開發布七款自主研發的MAI系列模型。這七款模型全部由微軟研究人員從頭訓練，使用商業授權資料，不採用OpenAI或任何第三方模型的蒸餾技術。這是微軟迄今最清晰的訊號：它打算擁有自己的AI技術棧。

「前沿模型訓練所使用的算力已增長了一兆倍，」Suleiman在Build現場表示，「我們預計未來三年還將再增長一千倍。打造一台不斷攀登的機器，才是在這場競賽中保持優勢的方式。」

## 七款模型，七個賭注

MAI系列涵蓋了企業客戶和開發者目前最主要的所有需求。

**MAI-Thinking-1** 是微軟的旗艦推理模型，針對複雜的多步驟任務設計。這款模型擁有350億活躍參數和25.6萬token的上下文視窗，專門應對那些讓較小模型束手無策的長篇、模糊、多跳躍推理任務。盲測結果顯示，獨立評審偏好它勝過Claude Sonnet 4.6，在軟體工程評測上表現與Claude Opus 4.6相當。Suleiman特別強調，MAI-Thinking-1完全以內部策劃的乾淨資料訓練，與業界普遍使用外部更強模型蒸餾的做法形成對比。

**MAI-Code-1-Flash** 是一款推理效率優先的程式碼生成模型，約有50億活躍參數。它鎖定的是成本敏感型市場——那些需要可靠程式碼生成與編輯，卻無法負擔最新前沿模型高額費用的開發者。目前已整合進GitHub Copilot和VS Code，在高流量、低風險的程式碼任務中運行，並在真正複雜的問題上才調用更強的算力。

**MAI-Transcribe-1.5** 在43種語言的轉錄準確率上達到業界最高水準，速度是競品的五倍，並支援特定領域術語。微軟表示，它在多語言評測上勝過Gemini和OpenAI的轉錄模型。這款模型直接針對企業客服中心、法律轉錄和全球支援業務市場。

**MAI-Voice-2** 能在超過15種語言中生成高品質語音，並可透過短暫音訊樣本適應新的聲音特徵。成本更低的Flash版本預計即將推出，並持續擴展支援語言數量。

**MAI-Image-2.5** 和 **MAI-Image-2.5-Flash** 是微軟首次以自研技術進軍文字生成圖像與圖像編輯領域。完整版據稱在競技場（Arena）評分上勝過同等級競品，Flash版則以部分畫質換取顯著的速度與成本優勢。

## 戰略邏輯

微軟對OpenAI的依賴從來都是雙面刃。這段合作讓公司在AI產品開發和雲端AI服務上搶得先機，但也製造了結構性脆弱：一旦微軟與OpenAI的關係生變——無論是治理分歧、商業利益衝突，還是OpenAI自己做大後帶來的競爭張力——微軟的整個AI戰略就岌岌可危。

這種風險並非假設。OpenAI透過API持續建立自己的企業客戶關係，直接與Azure的AI服務競爭。即將到來的IPO將賦予OpenAI更強的資本實力和獨立性，讓合作關係更有可能演化。微軟現在著手自建模型，正是因為它無法等到合作關係真正破裂才開始行動。

微軟與自家晶片團隊聯合開發的Maia 200晶片，構成這套基礎設施的底層，據稱能相對等效GPU工作負載帶來1.4倍的效能提升。擁有晶片、模型和應用三個層次，是完整的垂直整合佈局——讓微軟站上與Google（以TPU跑Gemini）和亞馬遜（以Trainium和Inferentia跑AWS）同等的結構性位置。

## 開發者怎麼看

Build現場開發者的反應相當分歧。一方面，在推理、程式碼生成、轉錄、語音和圖像各領域增添具有成本競爭力的模型，確實擴充了Azure AI客戶可用的選項；MAI-Code-1-Flash在早期測試中因速度和穩定性獲得好評。

另一方面，微軟推出模型並非首次——Phi系列小型語言模型算是一個成功案例，但始終未能在生產環境中取代OpenAI或Anthropic的模型。問題在於，MAI系列究竟是類似的利基產品，還是微軟終於打造出能在前沿品質上真正競爭的模型。

與Sonnet 4.6和Opus 4.6在程式碼評測上的比較頗具意義，但尚未具決定性。Anthropic的Claude模型在專業程式碼市場佔據主導地位——Cursor、Windsurf、GitHub Copilot都把複雜程式任務路由給Claude。要改變這種偏好，需要的是持續的高性能表現加上具競爭力的定價，而非僅憑單一基準測試的比較。

## 對OpenAI意味著什麼

這則公告的第一直覺是：對OpenAI不利。更準確的版本：情況比較複雜。

微軟仍是OpenAI最大的投資方，Azure仍是OpenAI的主要算力供應商。這段關係在雙方都產生巨額收入，不太可能迅速瓦解。但微軟在Build的訊息非常明確：它不再滿足於扮演AI最強大的轉售商，它要成為AI的生產者。

對OpenAI而言，這意味著最重要的市場推廣夥伴同時成了競爭對手。對更廣泛的AI市場而言，繼Google和亞馬遜之後，第三家宣示要從晶片到產品全棧自主的科技巨頭正式登場。AI模型高度集中的時代可能正走向終結，取而代之的是每家主要雲端供應商都自己跑前沿實驗室的新格局。

Suleiman說得毫不含糊：「長期自給自足不是備案，而是戰略本身。」

對台灣的科技業者來說，這個轉變有雙重意涵：一是微軟的AI服務生態將更多元，供應商鎖定的風險降低；二是整個AI模型市場的競爭格局將更分散，評估和選型的決策複雜度也隨之提升。
