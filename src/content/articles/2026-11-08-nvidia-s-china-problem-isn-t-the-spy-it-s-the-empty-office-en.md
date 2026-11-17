---
category: policy
featured: true
lang: en
publishedAt: '2026-11-08T06:16:48.799561+00:00'
relatedSlugs: []
sources:
- name: The Verge
  url: https://www.theverge.com/ai-artificial-intelligence/1029483/nvidia-ai-chips-china-blacklist-government
- name: TechCrunch
  url: https://techcrunch.com/2026/11/07/chinese-exec-was-recruited-to-spy-on-nvidia-ceo-according-to-us-intelligence-memo/
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/big-tech/nvidias-jensen-huang-officially-called-to-congress-due-to-reports-of-a-chinese-spy-plot-officials-mention-growing-concerns-over-national-security
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/big-tech/nvidia-tightens-tracking-of-ai-gpus-in-southeast-asia-as-chinese-chip-smuggling-draws-scrutiny-report-claims-cloud-providers-must-join-monitoring-program-to-qualify-for-official-partner-status
- name: The Verge
  url: https://www.theverge.com/tech/1029338/nvidia-ceo-jensen-huang-china-spy
summary: Washington took a cut of Nvidia's China sales, then approved a buyer that
  turned out to be an empty office, and nobody has explained what the vetting actually
  checked.
tags: []
title: Nvidia's China Problem Isn't the Spy. It's the Empty Office.
trending: true
type: analysis
---

The spy story is getting the attention. It has a Ministry of State Security recruitment, an executive with close access to the world's most valuable chip CEO, and, according to the Financial Times, an alleged romantic relationship. Three House committee chairs now want Jensen Huang in a closed-door room. It reads like a thriller.

The more damaging story is the empty office.

On November 7, The New York Times reported that New Matrix, a company the US Commerce Department approved to handle Nvidia's H200 chips, lists an address that is "a hollow gray shell with wires dangling from the ceiling where lights should be." The building directory doesn't list it. The industrial park's property manager has no record of it. The company is 17 months old, and its owners have ties to a Chinese private equity firm the US has blacklisted since 2024. According to the Times, New Matrix is not a one-off. It fits a pattern of approved buyers linked to entities under national-security trade restrictions.

A spy needs a way in. A shell company already has one, because the US approved it. If an empty room can pass federal vetting for one of the most strategically sensitive products America sells, then the export control regime has stopped working as a filter. It has become a toll booth.

## How a security policy turned into a revenue deal

The history matters here.

In October 2022, the Biden administration restricted China's access to top AI chips. Nvidia responded by designing chips that fell just under the limits, first the A800 and H800 and later the H20. Washington tightened the rules again in 2023. In April 2025, the H20 needed a license too, and Nvidia took a multibillion-dollar write-down on inventory it could no longer sell. For three years, the arrangement was a game of cat and mouse, but at least the government was clearly the cat.

Then the Trump administration changed the deal. Nvidia agreed to give the federal government a share of its China sales, 15% under the arrangement first reported in August 2025, and the restrictions loosened, eventually reaching the H200. Huang lobbied hard for it, including high-profile appearances alongside the president. The Verge's own headline from the time put it bluntly: "Apparently you can pay your way out of national security concerns."

Nobody is talking about the structural problem that creates. **When the government takes a percentage of every sale, the agency that approves buyers is approving revenue for its own boss.** Every rejected application is money the Treasury doesn't collect. That doesn't mean a Commerce official waved New Matrix through for the money. It means the incentives no longer push toward saying no, and an empty office passing review is exactly what that kind of incentive drift looks like.

Compare this with how the Bureau of Industry and Security (BIS) handled things before. The Entity List was blunt, and companies on it were out. Under the new model, the question is no longer whether a company is blacklisted. It's whether a company is connected to something blacklisted, through a series of newly registered entities that are cheap to create. A new Chinese company costs very little to register. A blacklist that can be dodged with a fresh business license and a rented floor is not a control.

## Megaspeed is where the two stories meet

The spy story and the shell company story are usually reported separately. They shouldn't be.

Megaspeed is the Singapore-based data center company where Alice Huang works. According to the Times, it has bought billions of dollars of Nvidia chips and continues to buy them. According to Tom's Hardware's summary of the reporting, Commerce has accused it since 2024 of smuggling $2 billion worth of advanced chips into China. The intelligence memo says the MSS recruited Alice Huang to gather information on US AI chips and "potentially influence the company to push for its most advanced chips to be made available to China." The Times also reports that she has relationships with top executives at Gigabyte, one of the Taiwanese server makers that sits between Nvidia's chips and the racks that end up in data centers.

