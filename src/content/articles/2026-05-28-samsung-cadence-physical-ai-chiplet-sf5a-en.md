---
title: "Samsung and Cadence Team Up on Physical AI Chiplet Platform Targeting Robotics and Automotive"
summary: "Samsung Foundry and Cadence Design Systems unveiled a joint Physical AI chiplet platform at CadenceLive 2026, built on Samsung's 5nm SF5A process. The pre-verified modular design targets real-time camera processing, AI radar, and autonomous systems, with tape-out planned for early 2027 and volume production in the second half of that year."
category: "hardware"
publishedAt: 2026-05-28
lang: "en"
featured: false
trending: false
sources:
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/317234/20260527/samsung-foundry-chiplet-platform-eyes-2027-production-robotics-automotive-ai.htm"
  - name: "Samsung Semiconductor"
    url: "https://semiconductor.samsung.com/news-events/tech-blog/samsung-foundry-and-cadence-accelerating-chiplet-solutions-for-physical-ai/"
  - name: "New Electronics"
    url: "https://www.newelectronics.co.uk/content/news/samsung-foundry-and-cadence-advance-chiplet-platform-for-physical-ai-applications"
tags:
  - "samsung"
  - "cadence"
  - "chiplet"
  - "physical-ai"
  - "robotics"
  - "automotive"
relatedSlugs:
  - "2026-05-27-nvidia-vera-rubin-q3-launch-5x-blackwell-en"
  - "2026-05-27-china-nine-domestic-ai-chips-anke-certification-en"
  - "2026-05-25-amazon-trainium-20b-chip-business-225b-backlog-en"
---

Samsung Foundry and Cadence Design Systems announced a joint Physical AI chiplet platform at CadenceLive 2026, marking the clearest signal yet that the semiconductor industry sees physical AI — the intelligence embedded in robots, autonomous vehicles, drones, and manufacturing systems — as a sufficiently distinct compute category to warrant purpose-built silicon architecture rather than adaptation of existing data center chips.

The platform is built on Samsung's SF5A 5-nanometer process technology and uses a modular chiplet design approach: a set of pre-verified, interoperable silicon tiles that can be combined to meet the specific compute, power, and latency requirements of different physical AI applications. A robotics arm and a self-driving car sensor system have very different requirements; a chiplet architecture allows both to share validated silicon IP while each product custom-configures its combination of compute, memory, and I/O elements.

## What Physical AI Demands

The compute requirements for physical AI differ fundamentally from the requirements that drove data center AI chip design over the past decade. Large language models and transformer-based systems are primarily matrix multiplication workloads: high parallelism, high memory bandwidth, and tolerance for latency measured in milliseconds to seconds. Physical AI workloads are characterized by the opposite priorities.

A camera processing system in a manufacturing robot needs to analyze frames in real time — under 10 milliseconds from sensor input to actuator response. An automotive radar system needs to detect objects at highway speeds with deterministic latency guarantees, not average latency. A warehouse sorting robot needs to process sensor fusion from multiple modalities simultaneously while operating within a tight power envelope that allows battery-powered continuous operation.

These are real-time, power-constrained, latency-deterministic workloads. They have more in common with automotive-grade embedded processors from the pre-AI era than they do with the Nvidia H100s running in data centers. The physical AI chiplet platform that Samsung and Cadence are building addresses exactly this gap between general-purpose AI silicon and the embedded systems world.

## The Chiplet Architecture Advantage

Chiplet-based design has become the dominant architectural approach for advanced semiconductor products over the past five years, primarily driven by the limitation of single-die scaling as Moore's Law has slowed. AMD, Intel, Apple, and TSMC have all built chiplet ecosystems for CPUs and GPUs. The Samsung-Cadence platform extends this approach specifically to physical AI edge compute.

