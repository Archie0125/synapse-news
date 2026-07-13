---
title: "Meta推出Muse Spark 1.1並開放首個付費AI API，正式進軍開發者市場"
summary: "Meta於7月9日發布Muse Spark 1.1，同步開放Meta Model API公開預覽，開啟公司首個付費AI服務。這款多模態代理人模型以每百萬輸入tokens 1.25美元定價，直接對標Anthropic與OpenAI的開發者API市場。祖克柏更打破三年沉默、重返X平台宣告這項消息。"
category: "ai-ml"
publishedAt: 2026-07-13
lang: "zh"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/07/09/meta-enters-the-crowded-ai-coding-battle-with-muse-spark-1-1/"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-07-09/meta-starts-charging-for-ai-with-muse-spark-1-1-agentic-model"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/07/09/meta-launches-flagship-muse-spark-1-1-model-multi-agent-upgrades/"
  - name: "DataCamp"
    url: "https://www.datacamp.com/blog/muse-spark-1-1"
tags:
  - "Meta"
  - "Muse Spark"
  - "AI模型"
  - "API"
  - "代理人AI"
  - "程式開發"
  - "多模態"
relatedSlugs:
  - "2026-07-05-meta-watermelon-model-gpt55-parity-zh"
  - "2026-07-03-meta-zuckerberg-ai-agents-slower-zh"
---

Meta花了好幾年時間打造強大的AI模型，然後免費釋出。2026年7月9日，這一切改變了。公司發布Muse Spark 1.1——其4月首款旗艦模型的升級版——同步在公開預覽階段推出Meta Model API，正式宣告進軍付費AI服務市場。這是一個分水嶺時刻：最後一家主要免費分發旗艦模型的大型AI實驗室，決定免費時代已告終結。

執行長馬克・祖克柏為這次發布畫龍點睛，在X上發布了三年多來的第一則推文，將Muse Spark 1.1描述為「一款強大的代理人與程式開發模型，定價非常親民」，並補充「更多模型即將推出」。重返X的象徵意義不容小覷——那個Meta曾公開批評、並試圖以Threads取而代之的平台。

## Muse Spark 1.1能做什麼

Muse Spark 1.1定位為一款專為代理人任務打造的多模態推理模型。根據Meta技術部落格，其核心優勢在於工具使用、電腦操控（computer use）、程式開發，以及多代理人協調。模型配備一百萬token的上下文視窗——在同等定價區間的競品中屬於領先水準——並設計為在長篇、複雜任務序列中維持連貫的狀態管理。

多代理人架構尤其值得關注。Meta將Muse Spark 1.1設計為能在代理人管線中扮演兩種截然不同的角色：作為協調者（orchestrator），它能蒐集上下文、制定多步驟計劃，並將執行委派給並行子代理人；作為子代理人（subagent），它能遵循主協調者的指令、管理可用工具集，並在需要時識別何時應向上呈報決策。這種雙模式設計專為企業自動化管線量身打造，適用於工作流程中不同環節可能運行在不同能力層級的場景。

程式開發是旗艦應用場景。Meta將模型描述為針對「大型代理人工作負載、修復程式錯誤、以及處理大規模程式碼遷移」優化，這正是Anthropic的Claude Code和GitHub Copilot在企業市場深耕的類別。發布後不久在社群媒體上流傳的第三方基準測試結果顯示，Muse Spark 1.1在長篇程式開發任務的指令遵循品質上，可與Claude Haiku 4.5和GPT-5.6 Luna這兩款同等定價區間的模型相抗衡。

## 定價策略與競爭定位

Meta Model API採用簡明定價：每百萬輸入tokens收費1.25美元、輸出tokens收費4.25美元，新帳戶享有20美元免費額度。這使Muse Spark 1.1的成本位於Anthropic Claude Haiku 4.5和OpenAI最具效率的GPT-5.6 Luna變體的同等水準——有意定位在開發者在高量推理工作負載中平衡品質與成本的甜蜜點。

