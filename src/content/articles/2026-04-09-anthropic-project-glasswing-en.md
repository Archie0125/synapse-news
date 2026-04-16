---
title: "Anthropic's Claude Mythos Is Too Dangerous to Release. So It Built Project Glasswing Instead."
summary: "Anthropic has launched Project Glasswing, a restricted cybersecurity initiative giving 40+ elite organizations access to Claude Mythos Preview — a frontier model Anthropic considers too powerful to release publicly. The model has already identified thousands of zero-day vulnerabilities in every major operating system and browser, some dormant for decades, raising urgent questions about the dual-use nature of advanced AI."
category: "ai-ml"
publishedAt: 2026-04-09T09:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "Anthropic"
    url: "https://www.anthropic.com/glasswing"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/anthropic-says-its-most-powerful-ai-cyber-model-is-too-dangerous-to-release"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-latest-ai-model-identifies-thousands-of-zero-day-vulnerabilities-in-every-major-operating-system-and-every-major-web-browser-claude-mythos-preview-sparks-race-to-fix-critical-bugs-some-unpatched-for-decades"
  - name: "CrowdStrike"
    url: "https://www.crowdstrike.com/en-us/blog/crowdstrike-founding-member-anthropic-mythos-frontier-model-to-secure-ai/"
  - name: "Fortune"
    url: "https://fortune.com/2026/04/07/anthropic-claude-mythos-model-project-glasswing-cybersecurity/"
tags:
  - "Anthropic"
  - "Claude Mythos"
  - "Project Glasswing"
  - "cybersecurity"
  - "zero-day"
  - "AI safety"
  - "frontier AI"
relatedSlugs:
  - "2026-04-06-anthropic-claude-mythos-en"
  - "2026-04-05-anthropic-claude-mythos-en"
  - "2026-04-06-anthropic-emotion-vectors-en"
---

The existence of Claude Mythos became public knowledge in late March, when a misconfigured content management system at Anthropic accidentally exposed internal documents describing a model the company called "by far the most powerful AI we have ever developed." Anthropic confirmed the leak, acknowledged training was complete, and said little else. On April 7, the company finally explained what it intends to do with the model — and the decision is unlike anything a major AI lab has done before.

Anthropic is not releasing Claude Mythos to the public. It is not even releasing it to paying Claude customers. Instead, it has launched Project Glasswing, a closed consortium of more than 40 organizations — including Amazon, Microsoft, Apple, Google, Cisco, CrowdStrike, Palo Alto Networks, and the Linux Foundation — given restricted access to what Anthropic is calling Claude Mythos Preview. The mission: use the model's extraordinary capabilities to find and fix software vulnerabilities before malicious actors can exploit them.

The reasoning behind the decision is stark. Newton Cheng, Anthropic's Frontier Red Team Cyber Lead, told VentureBeat: "We do not plan to make Claude Mythos Preview generally available due to its cybersecurity capabilities." The implication, spelled out clearly in Anthropic's Project Glasswing documentation, is that the model is sophisticated enough to identify and exploit vulnerabilities faster and more comprehensively than any human security researcher — and that this capability, unconstrained, would be catastrophically dangerous in the wrong hands.

## What the Model Found

The scope of what Claude Mythos Preview has already discovered in testing is difficult to fully absorb. Anthropic used the model, in a controlled internal environment, to scan the codebases of every major operating system and every major web browser. The result: thousands of high-severity zero-day vulnerabilities — previously unknown security flaws that attackers could, in principle, exploit immediately.

Among the discoveries were bugs that had existed undetected for years. The most striking: a 27-year-old vulnerability in OpenBSD, one of the security-focused operating systems most trusted by enterprises and infrastructure operators. A flaw of that vintage, in a system explicitly designed for security, surviving undetected for nearly three decades, suggests that the scale of undiscovered vulnerabilities in production software may be vastly larger than the industry has assumed.

