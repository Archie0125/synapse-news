---
title: "Decart AI Raises $300M at $4B Valuation to Build Real-Time World Models for Physical AI"
summary: "Israeli AI startup Decart has raised $300 million in a Series B led by Radical Ventures with participation from Nvidia, Adobe Ventures, and Toyota Ventures, valuing the company at $4 billion. The funding will accelerate Decart's three product lines: DOS, an ultra-fast inference and training stack processing 1,600+ tokens per second; Lucy, a real-time world model for immersive experiences; and Oasis, a world model for physical AI systems and robotics."
category: "ai-ml"
publishedAt: 2026-05-25
lang: "en"
featured: false
trending: true
sources:
  - name: "Decart AI"
    url: "https://decart.ai/publications/decart-raises-300m-tech-leaders-back-the-company-as-both-customers-and-investors"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/05/18/decart-raises-300m-ai-optimization-software-world-models/"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/decart-300-million-radical-ventures-world-models"
  - name: "Globes"
    url: "https://en.globes.co.il/en/article-decart-raises-300m-including-nvidia-investment-report-1001543260"
tags:
  - "decart"
  - "world-models"
  - "physical-ai"
  - "robotics"
  - "nvidia"
  - "inference"
  - "radical-ventures"
  - "israel-tech"
relatedSlugs:
  - "2026-05-19-mind-robotics-400m-rivian-physical-ai-manufacturing-en"
  - "2026-05-09-genesis-ai-gene-265-dexterous-robot-en"
  - "2026-05-20-fractile-220m-series-b-ai-inference-chips-en"
---

When Andrej Karpathy writes a personal check into an AI startup, people pay attention. The OpenAI co-founder and former Tesla AI director is among the angel investors in Decart's $300 million Series B, a round that values the Israeli AI startup at $4 billion and places it at the center of what may be the most strategically significant frontier in AI right now: world models for physical systems.

Radical Ventures led the round, with Nvidia participating alongside Adobe Ventures, Toyota Ventures, Atreides Management, Valor Equity Partners, and eBay Ventures. Returning backers Sequoia Capital, Benchmark, and Zeev Ventures also participated. The round brings Decart's total funding to over $450 million.

## What Decart Actually Builds

Decart has organized its products into three distinct but interconnected lines, each attacking a different constraint in AI's expansion into the physical world.

**DOS (Decart Operating System)**: The company's inference and training infrastructure stack. DOS 2.0 enables AI agents to process over 1,600 tokens per second—eight times the industry average—through a combination of optimized kernel-level compute management and custom memory access patterns. The system is hardware-agnostic and has been deployed across hundreds of thousands of GPUs for clients including Google, Microsoft, and xAI. For AI labs spending billions on compute, a system that extracts eight times more throughput from existing hardware represents direct cost reduction without any change to the underlying model.

**Lucy**: Decart's world model for immersive experiences. Lucy takes a video stream as input and modifies depicted objects in real time—enabling applications like virtual try-on (a shopper holds up clothing to a camera and sees it rendered on their body), interactive interior design visualization, and live product customization. The model processes high-definition video at up to 100 frames per second, fast enough for real-time consumer applications. Decart has signed enterprise partnerships with retail, fashion, and e-commerce companies to deploy Lucy in production environments.

**Oasis**: Described by Decart as "the world's first world model designed for Physical AI," Oasis simulates physical environments in real time. The model can generate photorealistic renders of environments, model the physics of object interactions, and serve as a training substrate for robotic systems that need to develop motor skills and spatial reasoning. Oasis 3, the next version, is slated for launch soon and is expected to significantly improve spatial reasoning accuracy and simulation fidelity.

## Why World Models Matter Now

The term "world model" describes an AI system that maintains an internal representation of a physical or virtual environment—one that allows it to predict how that environment will change in response to actions, without needing to observe each step in real time. In robotics, this capability is the difference between a system that must constantly query sensors and cameras for every decision, and one that can plan ahead and reason about consequences.

Decart's bet is that the rapid development of physical AI—autonomous vehicles, humanoid robots, warehouse automation, and surgical systems—is creating massive demand for the kind of real-time simulation infrastructure that lets these systems train and operate safely and efficiently. The physical AI market has seen over $5 billion in venture investment in the past twelve months alone, with companies like Figure, 1X, Apptronik, and Physical Intelligence attracting major funding.

The computational bottleneck in physical AI is not the model architecture—it is the ability to generate sufficiently realistic and physically accurate training environments fast enough to matter. A humanoid robot needs to complete millions of simulated trials before it can safely fold laundry or assemble electronics; if those simulations are slow, expensive, or physically inaccurate, training becomes the binding constraint.

Decart's DOS stack addresses the speed and cost constraint directly. Oasis addresses the realism and physical accuracy constraint. The combination positions Decart not just as a beneficiary of the physical AI boom but as infrastructure that other physical AI companies depend on.

## Strategic Significance of the Investor Roster

The composition of Decart's investor base is unusually revealing. Nvidia's participation is particularly notable: the GPU maker rarely invests in software companies that could be described as optimizing around its hardware. That Nvidia backed DOS—a system that dramatically improves GPU utilization—suggests the company sees DOS as complementary infrastructure that makes its GPUs more attractive to deploy rather than a threat to its business.

Toyota Ventures' presence is equally telling. Toyota has been one of the most active automotive investors in physical AI infrastructure, and its participation in Oasis signals that established automotive OEMs are beginning to position themselves as anchor customers for simulation infrastructure, not just end users of autonomous driving systems.

Adobe's involvement points toward Lucy's enterprise imaging and visualization applications—a natural adjacency to Adobe's creative cloud customer base, where virtual product visualization and real-time rendering have significant commercial value.

Karpathy's angel investment carries specific credibility: he spent years at OpenAI and Tesla building exactly the kinds of systems Decart is now commercializing. His conviction that world models represent a genuine technical path to scalable physical AI carries more signal than most institutional positions.

## The Israeli AI Ecosystem's Growing Moment

Decart is one of a cluster of Israeli AI startups that have raised major rounds in 2025-2026, reflecting both the depth of technical talent in Israel's AI research community and the increasing willingness of tier-1 Silicon Valley venture funds to back companies headquartered outside the Bay Area. Radical Ventures—the Toronto-based firm that led this round—has become one of the most active investors in frontier AI outside of the traditional US-centric venture ecosystem.

The company was founded by Uri Goldfeld and Yoav Shoham-like figures in Israel's AI research community, and maintains research operations in Tel Aviv while scaling commercial operations in the U.S.

## What the Funding Enables

Decart plans to deploy the $300 million across three priorities: scaling the DOS inference infrastructure to support substantially larger GPU deployments for enterprise clients, launching Oasis 3 and expanding the physical AI simulation product line, and growing the commercial team to convert the substantial inbound demand generated by Oasis's capabilities into enterprise contracts.

The company is also reportedly in discussions with multiple automotive OEMs and humanoid robotics companies about becoming the simulation substrate for their physical AI training programs—deals that would represent significant multi-year revenue commitments if closed.

At $4 billion, Decart is priced as a company whose technology is already deployed at scale—which it is, with DOS running on hundreds of thousands of GPUs. The question the market is implicitly answering is whether Oasis can become as critical to physical AI development as CUDA became to GPU computing: the infrastructure layer without which everything else is more expensive and slower.

The investor roster, led by Nvidia and including Karpathy, suggests the smart money thinks the answer is yes.
