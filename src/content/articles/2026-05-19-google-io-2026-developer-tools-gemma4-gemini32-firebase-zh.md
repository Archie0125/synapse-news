---
title: "Google I/O 2026開發者工具全覽：Gemma 4、Gemini 3.2 Flash與Firebase AI正式上線"
summary: "消費者端的亮點之外，Google I/O 2026為開發者端帶來了密集的平台升級：開源的Gemma 4 27B模型以一敵二十，Gemini 3.2 Flash以旗艦性能衝擊成本底線，Firebase AI Logic正式上線，Agent Platform獲得視覺化工具與持久記憶體。與此同時，Project Mariner已死——但它最好的想法，現在都成了API。"
category: "developer-tools"
publishedAt: 2026-05-19
lang: "zh"
featured: false
trending: false
sources:
  - name: "Google DeepMind — Gemma 4"
    url: "https://deepmind.google/models/gemma/gemma-4/"
  - name: "Build Fast With AI — Gemini 3.2 Flash"
    url: "https://www.buildfastwithai.com/blogs/gemini-3-2-flash-release-2026"
  - name: "Firebase AI Logic 文件"
    url: "https://firebase.google.com/docs/ai-logic"
  - name: "Nerova AI — Project Mariner 終止"
    url: "https://nerova.ai/news/google-shuts-down-project-mariner-gemini-agent-browser-2026"
tags:
  - "google"
  - "gemma"
  - "gemini"
  - "firebase"
  - "開源"
  - "開發者工具"
  - "ai代理"
relatedSlugs:
  - "2026-05-19-google-io-2026-keynote-gemini-project-astra-android-xr-zh"
  - "2026-05-18-google-googlebook-gemini-intelligence-android-show-zh"
  - "2026-05-03-ai-api-pricing-war-token-collapse-zh"
---

Google I/O 2026的消費者端頭條——Gemini 3.5、Project Astra正式上線、Android XR眼鏡——已足夠震撼，霸占了社群媒體的版面。但對真正用Google基礎設施動手做事的工程師和產品團隊而言，更重要的故事，發生在開發者專場、API文件更新，以及幾項低調宣告之中。這些加總起來，代表著Google對AI構建方式的重要轉向。

核心主題只有一句話：不要再把AI功能當作實驗，要開始把它當作基礎設施。

## Gemma 4：以一敵二十的開源模型

I/O 2026最具技術含量的開發者公告，不是什麼新的雲端服務或定價調整——而是一個以Apache 2.0授權發布的模型家族，Google宣稱它的表現能超越規模大它二十倍的競品。

Gemma 4於4月發布，在I/O獲得更多開發者端的聚焦，底層架構直接源自Gemini 3的研究成果。這個模型家族涵蓋四種規格，從針對端側優化的E2B，到新增的27B參數版本，適合伺服器端部署。所有模型均以Apache 2.0授權發布，開發者可以自由微調、再發行、打造商業產品，無需授權費用。

技術面的主要聲稱相當大膽。所有四種規格均原生支援視覺，可直接處理影片、圖像和文件；E2B和E4B版本更支援音訊輸入。上下文視窗方面，端側模型達到128,000 tokens，較大模型為256,000 tokens。所有模型支援逾140種語言。27B版本提供4位元量化支援，讓它能在過去需要專用推論硬體才能執行的設備上運行。

Google將Gemma 4定位為與當前開源領頭羊——Meta的Llama 4和Mistral最新版本——直接競爭的方案。目前已公布的基準測試數據頗具說服力：在推理和程式碼生成任務上，Gemma 4的27B模型據稱能達到甚至超越參數量大其五到二十倍競品的水準。若這些聲稱能通過獨立評測驗證，Gemma 4將代表開源AI效率的真正躍進。

實際使用上，Gemma 4與Keras、TensorFlow和Vertex AI部署管線原生整合，為已深植Google雲端生態的團隊提供從實驗到生產的順暢路徑。同時也在Hugging Face和Kaggle上架，觸及那些對Google雲端沒有特定偏好的大多數AI開發者。

## Gemini 3.2 Flash：終結API成本焦慮的模型

如果Gemma 4是為自架和開源開發者準備的，Gemini 3.2 Flash則是為使用Google API的團隊帶來的好消息。

這個新模型在正式發布前，已悄悄在Eleuther AI Arena上進行沉默式基準測試，I/O正式宣布後也坐實了預期。Google將它定位為2026年下半年的主力Flash級通用模型，商業定位相當進取：Gemini 3.2 Flash在程式碼生成方面能達到GPT-5.5約92%的水準，成本卻估計只有15到20分之一。

從Google AI Studio元數據外洩、並在I/O得到確認的定價來看：輸入每百萬tokens 0.25美元，輸出每百萬tokens 2.00美元——比Gemini 3.0 Flash的輸出定價（每百萬3.00美元）更低，也顯著低於GPT-5.5 Mini的對應層級。上下文視窗擴展至超過一百萬tokens。

早期基準數據顯示，Gemini 3.2 Flash在創意程式碼任務上超越了Gemini 3.1 Pro，包括結構化輸出生成和互動式3D環境建構。這個優勢是否具有廣泛性，仍有待獨立評測積累更多數據；但Arena的內部結果足夠有說服力，Google已加快步伐正式推出。

