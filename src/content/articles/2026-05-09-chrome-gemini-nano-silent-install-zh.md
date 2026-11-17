---
title: "Google Chrome 悄悄在你電腦裝了 4GB AI 模型——從沒問過你的意見"
summary: "資安研究員 Alexander Hanff 指出，Chrome 瀏覽器在未徵得同意的情況下，靜默在用戶裝置上存放約 4GB 的 Gemini Nano 模型檔案。Google 表示自 2024 年起已在 Chrome 提供 Gemini Nano，並於 2 月開始推出可關閉並移除該模型的設定。"
category: "ai-ml"
publishedAt: 2026-05-09
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: true
trending: false
sources:
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/cyber-security/google-chrome-silently-downloads-4gb-ai-model-to-your-device-without-permission-report-claims-researcher-says-practice-may-violate-eu-law-waste-thousands-of-kilowatts-of-energy"
  - name: "Gizmodo"
    url: "https://gizmodo.com/google-chrome-is-downloading-a-4gb-ai-model-onto-your-device-without-consent-researcher-warns-2000755201"
  - name: "The Register"
    url: "https://www.theregister.com/ai-and-ml/2026/05/07/chrome-silently-installs-a-4-gb-local-llm-on-your-computer/5230893"
  - name: "9to5Google"
    url: "https://9to5google.com/2026/05/06/google-chrome-4gb-storage-ai-details/"
tags:
  - "Google Chrome"
  - "Gemini Nano"
  - "端側 AI"
  - "隱私"
  - "GDPR"
  - "大型語言模型"
relatedSlugs:
  - "2026-05-09-google-android-show-aluminum-os-preview-zh"
  - "2026-05-06-google-io-2026-preview-android17-gemini-zh"
---

隱私研究員 Alexander Hanff 在自己的 Mac 上對一個稽核用設定檔進行例行磁碟用量檢查時，發現了一件他從未同意的事：Google Chrome 悄悄放進了約 4GB 的模型檔案。裡面有個名為 `weights.bin` 的檔案——那是 Gemini Nano 的神經網路權重，也就是 Google 較輕量的端側大型語言模型。整個過程沒有任何安裝提示，沒有任何確認視窗。Chrome 就這樣自行決定，靜默地把一個比幾部電影還大的模型下載到他的電腦。

Hanff 是隱私顧問公司「That Privacy Guy」的創辦人，曾就 Cookie 同意問題多次向監管機構提出申訴。他本週公開調查結果後，外界對 Google 積極將 AI 能力嵌入 Chrome 的批評聲浪隨即湧現。他的報告記錄了這個模型存放在 Chrome 設定檔目錄下、名為 `OptGuideOnDeviceModel` 的資料夾中——而且更關鍵的是，若用戶手動刪除它，Chrome 會自動重新下載，並且不會再次通知。

## Gemini Nano 在瀏覽器裡究竟做什麼

自 2024 年底以來，Google 持續在 Chrome 中整合端側 AI 功能。目前 Gemini Nano 為至少兩個已公開的 Chrome 功能提供支援：「幫我寫」（Help me write）會在網頁表單欄位中即時提供文字建議；另一套端側詐騙偵測系統則能在不向 Google 雲端伺服器傳送資料的情況下，即時分析可疑網頁內容。

後者確實有一定的隱私保護邏輯：Chrome 在本機分析威脅，無需將每個造訪的網址和頁面內容串流傳送到遠端服務。Apple 也為 Apple Intelligence 的本機處理設計提出了幾乎相同的論點。從這個角度來看，那 4GB 的下載是個功能，不是漏洞。

但核心問題並不在於端側 AI 是否有用，而在於用戶沒有選擇的機會。「這個下載完全沒有清楚的同意流程，」Hanff 在報告中寫道。Chrome 在下載模型前沒有提示用戶選擇加入，事後也沒有任何通知，而且直到 2026 年 2 月之前，都沒有提供任何用戶介面讓人關閉或移除它。模型就這樣靜默抵達、佔用儲存空間，刪掉了還會自動重裝。

Google 的官方回應僅部分承認問題。一位公司發言人向多家媒體確認，Chrome 從 2026 年 2 月起開始推出用戶可自行控制的選項——一個藏在 `chrome://settings/` 深處的開關，允許用戶停用 Gemini 功能並移除本機模型。企業用戶則有更細緻的群組原則和 Chrome 管理主控台可用。但對於那些沒有主動去找這個開關的用戶，預設行為依然不變：先下載，有投訴再提供控制。

