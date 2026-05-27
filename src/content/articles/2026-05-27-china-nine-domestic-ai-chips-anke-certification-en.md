---
title: "China Certifies Nine Domestic AI Chips for Government Procurement, Sidelining Nvidia"
summary: "Chinese authorities have certified nine domestically designed AI processors — including Huawei's Ascend 910 and Alibaba's T-Head Zhenwu M890 — under the country's Anke security framework, creating the first formal 'AI training and inference chips' procurement category. The move accelerates China's systematic effort to replace foreign silicon in government and state-enterprise AI infrastructure."
category: "hardware"
publishedAt: 2026-05-27
lang: "en"
featured: false
trending: true
sources:
  - name: "Digitimes"
    url: "https://www.digitimes.com/news/a20260527PD230/chips-security-it-training-ascend.html"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/semiconductors/china-certifies-nine-domestic-ai-chips-for-government-procurement"
  - name: "South China Morning Post"
    url: "https://www.scmp.com/tech/policy/article/3354993/china-adds-ai-chips-secure-technology-assessment-list-amid-us-curbs"
tags:
  - "China"
  - "AI chips"
  - "Huawei"
  - "Alibaba"
  - "semiconductor policy"
  - "hardware"
relatedSlugs:
  - "2026-05-15-nvidia-h200-china-sales-limbo-en"
  - "2026-05-10-trump-china-tech-ceo-chips-en"
  - "2026-05-21-alibaba-zhenwu-m890-qwen37-china-ai-stack-en"
---

China's official technology security authorities have certified nine domestically designed AI processors for state procurement — the first time AI training and inference chips have been added to the country's "Anke" security evaluation framework. The certifications, announced Tuesday by the China Information Technology Security Evaluation Centre and the National Secrecy Science and Technology Evaluation Centre, create a new dedicated hardware category and formalize the government's move away from Nvidia and other foreign chip suppliers in sensitive computing environments.

The nine approved processors span seven vendors: Huawei's Ascend 310 and Ascend 910, Alibaba's T-Head Zhenwu M530 and M890, plus chips from Biren Technology, Hygon Information Technology, Iluvatar CoreX, MetaX, and Moore Threads. Each certification carries a three-year validity period.

## What the Anke Framework Means

The Anke certification — shorthand for China's Information Technology Security Evaluation framework — is the country's primary mechanism for determining which technology products are deemed "secure and reliable" for use in government agencies and state-owned enterprises. Products must pass evaluation by designated security certification bodies and meet specifications covering both technical performance and supply chain provenance.

Until this week, the Anke framework covered categories like servers, storage systems, network equipment, operating systems, and databases. The addition of an "AI training and inference chips" subcategory under computing hardware is significant: it signals that China's government now views AI accelerators as critical infrastructure in the same category as the foundational IT layers it has been systematically domesticating since at least 2020.

For vendors, Anke certification is often a prerequisite for large government contracts and procurement cycles at major state banks, energy companies, and telecom operators that are themselves required to purchase from the approved list.

## The Certified Chips

The two Huawei entries — the Ascend 310 and Ascend 910 — are the most strategically significant inclusions. The Ascend 910, particularly the 910B and 910C variants manufactured on SMIC's 7nm-class process without EUV lithography, has become the de facto Nvidia substitute for large-scale AI training in China. Huawei shipped roughly 812,000 AI chips last year and is projecting $12 billion in AI processor revenue for 2026 — a figure that would make it one of the world's largest AI chip revenue generators even without access to advanced lithography from ASML.

Alibaba's T-Head division contributed two entries: the Zhenwu M530, a mid-range inference-focused chip deployed extensively within Alibaba Cloud's domestic AI services, and the M890, a higher-performance variant released in late 2025 that has powered the company's Qwen 3 model serving at scale. The M890 was featured prominently in Alibaba's cloud presentation last week as part of the broader Zhenwu AI stack announcement.

