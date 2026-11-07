---
category: ai-ml
featured: true
lang: zh
publishedAt: '2026-11-07T19:15:21.114772+00:00'
relatedSlugs: []
sources:
- name: GitHub Blog
  url: https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/
- name: The New Stack
  url: https://thenewstack.io/together-compiler-gpu-optimization/
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/grab-ai-generated-code-safety/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- name: The New Stack
  url: https://thenewstack.io/engineers-become-process-engineers/
- name: The New Stack
  url: https://thenewstack.io/scale-ai-code-reviews/
summary: GitHub 上四成 PR 已經由 AI 起草，巨頭現在搶的不是誰寫得快，而是誰能決定「這段 code 可以上線」。
tags: []
title: AI 寫 code 一秒鐘，人類審 code 兩天半：軟體業真正的瓶頸換位子了
trending: true
type: analysis
---

今年最能說明 AI 寫程式走到哪一步的發表，不是哪個新模型，而是 GitHub 默默換掉了底層的 Git 儲存架構。

在 GitHub Universe 上，GitHub 公開了新架構。內部測試中，同一個 repo 可以同時讓 5,000 個 agent 一起工作，每秒處理 7,200 次 push，讀取延遲依然穩定。為了做到這件事，GitHub 先把 99.99999% 的 repo 搬上 Azure，再重新設計 Git 的寫入方式。

人類團隊不需要每秒 7,200 次 push，再大的團隊也不會。GitHub 這樣改，是因為它預期未來寫 code 的主力不是人。

所以這篇的核心論點是：**寫 code 已經不稀缺了，稀缺的是願意在 PR 上按下 Approve、出事後要負責的那個人。** GitHub、GitLab、AWS、Google、Cursor 看得很清楚，現在大家搶的是 code 寫完之後的那一段。

### 數字說明工作卡在哪裡

先看普及速度。根據 GitHub Octoverse，到 2026 年 9 月，GitHub 上超過 40% 的 PR 由 agent 寫初稿，3 月時只有 17%，半年翻了一倍多。

但交付速度沒跟上。CircleCI 的 2026 交付報告顯示，平均每日 workflow 執行次數年增 59%。拆開來看差距很大：前 5% 的團隊成長 97%，最後四分之一的團隊幾乎沒成長。AI 沒有讓大家一起變快，而是拉開了兩群人的距離：一群改了交付流程，另一群只是換了寫 code 的工具。

另一份研究追蹤一家公司，管理層要求 PR 產量翻倍，結果每位 reviewer 的負擔也跟著翻倍。幾個月內，自動審查的覆蓋率就超過了人工審查。

這就是 Goldratt 在《目標》裡講的瓶頸理論：瓶頸以外的工序加速，只會讓工作堆在瓶頸前面。AI 讓寫 code 這一站變快了，工作就堆到了 code review、CI 和部署。

### 9 個工程師，每週 400 個 PR

Aviator 的例子最具體。他們每週合併的 PR 從大約 100 個暴增到 400 個以上，AI 產生的 PR 中位數是 640 行。業界普遍認為單次審查超過 400 行，抓 bug 的能力就會明顯下降。

9 個工程師、每週 400 個 640 行的 PR，不可能每行都認真看。如果流程不改，只剩兩條路：大家開始隨便蓋章，或者工作整個卡住。

Aviator 先試了三個常見做法，都失敗了：

- **加 AI reviewer。** 作者自己的一個 PR 上，18 則討論有 16 則是 AI 開的，大多在挑 magic number、React key 這類小毛病。只有一則抓到真正的 race condition。兩則真正重要的設計決策討論，反而被淹沒在雜訊裡。
- **規定四小時內要審。** 第一次回覆變快了，但 Approve 變得空洞。大家為了趕時限只是掃過去，自己的工作也被拖慢。
- **為自家慣例調校的自我審查工具。** 效果比通用 bot 好很多，但它還是在 code 寫完之後才看 diff。過程中最有價值的討論和決策，最後只留在聊天視窗裡，沒人再看到。

最後有效的做法，是不再把 diff 當作審查的主要對象，改看五件事：這個改動的意圖、驗收條件、不能被破壞的不變條件、過程中做了哪些決策、能證明它可以運作的證據。規則交給機器每次檢查，決策留給人。每個 PR 還是有人簽核，只是審的東西不一樣了。

結果是：同樣 9 個人，合併量變 4 倍，merge 時間中位數從 2.1 天降到 3.4 小時，revert 減少 40%。

這背後有個更少人注意的事實。微軟 2013 年 Bacchelli 與 Bird 的研究發現，code review 留言裡只有 14% 跟 bug 有關。Code review 本來就不只是抓 bug，它是團隊共享知識、讓每個人對系統保持同一套理解的方式。

**這才是沒人在談的風險：** 當大部分 code 由 AI 寫，團隊最先失去的就是這套共同理解。等到某天線上出事、沒人說得出這段 code 為什麼長這樣，才會發現已經失去好幾個月了。