模型的部署規模同樣值得關注。Gemini 3.2 Flash不只是一個API產品——它現在已是驅動Google搜尋AI摘要（AI Overviews）、Google地圖本地資訊摘要、YouTube章節和摘要生成、Google文件智慧撰寫，以及Gmail智慧回覆的推論引擎。Google在要求開發者押注之前，已在極大規模上自用，吃自己的狗糧。

## Firebase AI Logic與Genkit 2.0：AI不再是實驗

兩項Firebase公告正式確立了過去一年醞釀已久的轉變：將AI能力直接整合進Google的應用開發平台，讓團隊無需再管理獨立的AI基礎設施。

Firebase AI Logic正式上線（GA），邏輯清晰：讓行動和網頁客戶端直接存取Gemini模型，使用與Firestore和Storage相同的安全性模型（包含Security Rules）。API金鑰管理、使用量監控和速率限制全部自動處理，消除了AI整合應用最常見的生產事故根源之一。實際影響是：一個已熟悉Firebase的行動開發者，可以在數小時內把Gemini呼叫加進自己的App，而不必從頭搭建並鞏固一個後端代理伺服器。

Firebase Genkit 2.0也同步正式上線。這個協同框架新增了串流支援、多模型路由、原生Model Context Protocol（MCP）伺服器整合，以及透過Cloud Trace整合的可觀測性。MCP支援尤其值得關注：這意味著使用Genkit的開發者可以立即接入不斷壯大的MCP相容工具和資料來源生態，讓Genkit在已深入Firebase和Google雲端生態的團隊中，成為LangChain或CrewAI等框架的有力競爭者。

## Agent Platform：從展示走向開發者原語

Gemini Enterprise Agent Platform在I/O也獲得了重大升級，雖然消費者端的關注遠不如Project Astra。兩項能力正式上線：Agent Engine Sessions——讓AI代理在多次互動中維持持久的對話脈絡；以及Memory Bank——允許代理隨時間儲存和提取結構化資訊。這些聽起來像是產品功能，但本質上是開發者基礎設施——是讓可靠、有狀態的AI應用成為可能的原語，讓每個團隊不必各自從頭打造工作階段管理和記憶系統。

Agent Designer，一個用於構建代理工作流程的視覺流程畫布，進入開發者預覽。目標是讓產品團隊——不只是工程師——能夠設計和迭代代理行為，無需為每個連接撰寫程式碼。風險在於，如同所有視覺化AI工作流程工具，簡單協同它處理得好，複雜邏輯就容易崩潰。Google在這方面的紀錄參差不齊，證明要靠開發者真正用它建出什麼才算數。

Gemini API呼叫中新增的`thinking_level`參數——從minimal、low、medium到high——讓開發者可以在逐次呼叫層級上，以延遲換取推理深度。在代理應用中，有些步驟需要深度推理，有些可以快速而粗略，這種粒度控制對效能和成本都有實質影響。

## Project Mariner的終結：瀏覽器代理展示的謝幕

一項撤銷同樣值得關注。Google於5月4日悄然關閉了Project Mariner——其網頁瀏覽AI代理，距離I/O整整兩週前。這個在WebVoyager基準測試中拿到83.5%分數、可在雲端虛擬機上同時處理十個瀏覽器任務的獨立產品，從未作為公開產品正式推出。

官方說明，以及更有意思的訊號，是Google認為瀏覽器代理的概念以API原語交付，好過以獨立產品形式存在。Project Mariner的電腦操控能力已被整合進Gemini API、Gemini Agent和AI Mode，在那裡可以與其他能力結合使用，而不必受限於特定的展示介面。

這反映了Google更廣泛的規律：雄心勃勃的AI展示（Project Starline、Duplex、Mariner）吸引眼球之後，悄悄被吸收進平台層，底層技術得以大規模使用，但不再受原有展示介面的限制。這究竟是平台建設成熟度的體現，還是組織層面無法推出面向消費者產品的慣性，是業界關於Google的老問題。無可爭辯的是：瀏覽器代理能力現在以API形式對所有開發者開放，而不是被鎖在一個沒人能用的封閉產品裡。

## 對開發者的長遠賭注

綜合來看，Google在I/O 2026的開發者公告，構成一套平台整合策略：Gemma 4服務開源用戶，Gemini 3.2 Flash服務API用戶，Firebase AI Logic服務行動/網頁開發者，Genkit 2.0服務協同框架需求，Agent Platform服務構建生產代理的團隊。每個部件針對不同的開發者輪廓，但集體傳遞的訊息是一致的。

Google不再把贏得模型基準競賽作為主要目標——它試圖成為開發者依賴的基礎設施層，無論哪個前沿模型在基準排行榜上暫居首位。這個賭注能否奏效，取決於開發者是否覺得整合的Google技術棧，比從多個供應商拼湊最佳組合更具吸引力。Gemini 3.2 Flash的定價，以及Gemma 4的開放授權，顯示Google在這個論點上已做了仔細的盤算。
