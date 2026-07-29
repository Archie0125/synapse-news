---
title: "Anthropic's Claude Mythos Cracks Post-Quantum Cipher in 60 Hours That Stumped Humans for Two Years"
summary: "Anthropic published research showing its Claude Mythos Preview model autonomously discovered two significant cryptographic weaknesses: a key-recovery attack that halves the effective strength of HAWK, a leading post-quantum signature candidate, and a novel 'Möbius Bridge' technique that speeds up attacks on a reduced version of AES by 200-800x. Neither affects production systems, but both represent a qualitative advance in AI-driven cryptanalysis."
category: "ai-ml"
publishedAt: 2026-07-29
lang: "en"
featured: false
trending: false
sources:
  - name: "Anthropic Research"
    url: "https://www.anthropic.com/research/discovering-cryptographic-weaknesses"
  - name: "The Hacker News"
    url: "https://thehackernews.com/2026/07/claude-ai-just-cracked-post-quantum.html"
  - name: "Decrypt"
    url: "https://decrypt.co/374600/claude-mythos-cracked-post-quantum-cryptography"
  - name: "The Quantum Insider"
    url: "https://thequantuminsider.com/2026/07/29/ai-finds-new-weaknesses-in-cryptographic-algorithms-anthropic-says/"
tags:
  - "Anthropic"
  - "Claude"
  - "cryptography"
  - "post-quantum"
  - "HAWK"
  - "AES"
  - "AI-research"
  - "security"
relatedSlugs:
  - "2026-07-26-anthropic-claude-opus-5-launch-en"
  - "2026-07-07-jadepuffer-autonomous-ai-ransomware-en"
---

Anthropic published research on Monday showing that its Claude Mythos Preview model — an unreleased internal research variant of Claude — autonomously discovered two previously unknown weaknesses in widely studied cryptographic algorithms. The findings, published through Anthropic's Frontier Red Team research program and coordinated in advance with NIST and government partners, represent what may be the clearest demonstration yet that AI is becoming a genuine force in offensive cryptanalysis.

Neither finding affects production systems. But together they establish that an AI system can, given sufficient autonomy and compute, compress years of expert cryptographic research into days — and invent techniques that human researchers did not.

## Cracking HAWK in 60 Hours

HAWK is a post-quantum digital signature scheme that has been undergoing scrutiny as part of NIST's multi-year review of post-quantum cryptographic standards. Human experts spent roughly two years stress-testing HAWK's security properties without finding a meaningful structural flaw. Claude Mythos Preview did it in approximately 60 hours, at an API cost of around $100,000.

The attack targets the smallest parameter set, HAWK-256, and reduces its effective key strength from approximately 2^64 operations to 2^38. That is a reduction of about 67 million times in the effort required to recover a private key — the difference between an attack that is computationally infeasible for any adversary and one that is, in principle, tractable with access to significant computational resources.

The mechanism of the attack is technically sophisticated. HAWK's security rests on the hardness of problems in structured lattices. Prior work had established that if an efficient nontrivial automorphism (a mathematical symmetry) could be found within HAWK's specific lattice structure, it would enable a key-recovery attack — but researchers had been unable to determine whether such an automorphism existed. Mythos found one. Once the symmetry was identified, it enabled faster enumeration of the key space, though the attack remains exponential in nature rather than polynomial.

One researcher managed the HAWK discovery work; another built a separate scaffold for the AES research. The total token output for the HAWK work was substantially smaller than the AES effort.

HAWK has not been deployed in any production system. It remains a candidate under NIST review — review that was already underway specifically to find attacks like this before standardization. Anthropic's disclosure gives NIST and the cryptographic community time to assess the impact before any deployment decision is made.

## Inventing the Möbius Bridge

The AES finding is, in some ways, more remarkable. AES — the Advanced Encryption Standard — is the most widely deployed symmetric cipher in the world, and breaking it is a foundational problem of cryptography. The full 10-round version of AES-128 remains unbroken; the research targets a 7-round reduced variant that cryptographers study specifically to develop attack intuitions.

Mythos spent three days working autonomously on the 7-round AES-128 problem, generating approximately one billion output tokens at a total API cost of around $100,000. The model initially expressed skepticism about its chances: in one notable exchange, it stated "If you want a different outcome, the target has to change … AES-128 r5/r6 is just genuinely hard." A researcher encouraged it to pursue novel approaches rather than incremental improvements on existing known methods. The model then developed what it called the Möbius Bridge.

The Möbius Bridge is a fingerprinting algorithm that works by becoming invariant to certain guesses an attacker would otherwise need to make. In concrete terms, it eliminates one of the guesses in a particular attack stage — reducing that stage from 2^56 operations to a single computation — while accepting some computational overhead elsewhere. The net result is a 200 to 800 times improvement in attack speed against 7-round AES-128, depending on implementation parameters.

What makes this particularly notable is the validation problem it created. The model discovered the technique faster than human experts could verify it. Two researchers spent "several hundred hours" independently validating that the Möbius Bridge method is mathematically correct — and the overall research cycle of one week for discovery versus nearly a month for human validation illustrates a new challenge: AI-accelerated research may outrun human capacity to check its work.

Mythos also produced additional cryptanalytic results as side effects of these investigations: a practical attack on 13-round LEA completing in fewer than 230 encrypted plaintexts, and a full key-recovery attack on 6-round Serpent-128. These are not the headliners of the paper, but they suggest that Mythos was generating novel results across multiple attack surfaces simultaneously.

## What It Means — and What It Doesn't

Anthropic is explicit about the production impact: "Neither of these results has a practical impact on today's computer systems; no production software will have to change as a result." HAWK is undeployed. The 7-round AES attack does not apply to the full 10-round AES-128 used in TLS, disk encryption, and essentially every other real-world cryptographic application.

The framing Anthropic uses for the research is one of proactive stress-testing: this is what cryptographic review is supposed to do, and AI is now a powerful tool for doing it faster and at greater depth. "We coordinated with NIST and shared findings with government and industry partners before public release," the company notes — signaling that it sees this as a responsible component of the standardization process rather than a destabilizing disclosure.

But the broader implication deserves careful attention. The history of cryptography is one of asymmetric surprises: algorithms that appeared secure under human review proving vulnerable to novel attack techniques discovered unexpectedly. The timescales involved — two years of human expert attention versus 60 hours of AI-driven search — suggest that the rate at which AI can explore the attack surface of a cryptographic scheme is becoming incomparable to human review capacity.

What happens when that capability is applied to algorithms that are already deployed, at scale, in critical infrastructure? That question remains open. What the Mythos research does is sharpen it considerably.

For the cryptographic community, the immediate practical response is clear: standardization processes need to incorporate AI-assisted red-teaming as a standard phase, not an optional enhancement. NIST and its counterparts in other jurisdictions will need to decide how to integrate AI analysis into their review pipelines — and how to handle findings that arrive faster than human validators can confirm them.

For the AI safety community, the research is a data point in a different debate: about the gap between what AI systems can do in research settings and what their deployment in offensive contexts could enable. Anthropic's commitment to responsible disclosure and pre-publication coordination with NIST sets a clear norm. Whether that norm holds as AI cryptanalysis becomes more capable — and more widely accessible — is a harder question.
