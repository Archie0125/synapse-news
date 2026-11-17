---
category: ai-ml
lang: en
published: '2026-11-13T06:25:15.419380+00:00'
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/github-agentic-workflows-ga/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- name: Hacker News
  url: https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/
- name: The Verge
  url: https://www.theverge.com/tech/1030838/ebay-ai-agents-meta-muse-agentic-shopping
- name: The Verge
  url: https://www.theverge.com/ai-artificial-intelligence/1030787/google-gemini-4-carbon-public-rollout
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/adobe-adds-more-ai-to-its-products-and-launches-an-mcp/
summary: Companies love AI agents until an outside agent controls the purchase, the
  data, and the customer relationship.
title: The Agent Wars Are Really About Who Owns the Customer
trending_theme: AI Agents Become the Interface
type: analysis
---

The most important AI product launch of 2026 may be a rejection screen. United Airlines is blocking unauthorized agents from booking flights. eBay appears to be keeping Meta’s Muse away from its listings. Amazon has already shut out external shopping agents. These companies are not afraid that agents are useless. They are afraid that agents are becoming useful enough to stand between them and their customers.

That distinction matters. Chatbots answer questions; interfaces control what happens next. An agent that compares prices, edits a video, investigates a failed build, calls customer service, and authorizes a purchase is no longer a feature inside software. It is the layer through which people operate software. The underlying apps risk becoming interchangeable suppliers of inventory, data, and actions.

We have seen this movie before, but the stakes are higher. Web browsers weakened the grip of desktop operating systems in the 1990s. Google turned websites into destinations reached through search. Apple’s 2008 App Store took control of mobile distribution and payment. Agents compress all three functions—discovery, decision, and transaction—into one conversation. If that conversation happens in Gemini, ChatGPT, Claude, or a company’s internal assistant, the airline, retailer, and creative app may never get the user’s full attention.

Google is betting that more intelligence will accelerate this shift. Its Gemini 4 Carbon model is being introduced at $2 per million input tokens and $10 per million output tokens, before those rates double at the end of November. Even after the increase, Google says Carbon will remain cheaper per token than OpenAI’s GPT-6 Astra and Anthropic’s Fable 5.2. More revealing than the benchmark race is Carbon’s preview “swarm” mode in Antigravity: one prompt can dispatch a coordinated group of agents for long-running coding or research work.

The obvious story is that agents are getting smarter. The more important story is that one user request is becoming dozens or hundreds of machine actions. Cheap tokens do not guarantee cheap work when a swarm repeatedly searches, plans, checks, and retries. An agent interface therefore needs something the graphical interface never had: a meter, a mandate, and an audit trail for every task.

