---
category: industry
lang: en
published: '2026-11-11T18:33:05.371180+00:00'
sources:
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/drones/data-center-demand-for-fiber-optics-squeezes-ukrainian-drone-operations-supply-crunch-has-incurred-6x-10x-cost-increase-for-critical-cabling
- name: Wired
  url: https://www.wired.com/story/michigan-voters-want-utility-money-out-of-politics-lawsuit/
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/data-centers/softbank-loses-usd3-7-billion-on-canceled-ai-data-center-gas-turbine-orders-days-after-denying-elon-musks-claim-it-was-defaulting-company-kills-reserved-13-gigawatts-of-power-more-than-six-hoover-dams-worth-of-capacity
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/policy/microsoft-lobbies-against-potential-ban-on-chinese-optical-networking-gear-for-ai-data-centers-as-fcc-mulls-restricting-imports-industry-group-says-move-could-grind-data-center-rollout-to-a-halt
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/data-centers/china-builds-massive-800-megawatt-ai-data-center-campus-to-rival-us-stargate-project-galaxy-campus-delivers-first-120-megawatts-in-a-year-at-one-fifth-the-cost
summary: SoftBank just ate a $3.7 billion loss on turbines it never switched on, and
  that's not even the strangest thing about AI's infrastructure crunch.
title: AI's Real Bottleneck Isn't Chips. It's Glass, Gas, and Angry Voters
trending_theme: AI's Power and Infrastructure Crunch
type: analysis
---

The most revealing AI hardware story of 2026 isn't about a GPU. It's about a Japanese investment firm paying $3.7 billion to *not* own gas turbines.

According to the *Wall Street Journal*, SoftBank had reserved more than 13 gigawatts of turbine capacity from GE Vernova. That's more generating capacity than the whole state of Connecticut, or about six Hoover Dams. It has now cancelled the remaining reservations and taken the write-down. Days earlier, its CFO had denied Elon Musk's claim that SoftBank was defaulting on turbine blade contracts: "there is no such default." Technically that was true. Strategically it was beside the point.

Most people will read this as "Masa overreached again," and he did. The more useful reading is this: **the AI race is now a contest of physical logistics, and the industry is learning that the hard way.** Chips were the bottleneck in 2023. In 2026 the bottleneck is anything that needs a factory, a permit, or a vote: turbines, transformers, fiber, optical transceivers, and the patience of ratepayers.

## Hoarding was a bet on lasting scarcity, and it's breaking

Turbine makers charge tens of millions of dollars per gigawatt just to hold a slot. Delivery estimates for new units have slipped as far as 2030. SoftBank reasoned the way everyone in AI reasoned in 2024: if supply is short, own the supply. Whoever holds the turbines decides who gets to build.

That logic held only while scarcity was expected to last. It works for land and fails for capital equipment when (a) your own projects slip, and (b) everyone else finds workarounds. Both are happening. SoftBank's flagship project is a 9.2 GW, $33 billion gas plant in Ohio feeding an 8 GW data center leased to OpenAI. Construction doesn't start until early 2027, and Nvidia has been in discussions about guaranteeing about $250 billion of the financing. When a chip vendor has to backstop the customer's landlord's power plant, the capital stack is shaky.

The workarounds are moving quickly. SpaceX now makes its own turbine blades for Musk's AI facilities, which it says cuts generator delays by 18 months. Turbine makers are adding capacity. Once a scarce item stops being reliably scarce, a hoarder is left holding expensive inventory, and SoftBank was the hoarder.

**So what:** expect more cancelled reservations. SoftBank is the first big name to unwind publicly, but other speculative capacity reserved in 2024–2025 now has to justify itself against real tenants and real financing.

## The war for glass

Here's the part almost nobody in AI coverage is discussing: **the data center buildout is now in direct competition with a shooting war.**

Fiber-optic drones, tethered by a spool of glass fiber that jamming can't touch, have become standard equipment in Ukraine. Ukraine and Russia together are estimated to produce about 50,000 of them a month, with ranges up to 62 miles. A representative of the Ukrainian drone maker BlueBird Tech told *Ars Technica* that fiber prices have risen 6–10x over the past couple of years as AI data centers absorbed supply.

The numbers are lopsided. In August 2025, Ukraine obtained 72 miles of fiber from Chinese suppliers. Russia imported 328,000 miles in the same month. Over all of 2025, Russia is estimated to have bought 37 million miles, more than 10% of global production. The world is estimated to be 111 million miles short. Some Chinese suppliers reportedly refuse to sell to Ukraine at all, and building domestic production requires trained staff who have to practice on fiber Ukraine doesn't have.

