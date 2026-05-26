---
title: "10,000 Qubits Could Break Internet Encryption: How Quantum Computing Upended the Timeline for Cryptographic Collapse"
summary: "A March 2026 paper from Oratomic, Caltech, and UC Berkeley shook the cryptography world by showing that Shor's algorithm could crack RSA-2048 and elliptic-curve encryption with as few as 10,000 neutral-atom qubits — a tenfold improvement over previous estimates. Nature called it 'a real shock.' With Q-Day now a plausible 2030 milestone, organizations face a narrowing window to migrate to post-quantum cryptography before years of intercepted data become readable."
category: "hardware"
publishedAt: 2026-05-26
lang: "en"
featured: false
trending: true
sources:
  - name: "Nature"
    url: "https://www.nature.com/articles/d41586-026-01054-1"
  - name: "Science News"
    url: "https://www.sciencenews.org/article/quantum-bits-crack-internet-encryption"
  - name: "CoinDesk"
    url: "https://www.coindesk.com/markets/2026/03/31/quantum-computers-could-break-crypto-wallet-encryption-with-just-10-000-qubits-researchers-say"
  - name: "Quantum Pirates (Substack)"
    url: "https://quantumpirates.substack.com/p/rsa-will-die-oratomic-and-caltech"
tags:
  - "quantum computing"
  - "cryptography"
  - "RSA"
  - "encryption"
  - "cybersecurity"
  - "post-quantum"
  - "Shor's algorithm"
relatedSlugs:
  - "2026-05-22-us-quantum-computing-2b-grants-ibm-en"
  - "2026-05-25-github-nx-console-teampcp-supply-chain-attack-en"
---

On March 31, 2026, researchers from Oratomic, Caltech, and UC Berkeley published a paper that landed in the cryptography community like a depth charge. Its title — "Shor's algorithm is possible with as few as 10,000 reconfigurable atomic qubits" — understated the magnitude of what it implied. In two pages of clear language followed by dense technical appendices, the team showed that the mathematical wall between today's quantum computers and the encryption protecting the internet was far thinner than almost anyone had assumed.

Nature covered it the following week under a headline that captured the expert reaction precisely: "It's a real shock."

## What Changed: From Millions to Thousands

To understand why this matters, some background. RSA and elliptic-curve cryptography (ECC) — the encryption schemes that protect banking transactions, government communications, software update signatures, and essentially every secure connection on the internet — derive their security from the computational intractability of certain mathematical problems. For a classical computer, factoring a 2048-bit RSA key would take longer than the age of the universe. For a quantum computer running Shor's algorithm, the same task becomes feasible.

The catch, until this year, was that Shor's algorithm at cryptographically relevant scales was believed to require millions of physical qubits — far beyond what any existing or near-term quantum machine could provide. The largest publicly disclosed quantum processors as of early 2026 have between 1,000 and 4,000 physical qubits, with significant error rates that make long computations unreliable. Millions of qubits felt safely remote.

The Oratomic paper demolished that comfort zone. Using neutral-atom qubits — a technology in which individual atoms are suspended by laser light and moved around to create connections between any pair — the team showed that architectural efficiency gains could compress the qubit requirement dramatically. For ECC-256, the elliptic-curve variant that protects most cryptocurrency wallets and many government systems, space-efficient architectures require roughly 9,700 to 11,000 physical qubits. For RSA-2048, 11,000 to 13,300 physical qubits suffice under the space-efficient model, or approximately 102,000 under a more parallelized, time-efficient approach.

Tenfold improvement over previous estimates. For the same day that the paper appeared, a separate white paper from a Google Quantum AI team reached similar conclusions through a different analytical path, independently corroborating the Oratomic results. When two groups arrive at the same uncomfortable finding from different directions, the signal is not noise.

## Harvest Now, Decrypt Later: The Threat That Is Already Active

The natural response to hearing that Q-Day — the day a quantum computer first cracks a cryptographically relevant key — might arrive by 2030 is to assume there is time to address it. That assumption is wrong, and understanding why is essential to grasping the urgency.

Nation-state intelligence agencies and sophisticated criminal organizations have been collecting encrypted internet traffic for years with the explicit intention of decrypting it once quantum hardware crosses the necessary threshold. This strategy, known as "harvest now, decrypt later," means that any communication encrypted today with RSA or ECC is potentially sitting in an adversary's database, waiting. The data that matters — diplomatic cables, military communications, proprietary research, private medical records, financial histories — has a shelf life measured in decades, far longer than the gap between now and 2030.

