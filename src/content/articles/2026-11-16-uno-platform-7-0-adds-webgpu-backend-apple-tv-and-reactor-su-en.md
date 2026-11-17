---
category: developer-tools
faqs:
- answer: Uno Platform 7.0 renders all targets through a single SkiaSharp 4 pipeline,
    adds an experimental WebGPU backend and Apple TV support, and supports .NET 11
    from day zero. It also removes native rendering and Mac Catalyst.
  question: What are the biggest changes in Uno Platform 7.0?
- answer: The Uno team reports that 7.0 is about 2x faster at the median and 5x smaller
    than version 6.7, with some operations such as brush creation up to 38x faster.
    These are vendor benchmarks, and the workloads were not published in detail.
  question: How much faster is Uno Platform 7.0?
- answer: The WebGPU backend gave up to a 50% frame-rate improvement in the team's
    tests, depending on the scene, and a WebGPU-only app drops about 6 MB of uncompressed
    native code from WebAssembly builds. Developers can also issue their own WebGPU
    commands inside the UI through a new WebGpuCanvasElement.
  question: Why does the WebGPU backend matter for .NET developers?
featured: false
lang: en
publishedAt: '2026-11-16T09:00:00+00:00'
relatedSlugs: []
safeForPublic: true
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/Uno-Platform-6-7-targets/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
summary: Uno Platform 7.0 bets everything on Skia and WebGPU and drops native rendering.
  Cross-platform .NET is choosing consistency over native feel.
tags:
- developer-tools
- open-source
title: Uno Platform 7.0 Adds WebGPU Backend, Apple TV and Reactor Support, and Retires
  Native Rendering
trending: false
type: news
---

Uno Platform 7.0 bets everything on Skia and WebGPU and drops native rendering. Cross-platform .NET is choosing consistency over native feel.

## Key points

- Every target now renders through one pipeline built on SkiaSharp 4, with an experimental WebGPU backend; native rendering and Mac Catalyst have been removed.
- The team says 7.0 is about 2x faster at the median and 5x smaller than 6.7, but these are vendor benchmarks without detailed workloads.
- WebGPU delivers up to a 50% frame-rate gain depending on the scene and trims about 6 MB of native code from WebAssembly builds.
- Apple TV becomes a new target, .NET 11 is supported from day zero, and Microsoft.UI.Reactor plus third-party MAUI controls now work on every target.
- Uno co-maintains SkiaSharp with Microsoft's .NET team, which puts it closer to the center of the .NET UI ecosystem.

## Why it matters

Dropping native rendering is the boldest call in Uno 7.0. Flutter showed that owning the pixels beats wrapping native widgets, and .NET is finally acting on that lesson.

## Sources

- [InfoQ](https://www.infoq.com/news/2026/11/Uno-Platform-6-7-targets/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global)