### 台灣讀者應該很熟悉這個模式

The New Stack 有篇文章說「工程師正在變成製程工程師」。這句話在台灣應該特別有感，因為台灣半導體業就是這樣運作的。

晶圓廠裡，沒有人用手去刻電晶體。製程工程師的工作是設計流程、盯良率、調參數，在每一站設好檢查關卡。機台負責生產，人負責讓整條產線可靠。一片晶圓不會等到最後才檢查，每一站都有量測。

這跟豐田的「自働化」是同一個概念。豐田佐吉發明的織布機在斷線時會自動停機，所以一個人可以同時看好幾台。福特則把一台 Model T 的組裝時間從 12.5 小時壓到 93 分鐘（1914 年），靠的是重新設計產線，不是工人手變快八倍。

軟體業現在才開始學這一套。

### 部署鍵還是得有人按

Together AI 新推出的 Together Compiler，是值得參考的做法。他們讓 coding agent 自動優化 GPU kernel，一個晚上就能完成以前工程師要花好幾天甚至好幾週調的東西。官方說法是：優化迴圈完全自主，最終評估和部署流程也是自動的，但必須由人啟動，而且人要先看過改動才能上線。AI 可以自己反覆實驗，但最後放行的人還是人。

Grab 從手機 App 這端也走到同樣的結構，他們的原則是：AI 加速了寫 code，分層防禦才讓這個速度變得安全。他們的防線分成幾層：

- **合併前：** Android Lint 和 SwiftLint 加上自訂規則
- **測試：** 單元測試、UI 測試、QA
- **內部搶先體驗（Grab Early Access）：** 先發給內部員工試用，監控 crash
- **上線時：** 分階段推出加 feature flag，控制影響範圍

原因很現實：手機 App 一旦帶著 crash 上線，不是每個用戶都會自動更新，壞掉的版本會在手機上留很久。Crash 率還會直接影響 Google Play 排名。

### 為什麼巨頭都在搶這一層

看懂上面這些，就能理解各家在搶什麼：

- **GitHub** 重做儲存架構，又推出 Agent HQ，想讓各家 agent 都在它的平台上被調度，最後的 merge 鍵也在它手上。
- **GitLab** 的優勢是 CI/CD 和安全掃描，它賭的是誰控制流水線，誰就控制治理。
- **AWS** 在 agent 工具裡推「規格驅動開發」，在寫 code 之前先把意圖和驗收條件定清楚。
- **Google** 推非同步 agent，任務直接做完再交回來，問題全部轉到「怎麼驗證它是對的」。
- **Cursor** 從編輯器起家，先推出 Bugbot，再收購做 stacked PR 和 code review 的 Graphite，方向很明顯是往審查層走。

這帶來一個連鎖效應：**計價方式會從按人頭，改成按關卡收費。** 如果每個工程師底下跑 50 個 agent，用工程師人數計價就不合理了。真正值錢的會是每一次通過驗證的 merge、每一條政策檢查、每一次安全的部署。掌握放行關卡的平台，同時掌握稽核紀錄和帳單。

### 反方觀點

公平地說，「治理層」也可能只是 Jira 換個名字：更多儀表板、更多簽核、更多流程。Aviator 的方法在 9 人的精實團隊有效，放到 2,000 人的組織未必行得通。很多公司現在連驗收條件都沒在寫，更別說意圖文件。

另一種反方說法是：驗證技術會進步得夠快，審查瓶頸幾年內就會消失，現在大家花大錢蓋的治理層會變成沒人需要的東西。

我不太相信這個說法。形式化驗證已經「快要可以用了」四十年。更現實的是責任歸屬：出事時要負責的，永遠是按下 Approve 的那個人。連 Together AI 都不讓 agent 自己部署 GPU kernel，台灣的銀行和券商也不可能讓 AI 自己把交易系統推上 production。

### 值得關注

1. **平台會內建 PR 大小限制。** 2027 年底前，至少一家主要平台會對超過一定行數、又沒附結構化意圖或規格檔的 agent PR 發出警告或直接擋下。「400 行」會從研究結論變成產品功能。
2. **Revert 率會成為主要指標。** 工程主管會改報 revert 率和變更失敗率，不再強調「人均 PR 數」。賣 AI 寫 code 工具的廠商會被要求公開 revert 數字，不少家會不太好看。
3. **Feature flag 和漸進部署工具會被收購。** 這是最後一道防線，想掌握 agent 流程的平台都需要回滾能力。18 個月內應該會看到這個領域的收購案。
4. **CircleCI 報告裡的差距會繼續擴大。** 明年的數據會顯示前段團隊和後段團隊差距更大。關鍵不是用哪個模型，而是有沒有重新設計審查流程。
5. **按 agent 數量或用量計價會取代按人頭計價。** 2027 年中以前，上面五家至少有兩家會改。

寫 code 變便宜是最容易的部分。下一輪的贏家，會是能讓「放行一個改動」變便宜、同時又不草率的公司。