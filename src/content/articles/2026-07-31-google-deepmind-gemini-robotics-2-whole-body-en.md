---
title: "Google DeepMind Launches Gemini Robotics 2 With Full-Body Intelligence for Humanoids"
summary: "Google DeepMind released Gemini Robotics 2, a new suite of AI models enabling humanoid robots to coordinate full-body movements—from torso to legs—for the first time. The system achieves a 92% success rate on complex dexterous tasks, is being demonstrated on Apptronik's Apollo 2 humanoid, and is now available in private preview to over 100 trusted testers via Google AI Studio."
category: "ai-ml"
publishedAt: 2026-07-31
lang: "en"
featured: false
trending: true
sources:
  - name: "Google DeepMind Blog – Gemini Robotics 2 brings whole body intelligence to robots"
    url: "https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/"
  - name: "Robotics & Automation News – Google DeepMind unveils Gemini Robotics 2"
    url: "https://roboticsandautomationnews.com/2026/07/31/google-deepmind-unveils-gemini-robotics-2-as-apptronik-humanoid-demonstrates-whole-body-ai/103802/"
  - name: "SiliconANGLE – Google DeepMind debuts Gemini Robotics 2 model series for humanoid robots"
    url: "https://siliconangle.com/2026/07/30/google-deepmind-debuts-gemini-robotics-2-model-series-humanoid-robots/"
  - name: "Bloomberg – Gemini Robotics 2 Expands Google's AI Capabilities for Humanoid Robots"
    url: "https://www.bloomberg.com/news/articles/2026-07-30/google-unveils-gemini-ai-for-robots-struggling-with-dexterity"
tags:
  - "Google DeepMind"
  - "Gemini Robotics"
  - "humanoid robots"
  - "robotics"
  - "physical AI"
  - "Apptronik"
  - "whole-body intelligence"
relatedSlugs:
  - "2026-07-14-unitree-robotics-619m-shanghai-star-ipo-en"
  - "2026-07-24-japan-noetra-2b-physical-ai-robotics-en"
  - "2026-07-19-agility-robotics-spac-ipo-humanoid-nasdaq-en"
---

Google DeepMind unveiled Gemini Robotics 2 on Thursday, releasing what the company is calling the first AI model series capable of giving humanoid robots genuine whole-body intelligence—the ability to plan and coordinate movements not just in the arms and hands, but across the entire body, from the torso down to the legs.

The launch represents a significant leap beyond the original Gemini Robotics system, introduced in early 2025, which was limited to controlling a robot's upper body. With Gemini Robotics 2, a machine can now twist, lean, crouch, and reach simultaneously while reasoning through complex tasks in real time—the kind of fluid, integrated physical reasoning that humans perform automatically but that has proven stubbornly difficult to replicate in AI-controlled hardware.

## What "Whole-Body Intelligence" Actually Means

In robotics, the challenge of whole-body control has long been treated as a problem of coordination: a humanoid robot's 30-plus degrees of freedom—joints in the hips, knees, ankles, spine, shoulders, elbows, and wrists—must all be commanded simultaneously for a robot to perform natural, adaptive movements. Getting an AI model to reason across all of these simultaneously, while also reacting to changing conditions in real time, has been one of the hardest open problems in the field.

Previous approaches, including the original Gemini Robotics, handled this by decomposing the problem: a high-level reasoning system would plan a task, and a lower-level controller would execute it using pre-scripted or model-predictive motion primitives. The limitation was that this separation created gaps—when real conditions didn't match the motion primitive's assumptions, robots would fail ungracefully.

Gemini Robotics 2 replaces this decomposed architecture with a unified model that reasons about task completion and body motion simultaneously. The result is a system that can handle genuine physical contingencies—an object that slips, a surface that tilts—by adapting its entire body posture dynamically rather than failing when a pre-scripted motion sequence becomes inappropriate.

## Three Models, Three Deployment Profiles

The Gemini Robotics 2 suite is not a single model but three:

