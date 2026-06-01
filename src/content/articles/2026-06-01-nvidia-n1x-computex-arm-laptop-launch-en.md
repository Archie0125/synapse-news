---
title: "Nvidia Unveils N1X: First Blackwell Laptop Chip Signals New Era for Windows on Arm"
summary: "Jensen Huang took the stage at GTC Taipei on June 1 to officially unveil the Nvidia N1 and N1X, the company's first-ever laptop processors. Built with MediaTek on TSMC 3nm and pairing 20 Arm CPU cores with a 6,144-CUDA-core Blackwell GPU, the chips target a 150-million-unit-per-year market long dominated by Intel, AMD, and Qualcomm."
category: "hardware"
publishedAt: 2026-06-01
lang: "en"
featured: true
trending: true
sources:
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/pc-components/cpus/nvidias-long-awaited-n1-n1x-soc-specs-leak-ahead-of-computex-launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-with-12-and-10-core-configs"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/317428/20260530/nvidia-arm-laptop-chip-n1x-confirmed-computex-cuda-rtx-5070-gpu-onboard.htm"
  - name: "ChatForest"
    url: "https://chatforest.com/reviews/nvidia-gtc-taipei-2026-jensen-huang-keynote-n1x-vera-rubin-physical-ai-preview/"
  - name: "XDA Developers"
    url: "https://www.xda-developers.com/mere-days-before-computex-2026-information-on-the-nvidia-n1-chip-leaked-online/"
tags:
  - "Nvidia"
  - "N1X"
  - "Computex"
  - "Windows on Arm"
  - "laptop chips"
  - "Blackwell"
  - "MediaTek"
  - "AI PC"
relatedSlugs:
  - "2026-06-01-microsoft-build-2026-mai-coding-models-en"
  - "2026-06-01-google-gemini-35-pro-june-launch-en"
---

Jensen Huang has spent the last three years telling the world that the future of computing is accelerated. On June 1, standing in Taipei ahead of Computex 2026, he made that future tangible in a form factor that has until now been entirely outside Nvidia's reach: the laptop.

The GTC Taipei keynote marked the official debut of the Nvidia N1 and N1X — the company's first laptop system-on-chips, co-developed with MediaTek and fabbed on TSMC's 3nm process. It is, by any measure, one of the most consequential hardware announcements in Nvidia's history, extending the company's silicon empire from data centers and desktops into the roughly 150 million units shipped annually in the PC market.

## The Chips, Explained

The flagship N1X is a beast by laptop SoC standards. At its core sits a 20-core CPU complex, split between 10 high-performance Arm Cortex-X925 cores and 10 efficient Cortex-A725 cores — a configuration that mirrors what Qualcomm uses in its Snapdragon X Elite, but with a critical differentiator underneath: the GPU.

Where Qualcomm relies on its in-house Adreno graphics, the N1X pairs those CPU cores with a full Blackwell-architecture GPU carrying 6,144 CUDA cores across 48 shader multiprocessors. That is not a mobile-grade graphics block — it is, in performance terms, equivalent to a desktop RTX 5070. The chip ships with a unified LPDDR5X memory subsystem supporting up to 128GB, and fits within a 45–80W power envelope depending on OEM configuration.

The standard N1 variant targets thinner, more power-conscious designs, with configurations ranging from 10 to 12 CPU cores and a smaller GPU cluster. Both chips are built on TSMC's N3 process, the same node used in Apple's latest M-series and Snapdragon X processors.

"This is the Grace Blackwell architecture brought to the PC," Huang told the packed audience at Taipei Music Center. "Every laptop we ship will be able to run local AI natively. That changes everything about how people work."

## The Windows on Arm Bet

Nvidia's entry into laptops is not happening in a vacuum. The Windows on Arm ecosystem has spent three years clawing toward legitimacy. Qualcomm's Snapdragon X Elite gave the platform its first genuinely competitive chip in 2024. Apple, of course, demonstrated years ago that Arm laptops could be the best in class.

