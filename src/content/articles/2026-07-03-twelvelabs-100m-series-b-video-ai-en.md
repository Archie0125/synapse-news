---
title: "TwelveLabs Raises $100M to Build the Intelligence Layer for the World's Video Archives"
summary: "Video AI startup TwelveLabs has closed a $100 million Series B led by NEA and NAVER Ventures, with Amazon signing on as its preferred cloud partner. The funding accelerates TwelveLabs' vision of 'video superintelligence' — a full-stack cognitive system that makes every frame, sound, and spoken word in any video archive machine-readable and actionable by AI agents."
category: "ai-ml"
publishedAt: 2026-07-03
lang: "en"
featured: false
trending: true
sources:
  - name: "GlobeNewswire"
    url: "https://www.globenewswire.com/news-release/2026/07/01/3320545/0/en/twelvelabs-raises-100-million-in-series-b-funding-to-build-video-superintelligence.html"
  - name: "TwelveLabs Blog"
    url: "https://www.twelvelabs.io/blog/twelvelabs-series-b-100m"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/07/01/twelvelabs-raises-100m-bring-superintelligence-ai-video-models/"
tags:
  - "video AI"
  - "multimodal"
  - "Series B"
  - "video understanding"
  - "agentic AI"
relatedSlugs:
  - "2026-07-01-anthropic-claude-sonnet-5-agentic-launch-en"
  - "2026-07-01-higgsfield-ai-video-5b-valuation-500m-revenue-en"
---

The world generates roughly 720,000 hours of new video content every day. Almost none of it is computationally accessible. Text can be indexed, searched, and reasoned over by AI systems in milliseconds. Video — despite containing far richer information about the physical world than any text corpus — largely remains a black box to machines, queryable only by the metadata humans attach to it.

TwelveLabs, a San Francisco and Seoul-based AI startup, has spent the last three years trying to fix that. And on Tuesday, the company announced $100 million in Series B funding to accelerate what it is calling "video superintelligence" — a full-stack cognitive architecture that can perceive, remember, and reason across any video collection at machine speed.

The round was co-led by NEA and NAVER, the South Korean internet giant whose venture arm has backed TwelveLabs since its earliest stages. Additional investors include Amazon, Radical Ventures, Korea Investment Partners, Index Ventures, Quadrille Capital, and Red Bull Ventures. In a separate but simultaneous announcement, Amazon designated AWS as TwelveLabs' preferred cloud partner, with early model releases optimized for Trainium chips launching on AWS first — a pairing that reflects the growing importance of hardware-software co-design in AI infrastructure deals.

## What Video Superintelligence Actually Means

TwelveLabs' technical architecture rests on three interlocking capabilities the company calls Perception, Memory, and Reasoning.

**Perception** is the ingestion layer. Rather than treating video as a sequence of image frames, TwelveLabs' models process it as a rich multimodal stream: visual motion, ambient audio, speech transcription, and on-screen text all feed into a unified representation simultaneously. This is harder than it sounds. Most video AI systems either focus on visual content and ignore audio, or treat speech as a separate pipeline and miss the visual context. Synchronizing all four signal types into a coherent model requires architectural choices that the company says distinguish its approach from most commercial alternatives.

The Marengo embedding model — the company's third-generation video representation system — encodes these multimodal signals into a searchable vector space. An engineer or agent can query Marengo with natural language ("find every moment where a customer expresses frustration during a support call") and retrieve time-stamped clips with sub-second latency, even across archives containing thousands of hours of footage.

**Memory** converts that search capability into structured data. The companion Pegasus model ingests video and produces output formats that downstream systems can actually use: scene boundaries, entity lists, temporal segments, and semantic summaries indexed by timestamp. Rather than returning raw video clips in response to a query, Pegasus builds a machine-readable knowledge graph of the video's contents — the kind of structured representation that enables genuine reasoning, not just retrieval.

**Reasoning**, the third layer and the company's current development frontier, enables distributed analysis across time. The goal is a system that can identify patterns, track changes between clips, and answer causal questions that require connecting information from different moments in the same video — or across different videos in the same archive.

## Where the Market Is Going

The business case for video intelligence is broad enough to span industries that rarely share technology vendors. Sports leagues want to automatically tag every play in decades of archival footage. Security operations centers want to query surveillance camera networks in natural language rather than reviewing hours of recordings. Media companies want AI systems that can identify licensing violations by finding unauthorized clips across the internet. Insurance investigators want to automatically correlate dashcam footage with incident reports. Training data companies want to extract labeled examples of specific human behaviors from industrial video feeds.

What these use cases share is that they require understanding video at a semantic level that previous approaches couldn't achieve. Frame-level classification can tell you "this frame contains a car." Marengo can tell you "this is the moment the driver's expression changes from alert to distressed, three seconds before the collision, with the audio capturing a screech of brakes."

TwelveLabs has been quietly building customer relationships across these verticals, though it hasn't disclosed revenue figures. The company's Snowflake integration and AWS AI Competency recognition suggest it is positioned for enterprise procurement workflows rather than pure developer-API plays — a go-to-market orientation that tends to produce larger deal sizes and stickier contracts.

## The Video AI Competitive Landscape

TwelveLabs competes in a segment that has attracted significant attention since multimodal AI models began demonstrating video understanding capabilities. Google DeepMind's Gemini models include video input processing, and OpenAI's Sora and its successors generate video from text. But TwelveLabs is positioning against a different problem than generation: understanding and indexing existing video at scale, a workload that requires different architectural choices than the generative models dominating headlines.

Higgsfield AI, the video generation startup that recently disclosed $500 million in revenue and a $5 billion valuation, represents the creative generation side of the market. TwelveLabs is targeting the analytical intelligence side — understanding what's already on screen, not creating new content. The two applications are complementary and serve largely different buyers.

The NAVER connection also matters competitively. As one of Asia's largest internet platforms, NAVER generates and manages enormous quantities of video content across its search, media, and e-commerce properties. TwelveLabs' technology embedded in NAVER's infrastructure would provide the startup with one of the highest-volume production deployments in the world — a validation flywheel that helps attract both customers and research talent.

## Why This Matters Now

The timing of this raise coincides with the emergence of agentic AI systems — autonomous software agents that can browse, analyze, and act on information without constant human supervision. Text-based agents have made significant progress because the internet is largely text. But the physical world — manufacturing floors, retail stores, traffic intersections, hospital wards, construction sites — is not text. It is video.

TwelveLabs' $100 million bet is, at its core, a bet that the next major frontier for AI capability isn't making language models smarter about written language. It's giving AI systems the ability to see the world clearly enough to act within it.

The founding premise: "The world does not happen in text. It happens in motion." If TwelveLabs is right, the company that builds the intelligence layer for video owns a piece of every AI agent that will ever interact with the physical world.
