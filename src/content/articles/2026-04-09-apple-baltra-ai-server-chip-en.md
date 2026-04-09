---
title: "Apple's Secret AI Server Chip Gets a Glass Upgrade — and Samsung Is Supplying It"
summary: "Apple is advancing development of its first custom AI server chip, codenamed Baltra, while Samsung Electro-Mechanics has begun supplying experimental glass substrate samples for packaging. The collaboration marks Apple as the last major tech hyperscaler to build its own AI silicon, while the glass substrate technology represents a potential generational leap in chip packaging that could reshape AI hardware economics in the 2027–2028 timeframe."
category: "hardware"
publishedAt: 2026-04-09
lang: "en"
featured: false
trending: true
sources:
  - name: "The Elec"
    url: "https://www.thelec.net/news/articleView.html?idxno=6400"
  - name: "Sammy Fans"
    url: "https://www.sammyfans.com/2026/04/08/apple-taps-samsung-for-breakthrough-ai-chip/"
  - name: "SammyGuru"
    url: "https://sammyguru.com/samsung-helps-apple-make-ai-chips-with-glass-substrates/"
  - name: "TrendForce"
    url: "https://www.trendforce.com/news/2025/12/17/news-apple-reportedly-pushes-in-house-ai-chip-eyes-2027-server-deployment-foxconn-to-gain/"
  - name: "Digitimes"
    url: "https://www.digitimes.com/news/a20260408PD220/demand-substrate-capacity-2026-ic-substrate.html"
tags:
  - "Apple"
  - "Baltra"
  - "AI chip"
  - "Samsung"
  - "glass substrate"
  - "Broadcom"
  - "TSMC"
  - "hardware"
relatedSlugs:
  - "2026-04-05-nvidia-marvell-nvlink-fusion-en"
  - "2026-04-05-cognichip-ai-chip-design-en"
  - "2026-04-04-amd-mi300x-enterprise-en"
---

Apple has spent the past several years making M-series chips that have reshaped the laptop and desktop markets. Its next challenge — and arguably its most strategically consequential hardware project — is building a chip that can power AI inference at the scale of iCloud, Siri, and Apple Intelligence for a billion-plus users without paying Nvidia for every computation. New reporting this week reveals that Apple's effort to cross that line has accelerated, with Samsung Electro-Mechanics now supplying glass substrate samples for what could become the packaging foundation of Apple's first custom AI server chip.

The chip, codenamed Baltra, has been in development for roughly two years. It is being co-designed with Broadcom — whose networking expertise covers the interconnect fabric critical for AI server deployments — and is targeted for manufacture at TSMC's N3P process node, the same advanced 3-nanometer generation used by Nvidia and OpenAI's first custom silicon. A team of Apple engineers based in Israel, in the company's R&D center northeast of Tel Aviv, is leading the design effort. Servers using Baltra are expected to begin deployment in 2027.

## Why Glass Substrates Matter

The Samsung Electro-Mechanics substrate story is technically distinct from, but strategically intertwined with, the Baltra chip itself. Understanding why Apple is evaluating glass substrates requires a brief detour into chip packaging physics.

Every advanced chip ships inside a package — a substrate that connects the silicon die to the circuit board and distributes power, signal, and heat. For decades, the industry has used organic substrates made from resins and glass fiber. These are cheap and mature, but they have a critical weakness: they expand and contract with temperature, and as chips grow larger and denser, the mismatch between the silicon die and the organic substrate causes warping. Warped packages fail. And AI chips — among the largest, densest, and hottest semiconductors ever made — are pushing organic substrate limits hard.

Glass substrates solve this by replacing the organic core with glass, which has a thermal expansion coefficient roughly 30 times smaller than organic materials. This allows finer circuit patterns on the substrate (enabling denser, shorter signal paths), higher package flatness (reducing failure rates), and better high-frequency signal integrity (critical for the memory bandwidth AI workloads demand). Intel identified glass substrates as a key roadmap technology for its advanced packaging strategy as early as 2023; Samsung and SK hynix have been racing to develop commercial supply since.

Samsung Electro-Mechanics is now running a pilot glass substrate production line at its Sejong facility in South Korea. Mass production is not targeted until after 2027. But the supply of experimental samples to Apple is a meaningful signal: it suggests Apple is evaluating glass substrates not just as a commodity material to buy, but as a potential design-in for future AI chip packages — either for Baltra or for whatever follows it.

Industry observers see the Samsung-Apple engagement serving two purposes simultaneously. In the near term, Apple is almost certainly evaluating packaging material characteristics as an end customer of Broadcom-designed platforms. In the longer term, it may be laying groundwork to design its own server chip packaging using glass substrates when the technology matures for mass production. The distinction matters: the former is procurement due diligence; the latter is a bet on Apple exerting the same vertical integration over AI server packaging that it has historically exerted over device chips.

## The Last Hyperscaler to Build Its Own

The strategic backdrop for Baltra is straightforward: Apple is the last of the major hyperscalers to develop custom AI inference silicon, and the competitive gap has become uncomfortable.

Amazon's Trainium and Inferentia chips have been in production AWS deployments for years, enabling aggressive inference cost reductions. Google's TPUs are now in their fifth generation and are deeply integrated into Gemini's infrastructure. Microsoft has deployed its Maia AI accelerator across Azure clusters. Meta's MTIA chip is in active deployment for ranking and recommendation inference. Even startups like Cerebras and Groq have carved meaningful positions in specialized inference hardware.

Apple's AI infrastructure currently runs primarily on Nvidia A100 and H100 GPUs for the compute-intensive tasks, supplemented by the M-series chips in its Private Cloud Compute architecture. That architecture is technically impressive — Apple's Private Cloud Compute, which routes sensitive Siri and Apple Intelligence requests to on-demand cloud instances using M-series chips, was a notable 2024 innovation — but it was designed for privacy guarantees, not raw inference throughput economics. As Apple Intelligence expands in scope and the model calls grow more compute-intensive with each iOS release, the cost of running third-party silicon becomes more significant.

Baltra addresses this at the infrastructure layer. By co-designing the chip with Broadcom, Apple gains control over the networking architecture that connects chips in a multi-chip server deployment — the bottleneck for large language model inference, where data movement between chips often limits performance more than raw compute.

## What This Means for the AI Hardware Market

Apple entering the custom AI server chip market will have ripple effects across the supply chain. TSMC, which manufactures Apple's chips almost exclusively, will see additional N3P demand from a major customer. Broadcom's already-strong position as the custom AI chip co-designer of choice — it is working with Google, Meta, OpenAI, and now Apple — becomes further entrenched. Samsung Electro-Mechanics, if its glass substrate technology is adopted, gains a customer that could accelerate the commercial viability of a technology the company has been investing in for years.

For Nvidia, Apple's move is not an immediate threat — Baltra is internal infrastructure, not a product sold to Nvidia's customers. But it represents one more large-scale inference workload migrating away from Nvidia silicon as hyperscalers bring AI compute in-house. The trend is structural: every major cloud provider is now on a path toward custom AI silicon, and Nvidia's share of the inference market will be contested from an increasing number of directions.

The Baltra program is, in Apple's characteristically quiet way, one of the most consequential bets the company is making. If it succeeds — and Apple's silicon track record over the past decade makes skepticism difficult to sustain — it will mean that by the time Apple Intelligence reaches its full intended scope, the compute infrastructure underpinning it will be as proprietary as the device it runs on.
