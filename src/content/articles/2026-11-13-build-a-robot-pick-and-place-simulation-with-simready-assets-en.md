---
category: developer-tools
faqs:
- answer: It builds a beverage-can pick-and-place scene in Isaac Sim using a UR17G
    arm, a Robotiq gripper, and SimReady object assets. The workflow checks asset
    behavior and runs the task with agent-generated controls.
  question: What does the walkthrough actually demonstrate?
- answer: A SimReady asset includes authored physical and control properties such
    as mass, collisions, joints, and drives. Developers can therefore reuse more of
    a working simulation setup instead of configuring every downloaded model from
    scratch.
  question: Why do SimReady assets matter for robotics developers?
- answer: The walkthrough demonstrates that the assets and controls work in simulation,
    not that the same behavior transfers reliably to physical hardware. Real-world
    validation, cross-simulator consistency, and broader task coverage remain important
    tests.
  question: What remains unproven after this demo?
featured: false
lang: en
publishedAt: '2026-11-13T18:00:39+00:00'
relatedSlugs: []
safeForPublic: true
sources:
- name: Hugging Face Blog
  url: https://huggingface.co/blog/nvidia/simready-assets-robot-pick-and-place
summary: SimReady’s real breakthrough is not another robot demo, but reusable simulation
  assets that could make robotics experimentation faster and less fragile.
tags:
- developer-tools
- open-source
- ai-ml
title: Build a Robot Pick-and-Place Simulation with SimReady Assets
trending: false
type: news
---

SimReady’s real breakthrough is not another robot demo, but reusable simulation assets that could make robotics experimentation faster and less fragile.

## Key points

- The walkthrough assembles a UR17G robot arm, Robotiq gripper, and beverage can in Isaac Sim for a pick-and-place task using agent-generated controls.
- SimReady assets include simulation properties such as collisions, mass, joints, and joint drives instead of providing visual geometry alone.
- SimReady Central on Hugging Face offers an open library of reusable robot and object assets alongside profile-validation evidence.
- SimReady Foundation organizes compatibility through profiles, features, and testable requirements, creating a clearer contract between asset creators and simulation users.
- The larger implication is that standardized assets can reduce repetitive scene preparation, although the tutorial demonstrates simulation rather than transfer to a physical robot.

## Why it matters

Robotics AI does not mainly need flashier agents; it needs boring, validated assets that stop every team from rebuilding mass, collision, and joint settings from scratch.

## Sources

- [Hugging Face Blog](https://huggingface.co/blog/nvidia/simready-assets-robot-pick-and-place)