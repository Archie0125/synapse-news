---
title: "Supabase 以 105 億美元估值完成 5 億美元 F 輪融資，AI 程式設計工具重塑資料庫市場"
summary: "這家開源 Firebase 替代方案在 GIC 領投下完成 5 億美元 F 輪融資，八個月內估值翻倍。Anthropic 的 Claude Code 現已成為 Supabase 平台上最大的資料庫建立來源，超越所有人類開發者，揭示軟體基礎設施行業的結構性轉變。"
category: "developer-tools"
publishedAt: 2026-06-07
lang: "zh"
featured: true
trending: true
sources:
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/06/04/database-startup-supabase-raises-500-million-10point5-billion-valuation.html"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/06/04/supabase-raises-500m-ai-coding-tools-drive-phenomenal-growth/"
  - name: "TechStartups"
    url: "https://techstartups.com/2026/06/05/supabase-hits-10-5b-valuation-after-500m-funding-round-as-vibe-coding-drives-explosive-growth/"
tags:
  - "supabase"
  - "資料庫"
  - "開發者工具"
  - "氛圍程式設計"
  - "AI程式設計"
  - "新創融資"
  - "F輪"
relatedSlugs:
  - "2026-06-01-github-copilot-ai-credits-billing-change-zh"
  - "2026-04-04-cursor-devin-war-zh"
  - "2026-04-04-mcp-protocol-explosion-zh"
---

當 Supabase 執行長 Paul Copplestone 向投資人描述公司今年上半年的成長時，他拿出了一個出人意料的數據：平台上大多數新建資料庫，已不再出自人類開發者之手。「AI 程式設計助理現在佔了 Supabase 資料庫建立量的大多數，」Copplestone 說。更具體而言，Anthropic 的 Claude Code 已成為單一最大貢獻者——超越了所有個別人類客戶。

這個驚人的數字正是 Supabase 在 6 月 4 日宣布 5 億美元 F 輪融資的核心引擎，融資後估值達 105 億美元。本輪由新加坡主權財富基金 GIC 領投，參與方包括 Accel、Y Combinator、Craft Ventures、Felicis、Coatue，以及值得關注的支付巨頭 Stripe。這個估值較 2025 年 10 月的 50 億美元幾乎翻倍，距離上輪融資僅八個月。

## 「氛圍程式設計」帶來的紅利

「Vibe coding（氛圍程式設計）」這個詞已從網路梗圖演變成真實的市場類別。AI 程式設計工具讓開發者——甚至是非技術人員——只需以自然語言描述需求，就能由 Claude Code、OpenAI Codex 或 GitHub Copilot 等 AI 代理生成完整的程式碼，從前端介面到資料庫結構一氣呵成。Supabase 正好坐落在這條關鍵路徑上：當 AI 代理搭建新應用時，幾乎都需要後端資料庫、身份驗證和儲存層，而 Supabase 已成為預設答案。

這帶來了 Accel 合夥人口中「在資料庫層從未見過」的成長速度。Supabase 目前擁有超過 25 萬名客戶，員工約 350 人——對於這個估值量級的公司而言，是相當精簡的規模，也體現了公司以自動化為核心的文化。

Supabase 由 Copplestone 與技術長 Ant Wilson 於 2020 年創立，定位為 Google Firebase 的開源替代方案。不同於 Firebase 將開發者鎖定在 Google 生態系，Supabase 建立在 PostgreSQL 這個黃金標準的開源關聯式資料庫之上。這個架構選擇帶來了巨大的回報：PostgreSQL 的擴充套件生態——包括用於儲存 AI 向量嵌入的 pgvector——在大多數新創公司尚未察覺之前，就已讓 Supabase 完美定位於生成式 AI 浪潮中。

## 資金的用途

新資金將加速數個策略佈局。最引人注目的是 Supabase 預覽的新架構 **Multigres**，旨在協助應用程式突破通常迫使新創公司轉向更複雜分散式資料庫系統的擴展瓶頸。這個挑戰十分現實：AI 生成應用的快速成長意味著平台上的工作負載從零到大規模的速度，遠超傳統人工開發應用。

公司也持續投資向量資料庫能力。隨著 AI 應用大量湧現，儲存和檢索高維向量嵌入——支撐語義搜尋、RAG 管線和推薦系統的數值表示——已從利基工作負載變成核心需求。Supabase 原生整合 pgvector 的方式，給了它相對於缺乏關聯式能力的專用向量資料庫的明顯優勢。

身份驗證和儲存同樣是競爭護城河。當 AI 代理端對端建構應用時，通常傾向選擇能一站式處理資料、驗證和檔案三大支柱的單一供應商。Supabase 的整合式方案讓它成為阻力最小的路徑。

## 一種新型基礎設施公司

Supabase 本輪融資揭示了一個正在重塑企業軟體市場的更廣泛動態：AI 代理正成為一類全新的、規模龐大的客戶群。傳統開發者工具公司的成長靠的是說服個別工程師或工程團隊採用產品，銷售動作以人為核心——開發者關係、研討會贊助、文件品質、Hacker News 上的口碑。

這個模式依然重要，但如今又疊加了第二個成長向量：在 AI 程式設計工具中贏得預設推薦位。當 Claude Code 決定要啟動哪個資料庫時，這個決策受到模型訓練資料、可用工具和競爭對手文件品質的影響。Supabase 顯然在當前這一代中贏得了這場競爭，Claude Code 成為其最大的單一新資料庫來源。

這形成了一個具有顯著複利效應的飛輪。越多 AI 創建的資料庫，就意味著越多使用模式數據、越廣的開發者心智佔有率，以及 AI 模型提供商繼續推薦 Supabase 的更多理由。當然這也帶來風險：如果未來一代 AI 程式設計工具轉而偏好競爭對手——如 PlanetScale、Neon 或某家超大規模雲端商的託管 Postgres 方案——Supabase 的成長可能如同加速時一樣突然中斷。

開源基礎為公司提供了一定程度的保險。由於 Supabase 可以自行託管，它維持著一個草根開發者社群，能夠獨立於任何 AI 模型的推薦之外，持續貢獻口碑和文件。

## 更大的生態系統訊號

Stripe 的參與特別值得關注。這家支付公司正在悄悄建立開發者生態系統——Stripe 在代理式商務的佈局顯示，它把 AI 原生應用層視為下一個前沿。投資 Supabase——AI 生成應用的預設後端——與其說是純財務投注，不如說是戰略卡位。

對投資人而言，本輪融資代表對資料庫和後端基礎設施層能夠持續捕獲重要市值的信心。105 億美元的估值是否合理，取決於 Multigres 和向量資料庫路線圖能多快擴大每位客戶的平均營收，以及 AI 程式設計工具的順風車能持續多久。但有一點毋庸置疑：氛圍程式設計時代已造就了一批新的基礎設施贏家，而 Supabase 目前是其中最鮮明的例子。
