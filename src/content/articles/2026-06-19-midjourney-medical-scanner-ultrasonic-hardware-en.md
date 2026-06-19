---
title: "Midjourney Enters Medical Imaging with Radiation-Free Full-Body Ultrasonic Scanner"
summary: "The AI image generation company announces Midjourney Medical, a new division building a whole-body ultrasonic scanner it calls 'the first new whole-body medical imaging method in 50 years.' The device uses 500,000 ultrasonic sensors and no radiation, targeting a consumer spa launch in San Francisco by end of 2027."
category: "hardware"
publishedAt: 2026-06-19
lang: "en"
featured: true
trending: true
sources:
  - name: "PYMNTS"
    url: "https://www.pymnts.com/news/artificial-intelligence/2026/midjourney-enters-medical-imaging-with-60-second-full-body-scan/"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-06-18/ai-startup-midjourney-pivots-to-health-with-ultrasound-machine"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/318628/20260618/midjourney-full-body-ultrasound-scanner-targets-mri-speed-prototype-runs-20-minutes.htm"
  - name: "Engadget"
    url: "https://www.engadget.com/2196998/midjourney-full-body-ultrasonic-scanner/"
tags:
  - "midjourney"
  - "medical-imaging"
  - "ultrasound"
  - "hardware"
  - "health-tech"
  - "david-holz"
  - "butterfly-network"
relatedSlugs:
  - "2026-06-19-midjourney-medical-scanner-ultrasonic-hardware-zh"
  - "2026-06-18-snap-specs-ar-glasses-launch-en"
---

Midjourney, the AI image generation startup best known for conjuring surreal digital art from text prompts, has announced a dramatic pivot into hardware and healthcare. On June 18, the company unveiled **Midjourney Medical**, a new division building what founder David Holz describes as "the first new whole-body medical imaging method in 50 years" — a radiation-free, full-body ultrasonic scanner that promises to undercut MRI pricing by an order of magnitude.

The announcement reframes what many assumed was a software-only company as an increasingly hardware-ambitious venture, following a year in which Midjourney quietly recruited engineering talent away from Apple, Meta, and other consumer device makers.

## How the Scanner Works

The Midjourney Scanner doesn't look like a hospital device. Users would lower themselves into a shallow pool encircled by a ring of ultrasonic hardware — roughly 70 centimeters in diameter — lined with approximately 500,000 ultrasonic sensors across 40 hardware modules. Sound waves pulse through the body from every angle simultaneously, and the resulting data is handed off to a computing cluster that reconstructs the signals into full three-dimensional cross-sectional images.

Midjourney is calling the technique "Ultrasonic CT" — a deliberate nod to X-ray computed tomography, which similarly layers cross-sectional images into volumetric data, except that ultrasound carries no ionizing radiation and requires no magnetic field.

The company claims the finished device will complete a scan in roughly 60 seconds. There's an important asterisk: the current prototype reportedly takes closer to 20 minutes and has only been used on about a dozen people. Holz's framing — "around 10x cheaper and 60x faster than an MRI" — is, by his own acknowledgment, a target, not a shipping specification.

Still, the basic physics are not fantasy. Ultrasound is already the workhorse of clinical imaging for everything from cardiac screening to prenatal care. The technical gap is in reconstruction: turning acoustic backscatter data from half a million sensors into a diagnostically interpretable whole-body image requires computational approaches that have only recently become tractable at the scale Midjourney is targeting.

## Who Is Building This

Ahmad Abbas, who previously served as an engineering manager for Apple's Vision Pro, is leading Midjourney's hardware division. Holz himself co-founded Leap Motion before building Midjourney, giving him a longer hardware pedigree than his company's image-generation reputation might suggest.

Critically, Midjourney is not attempting to manufacture the ultrasound hardware itself. The company has entered a co-development agreement with **Butterfly Network** — a publicly traded semiconductor ultrasound firm that pioneered ultrasound-on-a-chip technology — worth up to $74 million over five years. Butterfly's stock jumped on the news, as the deal provides the startup with a manufacturing and regulatory partner experienced in navigating FDA clearance processes.

