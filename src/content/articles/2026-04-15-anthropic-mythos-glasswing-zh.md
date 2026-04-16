---
title: "Anthropic AI 發現數千個零時差漏洞，卻選擇不公開——轉而砸 1 億美元成立資安防禦聯盟"
summary: "Anthropic 的 Claude Mythos Preview 自主識別出各大作業系統與瀏覽器中數千個此前未知的安全漏洞，其中一個潛伏長達 27 年。Anthropic 認定模型風險過高，決定不對外公開，轉而推出「玻璃翼計畫」，攜手 11 家科技巨頭投入 1 億美元，搶在攻擊者利用類似 AI 能力之前修補關鍵軟體弱點。"
category: "ai-ml"
publishedAt: 2026-04-15T09:05:00Z
lang: "zh"
featured: true
trending: true
sources:
  - name: "Anthropic — 玻璃翼計畫"
    url: "https://www.anthropic.com/glasswing"
  - name: "The Hacker News — Anthropic Claude Mythos 發現數千個零時差漏洞"
    url: "https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html"
  - name: "VentureBeat — Anthropic 表示最強資安 AI 模型過於危險，不予公開"
    url: "https://venturebeat.com/technology/anthropic-says-its-most-powerful-ai-cyber-model-is-too-dangerous-to-release"
  - name: "Axios — Anthropic 因 Mythos 駭客能力過強而限制發布"
    url: "https://www.axios.com/2026/04/07/anthropic-mythos-preview-cybersecurity-risks"
tags:
  - "Anthropic"
  - "Claude Mythos"
  - "資安"
  - "零時差漏洞"
  - "玻璃翼計畫"
  - "AI安全"
relatedSlugs:
  - "2026-04-15-openai-gpt54-cyber-model-zh"
---

4 月 7 日，Anthropic 發布了一則震驚資安業界與 AI 研究圈的聲明：其最新前沿模型 Claude Mythos Preview，已悄然自主地在全球使用最廣泛的軟體中，發現了數千個零時差漏洞（zero-day）——亦即此前從未被任何人知曉的安全缺陷。波及範圍涵蓋每一個主流作業系統、每一個主流瀏覽器，以及龐大的關鍵開源工具生態系。

而 Anthropic 決定，不將這個模型對外公開。

取而代之的，是「玻璃翼計畫」（Project Glasswing）的誕生：一項攜手 11 家全球頂尖科技公司、投入 1 億美元的防禦性倡議，目標是在擁有類似 AI 能力的攻擊者得以武器化這些漏洞之前，將其全數修補。這場發布，既是 AI 攻擊潛力迄今最震撼的公開展示，也是前沿 AI 部署史上最具份量的決策之一。

## 一個在挖掘漏洞方面超越頂尖人類專家的模型

Anthropic 一再強調，Mythos Preview 是一個「通用型」前沿模型，並非資安專用工具。但它在資安領域所展現的能力，遠超過任何已公開披露的 AI 系統。

根據 Anthropic 自身的揭露，在數週的測試期間，Claude Mythos Preview 被部署於真實的程式碼庫與作業系統映像檔中。其發現令人震驚，無論從數量或嚴重程度來看皆然：

- **數千個零時差漏洞**，遍及所有主流作業系統（Windows、macOS、各大 Linux 發行版）與所有主流瀏覽器（Chrome、Safari、Firefox、Edge）
- **OpenBSD 中潛伏 27 年的漏洞**——OpenBSD 以安全設計著稱，卻有一個隱藏近三十年的缺陷，逃過無數人類研究員的眼睛
- **FFmpeg 中存在 16 年的弱點**——這個被全球數十億台設備與串流平台廣泛使用的開源多媒體框架，同樣暗藏重大安全隱患
- 多個廣泛使用的基礎設施元件中的嚴重漏洞

除了發現漏洞，Mythos Preview 還能對真實開源程式碼庫中的零時差漏洞實施利用、從封閉原始碼的二進位檔案逆向工程出攻擊手法，並將已知但尚未修補的漏洞轉化為可運作的攻擊程式碼。用 Anthropic 自己的話說，它已超越「絕大多數頂尖人類」資安研究員的能力。

最後這項能力——將已公開的 CVE 漏洞轉化為可用攻擊工具——尤其令人憂慮。資安界長期以來的心腹大患，是「修補空窗期」（patch gap）：從漏洞被揭露到組織實際完成修補之間的時間差。若 Mythos Preview 落入惡意之手，攻擊者將能系統性地在防禦方來得及反應之前，以工業規模武器化已知漏洞，將修補空窗期壓縮至趨近於零。

