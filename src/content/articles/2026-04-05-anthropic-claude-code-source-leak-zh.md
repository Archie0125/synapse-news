---
title: "Anthropic 意外洩露 51.2 萬行 Claude Code 原始碼，npm 套件漏洞引發供應鏈危機"
summary: "Bun 打包工具的已知 bug 導致 Claude Code v2.1.88 的完整原始碼——約 1,900 個 TypeScript 檔案、51.2 萬行程式碼——在 npm 上公開超過三小時。同一時間窗口內還出現了被植入木馬的 HTTP 客戶端套件，引發供應鏈攻擊疑慮。"
category: "developer-tools"
publishedAt: 2026-04-05T09:00:00Z
lang: "zh"
featured: true
trending: false
sources:
  - name: "The Register"
    url: "https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/"
  - name: "TechRadar"
    url: "https://www.techradar.com/pro/security/anthropic-confirms-it-leaked-512-000-lines-of-claude-code-source-code-spilling-some-of-its-biggest-secrets"
  - name: "Cybernews"
    url: "https://cybernews.com/security/anthropic-claude-code-source-leak/"
  - name: "NodeSource"
    url: "https://nodesource.com/blog/anthropic-claude-code-source-leak-bun-bug"
tags:
  - "anthropic"
  - "claude-code"
  - "資安"
  - "供應鏈攻擊"
  - "開源"
  - "npm"
relatedSlugs:
  - "2026-04-04-mcp-protocol-explosion-zh"
  - "2026-04-04-cursor-devin-war-zh"
---

2026 年 3 月 31 日凌晨，資安研究員 Chaofan Shou 在 npm 套件庫上發現了一件異常的事：`@anthropic-ai/claude-code` 2.1.88 版的完整、未混淆原始碼——約 1,900 個 TypeScript 檔案、共 51.2 萬行——竟透過已發布的套件，直接連結到 Anthropic 公開的 Cloudflare R2 儲存空間。

當 Anthropic 在 UTC 時間 03:29 下架套件時，這份程式碼已被複製逾 41,500 次。整個暴露窗口不到三個半小時，但這段時間已足夠讓這起史上最嚴重的 AI 工具原始碼意外洩露事件成為難以抹除的網路史實。

## 打包工具的 Bug 釀禍

這起事件的根本原因，可追溯至 Anthropic 在 2024 年底的一項收購：高效能 JavaScript 打包工具暨執行環境 Bun。Anthropic 將 Bun 整合進 Claude Code 的建置流水線後，Bun 的一個已知 bug 持續在產出 source map（原始碼映射檔），即便建置設定中已明確寫入 `development: false`。

Source map 原本是開發除錯用途，能將壓縮後的程式碼還原成可讀的原始碼，正式發布版本幾乎從不應對外公開。然而在這次的情況中，source map 直接包含了一個 URL，指向 Anthropic Cloudflare R2 儲存桶中未加密的原始碼壓縮檔。任何安裝這個套件、且知道要往哪裡找的開發者，都能輕鬆取得完整源碼。

Anthropic 在事後聲明中表示：「這是一起因人為失誤造成的發布打包問題，並非系統遭到入侵。」公司強調，沒有任何客戶資料外洩，AI 模型的權重檔也未受波及。但外洩的內容，仍包含了這款旗艦開發工具的完整內部架構：包含斜線指令（slash command）的實作邏輯、工具呼叫結構、內建的提示詞框架，以及 Claude Code 與 Anthropic 後端 API 的通訊機制。

## 同一時間窗口出現木馬程式

原始碼洩露已夠駭人聽聞，但資安研究人員在同一個三小時內，還發現了第二個更令人警覺的異狀：在這個受影響的 Claude Code 發布版本中，有一個被植入木馬的 HTTP 客戶端套件作為相依套件出現。

