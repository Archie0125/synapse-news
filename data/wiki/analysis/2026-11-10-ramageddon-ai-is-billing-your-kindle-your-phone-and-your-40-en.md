---
category: industry
lang: en
published: '2026-11-10T06:34:42.806108+00:00'
sources:
- name: TechCrunch
  url: https://techcrunch.com/2026/11/07/amazons-new-basic-kindle-proves-you-dont-need-all-the-bells-and-whistles/
- name: 9to5Google
  url: https://9to5google.com/2026/11/07/oppo-reportedly-cancels-find-x10-ultra-thanks-to-ramageddon/
- name: 9to5Google
  url: https://9to5google.com/2026/11/09/walmart-google-tv-streamer-lineup-price-hike/
- name: 9to5Google
  url: https://9to5google.com/2026/11/09/google-pixel-10a-deal-after-price-hike/
- name: Tom's Hardware
  url: https://www.tomshardware.com/pc-components/dram/memory-shortage-spurs-smartphone-makers-to-melt-used-memory-off-old-devices-then-re-solder-it-onto-new-products-recycled-memory-to-keep-budget-phones-affordable-reballing-adoption-to-double-by-2027
summary: The cloud AI boom is taking the memory your cheap devices need, and phone
  makers are now pulling chips out of old phones to keep up.
title: 'RAMageddon: AI Is Billing Your Kindle, Your Phone and Your $40 Stick'
trending_theme: RAMageddon Pushes Up Device Prices
type: analysis
---

The surest sign that AI demand has gotten out of hand isn't a trillion-dollar valuation or a gigawatt data center announcement. It's a factory in Shenzhen heating up an old phone's logic board, lifting off a 4GB LPDDR4X chip, and soldering it onto a "new" $150 handset.

That is happening now, and it's on the record. According to TrendForce, reballed memory (chips removed from old or scrapped devices and re-soldered onto new boards) already goes into 3–4% of smartphones. TrendForce expects that to reach 7–9% in 2027. The chips mostly end up in 4G phones priced under CNY 1,299 (about $200). The industry calls it cost management. A plainer description: the consumer electronics business can no longer get enough new memory to build its cheapest products.

Welcome to RAMageddon. Most coverage treats it as a pile of annoying price hikes. I think it's a transfer of wealth and capability from the edge to the cloud, and it is landing hardest on the people who can least afford it.

## The receipts

The past few weeks of price changes tell the story without any help:

- **Walmart's Onn Google TV lineup** went up another $10 per device this month, its second big hike of 2026. The cheapest streamer cost **$15** before this year. It now starts at about **$40**, an increase of more than 160%. The Onn 4K Pro went from $59.98 to $69.98, and the FHD stick from $29.98 to $39.98.
- **Google's Pixel 10a** launched at $499. In early October Google raised the starting price to **$599**, a 20% jump on a phone sold mainly on value. A $449 Woot deal looks like a bargain now only because the reference price moved.
- **Amazon's refreshed Kindle lineup** arrived in October **$40–$50 more expensive across the board**. The entry-level 6-inch Kindle now starts at $169.99 ad-free. It has no warm light, no waterproofing and half the Paperwhite's battery life.
- **Oppo** reportedly canceled the **Find X10 Ultra**, according to the leaker Digital Chat Station. It was supposed to carry a 200MP 1/1.12-inch main sensor, a 200MP periscope and a 50MP 10x telephoto. Oppo's current Find X10 Pro Max had already dropped from the X9 Ultra's Snapdragon chip and 16GB of RAM to a MediaTek chip and 12GB in most variants.

Look at the percentages. The flagship Pixel didn't take a 160% hike. The $15 streaming stick did. That pattern is the main thing to understand about this crisis.

## Why the cheap stuff breaks first

Memory makes up a much bigger share of the bill of materials in a $30 streaming stick than in a $1,200 flagship. A device with 1.5–2GB of RAM and 8GB of storage, sold on thin margins, has no room to absorb a jump in DRAM contract prices. The money has to come from somewhere, and Walmart chose the shelf price.

TrendForce makes the same point: budget buyers are the most price-sensitive, so brands can't raise prices without losing volume. Their options are to (a) pass the cost on, as Walmart, Google and Amazon did, (b) cut the spec, as Oppo did with the X10 Pro Max, (c) kill the product, as Oppo reportedly did with the Ultra, or (d) use reballed memory. In 2026 the industry is doing all four.

The cause is structural. Samsung, SK hynix and Micron have moved wafer capacity toward HBM for Nvidia and AMD accelerators, because HBM earns far better margins and the hyperscalers sign long contracts at almost any price. HBM also uses much more wafer area per bit than standard DRAM, so each wafer shifted to AI produces fewer bits for everyone else. Micron went as far as winding down its Crucial consumer brand. Memory makers aren't short of demand. They have decided who comes first, and your Kindle isn't near the top.