**Gemini Robotics 2** is the full cloud-hosted model, providing the highest capability for whole-body control, dexterous manipulation, and multi-robot coordination. It is designed to run inference from Google's cloud infrastructure and is best suited for research, development, and industrial deployments where network latency is acceptable.

**Gemini Robotics On-Device 2** is a smaller, optimized variant designed to run locally on robot hardware without requiring cloud connectivity. It trades some capability for dramatically lower latency—critical for reactive tasks where even a 50-millisecond round-trip to a cloud server would cause noticeable delays in physical response.

**Gemini Robotics ER 2** (Emergent Reasoning) is the most sophisticated variant, accessible via Google AI Studio and in private preview on Google's enterprise platform. ER 2 is designed for tasks requiring longer-horizon planning, multi-step task chaining, and reasoning about physical consequences across extended sequences of actions.

## Performance in Testing

DeepMind published benchmark results alongside the release. In tests involving unscrewing a lightbulb—a task that demands precise coordination between arm movement, grip force, torso stabilization, and visual feedback—Gemini Robotics 2 achieved a 92% success rate, compared to roughly 60% for leading prior systems on the same task.

The system is also the first to demonstrate reliable multi-robot coordination, where two Gemini Robotics 2-powered humanoids can hand objects between each other, coordinate on shared tasks, and avoid collisions while pursuing independent sub-goals—without pre-scripted choreography.

## Apptronik's Apollo 2 as the Lead Demo Platform

DeepMind chose Apptronik's Apollo 2 humanoid as the primary demonstration platform for Gemini Robotics 2. Apptronik, a Texas-based humanoid robotics company backed by Google, is one of a small number of hardware partners that received early access to the model for integration testing.

In live demonstrations, the Apollo 2 running Gemini Robotics 2 showed capabilities that represent genuine progress over prior benchmarks: picking objects off the floor while maintaining balance, carrying items while navigating cluttered environments, and performing two-handed manipulation tasks that require the robot to use its torso as a stabilizing reference point. The robot's movements are notably smoother than prior-generation demonstrations—a visible sign that the unified whole-body model is coordinating more naturally than decomposed architectures.

## Access and Availability

Gemini Robotics 2 and On-Device 2 are now being shared with more than 100 trusted testers, including academic robotics labs, industrial hardware partners, and select enterprise customers. Gemini Robotics ER 2 is available via Google AI Studio as an API endpoint and as a private preview on Google's enterprise AI platform.

Full general availability timelines have not been announced, but DeepMind said it expects to expand access throughout the second half of 2026, with the On-Device 2 variant expected to reach hardware integration kits for qualified partners before the end of the year.

## The Physical AI Race Intensifies

Gemini Robotics 2's launch comes in a year when physical AI—AI systems designed to operate in and interact with the physical world through robots, vehicles, and other embodied hardware—has emerged as one of the most competitive and capital-intensive frontiers in the industry.

Unitree Robotics listed on Shanghai's STAR market in July at a $619 million valuation. Agility Robotics completed a SPAC merger onto Nasdaq. Figure AI, Boston Dynamics (owned by Hyundai), and a growing roster of Chinese humanoid startups are all competing to establish manufacturing scale in a market that Goldman Sachs projects will surpass $100 billion annually by 2035.

Google's bet is that the model layer—not the hardware layer—will be where the most defensible value accumulates. If Gemini Robotics 2 becomes the default "brain" for third-party humanoid hardware the way Android became the default operating system for third-party smartphones, the economic implications would be substantial. That is the underlying strategic logic of releasing Gemini Robotics ER 2 as an API endpoint: make the capability available to every hardware maker rather than locking it to proprietary robots.

Whether the bet pays off will depend on whether DeepMind can maintain its lead over NVIDIA's physical AI stack, Boston Dynamics Atlas's increasingly capable whole-body control, and the growing number of Chinese robotics AI teams whose models are already demonstrating competitive performance on standard benchmarks.

For now, Gemini Robotics 2 sets a new public benchmark for what AI-powered whole-body coordination looks like—and raises the floor for every competitor coming behind it.
