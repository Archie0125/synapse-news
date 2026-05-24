---
title: "AWS 推出 AgentCore Payments：AI 代理人可透過穩定幣自主付款"
summary: "Amazon Web Services 推出 Amazon Bedrock AgentCore Payments，這是一套為自主 AI 代理人設計的託管支付基礎設施，與 Coinbase 和 Stripe 合作開發，讓代理人能透過 USDC 穩定幣進行即時交易。系統採用 x402 HTTP 支付協議，在 Base 網路上結算時間約 200 毫秒，每筆費用不到一美分的零頭。"
category: "ai-ml"
publishedAt: 2026-05-24
lang: "zh"
featured: false
trending: true
sources:
  - name: "AWS Machine Learning Blog"
    url: "https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/"
  - name: "CoinDesk"
    url: "https://www.coindesk.com/business/2026/05/07/amazon-rolls-out-ai-agent-stablecoin-payments-platform-with-coinbase-and-stripe"
  - name: "The Block"
    url: "https://www.theblock.co/post/400421/aws-taps-coinbase-and-stripe-to-power-usdc-payments-for-ai-agents"
tags:
  - "aws"
  - "amazon"
  - "ai-agents"
  - "stablecoin"
  - "coinbase"
  - "stripe"
  - "payments"
relatedSlugs:
  - "2026-05-03-microsoft-365-e7-agent-365-ga-zh"
  - "2026-05-19-google-io-2026-developer-tools-gemma4-gemini32-firebase-zh"
---

自主 AI 代理人究竟該如何處理「錢」的問題，長期以來是代理人 AI 技術棧中最模糊的一環。代理人現在已能瀏覽網頁、撰寫程式碼、管理日曆、發送郵件——但當它們需要支付資料訂閱費、購買專用 API 使用權，或補償另一個代理人提供的服務時，往往就此碰壁。2026 年 5 月 7 日，這個局面因 Amazon Web Services 的一項宣布而改變：AWS 推出了 Amazon Bedrock AgentCore Payments，這是第一套為自主代理人量身打造的託管支付基礎設施，與 Coinbase 及 Stripe 聯合開發，採用的是穩定幣而非傳統信用卡軌道。

此宣布在「What's Next with AWS 2026」活動上發布，使 AWS 成為第一個為「代理人經濟」的財務管道提供生產就緒解決方案的主要雲端服務商。

## 它解決了什麼問題

在多步驟代理人工作流程中，自主 AI 代理人經常遇到需要付費才能存取的端點：即時金融數據 API、高階氣象與衛星資料、專業研究數據庫，以及日益增多的「付費 AI 代理服務」。在沒有原生支付機制的情況下，開發者必須為每個付費資源各自建構計費整合，這是一個碎片化且耗時的過程，嚴重限制了多步驟代理人的能力邊界。

AgentCore Payments 消除了這種摩擦。系統採用 x402 協議——Coinbase 開發的直接內嵌於 HTTP 協議的開放支付標準。當代理人向付費端點發送請求並收到 HTTP 402「Payment Required」響應時（這個狀態碼自 1996 年就存在於 HTTP 規範中，卻幾乎從未被實際使用），AgentCore 支付引擎就會啟動：它驗證配置的錢包身份、執行穩定幣轉帳、將加密支付證明附加到請求標頭，然後重新發送原始請求，整個過程都在持續的執行循環中完成。對代理人而言，交易是透明的；對端點而言，付款是可驗證的。

結算在以太坊 Base 二層網路或 Solana 上使用 USD Coin（USDC）完成，耗時約 200 毫秒，每筆費用不到一美分——比傳統信用卡微支付便宜數個數量級。傳統卡片交換費讓一美元以下的交易根本不具備經濟可行性，而 USDC 鏈上結算則徹底改寫了這個算式。

## 兩種錢包路徑，一套治理模型

