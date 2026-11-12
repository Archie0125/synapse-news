---
category: industry
lang: en
published: '2026-11-12T06:29:55.865694+00:00'
sources:
- name: Hacker News
  url: https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/
- name: Engadget
  url: https://www.engadget.com/2314121/united-is-restricting-ai-agents-from-booking-flights/
- name: The Verge
  url: https://www.theverge.com/tech/1030838/ebay-ai-agents-meta-muse-agentic-shopping
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/openai-rolls-out-new-business-profiles-making-chatgpt-just-a-little-bit-more-like-google/
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/adobe-adds-more-ai-to-its-products-and-launches-an-mcp/
summary: 'The airline says the ban is about safety, but its CEO admitted the real
  reason on stage: ''I don''t want to create another middleman.'''
title: United and eBay Aren't Blocking AI Agents. They're Blocking a New Landlord
trending_theme: Platforms Push Back on AI Agents
type: analysis
---

United Airlines gave a long list of reasons for banning AI agents from booking its flights: exposed credentials, accidental purchases, misused MileagePlus miles, and an FAA rule that a human has to confirm their bag holds no explosives. All of these are true. None of them is the main reason.

CEO Scott Kirby gave the main reason himself, at an event the day before the ban was announced: "To be honest, I don't want to create another middleman."

That sentence explains this whole phase of the agent era. The fight isn't about safety and it isn't about bots. It's about who owns the customer, and the companies that own them now have decided to fight before the decision is made for them.

## Airlines have lost this fight before

United's reaction makes sense once you remember the last 30 years of airline distribution.

First came the global distribution systems: Sabre, Amadeus, Travelport. They took a fee on every booking. Then online travel agencies like Expedia and Booking took over the consumer front end. Then Google bought ITA Software in 2011 for about $700 million and built Google Flights on top of the same fare data airlines had been paying other people to show. Each layer took a share of margin and, more importantly, ownership of the customer.

Airlines have pushed back several times. In late 2010 American Airlines pulled its fares from Orbitz, and Expedia retaliated by burying American's flights. In 2015 Lufthansa added a €16 surcharge to tickets booked through GDS channels to push travelers to its own site. The industry's NDC standard is, in plain terms, a decade-long effort to get control of pricing and merchandising back from intermediaries.

Analyst Henry Harteveldt of Atmosphere Research put it plainly: United doesn't want "yet another, and potentially even more powerful, intermediary." The key words are *more powerful*. Kayak shows you a list, and you still pick the flight. An AI agent picks the flight for you. If ChatGPT or Meta's Muse decides you're flying Delta because it saved $14, United never gets to show you its seat upgrade, its credit card offer, or its loyalty program. Those are where airline profit actually comes from. The ticket itself mostly gets you through the door.

## eBay and Amazon are making the same move

eBay changed its user agreement in January to ban "buy-for-me agents" and "LLM-driven bots" that place orders without human review. In the past few weeks it appears to have gone further and blocked browsing too. A Verge reader who had used Muse to build a daily digest of watch listings found it had stopped working, and Muse began sending users to sites that mirror eBay listings instead.

That second detail matters. Block an agent and it doesn't give up. It goes around you, to scrapers, mirrors, and cached copies. The platform loses control of its own inventory data and still gets none of the relationship.

Amazon is the hardest line: no outside agents browsing or buying at all. Amazon sued Perplexity in November 2025 over its Comet browser agent, and has since blocked Muse. Target lets agents through some of the time. JPMorgan Chase restricted agent access to accounts in October. The pattern is consistent. Companies with a strong direct relationship and a loyalty or ads business to protect block agents. Companies without that leverage let them in.

Southwest is the useful comparison. It built a ChatGPT plugin and opened its inventory to the agent. That isn't Southwest being forward-thinking. Southwest never sold through the big OTAs and has long relied on direct bookings, so for a carrier with a smaller share of the network, being findable inside ChatGPT is worth more than defending a customer relationship it can't fully protect anyway. Where a company stands on agents tracks its market power.

## What nobody is talking about: the agents aren't even getting used yet

Here's the number that should get more attention. In its Q3 earnings, Uber said it handled 320 million trips and deliveries during the week of Halloween. AI agents accounted for about 500 Uber Eats orders and **four** rides.

Four.

So United, eBay, and Amazon aren't responding to traffic they're losing. They're blocking a threat that hasn't arrived, and that's why they're doing it now. Fighting a middleman after consumers already rely on it costs a lot. Ask any hotel chain that spent the 2010s paying Booking.com commissions of 15% or more and running "book direct" campaigns that mostly didn't work. Before the habit forms, blocking costs almost nothing, because nobody is using it yet.

The second thing being missed is the cost Harteveldt mentioned in passing: flight searches cost airlines money. Each fare query against a reservation system has a real compute and licensing cost. Agents don't search like people do. One "find me the cheapest way to Tokyo in March" request can generate hundreds of queries across dates and routes. A busy agent ecosystem would send airlines search bills that grow much faster than bookings. Shopping bots already pushed look-to-book ratios into the thousands in some markets. LLM agents would make that much worse.

## The AI companies are building the tollbooth

While the platforms block, the AI companies are adjusting. Look at what OpenAI just launched.

It retired its checkout and commission effort in March after it failed to catch on. On November 10 it released Business Hub, in beta: verified business profiles, a dedicated "business agent" that answers questions inside ChatGPT, and analytics on profile views, mentions, and website clicks. If that sounds like Google Business Profile plus Google Analytics, that's because it is the same model. Verified listings first, measurement next, paid placement after that. Benji Shomair, OpenAI's VP of Monetization, is presenting it, and his title tells you where it's going.

That changes how to read the dispute. OpenAI isn't asking United to let in an anonymous bot. It's offering United a verified, branded presence inside ChatGPT on OpenAI's terms. That's the same arrangement Google offered airlines 15 years ago, and airlines know where it led.

Adobe is going the opposite direction from United. At MAX it released a local MCP server that exposes Photoshop, Illustrator, After Effects, and Premiere functions to ChatGPT, Claude, and Gemini. VP Deepa Subramaniam said Adobe has no "need or desire" to limit what the endpoint exposes. That's a confident position, but Adobe's situation is different. Adobe doesn't sell a commodity seat on a plane. It sells the tool the work actually happens in. If Claude calls Photoshop's relighting feature, the user still pays for Creative Cloud. For Adobe, an agent sends more usage to its tools. For United, an agent is a buyer comparing it against everyone else.

That's the dividing line. **If an agent can easily swap you for a competitor, you'll block it. If the agent depends on you to get the job done, you'll open up to it.**

## The bear case

The best counterargument is that blocking has never held up long term. Airlines fought Google Flights and Google Flights won. Retailers fought price comparison sites, and those sites became a standard part of shopping. If agents get good enough, consumers will go wherever agents work, and the companies that blocked them will be the ones with less traffic. United's own ban accepts this partly: its fares stay on Kayak, Hopper, and Google Flights. It can block an agent from logging into your MileagePlus account. It can't stop an agent from reading Google Flights.

Fair. But it assumes agents will become a habit. Uber's four rides suggest that habit is far from formed, and Muse leaking a user's home address in September didn't help build trust. The platforms aren't betting they can block agents forever. They're betting they can stall until AI companies come to them for a licensed, verified deal, and then negotiate from a stronger position than they had with Google.

## What to Watch

1. **At least two more major US airlines will announce agent restrictions by mid-2027**, while at least one budget carrier copies Southwest and opens up. Airline responses will split by market power, as described above.
2. **OpenAI's Business Hub will add paid or sponsored placement within 12 months.** Verified profiles plus analytics is the setup for selling ads.
3. **The first major "agent access" licensing deal will be signed**, most likely between an AI lab and a large travel or retail platform, with per-query or per-booking fees. Blocking agents now is how platforms get to that table.
4. **MCP will become the standard way software companies cooperate with agents.** Expect Figma, Canva, and Autodesk to follow Adobe within two quarters. Tools that agents depend on will open up, and businesses agents could route around will stay closed.
5. **Watch the mirror sites.** If eBay's blocks push agents to scrapers and copies, expect eBay to start suing them, as Amazon did with Perplexity.

The agent era was supposed to remove the middleman. What's actually being negotiated is who gets to become the next one.