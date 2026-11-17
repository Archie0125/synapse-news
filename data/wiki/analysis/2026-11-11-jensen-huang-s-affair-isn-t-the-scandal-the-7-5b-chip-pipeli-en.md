---
category: policy
lang: en
published: '2026-11-11T06:24:18.283445+00:00'
sources:
- name: The Verge
  url: https://www.theverge.com/ai-artificial-intelligence/1031063/jensen-huang-ai-race-us-china-spy
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/policy/alice-huang-reportedly-instrumental-in-securing-over-usd7-5-billion-of-nvidia-ai-gpu-imports-during-three-year-relationship-with-jensen-huang-helped-move-240-000-banned-chips-into-china-mostly-h100-and-h200
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/policy/president-trump-says-the-fbi-is-investigating-jensen-huangs-affair-nvidia-also-accused-of-intervening-in-megaspeed-chip-smuggling-investigation
- name: Engadget
  url: https://www.engadget.com/2312947/nvidia-shareholders-are-suing-the-company-and-ceo-jensen-huang/
summary: Washington let one CEO's personal relationships do the work of export control,
  and the price so far is $470 billion in Nvidia market value.
title: Jensen Huang's Affair Isn't the Scandal. The $7.5B Chip Pipeline Is.
trending_theme: Nvidia CEO Spy Scandal Fallout
type: analysis
---

Coverage of the Jensen Huang story has been all leather jacket and pillow talk. That is the wrong way to read it. The affair is what got people to look. The story underneath is that America's main tool for keeping frontier AI hardware out of Beijing's hands depended on the judgment, and the personal life, of the man who earns the most from selling that hardware.

Start with what has been reported. Huang, 63 and married for 40 years, has admitted an affair with Alice Huang (no relation), a former executive at Singapore-based Megaspeed. US intelligence suspects she works with China's Ministry of State Security. According to *The Information*, she and her family built a network of companies in China and Singapore centered on Shanghai Century Litong. That company was founded in 2023 and soon became an Nvidia *preferred cloud partner*, which put it near the front of the queue for allocation. Over the three-year relationship, the network reportedly helped bring in about $7.5 billion worth of Nvidia GPUs, including roughly 240,000 banned chips, mostly H100s and H200s. About $4.6 billion of that reportedly went through Megaspeed between 2023 and 2025, and another $2 billion through a firm called Speedmatrix.

Nvidia has lost more than $470 billion in market value over two days. A shareholder, Mark Kistenmacher, has filed a proposed class action. Trump has confirmed the FBI is looking into it. Congress has summoned Huang. He has pulled out of the ElevenLabs Summit and the Anthropic CEO Forum. The board has set up an independent committee.

All of that is real. None of it is the most important part.

## The vendor was also the gatekeeper

Here is what nobody is talking about: **US chip export control has been run on the honor system, and the company being trusted is the one with the strongest reason to cheat.**

Recall how the rules developed. In October 2022, the Commerce Department cut China off from the A100 and H100. Nvidia answered with the A800 and H800, which were tuned to sit just under the performance thresholds. Commerce tightened the rules in October 2023, and Nvidia released the H20. In April 2025, Washington blocked the H20 as well, and Nvidia took a $4.5 billion charge. By August 2025, the government had stopped trying to block sales and started taking a share of them: first a 15% revenue cut on H20 sales, then approval of H200 exports with a 25% fee.

Each step relied on the same assumption: Nvidia would know its customers. The Bureau of Industry and Security has a few hundred enforcement agents. Nvidia has the order books, the allocation queues and the partner programs. In practice, knowing who buys Nvidia GPUs and where they end up has been outsourced to Nvidia.

Now look at what Bloomberg reported. During a 2025 US investigation into suspected smuggling by Megaspeed, Nvidia's general counsel, Tim Teter, contacted Commerce Under Secretary Jeffrey Kessler. The point is not whether that call broke any law. The point is that the company was involved in the investigation of its own customer's compliance. When the vendor sits in the enforcement loop, you don't have export control. You have Nvidia's sales department with a federal letterhead.

## The government knew

The second structural problem gets less attention because it makes everyone look bad, not just Nvidia. US intelligence reportedly told the President about Alice Huang's suspected MSS ties more than a year ago. Per reporting summarized by Tom's Hardware, he chose not to act, partly to protect Nvidia sales and avoid provoking Beijing during the trade talks that ended with H200 approval.