## 歐盟 GDPR 的法律疑雲

Hanff 的歐洲隱私法專業背景，讓他的研究具備了具體的法律指向。他認為，Chrome 的靜默模型部署可能違反了《一般資料保護規則》（GDPR）的核心原則——「隱私設計與預設」。GDPR 第 25 條要求，資料處理在預設狀態下必須最小化，且在處理開始前，用戶應獲得真實、充分的知情控制權。

將本機 LLM 推送至設備是否構成 GDPR 廣義定義下的「處理」，歐洲資料保護機構目前尚未針對 AI 模型分發給出明確裁定。但法規的精神是清楚的：用戶應當了解產品對其設備做了什麼，並應有能力在事前拒絕，而非事後才被告知。

由於 Google 的歐洲總部位於都柏林，愛爾蘭資料保護委員會（DPC）是 Chrome 的主要歐盟監管機構，但截至目前尚未就 Hanff 的報告公開表態。若 DPC 或其他歐盟機構認定此次下載構成缺乏充分法律依據的處理行為，Google 可能面臨監管程序，而這個監管框架過去十年已對 Google 開出數十億美元的罰款。

時間點也增添了政治敏感性。歐盟《AI 法案》對通用 AI 模型的義務已於 2025 年 8 月全面生效，各地監管機構對消費者端 AI 部署方式的審查力度正在加強。Chrome 將 Gemini Nano 預設啟用並分發的做法，直接落入了監管機構一直在尋找的具體案例範圍。

## 從沒人授權的碳排放

Hanff 提出的第二條批評路線在隱私圈子以外同樣引發共鳴：在未取得同意的情況下，向他所稱可能多達數億台的設備分發一個 4GB AI 模型，其環境代價究竟是多少？

在他的中間估算中，約有 5 億台設備收到 Gemini Nano 的下載，這代表單次模型分發事件就產生約 2 EB 的網路流量。加上持續的本機儲存，以及這些模型執行的任何本機推論運算，整體能源消耗在這個規模下相當可觀。

Google 在官方聲明中沒有具體回應環境面的核算。

這個批評在敏感時刻落地。包括 Google 在內的主要雲端業者，其企業永續承諾近年已因 AI 基礎設施建設加速而承受質疑。Alphabet 的資料中心用電量在 2024 和 2025 年隨 AI 需求急遽攀升。將推論模型分散部署到數億個端點，是將能源成本去中心化，但去中心化並不讓它憑空消失。

## 先推出、被罵再加控制：一個熟悉的劇本

Chrome 的 Gemini Nano 事件，遵循了消費者 AI 部署中一個如今已相當熟悉的劇本。微軟在 2024 年推出 Recall 功能時，遭遇了幾乎相同的強烈反彈——Recall 持續截圖用戶的電腦活動，以支援 AI 驅動的個人電腦歷史搜尋。資安研究員立即指出其隱私問題；微軟延後推出，委託資安公司進行大規模重新設計，最終以具有意義的「選擇加入」控制機制重新發布 Recall。整個循環——從發布到反彈到重新設計——耗費了將近一年時間。

Apple 的做法則走在光譜的另一端。Apple Intelligence 的端側處理被定位為透明度的展示，所有功能都需要用戶主動啟用，不會靜默出現。

Chrome 的做法更接近微軟 Recall 的那端：在完善的用戶控制機制到位之前，模型已大規模推送，而 Hanff 認為，Google 的揭露只記載在好奇的管理員才會找到的地方，而非一般用戶會查看的地方。

想確認 Chrome 是否已在自己的電腦上下載這個模型，可以在 Chrome 設定檔目錄中尋找 `OptGuideOnDeviceModel` 資料夾。macOS 上的路徑通常是 `~/Library/Application Support/Google/Chrome/Default/`；Windows 上則在 `%LOCALAPPDATA%\Google\Chrome\User Data\Default\`。若想移除，在 Chrome 設定中停用相關的 Gemini 功能，應可防止它再次自動下載。

Google I/O 2026 將於 5 月 19 日登場，屆時預計將宣布橫跨 Chrome、Android 17 和 Google Cloud 的重大 AI 整合。這場 Gemini Nano 爭議，是對未來幾年端側 AI 部署同意權攻防戰的一次早期預告。產業界尚未回答的問題其實很簡單：當一家公司決定 AI 應該住進你的設備，誰有資格做這個決定？

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 9 處。*