What has been missing — and what Nvidia now provides — is Arm-based Windows hardware with credible GPU performance for creative, gaming, and AI-inference workloads. The company claims the N1X delivers more than twice the GPU throughput of Snapdragon X Elite at comparable CPU performance, though independent benchmarks won't be available until launch units ship.

The strategic timing is deliberate. Intel's Lunar Lake and Arrow Lake laptop lines have struggled to close the efficiency gap with Arm competitors, and AMD's upcoming RDNA 4-based mobile chips are still months from market. Nvidia is walking through an opening.

## OEM Partners Ready on Day One

Unlike some chip unveilings where hardware is months from store shelves, Nvidia's announcement comes with a full partner ecosystem already assembled. Dell, Lenovo, Asus, and MSI have all confirmed N1X-based designs, with Asus committing to use the chip in multiple ZenBook and ProArt lines.

Dell's XPS series — long considered a gold standard for Windows laptop design — will be among the first to adopt N1X. Lenovo is positioning ThinkBook and Yoga models for the chip, while MSI is targeting creator and gaming-adjacent use cases where the Blackwell GPU provides a tangible advantage for local AI inference.

First commercial devices are targeted for the 2026 holiday season, with broader availability across SKUs expected in early 2027. Pre-production units will be available for developers and reviewers at Computex this week.

## Why This Matters for Local AI

The GPU inside the N1X is more than a performance differentiator — it is fundamentally a local AI compute engine. The 6,144 CUDA cores support Tensor Core operations for FP8, INT8, and INT4 inference, which translates directly to the ability to run large language models locally without cloud connectivity.

At 45W sustained power, Nvidia claims the N1X can run a 70-billion-parameter quantized model at practical speeds — roughly 15–20 tokens per second — on device. At the 80W ceiling, larger context windows and faster throughput become possible. For privacy-conscious users, regulated industries, or anyone in regions with unreliable connectivity, this changes the economics of AI-augmented software fundamentally.

Microsoft was a co-announcer on stage, with Windows chief Panos Panay describing the N1X as a platform that "makes every Windows app AI-native." Arm Holdings CEO Rene Haas appeared via video to describe the chip as validation of the consortium's long bet on Arm-based computing.

## Competitive Implications

Qualcomm's stock fell roughly 4% in early trading following the announcement, a signal that investors see the N1X as a direct challenge to Snapdragon's Windows on Arm dominance. Qualcomm has invested years of ecosystem-building and Microsoft partnership into making Snapdragon the go-to platform for AI PCs — and now faces a competitor with stronger GPU credentials and the Nvidia brand behind it.

Apple is a more complicated comparison. Apple Silicon remains the performance-per-watt champion for Arm-based laptops, and the M4 generation's Neural Engine retains advantages for on-device AI in Apple's controlled software stack. But Apple does not sell chips or license its platform, which means every enterprise IT buyer who wants Arm laptops with Windows now has a new, high-powered option.

For Intel, the timing is uncomfortable. Meteor Lake and Arrow Lake have failed to deliver the generational leap the company promised, and Arrow Lake's weak gaming performance was already an embarrassment. Nvidia entering its market from a position of GPU strength adds pressure from an entirely unexpected direction.

## What Comes Next

The full Computex week begins June 2, where Nvidia will be showing the N1X in live demonstrations across partner booths. Huang's keynote also previewed Vera Rubin, the next-generation data center GPU platform, and touched on Nvidia's physical AI roadmap — but the N1X was clearly the consumer headline.

The laptop chip market will not be reshaped overnight. Qualcomm's OEM relationships and Windows integration work run deep. Intel's manufacturing deals and roadmap give it runway. But for the first time since Arm entered the Windows laptop market in earnest, there is a GPU-first competitor willing to go toe-to-toe on the specifications that creative professionals and developers care about most. That, in itself, is a seismic shift.
