---
title: "Odyssey Raises $310 Million at $1.45B Valuation to Build AI That Learns Physics and Causality"
summary: "World model startup Odyssey closed a $310 million Series B backed by Amazon, AMD Ventures, and Google Ventures, bringing its valuation to $1.45 billion and total raised to $337 million. Founded by veterans of Voyage and Wayve, the company is betting that the next frontier in AI is not language but physics—models that simulate the real world with accurate causality, enabling breakthroughs in robotics, interactive video, and game creation."
category: "startups"
publishedAt: 2026-06-24
lang: "en"
featured: false
trending: false
sources:
  - name: "TechCrunch: World model maker Odyssey nabs $1.45B valuation backed by Amazon"
    url: "https://techcrunch.com/2026/06/17/world-model-maker-odyssey-nabs-1-45b-valuation-backed-by-amazon-and-other-big-names/"
  - name: "HPCwire: Odyssey Raises $310M Series B to Advance AI World Models"
    url: "https://www.hpcwire.com/off-the-wire/odyssey-raises-310m-series-b-to-advance-ai-world-models/"
  - name: "Unite.AI: Odyssey Raises $310 Million Series B at $1.45 Billion Valuation"
    url: "https://www.unite.ai/odyssey-raises-310-million-series-b-at-1-45-billion-valuation-to-advance-ai-world-models/"
  - name: "Odyssey blog: Our $310 Million Fundraise to Accelerate World Simulation"
    url: "https://odyssey.ml/our-series-b"
tags:
  - "world-models"
  - "startups"
  - "funding"
  - "robotics"
  - "Amazon"
  - "AWS"
  - "physical-AI"
relatedSlugs:
  - "2026-06-09-generalist-ai-400m-robot-foundation-model-en"
  - "2026-06-08-physicsx-300m-series-c-industrial-ai-en"
  - "2026-06-07-flourish-ai-500m-bezos-neuromorphic-en"
---

What if the next major leap in artificial intelligence is not a bigger language model, but a model that understands physics? That is the premise behind Odyssey, a three-year-old AI lab that on June 17, 2026 announced a **$310 million Series B** at a **$1.45 billion valuation**, bringing its total fundraising to $337 million. The round was led by Natural Capital and joined by Amazon, AMD Ventures, Google Ventures, and a set of angel investors that includes Jeff Dean, Elad Gil, Garry Tan, Guillermo Rauch, and Kyle Vogt.

The company is building what researchers call "world models"—AI systems designed not to predict the next token in a text sequence, but to predict the next state of a physical or interactive environment. Think less ChatGPT, more a physics engine that has watched enough of the real world to simulate it accurately.

## What World Models Actually Are

The term "world model" has been used loosely in AI circles for years, but Odyssey has a specific technical definition at its core. Its models are trained to "gather data from the physical world and simulate it with accurate physics," learning causal relationships between actions and outcomes rather than statistical correlations between tokens.

The distinction matters for applications. A language model can describe what happens when you drop a glass; a world model can simulate the trajectory, shatter pattern, and fragment distribution—and generalize that understanding to novel objects and surfaces it has never seen. The causal structure enables a class of predictions that statistical pattern-matching cannot reliably produce.

Odyssey's data collection methodology reflects this physical focus. The company has, literally, "sent people out with cameras strapped to their backs," capturing egocentric video of the world from the perspective of agents moving through it. This embodied-perspective data is a deliberate design choice: it teaches the model to represent the world from the viewpoint of a system that acts within it, not merely observes it.

## The Founders and Their Pedigree

Oliver Cameron, Odyssey's CEO, previously co-founded Voyage—an autonomous trucking company—and served as VP of Product at Cruise, where he was part of the team that built one of the first large-scale autonomous vehicle fleets. Jeff Hawke, the CTO, was a senior engineer at Wayve, the London-based autonomous driving startup that has also been exploring neural world models as a foundation for robotic perception.

