---
category: developer-tools
faqs:
- answer: DocumentDB 1.0 是一個開源、MIT 授權、建立在 PostgreSQL 上的文件資料庫的首個正式版。它支援 MongoDB 傳輸協定，多數
    MongoDB 驅動程式、工具與查詢不需修改即可使用。
  question: DocumentDB 1.0 是什麼？
- answer: MIT 授權允許商業使用、修改與託管，而且不要求公開專有程式碼。專案方明確拿這點與 MongoDB 的 SSPL 授權對比，因為 SSPL 對把資料庫當成服務提供有所限制。
  question: DocumentDB 採用 MIT 授權為什麼重要？
- answer: 微軟在 2025 年初開源 DocumentDB，專案後來加入 Linux 基金會，獲得 AWS、Cockroach Labs、Google、Snowflake
    與 Yugabyte 支持。
  question: DocumentDB 背後有哪些公司？
featured: false
lang: zh
publishedAt: '2026-11-14T06:37:00+00:00'
relatedSlugs: []
safeForPublic: true
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/mongodb-compatible-documentdb/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
summary: 與其說 DocumentDB 1.0 是新資料庫上市，不如說是一場授權策略布局：這款以 PostgreSQL 為基礎、採 MIT 授權的 MongoDB
  替代方案，背後有 MongoDB 最大的幾家雲端競爭對手撐腰。
tags:
- open-source
- developer-tools
- industry
title: 開源 DocumentDB 1.0 正式釋出
trending: false
type: news
---

與其說 DocumentDB 1.0 是新資料庫上市，不如說是一場授權策略布局：這款以 PostgreSQL 為基礎、採 MIT 授權的 MongoDB 替代方案，背後有 MongoDB 最大的幾家雲端競爭對手撐腰。

## 重點

- DocumentDB 1.0 是這個 MIT 授權、建立在 PostgreSQL 上的文件資料庫首個正式版。它支援 MongoDB 傳輸協定，多數 MongoDB 驅動程式、工具與查詢不必修改就能用。
- 架構由 PostgreSQL 擴充套件加上一個閘道組成，閘道負責把 MongoDB 請求轉成 PostgreSQL 呼叫。透過容器支援 PostgreSQL 15–18，並附 Kubernetes operator。
- 微軟在 2025 年初開源這個專案，後來交給 Linux 基金會，獲得 AWS、Google、Snowflake、Cockroach Labs、Yugabyte 支持。
- 專案公開拿寬鬆的 MIT 授權和 MongoDB 的 SSPL 對比，強調商業託管不必公開自家專有程式碼。
- 它跟 Amazon DocumentDB 撞名，官方還得特地發一篇名稱釐清文章。想成為中立的預設選項，品牌混淆是個麻煩。

## 為什麼值得注意

AWS、Google、微軟罕見地站在同一邊，力挺同一個 MIT 授權、相容 MongoDB 的資料庫。重點不在功能，而是直接回應 SSPL，MongoDB 該緊張了。

## 資料來源

- [InfoQ](https://www.infoq.com/news/2026/11/mongodb-compatible-documentdb/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global)