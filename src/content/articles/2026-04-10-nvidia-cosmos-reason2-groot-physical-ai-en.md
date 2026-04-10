---
title: "NVIDIA Releases Cosmos Reason 2 and GR00T N1.6 to Accelerate Physical AI Robotics"
summary: "During National Robotics Week 2026, NVIDIA released Cosmos Reason 2 — a leaderboard-topping reasoning vision-language model for physical AI — alongside GR00T N1.6, an open VLA model for full-body humanoid control. With Isaac Lab-Arena for evaluation and the OSMO compute framework, NVIDIA is positioning itself as the Android-like platform layer for next-generation robotics, drawing in global partners from Franka to NEURA Robotics."
category: "ai-ml"
publishedAt: 2026-04-10
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

When Jensen Huang took the stage at CES in January, he made a declaration that framed the rest of NVIDIA's year: physical AI — artificial intelligence embedded in systems that perceive and act in the real world — was the company's next frontier. The GPU business built NVIDIA. The AI training and inference business transformed it. Physical AI, Huang argued, would define it for the decade ahead.

That strategic bet is now moving from vision to product. During National Robotics Week 2026 in April, NVIDIA released two new open models — **Cosmos Reason 2** and **GR00T N1.6** — alongside a suite of developer tools designed to make building, training, and deploying physical AI systems dramatically faster. The releases drew in a wave of global robotics companies announcing new robot platforms powered by NVIDIA's stack, signaling that the company's attempt to become the de facto platform layer for the coming generation of intelligent machines is gaining traction.

### Cosmos Reason 2: A Reasoning Model That Understands the Physical World

Cosmos Reason 2 is NVIDIA's latest open reasoning vision-language model (VLM), specifically designed for applications in robotics, autonomous vehicles, and physical AI systems that need to understand and reason about the real world.

The model's core contribution is what NVIDIA calls "spatio-temporal reasoning" — the ability to track how objects move, change, and interact across both space and time. For a robot navigating a warehouse, this means understanding not just what is in front of it right now, but predicting where objects will be when it reaches them, how a human coworker's trajectory will intersect with its own, and whether a partially occluded object behind a box is likely to be a hazard. That kind of physics-grounded, causality-aware reasoning is the difference between a robot that can execute preprogrammed routines and one that can handle novel situations.

Cosmos Reason 2 ships in **two model sizes** — 2B and 8B parameters — enabling flexible deployment across the compute spectrum, from edge devices on the factory floor to cloud-connected inference servers. The model supports up to **256K tokens of context**, which is critical for long-horizon reasoning tasks that require holding an extended history of observations and actions in mind.

A key practical capability is timestamp-annotated reasoning for video. Cosmos Reason 2 can process real or synthetically generated training videos and produce precise timestamped descriptions of events — a capability that dramatically accelerates the creation of labeled training data for robot learning systems. Generating high-quality labeled training data has long been one of the most expensive bottlenecks in physical AI development; Cosmos Reason 2 directly attacks that constraint.

On published benchmarks, Cosmos Reason 2 sits at the top of the physical AI reasoning leaderboard, outperforming comparable open-weight models on tasks requiring spatial understanding, object tracking, and physics-grounded inference.

### GR00T N1.6: Open Full-Body Humanoid Control

GR00T N1.6 is the latest iteration of NVIDIA's open vision-language-action (VLA) model purpose-built for **humanoid robots**. Where Cosmos Reason 2 is a perception and reasoning model, GR00T N1.6 is an action model — it takes visual observations and language instructions as input and generates low-level motor commands that control a robot's full body.

The N1.6 update integrates Cosmos Reason 2's reasoning capabilities directly into the action pipeline, allowing humanoid robots to benefit from enhanced spatial understanding and causal reasoning before issuing motor commands. In practice, this means a GR00T N1.6-powered robot can handle more complex, multi-step manipulation tasks in unstructured environments — the kind of tasks that have historically required extensive hand-engineered control logic and still fail regularly in real-world deployment.

GR00T N1.6 is open-source and available on Hugging Face, lowering the barrier for robotics teams worldwide to build on and contribute to NVIDIA's physical AI stack. Several leading humanoid robotics companies — including **Franka Robotics**, **NEURA Robotics**, and **Humanoid** — have announced that they are using GR00T-enabled workflows to simulate, train, and validate new robot behaviors, with real-world deployments underway in manufacturing and logistics settings.

