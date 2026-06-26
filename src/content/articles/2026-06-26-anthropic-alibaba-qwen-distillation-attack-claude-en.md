---
title: "Anthropic Accuses Alibaba's Qwen Lab of History's Largest AI Distillation Attack"
summary: "Anthropic formally notified the White House and U.S. senators that Alibaba's Qwen AI lab deployed 25,000 fraudulent accounts to run nearly 29 million unauthorized Claude conversations over six weeks, targeting the software engineering and agentic reasoning capabilities of its Mythos Preview models. The campaign dwarfs all previous known distillation attacks combined, and has already prompted bipartisan legislation to sanction Chinese firms caught stealing U.S. AI model outputs."
category: "ai-ml"
publishedAt: 2026-06-26
lang: "en"
featured: true
trending: true
sources:
  - name: "The Next Web: Anthropic accuses Alibaba of running largest distillation campaign against Claude"
    url: "https://thenextweb.com/news/anthropic-accuses-alibaba-distillation-claude-qwen"
  - name: "Tom's Hardware: Anthropic claims Alibaba illicitly distilled Claude"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-claims-that-chinas-alibaba-illicitly-distilled-its-models-from-april-to-june-2026-says-effort-involved-25-000-fake-accounts-and-28-8-million-exchanges-on-claude"
  - name: "Cybersecurity Insiders: Anthropic accuses Alibaba of Distillation Attack on Claude"
    url: "https://www.cybersecurity-insiders.com/anthropic-accuses-china-alibaba-of-conducting-distillation-attack-on-claude-ai-models/"
  - name: "CryptoBriefing: Anthropic accuses Alibaba using 25,000 accounts to probe Claude"
    url: "https://cryptobriefing.com/anthropic-accuses-alibaba-claude-distillation-attack/"
tags:
  - "Anthropic"
  - "Alibaba"
  - "Qwen"
  - "distillation"
  - "AI security"
  - "US-China"
  - "Claude"
  - "export controls"
relatedSlugs:
  - "2026-06-13-trump-anthropic-fable5-mythos-export-controls-en"
  - "2026-06-06-us-chip-ban-chinese-overseas-subsidiaries-en"
  - "2026-06-22-freefable-400-experts-challenge-us-fable-mythos-ban-en"
---

The U.S.-China AI competition entered dangerous new territory this week when Anthropic formally accused Alibaba's specialized Qwen AI laboratory of orchestrating the largest known attack on any frontier AI model in history. In letters sent to White House officials and U.S. senators, the company described a meticulously coordinated campaign that ran nearly 29 million unauthorized Claude conversations through roughly 25,000 fraudulent accounts over six weeks—all aimed at stealing the cognitive architecture of its most advanced models before export controls could make such access impossible.

The allegations mark the first time Anthropic has publicly identified a Chinese technology giant, rather than a smaller AI startup, as the mastermind of a distillation attack. The escalation has rattled Washington and sent a bipartisan pair of senators rushing to draft emergency sanction legislation.

## The Anatomy of a Distillation Attack

To understand why Anthropic's accusation carries such weight, it helps to understand what distillation actually means in this context. Model distillation is a legitimate machine-learning technique in which a smaller, faster model is trained to mimic the outputs of a larger, more capable one—a kind of AI apprenticeship that compresses knowledge without transferring the original model weights.

When weaponized as "adversarial distillation," the technique becomes a form of AI espionage. An attacker with API access systematically queries a frontier model with millions of carefully designed prompts, harvesting its responses to build a training dataset. That dataset is then used to fine-tune a domestic model, effectively bootstrapping capabilities the attacker could never develop independently—at a fraction of the cost and time of original research.

The technique is particularly dangerous because it exploits the commercial accessibility of frontier models. Anthropic cannot wall off Claude entirely; the product is a revenue-generating chatbot. But by making Claude publicly available, Anthropic has also made its intelligence extractable at scale.

## A Campaign of Unprecedented Scale

The numbers Anthropic presented are staggering. Between April 22 and June 5, 2026, operators connected to Alibaba's Qwen AI laboratory ran 28.8 million exchanges with Claude through approximately 25,000 fraudulent accounts—accounts engineered to circumvent Anthropic's geographic controls that explicitly prohibit access from inside China.