這個惡意套件——Cybernews 與 NodeSource 的分析師將其描述為跨平台遠端存取木馬（RAT）——並非 Anthropic 所為。跡象顯示，它是由第三方攻擊者在即時偵測到漏洞後，趁窗口未關閉之前修改了其中一個相依套件連結所植入的。這隻 RAT 支援跨平台運作，針對 macOS、Linux 與 Windows 的開發者環境設計。

Anthropic 確認知悉木馬元件的存在，但未公開歸因對象，也未說明具體攻擊向量。獨立研究人員指出，套件在安裝時的相依性解析機制，使得一個被汙染的傳遞性相依套件可能在窗口期間觸及執行 `npm install` 的開發者——這是典型的供應鏈攻擊模式。

這起事件揭露了 AI 工具發布管道的結構性弱點。與一般軟體不同，Claude Code 這類 AI 開發工具存在於高信任（具備完整本機檔案系統存取權的開發機器）與高價值目標（連接到有計費風險的 LLM API）的交叉地帶。若木馬在此場景下成功部署，危害程度將遠超過一般 SaaS 情境。

## 原始碼洩露了什麼

在套件下架之前，那 41,500 多份複製品讓外界得以一窺 Anthropic 如何設計其旗艦開發產品。外洩的程式碼包含：

**斜線指令實作**：`/commit`、`/review-pr` 及其他內建 Claude Code 技能的內部架構，包括驅動這些功能的提示詞、工具鏈與控制流程邏輯。

**工具呼叫 Schema**：定義 Claude Code 如何建構 Anthropic API 呼叫的完整 JSON Schema，包含部分先前未公開記載的工具使用定義。

**Session 管理邏輯**：Claude Code 管理對話狀態、脈絡壓縮，以及不同 Agent 類型之間切換交接的程式碼。

**後端通訊模式**：客戶端如何向 Anthropic 基礎設施進行身份驗證與通訊的細節。資安研究人員指出，這些資訊理論上可被用來建構未經授權的 API 客戶端。

**內部測試架構**：單元測試與整合測試的 fixture，雖不直接構成漏洞，但讓競爭對手得以精確掌握這款產品的預期行為與邊緣案例。

Anthropic 迄今未提供完整的外洩內容清單，但 1,900 個檔案的規模顯示，洩露的範圍幾乎涵蓋 Claude Code 客戶端實作的全部。

## 更大的警示：AI 工具供應鏈極為脆弱

這起事件發生之際，AI 開發工具已成為越來越多軟體開發團隊的關鍵基礎設施。Claude Code、GitHub Copilot、Cursor 各自擁有數十萬名每日活躍用戶，這些用戶透過這些工具處理大量編程工作流程，其中往往涉及敏感的商業邏輯、API 金鑰及專有演算法。

供應鏈攻擊的面向尤其令人警醒。讓 Anthropic 原始碼意外公開的那個 npm 套件發布機制，同時也成了惡意程式碼注入的管道。2021 年的 Log4Shell 漏洞展示了廣泛使用的函式庫如何在一夕之間成為災難性的攻擊面；Claude Code 事件顯示 AI 工具的發布管道同樣面臨這種風險。

NodeSource 的事後分析提出了幾項緩解建議：強制使用 lockfile 以防止傳遞性相依套件被替換、為 AI 工具發布版本建立可重現的構建證明（reproducible build attestation），以及針對具備系統提升權限的套件提供帶外完整性驗證機制。Anthropic 尚未公布自身的事後安全改善措施。

對整個開發者社群而言，這起事件提出了一個更難回答的問題：隨著 AI 程式碼助手更深入地整合進建置流水線、CI/CD 系統與 IDE 工作流程，它們所代表的攻擊面也等比擴大。Claude Code 的原始碼洩露，按 Anthropic 自己的說法，是人為失誤——而非有針對性的攻擊。同一窗口內的木馬植入，就不是了。

兩者在同一個三小時內先後出現，是業界需要花很長時間消化的一次壓力測試結果。
