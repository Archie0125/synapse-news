---
title: "月之暗面發布 Kimi K3：2.8 兆參數開源模型，正面挑戰 GPT-5.5 與 Claude Opus 4.8"
summary: "北京月之暗面（Moonshot AI）發布了 Kimi K3，這是一個擁有 2.8 兆總參數的開源混合專家（MoE）模型，具備百萬 Token 上下文窗口，獨立評測顯示性能媲美 OpenAI GPT-5.5 與 Anthropic Claude Opus 4.8。完整模型權重將於 7 月 27 日公開發布，是迄今為止全球規模最大的開源 AI 模型。"
category: "ai-ml"
publishedAt: 2026-07-17
lang: "zh"
featured: true
trending: true
sources:
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/07/17/moonshot-ai-kimi-k3-model-openai-anthropic-china.html"
  - name: "Fortune"
    url: "https://fortune.com/2026/07/16/moonshots-kimi-k3-pushes-chinese-ai-into-fable-level-territory/"
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/07/16/moonshot-ai-releases-kimi-k3-a-2-8-trillion-parameter-open-moe-model-with-kimi-delta-attention-and-1m-context/"
tags:
  - "開源AI"
  - "月之暗面"
  - "Kimi K3"
  - "混合專家模型"
  - "中國AI"
  - "大型語言模型"
relatedSlugs:
  - "2026-07-17-moonshot-kimi-k3-open-weight-model-en"
  - "2026-07-16-google-gemini-35-pro-launch-zh"
---

2026 年 7 月 16 日，北京月之暗面（Moonshot AI）悄然重新洗牌了全球 AI 前沿排行榜。該公司發布了 Kimi K3——一個擁有 2.8 兆總參數的開源混合專家（MoE）模型，具備百萬 Token 上下文窗口——並宣布完整模型權重將於 7 月 27 日以寬鬆授權向公眾開放。來自 Artificial Analysis 的獨立評測顯示，其性能直接對標 OpenAI 的 GPT-5.5 和 Anthropic 的 Claude Opus 4.8，尤其在複雜多步推理與 AI 代理任務上表現突出。

對於任何追蹤 AI 前沿發展的人來說，這是一個具有里程碑意義的時刻。過去從未有任何開源模型接近這樣的規模，也從未有中國 AI 實驗室發布過能讓獨立評測機構認定與美國頂級閉源模型同等水準的產品。

## Kimi K3 的技術架構

Kimi K3 採用月之暗面內部自研的兩項核心技術構建稀疏 MoE 架構。第一項是 **Kimi Delta Attention（KDA）**：相較於標準多頭注意力機制，KDA 只計算 Token 表示之間的「差量」，而非對所有 Token 做全量注意力，大幅降低長文本處理的二次方計算成本。第二項是 **Attention Residuals（AttnRes）**：這項技術讓注意力輸出可以跨 Transformer 層混合，資訊無需逐層傳遞便可跳躍至後期階段，在不犧牲長期任務品質的前提下有效降低計算深度。

實際數字如下：模型共有 2.8 兆參數，分布在 896 個「專家」中，每個 Token 推理時只激活其中 16 個。這正是 MoE 架構的核心取捨——構建龐大的模型，但推理時只使用其中一小片，將實際計算成本控制在可接受範圍內。百萬 Token 的上下文窗口則是目前所有可量產開源模型中最長的。

發布時提供兩個版本：**K3 Max** 針對單用戶對話與標準 AI 代理任務優化；**K3 Swarm Max** 則專為大規模並行處理設計——同時運行大量代理、針對問題的不同切面並行推進——月之暗面設想將其用於複雜企業工作流，例如跨大型代碼庫重構或多步驟科學文獻綜述。

## 站上開源排行榜頂端

評測數據說明了一個具體的故事。在 MMLU-Pro、GPQA Diamond 和 LiveCodeBench 這三項最常用於區分前沿模型的評測上，Kimi K3 與 GPT-5.5 和 Claude Opus 4.8 的得分相差不超過一至兩個百分點。在某些長文本推理任務上甚至超越兩者，這與其架構對百萬 Token 高效注意力的強調完全一致。

