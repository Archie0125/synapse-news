---
title: "GitHub Copilot依Token計費新制引爆開發者強烈反彈"
summary: "GitHub於6月1日正式將Copilot切換至依使用量計費的AI積分模式，以Token消耗量取代原有的固定優質請求額度。開發者隨即反映月度積分在數小時內耗盡——有人因一次程式碼修改請求就燒掉逾6美元——引發大規模出走威脅，以及要求GitHub撤回此變更的強烈聲浪。"
category: "developer-tools"
publishedAt: 2026-06-16
lang: "zh"
featured: false
trending: false
sources:
  - name: "The Register"
    url: "https://www.theregister.com/ai-and-ml/2026/06/02/github-copilot-users-threaten-exit-as-metered-billing-kicks-in/5249826"
  - name: "gHacks Tech News"
    url: "https://www.ghacks.net/2026/06/02/github-copilot-usage-based-billing-takes-effect-drawing-developer-backlash-over-rapid-credit-depletion/"
  - name: "MLQ News"
    url: "https://mlq.ai/news/github-copilot-switches-to-token-based-billing-june-1-drawing-developer-backlash/"
  - name: "Windows Forum"
    url: "https://windowsforum.com/threads/copilot-to-usage-billing-june-1-2026-ai-credits-token-costs-and-meter-shock.420900/"
tags:
  - "GitHub"
  - "Copilot"
  - "微軟"
  - "開發者工具"
  - "AI編程"
  - "計費模式"
  - "代理AI"
relatedSlugs:
  - "2026-06-16-spacex-acquires-cursor-60-billion-zh"
  - "2026-06-16-alibaba-qwen-robot-suite-embodied-ai-zh"
---

當GitHub於2026年6月1日正式將其AI程式助手Copilot切換至依使用量計費模式時，公司以為是在解決一個商業問題。結果，這一舉措引發了該平台有史以來最激烈的開發者反彈——用戶紛紛反映月度積分在數小時內耗盡，甚至有開發者因一次程式碼修改請求就燒掉逾6美元。

這次轉型以「GitHub AI積分」取代原有的「優質請求」模式，依Token使用量計費，幾個月前便已預告。GitHub解釋，現在驅動Copilot的複雜自主代理工作流程，消耗的算力遠超固定月費訂閱模式所能維持的水準。但開發者反應的速度與規模，讓就連平台最堅定的支持者也措手不及。

## 6月1日後的變化

訂閱費沒有調漲。GitHub Copilot Pro每月仍為10美元；Pro+為39美元；Business每個座位19美元；Enterprise為39美元。但在這些數字之下，計費機制發生了根本性改變。

點數分配取代了原有的優質請求額度：組織版每用戶每月1,900積分，企業版3,900積分——現有客戶在2026年9月1日前將獲得過渡期加贈積分（分別為3,000和7,000），作為緩衝。積分消耗速度視任務而異：簡單的自動補全成本極低，而涉及程式碼庫索引、跨檔案編輯或呼叫進階推理模型的延伸代理會話則消耗大量積分。

最直接的問題在於可預測性。舊系統告訴用戶每月有固定的優質請求數——例如300次——這是一個可以明確規劃的數字。新系統按消耗的Token數量計費，而Token數量會因提示複雜度、上下文大小及處理請求的底層模型而大幅變動。許多用戶發現自己嚴重低估了積分的消耗速度。

## 一則引爆輿論的6美元投訴

讓開發者怒火集中爆發的，是一篇迅速在技術論壇上廣傳的貼文：一位GitHub Copilot Business訂閱者向專案提交了一個修改請求，結果單次互動就燒掉逾6美元積分。以這個消耗速度，19美元/月的Business訂閱不到四個月的日常編程就會耗盡。