The vulnerabilities span the full stack — kernel-level issues in operating systems, parsing flaws in browser engines, memory safety errors in foundational libraries. Project Glasswing partner organizations are now in a coordinated race to triage and patch the disclosed vulnerabilities before the information reaches adversaries. Several are reportedly working on emergency patches already.

Claude Mythos Preview scores 93.9% on SWE-bench Verified, a benchmark measuring AI's ability to resolve real software engineering issues — the highest score of any model publicly reported. It is also 4.9 times more token-efficient than Claude Opus 4.6, its public-tier predecessor. The efficiency gain matters for a use case like Glasswing: scanning millions of lines of code requires sustained, large-scale inference.

## The Consortium Structure

Project Glasswing operates under a tiered access model. Twelve "founding partners" — including CrowdStrike, Amazon, Apple, and Microsoft — receive full access to Mythos Preview for active defensive security work. The broader consortium of 40+ organizations gains access for research, validation, and targeted scanning of their own codebases. Anthropic has committed $100 million in model usage credits to Project Glasswing, with member organizations contributing additional usage.

The Linux Foundation's involvement is particularly notable: its role is to coordinate vulnerability disclosure and patch development for open-source projects that lack the resources of a large enterprise security team. The open-source ecosystem, which underpins virtually all production software, is statistically among the most vulnerable to undiscovered bugs — and among the hardest to patch quickly without coordinated infrastructure.

CrowdStrike, in a blog post confirming its founding membership, described Claude Mythos Preview as "a step change in autonomous vulnerability discovery" and noted that the model had already helped identify critical flaws in software running on its own sensor infrastructure.

## The Dual-Use Dilemma at Its Sharpest

Project Glasswing represents Anthropic's attempt to thread an almost impossible needle. The company has built what it believes is the most capable AI system ever developed for cybersecurity tasks — and its response is to keep it out of general circulation entirely. This is a significant departure from the conventional commercial AI model, where new capability is rapidly productized and monetized.

The decision will be tested hard. The cybersecurity community broadly understands that offensive and defensive capabilities are not cleanly separable — the same model that finds a vulnerability can be prompted to write an exploit for it. Restricting Mythos Preview to vetted organizations with contractual disclosure obligations creates a meaningful barrier, but not an insurmountable one. What happens when a Glasswing partner is itself breached, or when an employee leaves and takes knowledge of the model's capabilities with them, is an open question.

There are also questions about scope creep. Project Glasswing is framed as a defensive initiative, but several of its founding partners — Amazon, Microsoft, Apple — are also major commercial entities with interests that extend well beyond pure security research. How Anthropic polices the boundary between permitted defensive use and commercial advantage derived from exclusive frontier-model access will require ongoing scrutiny.

## Why This Matters Beyond Cybersecurity

Claude Mythos Preview's restricted release is a test case for a broader question the AI industry has so far mostly avoided confronting directly: what do you do when you build something too powerful to release safely?

The standard playbook — staged rollout, safety fine-tuning, usage policies — presupposes that a model can be made safe enough for general deployment with sufficient care. Project Glasswing suggests Anthropic has concluded that, at least for this model's cybersecurity capabilities, no amount of fine-tuning or policy enforcement makes general release acceptable. That is a significant line to cross, and the company deserves credit for the candor with which it has explained its reasoning.

The practical consequence is a world in which frontier AI capabilities become increasingly stratified: available to large institutions with the resources and credibility to join consortia like Glasswing, inaccessible to smaller organizations and individuals. Whether that stratification produces better security outcomes than broader access — through the diversity of perspectives and the sheer scale of defenders it would enable — is a genuine policy debate the industry has barely begun.

For now, the race to patch what Claude Mythos found is the most urgent priority. The bugs are real, the software is in production, and somewhere beyond the Glasswing consortium, someone else may be looking for the same vulnerabilities with less scrupulous intentions.
