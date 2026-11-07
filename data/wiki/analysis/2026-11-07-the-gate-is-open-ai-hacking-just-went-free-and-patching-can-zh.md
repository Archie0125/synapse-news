---
category: ai-ml
lang: zh
published: '2026-11-07T19:16:52.353428+00:00'
sources:
- name: The New Stack
  url: https://thenewstack.io/openai-gpt6-cyber-exploits/
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/cyber-security/combined-flaws-let-anyone-into-alpine-linux-and-other-distros-by-typing-anything-over-256-characters-as-a-password-emergency-fixes-for-openssh-and-musl-libc-issued-for-millions-of-systems-patch-immediately
- name: Wired
  url: https://www.wired.com/story/kernel-panic-refrigeration-hacks-internet-of-things/
- name: The Verge
  url: https://www.theverge.com/podcast/1029038/ai-cybersecurity-hackers-data-breach-dark-age-alex-stamos
- name: Wired
  url: https://www.wired.com/story/free-chinese-ai-models-are-getting-scary-good-at-hacking/
summary: OpenAI 把新模型的攻擊能力評為「critical」，而一個免費下載的中國模型只落後它 8 分。所謂的「限制開放」已經失效。
title: AI 駭客能力免費化：閘門已破，補丁跑不贏
trending_theme: AI 大幅強化駭客攻擊能力
type: analysis
---

OpenAI 上週四發表 GPT-6 Cyber 時，語氣有點微妙。官方自己把這個模型「找漏洞、寫 exploit」的能力評為「critical」，比上一代的「high」再高一級，然後強調只開放給「經過審核的 Daybreak Red 客戶」。

翻成白話就是：這東西危險到不能隨便給，但請放心，鑰匙在我們手上。

問題是，鑰匙早就沒用了。

## 81 分和 73 分，差距不到一個版本

AI 評測公司 Vals 最近做了一組實驗：讓各家模型去打模擬的企業內網。一個情境是從對外網站一路打進去，另一個更麻煩，要先攻下 A 公司，再拿 A 當跳板打 B 公司。

結果 OpenAI 只給信任夥伴用的 Daybreak 資安模型完成 81% 的任務，第一名。第二名是 DeepSeek，開放權重，任何人都能下載回家跑，沒有使用條款，沒有 log，沒有人審核你是誰，完成率 73%。部分任務上兩者分數一模一樣。

8 分的差距在 AI 圈大概就是一次改版。台灣讀者應該很有感：數位發展部 2025 年初就禁止公部門使用 DeepSeek。但這種禁令只管得到「我們自己不准用」，管不到「對方拿來打我們」。攻擊者不會因為你的公文就不下載。

## 「爭取時間」策略準時到期

限制開放這套邏輯本來就建立在時間表上。今年 4 月，Anthropic 透過 Project Glasswing 限量釋出 Claude Mythos Preview，理由是先讓防守方拿到工具，爭取領先時間。Anthropic 紅隊負責人 Logan Graham 當時對 WIRED 說：「我們必須現在就準備好，6 個月、12 個月、24 個月後，這些能力會廣泛流通。」

七個月後，預言成真。

我覺得最可怕的地方在這裡：他們預測得很準。業界明明知道窗口有多長，結果還是沒來得及把軟體修好。OpenAI 這次的公告自己也承認：「很明顯，我們利用前沿模型保護軟體的窗口有限。」當新聞稿讀，這是在呼籲行動；當進度報告讀，這是在說時間快到了，作業還沒寫完。

## 找漏洞早就不是瓶頸

很多人還在問「AI 能不能找到漏洞」，這題其實早就有答案。2024 年 Google 的 Big Sleep 在 SQLite 挖到真實漏洞；2025 年自動化滲透測試工具 XBOW 衝上 HackerOne 美國排行榜第一；同年 8 月 DARPA 的 AI Cyber Challenge 決賽，參賽系統直接在真實開源專案裡自動找洞、自動補洞。現在 OpenAI 說自家研究員用 GPT-6 Cyber 在 Firefox 和 Linux kernel 找到漏洞並寫出可用的 exploit，Cisco 和 CodeRabbit 也已經拿它來做 code review。

找漏洞變便宜了，把補丁送到每一台機器上卻還是一樣貴。

11 月 5 日爆出的 SSHhole 就是最好的例子。在 Alpine Linux 的 OpenSSH 密碼欄位隨便打超過 256 個字元，就能直接登入。原因是 musl libc 的 `crypt()` 出錯時回傳 `"*"` 而不是 null，OpenSSH 又剛好拿這個 `"*"` 去比對 `/etc/shadow` 裡那些「沒設密碼」帳號的佔位符 `*`，結果就比對成功了。

Alpine 預設開啟密碼登入、不走 PAM，條件全部符合。偏偏 Alpine 又是 Docker、Kubernetes、Proxmox 最常見的 base image，嵌入式設備也大量採用。Buildroot、Yocto、Void Linux 也都帶著這段有問題的程式碼，只是不一定預設啟用。

OpenSSH 出了 10.6p2，musl 作者 Rich Felker 也發了修正，然後雙方都覺得是對方的錯。