透過 Amazon Bedrock 部署代理人的開發者，可以選擇連接 Coinbase CDP 錢包或 Stripe Privy 錢包作為支付憑證。兩個選項都支持會話級支出上限——作為自主消費的限制器，開發者可以授權代理人每次會話最多花費 10 美元，防止代理人故障或遇到設計不良的端點時導致費用滾雪球式累積。

系統還附帶可觀測性工具，為開發者提供代理人每一筆交易的完整記錄：端點位址、金額、時間戳記以及觸發支付的任務上下文。這是一個關鍵的補充：隨著代理人開始代表用戶和企業採取財務行動，審計和歸因支出的能力已成為合規與法律責任的基本要求。

Stripe 的參與意義不止於錢包管理。Stripe Privy 錢包基礎設施帶來了法幣入場管道和企業級密鑰管理，讓過去未涉足加密基礎設施的公司也能透過熟悉的 Stripe 介面部署代理人支付。Coinbase 則帶來了 x402 Bazaar，這是一個精選的 x402 端點目錄，代理人可以程式化地搜尋和存取——實際上就是一個針對機器消費優化的可付費服務市場。

## x402 協議：HTTP 沉睡已久的支付層

AgentCore Payments 的技術核心是 Coinbase 在 2025 年 5 月推出的 x402 協議。該協議重新啟用了 HTTP 402 狀態碼——RFC 規範中原本保留給「需要付款」的代碼——作為端點向機器發送的原生信號，表示在交付響應之前需要先獲得補償。任何採用 x402 的伺服器，無需建立自訂計費後端即可立即參與代理人間的商業交易。

AWS 對 x402 的背書，是這個協議首次進入企業級生產基礎設施的規模化部署。AWS 表示將推動 x402 成為正式的 IETF 標準——一旦成功，將進一步鞏固穩定幣微支付作為 AI 代理人互動預設財務層的地位。

## 代理人今天能買什麼，明天又能買什麼

在目前的預覽版本中，AgentCore Payments 支持 API、資料訂閱、付費內容和 MCP（模型情境協議）伺服器的微支付。x402 Bazaar 中已列出金融市場數據端點、研究數據庫、地理空間數據提供商，以及多個提供代碼審查、翻譯和摘要服務的 AI 代理。

AWS 已透露路線圖遠不止微支付。未來版本的 AgentCore Payments 計劃支持更高金額的交易：酒店和航班預訂、供應鏈採購訂單以及商戶付款。在這個規模下，治理和可觀測性基礎設施變得更加關鍵——能夠代表企業預訂差旅或下採購訂單的代理人，需要多層授權和審計記錄，而現有的會話限制模型需要進一步演進。

## 代理人經濟的新底層

AgentCore Payments 更深層的意涵是結構性的：它為正在成形的代理人對代理人服務經濟提供了財務基礎。如果一個代理人能夠可靠地向另一個代理人付費——且接收方能在不到一秒的時間內確認付款已結算——那麼建構專業化代理人的激勵結構將發生根本性改變。擁有高品質即時翻譯代理人或特定領域研究代理人的開發者，無需建構計費基礎設施、簽署企業合約或管理用戶帳戶，就能直接透過 x402 端點變現。

對仍對加密貨幣持謹慎態度的企業而言，USDC 提供了一個相對穩定的入口：USDC 是受監管、充分儲備的美元穩定幣，Stripe Privy 錢包路徑則將大部分區塊鏈複雜性隱藏在熟悉的企業控制介面之後。AWS 的賭注是：鏈上微支付的運營優勢足夠引人注目，企業願意接受實現它所需的加密基礎設施——尤其是當代理人經濟開始交付具體 ROI 的時候。

這個賭注能否成功，取決於 x402 端點生態系統的成長速度。但隨著 AWS、Coinbase 和 Stripe 同時背書這一標準，自主代理人商業交易的基礎設施，已史上首次達到生產就緒的狀態。
