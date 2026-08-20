---
title: "927 AI Articles, 380 Clicks, Then a Cliff: First-Party Search Data from faq.com.tw"
summary: "Google Search Console, 18 May to 16 August 2026: faq.com.tw, an AI-written bilingual tech news site with 1,873 URLs, recorded 380 clicks. The same owner's human-written site, www.topclass.tw, recorded 359 clicks from 186 URLs. Search traffic on the AI site peaked around 28 clicks a day, then collapsed on 17 July — two and a half weeks before publishing stopped. Search Console showed no manual penalty. This is a first-party report of those numbers, not an explanation of why they happened."
category: "industry"
publishedAt: 2026-08-20
lang: "en"
featured: false
trending: false
sources:
  - name: "Google Search Console (first-party data)"
    url: "https://faq.com.tw"
  - name: "Google Search spam policies"
    url: "https://developers.google.com/search/docs/essentials/spam-policies"
tags:
  - "Google Search"
  - "Search Console"
  - "AI content"
  - "publishing"
  - "faq.com.tw"
  - "scaled content"
relatedSlugs:
  - "2026-07-13-google-search-gemini-flash-ai-blue-links-end-en"
  - "2026-07-10-cloudflare-pay-per-crawl-ai-content-monetization-en"
---

faq.com.tw is an AI-researched, AI-written technology news site, bilingual in English and Traditional Chinese, published from this repository onto Vercel. From 5 April 2026 to 3 August 2026 we shipped 927 English–Chinese article pairs — 1,854 Markdown files under `src/content/articles/`. The cadence was two waves a day, four commits per wave, four pairs a day. The sitemap lists 1,873 URLs.

The same owner, over the same months, also ran www.topclass.tw, a smaller human-written site. The only traffic source in this report is Google Search Console, search type Web, 18 May 2026 to 16 August 2026. In that window the two properties recorded almost the same number of clicks.

## The three-month table

| Metric | faq.com.tw | www.topclass.tw (human-written, same owner) |
|---|---|---|
| Clicks | 380 | 359 |
| Impressions | 75,300 | 55,600 |
| CTR | 0.5% | 0.6% |
| Average position | 9.4 | 11.8 |
| URLs | 1,873 | 186 |
| Clicks per URL | 0.20 | 1.93 |

One site published 1,873 URLs, the other 186. Over three months they produced 380 clicks and 359 clicks. Per URL, the human-written site received 9.6 times as many clicks. Average position on faq.com.tw was 9.4, against 11.8 on the human-written site. CTR was 0.5% against 0.6%. For three months the AI site collected 75,300 impressions at that average position. The later collapse happened to a property Google had already been showing.

## The cliff arrived before we stopped

Those totals hide the shape of the series, and the shape is the finding that is easiest to misread.

From 18 May through 11 June, clicks on faq.com.tw sat near zero.

From 17 June through 17 July the site had a real peak. The high days reached about 28 clicks and about 5,500 impressions.

After 17 July the series collapsed to zero. It stayed there through the end of the Search Console window on 16 August, and it is still there as of 20 August 2026.

A dead chart in August invites a simple story: we stopped writing, and traffic followed. Publication continued until 3 August — two and a half weeks after the collapse. The interval that matters is 17 July to 3 August. In those days the pipeline was still shipping four pairs a day, and the click series was already flat. A cause cannot arrive after its effect. The stop does not explain a drop that had already happened.

## A green manual-actions page

Google Search Console's manual-actions report showed no issues. The page was all green.

That observation excludes one class of event: a human reviewer at Google did not record a manual penalty against this site in the window we can see. It does not exclude automated spam classification, a core ranking update, a change in how Google crawls or serves the site, or any other system that never writes a row in that report. The 17 July break is compatible with an algorithmic or automated-systems event, in the narrow sense that it left no manual-action record. We do not have a name for the system.

## Hypotheses, all of them unproven

We do not know what happened on 17 July. The list below is speculation. Each item is a possibility, not a finding.

**Scaled content abuse, or a related spam-policy action.** Google's published spam policies define scaled content abuse as generating many pages primarily to manipulate search rankings and not helping users. The same page lists generative-AI tools used to produce many pages without added value as an example, and it defines site reputation abuse as third-party content published on a host mainly to borrow that host's ranking signals. Those are real, documented policies. Whether any of them fired on faq.com.tw on 17 July is unknown. This dataset does not establish a policy match.

**A core ranking update.** Core updates move sites without leaving a manual-actions row. We did not independently verify an update dated 17 July, and a date coincidence would not prove that an update, if one existed, targeted this site.

**Crawl budget.** A 1,873-URL property publishing four pairs a day can outrun how much Google is willing to recrawl. That is a speculation about discovery of new URLs. It is a weaker account of a site-wide cliff on URLs Google had already been showing. We do not have crawl-stats figures to test it.

**Index decay.** URLs can remain in a sitemap and drop out of serving. We did not measure indexed-URL counts day by day, so this remains untested.

A sentence of the form "Google is punishing AI content" is a conclusion these rows do not carry.

## The control site is a comparison with limits

www.topclass.tw is useful because the owner, the calendar, and the Search Console settings match. It is not a controlled experiment. The two sites cover different topics and different audiences. A 9.6× gap in clicks per URL can reflect subject matter, brand, query mix, and domain history as readily as it reflects "AI versus human." We are reporting the gap. We have not isolated a single cause.

The query list on faq.com.tw makes the same point from the other direction. Over three months the strongest query was `gemini 3.5 pro`, with 4 clicks and 99 impressions. Next were `tenstorrent` (3 clicks, 27 impressions) and `codex micro` (2 clicks, 225 impressions). `codex micro` had the most impressions of those three and still produced two clicks. No query produced more than four clicks. The 380 clicks were a long tail.

The corpus is still on the site. Search Console is still open, search type Web, same two properties. If the series on faq.com.tw leaves zero, that is the next measurement worth writing down. Until then, the record is the table, the dates, and a cliff that arrived while we were still publishing.