The remaining five vendors — Biren, Hygon, Iluvatar CoreX, MetaX, and Moore Threads — represent the diversity of China's rapidly scaling domestic GPU ecosystem. Biren, which has faced some export restrictions on its most advanced BR100 GPU due to U.S. performance thresholds, contributes a chip below those thresholds. Hygon, a spinout with historical ties to AMD through a now-discontinued licensing arrangement, supplies x86-compatible AI chips to a range of Chinese enterprise customers.

## Notable Absences

Two prominent Chinese chip companies did not appear on the list: Cambricon Technologies, a publicly traded Chinese AI chip company, and Kunlunxin, the AI chip unit backed by Baidu. Certification bodies have indicated that exclusion from the current list does not imply a failed evaluation — companies must opt in by submitting products for testing, and there is no public record of which submissions were made or declined.

Cambricon has historically focused on edge inference rather than the large-scale training and cloud inference workloads the certification specifically covers. Kunlunxin, which has shipped chips to enterprise customers domestically, may have products in the evaluation pipeline for a future certification cycle.

## Acceleration of Technology Decoupling

The certification represents the latest structural step in a multi-year campaign to reduce Chinese government and state enterprise dependence on foreign technology. The campaign, originally driven by U.S. export controls implemented from 2019 onward, has intensified with each successive round of chip restrictions.

The October 2023 update to U.S. export control rules effectively blocked Nvidia's H100 and A100 from China. The October 2023 and October 2024 restriction updates further tightened performance thresholds, blocking export of Nvidia's H800 and A800 — chips Nvidia had designed specifically to fall below earlier control limits. The May 2025 restrictions added the H20, a China-specific GPU that had briefly become a volume product in the market, to the controlled list.

Each successive restriction accelerated domestic chip investment. Chinese government data cited in the South China Morning Post shows domestic semiconductor firms delivered 1.65 million AI GPUs in 2025, claiming 41% of domestic AI server shipments. The Anke certification process now gives those domestic chips a formal procurement pathway that effectively makes them the default for government-adjacent buyers.

## Market Implications

For Nvidia, the immediate commercial impact of the Anke certification is modest — the company has already been largely excluded from Chinese government procurement by the existing export restrictions. The more meaningful pressure comes from the signal it sends about the medium-term trajectory of the Chinese enterprise market, where Nvidia still competes for private-sector AI deployments.

Domestic Chinese chip alternatives have historically faced a significant capability gap versus Nvidia's H100 and H200 architectures, particularly on memory bandwidth and interconnect performance for large model training. Huawei's Ascend 910C has narrowed that gap for inference workloads but still trails on multi-node training efficiency, according to published benchmarks from Chinese research institutions.

The certification is best understood not as a statement that domestic chips are now equivalent to Nvidia — they are not yet, in absolute performance terms — but as a policy guarantee that procurement decisions in the public sector will increasingly be made on the basis of supply chain security rather than raw benchmark performance.

For the seven certified vendors, the implications are favorable in the near term: government and state enterprise procurement provides a significant volume baseline that reduces the financial risk of continued R&D investment in next-generation architectures. Huawei's projected $12 billion in AI chip revenue for 2026 is already being driven largely by state-adjacent buyers who have been operating ahead of formal procurement policy; the certification formalizes and expands that channel.

## Looking Ahead

China's Ministry of Industry and Information Technology has indicated that additional certification rounds are planned, with the evaluation criteria expected to expand in scope to cover specialized edge inference chips and AI networking hardware. The current list covers seven vendors; industry analysts expect the next update to include Cambricon, potentially Kunlunxin, and possibly chips from startups including Enflame Technology and Tianshu Zhixin that have been shipping volume products to Chinese cloud operators.

For observers of the global AI chip supply chain, Tuesday's announcement is another data point in a clear direction: the world's largest AI computing market is systematically segmenting its hardware supply chain, and the gap between China's domestic AI stack and the global frontier is narrowing faster than the export control regime anticipated.
