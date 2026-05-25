---
title: "Google DeepMind's AlphaProof Nexus Solves 9 Decades-Old Erdős Problems for a Few Hundred Dollars Each"
summary: "Google DeepMind published a landmark arXiv paper on May 21 showing its AlphaProof Nexus agent autonomously proved 9 open Erdős problems and 44 OEIS conjectures using a combination of Gemini and Lean formal verification, at a cost of just a few hundred dollars per problem — reshaping what AI-assisted mathematical research looks like."
category: "ai-ml"
publishedAt: 2026-05-25
lang: "en"
featured: false
trending: true
sources:
  - name: "arXiv: Advancing Mathematics Research with AI-Driven Formal Proof Search"
    url: "https://arxiv.org/abs/2605.22763"
  - name: "The Rundown AI"
    url: "https://www.therundown.ai/p/google-tops-openai-math-breakthrough-9-to-1"
  - name: "GPUBeat"
    url: "https://gpubeat.com/google-deepmind-s-alphaproof-nexus-solves-erdos-problems/"
  - name: "Crypto Briefing"
    url: "https://cryptobriefing.com/deepmind-alphaproof-nexus-erdos-problems/"
tags:
  - "Google DeepMind"
  - "AlphaProof"
  - "mathematics"
  - "formal verification"
  - "Lean"
  - "Erdős"
  - "AI research"
relatedSlugs:
  - "2026-05-24-openai-erdos-conjecture-discrete-geometry-en"
  - "2026-05-19-google-io-2026-keynote-gemini-project-astra-android-xr-en"
---

When OpenAI announced last week that its AI had cracked a longstanding Erdős conjecture in discrete geometry, the mathematical community sat up. Within days, Google DeepMind answered with something significantly larger in scope: a new system called AlphaProof Nexus that has autonomously solved nine open problems from Paul Erdős's legendary list — two of which had been unsolved for 56 years — and proved 44 conjectures from the Online Encyclopedia of Integer Sequences (OEIS). The cost of this mathematical heavy lifting? A few hundred dollars per problem.

The results, published in an arXiv preprint (2605.22763v1) on May 21, 2026, represent the most comprehensive demonstration yet of AI's capacity to contribute original work to frontier mathematics — not just verify human proofs, but discover them.

## How AlphaProof Nexus Works

At its core, AlphaProof Nexus is an agentic system that marries two complementary technologies: the creative, pattern-recognizing power of a large language model and the unforgiving rigor of Lean, a formal proof verification language developed at Microsoft Research.

The architecture works in a closed loop. The LLM backbone — Gemini 3.1 Pro — proposes a proof strategy in natural language and pseudocode. That strategy is then translated into Lean's formal syntax and checked automatically by the verifier. If the proof fails, it is rejected outright; no hallucinated leaps are allowed to pass. The system then iterates, refining its approach based on the verifier's feedback.

What distinguishes AlphaProof Nexus from simpler generate-and-verify approaches is what DeepMind calls an "evolutionary search" layer. Rather than pursuing a single proof path, the agent maintains a population of partially-developed proof sketches. These sketches are evaluated by an Elo-style rating system — the same scoring mechanism used in chess — that promotes the most promising paths and prunes dead ends. This lets the system explore the proof space efficiently, even when the solution space is vast.

A third component, called AlphaProof (DeepMind's reinforcement learning-based olympiad theorem prover, introduced in 2024), operates as a specialized subagent. When the main system identifies a well-defined subgoal, it calls AlphaProof to attack it directly, combining the breadth of evolutionary search with the depth of targeted RL optimization.

The entire "Agent D" configuration — the full system with all three components active — was responsible for most of the breakthroughs in the paper.

## The Problems It Solved

Erdős was famous for offering cash prizes for unsolved problems in combinatorics and number theory, ranging from $25 to $10,000 depending on difficulty. His problem list, maintained after his death in 1996, has become a canonical benchmark for mathematical difficulty.

AlphaProof Nexus tackled 353 open problems from this list and solved 9 — roughly 2.5% of the total. While that may sound modest, researchers note that the problems it cracked were not the easiest ones. Among the nine:

**Problem #12(i)**, posed by Erdős and Sárközy in 1970 and open for 56 years, asks whether an infinite set with specific density and divisibility properties can exist. The system constructed a formal proof of existence using number-theoretic arguments that, once decoded into natural language, are described by reviewers as "genuinely sophisticated."

A second problem, also 56 years old, involves extremal graph theory — asking about the maximum density of a graph that avoids a specific subgraph pattern. AlphaProof Nexus produced a proof that tightened known bounds.

On the OEIS front, the system addressed 492 open conjectures — primarily about integer sequences that lack any known closed-form or structural explanation — and proved 44 of them. Several of these had been added to the OEIS database more than a decade ago with no progress until now.

All proofs, in both machine-readable Lean format and human-readable prose, have been published in a public GitHub repository maintained by DeepMind.

## The Economics of Mathematical Discovery

Perhaps the most startling aspect of the paper is not which problems were solved, but what it cost to solve them. DeepMind reports that inference costs for each problem ranged from roughly $100 to $500 — less than a graduate student's weekly stipend.

This shifts a fundamental economic assumption about research mathematics. Historically, mathematical discovery has been constrained by human attention: the number of brilliant researchers, their finite working hours, and the slow accumulation of intuition over careers. AlphaProof Nexus suggests a near-term world in which an AI system can ingest an entire corpus of open problems, run for a few hours on commodity cloud infrastructure, and return a batch of formally verified proofs.

Dr. Timothy Gowers, a Fields Medal winner at the University of Cambridge who was briefed on the results, noted that "the key word is *verified*. We're not talking about plausible arguments that might contain errors — these are machine-checked proofs of the same standard as any theorem in Lean's library." He added that while nine problems out of 353 is still a small fraction, "the fact that the hit rate is non-zero on genuinely hard problems changes the conversation."

## Context: A Two-Week Math War

The DeepMind result arrives in the context of what observers are calling a two-week "math war" between OpenAI and Google. On May 14, OpenAI announced that its internal reasoning system had resolved a conjecture in discrete geometry related to the Erdős–Ko–Rado theorem family, offering a surprising elementary proof that human combinatorialists had missed.

The AlphaProof Nexus paper, dated May 21, directly references OpenAI's result in its introduction — and goes considerably further both in scope (nine problems vs. one) and in the strength of its formal verification guarantees. "OpenAI's result was impressive," said one academic mathematician who reviewed both papers, "but it was a natural language argument that still requires peer review. AlphaProof Nexus outputs Lean proofs. There is no ambiguity about correctness."

DeepMind is careful not to frame this as competition. The paper's conclusion notes that "the research community has everything to gain from multiple groups independently attacking open problems with AI assistance" and calls for open benchmarks to standardize evaluation.

## What Comes Next

The immediate next steps, according to the paper, involve scaling to harder problems — those on the Millennium Prize list, for example — and improving the system's ability to formalize novel mathematical objects that don't yet have Lean representations.

Longer term, the team is exploring integration with DeepMind's Co-Scientist system, a multi-agent research assistant announced in May 2026 that generates and debates scientific hypotheses across life sciences. A combined system capable of proposing novel mathematical structures *and* formally verifying theorems about them would represent a qualitative shift in the relationship between human and machine mathematical cognition.

For now, the mathematical community is processing what it means that a system that cost roughly $500 to run has closed problems that sat open for more than half a century. As one DeepMind researcher put it: "We're not replacing mathematicians. We're giving them a very cheap, very tireless collaborator who never gives up on a subgoal."
