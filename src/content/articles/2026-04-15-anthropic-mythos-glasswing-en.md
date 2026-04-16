---
title: "Anthropic's AI Finds Thousands of Zero-Days—Then Launches a $100M Defense Fund Instead of Releasing It"
summary: "Anthropic's Claude Mythos Preview autonomously identified thousands of previously unknown vulnerabilities in every major OS and browser, including bugs hidden for 27 years. Deeming the model too dangerous to release publicly, Anthropic instead launched Project Glasswing: a $100 million defensive initiative with 11 tech titans to patch critical software before adversaries can exploit similar capabilities."
category: "ai-ml"
publishedAt: 2026-04-15T09:05:00Z
lang: "en"
featured: true
trending: true
sources:
  - name: "Anthropic — Project Glasswing"
    url: "https://www.anthropic.com/glasswing"
  - name: "The Hacker News — Anthropic's Claude Mythos Finds Thousands of Zero-Day Flaws"
    url: "https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html"
  - name: "VentureBeat — Anthropic says its most powerful AI cyber model is too dangerous to release"
    url: "https://venturebeat.com/technology/anthropic-says-its-most-powerful-ai-cyber-model-is-too-dangerous-to-release"
  - name: "Infosecurity Magazine — Anthropic Launches Project Glasswing"
    url: "https://www.infosecurity-magazine.com/news/anthropic-launch-project-glasswing/"
  - name: "Axios — Anthropic withholds Mythos Preview model because its hacking is too powerful"
    url: "https://www.axios.com/2026/04/07/anthropic-mythos-preview-cybersecurity-risks"
tags:
  - "Anthropic"
  - "Claude Mythos"
  - "cybersecurity"
  - "zero-day"
  - "Project Glasswing"
  - "AI safety"
relatedSlugs:
  - "2026-04-15-openai-gpt54-cyber-model-en"
---

On April 7, Anthropic made an announcement that sent shockwaves through the cybersecurity industry and the broader AI research community: its newest frontier model, Claude Mythos Preview, had quietly and autonomously found thousands of zero-day vulnerabilities—previously undiscovered flaws—embedded in the world's most widely used software. Every major operating system. Every major web browser. A sprawling ecosystem of critical open-source tools.

And Anthropic had decided it would not release the model to the public.

Instead, the company unveiled Project Glasswing: a $100 million defensive initiative pairing Mythos Preview with 11 of the world's largest technology companies to patch those vulnerabilities before adversaries with access to similar AI capabilities could weaponize them. The announcement was simultaneously the most impressive demonstration of AI's offensive potential and one of the most consequential decisions in frontier AI deployment to date.

## A Model That Outperforms Human Experts at Finding Exploits

Anthropic has been careful to call Mythos Preview a "general-purpose" frontier model—not a specialized security tool. But its capabilities in the cybersecurity domain are unlike anything previously demonstrated by a publicly disclosed AI system.

According to Anthropic's own disclosures, over a testing period of several weeks, Claude Mythos Preview was deployed against real codebases and operating system images. Its findings were stunning in both volume and severity:

- **Thousands of zero-day vulnerabilities** across every major operating system (including Windows, macOS, Linux distributions) and every major web browser (Chrome, Safari, Firefox, Edge)
- **A 27-year-old bug in OpenBSD**, one of the most security-focused Unix-like operating systems, that had evaded detection by human researchers for nearly three decades
- **A 16-year-old vulnerability in FFmpeg**, the widely deployed open-source multimedia framework used by billions of devices and streaming platforms
- Multiple critical vulnerabilities in other widely used infrastructure components

Beyond vulnerability discovery, Mythos Preview can exploit zero-day vulnerabilities in real open-source codebases, reverse-engineer exploits from closed-source binaries, and convert known-but-unpatched vulnerabilities into working exploits. It surpasses "all but the most skilled human" security researchers, in Anthropic's own assessment.

That last capability—turning published CVEs into functional exploits—is particularly alarming. Security researchers have long worried about the "patch gap": the window between a vulnerability being disclosed and organizations actually deploying a fix. Mythos Preview could, in hostile hands, systematically compress that window to near zero, enabling attackers to weaponize known vulnerabilities at industrial scale before defenders can respond.

## Why Anthropic Chose Not to Release It