**這是目前幾乎沒人在談的角度：** AI 時代最危險的漏洞，不在單一專案裡，而在專案和專案的接縫處。A 專案的行為合理，B 專案的行為也合理，兩個疊在一起就出事。這種接縫沒有維護者負責，也沒有哪個 fuzzer 會跨兩個專案去測。人類稽核員看到專案邊界就會停下來，AI 不會，它天生就適合在這種地方挖洞。

對台灣來說，這不是遠方的新聞。台灣是全球路由器、NAS、工控設備、IoT 模組的生產重鎮，韌體大量用 Yocto 和 Buildroot 打包。2022 年 DeadBolt 勒索軟體橫掃 QNAP 和 Asustor NAS 的記憶應該還沒褪色。問題從來不只是上游有沒有出修正，而是幾年前出貨的那批設備，韌體到底還有沒有人在更新。

## 冰箱被駭，跟 AI 沒什麼關係

如果你覺得「AI 末日論」講得太玄，看看歐洲的冰箱。

11 月 2 日，法國血液機構 EFS 有三個據點的冷藏室被入侵，溫度被「調到非常高」。還好警報系統和現場人員即時發現，血袋沒有受損。同一週，至少 11 個歐洲國家的連鎖超市冷凍櫃溫度被調高，大量食物只能報廢。10 月法國已經有數百家門市中招，8 月則是美軍基地大約六間福利社與超市發生同樣狀況，五角大廈正在和法國警方聯手調查。

這些攻擊不需要什麼前沿模型，靠的是連上網卻沒人管的溫控器。這跟 2016 年 Mirai 殭屍網路是同一種病，十年來沒有好轉。長期研究關鍵基礎設施的 Josh Corman 說得很到位：我們對聯網科技的依賴，成長速度一直快過保護它的決心，於是暴露在「意外、對手，以及現在可能出現的 AI agent」面前。

重點在這裡：AI 不必發明新的攻擊手法，它只要讓「找到十年前就存在的爛攤子」這件事變得更便宜。WIRED 報導過，連程度普通的北韓駭客都靠 AI 偷走數百萬美元。讓三流駭客變成二流，而且大量複製，這才是真正的威脅模型。

## Stamos 說的「黑暗時代」是對的

前 Facebook 資安長、現任 Cognition 資安長 Alex Stamos 在 The Verge 的訪談裡說，我們正進入資安的「黑暗時代」。他舉了 PHP 和 Node 的重大漏洞、一連串被攻破的 AI 新雲端業者（neocloud），還有他口中「人類史上最大搶案」的 Binance 駭客事件。

他的判斷是，建立在人工分析師、特徵碼偵測、一季一次滲透測試上的資安產業，本來就該被清算，AI 只是讓這一天提早來。

我同意，而且想再推一步：黑暗時代不是防守方遲早會追上的短暫低潮，而是攻防成本結構顛倒的這段期間。2026 年攻擊成本崩跌，防守成本卻幾乎沒變：還是要有人重 build image、要有廠商出韌體、要有維運人員半夜重開 production。這個落差就是黑暗時代。要等到補丁發布跟漏洞挖掘一樣自動化，它才會結束。

## 反方觀點

公平起見，看一下最強的反論。

Vals 測的是模擬網路，乾淨得不像話。真實企業裡滿是怪異的老系統、不穩定的 EDR，還有會覺得「怪怪的」的資安人員。多步驟攻擊的 8 分差距也會累積：如果十個步驟每一步都差一點，整條攻擊鏈的成功率可能掉很多。而且防守方拿得到一樣的工具，Cisco 現在就在用 GPT-6 Cyber 強化自家產品。OpenAI 若真把開源維護者拉進 Daybreak，可能會變成史上最大規模的協同程式碼稽核。

這些都對，但結論不變。防守方必須每一台都守住，攻擊方只要成功一次。在本來就不對稱的戰場上，模型能力打平不代表結果打平。更何況冰箱事件已經說明了，最脆弱的那些目標，本來就不會有人拿 GPT-6 去稽核。

## 值得關注

1. **半年內 Daybreak Red 全面開放。** 開源模型只落後個位數時，OpenAI 的限制開放會從安全措施變成形象包袱。我預期 2027 年第二季前會開放給所有 Daybreak Red 用戶，Anthropic 的 Glasswing 也會同步放寬。
2. **美國開始管制開放權重模型。** Vals 的數據是主張管制的人目前最有力的彈藥。2027 年會出現針對「資安評測超過某門檻」的開放權重模型的立法提案，中國模型是政治焦點。但權重早就流出去了，執行上幾乎沒有意義。
3. **Base image 重建時效變成採購條款。** SSHhole 之後，企業採購會開始問供應商：上游出 CVE 後，你們多久重 build 容器？Chainguard 這類持續重建的精簡 image 會迎來一波業績。台灣的 MSP 和雲端代理商可以提早布局。
4. **歐盟《網路韌性法》（CRA）的第一個 IoT 案例。** 已遭利用漏洞的通報義務在 2026 年 9 月生效，EFS 事件背後的冷凍設備供應商很可能成為早期的執法對象。外銷歐洲的台灣 IoT 廠商最好現在就盤點韌體更新流程。
5. **更多「雙專案接縫」漏洞。** SSHhole 不會是單一事件。我預測 2027 年年中以前，至少還會再爆出兩個高風險的跨函式庫漏洞，而且都是 AI 在沒人負責的專案邊界上找到的。