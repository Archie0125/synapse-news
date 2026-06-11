---
title: "MetaMask 讓 AI 代理擁有 DeFi 錢包——但套上了韁繩"
summary: "MetaMask 推出 Agent Wallet，這是專為自主 AI 代理設計的自托管加密錢包，可在 10 條區塊鏈網路上執行 DeFi 交易。系統引入護衛模式與野獸模式，讓用戶精確定義代理的自主程度，同時對每筆交易強制執行安全檢查。"
category: "products"
publishedAt: 2026-06-11
lang: "zh"
featured: false
trending: false
sources:
  - name: "MetaMask"
    url: "https://metamask.io/news/metamask-launches-agent-wallet-giving-ai-agents-full-defi-access-with-default-security-on-every-transaction"
  - name: "CoinDesk"
    url: "https://www.coindesk.com/tech/2026/06/08/metamask-launches-ai-agent-wallet-with-built-in-security-for-crypto-trades"
  - name: "CryptoSlate"
    url: "https://cryptoslate.com/metamask-just-gave-ai-agents-a-defi-wallet-with-a-leash"
  - name: "CoinTribune"
    url: "https://www.cointribune.com/en/crypto-metamask-opens-defi-to-autonomous-ai-agents/"
tags:
  - "metamask"
  - "DeFi"
  - "AI代理"
  - "加密貨幣"
  - "web3"
  - "consensys"
  - "自主交易"
relatedSlugs:
  - "2026-06-09-openai-chatgpt-superapp-aria-agents-zh"
  - "2026-06-11-cognition-devin-1b-26b-valuation-zh"
  - "2026-06-11-anthropic-2026-agentic-coding-trends-report-zh"
---

AI 代理與去中心化金融的交叉點，多年來一直停留在理論討論層面——紙上聽起來很美，實際落地卻困難重重。缺失的關鍵是基礎設施：自主代理需要能持有真實資產、簽署交易、與 DeFi 協議互動的錢包，同時又不需要在每一步都等待人工批准，還要保護用戶免受將財務控制權交給可能出錯或被操縱的軟體所帶來的顯而易見的風險。

2026 年 6 月 8 日，MetaMask 上線了這套基礎設施。Agent Wallet 是專為自主 AI 代理打造的自托管加密錢包，允許代理在去中心化交易所進行現貨交換、建立永續合約倉位、參與預測市場以及提供流動性——全程在用戶預先定義的安全規則範圍內運作。

「鏈上經濟的下一輪大擴張，不會只靠人類驅動，」ConsenSys 執行長 Joe Lubin 在發布活動上表示。「代理將管理真實資本，做出真實的財務決策。」

## Agent Wallet 如何運作

產品有兩種操作模式，代表自主性與安全性平衡上的不同取捨點。

**護衛模式（Guard Mode）**是預設模式。在此模式下，代理的每筆交易都必須符合用戶自訂的參數：每日支出上限、已批准協議白名單，以及用戶未明確允許的交易類型的硬性停止規則。任何超出這些參數、或被 MetaMask 安全掃描標記為潛在惡意的交易，都需要通過雙重身份驗證獲得人工批准才能執行。護衛模式為希望讓代理處理日常 DeFi 操作、但又想對任何異常情況保持知情的用戶而設計。

**野獸模式（Beast Mode）**降低了中斷頻率。在野獸模式下，錢包對每筆交易應用 Blockaid 的自動威脅掃描和 MEV（最大可提取價值）保護，但只在系統偵測到明確惡意交易時才觸發人工雙重驗證。這個名稱刻意帶有攻擊性，定位於高度信任自己代理、希望代理快速運作的資深交易員和開發者。

無論哪種模式，MetaMask 的交易保護計劃對系統認為安全的交易提供最高 1 萬美元的保障。協議層安全架構——簽名前的交易模擬、MEV 保護、透過 Blockaid 進行的威脅掃描——無論在哪種模式下都會對所有交易執行。

## 支援的網路與 DeFi 基礎操作

Agent Wallet 目前支援 10 條區塊鏈網路：以太坊、Linea、Arbitrum、Avalanche、Optimism、Base、Polygon、BSC、Sei 和 Hyperliquid。初始網路名單的廣度值得注意——涵蓋主要的以太坊 Layer 2（Arbitrum、Optimism、Base、Linea、Polygon）、以太坊主網、兩條 DeFi 活躍度較高的非以太坊鏈（Avalanche、BSC），以及鏈上永續合約的主導平台 Hyperliquid。

