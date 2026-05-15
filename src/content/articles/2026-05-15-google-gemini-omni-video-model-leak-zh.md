---
title: "Google「Gemini Omni」影片模型提前洩露：可能統一整個 Gemini 架構"
summary: "5 月 2 日，Gemini 應用程式介面出現「Powered by Omni」字串，揭示 Google 未發布的統一影片模型。洩露的演示畫面顯示物件替換、對話式影片編輯、範本創作等功能。距 5 月 19 日 Google I/O 主題演講僅剩四天，Gemini Omni 可能是 2026 年最重大的 AI 影片發表。"
category: "ai-ml"
publishedAt: 2026-05-15
lang: "zh"
featured: false
trending: false
sources:
  - name: "Testing Catalog"
    url: "https://www.testingcatalog.com/googles-gemini-omni-video-model-surfaces-ahead-of-i-o-debut/"
  - name: "Android Authority"
    url: "https://www.androidauthority.com/google-gemini-omni-video-model-leak-3665801/"
  - name: "Chrome Unboxed"
    url: "https://chromeunboxed.com/an-impressive-new-gemini-omni-video-model-just-leaked-ahead-of-google-i-o/"
  - name: "AIxploria"
    url: "https://www.aixploria.com/en/ai-radar/google-gemini-omni-leak-video-model-io-2026/"
tags:
  - "Google"
  - "Gemini"
  - "Gemini Omni"
  - "影片AI"
  - "Google IO"
  - "AI影片生成"
  - "多模態"
relatedSlugs:
  - "2026-05-15-google-io-2026-preview-gemini-android-zh"
  - "2026-05-12-android-show-io-2026-android17-xr-zh"
  - "2026-05-13-google-googlebook-ai-laptop-zh"
---

距 Google 年度開發者主題演講還有四天，這家公司不小心預告了它最重大的 AI 發表之一——而那不是 Gemini 4。

5 月 2 日，也就是 5 月 19 日 Google I/O 正式開幕前 17 天，一則 UI 字串在 Gemini 應用程式內部浮現：「Start with an idea or try a template. Powered by Omni.」這項發現由在 Google AI 功能預測上有出色記錄的 TestingCatalog 率先報導，隨即在 AI 研究社群引發一波分析熱潮，且隨著 I/O 主題演講臨近，討論聲浪只增不減。

過去兩週陸續洩露的資訊顯示，「Gemini Omni」遠不只是一次例行模型更新。它很可能是 Google 在 I/O 2026 發表的所有內容中最舉足輕重的一項。

## 洩露內容揭示了什麼

伴隨「Powered by Omni」字串一同曝光的 UI 文字更為直白：「Create with Gemini Omni: meet our new video model, remix your videos, edit directly in chat, try templates, and more.」（透過 Gemini Omni 創作：認識我們的全新影片模型、混剪你的影片、在對話中直接編輯、試用範本，以及更多功能。）

這四項能力——混剪、對話式編輯、範本、原始生成——代表了一種與目前市場主流截然不同的 AI 影片創作方式。Google 現有的影片生成能力 Veo 3.1 能夠產出令人印象深刻的成果，但基本上仍是一個相對封閉的生成系統：描述需求、接收片段。而 Omni 的描述暗示一種更具互動性、更強調反覆修改的工作流程。

Google 刪除之前在網路上流傳的演示片段，揭示了以下具體能力：

**現有片段內的物件替換**：使用者可以選取影片中的物件並描述替換方案，Omni 會重新生成受影響的幀，同時維持與周圍內容的視覺一致性。演示範例包含替換背景元素，以及在不同鏡頭間更換主角服裝。

**浮水印與疊加文字移除**：洩露片段顯示 Omni 能夠識別並乾淨地移除影片中的浮水印與文字疊加——對內容清理和再利用工作流程而言具有明確的商業價值。

**透過對話指令重寫場景**：使用者可以用自然語言描述對已生成場景的修改——「讓這個夕陽更戲劇性一些」、「把對話節奏改得更快」——並獲得更新版本，無需重新輸入完整的生成提示詞。

**範本式創作**：預製場景範本讓使用者填入自己的內容，降低非技術創作者製作產品示範或解說影片等結構化影片格式的門檻。

## Omni 究竟是什麼樣的模型？

這個名稱在 AI 研究社群引發了大量關於 Gemini Omni 底層架構的推測，目前出現三種主要假說：