定價決策具有策略意涵。Meta並未將Muse Spark 1.1定為高價品——如OpenAI的GPT-5.6 Sol每百萬輸入tokens收費5美元——也沒有走近乎免費的商品路線。公司以合理的企業定價入市，表明其目標是從AI服務建立真實的營收來源，而非以API作為品牌流量的虧損領頭羊。

對整個AI產業而言，Meta進入付費API市場之所以重要，在於其基礎設施優勢。Meta運營著全球最大規模的資料中心之一，並一直在打造自製晶片——其Iris推理晶片預計於2026年9月投入量產，由台積電製造、博通協助設計——專門用於降低推理成本。若Meta能以低於Anthropic或OpenAI的單位成本服務Muse Spark 1.1，同時收取相當的費用，它將擁有結構性的盈利優勢，既能提升開發者體驗，又能持續投入模型品質改善。

## Meta超級智能實驗室的脈絡

Muse Spark 1.1是Meta超級智能實驗室（MSL）推出的第二款產品。MSL是祖克柏在2026年初設立的部門，旨在將Meta的前沿AI研究整合至統一的組織架構下。MSL在Meta內部有點像一家獨立創業公司——擁有專屬算力、從Meta FAIR和外部招募組成的研究團隊，以及以具競爭力的節奏推出前沿模型的使命。

這種實驗室模式，部分是對人才壓力的回應。過去18個月，Meta持續面臨研究人員流向Anthropic、xAI和OpenAI的壓力，因為那些完全專注於前沿AI的實驗室提供了股權誘因和使命驅動的文化。透過將MSL打造為獨立品牌身份——有別於面向大眾的Llama模型系列——Meta試圖為希望研究最先進系統、又不願離開的研究員提供更具吸引力的內部目的地。

將Muse Spark 1.1定位為商業產品而非開源發布，也標誌著Meta對前沿模型開發與商業價值之間關係認識的轉變。Llama依然開放且免費——Meta並未放棄開源AI策略。但公司打造的最強前沿模型現在是商業授權的，暗示即便以Meta的規模，「免費為王」的路線也存在它最終難以為繼的極限。

## 這個API對開發者意味著什麼

Meta Model API對開發者的實際意義相當深遠。7月9日之前，取得Meta AI能力的主要管道，是透過消費端產品（WhatsApp、Instagram、Messenger上的Meta AI），或是透過AWS Bedrock和Azure AI Foundry等第三方雲端供應商取得Llama模型存取。這兩種管道都無法提供構建生產級AI應用所需的直連、低延遲API存取。

新API改變了這一切。開發者現在可以透過REST API直接調用Muse Spark 1.1，與標準工具使用框架整合，並以適合企業部署的吞吐量水準存取模型。發布時的API文件支援函數呼叫、串流回應、多輪對話，以及系統提示詞自訂——這些都是Claude和GPT-4用戶已使用超過兩年的標準工具組合。

新帳戶20美元免費額度是經典的開發者獲客手段，模仿了OpenAI和Anthropic在各自API發布初期的做法。Meta押注於：嘗試過Muse Spark 1.1並發現其在更低定價下仍具競爭力的開發者，會留下來成為付費用戶。

## 後續展望

祖克柏在發布公告結尾的那句「更多模型即將推出」，暗示Muse Spark 1.1只是開局，而非全部底牌。Meta有足夠的算力在多個能力層級訓練和部署模型，商業API基礎設施也已到位，可以進行商業化。

更重要的問題是：Meta姍姍來遲的付費AI服務，能否在Anthropic和OpenAI已領先18至24個月開發者關係積累的市場中奪得可觀的心智份額。API市場中，分發優勢至關重要：一旦開發者圍繞特定模型供應商建構了整合、提示詞和評估框架，切換成本就是真實存在的。Meta需要在品質、定價或可靠性上勝出——理想上三者兼備——才能在開發者已做出選擇的生產環境中取代現有廠商。

可以確定的是，Meta的加入改變了AI API市場的競爭動態。三家擁有真正具競爭力前沿模型、並提供商業定價的廠商，對Anthropic和OpenAI形成了雙雄鼎立時代所不具備的定價壓力。對企業客戶而言，這種壓力值得期待。