The decision to withhold Mythos Preview from public release is not unprecedented—OpenAI similarly restricted access to early versions of its most capable models on safety grounds—but the specific framing is new. Anthropic is not saying Mythos is merely more capable than prior models. It is saying that a publicly released version would represent a qualitative shift in the threat landscape: a point at which AI moves from being a research accelerant to an autonomous cyberattack engine within reach of nation-states, criminal organizations, and sophisticated individual actors.

The dual-use dilemma here is particularly acute because, unlike biological or nuclear weapons, cybersecurity knowledge is inherently symmetric. The same understanding of a vulnerability that lets a defender patch it lets an attacker exploit it. A model that can find zero-days is, by construction, a model that could help someone exploit them.

Anthropic's response is to control the supply chain of who interacts with the model, rather than who interacts with the knowledge it produces. Project Glasswing funnels Mythos Preview's capabilities into a highly controlled, defense-first pipeline operated by organizations with both the technical sophistication to use it responsibly and the institutional incentive to prioritize patching.

## Project Glasswing: The $100M Response

Project Glasswing brings together 11 major organizations, each contributing specific expertise and infrastructure:

- **Amazon Web Services** — cloud infrastructure and security toolchain integration
- **Apple** — proprietary OS and browser security
- **Broadcom** — enterprise networking and chip-level vulnerabilities
- **Cisco** — enterprise infrastructure and networking security
- **CrowdStrike** — threat intelligence and endpoint detection
- **Google** — Android, Chrome, and cloud platform security
- **JPMorgan Chase** — financial sector critical infrastructure
- **Linux Foundation** — open-source supply chain security coordination
- **Microsoft** — Windows, Azure, and enterprise software security
- **NVIDIA** — AI computing infrastructure security
- **Palo Alto Networks** — network security and threat intelligence

Anthropic is committing up to **$100 million in Mythos Preview usage credits** for the initiative, plus **$4 million in direct donations** to open-source security organizations including the Open Source Security Foundation and critical-software maintainer grants. The goal is explicitly to use the model to identify and remediate vulnerabilities before actors with access to equivalent AI capabilities—whether state-sponsored or criminal—can find and weaponize the same flaws.

Each partner organization has been granted controlled access to Mythos Preview through a custom security research interface designed to prevent the model from being used for anything other than vulnerability discovery and patch generation. Anthropic's red team monitors all usage logs and retains authority to revoke access.

## The AI Security Arms Race Enters a New Phase

The release of Mythos Preview details—even without the model itself being publicly available—marks an inflection point in the AI security discourse that has been building for several years. Prior to this, the most credible demonstrations of AI-powered vulnerability discovery involved models finding bugs in narrow, well-specified codebases under controlled conditions. Mythos Preview finding thousands of previously unknown bugs across heterogeneous, real-world production software is a different order of magnitude.

Security researchers at the UK AI Security Institute and its US counterpart have begun evaluating the claims independently. Early indications, according to sources familiar with the evaluations, suggest that Anthropic's characterization of Mythos's capabilities is broadly accurate—though independent researchers are still verifying the full scope of the zero-day findings.

The AI Safety Institute's involvement also reflects a broader shift in how governments are treating frontier model evaluations. Both the UK and the US now require pre-deployment safety testing for models above certain capability thresholds. Mythos Preview appears to be the first model to trigger government engagement specifically on the basis of its cybersecurity capabilities, as distinct from concerns about biological or chemical weapon assistance.

## What Comes Next

Anthropic has not announced a timeline for a broader Mythos release, or whether the model will eventually become publicly available in some form. The company says Project Glasswing is intended to be ongoing rather than time-limited—the model will continue to be used to identify new vulnerabilities as they emerge, not merely to clear a pre-existing backlog.

The 11 partner organizations are expected to begin publishing patches derived from Mythos Preview findings in coordination with Anthropic over the coming weeks, following standard coordinated disclosure protocols. For each vulnerability addressed, Anthropic will also publish a technical summary to help the broader security community understand the class of flaw and apply analogous fixes elsewhere.

For the rest of the technology industry, Project Glasswing raises an uncomfortable question: if a model available today can find thousands of undiscovered vulnerabilities in the world's most security-hardened software, how many of those same vulnerabilities are being actively discovered—right now—by adversaries with access to equivalent or similar models? The race to patch has never been more urgent.
