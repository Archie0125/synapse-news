---
title: "SpaceX Unveils AI1 Satellite: The World's First Orbital Data Center, Wider Than a Boeing 747"
summary: "SpaceX revealed its AI1 orbital AI compute satellite spanning 70 meters tip-to-tip and delivering 120 kW of sustained compute from low Earth orbit. The announcement, timed to the company's landmark IPO roadshow, targets one gigawatt of orbital AI compute by late 2027 and could fundamentally reshape where AI inference happens."
category: "hardware"
publishedAt: 2026-06-20
lang: "en"
featured: true
trending: false
sources:
  - name: "TechSpot"
    url: "https://www.techspot.com/news/112710-elon-musk-reveals-spacex-230-foot-wide-orbital.html"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/spacex-details-its-ai1-compute-satellite"
  - name: "KBTX"
    url: "https://www.kbtx.com/2026/06/10/spacex-reveals-plans-orbital-data-centers-terafab-ahead-historic-ipo/"
  - name: "MLQ AI News"
    url: "https://mlq.ai/news/spacex-unveils-ai1-orbital-data-center-satellite-targets-1-gw-space-compute-by-late-2027/"
tags:
  - "SpaceX"
  - "satellite"
  - "orbital-compute"
  - "AI-infrastructure"
  - "Elon-Musk"
  - "hardware"
  - "IPO"
  - "data-center"
relatedSlugs:
  - "2026-06-20-ferc-ai-data-center-power-fast-track-en"
  - "2026-06-17-naver-nvidia-dsx-gigawatt-sovereign-ai-korea-en"
---

When Elon Musk posted a rendering of the AI1 satellite to X on June 9, the image stopped engineers in their tracks: a spacecraft wider than a commercial jetliner, its twin solar panels fanning out 70 meters tip-to-tip above a sleek central bus, designed not to beam internet signals but to run AI workloads from low Earth orbit.

The AI1 is SpaceX's first-generation orbital data center satellite — and it may be the most consequential hardware announcement the company has made since Starship.

## An Orbital Data Center in Numbers

The AI1's specifications read like a thought experiment made real. The spacecraft stands 20 meters tall when deployed and spans 229.6 feet tip-to-tip, making it wider than a Boeing 747-8. Its twin solar arrays generate enough power to sustain 120 kilowatts of average compute, peaking at 150 kW during burst processing windows — a power density of approximately 70 kW per ton of spacecraft mass.

Keeping that much compute cool in the vacuum of space required an entirely new thermal architecture. SpaceX engineered 110 square meters of deployable liquid radiator panels with redundant pumping loops and micrometeoroid shielding, using ammonia as the likely coolant. The panels radiate waste heat at a density of 1,400 watts per square meter, nearly eight times the efficiency of Earth-bound air cooling in a comparable data center footprint.

The satellite operates at 600 kilometers above sea level in low Earth orbit, a sweet spot that provides the low-latency connectivity of Starlink's existing constellation while keeping satellites within range of rapid resupply and servicing.

Perhaps the most consequential engineering choice is the interchangeable compute payload. The AI1's central bus can accept different chip packages — initially Nvidia hardware — without redesigning the satellite. As AI accelerator generations turn over every two to three years, SpaceX can swap payloads rather than retire entire satellites, dramatically reducing the effective cost-per-compute-generation.

SpaceX engineer Ian Dahl characterized the AI1 as simpler than the Starlink V3 broadband satellites, which carry phased-array antennas and inter-satellite laser links far more complex than a standardized compute module. "The AI satellite is much simpler than a Starlink satellite," Musk echoed in a post to X. The company is leveraging a decade of high-volume satellite manufacturing to build AI infrastructure at costs that terrestrial hyperscalers cannot match on a per-watt basis.

## Terafab and the Gigasat Factory

Behind the AI1 hardware is an even more ambitious supply chain buildout.

SpaceX has disclosed Terafab, a semiconductor fabrication plan jointly developed with Tesla, targeting radiation-hardened chips specifically designed for the orbital compute environment. CFO Bret Johnsen confirmed that longer-term AI1 variants will rely on Terafab silicon rather than commercial Nvidia hardware. SpaceX has projected approximately $55 billion in investment to build out the Terafab initiative, though the timeline extends well into the 2030s.

Closer to operational reality is Gigasat, a planned manufacturing complex on approximately 1,000 acres in Bastrop County, Texas. At full buildout, the facility could encompass up to 11 million square feet of manufacturing space — larger than any existing semiconductor fab in the United States. A semiconductor packaging operation at the Bastrop campus began equipment installation in April 2026 and is targeting production readiness by end of year.

