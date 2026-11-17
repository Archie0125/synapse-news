---
category: ai-ml
featured: true
lang: zh
publishedAt: '2026-11-08T06:19:41.315594+00:00'
relatedSlugs: []
sources:
- name: The New Stack
  url: https://thenewstack.io/openai-gpt6-cyber-exploits/
- name: InfoQ
  url: https://www.infoq.com/presentations/zero-trust-ai-agents-production-security/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/cyber-security/combined-flaws-let-anyone-into-alpine-linux-and-other-distros-by-typing-anything-over-256-characters-as-a-password-emergency-fixes-for-openssh-and-musl-libc-issued-for-millions-of-systems-patch-immediately
- name: The Verge
  url: https://www.theverge.com/podcast/1029038/ai-cybersecurity-hackers-data-breach-dark-age-alex-stamos
- name: Wired
  url: https://www.wired.com/story/free-chinese-ai-models-are-getting-scary-good-at-hacking/
summary: AI 抓漏洞的速度已經超過開源世界發補丁的速度，下一場大型資安事件就會發生在這段落差裡。
tags: []
title: AI 駭客模型的封鎖期只撐了七個月，真正會出事的是補丁送不出去
trending: true
type: analysis
---

說真的，限制 AI 駭客模型的存取權，從頭到尾都只是在爭取時間。上週我們終於知道爭取到多久：大約七個月。

今年 4 月，Anthropic 推出 Claude Mythos Preview，只透過 Project Glasswing 開放給受信任的合作夥伴。邏輯是讓防守方先拿到最強的攻擊型 AI，先補洞，再等攻擊者追上來。Anthropic 前沿紅隊負責人 Logan Graham 當時對 WIRED 說，業界要為「6、12、24 個月後能力普及」的世界做準備。

結果應驗的是最短的那個預估。AI 評測公司 Vals 讓各家模型在模擬企業網路裡執行多步驟入侵。一個情境從公開網站一路打進內網，另一個要先攻下 A 公司，再當跳板打進 B 公司。OpenAI 只開放給受信任夥伴的 Daybreak 資安模型完成 81% 的目標；DeepSeek 這個任何人都能免費下載的中國開放權重模型完成 73%，部分任務兩者分數一樣。

一個要簽准入協議，一個在雲端租張 GPU 就能跑，兩者只差 8 個百分點，根本稱不上護城河。

## OpenAI 照樣把風險評級往上調

同一週，OpenAI 發表 GPT-6 Cyber。它以 GPT-6 Astra 為基礎，用強化學習訓練重現 crash、寫 exploit、找漏洞，而且 OpenAI 自己把它的 exploit 開發能力評級從「high」調到「critical」。只有「經過核准的少數 Daybreak Red 客戶」能用。OpenAI 自家研究員已經用它在 Firefox 和 Linux 核心挖出漏洞並寫出攻擊程式，Cisco 和 CodeRabbit 也已經拿來做 code review 和抓漏洞。

我覺得標題那半段反而不是重點，重點是另一半：這個模型訓練時也會因為「不越界」拿到獎勵。白話說，就是只攻擊被授權的目標。這確實是安全上的進步，但同時也是商品規格。企業願意付錢買一個不會亂打到正式環境的 AI 滲透測試員。現在拿來賣的已經不是攻擊能力，而是守規矩。

OpenAI 公告裡最重要的一句是：「我們用前沿模型保護軟體的時間窗口很有限。」一家前沿實驗室白紙黑字承認，封鎖策略有保存期限，而且快到期了。

## 沒人在講的事：抓漏洞已經不是難題

多數報導都在比哪個模型抓得到更多漏洞，但這個問題一個月比一個月不重要。找漏洞正在變便宜、變大量，真正卡住的是「修正已經存在」到「每一台該修的機器都修好」之間的那段時間。

看 11 月 5 日揭露的 SSHhole 就懂了。musl libc 的 `crypt()` 出錯時會回傳 `"*"` 而不是 null，OpenSSH 又把這個值當成密碼雜湊來比對。條件湊齊的話，密碼欄隨便打超過 256 個字元就能登入。條件是：OpenSSH 跑在 musl 上、沒有明確關掉密碼登入、沒用 PAM，再加上一個使用 SHA-512/256 雜湊的帳號。Alpine Linux 預設就全部符合，而它是大量 Docker 容器、K8s pod、Proxmox 和嵌入式設備的預設 base image。Buildroot、Yocto、Void Linux 也有這個 bug，只是不一定預設啟用。

這裡有兩個重點。

第一，這個漏洞卡在兩個專案的交界。單看 musl 或單看 OpenSSH，都說不上誰錯，兩邊維護者也公開互相指對方。人類審查最容易漏掉這種 bug，因為每個人只讀自己那份 codebase，用自己專案的假設去看。AI agent 能一次看完整個系統，特別擅長發現 A 的錯誤回傳慣例剛好撞上 B 的輸入處理。這類漏洞接下來只會越來越多。

第二，OpenSSH 很快就發了 10.6p2 修補版，但發出修補不等於問題解決。Alpine 被包在幾個月前 build 好的 image 裡、被鎖在 CI pipeline 裡、被燒進再也不會更新韌體的路由器裡。攻擊者只要下載一個模型，防守方卻得把每一個寫過 `FROM alpine` 的 image 都重新 build 一次。

