---
title: "Together AI完成8億美元C輪融資，估值達83億美元，開源推理需求飆升"
summary: "AI基礎設施新雲端服務商Together AI宣布完成8億美元C輪融資，由沙烏地阿拉伯石油公司旗下的Aramco Ventures領投，估值達83億美元。公司年度訂單量已突破11.5億美元，反映出企業市場對開源AI基礎設施的強勁需求——作為閉源模型API的替代選項，開源推理正加速主流化。"
category: "startups"
publishedAt: 2026-07-07
lang: "zh"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation/"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/319657/20260703/together-ai-raises-800m-open-source-inference-breaks-1b-closed-models-stall.htm"
  - name: "Yahoo Finance"
    url: "https://finance.yahoo.com/technology/ai/articles/open-source-ai-firm-together-110520468.html"
tags:
  - "together-ai"
  - "AI基礎設施"
  - "開源"
  - "融資"
  - "GPU雲端"
  - "推理"
relatedSlugs:
  - "2026-07-07-together-ai-800m-series-c-open-source-inference-en"
  - "2026-07-07-microsoft-mai-thinking-1-code-1-flash-launch-zh"
  - "2026-07-05-oxmiq-raja-koduri-35m-series-a-gpu-architecture-zh"
---

開源AI基礎設施市場剛收到了迄今最強烈的一張信心票。

Together AI於2026年7月1日宣布，完成8億美元C輪融資，公司估值躍升至**83億美元**。本輪由沙烏地阿美石油公司投資部門Aramco Ventures領投，其他投資方包括Vista Equity Partners、General Catalyst、Emergence Capital、輝達（Nvidia）、March Capital、廣達電腦旗下Pegatron，以及SentinelOne的S Ventures等。

這是Together AI迄今最大規模的單輪融資，較約16個月前以33億美元估值完成的3.05億美元B輪估值翻倍以上。更值得注意的是，公司上一季度年度訂單量已突破 **11.5億美元**，顯示Together AI的基礎設施已成為大量企業AI部署真正不可或缺的核心組件。

## Together AI做什麼

Together AI運營的是業界稱為「**AI新雲端**（AI neocloud）」的業務：一個從零開始為AI工作負載設計的超大規模GPU運算平台，有別於傳統雲端廠商在通用基礎設施上補裝AI能力的做法。公司租用Nvidia GPU叢集，並提供針對開源模型深度優化的推理API服務，涵蓋Meta Llama系列、Mistral系列、DeepSeek-R1、Qwen及其他數十個開放權重模型。

對企業客戶的價值主張簡單明瞭：開源模型已在大量基準測試中達到乃至超越閉源模型的水準，但在生產環境大規模運行這些模型，需要龐大的GPU基礎設施、模型優化專業知識和可靠的服務層——這些都是多數企業無法自行構建的能力。Together AI將這一切打包為托管服務，讓企業享受開源AI的靈活性與成本優勢，同時免去基礎設施的運維負擔。

## 市場為何向這個方向移動

Together AI訂單的激增，反映了企業AI戰略兩年來一直積累的結構性轉變。GPT-4剛發布時，閉源前沿模型與開源替代品之間的差距相當明顯，大多數企業預設選擇OpenAI、Anthropic和Google的API服務。這個差距如今已大幅縮小。

Llama 4、DeepSeek-R1和Mistral最新模型在大量實際任務上，已能與GPT-5.5和Claude Fable的表現競爭，而在專用GPU基礎設施上運行這些模型的成本，遠低於按量計費的API訪問。對每日需要處理數百萬次推理請求的企業——客服系統、文件處理流水線、內部知識助手、程式碼工具——這個成本差異足以激勵做出切換選擇。

開源基礎設施還提供了閉源API無法給予的核心優勢：**資料隱私與模型客製化**。金融、醫療、法律等受監管行業的企業，通常不能將敏感資料發送給第三方API端點。在企業自行掌控的專用基礎設施上運行開源模型，消除了這個合規障礙。在私有資料上進行微調（閉源模型提供商支援有限），對開放權重模型則完全沒有限制。

## Aramco Ventures領投的戰略意涵

由Aramco Ventures擔任領投方，不只是資本層面的選擇，背後帶有深遠的戰略意涵。沙烏地阿拉伯作為Vision 2030經濟多元化計劃的一部分，正積極投資AI基礎設施，已向多家AI企業做出重大的資料中心投入承諾。Aramco Ventures在本輪領投，暗示雙方可能存在更深層的合作關係——Together AI的基礎設施版圖可能將大幅向中東延伸，包括在沙烏地阿拉伯本地的資料中心部署。

對Together AI而言，一個既有資本實力又有區域基礎設施擴張雄心的核心投資方，提供了純財務投資者無法給予的國際化路徑。

## 五年基礎設施規模擴大50倍

Together AI計劃使用C輪資金，在未來五年將基礎設施規模擴大約 **50倍**——這意味著從當前數千張GPU，擴展到數十萬張。公司尚未具體說明優先採購哪些GPU架構，但隱含的是對輝達Blackwell及後續架構持續需求的重大押注，同時也布局新興開放替代方案。

這個規模目標也傳遞出Together AI的野心：不只是與CoreWeave、Lambda Labs、Vast.ai等其他AI新雲端競爭，更可能向AWS、Azure、GCP等主要超大型雲端廠商發起挑戰——隨著企業AI工作負載持續向開源模型和專業化推理基礎設施遷移。

## 開源AI基礎設施市場的大局

Together AI的融資，發生在AI基礎設施賽道整體高度活躍的背景下。競爭對手CoreWeave於今年3月以230億美元估值上市，為AI基礎設施企業在公開市場實現持久價值提供了先例。

基礎設施層越來越被認為是AI價值鏈中最具持久性的位置之一。頂級模型的能力正在收斂——主要實驗室之間前沿模型的效能差距正在縮小——但在企業規模下可靠地服務這些模型所需的算力基礎設施，仍是一個巨大的運營挑戰。能夠可靠地、大規模地解決這個問題，尤其是針對開源模型的企業，占據了一個難以快速複製的市場位置。

以11.5億美元年度訂單、剛到手的8億美元新資金，以及50倍基礎設施擴張的明確路線圖，Together AI正在邁向成為這個世代定義性的開源AI基礎設施公司。支撐開源AI革命的底層算力軌道之爭，已正式進入白熱化。