[GitHub’s Agentic Workflows](https://www.infoq.com/news/2026/11/github-agentic-workflows-ga/) offers the clearest blueprint so far. After entering public preview in June 2026, it became generally available on October 28. Agents begin with read-only access inside sandboxed containers. Proposed changes are passed to separate jobs holding their own write tokens, while a threat-detection job scans the output. The default ceiling is 1,000 AI Credits, or $10, per run; enterprise defaults include 5,000 credits per day, 400 credits for threat detection, and a 20-minute agent timeout.

Carbon makes agents more capable. GitHub is trying to make them governable. The second problem will decide adoption.

GitHub’s design is not magic armor. Direct write permissions and custom workflow jobs can bypass its protections. Its Kubernetes setup can also place a privileged Docker-in-Docker sidecar beside an agent designed around least privilege. Accenture says one lead saved an estimated 29 hours per week, but GitHub’s announcement does not explain the measurement. That number belongs in the marketing column until somebody publishes the baseline, task mix, and failure rate.

Still, GitHub has identified the right unit of trust: not “Do we trust this model?” but “Which action may this model take, with which credential, under which budget, and who approves the irreversible step?” That is a much better question than arguing over whether a benchmark moved three points.

United’s ban exposes the same issue from the opposite direction. The airline says third-party agents could expose payment credentials, trigger unintended purchases, alter accounts, or spend MileagePlus miles. It also points to federal requirements that passengers personally confirm their luggage does not contain prohibited materials. Those are legitimate concerns. A model should not improvise a legal attestation because it found a cheap connection through Denver.

But the commercial motive is impossible to miss. United already tolerates intermediaries such as Kayak, Hopper, and Google Flights. What it does not want is a new intermediary with enough context to compare every fare, ignore carefully designed upsells, and own the conversation before and after the purchase. Southwest is taking a different route by making its inventory visible through ChatGPT. One airline sees an acquisition channel; the other sees a potential landlord.

The same fault line runs through commerce. eBay’s January 2026 user-agreement update prohibited “buy-for-me” agents and LLM-driven bots from ordering without human review. Meta’s Muse could nevertheless browse eBay listings and assemble daily watch digests until access apparently stopped. Amazon blocks outside agents, while Target has reportedly allowed some browsing and blocked other attempts. Meanwhile, eBay continues putting AI into its own discovery and selling tools.

That is not inconsistency. It is platform strategy: “Our agent may mediate our marketplace; your agent needs permission.”

Adobe has chosen a more open position. At MAX, it announced a local Model Context Protocol interface that can expose functions from Photoshop, Illustrator, After Effects, and Premiere to ChatGPT, Claude, and Gemini. Firefly is also gaining an always-on agent, video assembly, selective image editing, and a Builder prototype tool that pushes toward Figma’s territory. Adobe already offers models from Google, Runway, ElevenLabs, OpenAI, Kling, ByteDance, and Black Forest Labs. Its wager is that Creative Cloud can remain valuable as the action layer even when another company owns the conversational interface.

Here’s what nobody is talking about: agent permissions will become a pricing system.

Retailers will not simply choose between “open” and “blocked.” They will create paid and negotiated lanes. Browsing may be free but rate-limited. Real-time inventory, loyalty pricing, reservation holds, returns, and purchases will require verified identity, scoped payment authority, and commercial agreements. Platforms will charge agents for reliable access—or demand referral fees when an agent delivers a customer. Today’s anti-bot wall becomes tomorrow’s agent tollbooth.

This also explains why agents threaten more than website traffic. A human shopper sees sponsored placement, bundles, loyalty prompts, and urgency banners. A disciplined agent asks for total cost, delivery date, cancellation terms, and expected quality. That can reduce the value of interface tricks and make products easier to compare. Companies with genuine price or service advantages should welcome that. Companies dependent on friction, confusing tiers, or captive attention will resist.

The bear case deserves respect. Agents still make incorrect assumptions, lose context, and can be manipulated by hostile instructions embedded in webpages or documents. A mistaken summary is annoying; an unwanted airline ticket, deleted repository, or published campaign is expensive. Consumers may also prefer a known app for high-stakes purchases. The answer, however, is not permanent prohibition. It is staged authority: search, recommend, prepare, request approval, execute, and produce a receipt.

The winning interface will not be the agent with the funniest personality or the highest isolated benchmark. It will be the one that can prove what it did, stay inside a budget, recover from failure, and carry authority across services without handing over a master password. Capability gets the demo. Permission gets the market.

## What to Watch

- **By mid-2027, major platforms will publish separate agent permissions for browsing, quoting, reserving, and purchasing.** A single “allow access” switch cannot survive contact with money, loyalty points, regulated attestations, and corporate data.

- **United will eventually admit certified agents, but on United’s terms.** Expect identity checks, approved partners, rate limits, and liability clauses—not a return to unrestricted browser automation.

- **Agent budgets will become standard enterprise policy.** GitHub’s $10-per-run ceiling is an early template. Coding, research, customer-service, and creative agents will be assigned both spending caps and action caps.

- **Adobe’s model will pressure workplace software vendors.** If users can operate Photoshop or Premiere from an outside assistant, other products will need to expose actions or risk becoming invisible. Pricing will move from seats toward actions, credits, throughput, and completed work.

- **The next platform war will be fought over receipts.** The agent that can show which model acted, which data it read, what permission it used, how much it spent, and how to reverse the result will beat a smarter agent that merely says, “Done.”