## What nobody is talking about: the cloud is eating on-device AI

This is the part I find most ironic. For the past two years every phone maker's pitch has been on-device AI. Apple Intelligence set an 8GB floor. Google's Gemini Nano drove Pixel RAM upward. Qualcomm and MediaTek built their flagship marketing around running local models, and local models consume RAM above everything else.

The AI boom in data centers is now starving the AI boom in your pocket. Oppo going from 16GB to 12GB isn't only a spec trim. It reduces the headroom for exactly the on-device models the industry promised would make phones "AI-native." If 12GB becomes the new flagship ceiling and 8GB the midrange ceiling for 2027, local AI features get smaller and more of the work moves back to the cloud. That drives more data center buildout and more HBM demand, which tightens memory supply further. The loop reinforces itself, and it pushes computing back toward centralized servers.

This is the second-order effect most people are missing. RAMageddon raises device prices, and it also quietly settles the edge-versus-cloud debate in favor of whoever owns the GPUs.

## The reballing problem

Reballed memory deserves more scrutiny than it gets. Reballing means reheating a chip that has already been through at least one reflow cycle and a full service life in someone's pocket. Thermal stress builds up with each cycle. Hobbyists can do impressive things with the technique: one turned a $120 secondhand SK hynix DDR5 SO-DIMM kit into desktop sticks running at DDR5-7800, a kit worth around $1,000 at today's prices. A hobbyist accepts the risk on their own hardware. A buyer of a $120 phone in Jakarta, Lagos or Dhaka never agreed to that.

TrendForce expects reballed and lower-spec parts to "gradually expand beyond the entry-level segment." If that happens, expect the first real reliability scandal within 18 months: a batch of budget phones with unusually high failure rates, traced to recycled DRAM. Disclosure rules don't exist yet. They should.

## The bear case, and why I don't buy it yet

The strongest counterargument is that memory is the most cyclical business in tech. In 2017–2018 DRAM prices spiked, and by 2019 they had crashed. In 2022–2023 the downturn was severe enough that Samsung, the market leader, posted heavy losses in its memory division. Every shortage brings a capacity rush, and every capacity rush ends in a glut. New fabs from SK hynix in Yongin, Samsung in Pyeongtaek and Micron in Idaho and New York will eventually flood the market, and today's $40 Onn stick will be $25 again.

That's correct about the long-term pattern and wrong about the timing. TrendForce expects DRAM prices to rise again in Q1 2027. New greenfield fabs take years to produce meaningful volume, and their first output is already committed to HBM. AI buyers also have a different demand curve from consumers. A hyperscaler spending $100 billion a year on capex doesn't cancel orders because DRAM went up 30%. Consumer demand destruction will happen, and it's starting, but it doesn't release supply when the marginal buyer is Microsoft.

There's also a ratchet effect. Prices that go up because of "memory costs" rarely come back down by the same amount. Google raised the Pixel 10a by $100. Don't expect the Pixel 11a to start at $499 again.

## Who wins

Apple, mainly. It has the scale and long-term supply contracts to keep its pricing stable while Android OEMs scramble, and a stable iPhone price looks better every time Android flagships cut specs or go up in price. Memory makers win too, along with Taiwan's second-tier DRAM suppliers that serve the legacy and consumer segments the big three are neglecting. The losers are Chinese Android brands with thin margins, retailers whose private labels depended on cheap components, and anyone who budgeted $200 for a phone.

## What to Watch

1. **More "Ultra" cancellations.** Oppo won't be alone. By mid-2027 expect at least one other Chinese OEM (Vivo, Xiaomi or Honor) to drop or delay an Ultra-tier camera flagship, or quietly ship it with less RAM.
2. **12GB as the 2027 Android flagship standard.** 16GB returns to being a gaming-phone and halo-SKU spec. Count how many spring 2027 flagships launch with 12GB base configurations.
3. **Reballed memory goes upmarket.** TrendForce's 7–9% figure for 2027 is the floor. The real signal will be reballed LPDDR5 in phones priced above $300.
4. **On-device AI gets quietly scaled back.** Watch for OEMs moving "AI features" to cloud processing in 2027 launches while keeping the same marketing language.
5. **The next price hike happens before the holidays end.** The Onn lineup has risen twice this year. Expect a third round in Q1 2027, and expect Fire TV and Chromecast-class devices to follow.

The AI industry likes to call itself a rising tide that lifts all boats. In 2026 the tide is mostly lifting prices, and the smallest boats are the ones taking on water.