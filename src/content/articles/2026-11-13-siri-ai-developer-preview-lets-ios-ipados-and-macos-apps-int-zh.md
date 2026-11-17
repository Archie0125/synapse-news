---
category: ai-ml
faqs:
- answer: 開發者可透過 App Intents 提供應用程式支援的內容與操作。Siri AI 隨後能根據自然語言、螢幕內容和對話脈絡呼叫這些功能。
  question: 第三方應用程式目前能接入哪些 Siri AI 能力？
- answer: 開發者可用 Skills 將多個動作組合成單一體驗。Siri AI 也能從一個應用程式找到內容，再交給另一個應用程式繼續處理。
  question: 複雜任務和跨應用程式操作怎麼完成？
- answer: 還不能。預覽功能目前限制於開發者版本和內部 TestFlight 測試，主要用途是開發與驗證。
  question: 這些整合現在能直接提供給一般使用者嗎？
featured: false
lang: zh
publishedAt: '2026-11-13T16:00:00+00:00'
relatedSlugs: []
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/apple-siri-ai-integration/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
summary: Apple 推出的 Siri 預覽版，有望讓使用者透過對話直接操控 App；但它能否真正發揮價值，關鍵在於是否能可靠地將指令導向正確操作，而不只是再展示一次包裝精美的語音助理。
tags:
- ai-ml
- products
- developer-tools
title: Siri AI 開發者預覽登場，iOS、iPadOS 與 macOS App 可整合 Siri
trending: false
type: news
---

[Apple released the Siri AI Developer Preview in the 27.3 beta releases of its operating systems](https://developer.apple.com/news/?id=gdk2umrf), enabling developers and apps to integrate with the assistant and hand off actions to it. During the Preview, access to Siri AI is restricted to developer builds and internal TestFlight testers.

Apple says that Siri AI is an entirely new version of its assistant which is "profoundly more capable, conversational, and personal".

Today’s preview allows any app to bring its content and actions directly into Siri AI by using App Intents, making it easier for all apps to tap into Siri AI’s newest capabilities, including personal context understanding, onscreen awareness, natural language, and more.


These new capabilities let users make natural language requests and have Siri AI carry out any custom action supported by the app. The framework also supports [complex requests](https://developer.apple.com/documentation/appintents/siri-ai-developer-preview#Extra-guidance-for-complex-actions) through Skills, a new feature that lets developers "teach Siri AI how to combine several actions into a single experience".

If a request does not specify an app name, it will automatically be routed to the app currently in the foreground, the app associated with an active Live Activity, or the app previously mentioned in the ongoing conversation. This allows users to continue conversations across an app and its Live Activity, or a different app altogether. While an app is running in the background, however, it will receive only requests that explicitly mention its name.

Requests can also include actions across apps, such as finding content in one app, sending it to another, and perform an action there.

Commenting on Apple's announcement, Reddit user sixtypercenttogether [noted](https://www.reddit.com/r/iOSProgramming/s/Z3mtwACUn6):

In my limited testing so far it does what it says. If you include a good description on your intent and parameters, Siri can figure it out. THIS is what Siri should have been all along, all the way back in 26.0.


User Medical\_Lengthiness6 [compared Apple's approach to integrating Siri AI to Google's AppFunctions](https://www.reddit.com/r/iOSProgramming/s/jyc8Rj7cmG):

Doing it via app intents was the right move. Google could have done this with the android intents but instead decided to make a completely different agent skills sdk that you have to implement.


All Apple Intelligence features, including Siri AI, may be subject to [usage limits](https://support.apple.com/en-gb/148587), with extended, premium access planned the future. Finally, developers besed in the EU should be aware that Siri AI is currently unavailable in the EU on iOS, iPadOS, and watchOS.

## Summary

**TLDR:** Apple’s Siri preview could make apps conversationally programmable, but its value depends on reliable action routing—not another polished assistant demo.

- Apple released the Siri AI Developer Preview through the 27.3 beta operating-system releases for developer builds and internal TestFlight testing.
- Apps expose content and actions through App Intents, allowing Siri AI to use personal context, onscreen awareness, and natural-language requests.
- A new Skills feature lets developers teach Siri AI to combine several app actions into a more complex workflow.
- Requests can move content and actions between apps, making Siri a potential orchestration layer rather than a voice-only launcher.
- Implicit routing favors the foreground app, an active Live Activity, or a recently mentioned app; background apps generally require explicit naming.

## 摘要

**重點摘要：** 新版 Siri 有機會讓應用程式變得可用對話操控，但成敗取決於動作路由是否可靠，而不是展示影片拍得多漂亮。

- Apple 在 27.3 測試版作業系統中推出 Siri AI 開發者預覽，目前僅供開發版本與內部 TestFlight 測試。
- 應用程式可透過 App Intents 暴露內容和操作，讓 Siri AI 結合個人脈絡、螢幕資訊與自然語言執行任務。
- 新的 Skills 機制可教 Siri AI 串接多個動作，完成較複雜的工作流程。
- 請求還能跨應用程式尋找、傳送及處理內容，使 Siri 有機會成為系統級協調層，而不只是語音啟動器。
- 未指定應用程式時，系統會優先路由至前景程式、進行中的即時動態或對話剛提及的程式；背景程式通常必須被點名。