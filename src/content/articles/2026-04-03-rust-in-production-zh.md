---
title: "Rust 進入生產環境：那些做了轉換的公司，到底發生了什麼"
summary: "Discord 重寫了訊息儲存。Cloudflare 替換了 C++ 代理。AWS 打造了 Firecracker。經過多年炒作，真實的 Rust 遷移數據終於出來了 — 不全是好消息。"
category: "developer-tools"
publishedAt: 2026-04-03T09:20:00Z
lang: "zh"
featured: false
trending: false
sources:
  - name: "InfoQ"
    url: "https://www.infoq.com"
  - name: "GitHub Blog"
    url: "https://github.blog"
tags:
  - "rust"
  - "systems-programming"
  - "performance"
  - "developer-tools"
relatedSlugs: []
---

## 炒作週期結束了。數據出來了。

Rust 連續八年是 Stack Overflow 上「最被喜愛的程式語言」。但喜愛一個語言跟用它出貨生產程式碼是完全不同的事。

2026 年，我們終於有了足夠多的大規模 Rust 生產部署來評估真實的取捨 — 不是理論上的，是實際的工程結果。這個畫面比 Rust 傳教士或懷疑論者想承認的都更複雜。

## 明確的勝利

**Discord 的訊息儲存重寫**（Go → Rust）：尾端延遲從 130ms 降到 5ms。記憶體使用減少 10 倍。服務每天處理 400 億則訊息，用更少的伺服器。這是 Rust 的主場 — 高吞吐、低延遲的資料處理。

**Cloudflare 的 Pingora**（C++ → Rust）：取代 nginx 作為代理層。第一年記憶體安全 bug 減少 70%。效能等同 C++，安全保證大幅提升。新功能出貨更快，因為開發者不需要除錯記憶體損壞問題。

**AWS Firecracker**（從零用 Rust 打造）：驅動 Lambda 和 Fargate 的微型 VM。冷啟動低於 200ms。Rust 的型別系統防止了在多租戶 VM 主機上會是災難性的整類安全漏洞。

模式很清楚：對於**效能和記憶體安全都重要的系統級基礎設施**，Rust 兌現了它的承諾。

## 誠實的掙扎

**編譯時間仍然很痛。** 大型 Rust 專案的乾淨建構要 10-30 分鐘。增量建構好一些（1-3 分鐘）但仍比 Go 或 Java 慢。對開發者生產力來說，這比跑分更重要。

**招聘很難。** 市場上 Go 開發者大約是 Rust 開發者的 10 倍。公司回報 Rust 職位的招聘時間長 2-3 倍，薪資溢價 20-30%。

**學習曲線是真的。** 團隊回報新的 Rust 開發者需要 3-6 個月才能上手。借用檢查器、生命週期和所有權模型在概念上合理，但在實作上很有挑戰。

**不是所有東西都需要 Rust。** 幾家公司已經公開撤回了在 Web 服務和商業邏輯上的 Rust 採用，因為安全保證不能合理化生產力成本。用 Rust 寫 CRUD API 比用 Go、Python 或 TypeScript 寫同樣的 API 需要更多程式碼、更多複雜度，而且開發更慢。

## Rust 適合什麼（和不適合什麼）

**很適合**：資料庫、網路基礎設施、嵌入式系統、加密/安全、遊戲引擎、OS 元件、高頻交易。

**要考慮**：Web 後端、微服務、資料管線、ML 推理、DevOps 工具。

**不適合**：快速原型、短命腳本、開發者速度比運行時效能更重要的場景。

共識正在形成：Rust 對大約 15-20% 的軟體工程工作是正確的工具 — 那些正確性和效能不可妥協的部分。對其他 80%，以開發者時間（不是 CPU 時間）衡量更快的語言是更好的選擇。

## 觀察重點

- Linux kernel Rust 採用進度 — 如果 kernel 完全擁抱 Rust，人才池會大幅擴張
- AI 輔助 Rust 開發 — Claude 和 Cursor 寫 Rust 正在變得非常好，可能降低門檻
- Rust 基金會的永續性 — 企業贊助者很關鍵，有些正在退出
- Rust 會不會侵蝕 Go 在雲端基礎設施的領地，還是 Go 守得住

*Rust 是有史以來最好的系統程式語言。它也是大部分軟體的糟糕選擇。兩件事都是真的，接受兩者才是智慧的開始。*
