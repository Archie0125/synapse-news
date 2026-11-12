---
category: ai-ml
lang: en
published: '2026-11-12T18:36:17.785593+00:00'
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/github-agentic-workflows-ga/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- name: The Verge
  url: https://www.theverge.com/tech/1030838/ebay-ai-agents-meta-muse-agentic-shopping
- name: The Verge
  url: https://www.theverge.com/ai-artificial-intelligence/1030787/google-gemini-4-carbon-public-rollout
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/adobe-adds-more-ai-to-its-products-and-launches-an-mcp/
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/anthropic-launches-claude-meetings-to-turn-workplace-discussions-into-plans-and-tasks/
summary: The agent race will not be won by the smartest model, but by whoever gets
  permission to touch the transaction.
title: 'AI Agents Hit the Wall: Platforms Own the Permission Layer'
trending_theme: AI Agents Meet Platform Resistance
type: analysis
---

The smartest AI agent in the world is useless when eBay refuses to open the door. That is the uncomfortable correction arriving just as Silicon Valley declares that agents are ready to book trips, buy products, operate business software, and coordinate entire teams. Model makers are racing toward more autonomy, yet the businesses controlling inventory, payments, and customer accounts are discovering that “autonomy” often means surrendering their most valuable asset: the customer relationship.

The warning came from a mundane shopping task. Meta’s Muse had been assembling daily watch listings from eBay, complete with prices, shipping information, and condition notes. Then it stopped retrieving links. Tests by [The Verge](https://www.theverge.com/tech/1030838/ebay-ai-agents-meta-muse-agentic-shopping) produced similar failures, sometimes redirecting users to sites that mirrored eBay listings. eBay would not confirm a blanket block, but said it restricts unauthorized scraping and training while taking a “selective approach” to third-party agents.

This is not a minor compatibility bug. In January 2026, eBay changed its user agreement to prohibit “buy-for-me agents” and LLM-based bots from ordering without human review. Amazon has taken an even harder position against external shopping agents, while Target reportedly allows some browsing attempts and blocks others. Three major retailers, three variations of the same message: AI companies do not get universal transaction rights merely because their models can operate a browser.

The economics explain the resistance. eBay ended 2024 with approximately 134 million active buyers, $74.7 billion in gross merchandise volume, and $10.3 billion in revenue. An outside agent that compares every listing by total price, ignores promoted placement, and returns only one recommendation may serve the buyer beautifully. It also turns eBay’s carefully designed marketplace into a commodity database.

That strips away more than page views. It weakens sponsored listings, recommendation systems, seller promotion tools, cross-selling, and the behavioral data used to improve all of them. A platform-native assistant can be instructed to maximize conversion, retain users, and respect paid placement. A buyer-controlled agent is supposed to maximize the buyer’s interests. Those objectives overlap only until the cheaper watch sits below the sponsored one.

This is the part nobody is talking about: agent blocking is becoming a new form of distribution control. Platforms will not simply decide whether agents are safe. They will decide which agents are commercially acceptable, which actions those agents may perform, and who gets paid when an agent changes a customer’s decision. The future “open agent web” is already drifting toward preferred-agent agreements, licensed APIs, attribution requirements, and tolls on automated transactions.

We have seen a softer version of this conflict before. The robots.txt convention dates to 1994 and became RFC 9309 in 2022. Search crawlers were tolerated because the bargain was legible: Google indexed a page, then sent people back to websites where publishers and merchants could show ads or complete sales. Agents break that exchange. They can extract the information, make the comparison, complete the action, and keep the user inside ChatGPT, Claude, Gemini, or Muse. The platform supplies the inventory while the agent company owns the interface.

That is why the model arms race is starting to look detached from the commercial bottleneck. Google’s Gemini 4 Carbon can coordinate an agent “swarm” through Antigravity, turning one prompt into a team of workers. Its introductory API pricing is $2 per million input tokens and $10 per million output tokens—about one-fifth the reported price of OpenAI’s GPT-6 Astra and one-quarter that of Anthropic’s Fable 5.2. Even after the introductory prices double at the end of November 2026, [Carbon remains cheaper per token than those rivals](https://www.theverge.com/ai-artificial-intelligence/1030787/google-gemini-4-carbon-public-rollout).

Cheap intelligence does not purchase access. A swarm of ten agents blocked by the same marketplace is not ten times more useful; it is ten times more traffic hitting the same locked gate. In fact, swarms amplify the platform’s concerns: more requests, more scraping, more opportunities for prompt injection, and more ambiguity about which sub-agent authorized a purchase.

GitHub offers a more realistic picture of how agent adoption will work. Its Agentic Workflows, generally available since October 28, 2026 after a June preview, start agents with read-only permissions. Proposed changes are passed to separate jobs holding their own write tokens. Teams can add a reviewer gate before a write job executes, while a firewall and threat-detection step inspect the proposal. This is delegation designed as a permission chain, not an agent wandering through the repository with an administrator credential.

GitHub also puts a price fence around autonomy. AI Credits cost $0.01 each, with a default ceiling of 1,000 credits—or $10—per run. Other defaults include 5,000 credits per day, 400 credits for threat detection, and a 20-minute agent timeout. At the stated rate, that means a $50 daily ceiling and up to $4 allocated to checking a run. The `gh aw forecast` command estimates monthly spending before deployment.

Those controls matter more than the headline claim from an Accenture manager that one lead saved 29 hours per week—a figure [GitHub’s announcement did not explain how it measured](https://www.infoq.com/news/2026/11/github-agentic-workflows-ga/). The real product is not “29 hours saved.” It is the ability to answer five operational questions: What may the agent read? What may it propose? Who approves the write? How much may it spend? What evidence remains afterward?

GitHub’s design is not magic. Direct write permissions and custom jobs can bypass its protections, and its support for Actions Runner Controller with Docker-in-Docker introduces an awkward tradeoff: the sidecar is privileged by default even though the agent is supposed to follow least-privilege rules. Still, this is far closer to a deployable agent system than a browser bot impersonating a customer across arbitrary websites.

Adobe is taking a related approach. At MAX in November 2026, it announced a local Model Context Protocol interface exposing selected actions from Photoshop, Illustrator, After Effects, and Premiere to ChatGPT, Claude, and Gemini. Adobe is opening controlled verbs while retaining authority over what those verbs can do. That distinction matters to a company whose fiscal 2024 revenue reached $21.51 billion: it wants agent traffic without becoming an invisible rendering engine behind someone else’s subscription.

Anthropic’s Claude Meetings makes the same boundary visible in workplace software. Claude joins Google Meet as an identified participant, drafts plans while people talk, and accesses connected applications. But it will not join meetings containing external guests without administrator authorization, and it automatically leaves if an external guest appears. [Claude Meetings launched in beta for Team and Enterprise customers](https://techcrunch.com/2026/11/10/anthropic-launches-claude-meetings-to-turn-workplace-discussions-into-plans-and-tasks/), where identity and policy can be enforced. That is not friction added after the product; the friction is the product’s permission model.

The counterargument is real. Platforms have legitimate reasons to distrust external automation. A shopping agent can misunderstand condition notes, trigger fraud systems, expose account credentials, or generate a flood of returns. A workplace agent can leak customer data or act on a malicious instruction hidden in a document. Native platform agents also have better access to inventory, fulfillment status, and dispute systems than a browser-driving outsider.

But blanket blocking is a weak long-term strategy. If Muse consistently sends collectors to alternative marketplaces because eBay listings are inaccessible, eBay protects its interface while losing demand. Smaller sellers and platforms will have an incentive to publish agent-readable catalogs precisely because incumbents refuse. Resistance will therefore produce a split market: high-value platforms charging for controlled access, and challengers using agent compatibility as customer acquisition.

Model quality will continue improving, but the decisive contest has moved elsewhere. The winners will build trusted delegation networks spanning platforms, identity providers, payment systems, and enterprise administrators. Intelligence is becoming abundant. Permission is becoming scarce.

### What to Watch

1. **Paid agent access arrives in 2027.** Expect at least one major marketplace or travel platform to announce a preferred-agent program with transaction fees, attribution rules, rate limits, and paid placement. “Open access” will become a commercial tier, not a default property of the web.

2. **Read and write permissions split apart.** GitHub’s pattern will spread: agents inspect broadly, propose actions, and hand expensive or irreversible operations to a separately authorized executor. Purchases, production deployments, refunds, and data exports will require explicit thresholds and approval receipts.

3. **Access partnerships beat benchmark scores.** A model that scores two points lower but can transact across Adobe, airlines, retailers, and enterprise systems will be more valuable than a brilliant model blocked at checkout. Agent leaderboards will eventually need to measure successful authorized actions, not just reasoning tasks.

4. **Platforms make agents carry identity.** Anonymous browser automation will be squeezed out by signed agent identities, revocable scopes, audit logs, and liability terms. By the end of 2027, the defining question will no longer be “Can the agent do it?” It will be “Who authorized it, under whose rules, and who pays when it goes wrong?”