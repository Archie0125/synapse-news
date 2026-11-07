---
category: policy
featured: true
lang: en
publishedAt: '2026-11-07T19:13:53.318723+00:00'
relatedSlugs: []
sources:
- name: The Verge
  url: https://www.theverge.com/ai-artificial-intelligence/1029483/nvidia-ai-chips-china-blacklist-government
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/artificial-intelligence/us-intelligence-believes-jensen-huang-had-romantic-relationship-with-chinese-spy-in-honeypot-operation-spy-suspect-linked-to-company-accused-of-smuggling-usd2-billion-in-ai-chips
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/big-tech/nvidias-jensen-huang-officially-called-to-congress-due-to-reports-of-a-chinese-spy-plot-officials-mention-growing-concerns-over-national-security
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/big-tech/nvidia-tightens-tracking-of-ai-gpus-in-southeast-asia-as-chinese-chip-smuggling-draws-scrutiny-report-claims-cloud-providers-must-join-monitoring-program-to-qualify-for-official-partner-status
- name: The Verge
  url: https://www.theverge.com/tech/1029338/nvidia-ceo-jensen-huang-china-spy
summary: The honeypot story is getting the headlines, but the real scandal is that
  Washington's AI chip vetting approved a company that doesn't seem to exist.
tags: []
title: Nvidia's China Scandal Isn't About a Spy. It's About an Empty Office.
trending: true
type: analysis
---

The spy story is the less important of Nvidia's two China scandals this month.

That's a strange thing to say about a report that US intelligence believes China's Ministry of State Security recruited Alice Huang (also known as Huang Le), a Megaspeed executive, to get close to Jensen Huang. Spies, a CEO married for 41 years, a company accused of moving $2 billion in chips: it's built to go viral. Three House chairs, John Moolenaar (China), Brian Mast (Foreign Affairs) and Rick Crawford (Intelligence), have asked Huang to come in for a closed-door briefing.

But a honeypot is about one person's judgment. An empty office in China that got approved to receive H200s is about the system. People can be compromised. A system that can't tell a real buyer from a gray concrete shell with wires hanging from the ceiling is just broken.

## Here's what actually happened

Two stories landed on top of each other. The New York Times reported, and the FT and WSJ followed, that the MSS allegedly enlisted Alice Huang to collect intelligence on American AI chips and "potentially influence" Nvidia to push for its most advanced chips to be sold to China. She reportedly also had ties to senior people at Gigabyte. President Trump was reportedly briefed on the relationship last year and did nothing. According to the Times, Jensen Huang never got a "defensive briefing," the routine warning US agencies give people they think foreign intelligence is targeting.

Her company is the reason this is more than gossip. Megaspeed, based in Singapore, has been under Commerce Department scrutiny since 2024 over allegations that it moved about $2 billion of advanced Nvidia silicon into China through Speedmatrix, a subsidiary with two offices in Johor, Malaysia. The Times says Megaspeed kept buying billions of dollars of Nvidia hardware anyway. Nvidia says Megaspeed has no ties to China.

The second story is the one that matters. The Times found that New Matrix, a company on the list of Chinese firms approved to handle H200s, operates out of an empty office. It was set up 17 months ago. It isn't in the building directory, and the industrial park's management office has no record of it. Its owners are linked to a Chinese private equity firm the US has blacklisted since 2024. The Times describes this as a pattern, not a one-off.

## The incentive problem nobody is talking about

Look at how the rules changed. Under Biden, the H100 and then the cut-down H800 and A800 were blocked in stages through 2022 and 2023. Under Trump, Nvidia first got H20 licenses in exchange for paying the government 15% of China revenue, and later got the H200 opened up with a revenue share attached. The Verge's headline summary puts it bluntly: a revenue cut seems to have replaced due diligence.

I'd go further. **Once Washington takes a share of every sale, the agency doing the vetting is also, structurally, a beneficiary of the sale.** Nobody has to be corrupt for that to matter. Incentives work through small choices: which applications get a closer look, whose diligence gets a pass, which red flags count as worth delaying a deal. An export regime that earns money from approvals has a reason to approve things.

