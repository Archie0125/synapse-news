---
title: "Anthropic：Claude Mythos 太危險，不能公開發布——於是打造了 Project Glasswing"
summary: "Anthropic 啟動 Project Glasswing，將旗下前沿模型 Claude Mythos Preview 限制性開放給 40 多個頂尖組織存取。這款模型已在所有主流作業系統與瀏覽器中識別出數千個零時差漏洞，其中最古老的一個已潛伏 27 年。Anthropic 認為此模型威力過強，無法公開發布，本次做法在 AI 產業史上史無前例。"
category: "ai-ml"
publishedAt: 2026-04-09
lang: "zh"
featured: false
trending: true
sources:
  - name: "Anthropic"
    url: "https://www.anthropic.com/glasswing"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/anthropic-says-its-most-powerful-ai-cyber-model-is-too-dangerous-to-release"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-latest-ai-model-identifies-thousands-of-zero-day-vulnerabilities-in-every-major-operating-system-and-every-major-web-browser-claude-mythos-preview-sparks-race-to-fix-critical-bugs-some-unpatched-for-decades"
  - name: "Fortune"
    url: "https://fortune.com/2026/04/07/anthropic-claude-mythos-model-project-glasswing-cybersecurity/"
tags:
  - "Anthropic"
  - "Claude Mythos"
  - "Project Glasswing"
  - "資安"
  - "零時差漏洞"
  - "AI 安全"
  - "前沿 AI"
relatedSlugs:
  - "2026-04-06-anthropic-claude-mythos-zh"
  - "2026-04-05-anthropic-claude-mythos-zh"
  - "2026-04-06-anthropic-emotion-vectors-zh"
---

Claude Mythos 的存在在三月下旬成為公眾知識——Anthropic 的一套內容管理系統配置錯誤，意外洩露了內部文件，描述這款模型是公司「有史以來最強大的 AI 系統」。Anthropic 確認了洩露事件，表示訓練已完成，但未透露更多。4 月 7 日，公司終於說明打算如何使用這款模型——而這個決定，在主要 AI 實驗室的歷史上前所未有。

Anthropic 不會公開發布 Claude Mythos，甚至不會向付費的 Claude 用戶開放。取而代之的是 Project Glasswing：一個由超過 40 個精選組織組成的封閉聯盟，成員包括 Amazon、Microsoft、Apple、Google、Cisco、CrowdStrike、Palo Alto Networks 和 Linux Foundation，獲准存取 Anthropic 所稱的 Claude Mythos Preview。使命只有一個：在惡意行為者能夠利用漏洞之前，用這款模型的超強能力找出並修補軟體中的安全漏洞。

Anthropic 前沿紅隊網路安全負責人 Newton Cheng 對 VentureBeat 表示：「由於 Claude Mythos Preview 的網路安全能力，我們不計劃將其公開提供。」言下之意已相當清楚：這款模型辨識和利用漏洞的能力，已經超越任何人類資安研究員——若不受約束地廣泛流通，後果將是災難性的。

## 它發現了什麼

Claude Mythos Preview 在測試中的發現規模令人難以消化。Anthropic 在受控的內部環境中，讓模型掃描了所有主流作業系統與所有主流瀏覽器的程式碼庫。結果：數千個高嚴重性的零時差漏洞——攻擊者理論上可以立即利用的未知安全缺陷。

其中不乏存在多年卻未被發現的漏洞。最震驚業界的一個：OpenBSD 中一個已潛伏 27 年的漏洞。OpenBSD 是以資安為核心設計理念的作業系統，長期被企業和關鍵基礎設施運營商視為最可信賴的選擇——這樣一個系統中的漏洞在近三十年內未被察覺，顯示生產環境軟體中未被發現漏洞的規模，可能遠遠超出業界的估計。

這些漏洞遍布整個技術棧：作業系統的核心層問題、瀏覽器引擎的解析缺陷、基礎函式庫中的記憶體安全錯誤。Project Glasswing 的合作夥伴正在緊鑼密鼓地分類和修補已揭露的漏洞，部分組織據報已在趕製緊急補丁。

