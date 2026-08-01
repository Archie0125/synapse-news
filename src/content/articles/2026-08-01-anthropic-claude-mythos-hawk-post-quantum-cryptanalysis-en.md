---
title: "Anthropic's Claude Mythos Cracks Post-Quantum Cipher in 60 Hours That Stumped Experts for Two Years"
summary: "Anthropic disclosed that its unreleased Claude Mythos Preview model discovered a structural weakness in HAWK, a post-quantum digital signature scheme under NIST standardization review, reducing the cost of key recovery attacks by a factor of 67 million — a landmark demonstration of AI-powered cryptanalysis that will reshape how the security community evaluates frontier AI risk."
category: "ai-ml"
publishedAt: 2026-08-01
lang: "en"
featured: false
trending: true
sources:
  - name: "The Hacker News — Claude AI Just Cracked a Post-Quantum Test Scheme"
    url: "https://thehackernews.com/2026/07/claude-ai-just-cracked-post-quantum.html"
  - name: "Anthropic Research — Discovering Cryptographic Weaknesses with Claude"
    url: "https://www.anthropic.com/research/discovering-cryptographic-weaknesses"
  - name: "CyberScoop — Anthropic's Claude Mythos Finds Weaknesses in Encryption Algorithms"
    url: "https://cyberscoop.com/anthropic-claude-mythos-encryption-flaws-hawk-aes-pqc/"
  - name: "Decrypt — Claude Mythos Cracked Post-Quantum Cryptography"
    url: "https://decrypt.co/374600/claude-mythos-cracked-post-quantum-cryptography"
  - name: "TechTimes — AI Cracks Post-Quantum Cipher in 60 Hours"
    url: "https://www.techtimes.com/articles/321876/20260728/ai-cracks-post-quantum-cipher-60-hours-after-two-years-human-review-failed.htm"
  - name: "CSO Online — Anthropic finds weakness in Hawk post-quantum digital signature algorithm"
    url: "https://www.csoonline.com/article/4202920/mythos-takes-its-first-shot-at-post-quantum-cryptography.html"
tags:
  - "Anthropic"
  - "Claude Mythos"
  - "post-quantum cryptography"
  - "HAWK"
  - "NIST"
  - "cryptanalysis"
  - "AI security"
relatedSlugs:
  - "2026-07-31-anthropic-claude-hacked-3-organizations-cyber-tests-en"
---

In a disclosure that sent ripples through both the AI safety and cryptography communities, Anthropic revealed on July 28 that its unreleased Claude Mythos Preview model had accomplished something that a global cohort of expert cryptanalysts had failed to do in two years: identify a meaningful structural weakness in HAWK, one of the leading candidates in NIST's ongoing post-quantum digital signature standardization process.

The announcement, published simultaneously as a research paper and a company blog post, describes how Anthropic researchers directed Claude Mythos to independently probe cryptographic algorithms for flaws. In approximately 60 hours of directed analysis — and at a cost of roughly $100,000 in API credits — the model discovered a previously overlooked symmetry in HAWK's mathematical foundation that dramatically reduces the computational cost of key recovery attacks.

The finding raises a question that policymakers, security architects, and AI researchers alike will be grappling with for months: if frontier AI models can break cryptographic schemes that survived years of expert scrutiny, what does that imply about the adversarial capabilities of the most powerful AI systems — and the security of the infrastructure that protects the internet?

## What HAWK Is, and Why It Matters

HAWK is a lattice-based digital signature scheme developed by a European academic consortium and submitted to NIST's Post-Quantum Cryptography standardization process. Unlike the RSA and elliptic-curve algorithms that secure the vast majority of today's encrypted communications — which would be broken by a sufficiently powerful quantum computer — HAWK is designed to remain secure even in a post-quantum world.

The NIST PQC standardization process, which has been running since 2016, is regarded as one of the most rigorous public cryptographic evaluations ever conducted. Submissions are subjected to years of open academic review, with leading cryptographers worldwide invited to probe for weaknesses. HAWK had survived this process intact through multiple rounds of review, with no exploitable structural vulnerabilities publicly documented.

That record is now partially qualified.

## The Attack: What Mythos Found

Anthropic's disclosure is careful with language, and appropriately so. The weakness Claude Mythos identified is real, mathematically verified, and novel — but its practical significance is bounded.