### Isaac Lab-Arena and OSMO: The Tooling Layer

Models alone do not build robot systems. The releases were accompanied by two tooling updates that complete the developer platform picture:

**Isaac Lab-Arena** is NVIDIA's new robot evaluation framework, providing standardized benchmarks and simulation environments for measuring robot policy performance. Before GR00T N1.6, there was no consistent way to compare robot performance across different tasks, hardware platforms, and training regimes. Isaac Lab-Arena establishes a common evaluation layer — a critical piece of infrastructure for the field to make systematic progress.

**OSMO** is NVIDIA's edge-to-cloud compute orchestration framework for physical AI workflows. It simplifies the process of moving robot training workloads across development environments: data collection on the factory floor, synthetic augmentation in simulation, large-scale reinforcement learning training on cloud GPU clusters, and then deployment back to edge devices on the robot. By providing a unified compute fabric, OSMO eliminates the integration overhead that has historically made robot development far slower than software development.

Together, Isaac Lab-Arena and OSMO represent NVIDIA's attempt to build the "Android of robotics" — not just providing the chips and models, but establishing the full-stack platform on which robot builders develop, test, and ship. The strategic parallels to Google's move in the smartphone era are not accidental.

### National Robotics Week and Industry Momentum

The timing of the releases — during National Robotics Week — is deliberate branding, positioning NVIDIA as the center of gravity for the global robotics ecosystem. The company used the occasion to highlight a growing wave of partner announcements, including:

- **Serve Robotics** debut of "Maggie," the company's first AI-powered conversational delivery robot, demonstrated live at NVIDIA GTC 2026 in San Jose.
- **Agricultural robotics** applications in precision farming, where vision AI models are enabling autonomous weeding, harvesting, and crop monitoring.
- **Energy sector robots** being deployed for inspection and maintenance in environments too dangerous or remote for human workers.
- **Warehouse and logistics** robots from multiple partners, using GR00T N1.6 for bin picking, packing, and inventory management.

The breadth of application domains reflects the key insight behind NVIDIA's physical AI strategy: foundation models trained on diverse physical world data generalize in ways that task-specific robot controllers do not. A model that understands physics, causality, and spatial relationships deeply enough can be fine-tuned to a new application far faster than a traditional control system can be redesigned from scratch.

### The Competitive Landscape

NVIDIA's physical AI stack is competing with building efforts at several fronts. Google DeepMind's **Gemini Robotics** program — built on Gemini 3.1's multimodal capabilities — is the most direct competitor at the foundation model level, with a particular focus on dexterous manipulation and physical reasoning. Boston Dynamics continues to develop its own foundation models for Atlas, though it has been more cautious about open-source release. Figure AI and 1X Technologies, two of the best-funded humanoid startups, have also been developing proprietary VLA models optimized for their specific hardware.

What gives NVIDIA structural advantages in this competition are the same forces that have driven its dominance in AI training: the CUDA software ecosystem, the NVIDIA DGX infrastructure used to train these models, and the Jetson edge compute platform used to deploy them on robots. A robotics team that trains on NVIDIA hardware and deploys on Jetson has a seamlessly integrated development stack — a significant practical advantage over competitors assembling heterogeneous infrastructure from multiple vendors.

### Why Physical AI Is NVIDIA's Next Act

The business logic behind NVIDIA's physical AI investment is straightforward. The AI training and inference market — though still growing rapidly — has a ceiling defined by the number of companies building large-scale AI systems. The physical AI market, by contrast, has a ceiling defined by the number of machines in the world that could, in principle, be made intelligent: factory robots, warehouse systems, delivery vehicles, construction equipment, agricultural machinery, and eventually household robots. That market is orders of magnitude larger than the AI software market.

Jensen Huang has compared the opportunity to the transition from single-purpose calculators to general-purpose computers. The analogy is imperfect but directionally compelling. NVIDIA's bet is that the transition from single-purpose industrial robots to general-purpose physical AI systems will generate a technology platform opportunity every bit as large as the transition to AI-accelerated computing — and that the company that provides the foundation model stack, the training infrastructure, and the deployment edge compute will capture the lion's share of that value.

Cosmos Reason 2 and GR00T N1.6 are not the endpoint of that bet. They are the latest evidence that the build is progressing on schedule.
