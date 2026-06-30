---
title: "SpaceX's Historic $75B IPO Bets on Space-Based AI Compute With AI1 Orbital Data Centers"
summary: "SpaceX completed the world's largest-ever IPO on June 12, raising $75 billion at a $2.1 trillion market cap under Nasdaq ticker SPCX. The company simultaneously unveiled AI1, a 70-meter orbital compute satellite targeting 1 GW of space-based AI capacity by late 2027, with Google already contracted to pay $920 million per month for access."
category: "hardware"
publishedAt: 2026-06-30
lang: "en"
featured: true
trending: true
sources:
  - name: "CNBC - SpaceX IPO SPCX"
    url: "https://www.cnbc.com/2026/06/12/spacex-ipo-spcx-live-updates.html"
  - name: "Tom's Hardware - SpaceX AI1 Details"
    url: "https://www.tomshardware.com/tech-industry/spacex-details-its-ai1-compute-satellite"
  - name: "Quartz - SpaceX AI1 Satellite Design"
    url: "https://qz.com/spacex-ai1-satellite-orbital-data-center-ipo-061026"
  - name: "Data Center Dynamics - SpaceX Orbital Data Centers"
    url: "https://www.datacenterdynamics.com/en/news/spacex-ipo-musks-firm-set-to-launch-first-orbital-data-center-ai1-satellites-in-2027-will-put-compute-on-starlink-craft/"
tags:
  - "SpaceX"
  - "IPO"
  - "AI compute"
  - "orbital data centers"
  - "Elon Musk"
  - "hardware"
  - "cloud computing"
relatedSlugs:
  - "2026-06-29-ai-chip-stock-selloff-june-2026-en"
  - "2026-06-29-openai-jalapeno-broadcom-inference-chip-en"
  - "2026-06-26-openai-jalapeno-broadcom-inference-chip-en"
---

On June 12, 2026, SpaceX priced its initial public offering at $135 per share on Nasdaq — and by the time trading closed that afternoon, the stock sat at $160.95. The 19% single-day pop gave the company a market capitalization of roughly $2.1 trillion, making it the most valuable public debut in history and eclipsing Saudi Aramco's 2019 record by a comfortable margin. The $75 billion raised in the offering itself set another record. But the number that rattled the technology industry most wasn't on the stock ticker — it was the wingspan of a satellite.

## The AI1 Satellite: Compute That Orbits

Two days before the IPO priced, SpaceX CEO Elon Musk posted a video to X unveiling AI1, the company's first orbital artificial intelligence compute platform. The satellite is extraordinary in its ambitions: at 70 meters tip-to-tip — wider than a Boeing 747 — and 20 meters tall when fully deployed, it is the largest compute-focused spacecraft ever publicly disclosed.

The specs are equally dramatic. AI1 is designed to sustain 120 kilowatts of average compute power and burst to 150 kW at peak, powered by solar arrays rated at 150 kW total at roughly 250 watts per square meter of panel area. In the vacuum of orbit, there is no air or water for cooling, so SpaceX engineered a deployable liquid radiator spanning 110 square meters of panel area, capable of shedding heat at approximately 1,400 watts per square meter — a density that SpaceX claims significantly outperforms terrestrial cooling alternatives at this power level.

The payload itself is modular. SpaceX designed AI1 around a swappable compute cartridge, meaning successive generations of GPU or custom accelerator silicon can slot into the same satellite body without redesigning the spacecraft. COO Gwynne Shotwell described the architecture as "upgradeable infrastructure, not disposable hardware." Each Starship launch, she noted, can carry between 30 and 50 AI1 units to orbit — a cadence that makes the economics of large-scale deployment plausible in ways that no prior launch vehicle could.

## The Road to 1 Gigawatt in Space

SpaceX's disclosed roadmap calls for two AI1 prototype satellites to launch in early 2027, followed by a ramp targeting approximately 1 GW of cumulative orbital AI compute capacity by the end of 2027. The company has told the FCC it intends to eventually deploy up to one million such satellites — a constellation that would more than double every object currently in orbit combined.

