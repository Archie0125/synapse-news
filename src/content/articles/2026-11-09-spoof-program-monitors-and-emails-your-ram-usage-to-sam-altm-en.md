---
category: hardware
faqs:
- answer: It is a bash script that checks a PC's RAM usage every five minutes using
    the kernel's MemAvailable estimate. If utilization stays under 90%, it emails
    Sam Altman a humorous daily summary built from the CSV logs.
  question: What does ram-altman do?
- answer: Developer Iain Kay wrote it after Sam Altman said on a podcast that people
    having spare, underutilized RAM at home is 'quite terrible' compared with data
    center utilization. Kay describes the memory accounting as serious and the emails
    as a joke.
  question: Why was it created?
- answer: Altman's email address is not included in the script, so users must add
    it themselves. A --dry-run option lets people run the checks without emailing
    anyone.
  question: Will it actually spam Altman?
featured: false
lang: en
publishedAt: '2026-11-09T12:31:12+00:00'
relatedSlugs: []
sources:
- name: Tom's Hardware
  url: https://www.tomshardware.com/pc-components/ram/spoof-program-monitors-and-emails-your-ram-usage-to-sam-altman-if-under-90-percent-utilization-ram-altman-logs-usage-and-reports-you-for-wasting-memory
summary: ram-altman is a joke, but it lands because the memory shortage is real, and
  Altman's 'idle RAM is terrible' line sounds like a landlord complaining about your
  spare room.
tags:
- open-source
- ai-ml
- developer-tools
title: Spoof program monitors and emails your RAM usage to Sam Altman if under 90%
  utilization
trending: false
type: news
---

A new GitHub repository dubbed [ram-altman](https://github.com/IainKay/ram-altman) features a script to monitor your PC’s RAM usage and report back to the eponymous OpenAI boss. Sam Altman infamously described people having spare, underutilized DRAM in computers at home as “[quite terrible](https://www.tomshardware.com/tech-industry/data-centers/openai-ceo-says-its-quite-terrible-for-your-pc-to-have-ram-sam-altman-says-data-centers-offer-better-utilization)” in a recent podcast. Thus, developer Iain Kay was inspired to write a bash script that emails the OpenAI boss once a day to report on any RAM that is underutilized. Clearly this is not a serious tool, or rather “The memory accounting is. The correspondence isn't,” says Kay.

ram-altman leans on the MemAvailable query, which returns the kernel's own estimate of how much memory programs can claim without swapping, explains the developer of this script. When installed, it checks every five minutes and emails Altman once a day if you are found to be wasting this precious resource.

The emails take the .CSV file logs of your RAM use throughout the day as the data source to compose a summary email. These script-generated messages rotate through eight subject lines, 10 humorous message boilerplates, and six signoffs. Sample emails can be seen on the [ram-altman.lol](https://ram-altman.lol/) website. Altman’s email address isn’t supplied as part of the script.

If your machine is using 90% or more of its RAM, then you won’t be reported to the OpenAI boss for wasting memory. Also, if you don’t want to disturb Altman, you can run the tests without emailing anyone with the terminal command: *bash ram-altman.sh --dry-run*

The developer isn’t too scathing of the OpenAI boss. Kay quotes Altman’s explanations that his remarks were taken out of context. Moreover, the dev doffs his cap to the artificial intelligence leader’s humorous display name change to ‘Ram Altman’ on X last week. That’s where the name for this script came from.

ram-altman is a free bash script available on GitHub. It runs natively on Linux. On Windows, you can use WSL to run it, but someone has ported it [for PowerShell](https://github.com/paradonym/ram-altman-windows/blob/main/test-ram-altman.ps1) too. It won’t run on Mac, but Altman and his minions would find it inconvenient, at best, to remove your soldered-down Apple RAM.

*Follow Tom's Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

- 
Tanakoi said:Creating a program to auto-flood a personal email account is no different than any other malicious software, and both the script author and anyone who uses it should face criminal charges.Oh, lighten up... it doesn't even include his actual email and it's not like every rando knows what it is anyway. This is, in fact, a hilarious use of coding and I applaud the maker.
[Reply](https://forums.tomshardware.com/threads/spoof-program-monitors-and-emails-your-ram-usage-to-sam-altman-if-under-90-utilization.3902112/)
- 
I wonder what sam Altman thinks of the unoccupied rooms in the vacation homes of his fellow rich buddies and investors. Perhaps he'd like to weigh on the moral dilemma of stealing the Internet to sell it back to us?
[Reply](https://forums.tomshardware.com/threads/spoof-program-monitors-and-emails-your-ram-usage-to-sam-altman-if-under-90-utilization.3902112/)
- 
I would love to see Sam's horrified expression when he finds out what I'm doing with my PC when I start maxing out RAM utilization. :devilish: I'm not sure what will do more mental damage to him -- the lack of profit motive or the subject matter.
[Reply](https://forums.tomshardware.com/threads/spoof-program-monitors-and-emails-your-ram-usage-to-sam-altman-if-under-90-utilization.3902112/)

## Summary

**TLDR:** ram-altman is a joke, but it lands because the memory shortage is real, and Altman's 'idle RAM is terrible' line sounds like a landlord complaining about your spare room.

- Developer Iain Kay's ram-altman bash script checks RAM every five minutes and emails Sam Altman once a day if utilization is under 90%.
- It reads the kernel's MemAvailable estimate, logs usage to CSV, and rotates through 8 subject lines, 10 message templates, and 6 sign-offs.
- Altman's email address is not included, and a --dry-run flag lets users test it without sending anything.
- It responds to Altman's podcast remark that spare home RAM is 'quite terrible' compared with data center utilization.
- The satire touches a real sore spot: consumers are paying more for memory while AI data centers absorb supply.

## 摘要

**重點摘要：** ram-altman 是個玩笑，但它好笑是因為記憶體短缺是真的；Altman 那句「閒置 RAM 很糟」，聽起來就像房東嫌你家空房沒租出去。

- 開發者 Iain Kay 寫的 ram-altman 是一支 bash 腳本，每 5 分鐘檢查一次 RAM，使用率低於 90% 就每天寄一封信給 Sam Altman。
- 它讀取核心的 MemAvailable 估計值，把用量記到 CSV，信件會輪流使用 8 種主旨、10 種內文範本與 6 種結尾。
- 腳本沒有附上 Altman 的信箱，還有 --dry-run 參數可以只測試、不寄信。
- 起因是 Altman 在 podcast 上說，家用電腦閒置的 RAM 跟資料中心的使用率比起來「相當糟糕」。
- 這個惡搞戳中真正的痛點：AI 資料中心吃掉供給，消費者買記憶體越來越貴。