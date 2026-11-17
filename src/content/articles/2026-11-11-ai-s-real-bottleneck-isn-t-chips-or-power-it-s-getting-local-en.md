---
category: industry
featured: true
lang: en
publishedAt: '2026-11-11T06:27:18.612864+00:00'
relatedSlugs: []
sources:
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/x-energy-gets-green-light-to-build-its-first-small-modular-nuclear-reactors/
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/data-centers/china-builds-massive-800-megawatt-ai-data-center-campus-to-rival-us-stargate-project-galaxy-campus-delivers-first-120-megawatts-in-a-year-at-one-fifth-the-cost
- name: Wired
  url: https://www.wired.com/story/bug-activists-and-biker-gang-members-are-teaming-up-to-protest-data-centers/
- name: TechCrunch
  url: https://techcrunch.com/2026/11/09/fervo-now-has-12b-in-orders-for-its-geothermal-power-tech/
- name: The Verge
  url: https://www.theverge.com/science/1030252/ai-data-center-climate-pledge-united-nations-cop31
summary: Anthropic can buy $3.4 billion of gas turbines, but it can't buy the consent
  of a Thurrock biker gang.
tags: []
title: AI's Real Bottleneck Isn't Chips or Power. It's Getting Locals to Say Yes
trending: true
type: analysis
---

Everyone says AI has an electricity problem. That's only half right. Electricity can be bought, built, or burned. What AI is really short of is permission: from regulators, from grid operators, and from the people who live next to the site. This week's news shows that permission, not megawatts, now sets how fast AI can grow.

Look at what happened in one week. Anthropic reportedly committed $3.4 billion to gas turbines. Fervo's contracted geothermal revenue rose from $7.2 billion to $11.9 billion in a single quarter. The NRC approved X-energy's first four small modular reactors. Envision built 120MW of a Chinese AI campus in under a year. And in Europe, protesters climbed a crane at a Microsoft data center site in Amsterdam, while nearly 55,000 people signed a petition telling Google to "search elsewhere" than Thurrock, Essex.

These look like separate stories about energy and activism. They're one story. Every company in it is paying to skip a queue.

## The price of skipping the line

Start with the gas turbines. Nobody spends $3.4 billion on on-site generation because gas is cheap. They do it because the alternative is waiting years for a grid interconnection that may never come. US turbine shortages have already pushed some delivery estimates to 2030. SpaceX has started making its own turbine blades because it was tired of waiting. OpenAI's Stargate site in Abilene, Texas, with about 820MW of critical IT capacity, is also adding gas turbines. Behind-the-meter gas has become the default fix for American AI. You aren't buying the cheapest power. You're buying power you control on your own timeline.

Fervo's numbers show where that leads. Its first Cape Station phase in Utah cost $7,000 per kilowatt. The 396MW Google project, now called Cape Google 400, costs $5,500 per kilowatt. TechCrunch notes that even with subsidies, that's roughly what a new gas plant costs when gas runs $6 per million BTUs, which is about double the current price of gas. By any normal utility standard, it's expensive power.

Hyperscalers are buying it anyway, because speed matters more to them than price right now. Fervo CEO Tim Latimer said it plainly on the earnings call: "We built Cape Station on our schedule. Google can develop a potential data center on their schedule, and neither party is waiting on the other." Read it as a statement about time, not geothermal. Google is paying a premium so its plans don't depend on anyone else's schedule.

## Here's what nobody is talking about: power is being sized to match server halls

The design detail worth paying attention to is in Fervo's GeoBlocks. Each newer well produces 15MW gross. Several wells together form a GeoBlock, and the latest ones produce 50MW, which Fervo says is about what a typical data center hall uses. Power is now built in hall-sized units that switch on one at a time.

X-energy's Xe-100 does the same thing at 80MW per reactor. Envision does it in Inner Mongolia, sizing wind and batteries to each phase of its Galaxy campus. Nuclear plants and gas plants used to be gigawatt projects that cities built around. Now the unit of generation is shrinking to the unit of compute.

The consequence goes beyond engineering. Power built in small blocks can be approved in small blocks. A 1GW plant needs one huge yes that's easy to block. A series of 50MW blocks lets a developer collect smaller approvals over time. The industry is breaking its power supply into pieces partly to make it harder for anyone to stop the whole thing.

## China isn't winning on chips. It's winning on approvals

