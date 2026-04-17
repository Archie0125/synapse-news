---
title: "NVIDIA Launches Ising: The World's First Open AI Models for Quantum Computing"
summary: "NVIDIA has released Ising, a family of open-source AI models designed to accelerate the path to fault-tolerant quantum computers — delivering error correction that is 2.5x faster and 3x more accurate than leading open-source tools. The launch sent quantum computing stocks surging and marks a pivotal convergence between classical AI infrastructure and quantum hardware development."
category: "hardware"
publishedAt: 2026-04-17
lang: "en"
featured: true
trending: true
sources:
  - name: "NVIDIA Newsroom"
    url: "https://nvidianews.nvidia.com/news/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers"
  - name: "The Quantum Insider"
    url: "https://thequantuminsider.com/2026/04/14/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers/"
  - name: "NVIDIA Technical Blog"
    url: "https://developer.nvidia.com/blog/nvidia-ising-introduces-ai-powered-workflows-to-build-fault-tolerant-quantum-systems/"
  - name: "CIO"
    url: "https://www.cio.com/article/4158418/nvidia-announces-quantum-ai-models.html"
tags:
  - "nvidia"
  - "quantum computing"
  - "open source"
  - "error correction"
  - "AI models"
  - "Jensen Huang"
relatedSlugs:
  - "2026-04-15-ionq-photonic-quantum-networking-darpa-en"
  - "2026-04-10-nvidia-cosmos-reason2-groot-physical-ai-en"
---

NVIDIA has spent the past two years quietly assembling a quantum AI research team. On April 14, 2026, that work went public.

The company released **Ising** — the world's first family of open-source AI models built specifically to accelerate quantum computing research and deployment. Available now on Hugging Face and through the NVIDIA NGC catalog at no cost, the models target the two most operationally painful bottlenecks standing between today's quantum hardware and production-grade deployment: calibration and error correction.

The name is a deliberate nod to the Ising model, the foundational statistical mechanics framework that has served as a benchmark for quantum annealers and optimization problems for decades. For Jensen Huang, who fronted the announcement personally, it signals that quantum computing is no longer a speculative adjacency to NVIDIA's core GPU business — it is part of the platform roadmap.

## Two Models, Two Bottlenecks Solved

Ising ships as two distinct components, each designed to eliminate a specific class of failure that has stalled quantum hardware commercialization.

**Ising Calibration** is a vision-language model trained to interpret the raw measurement outputs of quantum processors — the noisy, drift-prone signal streams that quantum engineers currently spend days manually analyzing and compensating for. Quantum hardware is inherently unstable: qubit frequencies drift with temperature, electromagnetic interference, and material aging. Recalibrating a large quantum processor from scratch can take anywhere from eight hours to three days, depending on qubit count and system complexity.

Ising Calibration treats this problem as a multimodal perception task. The model reads quantum state tomography data the way a conventional vision model reads an image, identifies drift signatures, and recommends parameter corrections automatically — compressing calibration cycles from days to hours. For quantum teams trying to achieve high uptime on production hardware, that compression is the difference between a research instrument and a deployable system.

**Ising Decoding** addresses the harder problem: real-time quantum error correction. Quantum computers make errors at rates that, without correction, would render any computation meaningless. Quantum error correction codes — particularly surface codes — work by entangling multiple physical qubits to encode a single logical qubit, then measuring syndrome bits to detect and correct errors before they propagate. The challenge is speed: the classical decoding hardware must interpret syndrome data and issue corrections faster than the rate at which new errors accumulate, a constraint that grows exponentially with qubit count.

NVIDIA benchmarked Ising Decoding against pyMatching, the current open-source industry standard for surface code decoding, and found it runs **2.5x faster** while achieving **3x greater accuracy**. Two variants ship simultaneously: one optimized for raw throughput (targeting hardware pipelines where latency is critical) and one optimized for decoding fidelity (for research settings where minimizing logical error rates matters more than speed).

