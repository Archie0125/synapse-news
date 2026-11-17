---
title: "NVIDIA Releases Cosmos Reason 2 and GR00T N1.6 Open Models for Physical AI Robotics"
summary: "At CES, NVIDIA released Cosmos Reason 2, a leaderboard-topping reasoning vision-language model for physical AI, alongside GR00T N1.6, an open VLA model for full-body humanoid control. With Isaac Lab-Arena for evaluation and the OSMO compute framework, NVIDIA is also drawing in global partners from Franka to NEURA Robotics."
category: "ai-ml"
publishedAt: 2026-04-10T09:25:00Z
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: false
sources:
  - name: "NVIDIA Newsroom"
    url: "https://nvidianews.nvidia.com/news/nvidia-releases-new-physical-ai-models-as-global-partners-unveil-next-generation-robots"
  - name: "Hugging Face Blog"
    url: "https://huggingface.co/blog/nvidia/nvidia-cosmos-reason-2-brings-advanced-reasoning"
  - name: "The Robot Report"
    url: "https://www.therobotreport.com/nvidia-releases-new-physical-ai-models-plus-autonomous-vehicle-tools/"
  - name: "NVIDIA Blog"
    url: "https://blogs.nvidia.com/blog/national-robotics-week-2026/"
tags:
  - "NVIDIA"
  - "robotics"
  - "physical AI"
  - "Cosmos"
  - "GR00T"
  - "humanoid robots"
  - "foundation models"
relatedSlugs:
  - "2026-04-07-nvidia-vera-rubin-nvl72-production-en"
  - "2026-04-05-cognichip-ai-chip-design-en"
  - "2026-04-06-weride-uber-dubai-robotaxi-en"
---

## NVIDIA's Bid to Become the Android of Robotics Moves Into High Gear

At CES in January, Jensen Huang said that "the ChatGPT moment for robotics is here," pointing to breakthroughs in physical AI: models that understand the real world, reason and plan actions. The GPU business built NVIDIA. The AI training and inference business transformed it.

That strategic bet is now moving from vision to product. At CES in January, NVIDIA released new open models, including **Cosmos Reason 2** and **GR00T N1.6**, alongside open-source frameworks for robot development. Global partners including Boston Dynamics, Caterpillar, Franka Robotics, Humanoid, LG Electronics and NEURA Robotics used the NVIDIA robotics stack to debut new robots and autonomous machines.

### Cosmos Reason 2: A Reasoning Model That Understands the Physical World

Cosmos Reason 2 is NVIDIA's latest open reasoning vision-language model (VLM), specifically designed for applications in robotics, autonomous vehicles, and physical AI systems that need to understand and reason about the real world.

Among the model's improvements is better spatio-temporal understanding and timestamp precision. That kind of physics-grounded, causality-aware reasoning is the difference between a robot that can execute preprogrammed routines and one that can handle novel situations.

Cosmos Reason 2 ships in **two model sizes** — 2B and 8B parameters — enabling flexible deployment across the compute spectrum, from edge devices on the factory floor to cloud-connected inference servers. The model supports up to **256K tokens of context**, which is critical for long-horizon reasoning tasks that require holding an extended history of observations and actions in mind.

A key practical capability is timestamp-annotated reasoning for video. Cosmos Reason 2 can process real or synthetically generated training videos and produce precise timestamped descriptions of events — a capability that dramatically accelerates the creation of labeled training data for robot learning systems. Generating high-quality labeled training data has long been one of the most expensive bottlenecks in physical AI development; Cosmos Reason 2 directly attacks that constraint.

### GR00T N1.6: Open Full-Body Humanoid Control

GR00T N1.6 is the latest iteration of NVIDIA's open vision-language-action (VLA) model purpose-built for **humanoid robots**. Where Cosmos Reason 2 is a reasoning vision-language model, GR00T N1.6 is a vision language action model that unlocks full body control.

GR00T N1.6 uses NVIDIA Cosmos Reason for better reasoning and contextual understanding.

GR00T N1.6 is an open model available on Hugging Face, lowering the barrier for robotics teams to build on NVIDIA's physical AI stack. Franka Robotics, NEURA Robotics and Humanoid are using GR00T-enabled workflows to simulate, train and validate new robot behaviors.

### Isaac Lab-Arena and OSMO: The Tooling Layer

Models alone do not build robot systems. The release was accompanied by two open-source frameworks for robot development:

**Isaac Lab-Arena** is NVIDIA's new robot evaluation framework, providing standardized benchmarks and simulation environments for measuring robot policy performance. Benchmarking has often been manual and hard to scale, and Isaac Lab-Arena connects to benchmarks such as Libero and Robocasa to standardize testing. Isaac Lab-Arena establishes a common evaluation layer — a critical piece of infrastructure for the field to make systematic progress.

**OSMO** is NVIDIA's edge-to-cloud compute orchestration framework for physical AI workflows. It lets developers define and run workflows such as synthetic data generation, model training and software-in-the-loop testing across different compute environments, from workstations to mixed cloud instances. By unifying robotic development into a single command center, OSMO speeds up development cycles.

Together, Isaac Lab-Arena and OSMO represent NVIDIA's attempt to build the "Android of robotics" — not just providing the chips and models, but establishing the full-stack platform on which robot builders develop, test, and ship. The strategic parallels to Google's move in the smartphone era are not accidental.

### National Robotics Week and Industry Momentum

The company used the occasion to highlight a growing wave of partner announcements, including:

- **Agricultural robotics** applications in precision farming, where vision AI models are enabling autonomous weeding, harvesting, and crop monitoring.

The breadth of application domains reflects the key insight behind NVIDIA's physical AI strategy: foundation models trained on diverse physical world data generalize in ways that task-specific robot controllers do not. A model that understands physics, causality, and spatial relationships deeply enough can be fine-tuned to a new application far faster than a traditional control system can be redesigned from scratch.

### The Competitive Landscape

NVIDIA's physical AI stack is competing with building efforts at several fronts.

What gives NVIDIA structural advantages in this competition are the same forces that have driven its dominance in AI training: the CUDA software ecosystem, the NVIDIA DGX infrastructure used to train these models, and the Jetson edge compute platform used to deploy them on robots. A robotics team that trains on NVIDIA hardware and deploys on Jetson has a seamlessly integrated development stack — a significant practical advantage over competitors assembling heterogeneous infrastructure from multiple vendors.

### Why Physical AI Is NVIDIA's Next Act

The business logic behind NVIDIA's physical AI investment is straightforward. The AI training and inference market — though still growing rapidly — has a ceiling defined by the number of companies building large-scale AI systems. The physical AI market, by contrast, has a ceiling defined by the number of machines in the world that could, in principle, be made intelligent: factory robots, warehouse systems, delivery vehicles, construction equipment, agricultural machinery, and eventually household robots. That market is orders of magnitude larger than the AI software market.

The analogy is imperfect but directionally compelling. NVIDIA's bet is that the transition from single-purpose industrial robots to general-purpose physical AI systems will generate a technology platform opportunity every bit as large as the transition to AI-accelerated computing — and that the company that provides the foundation model stack, the training infrastructure, and the deployment edge compute will capture the lion's share of that value.

Cosmos Reason 2 and GR00T N1.6 are not the endpoint of that bet. They are the latest evidence that the build is progressing on schedule.

*Correction (November 15, 2026): 26 sentences were corrected or removed to match the sources listed on this page.*