**假說一：Omni 是 Veo 路徑的重新品牌**。最簡單的解釋是，Google 正在將其現有的 Veo 影片生成能力重新命名為「Omni」，以用於消費者端產品，底層模型並未改變。這將主要是一項行銷決策。

**假說二：Omni 是全新的獨立影片模型**。對話式編輯和物件替換等能力，超出了 Veo 3.1 公開展示的範疇。這個假說認為 Omni 是一個專為影片生成與編輯打造的獨立模型，與 Veo 系列並行運作而非取代。

**假說三：Omni 是統一多模態模型**。最宏觀的解讀是，Gemini Omni 是一個在單一模型家族中同時處理文字、圖像與影片生成的全新架構，取代現有分散的獨立系統（Gemini 處理文字、Imagen 處理圖像、Veo 處理影片），整合為統一的生成管道。這將解釋為何模型命名為「Omni」——它能處理一切。

從洩露的 UI 和演示片段來看，現有證據最符合假說三。尤其是對話式編輯介面，意味著一個以與 Gemini 理解文字相同的情境理解方式來理解影片內容的模型——能夠遵循指向現有內容特定元素的指令，而非每次從零開始生成。

## 使用限制與算力成本

來自早期洩露存取的一個細節引發了廣泛關注：Gemini Omni 的資源消耗似乎相當可觀，Google 即便對最高消費者方案的訂閱用戶也設置了嚴格的使用限制。

一位 Google AI Pro 方案（目前月費 20 美元）的使用者回報，生成兩個詳細影片片段已消耗其每日使用配額的 86%。這意味著在最高品質設定下，Omni 生成的每日算力配額大約只夠生成 2 至 3 個完整影片，或在較低解析度下生成更多短片段。

相比之下，Runway 和 Sora 以每月生成影片分鐘數作為配額單位，各方案月度上限從 125 秒到 2,000 秒不等。Google 採用每日限制而非月度累計配額的方式相當罕見，可能反映了即時互動式編輯相較於批次生成的算力成本。

## 競爭格局

AI 影片生成市場在 2026 年加速演進。字節跳動的 Seedance 2 被普遍認為是目前原始生成品質的領頭羊，為競爭對手設定了高標準。OpenAI 的 Sora 擴大了存取範圍，但在編輯能力上仍有所局限。Runway Gen-4 系列持續提升，尤其在電影風格生成方面。

對 Gemini Omni 片段的初步評估顯示，在純粹的生成品質——新創片段的真實感與動態連貫性——上，它在同等解析度下落後於 Seedance 2。但這個比較可能有些失公平：Omni 的差異化賣點並非僅在生成品質，而在於互動式編輯層，定位為內容修改和混剪工具，而非單純的從零生成系統。

若假說三（統一多模態）的解讀成立，競爭比較的座標系也將隨之改變。一個能在與文字相同的對話情境中討論、分析、編輯和生成影片的模型——整合進數十億人已在使用的 Gemini 助理介面——擁有的分發優勢，是專門化影片生成工具難以複製的，無論其輸出品質在邊際上有多高。

## Google I/O 的觀察重點

Google I/O 2026 於 5 月 19 日太平洋時間上午 10 點開幕。根據洩露資訊及 Google 的 I/O 前披露節奏，可以預期的是：

Google 將正式以名稱公布 Gemini Omni，並以精心挑選的示範展示其互動式編輯能力，凸顯 Omni 與現有影片生成系統的差距。具體定位方式——是新 Gemini 模型、Veo 升級版，還是獨立產品——將釐清三種假說的爭議。

上市時間表同樣關鍵。Google AI 功能的洩露 UI 通常比正式推出提前 2 至 8 週。若 Gemini Omni 遵循這個規律，Pro 方案訂閱者最快可能在 I/O 後數天內獲得存取權限。

定價方面目前完全不明朗。互動式影片編輯的大量算力需求，意味著 Omni 最終可能被鎖定在更高定價的方案或以獨立附加選項提供——不過 Google 也可能選擇在現有 Pro 方案中納入它，以在 6 月蘋果 WWDC 發表 iOS 27 AI 功能的競爭期間作為差異化籌碼。

目前，Gemini Omni 的存在不再是推測。唯一待解的問題，是洩露與現實之間的落差究竟有多大。