## Anthropic 為何選擇不公開

將 Mythos Preview 限制公開存取的決定並非史無前例——OpenAI 也曾以安全為由限制其最強模型的早期存取——但這次的定性截然不同。Anthropic 並非只是說 Mythos 比過去的模型更強大，而是明確表示：若公開發布，將代表威脅格局的質變——AI 將從研究加速工具，一躍成為可被國家行為者、犯罪組織和老練個人直接使用的自主網路攻擊引擎。

這裡的雙用途困境尤為尖銳，原因在於資安知識本質上是對稱的：讓防禦者得以修補漏洞的同一份認知，也能讓攻擊者加以利用。一個能找到零時差漏洞的模型，在本質上就是一個也可能協助利用這些漏洞的模型。

Anthropic 的解法是控制與模型互動的主體，而非控制模型產出的知識。玻璃翼計畫將 Mythos Preview 的能力，導入由具備足夠技術素養和負責任制度激勵的組織所構成的、高度受控的防禦優先管道。

## 玻璃翼計畫：1 億美元的回應

玻璃翼計畫匯聚了 11 家主要組織，各自貢獻特定專業與基礎設施：

- **Amazon Web Services** — 雲端基礎設施與資安工具鏈整合
- **Apple** — 自有作業系統與瀏覽器的資安
- **Broadcom** — 企業網路與晶片層級的漏洞
- **Cisco** — 企業基礎設施與網路資安
- **CrowdStrike** — 威脅情報與端點偵測
- **Google** — Android、Chrome 及雲端平台資安
- **JPMorgan Chase** — 金融業關鍵基礎設施
- **Linux Foundation** — 開源供應鏈資安協調
- **Microsoft** — Windows、Azure 及企業軟體資安
- **NVIDIA** — AI 運算基礎設施資安
- **Palo Alto Networks** — 網路資安與威脅情報

Anthropic 為此計畫承諾提供高達 **1 億美元的 Mythos Preview 使用點數**，另加 **400 萬美元的直接捐款**，用於支持開源安全組織，包括開源安全基金會（OpenSSF）及關鍵軟體維護者補助計畫。計畫的明確目標，是在擁有同等 AI 能力的攻擊者（無論是國家支持或犯罪組織）找到並武器化相同漏洞之前，率先識別並修補它們。

每家夥伴組織均透過客製化的安全研究介面獲得 Mythos Preview 的受控存取，該介面設計上防止模型被用於漏洞發現與補丁生成以外的任何用途。Anthropic 的紅隊監控所有使用記錄，並保留撤銷存取權限的最終決定權。

## AI 資安軍備競賽進入新階段

Mythos Preview 細節的公開——即便模型本身未對外提供——標誌著醞釀多年的 AI 資安論述走到了一個拐點。在此之前，AI 驅動漏洞發現最具說服力的示範，都是在狹義、定義清晰的程式碼庫中、受控條件下找到特定類型的漏洞。Mythos Preview 在異質、真實的生產環境軟體中發現數千個此前未知的缺陷，是不同量級的突破。

英國 AI 安全研究所及其美國對等機構的研究人員，已開始獨立評估 Anthropic 的說法。據熟悉評估進程的人士透露，初步跡象顯示 Anthropic 對 Mythos 能力的描述大體準確，儘管獨立研究人員仍在核實零時差發現的完整範疇。

兩國 AI 安全研究所的介入，也反映出政府對前沿模型評估態度更廣泛的轉變。英美兩國目前均要求超過一定能力門檻的模型在發布前接受安全測試。Mythos Preview 似乎是首個因資安能力——有別於生物或化學武器協助等以往關注的面向——而觸發政府介入的模型。

## 接下來怎麼走

Anthropic 尚未宣布更廣泛發布 Mythos 的時程，也未說明模型最終是否會以任何形式公開提供。公司表示玻璃翼計畫是持續性的，而非一次性清除積壓漏洞——模型將持續被用於隨著時間推移識別新出現的漏洞。

11 家夥伴組織預計將在未來數週內，依據標準協調披露程序，開始發布源自 Mythos Preview 發現的補丁。對於每個被修復的漏洞，Anthropic 也將發布技術摘要，幫助更廣泛的資安社群理解相關漏洞的類型，並在其他軟體中應用類似的修復邏輯。

對整個科技業而言，玻璃翼計畫提出了一個令人不安的問題：若今日已有模型能在全球安全加固程度最高的軟體中找到數千個未知漏洞，那麼有多少同樣的漏洞，此刻正被掌握同等或類似模型的攻擊者主動發現著？修補競賽，從未如此緊迫。
