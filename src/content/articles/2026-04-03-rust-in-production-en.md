---
title: "Rust in Production: The Companies That Made the Switch and What Actually Happened"
summary: "Discord rewrote their message store. Cloudflare replaced their C++ proxy. AWS built Firecracker. After years of hype, the real-world Rust migration data is finally in — and it's not all good news."
category: "developer-tools"
publishedAt: 2026-04-03T09:20:00Z
lang: "en"
featured: false
trending: false
sources:
  - name: "InfoQ"
    url: "https://www.infoq.com"
  - name: "GitHub Blog"
    url: "https://github.blog"
tags:
  - "rust"
  - "systems-programming"
  - "performance"
  - "developer-tools"
relatedSlugs: []
---

## The Hype Cycle Is Over. The Data Is In.

Rust has been the "most loved programming language" on Stack Overflow for eight years running. But loving a language and shipping production code in it are very different things.

In 2026, we finally have enough large-scale production Rust deployments to assess the real tradeoffs — not the theoretical ones, the actual engineering outcomes. The picture is more mixed than either Rust evangelists or skeptics want to admit.

## The Clear Wins

**Discord's message store rewrite** (Go → Rust): Tail latency dropped from 130ms to 5ms. Memory usage cut by 10x. The service handles 40 billion messages per day with fewer servers. This is Rust's home turf — high-throughput, low-latency data processing.

**Cloudflare's Pingora** (C++ → Rust): Replaced nginx as their proxy layer. 70% fewer memory safety bugs in the first year. Performance equivalent to C++ with dramatically better safety guarantees. New features ship faster because developers aren't debugging memory corruption.

**AWS Firecracker** (purpose-built in Rust): The microVM that powers Lambda and Fargate. Sub-200ms cold starts. The Rust type system prevents entire categories of security vulnerabilities that would be devastating in a multi-tenant VM host.

The pattern is clear: for **systems-level infrastructure** where performance and memory safety both matter, Rust delivers on its promises.

## The Honest Struggles

**Compile times are still painful.** A clean build of a large Rust project takes 10-30 minutes. Incremental builds are better (1-3 minutes) but still slower than Go or Java. For developer productivity, this matters more than benchmarks.

**Hiring is hard.** There are roughly 10x more Go developers than Rust developers in the job market. Companies report 2-3x longer time-to-hire for Rust positions and 20-30% salary premiums.

**The learning curve is real.** Teams report 3-6 months before new Rust developers become productive. The borrow checker, lifetimes, and ownership model are conceptually sound but practically challenging.

**Not everything needs Rust.** Several companies have publicly walked back Rust adoptions for web services and business logic where the safety guarantees don't justify the productivity cost. A CRUD API in Rust is more code, more complexity, and slower to develop than the same API in Go, Python, or TypeScript.

## Where Rust Makes Sense (and Doesn't)

**Strong fit**: Databases, networking infrastructure, embedded systems, crypto/security, game engines, OS components, high-frequency trading.

**Questionable fit**: Web backends, microservices, data pipelines, ML inference, DevOps tooling.

**Bad fit**: Rapid prototyping, short-lived scripts, areas where developer velocity matters more than runtime performance.

The wisdom is settling: Rust is the right tool for about 15-20% of software engineering work — the part where correctness and performance are non-negotiable. For the other 80%, faster languages (in developer time, not CPU time) are the better choice.

## What to Watch

- Linux kernel Rust adoption progress — if the kernel fully embraces Rust, the hiring pool will grow significantly
- AI-assisted Rust development — Claude and Cursor are getting remarkably good at writing Rust, which could lower the barrier
- The Rust Foundation's sustainability — corporate sponsors are critical, and some are pulling back
- Whether Rust eating into Go's territory in cloud infrastructure or if Go holds the line

*Rust is the best systems programming language ever created. It's also a terrible choice for most software. Both things are true, and accepting both is the beginning of wisdom.*