This is not theoretical. The NSA's MUSCULAR program and similar operations disclosed through historical leaks demonstrated that bulk interception of encrypted traffic at scale is operationally feasible. The Oratomic and Google papers did not create this threat; they compressed the timeline for when it materializes into a decryption capability.

## What Is at Risk, Specifically

RSA and ECC are not niche technologies. They underpin:

**TLS/HTTPS**: Every secure web connection, from online banking to corporate VPNs to government portals, relies on RSA or ECC for the key exchange that establishes encryption. Breaking RSA or ECC retroactively breaks every stored session negotiated using those algorithms.

**Code signing**: Software updates from Microsoft, Apple, Google, and essentially every major vendor are authenticated with digital signatures based on ECC or RSA. A quantum adversary capable of forging these signatures could distribute malware that the operating system accepts as legitimate.

**Cryptocurrency**: Bitcoin's wallet addresses derive from ECC-256 keys. An attacker with a quantum computer capable of running Shor's algorithm could, in principle, derive private keys from public addresses and drain wallets — not just future transactions, but wallets that have ever exposed their public key in a transaction.

**PKI infrastructure**: Certificate authorities that anchor trust for the internet's identity systems, government identity documents in countries that have adopted cryptographic identification, and enterprise zero-trust architectures all depend on the same mathematical assumptions now under scrutiny.

## The Post-Quantum Response: NIST's Standards

The cryptographic community has not been idle. The National Institute of Standards and Technology (NIST) spent eight years evaluating post-quantum cryptographic algorithms and finalized its first three standards in 2024: CRYSTALS-Kyber (now ML-KEM) for key encapsulation, CRYSTALS-Dilithium (ML-DSA) for digital signatures, and SPHINCS+ (SLH-DSA) as a hash-based signature backup. A fourth standard, FALCON (FN-DSA), followed. These algorithms are believed to be resistant to attacks from both classical and quantum computers.

The challenge is migration, not invention. Replacing cryptographic primitives across a large organization's infrastructure is an operation that typically takes years of planning, testing, and rollout. Every library, protocol, hardware security module, and certificate that uses RSA or ECC must be inventoried, replaced, and validated. For enterprises running legacy systems on mainframes or embedded in industrial control equipment, the complexity is compounded by hardware that may not support software updates at all.

The US government's migration deadline — set by CISA in guidance that accompanied NIST's final standards — calls for federal agencies to complete the transition to post-quantum cryptography by 2030. For systems that handle classified information, the deadline is earlier. The Oratomic paper's compression of the qubit timeline has added urgency to what was already an aggressive schedule.

## The Hardware Reality Check

One piece of context that should not be lost: the Oratomic paper describes what a quantum computer could do if it achieves 10,000 high-quality, error-corrected logical qubits. The word "logical" is load-bearing. Physical qubits are noisy; logical qubits are the error-corrected version, typically requiring anywhere from dozens to hundreds of physical qubits each to implement reliably, depending on the error rate and correction scheme.

Current neutral-atom machines from companies including Atom Computing, QuEra, and Oratomic's own hardware division have demonstrated high-fidelity two-qubit gates, but operating 10,000 physical qubits with the error rates required for sustained Shor's algorithm execution remains a significant engineering challenge. The Oratomic paper is a resource analysis — it tells us what goal the hardware must hit, not that the goal has been hit.

What makes the paper alarming is the trajectory. Neutral-atom systems have improved faster than most projections suggested they would. The companies advancing this technology are well-funded, and the physics of the neutral-atom architecture scales more favorably than superconducting qubits in several respects. The 2030 timeline for Q-Day is not a certainty, but it is no longer a fantasy.

## The Clock Is Running

For enterprise security teams and government officials, the Oratomic paper should reframe the post-quantum cryptography migration from a long-range planning exercise into an active project with a hard deadline. The question is not whether quantum computers will eventually become capable of breaking RSA and ECC. The question is whether they will do so before the world has replaced those algorithms.

The gap between today's largest quantum computers and the 10,000-logical-qubit threshold is real, but it is no longer the comfortable buffer that previous estimates implied. Organizations that treat 2030 as a distant horizon rather than an imminent deadline are making a risk calculation that the Oratomic and Google papers have fundamentally changed.

As one cryptographer quoted in the Nature piece put it, the question is now "not if, but when." And when matters a great deal when the data being protected was encrypted years ago, is already in someone else's database, and will remain sensitive for decades to come.