The model identified an unused symmetry in HAWK's signing and key generation process. By exploiting this symmetry, an attacker can reduce the cost of full key recovery for HAWK-256 (the smallest parameter set, intended for environments where performance matters more than maximum security) from approximately 2^64 operations to approximately 2^38 operations. That is a reduction in difficulty by a factor of roughly 67 million — from a computation that would take years on modern hardware to one theoretically feasible with substantial but not extraordinary resources.

The same vulnerability leaves HAWK-512 and HAWK-1024 — the larger parameter sets used in environments where security headroom is the priority — essentially unaffected. The attack against those configurations remains computationally infeasible.

Anthropic additionally disclosed that Claude Mythos found a faster attack on a seven-round reduced version of AES-128, though the company noted this improvement does not translate to any vulnerability in full AES-128, which uses ten rounds and remains one of the most battle-hardened symmetric encryption standards in existence.

## The Process: 60 Hours, $100,000, and an AI Doing the Work

The process Anthropic describes is almost more significant than the specific result. Researchers did not feed Claude Mythos a predetermined attack strategy to verify. They gave it access to HAWK's academic specification, existing cryptanalysis literature, and mathematical reasoning tools, then asked it to try to break the scheme.

The search, development, and verification of the HAWK attack took approximately 60 hours of compute time, consuming around $100,000 in API credits. Each of the two research threads — the HAWK work and the AES analysis — ran on similar budgets.

For context: the NIST PQC review process that failed to surface this vulnerability involved hundreds of the world's leading cryptographers working over multiple years. The cost differential is striking. Human expert time at that scale would easily total in the tens of millions of dollars; the AI equivalent ran in five figures.

Anthropic was explicit that the comparison is not a clean indictment of human cryptanalysts. The model had advantages they did not: it could enumerate potential attack strategies exhaustively and systematically in ways that exceed human endurance, and it could check mathematical derivations without fatigue-induced errors. But it also had limitations — it required significant human scaffolding to set up the task, and its output required extensive expert verification before Anthropic could publish with confidence.

## Industry and Policy Implications

The disclosure lands at an uncomfortable moment for both the AI safety and cryptographic standards communities.

For AI safety researchers, the finding substantiates concerns about what Anthropic's own published safety framework calls "cybersecurity-adjacent" model capabilities. The company had previously disclosed that its AI models had breached three organizations during internal testing; the HAWK result demonstrates a related but distinct category of risk — not the ability to exploit known vulnerabilities, but to discover previously unknown ones.

Anthropic stated explicitly that the results "do not affect production systems and do not require changes to deployed software." Full AES-128 is not broken. HAWK-512 and HAWK-1024 are not broken. The vulnerability found in HAWK-256 is a structural concern for standardization, not an immediate deployment emergency.

NIST has been notified and is expected to evaluate the finding as part of its ongoing standardization process. HAWK's submitters — researchers at CWI Amsterdam, Léo Ducas among them — acknowledged receipt of Anthropic's disclosure and said they would provide a technical response within the standard NIST comment period.

For the cryptographic community, the implications are more forward-looking than immediate. If a current-generation frontier model can find a novel attack on a scheme that survived two years of open expert review, what becomes possible when models are an order of magnitude more capable — or when adversarial actors deploy similar techniques without the ethical guardrails Anthropic has chosen to apply?

## The Dual-Use Problem at the Frontier

Anthropic's disclosure is a deliberate act of transparency in a space where secrecy would have been easier and arguably safer in the short term. The company argues — consistent with its longstanding public safety commitments — that surfacing AI's cryptanalytic capabilities now, while the impacts are bounded and manageable, gives the security community time to respond before more powerful models make the calculus harder.

That argument has real merit. The NIST PQC process exists precisely to stress-test candidate algorithms before they are deployed at internet scale. Discovering HAWK-256's weakness now, through a disclosed research collaboration, is categorically better than discovering it after deployment through an adversarial breach.

But the disclosure also demonstrates the dual-use tension at the heart of frontier AI development. The same capability that helps researchers find and fix cryptographic flaws before deployment could, in the hands of a state-level adversary operating a model of equivalent power without Anthropic's disclosure culture, be directed at algorithms already deployed at scale.

The race between algorithmic robustness and AI-powered cryptanalysis is now publicly acknowledged to be underway. NIST's post-quantum standardization process will need to incorporate AI-assisted review as a standard tool going forward — and the security community will need to decide whether AI models should be routinely deployed in adversarial probing of cryptographic candidates, with outputs shared openly, or whether the dual-use risk of that practice creates more problems than it solves.

That is a debate the field was not quite ready to have six months ago. Claude Mythos has forced it onto the agenda.