月之暗面內部測試數據顯示：K3 在 GPQA Diamond 上得分 76.4（GPT-5.5 報告值為 77.1），在 MATH-500 上得 85.2，在 SWE-bench Verified（衡量模型解決真實 GitHub Issue 能力的知名代碼評測）上得 67.8。最後一個數字大致與 Claude Sonnet 5 在 AI 代理編碼任務上的表現相當，但仍低於 Claude 最強編碼特化配置。

數字之外，更重要的是質的轉變：這是開源模型第一次能夠有憑有據地聲稱自己站在閉源前沿同一層次。這改變了開發者、研究人員和企業能夠構建的東西——他們不再需要簽署服務條款或將數據路由到第三方 API。

## API 先行，權重隨後

Kimi K3 於 7 月 16 日在 Kimi Code 開發者平台和 Kimi 消費端應用上線，API 定價為每百萬輸入 Token 3 美元、每百萬輸出 Token 15 美元——略高於 Claude Sonnet 等級定價，但低於 Opus 4.8。網路搜索功能每次調用收費 0.015 美元。這一定價將其定位在「優質但可觸達」的區間，面向需要長上下文推理的 AI 代理開發者。

完整開源權重將於 7 月 27 日發布。這兩週的時間差是刻意為之：月之暗面希望在開源社群開始在私有基礎設施上運行模型之前，先將 API 確立為主要商業接入點。一旦權重開放，局面將徹底改變——企業和研究人員可以在自有硬體上部署 Kimi K3、訓練衍生模型，並在不依賴 API 的情況下將其整合進工作流。

## 對競爭格局的意義

今年早些時候，DeepSeek 的 V3 和 R2 版本確立了中國 AI 實驗室在特定任務上能夠比肩美國前沿模型同時開源的能力。Kimi K3 將這一模式延伸到不同方向：純粹的規模。DeepSeek 用成本效率與數學推理能力競爭，月之暗面則以能力廣度和上下文長度競爭。

對月之暗面而言，策略邏輯清晰：公司通過 Kimi 消費端應用和 Kimi Code 開發者平台產生收入，兩者均運行在自有基礎設施上。開源模型權重能夠建立開發者社群、推動 API 採用，並讓 Kimi K3 成為企業 AI 團隊評估前沿模型時的默認基線——尤其是在數據主權顧慮使美國閉源模型難以採用的市場。

對整個行業而言，這標誌著開源模型生態系統的一次成熟——成熟速度比多數人預期的快得多。十八個月前，開源與閉源前沿模型之間的差距被普遍認為是結構性的，是只有少數公司才能調動的資源優勢的產物。Kimi K3 的發布以具體方式挑戰了這一假設，力道之重是之前的開源發布所不及的。

## 晶片管制的反諷

時間節點——恰逢 2026 年世界人工智能大會於上海舉行、習近平親自出席並呼籲 AI 發展成為「全球合奏」的同一週——恐怕並非巧合。月之暗面總部位於北京，創始人楊植麟在卡內基梅隆大學受訓、曾任職 Google 研究院後回國創業，Kimi K3 現已被中國官方媒體引用，作為國內 AI 研發已達到與美國系統同等水準的佐證。

美國出口管制制度迄今限制了中國獲得最高端訓練晶片的能力。月之暗面未披露 K3 的具體訓練硬體，但公司一直在現有國產晶片和老一代英偉達硬體的限制下運營。若評測結果在獨立驗證下成立——早期跡象顯示將會如此——那麼「晶片管制足以阻止中國達到前沿 AI 能力」這一政策論據，將面臨嚴肅的重新審視。

對西方 AI 實驗室而言，當下最迫切的實際問題是：當 Kimi K3 的完整權重於 7 月 27 日全面開放後，對開源競爭格局意味著什麼？答案幾乎可以確定：大幅加速的微調、蒸餾和衍生模型開發，集中於那些與閉源模型提供商競爭最為直接的研究機構和企業社群之中。

模型現已可通過 Kimi API 調用，開發者們大概可以期待一段忙碌的兩週，等待模型權重正式落地。
