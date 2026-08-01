---
title: "Anthropic的Claude Mythos在60小時內破解了讓密碼學家兩年束手無策的後量子加密算法"
summary: "Anthropic在7月28日揭露，其尚未公開發布的Claude Mythos Preview模型發現了HAWK後量子數位簽名方案的一個結構性弱點——這項算法正在NIST標準化審查中——使金鑰恢復攻擊成本降低了6,700萬倍，是AI輔助密碼分析能力的一次標誌性展示。"
category: "ai-ml"
publishedAt: 2026-08-01
lang: "zh"
featured: false
trending: true
sources:
  - name: "The Hacker News — Claude AI Just Cracked a Post-Quantum Test Scheme"
    url: "https://thehackernews.com/2026/07/claude-ai-just-cracked-post-quantum.html"
  - name: "Anthropic Research — Discovering Cryptographic Weaknesses with Claude"
    url: "https://www.anthropic.com/research/discovering-cryptographic-weaknesses"
  - name: "CyberScoop — Anthropic's Claude Mythos Finds Weaknesses in Encryption Algorithms"
    url: "https://cyberscoop.com/anthropic-claude-mythos-encryption-flaws-hawk-aes-pqc/"
  - name: "TechTimes — AI Cracks Post-Quantum Cipher in 60 Hours"
    url: "https://www.techtimes.com/articles/321876/20260728/ai-cracks-post-quantum-cipher-60-hours-after-two-years-human-review-failed.htm"
tags:
  - "Anthropic"
  - "Claude Mythos"
  - "後量子密碼學"
  - "HAWK"
  - "NIST"
  - "密碼分析"
  - "AI安全"
relatedSlugs:
  - "2026-08-01-anthropic-claude-mythos-hawk-post-quantum-cryptanalysis-en"
  - "2026-07-31-anthropic-claude-hacked-3-organizations-cyber-tests-zh"
---

7月28日，一則同時震撼AI安全與密碼學界的揭露出現了：Anthropic宣布，其尚未正式發布的Claude Mythos Preview模型，做到了一件全球密碼學家花了整整兩年都沒能完成的事——發現HAWK算法中一個具有實質意義的結構性弱點。

HAWK是NIST（美國國家標準暨技術研究院）後量子數位簽名標準化競賽的主要候選方案之一。這份揭露以研究論文與公司部落格文章的形式同步發布，描述了Anthropic研究人員如何引導Claude Mythos自主探索密碼算法中的缺陷。模型在大約60小時的分析中——耗費約10萬美元的API費用——發現了HAWK數學結構中一個此前被忽略的對稱性，大幅降低了金鑰恢復攻擊的運算成本。

這項發現引出了一個政策制定者、安全架構師和AI研究人員在未來數月都將不得不面對的問題：如果前沿AI模型能夠破解通過多年專家審查的加密方案，這對最強大AI系統的對抗性能力——以及保護網際網路的基礎設施安全——意味著什麼？

## HAWK是什麼，為什麼重要

HAWK是一種格密碼學（lattice-based）數位簽名方案，由歐洲學術聯盟開發，提交至NIST後量子密碼學標準化流程。與目前保障絕大多數加密通訊的RSA和橢圓曲線算法不同——後者會被足夠強大的量子電腦破解——HAWK的設計目標是在後量子時代依然安全。

NIST的後量子密碼學標準化流程自2016年啟動，被普遍視為史上最嚴格的公開密碼學評估之一。每項提交方案都要經過多年公開學術審查，全球頂尖密碼學家受邀探查任何可能的弱點。HAWK在多輪審查中完好無缺，從未有已知的可利用結構性漏洞被公開記錄。

這份紀錄，現在有了一個新的但書。

## 攻擊手法：Mythos發現了什麼

Anthropic在用詞上非常謹慎，這是合理的。Claude Mythos發現的弱點是真實的、經過數學驗證的，也是全新的——但其實際影響範圍是有限度的。

模型在HAWK的簽名和金鑰生成過程中，識別出一個未被利用的對稱性。藉由利用這個對稱性，攻擊者可以將HAWK-256（最小參數集，適用於效能優先的環境）的完整金鑰恢復成本，從約2的64次方次運算降低至約2的38次方次運算。難度降低了大約6,700萬倍——從在現代硬體上需要數年才能完成的計算，變成以相當但非超凡的資源就理論上可行的攻擊。