## The Spa Strategy and Regulatory Path

Perhaps the most unusual aspect of Midjourney Medical's launch is its go-to-market strategy. Rather than selling to hospitals, the company plans to open **Midjourney Spa** — a 25,000-square-foot wellness facility in San Francisco's Union Square district by end of 2027. The space will combine hot tubs, saunas, cold plunges, and gym facilities, with the scanner positioned as a premium wellness feature rather than a diagnostic tool.

That positioning is partly a regulatory play. Full diagnostic claims require FDA clearance, which could take years and demands clinical evidence Midjourney doesn't yet have. Body composition mapping — showing fat distribution, muscle mass, and tissue density without claiming to diagnose any condition — operates in a softer regulatory category. Midjourney plans to begin there and layer on FDA approvals incrementally as clinical evidence accumulates.

It's a strategy reminiscent of how consumer health wearables have long walked the line between wellness devices and regulated medical instruments, starting with step counting and working up to FDA-cleared ECG readings.

## Scale Ambitions and the Billion-Scan Target

Midjourney's long-term projections are sweeping. The company's stated goal is 50,000 scanners globally by 2031, capable of processing one billion scans per month. For context, the entire global installed base of MRI machines is roughly 60,000 to 80,000 units — and each costs between $1 million and $3 million, plus substantial infrastructure for shielding and cooling superconducting magnets.

The implied unit economics of the Midjourney scanner, if achieved, would be transformative. Standard MRI procedures currently cost patients $400 to $12,000 depending on the body region, insurance coverage, and facility. They also require physician referrals, hospital infrastructure, and 30 to 60 minutes of staying motionless inside a deafeningly loud tube. Midjourney is targeting "a few dollars per session" in the spa context — which would represent one of the largest reductions in per-scan imaging cost in the history of radiology.

## The Strategic Bet Behind the Pivot

The move raises obvious questions about focus. Midjourney's text-to-image platform competes directly with Stable Diffusion, DALL-E, and Adobe Firefly in a market that has become intensely commoditized. Margins in AI-generated imagery are under pressure as open-source models have made the underlying capability increasingly accessible.

Medical imaging, by contrast, remains one of the least disrupted corners of the healthcare system, characterized by legacy vendor lock-in, significant per-unit hardware revenue, and recurring software revenue for analysis tools. The regulatory and technical moats are genuinely high.

Holz's bet appears to be that Midjourney's core strength — applying machine learning to reconstruct and interpret visual data — transfers to a domain where the compute requirements and AI differentiation are arguably even higher. Reconstructing clinically useful 3D anatomy from ultrasonic backscatter is a harder problem than generating a stylized image from a text prompt, but the resulting defensible position could be considerably more durable.

## Skepticism and Open Questions

The medical and investor community's reaction has been cautiously watchful rather than enthusiastic. The scanner has not been peer-reviewed, has no published clinical data, and carries no FDA clearance. The prototype's 20-minute scan time is a far cry from the 60-second target. Regulatory approval for diagnostic use — the step that would unlock reimbursement from payers and integration into clinical workflows — remains years away at minimum.

There are also open questions about image quality relative to established modalities. MRI's strength is in soft-tissue contrast; CT's is in bone and density differentiation; ultrasound traditionally excels at real-time imaging of moving structures like the heart and fetus, but historically suffers from limited penetration depth, operator-dependence, and significant artifacts in dense tissue. Whether Midjourney's computational CT approach can overcome these limitations at a whole-body scale is the $74 million question — quite literally, given the Butterfly Network deal size.

What is clear is that Midjourney has made the most surprising hardware announcement in the AI industry this year. Whether the scanner becomes the accessible preventive care tool Holz envisions, or remains a wellness gimmick in a San Francisco spa, depends entirely on science, regulatory diligence, and execution that the company has yet to demonstrate. The bet is audacious. The timeline is ambitious. And in a year of incremental AI product announcements, it is at minimum genuinely new.
