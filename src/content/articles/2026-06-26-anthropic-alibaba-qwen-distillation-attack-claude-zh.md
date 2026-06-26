---
title: "Anthropic 指控阿里巴巴 Qwen 實驗室發動史上最大規模 AI 蒸餾攻擊"
summary: "Anthropic 正式向白宮及美國參議員發出書面指控，聲稱阿里巴巴旗下 Qwen AI 實驗室以約 25,000 個虛假帳號對 Claude 進行近 2,900 萬次未授權對話，目標是竊取 Mythos Preview 模型的軟體工程與代理推理能力。此次行動規模超越此前所有已知蒸餾攻擊的總和，已促使美國兩黨議員提出緊急制裁立法草案。"
category: "ai-ml"
publishedAt: 2026-06-26
lang: "zh"
featured: true
trending: true
sources:
  - name: "The Next Web: Anthropic accuses Alibaba of running largest distillation campaign against Claude"
    url: "https://thenextweb.com/news/anthropic-accuses-alibaba-distillation-claude-qwen"
  - name: "Tom's Hardware: Anthropic claims Alibaba illicitly distilled Claude"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-claims-that-chinas-alibaba-illicitly-distilled-its-models-from-april-to-june-2026-says-effort-involved-25-000-fake-accounts-and-28-8-million-exchanges-on-claude"
  - name: "Cybersecurity Insiders: Anthropic accuses Alibaba of Distillation Attack on Claude"
    url: "https://www.cybersecurity-insiders.com/anthropic-accuses-china-alibaba-of-conducting-distillation-attack-on-claude-ai-models/"
  - name: "CryptoBriefing: Anthropic accuses Alibaba using 25,000 accounts to probe Claude"
    url: "https://cryptobriefing.com/anthropic-accuses-alibaba-claude-distillation-attack/"
tags:
  - "Anthropic"
  - "阿里巴巴"
  - "Qwen"
  - "蒸餾攻擊"
  - "AI 安全"
  - "美中科技戰"
  - "Claude"
  - "出口管制"
relatedSlugs:
  - "2026-06-13-trump-anthropic-fable5-mythos-export-controls-zh"
  - "2026-06-06-us-chip-ban-chinese-overseas-subsidiaries-zh"
  - "2026-06-22-freefable-400-experts-challenge-us-fable-mythos-ban-zh"
---

美中 AI 競賽的正面衝突，本週進入了一個危險的新階段。Anthropic 正式向白宮官員及美國參議員遞交書面指控，聲稱阿里巴巴旗下 Qwen AI 實驗室策動了迄今針對任何前沿 AI 模型的最大規模攻擊。六週時間內，約 25,000 個精心設計的虛假帳號，對 Claude 進行了近 2,900 萬次未授權對話——目標是在出口管制讓此類存取徹底不可能之前，竊取 Anthropic 最先進模型的核心智能架構。

這是 Anthropic 首次公開點名一家中國科技巨頭（而非小型 AI 新創）主導蒸餾攻擊。此番升級已震動華府，並促使兩黨議員緊急起草制裁立法。

## 蒸餾攻擊的解剖

要理解 Anthropic 指控的嚴重性，首先需要了解「蒸餾」在此脈絡下的真正含義。模型蒸餾本是一種合法的機器學習技術：讓一個較小、較快的模型學習模仿更大、更強大模型的輸出——類似一種 AI 師徒傳承，以壓縮知識而無需轉移原始模型權重。

然而，一旦被武器化，成為「對抗性蒸餾」，這項技術便搖身一變成為 AI 間諜活動的手段。攻擊者透過 API 存取，以數以百萬計的精心設計提示詞系統性地查詢前沿模型，收集其回答以建立訓練資料集。這份資料集再被用於微調本土模型，讓攻擊者得以在原創研究成本的一小部分之下，完成本來無法自主達到的能力躍升。

蒸餾攻擊之所以特別危險，在於它利用的正是前沿模型的商業可及性。Anthropic 無法完全封鎖 Claude 的存取——這是一款商業聊天機器人，開放性是其收入的基礎。但也正因如此，Claude 的智能在技術上是可以被大規模萃取的。

## 前所未見的規模

Anthropic 呈交的數字觸目驚心。從 2026 年 4 月 22 日到 6 月 5 日，與阿里巴巴 Qwen 實驗室有關聯的操作者，透過約 25,000 個虛假帳號對 Claude 發起了 2,880 萬次交流。這些帳號經過刻意設計，以躲過 Anthropic 明確禁止中國境內存取的地理管控機制。