The pre-verified nature of the chiplets is commercially critical. Verifying that silicon IP meets functional, power, and timing specifications is one of the most time-consuming and expensive phases of chip design. A chiplet platform with pre-verified IP blocks allows a robotics startup designing its first custom silicon to begin from a validated foundation rather than from scratch, potentially cutting years off the development timeline.

Individual chiplets can be optimized for specific voltage and frequency requirements — a capability particularly valuable for battery-powered edge devices, where different functional blocks may need to operate at different power states simultaneously. The platform also targets yield improvement: smaller individual dies have higher manufacturing yields than large monolithic chips, reducing per-unit cost as volumes scale.

## Target Applications and Market Context

The first-wave target applications for the platform are real-time camera processing, AI-enhanced radar in autonomous vehicles, smart manufacturing equipment, and sensor-driven robotic systems. These categories share a common characteristic: they require high compute density in confined physical environments where power and thermal constraints are tight, and where failure modes have physical consequences rather than just service degradation.

The automotive application is arguably the largest near-term market. Advanced Driver Assistance Systems (ADAS) and full autonomous driving require continuous processing of camera, radar, and lidar inputs at speeds where data center AI inference would introduce unacceptable latency. Current automotive AI chips from companies like Mobileye, Qualcomm, and NVIDIA's Drive platform are designed for this purpose, but the Samsung-Cadence platform positions itself as a more flexible foundation for second and third-generation automotive AI systems — one that chip designers can configure for specific safety and performance profiles rather than buying a fixed solution.

The manufacturing robotics application is growing rapidly. With automation investment accelerating across industrial production — particularly as supply chain redundancy strategies have incentivized near-shoring and on-shoring of manufacturing — the demand for capable, power-efficient perception and control chips for factory robots is substantial. Physical AI chiplets that meet ISO 26262 and IEC 61508 functional safety standards (the automotive and industrial safety certification frameworks respectively) represent a significant market opening.

## Timeline and Competitive Context

Samsung and Cadence are targeting a prototype tape-out in early 2027, with volume manufacturing on the SF5A process expected in the second half of 2027. This is a relatively aggressive timeline for a new chiplet ecosystem and reflects both the urgency of the physical AI market and Samsung Foundry's need for differentiated advanced-node revenue as TSMC maintains its lead at the process frontier.

Samsung Foundry's position in the semiconductor industry has been a persistent topic of analysis over the past two years. Its 3nm and 4nm processes have experienced yield challenges that allowed TSMC to maintain dominance in premium advanced-node manufacturing. The Physical AI chiplet platform represents a strategic move to compete on system-level value rather than purely on process node competition — offering an integrated design solution that includes not just the foundry process but the pre-verified IP, design tools, and Cadence's extensive EDA ecosystem.

Cadence's role in this partnership extends beyond providing the EDA tools used to design the chiplets. The company's verification intellectual property and design rule checks are embedded in the platform, meaning chiplet designs created within the ecosystem carry Cadence's own certification as meeting specified standards. For automotive and industrial customers who require third-party validation of safety-critical silicon, this embedded Cadence validation is commercially significant.

## Why This Matters Beyond Chips

The Samsung-Cadence partnership is a leading indicator of where the physical AI compute market is heading. For the past several years, physical AI has largely run on adapted versions of chips designed for other purposes — mobile SoCs, gaming GPUs, data center inference accelerators. As physical AI applications mature and volume scales, the economic case for purpose-built silicon becomes compelling.

NVIDIA has recognized this with its push into automotive through Drive Thor and its investment in robotics companies. Qualcomm's Snapdragon Ride platform addresses similar territory. The difference is that Samsung and Cadence are offering a foundry-plus-design-ecosystem solution rather than a finished chip, which gives physical AI companies a path to custom silicon that doesn't require building an in-house chip design team from scratch.

The tape-out timeline puts volume production in late 2027 — which means the first generation of products built on this platform will likely appear in commercial robots, vehicles, and industrial systems in 2028 and 2029. The decisions that physical AI companies make about their silicon strategy today will shape the competitive landscape of autonomous systems a decade from now.