在GitHub社群論壇、Hacker News和Reddit上，大量用戶反映了類似的經歷。浮現出的規律十分一致：代理式任務——例如要求Copilot「修復這個Bug」或「跨多個檔案重構這個函數」——比非代理介面消耗多得多的積分，因為模型在索引上下文、規劃步驟、執行子任務並最終呈現結果的整個過程中，都在持續消耗積分。

「透明度幾乎為零，」一位開發者在Hacker News上寫道，「在事後之前，我根本不知道點擊『修復』會花10積分還是500積分。」

## GitHub的回應

GitHub迅速在介面中新增了更清晰的積分使用量指示，並發布了各操作消耗積分的詳細說明。公司也確認，Business和Enterprise客戶的過渡期加贈積分將延續至9月1日，給予用戶更多調整工作流程的空間。

GitHub在一篇部落格文章中為此次轉型辯護：「Copilot現在驅動的工作流程遠比以前複雜，消耗的算力也大得多。現有模式已無法在繼續提供開發者應得的AI輔助品質的同時保持可持續性。」

公司也指出仍有Copilot免費層級可選——每月提供50次聊天補全和2,000次程式碼補全——作為無法接受依使用量計費的用戶的基礎選項。批評者則指出，免費層級的額度過低，無法作為專業用戶的有效替代方案。

## 競爭壓力

這場反彈出現在GitHub戰略上最為敏感的時刻。AI程式助手市場的競爭從未如此激烈。Cursor——剛與SpaceX達成600億美元收購協議——其Pro方案每月固定20美元，標準功能無使用量限制。JetBrains AI Assistant和Tabnine均已宣布將維持固定費率模式，直接回應GitHub的轉型舉措。

Cursor尤其是Copilot動盪的最大受益者。這款受開發者青睞的AI IDE在整個2025年已持續從GitHub搶奪市場份額；計費爭議進一步加速了這一遷移。六月初流傳的開發者調查顯示，有23%使用Copilot的受訪者計劃或已轉向其他工具。

「GitHub在用長期的開發者忠誠度換取短期的收入優化，」一位分析師指出，「開發者不像一般SaaS用戶——如果覺得被宰，他們會換工具。而且他們會把這件事告訴所有認識的人。」

## 更廣泛的AI計費難題

GitHub的遭遇指向整個行業共同面臨的挑戰：當AI工具的能力大幅提升——算力消耗也大幅增加——如何在不讓讓這些工具成功的用戶感到被背棄的前提下合理定價？

這一矛盾並非GitHub獨有。OpenAI在2026年初將ChatGPT Plus的GPT-5系列模型設為預設後也調漲了費用，引發類似投訴。Anthropic對Claude Pro的每日訊息限制方案也曾讓重度用戶感到沮喪。每個案例中，AI提供商都面臨相同的結構性問題：當平均用戶會話消耗的算力相對有限時，固定費率訂閱是合理的；但代理AI會話可能消耗是普通聊天的50倍算力。

從提供商角度看，依使用量計費在經濟上是合理的。但正如GitHub正在發現的，它對用戶體驗而言，是對固定月費所代表的簡單性和可預測性的重大退步。開發者評估工具不僅看能力，還看可預測性、信任感，以及是否被公平對待的感受。

## 開發者的訴求

開發者社群的反饋指向幾個明確需求：在請求執行前提供更好的積分預估、設定硬性月上限以防止超支意外，以及——最重要的——可預測性。核心訴求並非關於絕對費用；許多開發者承認，20-30美元/月換取節省數小時工作是合理的。訴求是對控制權和透明度的渴望。

如果GitHub能解決可預測性問題——在開發者確認操作前精確顯示消耗積分數，並提供可設定的預算硬性停止——底層計費模式或許比當前情緒所反映的更具持久性。

如果做不到，這次轉型可能最終成為加速AI編程市場永久性去中心化的轉折點，使市場從GitHub歷史性的主導地位散開。同月宣布的SpaceX以600億美元收購Cursor的消息，則意味著市場上已出現資本雄厚、且對待開發者理念截然不同的強力競爭者。
