---
title: "Mistral's Leanstral 1.5 Brings Formal Verification Within Reach — and Found 5 Previously Unreported Bugs"
summary: "Mistral has open-sourced Leanstral 1.5, a model under Apache 2.0 for proof engineering in Lean 4. On PutnamBench it costs roughly $4 per problem, against an estimated $300 or more for Seed-Prover 1.5, and it found five previously unreported bugs when tested against 57 open-source repositories."
category: "developer-tools"
publishedAt: 2026-07-12
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "Mistral AI"
    url: "https://mistral.ai/news/leanstral-1-5/"
  - name: "MLQ News"
    url: "https://mlq.ai/news/mistral-releases-leanstral-15-an-open-source-formal-verification-model-that-found-five-unknown-bugs/"
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/07/03/mistral-ai-releases-leanstral-1-5-an-apache-2-0-lean-4-code-agent-model-solving-587-of-672-putnambench-problems/"
  - name: "i-SCOOP"
    url: "https://www.i-scoop.eu/mistral-leanstral-1-5-formal-verification-within-reach-for-every-developer/"
tags:
  - "mistral"
  - "formal-verification"
  - "lean4"
  - "open-source"
  - "developer-tools"
  - "software-safety"
relatedSlugs:
  - "2026-07-12-openai-gpt56-sol-cycle-double-cover-proof-en"
---

For most software developers, formal verification has always been something that happens in the aerospace industry, in safety-critical automotive systems, or in the research papers of academics who have never shipped a product on a deadline. Mistral wants to change that. Mistral AI released Leanstral 1.5 under the Apache 2.0 license — an open-weights model purpose-built for proof engineering in Lean 4.

The headline claim is striking: when tested against 57 open-source software repositories, Leanstral found five previously unknown bugs, including one that caused crashes in debug mode and silent data corruption in release builds. Those are exactly the kinds of errors that escape conventional testing.

## What Formal Verification Actually Means

Conventional software testing works by running code against a set of inputs and checking that the outputs match expectations. It is inherently incomplete: you can test a million cases and still miss the one that breaks production. Formal verification takes a different approach. Instead of running code, it uses mathematical proof to establish that the code satisfies a given specification — not for a sample of inputs, but for all possible inputs.

The catch has always been that writing formal proofs is extraordinarily difficult and time-consuming. Lean 4, the proof assistant Leanstral is built for, is a powerful tool used primarily by academic mathematicians and a small community of formal methods engineers. Getting it to work on industrial code typically requires deep expertise in both the programming language and the proof assistant — a combination rare enough that it has kept formal verification out of most software development workflows.

Leanstral changes the equation by automating the proof-generation step.

## Model Architecture and Performance

Leanstral 1.5 is a mixture-of-experts model with 119 billion total parameters and 6.5 billion active parameters per token — a design that enables high capability at relatively low inference cost. The context window is 256,000 tokens, large enough to reason over substantial codebases. The weights are available on Hugging Face, and a free API endpoint named leanstral-1-5 is live.

The benchmarks are impressive across the board. On miniF2F — a standard test of formal mathematical reasoning — Leanstral saturates the benchmark, achieving 100%. On PutnamBench, a collection of problems from the William Lowell Putnam Mathematical Competition widely used to evaluate theorem-proving systems, Leanstral solved 587 out of 672 problems. No prior open model came close.

The cost advantage over proprietary alternatives is equally notable. For developers who want to experiment with formal verification without a dedicated research budget, this changes what is practical.

## Five Real Bugs in 57 Repositories

The most compelling evidence for Leanstral's practical utility comes not from benchmarks but from its performance on real code. Mistral tested the model against 57 open-source repositories, using a pipeline that translated Rust code into Lean 4 using the Aeneas translation tool, generated correctness properties, and attempted proofs of those properties.

The system found five previously unreported bugs. The most significant was an integer overflow in the zigzag decoding function within the `varinteger` library — a Rust crate for reading and writing variable-length integers. On input Std.U64.MAX, the expression (value + 1) overflowed, causing crashes in debug mode and silent corruption in release mode. The `varinteger` library had passed its full test suite without triggering the issue.

This is the type of edge case that testing and fuzzing would typically miss. The overflow only manifests for specific edge-case input values that a random or coverage-based test suite is unlikely to generate. Proving that the function is correct for *all* inputs would have revealed the gap — and Leanstral's proof attempt failed, which itself constitutes detection.

## The Lean 4 Ecosystem

The choice of Lean 4 as the target proof assistant is deliberate. Lean 4 occupies an unusual position: it is both a functional programming language and a proof assistant, meaning that programs written in Lean 4 can themselves carry mathematical proofs of their correctness. The language has attracted growing interest from mathematicians following DeepMind's use of it in AlphaProof, and Microsoft Research has invested heavily in its development.

Leanstral integrates natively with Mistral Vibe, the company's agentic coding platform, making it possible to invoke formal verification as part of a standard development workflow rather than as a separate, specialized step. The model also supports *test-time scaling* — the more compute you allocate to a given proof search, the better results it achieves. On PutnamBench, scaling from 50,000 tokens to 4 million tokens improved performance from 44 solved problems to 587.

## What This Means for Software Quality

Formal verification has historically followed the Pareto principle in the wrong direction: it takes roughly 80% of the effort to verify the last 20% of the code, making complete verification of large systems economically impractical. The realistic near-term use case for Leanstral is not full program verification but *targeted* verification of high-value code paths — cryptographic routines, parser implementations, arithmetic operations on untrusted inputs, protocol state machines.

These are precisely the code areas where the gap between test coverage and actual correctness matters most, and where bugs tend to have the highest impact. An integer overflow in a variable-length integer codec is exactly the kind of thing that turns into a CVE two years after it ships.

For open-source maintainers, Leanstral offers a practical argument for exploring formal verification: a free API, Apache-licensed weights, and a demonstrated ability to find bugs that some traditional methods overlook. The barrier is no longer cost or access — it is learning enough Lean 4 to write the specifications that the model will attempt to prove.

That last step remains non-trivial. Leanstral automates proof generation, but someone still needs to write a specification that accurately captures what the code should do. If the specification is wrong or incomplete, the proof is correct for the wrong property. This is the fundamental challenge of formal verification that no model can fully automate: the intelligence needed to define "correct" in the first place.

Still, for the category of bugs Leanstral caught — arithmetic overflow, boundary conditions, off-by-one errors — the specifications are often straightforward enough that the automation is genuinely useful. Five previously unreported bugs found across 57 repositories is a result that should interest any team maintaining performance-critical or security-sensitive code.

## Open Source as Strategy

The Apache 2.0 license is worth dwelling on. Mistral has made a consistent bet on open-source as a business strategy, and Leanstral continues that pattern. By releasing model weights under a permissive license, Mistral makes the model available for commercial deployment, enterprise fine-tuning, and research use without restrictions — differentiating it from the closed proprietary alternatives that are cheaper per API call but cannot be self-hosted or customized.

For formal verification in regulated industries — finance, healthcare, aerospace — the ability to run verification workloads on-premises rather than through a third-party API may be the deciding factor. Leanstral's open license makes that possible in a way that its competitors' models do not.

The model's release arrives in the same week as OpenAI's GPT-5.6 Sol claimed a formal proof of the Cycle Double Cover Conjecture. That the two most significant formal reasoning announcements in recent memory arrived within days of each other is either coincidence or a signal about where the frontier is moving. Either way, formal verification — once the province of specialists — is increasingly within reach of anyone with a terminal.

*Correction (November 15, 2026): 9 sentences were corrected or removed to match the sources listed on this page.*