SpaceX has set an audacious scale target: one gigawatt of operational orbital AI compute by late 2027, scaling toward 100 gigawatts within three-and-a-half years. Even the near-term milestone would represent a meaningful fraction of the AI compute capacity that major hyperscalers currently operate on the ground — all of it powered by sunlight rather than strained power grids.

## The IPO Connection

The AI1 reveal was not accidental timing. SpaceX priced its IPO during the week of June 11 under the ticker SPCX on Nasdaq, targeting a valuation of approximately $1.75 trillion and raising around $75 billion — making it one of the largest public offerings in history. The IPO prospectus listed AI1 and orbital compute as a core growth pillar distinct from the Starlink satellite internet business, which already runs at meaningful profit margins.

The company's 2025 revenue of $18.7 billion came primarily from launch services and Starlink subscriptions, alongside a $4.94 billion net loss reflecting heavy reinvestment. But SpaceX is framing the orbital compute opportunity as a new category that leverages the same rockets, satellite manufacturing capabilities, and constellation management infrastructure that Starlink requires — turning sunk costs into scalable margin on a second revenue line.

## Why Orbit?

The business logic for orbital data centers rests on a set of structural advantages that on-ground alternatives cannot replicate.

Power is the most obvious. Terrestrial AI data centers are now consuming electricity at rates that strain regional grids and require years of permitting and construction for new capacity. The US Federal Energy Regulatory Commission (FERC) this week issued emergency rules to fast-track data center grid connections, a tacit acknowledgment that the permitting pipeline cannot keep pace with demand. Orbital solar is functionally unlimited: a satellite in low Earth orbit receives sunlight roughly 60 percent of its orbit with no atmospheric attenuation, no land acquisition, and no transmission losses from distant power plants.

Latency matters too, but differently than one might expect. Most AI inference workloads are not ultra-low latency; they involve sending a large prompt and waiting several hundred milliseconds for a response. At 600 km altitude, round-trip latency from the ground to an AI1 satellite and back is roughly 4–8 milliseconds over Starlink's existing laser inter-satellite links — comparable to a well-provisioned hyperscale edge node.

The geopolitical dimension may prove equally important. An AI compute node in orbit sits outside the jurisdiction of any national government, a fact with significant implications for customers subject to export controls or operating across multiple regulatory regimes. This angle became more salient this month when the US government's export ban on Anthropic's Fable 5 and Mythos 5 models left international customers scrambling for alternatives. SpaceX, whose own relationship with the federal government is complex, has not explicitly addressed this use case — but analysts note that orbital compute sidesteps the geographic enforcement mechanisms on which traditional export controls rely.

## The Hard Problems

The skeptics have legitimate concerns. Microsoft's Project Natick, an experiment in underwater data centers, demonstrated that novel deployment environments create maintenance challenges that erode cost advantages over time. Radiation in low Earth orbit degrades semiconductors at measurable rates; the interchangeable payload architecture is partly a response to this reality. If chip lifetimes in orbit prove shorter than ground-based alternatives, the economics of frequent resupply could dwarf the power savings.

Bandwidth is a second constraint. Downloading the output of 120 kW of continuous AI inference requires massive downlink capacity. SpaceX has not published throughput specifications for the AI1's communication links, and at current Starlink capacity the constellation would saturate quickly if orbital compute scales as planned. The company will need to integrate dedicated high-throughput downlinks — a capability that adds cost and complexity not reflected in the satellite's current design specs.

The regulatory environment for mega-constellations is also in flux. Coordination between AI1 deployments, existing Starlink operations, and other operators in the increasingly crowded 550-600 km shell will require ongoing engagement with the ITU and national regulators.

## The Bigger Picture

Whatever the operational challenges, SpaceX's entry into orbital AI compute changes the conversation about where AI infrastructure can go. For a decade, the debate over AI data centers has been a fight over power purchase agreements, cooling water rights, and GPU allocations — all terrestrial concerns measured in megawatts and zoning approvals. The AI1 reframes the question at a planetary scale.

Prototype AI1 units are scheduled for launch in early 2027, with commercial deployment and volume production following through that year. If SpaceX's manufacturing cadence even approaches what it achieved with Starlink V2 Mini satellites — more than a hundred per Falcon 9 launch — the orbital compute buildout could scale faster than any comparable ground-based infrastructure campaign in history.

The sky, it turns out, is not the limit. It is the address.