此次攻擊的目標，是 Claude 的「軟體工程與代理推理」能力——也就是嵌入在 Mythos Preview 模型系列中、被美國政府列為出口管制對象的高價值能力。Anthropic 告知立法者，這場行動的目的是「加速中國突破 Anthropic 旗艦 Mythos Preview 模型能力的進程」。

作為對比：Anthropic 於今年 2 月揭露的三起早期攻擊，分別指向 DeepSeek、MiniMax 和 Moonshot AI，三者合計透過約 24,000 個帳號產生約 1,600 萬次交流。阿里巴巴的單一行動，在規模上超過上述三者總和將近 80%。

## Qwen 的崛起與威脅

阿里巴巴 Qwen 團隊近年迅速崛起為中國最具競爭力的 AI 研究力量。其開源模型系列多次在國際基準測試中名列前茅，能力躍升的速度也讓美國國家安全官員深感困惑——在中國 AI 產業理應面臨硬體制約的背景下，這樣的進展難以完全用已知因素解釋。

Anthropic 的信件將此次攻擊定性為蓄意的競爭策略，而非機會主義式的數據竊取。與其花費數年時間與數百億美元從合法資料從頭訓練前沿模型，不如將 Anthropic 的商業產品本身，變成向自家模型灌輸前沿能力的「免費教師」——這正是蒸餾攻擊最核心的危機所在。

阿里巴巴方面拒絕對此指控發表評論。

## 在白宮警告後仍我行我素

這場攻擊的時間點，使整件事更具挑釁意味。2026 年 4 月，白宮科技政策辦公室（OSTP）主任 Michael Kratsios 發出備忘錄，正式將 AI 模型蒸餾認定為國家安全威脅，並承諾政府將主動向美國 AI 公司通報外國蒸餾攻擊的情資。

然而，阿里巴巴的行動據稱在備忘錄發出後仍持續進行，直至 6 月初才停止。Anthropic 在信中寫道：「這場攻擊發生在行政當局明確發出警告之後。」措辭不僅將事件定位為違反服務條款，更將其框架為針對白宮明確政策立場的蓄意地緣政治挑釁。

## Anthropic 的三點核心訴求

信件包含三項具體政策請求，合計代表了 AI 公司迄今向政府提出的最激進要求。

**第一**，Anthropic 要求立法者明確反壟斷指引，允許美國 AI 公司之間共享蒸餾攻擊情報，而不必承擔競爭法風險。理由是：面對有組織的國家力量，任何單一公司都無力獨立監測，而情報共享是最自然的反制手段——但目前處於法律灰色地帶。

**第二**，Anthropic 再次力推擴大先進 AI 晶片出口管制。其隱含論點是：如果競爭方能透過 API 大規模汲取前沿模型的能力，單靠硬體禁令已不足夠，但這仍是必要的防線，必須加以維繫。

**第三**，也是最具侵略性的一點：Anthropic 要求對任何被查明透過蒸餾竊取美國 AI 系統能力的企業，直接施以財務和法律制裁——將這種技術定性為知識產權盜竊，即便其針對的是刻意對外開放的商業產品。這是一項政策新領域的突破性請求。

## 兩黨迅速響應

美國國會的反應異常迅速。共和黨參議員 Bill Hagerty 與民主黨參議員 Andy Kim 聯合宣布，計劃提出國防授權法案修正案，以「將任何被發現不當存取美國 AI 模型輸出的中國企業列入黑名單或予以制裁」。兩黨合作的框架尤為值得關注：AI 安全已成為當今美國政壇罕見的跨黨共識議題。

若該制裁機制成立，其射程將遠超現行出口管制。它不是限制硬體的輸出，而是直接針對模型智能本身的萃取行為，建立具有懲罰性的法律框架——這意味著 AI 競賽的前線，正在被官方明確承認為「已從矽片轉移到軟體」。

## 無法被出口管制完全封堵的結構性漏洞

阿里巴巴事件揭示了前沿 AI 經濟學中一個任何出口管制都難以完全彌補的結構性脆弱點。

從頭訓練一個前沿模型，需要巨量算力——這正是出口管制試圖限制的資源。但蒸餾只需要推論算力，成本更低、取得更廣泛。攻擊者只需 API 存取權限和耐性，便可執行數百萬次查詢。

若大規模蒸餾攻擊確能有效縮短美中前沿模型之間的差距，那麼 AI 出口管制的核心邏輯——「硬體稀缺可轉化為持久的模型能力優勢」——就面臨根本性的動搖。Anthropic 的這封信，也是一個警示：這場競賽的算術正在改變，而既有的政策框架，並非為此而設計。

美國在追上這一轉變之前，窗口可能已比想像中要窄。