SemiAnalysis visited Envision's Galaxy campus in Ulanqab and found the first 120MW finished in under a year, at roughly one-fifth the cost of comparable US projects. The full campus targets 800MW of IT capacity by the end of 2027, about the size of Stargate Abilene.

The power setup is clever. Envision built 420MW of wind across two farms about 80km apart to serve 240MW of load in the first two phases. With Ulanqab's capacity factor of 35–40%, 420MW of wind averages around 155MW. That's about 65% of the load, which matches Envision's target of "over 60%," and four-hour batteries cover the gaps. Inside, solid-state transformers convert 10kV AC straight to 800V DC at the rack, skipping several conversion steps that US facilities still use.

The one-fifth cost figure isn't mainly about cheap labor or cheap steel. It reflects how much less time Envision spends getting approvals. There's no Buglife lawsuit or petition in Ulanqab, and nobody is arguing over a rare bumblebee. When the government decides Inner Mongolia is a compute zone, permits are settled before construction begins. In democracies, permission costs a lot. In China, it costs almost nothing. That gap counts as much as anything Nvidia ships.

## The backlash is a coalition, and that's what should worry developers

Wired's account of Thurrock deserves a close read because of who showed up. Buglife is worried about an endangered plant and invertebrate habitat. Foxglove is worried about emissions. The Thurrock Hammers motorcycle club wants its racetrack back. These groups don't normally agree on anything, and they're working together.

Developers should take that seriously. A single-issue protest can be settled. You add a biodiversity offset, sign a renewables PPA, or donate to a local charity. A coalition with unrelated grievances has no single price. Google's answer, that it "shares the concerns" of Buglife, speaks to the bug people and ignores the bikers.

Amsterdam has seen this before. The city paused new data centers in 2019. Ireland's data centers used about 21% of the country's electricity in 2023, and Dublin's grid operator effectively stopped new connections. This month's crane climb at the Microsoft site comes after years of unease, and it was part of coordinated actions across Europe.

That's why on-site gas is riskier than it looks. Turbines fix the grid problem and make the community problem worse. Each turbine at a data center gives Foxglove-type groups something concrete to oppose: a smokestack, air permits, NOx emissions. Companies are swapping a queue at the utility for a fight in the local planning committee.

## The pledges won't help

COP31 in Antalya is producing an "AI Pledge" that its own text calls "voluntary and non-prescriptive" and says "create[s] no new obligations." The Verge called it a cruel joke, and that's fair. The bigger problem is that it misreads the politics. Climate pledges are written for diplomats. The people who decide data center sites are county commissioners, planning inspectors, and neighbors with petitions. No national pledge has ever won a planning appeal in Thurrock.

## The bear case

Some of this demand may be inflated. Utilities report interconnection requests far beyond what will actually be built, because developers file for multiple sites and drop most of them. If model efficiency keeps improving, as DeepSeek showed in early 2025 that it can suddenly, the hyperscalers' willingness to pay any price could end quickly. Fervo says its own business depends on getting costs down. X-energy shares are already trading below half their April IPO price, and its first reactors won't run until the early 2030s. Investors are pricing in exactly this risk. If the AI capex cycle cools in 2027, expensive firm power signed in 2026 turns into stranded assets.

I still think the bear case gets the timing wrong rather than the direction. Even if demand comes in 30% below forecasts, the gap between what gets proposed and what gets approved keeps growing. Grid capacity that's hard to get stays valuable whether or not demand peaks.

## What to Watch

- **A major European project gets cancelled or moved.** Before the end of 2027, at least one hyperscaler will publicly drop or relocate a European data center over local opposition, not grid limits. Thurrock is a strong candidate.
- **On-site gas becomes the next protest target.** Within 18 months, air-permit challenges against behind-the-meter turbines will be the main legal tactic against US data centers.
- **Fervo passes $20 billion in contracted revenue by Q3 2027,** and at least one non-Google hyperscaler signs a GeoBlock-style phased deal.
- **X-energy's Dow reactors start after 2032.** The deferred safety questions the Union of Concerned Scientists flagged will come back as delays.
- **800V DC becomes a standard US spec by 2028,** after Chinese campuses show the efficiency gains.
- **Community benefit agreements get priced into AI capex.** Expect hyperscalers to start disclosing local "consent spend" as its own line item. In democracies, that's what permission now costs.