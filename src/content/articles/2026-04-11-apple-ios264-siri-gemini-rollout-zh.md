---
title: "Gemini驅動的全新Siri功能並未隨iOS 26.4推出，何時登場仍不明朗"
summary: "Apple與Google合作帶來的新Siri功能並未包含在iOS 26.4中。據報導，Apple已將目標調整為iOS 26.5與iOS 27，但目前尚不清楚哪些功能會在哪個版本推出。"
category: "products"
publishedAt: 2026-04-11T09:00:00Z
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: false
sources:
  - name: "9to5Mac"
    url: "https://9to5mac.com/2026/03/20/apples-gemini-powered-siri-upgrade-could-still-arrive-this-month/"
  - name: "MacRumors"
    url: "https://www.macrumors.com/2026/01/25/siri-google-gemini-release-date/"
  - name: "Geeky Gadgets"
    url: "https://www.geeky-gadgets.com/ios-26-4-siri-2-0-gemini/"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html"
tags:
  - "Apple"
  - "Siri"
  - "Google Gemini"
  - "iOS 26.4"
  - "Apple Intelligence"
  - "人工智慧"
  - "行動裝置"
relatedSlugs:
  - "2026-04-07-apple-ios26-sdk-msca-zh"
  - "2026-04-05-apple-business-platform-zh"
  - "2026-04-09-apple-baltra-ai-server-chip-zh"
---

五年來，Apple在AI領域最一致的故事，是一個令人尷尬的故事：Siri是全球裝機量最大的語音助理，卻不斷被擁有遠少於Apple資源的競爭對手壓著打。今年1月宣布與Google合作、以每年約10億美元的代價，用客製版Gemini替換Siri背後的AI引擎——這是Apple迄今為止對「自力打造有競爭力的大型語言模型」這一戰略已然失敗的最明確承認。

iOS 26.4功能相當豐富，但這項合作帶來的新Siri功能並未包含在內。但若你期待Siri一夜之間脫胎換骨，現實要複雜得多——而在某種程度上，這也更如實地呈現了從內部重建一個有十年歷史的語音助理的難度。

## iOS 26.4實際帶來了什麼

## 承諾與交付之間的落差

讓人沮喪的並非iOS 26.4本身不好——第一階段的功能代表著相較於前代Siri真實且有意義的進步。令人沮喪的是，Apple在1月所宣布的與眼前實際交付的內容之間，存在相當的距離。

1月12日以Apple與Google聯合聲明形式發布的公告，表示下一代Apple Foundation Models將以Gemini模型與雲端技術為基礎，協助驅動未來的Apple Intelligence功能，包括今年推出、更個人化的Siri，同時維持「Apple業界領先的隱私標準」。這項合作核心的客製化Gemini模型據報是Apple現有雲端AI模型的八倍大——一個專為Apple特定需求打造的1.2兆參數系統。

新的Siri功能並不屬於iOS 26.4。根據Bloomberg的Mark Gurman報導，Apple將改以iOS 26.5與iOS 27作為新Siri功能的目標版本，但目前尚不清楚哪些功能會在哪個版本推出。最常被引用的原因是整合複雜度：在維持Apple承諾的隱私保證的同時，將Gemini的推論導入Apple私有雲端運算架構，所需的工程工作量超出原本時程的預期。

## 隱私架構的工程挑戰

隱私工程問題值得比一句輕描淡寫更多的關注。Apple的私有雲端運算是真正前所未有的基礎設施——一套允許裝置端與雲端AI推論以Apple自身也無法存取用戶資料的方式執行的系統，並透過資安研究者公開審計的密碼學驗證機制加以保證。將1.2兆參數規模的客製化Gemini整合進這套框架，絕非普通的API對接。

核心工程挑戰在於：Gemini的對話能力——尤其是其記憶與長上下文推理——依賴的是假設模型能維持狀態並存取廣泛情境的基礎設施。而Apple的隱私架構，恰恰是為了防止這種持久性的用戶資料存取而設計的。在不犧牲Gemini能力也不損害Apple隱私保證的前提下，調和這兩種設計哲學，正是把第二階段推遲到後續版本的根本原因。

第二階段上線後，目標是讓Siri能綜合用戶完整的資料足跡——訊息、電子郵件、照片、健康資料、行事曆與第三方應用程式——以Gemini的對話流暢度進行互動，同時透過相同的私有雲端運算驗證模型運行。如果Apple能兌現，這將是前所未有的隱私故事：一個在前沿能力水準運作、卻對AI供應商提供零知識保證的兆參數對話AI。

## 商業層面的代價

對Apple而言，讓Siri重回正軌的賭注，不只是產品形象的問題。公司的核心硬體溢價——iPhone與Mac比Android替代品售價更高的理由——歷來建立在軟體品質與生態整合上。隨著AI助理日益成為人們與裝置互動的核心，一個在Google自家Android裝置上明顯落後於Gemini、或在iPhone上被用戶主動下載ChatGPT取代的Siri，正在侵蝕這個核心價值主張。

每年10億美元支付給Google的費用是一筆驚人的承諾——規模超過多數AI公司的全年總營收——反映的是Apple的判斷：授權Gemini的成本，低於持續推出平庸Siri功能所帶來的聲譽損失。但授權本身不保證成功的整合。第二階段的延誤提醒我們：難的不是取得強大AI的使用權，而是將其編織進一個感覺無縫的產品體驗。

已安裝iOS 26.4的早期採用者描述第一階段Siri改進為「明顯更好，但還不是革命性的更好」——這個評語或許相當公允。真正的考驗將在9月到來，屆時iOS 27會攜帶完整的第二階段能力上線。如果Apple兌現了1月的承諾，敘事將從「Apple的AI困境持續」轉向「Apple解決了其他人從未嘗試的隱私問題」。如果第二階段再度延誤，每年10億美元的Gemini合約，將成為Apple承認競爭差距卻仍無法在自己時程內補足的昂貴佐證。

Apple產品週期的歷史告訴我們，第一代交付的功能很少是完整故事。但用戶等待Siri升級，已經等了太多年。他們的耐心，就像第二階段的推出一樣，是有截止日期的。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 15 處。*