Manufacturing at that scale requires infrastructure that does not yet exist. SpaceX is building what it calls Gigasat, a campus occupying roughly 1,000 acres in Bastrop County, Texas, with eventual plans for up to 11 million square feet of production floor. The facility integrates solar cell manufacturing, circuit board assembly, satellite integration, and semiconductor packaging under one roof — a vertical supply chain reminiscent of the approach that made Tesla's Gigafactory competitive.

Whether orbital compute can beat terrestrial costs remains genuinely unresolved. Electricity for ground-based data centers runs between $30 and $60 per megawatt-hour; space-based power from sunlight is effectively free once the satellite is built, but capital costs per kilowatt of orbital capacity are currently estimated to be far higher than equivalent ground installations. SpaceX has not publicly disclosed unit economics or pricing for its AI compute constellation.

## Customers Are Already Signed

What SpaceX has disclosed is that customers exist and contracts are signed. Google agreed to pay SpaceX $920 million per month for orbital compute access from October 2026 through June 2029 — a 32-month arrangement worth roughly $29 billion that provides Google access to the equivalent of approximately 110,000 NVIDIA GPUs, along with supporting memory and networking hardware. Anthropic, the AI safety company, is also in discussions to route inference workloads through SpaceX's infrastructure.

The Google deal in particular has drawn attention for what it implies about the trajectory of AI compute demand. Google already operates some of the largest ground-based data centers in the world and has invested heavily in its own custom TPU silicon. The decision to additionally contract $29 billion worth of orbital compute suggests that hyperscaler demand is outrunning terrestrial supply chains by a margin that even the world's most capital-intensive infrastructure companies cannot resolve on their own.

## What the IPO Tells Us About AI Infrastructure

SpaceX's IPO was constructed around multiple narratives — Starlink's satellite internet dominance, Starship's cargo capabilities, the Mars colonization mission — but the financial markets were primarily pricing in an AI infrastructure thesis. The S-1 filing disclosed that SpaceX has earmarked a significant portion of IPO proceeds for Gigasat construction and AI1 production ramp, framing orbital compute as a long-cycle infrastructure bet analogous to early fiber-optic cable deployment.

Investor appetite validated the framing. SPCX opened to retail trading with a book that was reportedly oversubscribed by more than 10x at the $135 offering price. Marc Andreessen, speaking at a Bloomberg conference days before pricing, called Starship "the key enabling technology for AI data centers in orbit," arguing that SpaceX's launch cost advantage — roughly 10-20x cheaper per kilogram to orbit than any existing competitor — makes orbital compute viable at scale in ways that were "simply not possible before 2025."

The market is implicitly betting he is right. At $2.1 trillion, SpaceX is priced as if orbital AI compute is not a speculative curiosity but an inevitable infrastructure layer — one that happens to be regulated by physics rather than permitting boards, powered by sunlight rather than utility agreements, and cooled by the vacuum of space rather than chillers that consume 30% of a data center's energy budget.

## Skeptics and Open Questions

Not everyone agrees. CNBC ran an analysis the week of the IPO asking "Do AI data centers in space actually make economic sense?" and found expert opinion sharply divided. Critics point out that the latency of signals traveling from orbit adds milliseconds that matter for real-time AI inference applications; that manufacturing and launch costs per kilowatt of orbital compute remain orders of magnitude higher than terrestrial equivalents at current scales; and that a single solar flare or Kessler cascade event could destroy significant portions of a space-based compute constellation with no on-orbit repair capability.

SpaceX's answer to these objections is essentially: the same arguments were made about satellite internet before Starlink demonstrated that reusable launch economics could change the equation entirely. That argument persuaded enough institutional investors to make SPCX the most talked-about public offering of 2026. Whether AI1 vindicates the thesis will become apparent when the first prototype satellites reach orbit sometime next year.

For now, the space industry has a new vertical: orbital AI compute. And it arrived via the largest IPO in history.
