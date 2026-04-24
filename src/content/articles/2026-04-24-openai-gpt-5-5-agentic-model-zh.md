---
title: "OpenAI 發布 GPT-5.5：能自主規劃、寫程式、執行任務的新世代 AI"
summary: "OpenAI 於 4 月 23 日發布迄今最強大的代理型模型 GPT-5.5，在 Terminal-Bench 2.0 測試中得分 82.7%，GDPval 職業能力測試達 84.9%。模型運行於 NVIDIA GB200 NVL72 架構，已為超過 1 萬名 NVIDIA 員工的 Codex 提供支援，API 定價為每百萬輸入／輸出 tokens 各 $5/$30 美元。"
category: "ai-ml"
publishedAt: 2026-04-24
lang: "zh"
featured: true
trending: true
sources:
  - name: "OpenAI 官方部落格"
    url: "https://openai.com/index/introducing-gpt-5-5/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/"
  - name: "NVIDIA Blog"
    url: "https://blogs.nvidia.com/blog/openai-codex-gpt-5-5-ai-agents/"
  - name: "The Decoder"
    url: "https://the-decoder.com/openai-unveils-gpt-5-5-claims-a-new-class-of-intelligence-at-double-the-api-price/"
tags:
  - "OpenAI"
  - "GPT-5.5"
  - "AI代理"
  - "自主AI"
  - "Codex"
  - "NVIDIA"
  - "大型語言模型"
relatedSlugs:
  - "2026-04-24-openai-gpt-5-5-agentic-model-en"
  - "2026-04-23-meta-model-capability-initiative-tracking-zh"
---

OpenAI 於 4 月 23 日正式發布 GPT-5.5，這款經過完整重新訓練的模型被該公司稱為「迄今最聰明、最直覺」的版本——而各項測試數據確實撐得起這個說法。GPT-5.5 在 Artificial Analysis 智慧指數中以 60 分奪冠，領先第二名的 Claude Opus 4.7 與 Gemini 3.1 Pro Preview（均為 57 分）三個百分點。

這次發布絕非小幅升級。GPT-5.5 代表 OpenAI 對「代理型工作」的全面押注：給模型一項複雜、多步驟的任務，它會自行規劃、呼叫工具、核查結果、應對模糊情況，直到完成為止。這讓它從「更強的聊天機器人」躍升為自主 AI「數位工作者」的基礎設施。

## 跨代理任務的全面測試領先

OpenAI 發布了一份完整的評測成績單，全面佐證 GPT-5.5 在真實部署場景中的最強地位：

- **Terminal-Bench 2.0**（需要規劃、迭代與工具協調的複雜命令列工作流程）：**82.7%**，較 GPT-5.4 的 75.1% 提升 7.6 個百分點。
- **SWE-Bench Pro**（真實 GitHub 問題解決能力）：**58.6%**，單次完整解決任務的比率超越任何前代模型。
- **GDPval**（涵蓋法律研究、財務分析等 44 種職業的代理人表現）：**84.9%**。
- **OSWorld-Verified**（自主操作真實電腦環境）：**78.7%**。
- **Tau2-bench 電信客服**（複雜客服工作流程自動化）：零提示調整下達 **98.0%**。
- **Expert-SWE**（OpenAI 內部程式碼評測）：**73.1%**，GPT-5.4 為 68.5%。

綜合來看，這些數字顯示模型在代理能力上已跨越重要門檻——不只是在「描述」任務，而是能在多元、高風險的場景中可靠地「完成」它們。

## Codex 搭載 GPT-5.5，NVIDIA 已大規模部署

最具體的部署訊號來自 NVIDIA。GPT-5.5 現已為 OpenAI 的代理程式設計應用 Codex 提供動力，運行於 NVIDIA GB200 NVL72 機架規模系統上。根據 NVIDIA 的說法，超過 **1 萬名員工**——涵蓋工程、產品、法務、行銷、財務、業務、人資及營運——已在日常工作中使用由 GPT-5.5 驅動的 Codex。

這是企業全面採用代理型 AI 的重要概念驗證。硬體面的背景同樣關鍵：NVIDIA GB200 NVL72 系統相比前一代基礎設施，每百萬 tokens 成本低 35 倍，每瓦每秒輸出 tokens 速率高 50 倍。GPT-5.5 從設計之初就針對 GB200 和 GB300 NVL72 系統進行聯合優化，是首批與執行硬體深度協同設計的前沿模型之一。

據悉，OpenAI 內部將此模型代號定為「Spud」（馬鈴薯），與其對外的宏大定位形成有趣反差，但這符合該公司一貫低調的內部命名傳統。

## 實際使用上的根本轉變

對開發者與企業用戶而言，最重要的改變在於模型「行為方式」，而非僅僅是數字。GPT-5.5 能更快理解使用者意圖，並自行承擔更多執行工作。前幾代模型在處理複雜任務時，需要細緻的逐步引導才能穩定運作；GPT-5.5 的設計目標是接受模糊、未完整定義的指令，並產出乾淨、經過驗證的成果。

實際上，這意味著使用者可以把一份雜亂的研究大綱、一個需求不明確的多檔案程式庫，或是複雜的客服工作流程交給模型——預期它能做出合理推斷、適當呼叫工具、自我核查輸出，並完成任務，而不需要持續介入引導。

OpenAI 將這種轉變定位為邁向「數位工作者」的關鍵一步：不只輔助人類，而是自主承擔完整的工作流。GPT-5.5 的強項特別體現在：撰寫與除錯程式碼、進行線上研究、分析資料、建立文件與試算表、操作軟體介面，以及跨工具串聯執行。

## 定價：成本加倍，但所需 tokens 更少

對 API 開發者而言，GPT-5.5 帶來明顯的價格調漲：**每百萬輸入 tokens 5 美元、輸出 tokens 30 美元**，是 GPT-5.4（$2.50/$15）的整整兩倍。重度代理使用場景的 Pro 方案更高達 $30/$180 每百萬 tokens。

OpenAI 與第三方評測機構 Artificial Analysis 均指出，GPT-5.5 在同等代理任務上所需 tokens 數量比前代減少約 **40%**，這在很大程度上抵消了單價漲幅。實際工作負載的淨成本增加估計約為 **20%**——對於輸出品質能帶來對應回報的應用來說，仍在可接受範圍內。

服務自 4 月 23 日起立即向 ChatGPT Plus、Pro、Business 及 Enterprise 訂閱者開放，API 存取同步開通。

## 競爭格局再次洗牌

這次發布重新設定了前沿競爭的基準線。Anthropic 幾天前剛發布的 Claude Opus 4.7 曾短暫奪下智慧指數榜首，GPT-5.5 在不到一週內便將其取代。2026 年，前沿模型的超越速度已大幅加快，Anthropic、Google、xAI 與 OpenAI 的重大發布接連而至。

對於正在評估基礎模型選型的企業而言，這種波動既是機遇也是風險。GPT-5.5 在代理能力測試上的強勁表現，使其成為當前自主工作流自動化的首選——但頂尖模型之間的差距正在收窄，一個月後的格局或許又大不相同。

可以確定的是，業界已不再爭論「AI 能否自主處理複雜任務」，而是在問：哪款模型最可靠、成本如何、有哪些治理機制可以依靠。GPT-5.5 在 2026 年代理 AI 浪潮中率先出招——但競爭對手正密切盯著它的每一步。
