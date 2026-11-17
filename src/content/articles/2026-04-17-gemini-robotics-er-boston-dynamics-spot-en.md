---
title: "Google DeepMind's Gemini Robotics-ER 1.6 Brings AI Reasoning to Boston Dynamics' Spot"
summary: "Google DeepMind launched Gemini Robotics-ER 1.6, a reasoning-first model that enhances robots' spatial reasoning and multi-view understanding and adds instrument reading for complex gauges. Boston Dynamics is integrating it into its Orbit AIVI-Learning inspection software for Spot."
category: "ai-ml"
publishedAt: 2026-04-17
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "Google DeepMind Blog"
    url: "https://deepmind.google/blog/gemini-robotics-er-1-6/"
  - name: "SiliconAngle"
    url: "https://siliconangle.com/2026/04/15/deepmind-launches-gemini-robotics-er-1-6-meet-precise-physical-ai-demands/"
  - name: "The Robot Report"
    url: "https://www.therobotreport.com/boston-dynamics-and-google-deepmind-are-using-gemini-to-make-spot-smarter/"
  - name: "IEEE Spectrum"
    url: "https://spectrum.ieee.org/boston-dynamics-spot-google-deepmind"
  - name: "Robotics and Automation News"
    url: "https://roboticsandautomationnews.com/2026/04/15/boston-dynamics-integrates-google-deepminds-gemini-robotics-model-into-spot-inspection-platform/100585/"
tags:
  - "google deepmind"
  - "robotics"
  - "boston dynamics"
  - "physical AI"
  - "gemini"
  - "Spot"
relatedSlugs:
  - "2026-04-10-nvidia-cosmos-reason2-groot-physical-ai-en"
  - "2026-04-17-nvidia-ising-quantum-ai-models-en"
---

For years, the gap between robot hardware and robot intelligence has been the defining problem of industrial automation. The hardware — cameras, actuators, sensors — has gotten extraordinarily capable. The intelligence layer has lagged, requiring robots to operate within narrowly scripted environments with little tolerance for the messiness of real-world conditions.

Google DeepMind has released **Gemini Robotics-ER 1.6**, and that gap got meaningfully smaller.

The model, described by DeepMind as a "reasoning-first" upgrade to its Gemini Robotics line, brings a qualitatively different kind of intelligence to physical systems: the ability to look at an environment and actually understand it — not just detect objects, but reason about spatial relationships, assess task completion, and decide when to escalate to more specialized tools. On the same day, Boston Dynamics announced it is integrating Gemini and Gemini Robotics-ER 1.6 into Orbit AIVI-Learning, part of the software platform used for Spot's industrial inspection workflows.

The model is available starting today to developers via the Gemini API and Google AI Studio.

## What "Embodied Reasoning" Actually Means

DeepMind describes Gemini Robotics-ER as a reasoning-first model built around "embodied reasoning," the capability that lets a robot bridge digital intelligence and physical action.

Standard vision-language models are good at describing what they see. Embodied reasoning models are designed to understand what to do with what they see — a distinction that sounds subtle but matters enormously in physical environments. A robot equipped with a description-only model can tell you there is a gauge on the wall. An embodied reasoning model can read the gauge, interpreting needles, tick marks and numbers.

Gemini Robotics-ER 1.6 specifically improves several capabilities for robotics:

**Spatial reasoning**: DeepMind says the model enhances spatial reasoning and multi-view understanding, including pointing and counting. This supports robots in understanding their environments with greater precision.

**Task completion assessment**: Rather than relying on scripted success criteria, the model can evaluate whether a task has been accomplished by interpreting visual evidence — a critical capability for autonomous quality inspection workflows where success is often ambiguous from a single frame.

**Tool escalation**: When the model encounters a situation beyond its direct capabilities, it can identify and invoke specialized vision-language-action (VLA) models to handle the specific subtask. This meta-capability turns Gemini Robotics-ER 1.6 into an orchestration layer for a broader ecosystem of specialized robotics models.

## Boston Dynamics' Bet on AI-Powered Inspection

The partnership with Boston Dynamics is a key part of the Gemini Robotics-ER 1.6 launch, and the Gemini-powered AIVI-Learning system is already live for existing customers.

Boston Dynamics is integrating the model into its Orbit software platform, including **AI Visual Inspection (AIVI)**, which lets Spot answer questions about a facility from visual data, and **AIVI-Learning**, which delivers insights trained on industrial data sets.

With Gemini Robotics-ER 1.6 onboard, Spot gains a set of capabilities that mark a qualitative leap for industrial inspection robots. The system can now autonomously detect dangerous debris or liquid spills on floors and surfaces — a safety-critical function in manufacturing, oil and gas, and utility environments. It can read complex gauges and sight glasses, interpreting analog instruments that previously required human visual assessment. And it can call on specialized VLA models when it encounters something outside its direct knowledge — a manufacturing anomaly it hasn't seen before, an unfamiliar equipment configuration, or a situation requiring fine manipulation reasoning.

Industrial inspection has been one of the most compelling early applications for autonomous mobile robots, but the limiting factor has consistently been intelligence rather than mobility. What it has lacked is the ability to make nuanced judgments about what it observes. Gemini Robotics-ER 1.6 directly addresses that gap.

## The Physical AI Race Heats Up

The release lands in an increasingly competitive landscape for physical AI.

Rather than owning the robot, DeepMind aims to own the intelligence layer.

This is consistent with Google's broader strategy. Making Gemini Robotics-ER available via API means any developer building robotics applications can call on DeepMind's latest research without needing to build and train embodied reasoning capabilities from scratch.

The Boston Dynamics partnership is particularly notable because Boston Dynamics occupies a unique position in the robotics market: it makes hardware that people genuinely trust with safety-critical tasks.

## Developer Access and What Comes Next

Gemini Robotics-ER 1.6 is available to developers starting today via the Gemini API and Google AI Studio.

For robotics developers and integrators, Gemini Robotics-ER 1.6 raises the floor of what's achievable with off-the-shelf AI. Robots don't need to be programmed for every scenario if the model can reason through novel situations. That shift — from scripted automation to adaptive intelligence — is the transition the industry has been building toward for years.

It's no longer theoretical.

*Correction (November 15, 2026): 25 sentences were corrected or removed to match the sources listed on this page.*