Trump now says Huang "had absolutely no idea that the person in question was a spy" and that "he'll be in good shape." Maybe so. But the White House was holding a counterintelligence warning about the CEO of the most strategically important chip company in the country, and it decided the trade relationship mattered more. Once Washington started collecting 25% of Nvidia's China revenue, it became a partner in the business it was meant to police. A partner that gets paid by volume has little reason to slow volume down.

## Why the timing matters in court

Engadget's framing is right: Nvidia's legal exposure is less about the affair and more about the timeline. The class period starts October 9, 2025, when *The New York Times* first described the Nvidia–Megaspeed relationship and Nvidia called it routine business. It ends November 8, 2026, the day Huang admitted the affair and the company said it was investigating whether he had been targeted by a foreign intelligence operation.

In between, after the *Times* published a detailed feature on October 29, Nvidia spokesperson John Rizzo said: "Jensen's interactions with Ms. Huang are not unusual or unexpected. Meetings with customers are part of a CEO's job."

That one sentence is the plaintiffs' case. Securities fraud claims don't turn on morality. They turn on whether a material statement was false when it was made. Ten days separate "not unusual" from "I had an affair with her." Nvidia's lawyers would prefer to fight almost any other fact pattern.

## How much this matters to the AI race

The Verge quotes a researcher saying that with enough of these chips, "the US lead could vanish in a matter of weeks or months." That overstates it, but less than you might expect. Consider the scale: 240,000 H100/H200-class GPUs is in the same range as the largest single training clusters American labs had built by 2024. Epoch AI has documented a large black market in restricted chips. DeepSeek's January 2025 release already showed that Chinese labs can get frontier-adjacent results from constrained hardware.

Compare the alternatives. Huawei's Ascend 910C and Cambricon's accelerators are improving, but neither matches the H200 on performance per dollar, and neither comes with Nvidia's CUDA software ecosystem. For a Chinese lab, a smuggled H100 is worth more than its specifications because it runs software the lab already has. That is why the gray market keeps going even as Beijing pushes domestic substitution.

So what? If the reported numbers hold, the export regime that has shaped US–China tech policy since 2022 was leaking at a level big enough to matter strategically, and through a channel Nvidia's own partner program had approved.

## The case for the defense

Here is the strongest argument on Huang's side, because it deserves a fair hearing. Nothing reported so far shows he knowingly approved illegal shipments or handed over technical secrets. Megaspeed was a Singapore company, and Singapore is a legitimate and large market. Plenty of distributors launder chips without the CEO knowing anything, and the Linwei Ding case at Google showed that insiders can take crown-jewel IP without leadership being aware. Nvidia's stock may also be pricing in a worst case that never arrives. Losing $470 billion over a personal scandal with no proven legal violation looks like panic.

Still, "the CEO didn't know" is a governance failure in its own right. For three years a suspected intelligence asset posted photos with Huang on WeChat, showed them to customers as proof of her access, attended Nvidia's China partner event, and reportedly cleared supply-chain delays by name-dropping him. A preferred-partner program that never noticed this was not doing know-your-customer checks. It was doing know-your-CEO's-friends.

## What to Watch

- **Huang stays CEO, but loses some control.** He survives the next quarter. The board names a powerful lead independent director and an external chief compliance officer who reports to the board, not to Huang. Removing him would cost more than keeping him, and the board knows that.
- **Commerce goes after partner programs.** Within six months, BIS issues rules requiring chip vendors to disclose end-user ownership for allocation and preferred-partner programs. AMD and Broadcom will be covered too, even though they had nothing to do with this.
- **The Chip Security Act moves forward.** Senator Tom Cotton's bill to require location verification on exported AI chips stalled in 2025. This scandal gives it the votes. Expect attestation hardware built into Blackwell successors bound for Asia.
- **The H200 China channel narrows.** It may not close formally, but licenses slow down and the 25% fee becomes politically hard to defend. Nvidia's China revenue guidance goes down again.
- **Settlement, not trial.** The Kistenmacher suit and the copycat suits that follow settle within 18 to 24 months for nine figures. The discovery record, especially internal emails about Megaspeed allocations, will matter more than the payout.

The lesson is not to keep CEOs away from charming customers. The lesson is that a national security policy which depends on one executive's personal judgment was never much of a policy.