代理可存取的 DeFi 基礎操作涵蓋鏈上交易的核心功能：現貨交換、永續合約、預測市場（包括 Polymarket）和流動性提供。這意味著持有 Agent Wallet 的代理，可以建立和管理此前需要人工交易員持續關注、或需要客製化智能合約基礎設施才能操作的複雜 DeFi 倉位。

錢包對框架沒有偏好。基於 OpenAI API、Anthropic Claude、Nous Research 模型或其他任何框架構建的代理，均可通過目前處於早期測試的標準 CLI 介面接入 Agent Wallet。

## 市場機遇：從 54 億美元到 2360 億美元

MetaMask 的產品時機，與一條難以忽視的市場軌跡緊密相連。全球 AI 代理市場在 2024 年估值約 54 億美元；分析師預測到 2034 年將達到 2360 億美元，複合年增長率約 45%。隨著代理的普及和承擔越來越重要的經濟任務，代理持有和花費資產的能力——而不只是提供建議——成為結構性需求而非可選功能。

這個市場的 DeFi 維度尤其值得關注。去中心化金融協議累計鎖定了數百億美元的價值，主要平台每日交易量常超過 500 億美元。目前這些協議的用戶群高度集中於技術水平較高的個人，他們能夠管理錢包安全、理解協議風險並主動監控倉位。以 DeFi 交易系統形式部署的 AI 代理，可以通過將 DeFi 的技術複雜性抽象為目標導向介面，大幅擴展潛在用戶群體。

對於截至 2026 年初擁有逾 3000 萬月活躍用戶的 MetaMask 而言，Agent Wallet 代表著對一次平台轉型的戰略押注。MetaMask 的收入歷來主要來自用戶交換交易的手續費。如果 AI 代理成為 DeFi 市場的重要參與者——執行高頻策略、管理收益倉位、進行套利——MetaMask 的基礎設施層將直接處於交易流中。

## 安全架構作為競爭護城河

在發布活動中，MetaMask 選擇以安全架構而非能力廣度為中心，反映了刻意的市場定位決策。MetaMask 的安全堆疊——十年久經考驗的錢包基礎設施、Blockaid 的威脅情報、所有交易的 MEV 保護——是新進入者難以快速複製的。

這一點至關重要，因為自主 AI 交易代理的風險特徵與人類用戶在質上有所不同。人類可以識別釣魚嘗試、在批准可疑交易前暫停思考、對異常行為進行背景判斷。AI 代理在沒有明確防護措施的情況下，無法可靠地做到這些。DeFi 的歷史中充斥著讓老練人類用戶損失慘重的駭客攻擊、捲款跑路和漏洞利用。一個在沒有強健交易級安全防護的情況下運作的 AI 代理，將成為攻擊目標。

MetaMask 的做法——對每筆交易強制執行威脅掃描、用戶定義的政策護欄、對系統批准的交易提供保障——嘗試在將人從執行迴路中移除的同時，保留關鍵的人工保護機制。這個架構是否足以保護在對抗性鏈上環境中運作的代理，隨著產品從早期測試走向正式上線，答案將逐漸清晰。

## 早期測試與正式上線路線圖

初期推出規模有限：早期測試計劃約 200 名用戶，通過 CLI 獲得存取權限。產品團隊描述「數月內」進行更廣泛的推出，目標在 2026 年夏季實現全面上線。

以 CLI 為先的方式表明，初期受眾是開發者和代理構建者，而非一般用戶——他們正在構建交易機器人、投資組合管理代理和 DeFi 自動化工具，而不是尋找即插即用自主交易產品的個人。對於在金融情境中 AI 代理的安全性和行為特性仍在建立認知的環境中推出的產品來說，這是正確的推出順序。

這次發布也是對整個 AI 代理生態走向的一個信號。過去兩年，AI 代理的主流敘事集中在信息工作——寫作、編程、研究、客服。MetaMask 的產品提醒我們，代理正越來越多地被委以重要的經濟決策，而支撐這種信任的基礎設施，需要以金融服務基礎設施所要求的同等嚴格標準來構建。

對於在任何涉及真實資產的場景中部署代理的 AI 構建者——無論是加密貨幣、金融市場還是商業交易——Agent Wallet 安全模型中的設計選擇都值得仔細研究。MetaMask 為代理套上的這條「韁繩」，很可能是整個產品中最重要的功能。
