---
category: industry
lang: en
published: '2026-11-10T06:29:52.070084+00:00'
sources:
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/data-centers/china-builds-massive-800-megawatt-ai-data-center-campus-to-rival-us-stargate-project-galaxy-campus-delivers-first-120-megawatts-in-a-year-at-one-fifth-the-cost
- name: TechCrunch
  url: https://techcrunch.com/2026/11/09/fervo-now-has-12b-in-orders-for-its-geothermal-power-tech/
- name: Dev.to
  url: https://dev.to/frankchu/34b-bought-anthropic-17-gw-of-gas-turbines-2ce2
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/data-centers/anthropic-skips-six-year-waitlist-with-massive-usd3-4-billion-gas-turbine-generator-deal-firm-takes-over-onepwrs-orders-secures-1-7gw-of-capacity-to-power-ai-data-centers
- name: Dev.to
  url: https://dev.to/delimitter/anthropic-secures-17-gw-of-gas-generators-in-a-34-billion-dollar-deal-23h4
summary: The scarcest thing in AI today isn't electricity or GPUs. It's a delivery
  slot in a factory schedule that's sold out until 2031.
title: Anthropic's $3.4B Turbine Deal Isn't About Power. It's About Time.
trending_theme: Electricity Becomes AI's Main Bottleneck
type: analysis
---

On paper, Anthropic just paid $2,000 per kilowatt for gas generators. What it actually paid for was about six years of waiting it no longer has to do.

The Financial Times reported on November 8 that Anthropic agreed in late September to pay roughly $3.4 billion for 1.7 gigawatts of Caterpillar-built heavy-duty generators. It did that by taking over orders that OnePWR Solutions, an equipment supplier in San Antonio, placed about two years ago and couldn't finance. Anthropic didn't buy OnePWR, and no OnePWR staff moved over. It bought the place in line, plus the engineering and construction work needed to install the machines. Neither company has commented, and Reuters said it couldn't independently verify the report. Piper Sandler, which advised OnePWR, lists a $3.4 billion sell-side deal on its own site: the sale of a "power generation platform to a frontier AI lab." That's about as close to confirmation as these deals usually get.

Most coverage has framed this as "AI companies are buying power now." That's true but not very useful. Here's the sharper version: **the AI bottleneck has moved from silicon to the physical lead time of heavy industrial equipment, and money can no longer shorten that lead time.** You can't simply pay more to get turbines faster. You have to buy someone else's spot.

## The math of a sold-out world

Look at the supply side. Global turbine orders have reportedly passed 100GW, while manufacturing capacity is estimated at 60–70GW a year. Average U.S. delivery times have stretched to six years, and some new orders now land in 2030 or 2031. Grid interconnection queues are about as long. Caterpillar's Power Generation sales rose 30% to $3.421 billion in Q3, mostly from data center demand, and CEO Joe Creed described a record $78 billion backlog. When a 100-year-old industrial company's order book looks like Nvidia's did in 2023, the constraint has changed.

Now measure the deal against Anthropic's own disclosures. Its amended S-1, filed November 2, shows about $895.4 billion in total purchase and lease commitments, with $69.8 billion due in the next twelve months. Q3 revenue was $17.0 billion. Compute and infrastructure spending was about $9.86 billion, or 58% of revenue. The filing also shows Anthropic paying xAI $1.25 billion a month for compute through May 2029. So the turbines cost less than three months of rent paid to a direct competitor, and they're a hard asset Anthropic owns.

That last point is what nobody is talking about. **Anthropic, a company built on rented compute, now pays one of its fiercest rivals more than $15 billion a year for capacity.** Owning generation is about more than keeping the lights on. It's how a frontier lab stops renting its survival from people who want it dead. xAI understood this early: it spent about $2 billion on mobile gas turbines this year and put eight converted GE jet engines, up to 400MW combined, into service in Mississippi. Anthropic is following that playbook, minus the jet engines.

## Three answers to the same problem

Line up the three stories in this week's news and you get three different theories of how to power AI.

**Gas: fast and cheap upfront, expensive forever.** Anthropic's $2,000/kW is the cheapest capex here by a wide margin, and gas generators can be placed almost anywhere there's a pipeline. The catch is that you're buying a lifelong fuel bill and an emissions fight. The Southern Environmental Law Center is already challenging xAI's Mississippi permits. Shakeel Hashim of Transformer called Anthropic's purchase "pretty grim." For the company that markets itself as the safety-first lab, that criticism costs more than it would cost Musk.