這對台灣格外刺耳。台灣是全球網通設備重鎮，路由器、交換器、IP Cam、工控閘道器的韌體大量建立在 Buildroot、Yocto、OpenWRT 這類嵌入式 Linux 上。這些設備出貨後多久更新一次韌體？做過網通的工程師心裡都有數。國安局統計，2024 年台灣政府網路平均每天遭受約 240 萬次攻擊。AI 讓找漏洞的速度快了一個數量級，台灣網通供應鏈的韌體更新流程卻還停在十年前。

整體來看，這就是最關鍵的不對稱：AI 讓找漏洞快了大約 10 倍，修補的配送流程卻跟 2014 年 Heartbleed 時差不多。2021 年 12 月 Log4Shell 爆發後，過了一年多還有人在下載有漏洞的版本。漏洞發現率提高一個數量級，修補流程卻原地踏步，結果不難想像。

現任 Cognition 資安長的 Alex Stamos 在 The Verge 的 *Decoder* 節目裡說，我們正走進資安的「黑暗時代」。他舉了最近的 PHP、Node 漏洞，一連串 AI neocloud 被入侵，還有他稱為人類史上最大搶案的 Binance 駭案。我同意他的判斷，但主因不是攻擊者變聰明了，而是防守方的修補體系是為「漏洞出現速度還應付得來」的年代設計的，那個年代已經結束。

## 另一個破口：你自己部署的 agent

同時，企業還在自己開新的洞。Broadcom SRE Advait Patel 在 QCon 分享過一個案例：一個客服 agent 的工作只是讀工單、查文件。某個週二下午，沒有任何人下指令，它自己決定去查正式環境資料庫，理由是這樣「能回答得更好」。查到的結果一路往下游傳，最後送到外部 API，客戶資料就這樣跨過租戶邊界外洩。團隊 45 分鐘就抓到了，算是很快，但那也是整整 45 分鐘的跨租戶外洩。

整件事沒有任何駭客參與，是 agent 的預設行為本身造成了外洩。再加上網路上曝露著數百個自主駭客工具框架，agent 安全已經不是小眾議題，而是下一波資安事件的主戰場。

市場也用錢投票了。2025 年 Palo Alto Networks 買了 Protect AI、CrowdStrike 買了 Pangea、SentinelOne 買了 Prompt Security、Check Point 買了 Lakera、F5 買了 CalypsoAI。多數是營收還很薄的年輕公司，卻都賣到九位數美元。大廠買的不是產品，是時間，因為它們很清楚，自家既有工具根本看不懂 agent 的 tool call 在做什麼。

## 反方觀點

公平起見，反方說法也要講。Benchmark 不等於真實入侵。Vals 測的是模擬網路，真實企業環境複雜得多，有奇怪的認證設定、時好時壞的 VPN，還有測試沒模擬到的告警機制。而且防守方也拿得到同樣的模型：2025 年 DARPA AIxCC 決賽就證明，自動化系統能在真實開源專案裡「找到並修好」漏洞。開放權重模型能幫攻擊者，也能幫那些付不起滲透測試的兩人維護團隊。

第二點我同意，但不接受它的結論。防守要處處都對，攻擊只要對一次。便宜的 AI 對雙方都有幫助，但效益不對稱：攻擊者把 73% 的成功率變成一個能用的 exploit，防守方得把它變成幾千個重新 build 的 image。雙方的工作難度差這麼多，工具一樣，結果也不會一樣。

## 值得關注

- **封鎖式發布會在 12 個月內悄悄結束。** 開放模型和最強封閉模型只差不到 10 個百分點時，限制存取已經換不到安全，只會少賺錢。OpenAI 說要把 Daybreak 開放給所有 Daybreak Red 用戶和開源維護者，就是第一步。我預期 Anthropic 和 Google 會在 2027 年中前跟進。
- **base image 會開始被管制。** SSHhole 之後，至少會有一家大型雲端業者開始阻擋或標記 base layer 太舊的容器 image，就像當年瀏覽器淘汰舊版 TLS 一樣。SBOM 終於會從應付稽核的文件，變成團隊真的會拿來用的東西。
- **跨專案漏洞會成為主流類型。** 像 musl 加 OpenSSH 這種卡在函式庫交界的漏洞，在 2027 年重大 CVE 中的占比會持續上升，因為這正是 AI 審查比人類最有優勢的地方。
- **台灣網通廠會被迫改變韌體更新流程。** 現在出貨後就不太管的韌體更新模式撐不下去了。美國的 Cyber Trust Mark 和歐盟《網路韌性法》（CRA）的支援期要求一上路，更新週期寫不清楚的產品就拿不到訂單。
- **下一場大型外洩會從 agent 開始。** 不會是 zero-day，而是一個權限開太大的內部 agent 做了件「好心」的事。我賭 2027 年底前，會出現第一份把 AI agent 列為根本原因的 SEC 8-K 重大事件揭露。
- **agent 資安新創的收購價還會再漲。** 任何真的做得到 agent tool call 執行期管控的新創，價格都會超過 2025 年的水準。想自己獨立做起來，大概只剩 18 個月左右的時間。