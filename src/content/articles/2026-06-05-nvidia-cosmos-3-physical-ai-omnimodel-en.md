---
title: "NVIDIA Cosmos 3: The World's First Fully Open Omnimodel for Physical AI"
summary: "NVIDIA unveiled Cosmos 3 at GTC Taipei — the world's first fully open omnimodel for physical AI. Its mixture-of-transformers architecture combines vision reasoning, world generation, and action prediction in a single system, reducing physical AI training and evaluation cycles from months to days."
category: "ai-ml"
publishedAt: 2026-06-05
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: true
trending: true
sources:
  - name: "NVIDIA Newsroom"
    url: "https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai"
  - name: "Hugging Face Blog"
    url: "https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai"
  - name: "HPCwire / AIwire"
    url: "https://www.hpcwire.com/aiwire/2026/06/01/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai/"
  - name: "NVIDIA Investor Relations"
    url: "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Launches-Cosmos-3-the-Open-Frontier-Foundation-Model-for-Physical-AI/default.aspx"
tags:
  - "NVIDIA"
  - "Cosmos 3"
  - "physical AI"
  - "robotics"
  - "foundation model"
  - "open source"
  - "Computex 2026"
relatedSlugs:
  - "2026-06-03-nvidia-rtx-spark-superchip-computex-en"
  - "2026-06-01-nvidia-n1x-computex-arm-laptop-launch-en"
---

For over a decade, building a capable robot required stitching together dozens of separate components: computer vision systems, physics simulators, motion planners, and language interfaces — each trained independently, each speaking a different data format. NVIDIA's Cosmos 3, announced at GTC Taipei, is an attempt to collapse that entire stack into a single, open model.

"The big bang of physical AI is just around the corner thanks to breakthroughs in multimodal reasoning language, vision and world models," NVIDIA CEO Jensen Huang said.

## A New Kind of Foundation Model

Cosmos 3 is what NVIDIA calls an "omnimodel" — a single neural system that simultaneously perceives and generates across text, images, video, ambient sound, and robot actions. The distinction from prior multimodal models is significant: Cosmos 3 doesn't simply describe what it sees or generate images from prompts. It can reason about physical interactions, simulate how objects move through space, and output the precise action trajectories a robot needs to complete a task.

The architecture powering this is a mixture-of-transformers (MoT) design that pairs a **reasoning transformer** with an **expert generation transformer**, letting Cosmos 3 understand object interactions, motion and spatial-temporal relationships before generating video and action trajectories.

This pairing allows Cosmos 3 to understand object interactions, motion and spatial-temporal relationships before generating video and action trajectories. Earlier systems could produce video that looked realistic but violated basic physics — objects phasing through walls, liquids flowing uphill. Cosmos 3's internal reasoning step acts as an implicit physics constraint, confining generation to trajectories consistent with real-world dynamics.

## Two Models Available, One Coming Soon

NVIDIA released two variants on launch day, available now via Hugging Face, GitHub, build.nvidia.com, and NIM microservices:

**Cosmos 3 Nano** pairs an 8B-parameter reasoner with an 8B-parameter generator. Nano is designed for efficient inference on workstation-grade compute such as the RTX PRO 6000 GPU, and for high-quality video and action reasoning in fractions of a second.

**Cosmos 3 Super** pairs a 32B-parameter reasoner with a 32B-parameter generator. This larger variant is aimed at post-training robotics and AV models that need the highest physics accuracy and generation quality, as well as large-scale synthetic data generation and research.

**Cosmos 3 Edge** is announced as coming soon. Details remain limited, but the name implies a highly compressed variant optimized for deployment directly on embedded robotic hardware, potentially as a sub-8B model.

The model was trained on one of the largest multimodal physical AI datasets, including billions of samples across text, image, video, sound and action trajectories.

## The Robotics Data Bottleneck

The canonical challenge in robotics has always been data. Training a robot for a new task — picking irregularly shaped parts off a conveyor, navigating an unfamiliar warehouse floor — traditionally requires thousands of hours of real-world demonstrations followed by months of simulation-to-reality transfer work. The pipeline is expensive, specialized, and brutally slow.

Cosmos 3 attacks this problem at two levels. As a **world model**, it can generate synthetic video of novel physical scenarios, effectively manufacturing training examples that don't exist yet in the real world. As an **action model**, it translates simulated experience into robot-ready trajectory data, closing the loop between imagination and execution.

NVIDIA claims the result is a compression of training cycles from months to days. Even if the actual speedup varies significantly by application — and it will — a 10x improvement in robotics R&D velocity would be transformative for an industry where development timelines typically span years and average prototype costs run into the millions.

## The Cosmos Coalition

To accelerate ecosystem adoption, NVIDIA launched the Cosmos Coalition — a global collaboration between world model builders and AI developers, whose members can contribute models, research and evaluation techniques. Founding members include Agile Robots, Black Forest Labs, Generalist, LTX, Runway, and Skild AI.

The coalition's structure is deliberately cross-disciplinary. Runway's video generation expertise creates a pipeline for richer visual training data. Skild AI's robot learning research feeds into action model improvements. Black Forest Labs contributes image generation capabilities that help bridge the gap between static scene understanding and dynamic world simulation.

On the developer side, Doosan Robotics, LG Electronics, Samsung Electronics, Li Auto, Centific, Fogsphere, Linker Vision, Milestone Systems, and Yuan are building on the Cosmos platform.

## "Open" — With Important Caveats

The "open" label on Cosmos 3 invites scrutiny. NVIDIA has released model weights and made the system accessible through Hugging Face — a meaningful commitment compared to the fully proprietary approach of competitors like Boston Dynamics or Agility Robotics.

For most commercial users — robotics startups, enterprise integrators, industrial automation vendors — that distinction is irrelevant. For academic researchers studying how physical AI learns from data, it matters considerably.

## Competitive Context

Cosmos 3 enters a quickly consolidating field. Google DeepMind has been advancing physical AI through its robotics team and Gemini-based integrations. Figure AI and Physical Intelligence (Pi) are building proprietary robot foundation models backed by substantial venture funding. Amazon's robotics division is quietly deploying AI-native systems across its fulfillment network, accumulating proprietary data at scale.

What distinguishes Cosmos 3 is the combination of openness and benchmark performance. That lead may prove temporary — the pace of progress in physical AI is relentless — but NVIDIA has staked out a commanding early position.

## What Comes Next

The immediate watch item is Cosmos 3 Edge, whose specifications NVIDIA has not yet disclosed. If it achieves competitive performance on embedded hardware — especially on NVIDIA's own Jetson platform — it could become the default substrate for a new generation of cost-effective autonomous systems deployable without cloud connectivity.

Longer term, Cosmos 3's impact will be measured not in benchmark scores but in what actually ships. If the Cosmos Coalition's development timeline holds, expect to see the first commercial deployments in manufacturing and logistics by early 2027. Jensen Huang's "big bang" of physical AI may still be just around the corner — but the countdown has unmistakably begun.

*Correction (November 15, 2026): 17 sentences were corrected or removed to match the sources listed on this page.*
