---
category: developer-tools
faqs:
- answer: For each app, the scraper returns pricing plans with features, ratings and
    rating distributions, developer details, launch date and category ranks. With
    reviews on, it also returns each review's stars, date, text, merchant country,
    how long the merchant used the app and the developer's reply.
  question: What data can be pulled from the Shopify App Store for competitor tracking?
- answer: Comparing pricing across ten competing apps means opening ten listings by
    hand, and catching a new rival or a fresh one-star review means checking every
    day. Automating it turns public listings into a daily feed of changes.
  question: Why would a Shopify app developer automate this?
- answer: No. The post's author built the Shopify App Store Scraper on Apify and discloses
    that it is a paid tool, so the tutorial is also a product pitch.
  question: Is the tool in this tutorial free?
featured: false
lang: en
publishedAt: '2026-11-12T05:55:15+00:00'
relatedSlugs: []
sources:
- name: Dev.to
  url: https://dev.to/aurelix_solutions/track-shopify-app-store-competitors-pricing-plans-category-ranks-and-new-reviews-in-python-3ap3
summary: Shopify app competitor data is all public but painful to compare by hand.
  A paid scraper fixes that, though the real value is the daily alert feed, not the
  table.
tags:
- developer-tools
- products
- startups
title: 'Track Shopify App Store competitors: pricing plans, category ranks and new
  reviews in Python'
trending: false
type: news
---

If you build a Shopify app, the App Store is your market map. Your competitors' plans and prices are public, so is where they rank in your category, and every merchant review (with the developer's reply) is right there. What the App Store does not give you is a table: comparing ten email apps' entry prices means opening ten listings and copying numbers by hand, and noticing a new competitor or a fresh one-star review means checking every day.

This post pulls that data into Python, then turns it into a morning feed of new apps and new reviews.

**Disclosure:** I'm Aurelix, and I built the [Shopify App Store Scraper](https://apify.com/aurelix/shopify-app-store-scraper). It's a paid tool (prices below).

One row per app (`record_type: "app"`):

- `name`, `tagline`, `description`, `highlights`, `icon_url`, `built_for_shopify`.
- `rating`, `review_count` and `rating_distribution` (reviews per star level).
- `pricing_plans`: every plan shown on the listing with `name`, `price`, `currency`, `billing_period`, `details` and its `features`.
- `developer_name`, `developer_url`, `developer_website`, `developer_address`, `developer_country`, `launched_date`, `languages`, `works_with`, `categories`.
- `category_ranks`: the app's position in each category the run read, in Shopify's order or newest first.

With reviews on, one row per review (`record_type: "review"`): stars, date, text, the merchant's store name and country, how long they had used the app, and the developer's reply.

Start from app handles or links, category names (`"Email marketing"` works, so does a category link), or developer pages.

```
pip install apify-client
```
```
import os
from apify_client import ApifyClient
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("aurelix/shopify-app-store-scraper").call(
    run_input={"categoryUrls": ["Email marketing"], "maxAppsPerCategory": 48}
)
apps = [r for r in client.dataset(run["defaultDatasetId"]).iterate_items() if r["record_type"] == "app"]
def entry_price(app):
    paid = [p["price"] for p in app["pricing_plans"] if p["price"]]
    return min(paid) if paid else None
for app in sorted(apps, key=lambda a: a["category_ranks"][0]["position"]):
    rank = app["category_ranks"][0]["position"]
    free = any(p["price"] == 0 for p in app["pricing_plans"])
    print(f"#{rank:>2} {app['name'][:40]:40} {app['rating'] or '-':>4} ({app['review_count']:>6} reviews) "
          f"free plan: {'yes' if free else 'no ':3} from ${entry_price(app) or '-'} launched {app['launched_date']}")
```
That is a positioning sheet in one run: who ranks above you, who has a free plan, where the lowest paid plan starts and which apps are new. Run it weekly and you also have a rank history.

```
run_input = {
    "categoryUrls": ["Email marketing"],
    "categorySort": "newest",
    "maxAppsPerCategory": 48,
    "appUrls": ["klaviyo-email-marketing", "omnisend"],
    "includeReviews": True,
    "maxReviewsPerApp": 50,
    "onlyNewEntries": True,
    "stateKey": "email-marketing-watch",
    "slackWebhookUrl": "https://hooks.slack.com/services/...",
}
```
With `onlyNewEntries` on, the first run returns the newest apps in the category and the latest reviews of the two competitors. Each later run with the same `stateKey` returns only apps listed since and reviews you have not seen yet; the two listed apps come back every run with their current rating and review count, so you can chart them. A category stops paging at the first page with nothing new, so a quiet day costs little more than the start fee. Save the input as a task in the Apify Console, schedule it daily, and the Slack URL gets a short digest.

- $0.75 per 1,000 apps ($0.50 on paid plans), and reviews at $0.025 per 1,000, cheaper than the leading tools.
- Apps, categories, developers and reviews in one run.
- Category rank on every app.
- Only new apps and new reviews since the last run.
- What it doesn't cover: keyword (search) rankings, because the App Store's robots.txt disallows its search pages.

- Plan prices are in the visitor's currency; runs on Apify's US servers see US dollars, and every plan carries its `currency`.
- Listings show up to about four plans; a "See all pricing options" page is not read.
- The App Store rate-limits app pages, so full details run at about one app a second; a rank list with `appDetails` off reads 24 apps per page in half a second.

The tool reads only what a logged-out visitor sees on apps.shopify.com, follows robots.txt and returns reviews word for word as the page shows them, paragraph breaks kept.

## Top comments (0)

## Summary

**TLDR:** Shopify app competitor data is all public but painful to compare by hand. A paid scraper fixes that, though the real value is the daily alert feed, not the table.

- The Shopify App Store shows competitors' pricing plans, category ranks and merchant reviews publicly, but doesn't offer them as a comparable table.
- The author's paid Apify actor returns structured data: pricing plans, rating distributions, developer details and category ranks.
- Review rows include stars, the merchant's country, how long they used the app and the developer's reply.
- The workflow pulls the data into Python with apify-client and builds a morning feed of new apps and new reviews.
- The post is written by the tool's own developer, so read it as a product tutorial rather than a neutral comparison.

## 摘要

**重點摘要：** Shopify 應用程式的競品資料全都公開，只是手動比較很痛苦。付費爬蟲解決了這件事，但真正的價值在每日警示，而不是那張表。

- Shopify App Store 公開了競品的定價方案、分類排名與商家評論，卻沒有整理成可以比較的表格。
- 作者開發的付費 Apify 工具會輸出結構化資料，包括定價方案、評分分布、開發商資訊與分類排名。
- 每則評論的資料包含星等、商家所在國家、使用時間長短，以及開發商的回覆。
- 流程是用 apify-client 把資料拉進 Python，再整理成每天早上的新應用程式與新評論快訊。
- 文章由工具開發者本人撰寫，應該當成產品教學來看，而不是中立的評比。