Taken together, the alleged playbook has three parts: a relationship with the CEO, a customer relationship that moves volume, and influence over policy pushing toward looser rules. If even half of it is accurate, Beijing didn't need to hack Nvidia. It needed someone with access, a distribution channel in Southeast Asia, and a US policy debate that was already moving in its favor. The H200 decision happened. That doesn't prove the plot worked, since there were plenty of American reasons for it, starting with Nvidia's shareholders. But it does mean the plot's stated goal and the actual outcome point in the same direction, and Congress will notice.

The most troubling detail, according to the Times, is that Huang never received a "defensive briefing," the standard warning US agencies give people who are likely intelligence targets. The Times also reports that President Trump was briefed on the relationship last year and took no action. Either the intelligence community didn't think the threat warranted a warning, or someone decided that warning him was politically awkward. Neither answer is reassuring.

## The bear case, taken seriously

There is a fair argument on the other side.

First, the memo is unverified intelligence leaked through anonymous officials, and the romance detail is the kind of claim that spreads quickly whether it's true or not. Nvidia says Huang's interactions with Alice Huang were "not unusual" and that the company shares no classified information with customers. That second point matters. Nvidia's chip designs are not state secrets in the legal sense, and a CEO meeting a large customer's executives is a normal part of his job.

Second, the H200 is no longer Nvidia's best chip. Blackwell is shipping, and Rubin is next. If the argument is that a generation-old part keeps China dependent on the CUDA ecosystem rather than speeding up Huawei's Ascend roadmap, that is a real strategic position. Huang has made it publicly for two years.

Third, Beijing itself has been discouraging Chinese firms from buying Nvidia's China-specific chips and pushing them toward domestic silicon. A market that China is partly closing on its own is not a market America can hold hostage.

All three points are reasonable. None of them explains the empty office. You can believe that selling H200s to China is sound strategy and still believe the buyers should exist. The debate over whether to sell is separate from whether the system can tell who it is selling to, and right now the answer to the second question looks like no.

## Nvidia is now policing itself

Here is the second thing being missed. While Washington's vetting looks hollow, Nvidia is building its own enforcement system.

According to Bloomberg, cloud providers in Southeast Asia that want official Nvidia Cloud Partner (NCP) status must now enroll in Fleet Intelligence, the company's fleet management software. It can estimate where each GPU is running using telemetry and network latency measurements. NCP status brings Nvidia's public endorsement and priority access to supply, which is a strong incentive to join. Outside of the NCP requirement, participation is still voluntary, and Nvidia hasn't said whether existing partners must enroll or whether the requirement will expand beyond the region.

Think about what that means. The most effective export enforcement tool in the region is not run by BIS. It's run by the seller, enforced through access to supply rather than law, and limited to the customers who opt in. Smugglers, by definition, won't. Privatized compliance helps Nvidia tell Congress it's taking the problem seriously. It does not catch the buyer who never applies for partner status.

## What to Watch

**1. New Matrix loses its authorization before year-end.** Commerce can't defend this one, and revoking a single license is the cheapest way to show it's acting. Expect the agency to describe it as an isolated case even though the Times describes a pattern.

**2. Huang's closed-door briefing happens, and a version of it leaks within days.** Moolenaar, Mast, and Crawford chair three committees. A briefing involving that many members won't stay confidential. The detail most likely to leak is the missing defensive briefing, because it shifts blame toward the executive branch, which is where Republicans in Congress would like it to land.

**3. Chip location verification becomes law in 2027.** The idea of requiring tracking for exported AI chips has been floating in Congress since 2025. Fleet Intelligence gives lawmakers proof that the technology works. Expect a mandatory version attached to a defense bill, possibly copying Nvidia's own approach.

**4. Megaspeed becomes the test case.** If Commerce has accused it of $2 billion in smuggling since 2024 and it is still buying billions of dollars of Nvidia chips, the obvious question is why it isn't on the Entity List yet. If it gets added in the next six months, that confirms the spy story changed the politics. If it doesn't, the toll booth model is winning.

**5. The 15% cut gets reopened.** Not because it's unconstitutional, though that argument exists, but because "the government profited from sales to a blacklisted network" is a line both parties can run on in the 2026 cycle's aftermath. The revenue-sharing model is the most exposed part of this whole arrangement, and it will be the first thing to give.

The spy story will fade or be confirmed. The empty office won't fade, because it's a working example of what the current system lets through.