That's what a physical bottleneck actually looks like. Fiber is a commodity used by hyperscalers, telecoms, and militaries alike. When Microsoft, Meta and Oracle all buy at once, the marginal buyer gets priced out, and right now the marginal buyer is defending a front line. AI companies talk about "compute as a strategic asset." Their purchasing is already shaping geopolitics, and nobody signed up for that.

## Washington wants to cut China out of the optics supply. It can't yet.

Up one level from fiber are optical transceivers, the modules that turn electrical signals into light so GPUs in different racks can work as one cluster. The FCC is weighing an import ban on Chinese transceivers on espionage and sabotage grounds, the same logic it used against Huawei. Microsoft, which is building 35 US data centers and plans 134 more, has lobbied the White House against it through the Information Technology Industry Council.

ITI's John Miller put the problem plainly: without transceivers, AI chips "literally could just sit there waiting around unutilized." Chinese vendors hold somewhere between 56% and 66% of the global market, depending on whose count you use. The US alternatives are essentially Coherent and Lumentum. The Huawei comparison breaks down here: when Washington banned Huawei, Ericsson and Nokia were ready to take over. For data center optics, no one has that kind of spare capacity.

My view: the security concern is real, but a quick ban would hurt US AI capacity far more than it would hurt Beijing. A $40,000 GPU sitting idle for want of a $1,000 module is the most expensive way to make a point.

## Meanwhile, China builds cheaply and powers it with wind

SemiAnalysis visited Envision's Galaxy campus in Ulanqab, Inner Mongolia. It's planned at 800 MW of IT capacity by the end of 2027, close to the ~820 MW at OpenAI's Stargate site in Abilene, Texas. The first 120 MW went up in less than a year at about **one-fifth the cost** of comparable US projects.

The power approach is the real contrast. US developers are adding on-site gas turbines to get around grid queues. Envision is building 420 MW of its own wind capacity across two farms, about 80 km apart, to serve 240 MW of load in the first two phases, backed by four-hour battery storage because Ulanqab's wind capacity factor is only around 35–40%. Inside, solid-state transformers convert 10 kV AC directly to 800 V DC for the racks, skipping several conversion stages that US facilities still use.

The second-order point: **the US is trying to win an infrastructure race with 20th-century generation and 21st-century permitting delays**, while China treats the data center, the power plant and the electrical design as one product. America still has the better chips. China is getting good at everything that surrounds them.

## Data centers have become a ballot issue

Then there are the voters. In Michigan, 81% voted for Proposal 2, which bans political donations from utilities and from contractors with more than $250,000 a year in state and local contracts. Consumers Energy and DTE sued within days, claiming First and 14th Amendment violations.

The background is simple: Michigan has at least 26 planned data center projects. DTE has proposed two gas plants costing $6.4 billion to serve possible data center load, with ratepayers potentially paying for them. Residential bills rose 10% in the past 12 months, the fourth-largest increase in the US. People connect those numbers on their own.

This is the change that matters most. Data centers used to be invisible, a warehouse with a tax break. Now they show up on a power bill, and the utilities that courted them are the political target. If AI's social license runs through utility rates, the industry has a problem no software update can fix.

## The bear case

The strongest counterargument: this is a normal capex cycle, and shortages always end. Turbine makers add lines, Coherent and Lumentum add capacity, fiber plants come online, and by 2028 we're talking about overbuild. SoftBank's cancellation even supports this, since people don't cancel scarce goods.

I partly agree. Equipment shortages will ease. Political limits won't, because you can't manufacture your way out of an angry electorate or a national-security ban. The bottleneck isn't going away. It's moving from factories to legislatures.

## What to Watch

- **The FCC transceiver ban arrives with a long phase-in.** I expect a headline ban with waivers or transition periods of 18–24 months. Washington won't idle its own GPUs. Watch for Coherent and Lumentum to announce capacity expansions with federal support within six months.
- **More turbine reservations get cancelled in 2027.** At least one more major developer or hyperscaler will disclose cancelled or resold capacity. GE Vernova's backlog commentary is the signal to follow.
- **"Large-load" tariffs spread.** Expect several more states to make data centers pay directly for the generation built to serve them, using Michigan as the political template. Utilities will fight Proposal 2 to the appellate courts and probably lose on the contractor provisions.
- **800 V DC becomes the next spec war.** Envision is already running it. US operators will announce 800 V DC deployments by late 2027, and power-electronics suppliers stand to gain more than another GPU generation would deliver.
- **The fiber shortage becomes a defense-policy issue.** NATO governments will start treating optical fiber as strategic material, with stockpiles, export rules and subsidized non-Chinese supply. When that happens, AI companies will find they're competing with defense ministries for the same spools.