The models are hardware-agnostic by design. They work across superconducting qubits, trapped ions, neutral atoms, and photonic platforms — meaning NVIDIA does not need to bet on a single winning hardware modality to benefit from the ecosystem's adoption.

## Who's Building With It Already

The launch comes with a credible and geographically diverse list of early adopters.

**Atom Computing**, the neutral-atom quantum hardware startup, is using Ising Calibration in its automated drift-correction pipeline. **EeroQ**, which is building qubit systems using helium-3 surface electrons, is evaluating Ising Decoding for its error correction stack.

**Fermi National Accelerator Laboratory (Fermilab)** and **Harvard's quantum research group** are both running early research workloads on the models — a combination of national laboratory credibility and elite academic validation.

**Academia Sinica** in Taiwan, one of Asia's most significant quantum research institutions, is also listed among adopters. The inclusion is notable given Taiwan's central role in NVIDIA's hardware supply chain and the Taiwanese government's growing investment in quantum computing capability.

**Conductor Quantum**, a quantum compiler startup that recently emerged from stealth, announced it is integrating Ising Decoding directly into its control stack as a default error correction layer — a strong signal that the models are already production-grade enough for commercial tooling.

## IonQ Surges 20%; Quantum Sector Rallies

The release triggered an immediate and significant reaction in quantum computing equities. **IonQ**, the NYSE-listed quantum hardware company, saw its stock rise more than **20% in a single session** following the announcement. Other quantum-adjacent names — including Rigetti Computing and D-Wave — posted gains in the range of 8 to 12%.

The investor interpretation appears less about NVIDIA's specific product and more about what it signals: that the classical AI infrastructure buildout is now creating conditions for quantum hardware to cross the deployment threshold. NVIDIA's willingness to invest in open quantum AI tooling suggests the company believes commercial quantum systems are arriving on a timeline measured in years, not decades.

"The calibration and error correction problems have been the graveyard of quantum roadmaps for a decade," one quantum infrastructure investor noted after the announcement. "If NVIDIA's models hold up in production, they remove two of the biggest technical excuses for not deploying."

## Jensen Huang's Platform Bet

Huang's decision to personally front the Ising announcement carries strategic weight beyond the quantum sector. At GTC 2026 earlier this year, he identified physical AI and quantum computing as the two major frontiers beyond the current large language model paradigm. Ising is the first concrete deliverable from NVIDIA's quantum AI research unit — established quietly in late 2024 with hires from IBM Quantum, Google Quantum AI, and leading academic quantum labs.

The release also reflects a larger and increasingly visible pattern: NVIDIA is no longer content to be merely a GPU supplier. With **Cosmos** for physical AI simulation, **Isaac GR00T** for robotics, and now **Ising** for quantum, the company is assembling a software and model stack that would make it very difficult for any future hardware competitor to displace NVIDIA GPUs without causing customers to lose access to critical infrastructure.

Open-sourcing Ising is not a concession — it is a moat-building move. Models that become foundational to quantum research workflows create ecosystem lock-in independent of whether the underlying compute is NVIDIA hardware. NVIDIA earns when the systems running these models scale, and all of those classical control systems, for the foreseeable future, will run on NVIDIA silicon.

## What Comes Next

NVIDIA has indicated that Ising is the opening release in a broader quantum AI model series. Future releases, expected later in 2026, will include models for quantum circuit compilation optimization — helping classical compilers map logical quantum circuits onto specific hardware topologies — and quantum advantage benchmarking, a long-contested challenge where reliably demonstrating that a quantum system has outperformed the best classical algorithms on a commercially meaningful task remains elusive.

The roadmap suggests NVIDIA intends to own the software layer of quantum computing the same way it came to own the software layer of GPU-accelerated machine learning through CUDA. That took fifteen years. The quantum version may be faster.

The models are live. The race to useful quantum computing just added a new competitor — and it's the one that already makes the hardware the entire industry runs on.
