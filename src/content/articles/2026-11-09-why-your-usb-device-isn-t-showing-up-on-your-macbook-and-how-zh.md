---
category: products
faqs:
- answer: 常見原因是 macOS 要求配件連線前先取得授權，如果拒絕了提示，資料就無法傳輸。線材損壞或配件電力需求太高也可能造成問題。
  question: 為什麼 Mac 抓不到 USB 配件？
- answer: 把配件拔掉再重新插上，macOS 通常就會再次顯示授權提示，讓你允許連線。
  question: 要怎麼讓 macOS 的 USB 授權提示再次出現？
- answer: 這個機制是為了防止來路不明的 USB 裝置植入惡意程式。被拒絕的配件仍可充電，但在授權前無法傳輸資料。
  question: macOS 為什麼要求授權才能連接配件？
featured: false
lang: zh
publishedAt: '2026-11-09T01:00:00+00:00'
relatedSlugs: []
sources:
- name: Engadget
  url: https://www.engadget.com/2309279/why-usb-device-not-showing-up-macbook-fixes/
summary: USB 裝置抓不到，多半不是壞了，真正的元凶其實是 macOS 那個不太起眼的配件連線授權提示。這也說明了安全機制往往會在不知不覺中犧牲使用便利性。
tags:
- products
- hardware
- cybersecurity
title: MacBook 抓不到 USB 裝置？原因與解決方法一次看
trending: false
type: news
---

# Why your USB device isn't showing up on your MacBook and how you can fix it

Fix hardware and software issues with some simple solutions.

USB wouldn't be what it is today without Apple. The format predates the [original iconic iMac](https://www.engadget.com/2018-05-06-apple-imac-turns-20.html) — but Apple's gumdrop-shaped computer helped popularize it by ditching all the legacy connectors that had been haunting the industry. USB became so commonplace, in fact, that the push came back to bite the company, with European Union regulations [forcing it to ditch Lightning ports on iPhones](https://www.engadget.com/iphones-switch-usb-c-comply-eu-charger-law-075020117.html). The days of Apple-exclusive ports are effectively over, MagSafe being the major remaining holdout.

Modern [USB Mac accessories](https://www.engadget.com/computing/accessories/best-macbook-accessories-150014737.html) tend to be well-behaved. On occasion, though, macOS can fail to detect them, which is understandably maddening. With USB being as widespread as it is, anything less than a seamless experience feels unacceptable.

The good news is that there are known hardware and software explanations for why this happens, like damaged cords or an accessory that requires more power. In many situations the fixes are remarkably simple, particularly on the macOS side. There are rare instances, however, where you may need to seek outside help.

## How to solve missing USB devices on your Mac

The first thing to remember is that by default, macOS requires you to give permission for accessories to connect. This prevents malware from being injected. At the same time, if you accidentally reject a permission prompt, a legitimate accessory won't transmit data until you give the green light. Charging should still work in either direction.

Typically, you can force macOS to re-display the permission prompt by unplugging an accessory and plugging it back in again. To minimize future hassle, though, go to **Apple menu > System Settings > Privacy & Security**, then scroll down to the **Accessories** section. Here you can choose **Ask for new accessories**, **Automatically allow when unlocked** or **Always allow**. It's best to skip that third option unless you're always around your Mac or in a very secure environment.

If that doesn't change anything, you might want to verify that macOS sees your device in the first place. Hold down the Option key, then click on **Apple menu > System Information**. If you see the accessory listed under **Hardware**, you may need to check the manufacturer's online support info. If it's invisible, or if it's detected but you keep getting an error message when plugging in, there may be more we can help with.

A probable cause in that regard is power. Some accessories may require more than a Mac's USB port can supply, in which case you should get a related message, and there may be a separate power cable you need to plug in. If there's no separate power on your accessory, however, the USB port itself may be the issue. Try alternate ports on your Mac or connecting directly if you were using a hub or dock as an intermediary. If you keep getting power-related warnings, you may want to talk to Apple tech support — it could be that your Mac just isn't feeding power to USB.

## Other potential USB flaws and their fixes

Speaking of hubs and docks, don't forget that those often require their own power supplies. And even if they don't, things can go wrong with device chains, since of course they have to successfully transmit power or data across multiple hops. We recently had an experience with a Thunderbolt dock in which a wireless mouse receiver became unusable until it was plugged directly into a laptop — never mind that an SSD on the dock was doing just fine. It's always safer to skip the middleman if you have enough ports free.

Make sure that macOS is fully up-to-date by going to **Apple menu > System Settings > General**, then clicking on **Software Update**. Bugs or driver compatibility issues could hypothetically be interfering. Some accessories may also rely on proprietary software to do much of anything, in which case you'll want to make sure the latest version of that is installed. Check the Mac App Store or a manufacturer's website. External cards and drives need to use file system formats compatible with macOS, namely APFS, FAT or ExFAT.

Lastly, be sure that you're using the right type of USB cable for a device's power and bandwidth requirements and that there's no damage or debris interfering with either cables or ports. Things like lint and bent pins may be all it takes to block something from working. Lint, dust and grime can typically be cleaned out with an air can or by gently swiping a soft-tipped tool. As for damage, you'll likely just need to swap in a new cable, especially if there are any signs of browning or exposed wires. Those signal a fire hazard.

## Summary

**TLDR:** Your missing USB device often isn't broken. macOS's accessory permission prompt is the hidden culprit, and it shows how security quietly costs usability.

- By default, macOS asks for permission before an accessory can connect, to block malware injection over USB.
- If you accidentally reject the prompt, the device won't transfer data, though charging still works.
- Unplugging and reconnecting the accessory usually brings the permission prompt back.
- Other common causes include damaged cables and accessories that need more power than the port supplies.
- EU rules forced Apple to move the iPhone from Lightning to USB-C, leaving MagSafe as the main remaining Apple-only connector.

## 摘要

**重點摘要：** Mac 抓不到 USB 裝置，常常不是壞了，而是 macOS 的配件授權提示在作怪，這正是安全默默犧牲易用性的例子。

- macOS 預設會在配件連線前要求授權，以防止惡意程式透過 USB 植入。
- 如果不小心按了拒絕，裝置就無法傳輸資料，但充電仍然正常。
- 通常只要拔掉再重新插上，授權提示就會再次出現。
- 其他常見原因包括線材損壞，或配件需要的電力超過連接埠能提供的範圍。
- 歐盟法規迫使 iPhone 從 Lightning 改成 USB-C，MagSafe 成為蘋果碩果僅存的專屬接頭。