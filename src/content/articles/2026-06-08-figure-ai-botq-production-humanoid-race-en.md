---
title: "One Robot Per Hour: Figure AI's BotQ Signals Humanoid Manufacturing Has Arrived"
summary: "Figure AI's BotQ facility in California has ramped production of its Figure 03 humanoid robot from one unit per day to one per hour — a 24-fold increase in under four months — targeting 12,000 units annually. The milestone, combined with Boston Dynamics Atlas deployments at Hyundai and NVIDIA's Unitree partnership for research labs, marks the moment humanoid robotics transitions from demo to manufacturing reality."
category: "hardware"
publishedAt: 2026-06-08
lang: "en"
featured: false
trending: true
sources:
  - name: "Figure AI"
    url: "https://www.figure.ai/news/botq"
  - name: "eWeek"
    url: "https://www.eweek.com/news/figure-03-humanoid-robot-production-helix-ai/"
  - name: "Interesting Engineering"
    url: "https://interestingengineering.com/ai-robotics/figure-humanoid-robot-production-scale-up"
  - name: "Robotics and Automation News"
    url: "https://roboticsandautomationnews.com/2026/05/27/figure-ramps-humanoid-robot-manufacturing-at-unprecedented-speed/101954/"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/06/01/nvidia-unitree-humanoid-robotics-system-researchers.html"
tags:
  - "Figure AI"
  - "humanoid robots"
  - "robotics"
  - "BotQ"
  - "physical AI"
  - "manufacturing"
  - "NVIDIA"
  - "Boston Dynamics"
relatedSlugs:
  - "2026-06-07-byd-humanoid-robot-yao-shun-yu-en"
  - "2026-06-05-nvidia-cosmos-3-physical-ai-omnimodel-en"
---

The humanoid robot industry has spent years promising factory-floor deployments, automotive assembly lines, and warehouse automation. In the spring of 2026, at least one company has stopped promising and started shipping — at a pace that would have seemed implausible eighteen months ago.

Figure AI's BotQ facility in San Jose, California has ramped production of its Figure 03 humanoid robot from one unit per day to one per hour. The 24-fold output increase was achieved in under four months, making BotQ the most productive humanoid robot factory in the world. The company is targeting 12,000 units annually, with production velocity still increasing.

## Inside BotQ

BotQ — shorthand for "Bot Quality" — is Figure's purpose-built manufacturing complex, a departure from the contract manufacturing arrangements most robotics startups use for initial production runs. Figure built BotQ to own the full manufacturing stack: component sourcing, assembly, quality inspection, software flashing, and final testing all happen under one roof, with over 150 networked workstations tracking every unit through each stage.

The ramp was not smooth. Early in 2026, BotQ was producing roughly two to three units per week, with high reject rates at final inspection related to actuator calibration drift and harness routing failures. Figure addressed the calibration issue by integrating an automated in-line calibration step that runs each joint through a full range-of-motion test before the robot leaves the assembly cell. Harness routing was standardized through a combination of jigs and torque-spec software that eliminated technician variability.

By March, daily output had reached three units. By May, the company crossed ten units per day. The current rate of one per hour — approximately 720 units per month — is the result of a manufacturing learning curve that compressed what other industries took years to achieve into months.

## The Figure 03 Platform

Figure 03 is the company's third-generation commercial humanoid, powered by the Helix AI system — a multimodal model trained on human demonstration data that enables the robot to interpret natural language instructions, recognize objects and spatial relationships, and plan multi-step manipulation tasks without explicit programming for each action type.

The robot stands 5'6" and weighs 140 pounds. It can lift 55 pounds, walk at 2.7 miles per hour, and operate for approximately four hours on a single charge. Its hands, redesigned from the Figure 02 generation, have improved finger dexterity that allows it to handle objects as small and irregular as loose screws or crumpled material — a capability essential for the assembly and warehouse tasks that represent Figure's primary commercial markets.

Current customers include BMW, which deployed Figure 03 units at its Spartanburg, South Carolina plant for body-shop material handling tasks, and an unnamed logistics operator running a proof-of-concept in a cold storage distribution center. Figure has disclosed a revenue pipeline exceeding $14 billion through 2029 based on customer letters of intent, with Amazon and Mercedes cited as parties to major forward commitments.

## The Manufacturing Milestone's Deeper Significance

Figure framed the production ramp explicitly as more than a manufacturing achievement. "This 24x increase represents more than just manufacturing efficiency — it is a fundamental shift in our development velocity," the company wrote in its BotQ update. The logic is that each deployed robot generates proprietary operational data — real-world manipulation sequences, failure modes, edge-case object recognition challenges — that feeds back into Helix AI model training.

At one unit per day, the data pipeline was narrow. At one unit per hour, Figure deploys roughly 720 robots per month into operational environments, each generating continuous behavioral data. The compounding effect of that data on model quality creates a flywheel that pure-software AI companies have used to build durable advantages — and Figure is betting the same dynamic applies to physical AI.

This is the core thesis of the physical AI investment thesis driving 2026's humanoid robot funding boom. The companies that scale hardware production fastest will accumulate the richest behavioral datasets, enabling model improvements that make their robots more capable in ways that are difficult to replicate from synthetic data alone.

## The Broader Race

Figure's milestone lands in an industry experiencing unprecedented consolidation of attention and capital. Boston Dynamics began shipping initial units of its electric Atlas robot to Hyundai and Google DeepMind in the current quarter — the first commercial deployment of a fully electric Atlas after decades of hydraulic systems. Atlas carries a significantly higher price point than Figure 03 but is designed for more extreme industrial applications, including environments where explosion-proofing or high-temperature tolerance is required.

NVIDIA extended its physical AI platform strategy at Computex with the announcement that it has selected Chinese startup Unitree as the first robotics platform it will distribute directly to research institutions — Stanford, ETH Zurich, and others. The Unitree H2 Plus, powered by NVIDIA Jetson Thor, will be available in October. The selection signals that NVIDIA views Unitree's price-to-capability ratio — roughly $25,000 per unit compared to Figure's enterprise pricing above $150,000 — as optimal for research applications where deployment cost matters more than production grade.

Chinese manufacturers remain the most aggressive on volume. Robotera disclosed a funding round exceeding $200 million in May and reported production growth above 300% during Q2 2026. Unitree, UBTECH, and several newer entrants are scaling logistics and industrial deployments in ways that give Chinese manufacturers a data advantage in the world's largest manufacturing economy.

## What Comes After Scale

The question the industry hasn't fully answered is what happens when humanoid robot production achieves automotive-style scale — tens of thousands of units per quarter rather than per year. At that point, the competitive dynamics shift from manufacturing capability to software capability: which company's robot can learn new tasks fastest, generalize across the widest range of environments, and fail gracefully when it encounters conditions outside its training distribution.

Figure has argued its data flywheel gives it an advantage on that second question. Boston Dynamics argues its decades of locomotion research provide a mechanical robustness baseline that newer entrants can't replicate quickly. NVIDIA is positioning itself as the neutral infrastructure provider — the GPU company of physical AI — that wins regardless of which humanoid OS wins.

For the first time, the argument is not theoretical. At one robot per hour, humanoid manufacturing has arrived. The race to determine which company's robots will outnumber humans on factory floors is now primarily a software contest dressed in hardware clothing.