Claude Mythos Preview 在 SWE-bench Verified（衡量 AI 解決真實軟體工程問題能力的基準測試）上拿到 93.9% 的成績，是目前公開報告的所有模型中最高分。其 Token 效率也是前代公開模型 Claude Opus 4.6 的 4.9 倍——對於 Glasswing 這類需要掃描數百萬行程式碼的場景，推論效率至關重要。

## 聯盟架構

Project Glasswing 採用分層存取模式。12 個「創始合作夥伴」——包括 CrowdStrike、Amazon、Apple 和 Microsoft——獲得完整存取 Mythos Preview 的權限，用於主動防禦安全工作。更廣泛的 40 多個組織聯盟則獲得研究、驗證和掃描自身程式碼庫的存取許可。Anthropic 承諾向 Project Glasswing 投入 1 億美元的模型使用點數，成員組織也將貢獻額外的使用量。

Linux Foundation 的參與格外值得關注：它的角色是協調開源專案的漏洞揭露與補丁開發——這些專案缺乏大型企業安全團隊的資源。開源生態系統是幾乎所有生產環境軟體的底層支柱，在統計上是未被發現漏洞最密集的地方之一，也是在沒有協調基礎設施支持下最難快速修補的地方。

CrowdStrike 在確認其創始成員身份的部落格文章中，將 Claude Mythos Preview 描述為「自主漏洞發現的重大躍進」，並表示模型已在掃描其自身感測器基礎設施的軟體時，識別出多個關鍵缺陷。

## 雙重用途困境的最尖銳體現

Project Glasswing 代表 Anthropic 試圖在幾乎不可能的針孔穿線：公司建造了它認為在網路安全任務上迄今最強的 AI 系統，而其回應卻是完全不讓它進入一般流通。這與傳統商業 AI 模式——快速將新能力產品化並變現——有著根本性的背離。

這個決定將受到嚴格考驗。網路安全社群普遍理解，攻擊性與防禦性能力並非乾淨地可分：同樣的模型在找到漏洞後，也可以被提示撰寫針對該漏洞的攻擊程式。將 Mythos Preview 限制於具有合約揭露義務的審查過組織，製造了有意義的障礙，但並非不可逾越。當一個 Glasswing 合作夥伴自身遭到入侵，或員工離職後帶走對模型能力的知識，會發生什麼，是一個懸而未決的問題。

還有範圍蔓延的疑慮。Project Glasswing 以防禦性計畫為框架，但幾個創始合作夥伴——Amazon、Microsoft、Apple——也是商業利益遠超純粹資安研究的重量級企業。Anthropic 如何監管許可的防禦性使用與從獨家前沿模型存取中衍生的商業優勢之間的界限，需要持續的公眾審視。

## 為何這件事的影響遠超資安本身

Claude Mythos Preview 的限制性發布，是整個 AI 產業迄今基本上迴避正面回答的一個更大問題的測試案例：當你建造出一個強大到無法安全發布的東西時，你該怎麼辦？

標準做法——分階段上線、安全微調、使用政策——預設了一款模型可以透過足夠的謹慎被調整到足夠安全以供一般部署。Project Glasswing 暗示 Anthropic 已得出結論：至少就這款模型的網路安全能力而言，無論多少微調或政策執行都無法讓一般發布成為可接受的選項。這是一條重要的分界線，公司因坦誠地解釋其推理而值得認可。

實際後果是：前沿 AI 能力變得日益分層——大型機構有資源和信譽加入 Glasswing 這樣的聯盟，較小的組織和個人則無從觸及。這種分層是否比更廣泛的存取——透過視角多樣性和防禦者的規模效應——產生更好的資安結果，是一場 AI 產業幾乎尚未開始的真實政策辯論。

眼下最緊迫的優先事項，是修補 Claude Mythos 發現的漏洞。這些缺陷是真實存在的，軟體正跑在生產環境中，而在 Glasswing 聯盟之外的某處，可能有人正在以沒那麼謹慎的意圖尋找同樣的漏洞。
