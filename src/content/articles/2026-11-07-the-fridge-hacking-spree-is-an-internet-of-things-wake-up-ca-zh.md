---
category: industry
faqs:
- answer: 攻擊者鎖定聯網冷凍系統，讓至少 11 個歐洲國家的連鎖超市冰箱溫度升高，造成大量食物報廢。在法國，血液機構 EFS 使用的冷藏室也在 11 月
    2 日被升到非常高的溫度。
  question: 歐洲冰箱駭侵事件發生了什麼事？
- answer: 沒有。EFS 表示，警報系統與工作人員迅速發現溫度異常並啟動備援措施，血液與血漿沒有變質或受損。
  question: 法國的血液庫存有受損嗎？
- answer: 它顯示關鍵供應鏈裡的聯網設備不需要高階駭客技術，就能讓醫療與食品系統出問題。供應商資安審查、網路分段與實體警報等基本措施，和防範 AI 輔助攻擊一樣重要。
  question: 這起攻擊對物聯網資安有什麼啟示？
featured: false
lang: zh
publishedAt: '2026-11-07T13:00:00+00:00'
relatedSlugs: []
sources:
- name: Wired
  url: https://www.wired.com/story/kernel-panic-refrigeration-hacks-internet-of-things/
summary: 外界都在擔心 AI 驅動的駭客攻擊，但今年最令人不安的基礎設施攻擊，竟然來自連網冰箱，起因是基本的資安防護沒做好。
tags:
- cybersecurity
- hardware
- policy
title: 冰箱遭駭事件頻傳，為物聯網安全敲響警鐘
trending: false
type: news
---