The campaign targeted Claude's "software engineering and agentic reasoning" capabilities specifically—the same high-value skills embedded in Anthropic's Mythos Preview model line, which the U.S. government has placed under export restrictions. The goal, Anthropic told lawmakers, was to "accelerate China's ability to reach Anthropic's advanced Mythos Preview capabilities."

For scale: in February 2026, Anthropic disclosed three separate distillation campaigns attributed to smaller Chinese AI firms—DeepSeek, MiniMax, and Moonshot AI—that collectively generated approximately 16 million exchanges through roughly 24,000 accounts. The Alibaba operation, in a single unified campaign, exceeded that combined total by nearly 80 percent.

## The Qwen Connection

Alibaba's Qwen team has rapidly emerged as one of China's most formidable AI research organizations. Its open-weight model series has repeatedly topped international benchmarks, and the division has attracted particular attention from U.S. national security officials for the speed at which its capabilities appear to be advancing—advances that American officials have struggled to fully explain given the hardware constraints China's AI sector ostensibly faces.

Anthropic's letter frames the distillation campaign as a deliberate competitive strategy rather than opportunistic data theft. Rather than investing the years and tens of billions of dollars required to train a frontier model from scratch on legally obtained data, the alleged operation attempted to harvest Anthropic's research investment by turning its own commercial product against it.

Alibaba declined to comment on the allegations when contacted by reporters.

## Defying the White House

The timing of the alleged campaign makes the provocation particularly pointed. In April 2026, OSTP Director Michael Kratsios published a government memo formally identifying AI model distillation as a national security threat and committing the White House to share intelligence with U.S. AI labs about foreign distillation campaigns.

Anthropic's letter told officials that the Alibaba operation unfolded in the weeks after that memo was published—and continued until early June. "This campaign occurred in defiance of the administration's warnings," the company wrote, framing the activity not merely as a terms-of-service violation but as a calculated geopolitical provocation against an explicit White House policy statement.

## Three Demands, One Escalation

The letter contained three specific policy requests that together represent a significant expansion of what AI companies have previously asked from government.

First, Anthropic called for antitrust guidance that would explicitly allow U.S. AI companies to share intelligence about distillation campaigns with one another without competition-law exposure. The rationale: individual companies lack the visibility to monitor coordinated state-adjacent actors, and information-sharing is the natural countermeasure—but currently exists in a legal gray zone.

Second, the company renewed its push for continued and expanded export controls on advanced AI chips. The implicit argument: hardware restrictions alone are insufficient if Chinese labs can extract the functional intelligence of frontier models through API interactions, but they remain a necessary layer of defense that must be sustained.

Third, and most aggressively, Anthropic called for direct financial and legal penalties against any firm caught using distillation to extract capabilities from U.S. AI systems—framing the technique as IP theft even when it exploits intentionally public-facing products. This ask is new territory: it would effectively criminalize a machine-learning technique when applied to U.S. systems by adversary-linked actors.

## Bipartisan Response

The legislative reaction was unusually swift. Senators Bill Hagerty (R-TN) and Andy Kim (D-NJ) jointly announced plans to introduce amendments to defense authorization legislation that would "blacklist or sanction any Chinese firm found to be improperly accessing US AI model output." The bipartisan framing is notable: AI security has become one of Washington's rare areas of genuine cross-party agreement, cutting through the partisan gridlock that stalls most tech regulation.

The proposed mechanism would go beyond existing export controls. Rather than simply restricting hardware access, it would create a punitive legal framework targeting the extraction of model intelligence itself—an acknowledgment that the front line of the AI race has moved from silicon to software.

## The Deeper Threat

The Alibaba episode illustrates a structural vulnerability in the economics of frontier AI that no export control can fully address. Training a frontier model from scratch requires enormous compute—precisely the hardware that controls are designed to restrict. But distillation requires only inference compute, which is far cheaper and more widely available. An attacker needs only API access and patience to run millions of queries.

If large-scale distillation campaigns can meaningfully close the capability gap between frontier U.S. models and Chinese competitors, the fundamental premise of AI export controls—that hardware scarcity translates into durable model capability advantages—becomes shakier. Anthropic's letter is, in part, a warning that the arithmetic of the AI competition is changing in ways that existing policy frameworks were not designed to handle.

The company is asking Washington to catch up before the gap closes entirely.
