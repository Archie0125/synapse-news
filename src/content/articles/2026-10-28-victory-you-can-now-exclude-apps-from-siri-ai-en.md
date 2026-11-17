---
category: ai-ml
faqs:
- answer: iOS 27.2 lets users exclude selected applications from Siri AI. Siri AI
    should no longer access those apps’ content, although related AI features may
    become unavailable.
  question: What does the new iOS setting allow users to do?
- answer: End-to-end encryption protects messages during transmission, but an operating
    system may still read content after it is decrypted on the device. Cloud-based
    AI processing can create an additional data path unless users can block the assistant’s
    access.
  question: Why does this matter for end-to-end encrypted messaging?
- answer: No. It provides a clearer app-level access boundary, but it does not by
    itself explain every data flow or eliminate cloud processing elsewhere. Users
    who want a broader restriction can still disable Siri AI and use Siri Classic.
  question: Does the switch solve every Siri AI privacy concern?
featured: false
lang: en
publishedAt: '2026-10-28T20:04:21+00:00'
relatedSlugs: []
sources:
- name: EFF
  url: https://www.eff.org/deeplinks/2026/10/victory-you-can-now-exclude-apps-siri-ai
summary: Apple’s app-exclusion switch is meaningful privacy engineering precisely
  because it lets users sacrifice AI convenience instead of silently sacrificing encrypted
  context.
tags:
- ai-ml
- products
- cybersecurity
title: Victory! You Can Now Exclude Apps from Siri AI
trending: false
type: news
---

In the most recent update to Apple’s devices, iOS 27.2, the company has introduced a new setting to “Exclude Apps” from Siri AI, fulfilling one of our asks from [our Encrypt It Already campaign earlier this year](https://encryptitalready.org/).

One of our main concerns with new AI features on devices is how those features interact with end-to-end encrypted content, particularly with secure messaging apps. Many AI features require cloud processing, and despite [privacy protections engineered into these systems](https://www.eff.org/deeplinks/2026/09/secure-messaging-and-ai-remain-conflict-despite-promise-tees), the content of secure messaging apps may leave a user’s device without their knowledge. That changes the privacy concerns around using those tools. In a perfect world, users would be able to put a barrier up to ensure data from certain apps doesn’t leave the device. Here was our initial ask:

*You should be able to tell the operating system’s AI to not access an app, even if that comes at the “cost” of missing out on some features. The setting should be straightforward and easy to understand in ways the Gemini and Apple Intelligence controls currently are not.*

At launch, we found the settings to control Siri AI’s app access [behavior pretty confusing](https://www.eff.org/deeplinks/2026/09/how-limit-what-apples-new-siri-ai-can-access-ios-27). You had to toggle several options to block Siri AI off from accessing an app, or disable Siri AI entirely. Turning off Siri AI and [reverting to Siri Classic](https://www.eff.org/deeplinks/2026/09/how-limit-what-apples-new-siri-ai-can-access-ios-27#classicsiri) is, for now, still a good option if you’d prefer to use the older version.

The most recent update is far more clear and does more to protect your data. And, just as expected, it comes at the cost of some features. That’s a good thing, actually. The features not working shows that the new setting is effective.

Here’s how to add apps to the exclusion list, once you’ve updated to 27.2:

- Open ***Settings*** > ***Siri*** > ***Excluded Apps***
- Tap “Add Apps” and select any apps you’d like to add to the exclusion list


Now Siri AI cannot access the contents of the app. Excluding an app also means you may lose some features. For example, if you exclude the Apple Messages app, you will no longer be able to have Siri AI read or respond to messages for you. Even the “onscreen awareness” feature, where you invoke Siri and ask it for information about what you’re currently looking at, will not work anymore. For example, if you exclude Signal, you cannot invoke Siri and ask it to discern any information in the Signal app. You’ll just get these messages:


## What’s the State of This on Android?

This update from Apple is also a good excuse to check in on the process on Android. It has improved a little, but is [not as straightforward](https://support.google.com/gemini/answer/13594961?hl=en#screen_automation&zippy=%2Cwhat-happens-with-my-data-when-gemini-uses-screen-automation-to-help-me-get-tasks-done-in-android-apps%2Cwhat-happens-to-my-data-when-i-use-geminis-agentic-calling-capability) as Apple’s new settings, and lacks the ability to set the screen context feature per-app. But you do have some control over what Gemini can access:

- Open up the Gemini app
- Tap your user photo, then ***Settings > Personal Intelligence*** > ***Connected Apps***
- Revoke access to any apps you do not want Gemini to have access to

This process seems to work well enough for some data and we like that it’s opt in, but it’s not exactly intuitive. For example, Signal doesn’t appear there because Signal doesn’t support Gemini’s app access feature at all. That means Gemini can’t access the content of Signal directly, which is good.

But Gemini can read notifications if you’ve enabled the “[Device Assistance](https://support.google.com/gemini/answer/15235441)” Connected App (which you likely have, since that also enables basic features, like setting a timer—check under ***Settings*** > ***Personal Intelligence*** > ***Connected Apps***), and it can use screen context unless you’ve disabled the ***Device controls*** > ***Screen context*** > “Use screen and app data” option in the Gemini Settings. These two features may access the contents of the Signal app or notifications, if you choose to use them. We’d prefer a more hard-lined approach that reduces the chances of user error here: Google should give users the ability to turn these features off per app.

Apple clearly understands that some users want stronger controls over what Siri AI can and cannot access. But we think they should go further and offer the option to only use “on device” AI features, similar to [what Samsung offered with its Galaxy AI](https://www.wired.com/story/limit-galaxy-ai-to-on-device-processing-or-turn-it-off/). We’re happy to see this change and think all operating systems need to consider similar controls moving forward.

## Summary

**TLDR:** Apple’s app-exclusion switch is meaningful privacy engineering precisely because it lets users sacrifice AI convenience instead of silently sacrificing encrypted context.

- iOS 27.2 adds a clear setting that can exclude selected apps from Siri AI access.
- EFF had requested this capability because AI features may send locally accessible content to cloud processors, including content originating in end-to-end encrypted apps.
- Previously, users needed to change several controls for each app or disable Siri AI and return to Siri Classic.
- Some Siri AI features stop working for excluded apps, which is expected evidence that the access boundary is being enforced.

## 摘要

**重點摘要：** Apple 的應用程式排除開關之所以重要，正是因為它讓使用者選擇犧牲人工智慧便利，而不是在不知情下犧牲加密內容。

- iOS 27.2 新增明確的「排除應用程式」設定，使用者可以禁止 Siri AI 存取指定 App。
- EFF 推動這項功能，是因為人工智慧可能把裝置上可讀取的內容送往雲端處理，其中也可能包含原本來自端對端加密通訊軟體的資料。
- 過去若要阻擋存取，使用者必須調整多個選項，或完全關閉 Siri AI、改回 Siri Classic。
- 排除後部分功能會失效；這不是缺陷，而是存取界線確實生效的可見證據。