Both founders bring the specific combination of skills that world model development requires: deep experience with sensor fusion, physical-world data collection at scale, and the kind of iterative closed-loop training that teaches models to predict environmental dynamics rather than text. Their autonomous driving backgrounds are not incidental—AV development spent the past decade grappling with exactly the problem that world models are supposed to solve: how to teach a system to predict what the world will do next, in enough detail to act safely within it.

## AWS as Preferred Cloud, Trainium as the Bet

The fundraise comes with a strategic infrastructure commitment. Amazon Web Services will become Odyssey's preferred cloud provider, and the company will optimize its models to run on AWS's **Trainium** chips—the custom silicon that Amazon has positioned as its primary challenge to Nvidia's datacenter dominance.

This is a meaningful bet in the current competitive landscape. Trainium 2 and the forthcoming Trainium 3 represent AWS's most aggressive effort to capture a share of AI training workloads that has historically been dominated by Nvidia's H100 and B200 GPUs. Odyssey committing to Trainium optimization gives Amazon a high-profile proof point for the chip's viability at frontier training workloads, while giving Odyssey preferential access to AWS's compute resources and potentially lower negotiated rates.

Amazon's participation as an investor—not just a cloud partner—signals that the company sees world models as a genuine frontier, not merely a research curiosity. Amazon's robotics and fulfillment operations are an obvious eventual customer for physical AI systems that can simulate and plan in factory and warehouse environments.

## Three Application Domains

Odyssey is targeting three initial application areas, each of which is limited by the absence of reliable physics-aware AI:

**Robotics.** The most consequential near-term use case. Current robotic systems are brittle in novel environments because they rely on rules and scene parsers that break down when confronted with objects or configurations outside their training distribution. A world model that understands causal physics can generalize—it knows that a box will fall if unsupported regardless of whether it has seen that exact box before. This is the capability gap that has prevented general-purpose robot arms and mobile robots from operating reliably outside carefully controlled environments.

**Interactive video generation.** Existing video generation models (Sora, Kling, Veo) produce visually impressive clips but frequently violate physical laws—objects pass through each other, gravity behaves inconsistently, shadows don't match light sources. World models trained on physical causality could produce video that is not just visually coherent but physically plausible, enabling applications from cinematic pre-visualization to training data generation for other AI systems.

**Video game creation.** Games are a natural fit for world models: they are fully simulated environments with explicit physics engines. Odyssey's technology could allow developers to describe game environments in natural language and have an AI generate physically consistent interactive worlds, dramatically compressing the asset creation and world-building pipeline that currently accounts for much of AAA game development cost.

## The Broader World Model Wave

Odyssey is not alone. Google DeepMind's Genie and its successors, Meta's V-JEPA series, and a wave of smaller labs have converged on the insight that the next capability frontier in AI involves learning to model the structure of the physical world, not just its linguistic surface. The reasoning: language models have essentially exhausted the information available in text; the untapped information in the physical world—causality, physics, embodied interaction—is vastly larger and potentially more generalizable.

The $310 million Odyssey has raised is, in this context, a vote that the world model paradigm is real and that the infrastructure to train these systems at scale is worth funding years ahead of clear product-market fit.

That's a familiar investment thesis in AI. It was the same bet made on large language models before ChatGPT showed what they could do. World models are earlier, harder to evaluate, and farther from consumer applications—but the investor roster, which includes the chief scientist of Google and the founder of Y Combinator, suggests the technical credibility behind Odyssey's approach is seen as genuine.

## What Comes Next

With $310 million in new capital, Odyssey's immediate priorities are scaling training runs, expanding the team, and deepening the AWS partnership to deploy Trainium-optimized inference at production scale. The company has not announced a specific product launch timeline but has indicated that robotics applications are closest to commercialization.

The test of the world model thesis will come when Odyssey's systems are deployed in real robotic environments and interactive applications—when the question shifts from "can you simulate physics?" to "can you simulate physics well enough that it matters for real tasks?" On that question, the company has the attention of Amazon, Google, AMD, and some of the most respected operators in AI. That credibility may be the most important thing $310 million can buy before the physics of the market delivers its own verdict.