同樣的漏洞對HAWK-512和HAWK-1024——在安全冗餘度優先的環境中使用的較大參數集——幾乎沒有影響。針對這些配置的攻擊在計算上仍然不可行。

Anthropic另外披露，Claude Mythos還發現了針對七輪縮減版AES-128的更快攻擊，但公司指出這一改進並不適用於完整的AES-128（使用十輪），後者依然是業界最久經考驗的對稱加密標準之一。

## 過程：60小時、10萬美元、由AI完成

Anthropic所描述的研究過程，其意義幾乎不亞於具體的發現本身。研究人員並非給了Claude Mythos一個預設的攻擊策略讓它去驗證——他們給了它HAWK的學術規格文件、現有的密碼分析文獻和數學推理工具，然後讓它嘗試破解這個方案。

搜尋、開發和驗證HAWK攻擊的過程耗時約60小時，消耗約10萬美元的API費用。HAWK和AES兩條研究線各自的花費規模相近。

對比之下：NIST後量子密碼學審查流程未能發現這個弱點，涉及了全球數百位頂尖密碼學家多年的工作。成本差距是驚人的。以那個規模動用人類專家的時間，輕易就要花上數千萬美元；而AI完成了同樣的工作，費用僅在五位數。

Anthropic明確指出，這不是對人類密碼學家的簡單否定。模型具備人類難以匹敵的優勢：它可以系統性地窮舉潛在的攻擊策略，並在不出現疲勞錯誤的情況下核查數學推導。但它也有局限——需要大量人工搭建任務框架，其輸出在發表前也需要深度的專家驗證。

## 產業與政策影響

這項揭露發生在AI安全和密碼標準社群都感到不安的時刻。

對AI安全研究者而言，這一發現驗證了他們對前沿AI「網路安全鄰近能力」的擔憂。Anthropic此前已披露其AI模型在內部測試中入侵了三個組織；HAWK的結果展示了一類相關但不同的風險——不是利用已知漏洞的能力，而是發現此前未知漏洞的能力。

Anthropic明確表示，這些結果「不影響生產系統，也不需要對已部署的軟體進行更改」。完整的AES-128沒有被破解。HAWK-512和HAWK-1024沒有被破解。HAWK-256中發現的弱點是標準化層面的結構性顧慮，而非立即的部署緊急事件。

NIST已獲通知，預計將在標準化流程中評估這項發現。HAWK的提交者——包括CWI阿姆斯特丹的Léo Ducas等研究人員——確認收到了Anthropic的揭露，並表示將在NIST意見期限內提供技術回應。

對密碼學界而言，這項發現的影響更著眼於未來而非當下。如果現在這一代的前沿模型能夠在兩年公開專家審查後發現新型攻擊，當模型能力再提升一個數量級時，又或者當對抗性行為者在沒有道德護欄的情況下部署類似技術時，會發生什麼？

## 前沿AI的雙用途困境

Anthropic的主動揭露，是在一個保持沉默本可更輕鬆（甚至短期而言更安全）的領域，刻意選擇了透明。公司認為——與其長期公開的安全承諾一致——現在就曝光AI的密碼分析能力，在影響可控的情況下，能給安全社群留出應對時間，讓他們在更強大的模型讓局面更難收拾之前就採取行動。

這個論點有其道理。NIST後量子密碼學流程存在的意義，正是在算法大規模部署之前進行壓力測試。在公開的研究合作中現在就發現HAWK-256的弱點，在類別上好過在部署後因對抗性入侵而被發現。

但這項揭露同時也展示了前沿AI開發核心的雙用途張力。幫助研究人員在部署前發現並修復密碼漏洞的同一種能力，若落入掌握同等能力模型但缺乏Anthropic揭露文化的國家級對手手中，完全可以被指向已大規模部署的算法。

AI能力與密碼分析能力之間的競賽，現在已被公開承認正在進行。NIST的後量子標準化流程未來必須將AI輔助審查作為標準工具納入——安全社群也需要決定：是否應常態化地將AI模型用於密碼候選方案的對抗性探查，並公開輸出結果？還是說這種做法的雙用途風險，製造的問題比解決的更多？

這場辯論，六個月前整個領域還沒準備好面對。Claude Mythos已將它強制推上了議程。
