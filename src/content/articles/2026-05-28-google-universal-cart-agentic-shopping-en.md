---
title: "Google's Universal Cart Brings Agentic Shopping Across Search, Gmail, YouTube, and Gemini"
summary: "Google is launching Universal Cart, a cross-retailer AI shopping hub that lets users add items from any Google surface and have Gemini monitor prices, surface deals, and complete purchases through a new Agent Payments Protocol. The rollout begins in the US this summer with Nike, Walmart, Sephora, Target, and major Shopify merchants."
category: "products"
publishedAt: 2026-05-28
lang: "en"
featured: false
trending: true
sources:
  - name: "Google Blog"
    url: "https://blog.google/products-and-platforms/products/shopping/google-shopping-cart/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/19/googles-new-universal-cart-wants-to-follow-your-entire-shopping-journey-across-the-internet/"
  - name: "Retail Dive"
    url: "https://www.retaildive.com/news/google-launches-cross-retailer-universal-cart/820957/"
tags:
  - "google"
  - "ai-shopping"
  - "ecommerce"
  - "gemini"
  - "agentic-commerce"
relatedSlugs:
  - "2026-05-28-microsoft-cancels-claude-code-licenses-copilot-cli-en"
  - "2026-05-24-google-gemini-35-flash-agentic-model-en"
  - "2026-05-20-google-gemini-spark-personal-ai-agent-en"
---

Google announced Universal Cart at I/O 2026 on May 19, and the product is now rolling out to US users this summer — a single, AI-powered shopping cart that follows you across every Google surface and actively works on your behalf to find better prices, flag out-of-stock items, and complete purchases. It is the most consequential move Google has made in e-commerce since it eliminated transaction fees for Google Shopping in 2020, and it is a direct shot at Amazon's position as the default starting point for product search.

Universal Cart works across Google Search, the Gemini app, YouTube, and Gmail. When you see a product you want — in a search result, in a YouTube review, in a promotional email — you add it to the cart. The cart then does the work you would otherwise do manually: it monitors price history, alerts you when prices drop, notifies you when out-of-stock items become available, and can complete checkout with Google Pay or transfer the order to the merchant's own checkout flow.

## How It Works

The technical architecture of Universal Cart is built on three interlocking components: the cart interface itself, Gemini as the intelligent layer on top, and the Agent Payments Protocol (AP2) that governs how agentic transactions are authorized and executed.

The cart interface is persistent across Google products. It remembers what you've added whether you're in mobile Search, desktop Gemini, or watching a YouTube video. Items can be added via standard "Add to Cart" buttons on merchant integrations, via conversational prompting ("add this to my cart"), or — for qualifying merchants — by having Gemini automatically identify products from visual or textual content you're interacting with.

Gemini functions as the active intelligence layer. It doesn't just store your items; it watches them. Price drops trigger notifications. Historical price data is surfaced so you can see whether a claimed sale is genuine or whether the item was more expensive last week. Compatibility checks run automatically for multi-component purchases — if you're building a PC, Gemini will warn you if the GPU you've added won't work with the motherboard already in your cart.

AP2 is the most technically significant new component. It is Google's standard for authorizing AI agents to make financial transactions on behalf of users. Users define spending limits, approved merchants, and specific product criteria before an agentic transaction can occur. The agent can only execute a purchase when all criteria are met. Merchants stay as the merchant of record throughout — Google is facilitating the transaction infrastructure, not taking on financial or inventory risk itself.

## The Retailers

The initial US launch includes a set of retailers that covers significant surface area of consumer spending: Nike, Sephora, Target, Ulta Beauty, Walmart, and Wayfair, along with Shopify merchants including Fenty Beauty and Steve Madden. The Shopify integration is particularly significant — Shopify powers roughly 15% of total US e-commerce, and Universal Cart integration means those hundreds of thousands of merchants inherit agentic checkout functionality without custom engineering work.

Google describes this as the "merchant stays merchant of record" model deliberately. The concern that Google was positioning itself as a marketplace — competing directly with the retailers it sends traffic to — has been a recurring friction in Google's shopping relationships. AP2 is designed to resolve that by making the payment flow transparent and preserving brand control at checkout.

## Why This Is Different From Google Shopping History

Google has tried to win e-commerce before. Google Product Listing Ads launched in 2012. Google Shopping Actions launched in 2019. Google free listings launched in 2020. Each version expanded Google's surface area in commerce but didn't fundamentally change user behavior, because none of them changed where users actually began their shopping journeys.

Universal Cart is a different category of product because it is not trying to capture search-intent shopping. It is trying to capture ambient shopping — the browsing-while-watching, reading-while-scrolling mode that accounts for an enormous portion of product discovery but has never had a good persistent storage mechanism.

If someone watches a YouTube review of a running shoe, adds it to Universal Cart without leaving the video, gets a price drop notification three days later, and completes the purchase in two taps, they haven't started a new shopping session on Amazon. They've completed a purchase that started in Google's ecosystem and ended there. That is the behavioral change Google is trying to engineer.

## The Amazon Question

Amazon's market position in product search is the implicit backdrop for everything about Universal Cart. Surveys consistently show that roughly 60% of US online shoppers begin product searches on Amazon rather than Google, a shift from the early 2010s when Google was the dominant product discovery engine. Amazon has converted its logistics infrastructure, Prime membership, and seller relationships into a default behavior that is very hard to dislodge.

Universal Cart does not attack that default behavior directly — it tries to make it irrelevant by capturing purchase intent before it has a chance to travel to Amazon. If the product is already in the Google cart, added mid-YouTube-video or mid-Gmail-read, the question of whether to search Amazon doesn't arise.

The question is whether AP2 and the agent-mediated purchase flow is smooth enough to close that loop. Google Pay's checkout success rates and the quality of merchant integrations will determine whether Universal Cart becomes a genuine behavioral alternative to Amazon's one-click purchasing, or another feature that gets added to carts and then abandoned before checkout.

## What Brands Need to Know

For retail brands and their digital marketing teams, Universal Cart creates both an opportunity and an obligation. The opportunity: product discovery and purchase can now happen within YouTube content, Gmail promotions, and Gemini conversations without requiring the user to navigate to a separate shopping session. The obligation: brands need to integrate with Universal Commerce Protocol (UCP), Google's merchant-facing API, to ensure their products appear correctly in cart search results, trigger accurate price history data, and enable seamless AP2 checkout.

Brands that integrate deeply with UCP will have structural advantages in Universal Cart's surfacing — similar to how Amazon Prime eligibility affects Buy Box prominence. Brands that don't integrate will still be discoverable but will lose the native checkout experience, with users transferred to their own checkout flows rather than completing within Google's ecosystem.

The rollout timeline from Google positions this summer as the critical integration window for retail brands. The merchants who optimize for Universal Cart now are positioning for the back-to-school and holiday shopping seasons that will be the real-world test of whether agentic commerce becomes a mainstream consumer behavior.
