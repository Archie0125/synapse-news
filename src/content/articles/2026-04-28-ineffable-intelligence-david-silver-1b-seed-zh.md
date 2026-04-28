---
title: "前DeepMind研究員David Silver募得11億美元，要打造不靠人類數據就能自學的AI"
summary: "AlphaGo與AlphaZero的核心架構師David Silver正式宣布創立Ineffable Intelligence，這家倫敦AI實驗室以51億美元估值完成了歐洲史上最大種子輪融資，金額高達11億美元。公司的目標直指「超級學習者」——一套完全透過自身經驗習得知識的AI系統，不仰賴任何人類生成的訓練資料，最終目標是「與超級智能建立第一次接觸」。"
category: "ai-ml"
publishedAt: 2026-04-28
lang: "zh"
featured: true
trending: true
sources:
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/04/27/deepmind-ineffable-intelligence-record-seed-funding-nvidia-google.html"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/27/deepminds-david-silver-just-raised-1-1b-to-build-an-ai-that-learns-without-human-data/"
  - name: "Sequoia Capital"
    url: "https://sequoiacap.com/article/partnering-with-ineffable-intelligence-a-superlearner-for-the-era-of-experience/"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-04-27/sequoia-and-nvidia-back-ex-deepmind-researcher-at-5-1-billion-value"
tags:
  - "強化學習"
  - "超級智能"
  - "DeepMind"
  - "種子輪融資"
  - "英國AI"
  - "超級學習者"
relatedSlugs:
  - "2026-04-17-claude-opus-47-release-zh"
  - "2026-04-25-deepseek-v4-flagship-model-release-zh"
---

今年AI領域最重磅的一筆賭注，或許不是從舊金山下的，而是來自倫敦。

4月27日，星期一，Google DeepMind強化學習部門前負責人David Silver——正是他設計出擊敗圍棋世界冠軍的AlphaGo、無師自通學會西洋棋的AlphaZero——走出隱身狀態，宣布創立新公司**Ineffable Intelligence**，並帶著11億美元（約新台幣357億元）的種子輪資金公開亮相。

這輪融資由Sequoia Capital與Lightspeed Venture Partners共同領投，參投方包括輝達（Nvidia）、Google、Index Ventures、DST Global、BOND、EQT，以及英國政府旗下的主權AI基金（Sovereign AI Fund）。公司估值達51億美元，正式成為一家在發布任何產品之前便已多次超越獨角獸門檻的AI實驗室。

這也是歐洲科技業史上金額最大的種子輪融資，紀錄甫創立便遙遙領先其他競爭者。

## 「經驗時代」的超級學習者

Silver在DeepMind深耕逾十年。在他主導下，DeepMind的系統學會了比任何人類更出色地玩Atari遊戲，以令圍棋九段大師瞠目結舌的方式征服圍棋，最終更透過AlphaFold解開了困擾生物學數十年的蛋白質結構預測難題。

這些成就的共同底色是一個字：**經驗**（experience）。不是模仿人類，不是爬梳網路文字，不是人工標注——而是讓系統在環境中不斷互動、試錯，自行摸索什麼可行、什麼不可行。這套學習範式的理論基礎正是強化學習（Reinforcement Learning，RL），而Silver相信，這個領域的潛力才剛剛開始被挖掘。

「我們的使命，是與超級智能建立第一次接觸，」Silver在融資公告中說。「我們正在打造一個超級學習者，讓它完全從自身的經驗中發現所有知識——從基礎的運動技能，到深刻的智識突破。」

這套定義有其深意。Silver所說的「超級學習者」與當今主流的大型語言模型（LLM）有本質區別：LLM的目標是壓縮並重現人類文字中的模式，而超級學習者則要從第一原理出發，透過與環境的自主互動發現世界的運作規律——包括那些人類可能從未明確描述過的知識。

## 為何是現在？為何是倫敦？

Ineffable的誕生，恰好對應了三項讓Silver的長期信念終於變得「可投資」的條件。