The way vetting works makes it worse. Export screening runs on legal entities. Is this company on the Entity List? Do its owners show up? But entities are disposable. New Matrix is 17 months old. Setting up a new Chinese shell company takes a few weeks and costs less than one H200 server. When the cost of getting around a check is that low and the check only looks at paperwork, the check is decoration.

## Why the honeypot still matters, just not the way you think

The common assumption is that a spy near Jensen Huang would be after chip designs. That isn't the valuable part. Blackwell's architecture is already being studied by every competitor with an electron microscope. What can't be bought is **strategic intent**: how Nvidia ranks customers when supply is tight, which policy arguments Huang plans to bring to the White House, where Nvidia will give ground on export terms and where it won't.

Huang has been the most effective lobbyist for China sales anywhere. He has said China is roughly a $50 billion market and argued that blocking Nvidia just hands it to Huawei. Whatever you think of that argument, it is the argument Beijing wants made. If the MSS really did have someone near the person making it, the payoff wasn't stolen IP. It was a read on, and maybe a hand in, US policy.

## The irony of Nvidia becoming the export police

Meanwhile Nvidia is building its own enforcement tools. Bloomberg reports that Southeast Asian cloud providers now have to enroll in Nvidia's Fleet Intelligence system, which estimates a GPU's location from telemetry and network latency, if they want Nvidia Cloud Partner status. That status brings preferred chip allocation, so it is real leverage.

There's some dark comedy here. In July 2025, the Cyberspace Administration of China summoned Nvidia over alleged "tracking and remote shutdown" backdoors in the H20, and Nvidia firmly denied having any. Sixteen months later, Nvidia is rolling out location tracking as a requirement for partners in exactly the region that smuggled chips pass through.

The next effect matters more: **export control is being privatized**. Commerce doesn't have the staff to inspect data centers in Johor. Nvidia does have the telemetry. The Chip Security Act, which Sen. Tom Cotton introduced in 2025 to require location verification on advanced chips, would have written this into law. Instead it's happening through commercial terms, set by the company whose revenue depends on loose enforcement. Fleet Intelligence is still opt-in outside the NCP requirement, and Nvidia hasn't said whether existing partners have to join.

## The bear case, taken seriously

There's a reasonable case for skepticism. The honeypot allegations come from unnamed intelligence officials, and they surfaced in the middle of an ugly fight between China hawks in Congress and the White House camp that wants to sell to China. Leaking a lurid story about the CEO at the center of that fight is an old tactic. Nvidia and Megaspeed both deny the key claims.

There's also the realist case that the controls never worked and never could have. Huawei's Ascend roadmap keeps moving. DeepSeek trained frontier-class models on restricted hardware. Malaysia only added permit requirements for US AI chip exports in July 2025, after years of open leakage. By this logic, selling H200s at least keeps Chinese developers on CUDA and gives Washington a cut.

That case is coherent, but it argues for a different policy, not for this one. If the US's position is that controls don't work, it should say so and drop them. What we have now is the worst combination: export restrictions that look strict, revenue-sharing that creates conflicted incentives, and vetting that can't find an empty office. China gets the chips anyway, and the US gives up both the leverage and the credibility.

## What to Watch

- **The briefing happens, nothing public comes out.** Huang will attend before year-end and there will be no public testimony. The pressure will move to Commerce, not Nvidia.
- **New Matrix-style firms hit the Entity List within 90 days.** Commerce needs a visible fix. Expect several approved H200 recipients to be delisted or blacklisted, and an announcement about tighter end-user verification that still won't include on-site inspections.
- **Location verification becomes law in 2027.** Some version of the Chip Security Act will ride on the next NDAA. Nvidia will support it publicly, because Fleet Intelligence will already be the compliance tool everyone uses.
- **Fleet Intelligence moves beyond Southeast Asia.** The Gulf, where the UAE and Saudi deals involve hundreds of thousands of chips, is next, by mid-2027.
- **H200 revenue from China disappoints anyway.** Beijing has already discouraged buying the H20. It will push domestic accelerators for state-linked buyers, which means the scandal costs Nvidia political capital in exchange for China revenue that never shows up at scale.