*Welcome to [Kernel Panic](https://www.wired.com/newsletter/exclusive/kernel-panic),* *a weekly newsletter by [Lily Hay Newman](https://www.wired.com/author/lily-hay-newman/) and [Matt Burgess](https://www.wired.com/author/matt-burgess/) from inside the new world of privacy and digital security. To receive this newsletter in your inbox each week, [sign up here](https://www.wired.com/newsletter/exclusive/kernel-panic).*

Amid an onslaught of [AI vulnerability discovery](https://www.wired.com/story/kernel-panic-ai-vulnerability-explosion/) and [AI-assisted hacking](https://www.wired.com/story/ai-tools-are-helping-mediocre-north-korean-hackers-steal-millions/), some of the most consequential critical infrastructure attacks this year may have little to do with the technology at all—instead providing a stark reminder that cybersecurity fundamentals are still key to digital defense.

Three sites in France that handle blood and plasma bags were briefly impacted this week by widespread attacks on vulnerable internet-connected refrigerators. On Wednesday, the Établissement Français du Sang (EFS) [confirmed](https://presse.efs.sante.fr/actualites/l-efs-confirme-l-incident-de-cybersecurite-impactant-un-de-ces-prestataires-d-equipement-frigorifique-2c07c-08a0a.html) that cold rooms storing blood were “raised to very high temperatures” on November 2. The blood samples, thankfully, weren’t altered or damaged, the EFS said, because the organization’s alarm facilities and [staff](https://www.cyberattaque.org/cyberattaque-contre-lefs-des-hackers-sattaquent-aux-reserves-de-plasma-sanguin/) quickly detected the changes and implemented fail-safe measures.

The incident, however, comes amid a wave of cyberattacks in recent days affecting supermarket chains in at least 11 European countries that also drastically increased the temperatures of their refrigerators. Pictures from across the continent show [huge volumes of food being trashed](https://www.theguardian.com/world/2026/nov/02/supermarket-freezers-across-europe-hit-by-second-suspected-cyber-attack) following the spikes. Similar fridge attacks in October affected hundreds of French stores that were forced to throw away food. And in August, roughly six commissaries and grocery stores on United States military bases suffered similar incidents resulting in spoiled food. The Pentagon is investigating the incidents and is collaborating with French law enforcement, Reuters [reported](https://www.reuters.com/technology/pentagon-treating-military-base-freezer-malfunctions-suspected-cyberattack-2026-10-29/) last week.

“It's been true for more than a decade now that our dependence on connected technology is growing faster than our collective will to protect it, which has exposed us to accidents, adversaries, and now potentially agents,” says longtime critical infrastructure researcher Josh Corman, who is currently the executive in residence for public safety and resilience at the nonprofit Institute for Security and Technology. “These fragile cold-chain systems are too critical to fail, but we keep experiencing hard lessons.”

It is still unclear who is behind the incidents and whether the attacks are all connected or being carried out by multiple actors. The first recent wave of attacks against French supermarkets last month appears to have been caused by attackers exploiting [unpatched](https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-012/) refrigeration controllers exposed to the internet—including software versions that [allegedly](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers) used weak passwords formulated based on the date.

Many of the hacks stem from attackers exploiting vulnerabilities in temperature controllers made by the Danish firm Danfoss, and researchers say the attacks would not have been particularly difficult to pull off. Danfoss did not return WIRED’s request for comment.

In other statements, Danfoss [said](https://www.reuters.com/business/retail-consumer/french-supermarket-chain-intermarche-hit-by-cyberattack-150-stories-targeted-2026-10-12/) impacted systems “were running outdated firmware” and urged customers to keep products updated. In an [alert](https://www.cisa.gov/resources-tools/resources/us-government-partners-urge-hardening-industrial-refrigeration-and-cold-chain-monitoring-systems) on Thursday addressing the rash of incidents, the US Cybersecurity and Infrastructure Security Agency said attacks could exploit flaws in cold storage systems via authentication bypasses, arbitrary code injections, and weak configurations. Experts have long warned about the dire threats to critical infrastructure posed by these types of weaknesses in so-called internet-of-things devices.

Russian hacktivists tried to [claim responsibility](https://www.bbc.co.uk/news/articles/c8vgxyvz6y9ro) for some of the attacks but did not provide credible evidence. Still, some researchers [see signs](https://www.thetimes.com/world/europe/article/cyberattack-civilian-target-trigger-article-5-nato-sr9j723cn) that Russia-based actors may have been involved in at least [some](https://www.flyingpenguin.com/french-food-chains-hacked-with-freezer-bug-following-us-military-base-case/) of the incidents. The Kremlin this week [denied](https://www.interfax.ru/russia/1127149) involvement. In other cases, researchers have found [potential ties to Iran-linked](https://www.npr.org/2026/11/03/nx-s1-6026676/cold-war-hackers-fridges) actors. NextGov/FCW [reported](https://www.nextgov.com/cybersecurity/2026/10/officials-suspect-iran-series-cyberattacks-military-base-freezers/416934/) last week that unnamed US officials suspect Iran-linked attackers may have been behind the freezer attacks on US military bases, though they noted that the investigation is still ongoing.

This type of refrigerator/freezer attack is not new. Back in 2022, 16 supermarkets in Russia were targeted at the start of the country’s full-scale war with Ukraine. That year, 40 stores in Israel were similarly attacked, [according](https://assets.danfoss.com/documents/latest/533772/AO540160316124en-000101.pdf) to a 2025 report by Danfoss.

“Many businesses use older technology while the systems become increasingly connected,” Sweden’s National Cyber Security Center [pointed out](https://www.ncsc.se/sv/aktuellt/cyberangrepp-mot-kylsystem) in a recent advisory about the freezer attacks, noting that companies should inventory which of their devices are connected to the internet, disconnect them whenever possible, and make sure they are kept access-controlled, patched, and monitored if they must be connected.

## Comments

Back to top

## Summary

**TLDR:** Everyone is worried about AI-powered hackers, but this year's scariest infrastructure attack came from internet-connected fridges with weak security basics.

- France's blood service EFS confirmed that cold rooms storing blood were 'raised to very high temperatures' on November 2 after an equipment supplier was hit.
- EFS said the blood was not damaged because alarms and staff caught the change quickly and fail-safe measures kicked in.
- Similar attacks hit supermarket refrigerators in at least 11 European countries and spoiled large amounts of food.
- The attacks used weak spots in connected refrigeration equipment from suppliers, not advanced AI tools.
- IoT devices in critical supply chains need basic security such as changing default credentials, network segmentation, and vendor oversight.

## 摘要

**重點摘要：** 大家都在擔心 AI 駭客，但今年最嚇人的基礎設施攻擊，卻來自基本資安沒做好的聯網冰箱。

- 法國血液機構 EFS 證實，一家設備供應商遭攻擊後，儲血冷藏室溫度在 11 月 2 日被「調高到非常高」。
- EFS 表示血液沒有受損，因為警報系統與人員迅速發現異常，並啟動了備援措施。
- 類似攻擊同時波及至少 11 個歐洲國家的超市冰箱，造成大量食物報廢。
- 攻擊利用的是供應商聯網冷凍設備的弱點，不是高階 AI 工具。
- 關鍵供應鏈中的物聯網設備需要做好基本資安，例如更改預設帳密、網路分段與管理供應商。