**Geothermal: expensive upfront, nearly free to run.** Fervo's contracted revenue jumped from $7.2 billion to $11.9 billion in a single quarter. Its first 100MW plant at Cape Station in Utah is connected to the grid, and a 396MW plant for Google, "Cape Google 400," is due by the end of 2028. Costs fell from $7,000/kW in phase one to $5,500/kW for the Google project. That's still nearly three times what Anthropic paid for gas, but there's no fuel bill. What makes Fervo a good fit for AI is the modular build: each new well generates 15MW gross, and wells are grouped into "GeoBlocks" that have grown from 33MW to 50MW. That's sized to match one data center hall, so power and compute can come online in matching steps.

**China's version: build the grid yourself, right next to the servers.** Envision's Galaxy campus in Ulanqab, Inner Mongolia, delivered its first 120MW in under a year. SemiAnalysis puts the cost at about one-fifth of comparable U.S. projects. The full campus targets 800MW of IT capacity by the end of 2027, roughly the size of Stargate's ~820MW in Abilene. Envision is pairing 420MW of its own wind farms with four-hour batteries to cover more than 60% of the first two phases' 240MW load. Inside, solid-state transformers convert 10kV AC directly to 800V DC at the rack. While U.S. builders compete for Caterpillar slots, a Chinese turbine maker with more than 100GW of installed wind is simply using its own supply chain.

That comparison should worry Washington more than any benchmark chart. The U.S. leads on chips. China leads on the ability to turn steel, copper and wind into running megawatts quickly. Export controls can slow the first. Nothing America has can slow the second.

## The second-order effects

**AI labs are turning into energy traders.** Fervo CEO Tim Latimer explained why Cape Google 400 is grid-connected: Google can sell the power to others if its data center isn't ready. "Neither party is waiting on the other." The hyperscaler holds a tradable energy position, not a single-use supply. Alphabet buying the energy developer Intersect in late 2025 points the same way. In five years, expect at least one frontier lab to report meaningful revenue from selling electricity.

**Power hardware becomes a strategic sector.** SpaceX now makes its own turbine blades to cut 18 months off generator delays. Companies that make transformers, switchgear and 800V DC power systems are getting the kind of pricing power that used to belong only to TSMC.

**The moat moves.** If the best frontier models stay within a few months of each other, the lab that wins is the one that can switch on the next gigawatt first. Model weights leak and get distilled. A 1.7GW queue position doesn't.

## The bear case

There's a fair argument that Anthropic is buying at the top. Gas turbines last 25–30 years. If inference efficiency keeps improving the way it has, with per-token costs falling by an order of magnitude every year or two, today's power panic could become 2029's stranded assets. Labs that signed take-or-pay compute contracts in a frenzy could find themselves holding generators sized for demand that never arrived. Fervo is also still losing money ($43.7 million operating loss last quarter, though it has $1.9 billion in cash), and even with subsidies its power costs about twice what natural gas does.

I don't buy the bear case for the next three years. Efficiency gains have so far been eaten by usage growth every time: cheaper tokens mean more agents, longer contexts and more reasoning loops. Jevons wins this round. But the risk is real for whoever holds the last turbine when the cycle turns, and it won't be the companies buying today.

## What to Watch

1. **Another frontier lab announces owned generation of 1GW or more by mid-2027.** OpenAI is the most likely, given Stargate's scale. Meta comes second.
2. **The resale market for turbine delivery slots goes public.** The OnePWR deal is an early example. Expect brokers and specialist funds trading slots, with prices per kW climbing well above $2,000.
3. **Anthropic's emissions story becomes an IPO issue.** Expect explicit carbon-offset or geothermal/nuclear pairing commitments in a later S-1 amendment or roadshow, because the "safety lab" brand can't carry 1.7GW of unmitigated gas.
4. **Fervo crosses $20 billion in contracted revenue within 12 months** and announces a second Cape-scale site, as Cape Station's revised 8.4GW resource estimate attracts more buyers.
5. **Galaxy hits its 2027 target on time.** If it does, "one-fifth the cost" becomes the most uncomfortable number in U.S. AI policy, and 800V DC power architecture becomes the industry default by 2028.

The GPU shortage made Nvidia the world's most valuable company. The power shortage is going to produce its own winners, and many of them will look a lot more like Caterpillar.