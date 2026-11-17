---
category: developer-tools
faqs:
- answer: DocumentDB 1.0 is the first generally available release of an open source,
    MIT-licensed document database built on PostgreSQL. It supports the MongoDB wire
    protocol, so most MongoDB drivers, tools and queries work without changes.
  question: What is DocumentDB 1.0?
- answer: The MIT license allows commercial use, modification and hosting without
    requiring disclosure of proprietary code. The project explicitly contrasts this
    with MongoDB's Server Side Public License (SSPL), which places restrictions on
    offering the database as a service.
  question: Why does DocumentDB's MIT license matter?
- answer: Microsoft open-sourced DocumentDB in early 2025, and the project later joined
    the Linux Foundation with support from AWS, Cockroach Labs, Google, Snowflake
    and Yugabyte.
  question: Who is behind DocumentDB?
featured: false
lang: en
publishedAt: '2026-11-14T06:37:00+00:00'
relatedSlugs: []
safeForPublic: true
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/mongodb-compatible-documentdb/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
summary: 'DocumentDB 1.0 is less a database launch than a licensing move: an MIT-licensed,
  Postgres-based MongoDB alternative backed by MongoDB''s biggest cloud competitors.'
tags:
- open-source
- developer-tools
- industry
title: Open Source DocumentDB 1.0 Reaches General Availability
trending: false
type: news
---

DocumentDB 1.0 is less a database launch than a licensing move: an MIT-licensed, Postgres-based MongoDB alternative backed by MongoDB's biggest cloud competitors.

## Key points

- DocumentDB 1.0 is the first generally available release of the MIT-licensed document database built on PostgreSQL. It speaks the MongoDB wire protocol, so most MongoDB drivers, tools and queries work unchanged.
- The architecture is a PostgreSQL extension plus a gateway that translates MongoDB protocol requests into PostgreSQL calls. It supports PostgreSQL 15–18 through containers and includes a Kubernetes operator.
- Microsoft open-sourced it in early 2025, and it later joined the Linux Foundation with support from AWS, Google, Snowflake, Cockroach Labs and Yugabyte.
- The project openly positions its permissive MIT license against MongoDB's SSPL, telling teams they can host it commercially without disclosing proprietary code.
- The name overlaps with Amazon DocumentDB, and the project had to publish a disambiguation page. That is a branding headache for a project that wants to be the neutral default.

## Why it matters

When AWS, Google and Microsoft all back the same MIT-licensed MongoDB-compatible database, it's not about features. It's a direct answer to the SSPL, and MongoDB should be paying close attention.

## Sources

- [InfoQ](https://www.infoq.com/news/2026/11/mongodb-compatible-documentdb/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global)