**第一，算力門檻終於達到。** Silver構想中的RL訓練規模，需要同時跑數以百萬計的並行模擬，讓每次互動產生的經驗數據持續回饋模型更新。輝達最新的Blackwell架構、Google的第八代Ironwood TPU，讓這種規模的模擬在今天成為可能，而三年前這仍是遙不可及的事。

**第二，人類數據已見天花板。** OpenAI、Anthropic等頂級AI實驗室已私下承認，用來預訓練LLM的高品質人類文字正逐漸枯竭。網路爬蟲採集到的內容越來越充斥AI生成物，製造的是反饋迴圈而非真實知識。基於RL的系統自行生成訓練數據，根本不存在這個瓶頸。

**第三，模仿範式的極限之爭。** 多年來，LLM批評者一直指出：訓練系統預測「下一個token」只能逼近人類智能，永遠無法超越訓練數據所設定的上限。強化學習在理論上不存在這個天花板——AlphaGo超越了人類有史以來最強的圍棋選手，恰恰因為它從來不是在模仿任何人。

選擇倫敦，是深思熟慮的結果。Silver與共同創辦人——DeepMind系的Wojciech Czarnecki、Lasse Espeholt和Junhyuk Oh——都在英國，希望就地建立公司。英國政府為留住前沿AI人才不再出走加州，透過英國商業銀行旗下的主權AI基金直接注資參與了這輪融資。

## 投資人的邏輯

Sequoia在公司尚無任何公開模型、無任何基準測試成績、無任何收入的情況下，便以51億美元估值共同領投，這筆賭注更多是押在David Silver這個人身上，而非某一具體技術規格。

Sequoia合夥人在罕見的公開聲明中，稱Ineffable為「經驗時代的超級學習者」，並將Silver整個職業生涯定性為對同一個核心原則的持續驗證：「自我博弈與從經驗中學習，比模仿更具可擴展性。」AlphaGo、AlphaZero、AlphaFold並非三個孤立的成就，而是Silver幾十年如一日沿著同一條研究軌跡走下去的里程碑。

輝達的參投格外值得關注。作為同時投資OpenAI、Anthropic、Mistral和十幾家前沿AI實驗室的晶片巨頭，輝達極少在這麼早期的階段下注。這一動作既傳遞商業訊號——Silver的RL系統將需要海量GPU算力——也體現了輝達在AI版圖快速重塑時期，確保與每一個潛在突破性玩家保持關係的戰略布局。

Google的參投則有另一層含義。Silver在Google旗下的DeepMind工作了十餘年，而Google選擇投資他的新公司而非將他再度攬入麾下，這至少說明：與其放手讓Sequoia和輝達獨享上行空間，不如在外部持股參與。

## 前路：挑戰與期待

Ineffable Intelligence尚無公開的技術路線圖，也未設定任何公開的基準目標。據知情人士透露，投資人內部簡報預期第一批模型成果將在2026年底前出現，但Silver明確表示不會承諾公開發布的時間節點。

公司面臨的科學挑戰是真實的，不是任何資本可以輕易化解的。強化學習歷來存在脆性問題：在定義清晰的封閉環境中（棋盤、蛋白質結構）表現卓越的系統，往往在面對開放性任務時便土崩瓦解。RL領域的歷史上充斥著在訓練環境中無敵、環境稍作改變便失效的案例。

Silver對此問題的答案——「超級學習者」架構——尚未有公開的技術細節。名稱與定位暗示的是一套設計用來廣泛學習、跨域遷移知識的系統。這個目標能否工程化落地，至今仍是AI研究的核心未解之謎。

可以確定的是，AI產業的重心正在移動。一年前，主流範式是「規模」：更大的語言模型、更多的token、更大的算力集群。而今，由11億美元機構資本和一位業界最具聲望的研究者背書的一派力量，開始押注：下一個突破不會來自「模仿的規模化」，而會來自「經驗的自主積累」。

Silver將Ineffable定義為「我一生的工作」，並說這個世界需要一個「讓強化學習範式的全部雄心得以自由伸展的地方」。這個地方，就是本週在倫敦誕生的這家億級估值AI實驗室。
