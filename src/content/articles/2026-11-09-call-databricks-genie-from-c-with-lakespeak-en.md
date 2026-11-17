---
category: developer-tools
faqs:
- answer: LakeSpeak.NET is an open-source .NET library that handles the multi-call
    Databricks Genie conversation flow, from starting a conversation to waiting on
    and reading the answer, SQL and result rows. Version 0.4.0 of the LakeSpeak.Genie
    package targets .NET 8.
  question: What does LakeSpeak.NET do?
- answer: Yes. The companion project includes an offline HTTP fixture that returns
    sample conversation and query responses in memory, so the first run only needs
    .NET 8 and NuGet access.
  question: Can developers try it without a Databricks account?
- answer: Many enterprises run their line-of-business apps on .NET, while Databricks
    tooling leans toward Python. A typed C# client lets those teams add natural-language
    data queries to existing apps without changing stacks.
  question: Why does a C# client for Genie matter?
featured: false
lang: en
publishedAt: '2026-11-09T05:52:28+00:00'
relatedSlugs: []
sources:
- name: Dev.to
  url: https://dev.to/ivan_vydrin_cb049e905960f/call-databricks-genie-from-c-with-lakespeak-3ahh
summary: LakeSpeak gives .NET shops a clean path into Databricks Genie, and its offline-fixture-first
  approach is a quiet lesson in how SDK onboarding should work.
tags:
- developer-tools
- open-source
- ai-ml
title: Call Databricks Genie from C# with LakeSpeak
trending: false
type: news
---

A Genie question takes more than one API call. Your app starts a conversation, waits for

Genie to finish, then reads the answer, SQL, or rows it returns.

I maintain LakeSpeak.NET, an independent open-source project. In this walkthrough, a .NET 8

console app uses `LakeSpeak.Genie` 0.4.0. Run it against a local HTTP fixture first, then use

the same client with a Genie Agent you can access.

Install the [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0).

The first run needs NuGet access. It does not need a Databricks account or the LakeSpeak CLI.

Download the [companion project](https://compiletheory.com/library-guides/lakespeak/lakespeak-demo.zip) and extract it. The

[source directory](https://github.com/ivanvyd/LakeSpeak.NET/tree/c275383b058dffde3b925a5cd6a902686d89726f/examples/package-quickstart)

is pinned to the tested revision. Run these commands inside the extracted project:


```
dotnet restore --locked-mode --source https://api.nuget.org/v3/index.json
dotnet build -c Release --no-restore
dotnet run -c Release --no-build --no-restore -- --fixture
```
The output is:


```
OFFLINE HTTP fixture: no workspace, credentials, or Databricks CLI calls.
There were 42 orders yesterday.
SQL: SELECT count(*) AS order_count FROM orders WHERE order_date = current_date() - 1
order_count
42
OFFLINE fixture PASS (published LakeSpeak.Genie 0.4.0).
```
`FixtureHandler` supplies the conversation and query-result responses in memory. The installed

client parses those responses. The companion checks the returned SQL and one complete row

containing `42`.

The SQL shown here is fixture data. This command does not execute it against a warehouse.

The live path uses these registrations:


```
var services = new ServiceCollection();
services.AddDatabricksCliAuthentication(profileName);
services.AddLakeSpeak(options => options.Profile = profileName);
using var provider = services.BuildServiceProvider();
var genie = provider.GetRequiredService<IGenieClient>();
var response = await genie.AskAsync(
    agentId, question, cancellationToken: cancellationToken);
```
The complete project includes the `using` directives and argument handling. In a hosted

application, use your existing dependency-injection container and supply the cancellation

token from the request or background task.

The response can contain answer text, generated SQL and a tabular result. Genie can also ask

for clarification. Check whether a result exists before using its rows. The example prints

an incomplete-result warning and exits with code `1` if the result is truncated.

For a live question, you need:

- The [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/install) available to the process.
- An existing Genie Agent shared with your identity.
- Permission to use the Agent's warehouse and underlying data.

Copy the Agent's ID from Databricks. This console example does not resolve display names.

Replace `YOUR_WORKSPACE_HOST` and `YOUR_AGENT_ID` before running these commands:


```
databricks auth login --host "https://YOUR_WORKSPACE_HOST" --profile my-workspace
dotnet run -c Release --no-build --no-restore -- my-workspace "YOUR_AGENT_ID" "How many orders were placed yesterday?"
```
The selected CLI profile owns login and token refresh. Check `DATABRICKS_HOST` too: an existing

environment value can override the profile's host. The [authentication guide](https://github.com/ivanvyd/LakeSpeak.NET/blob/89fc345147e62d74124f7990824c8bbd45f3e1cb/docs/authentication.md)

documents that precedence and the OAuth M2M path for unattended applications.

A live question creates conversation history and can use warehouse compute. Inspect the

returned SQL and compare the answer with a result you understand before relying on it.

| Symptom | Check | 
|---|---|
| The process cannot find `databricks` | Confirm the CLI is installed and on the PATH inherited by the application. | 
| The request reaches the wrong workspace | Check the selected profile and any `DATABRICKS_HOST` override. | 
| The Agent is not found or access is denied | Check that you passed an ID, then check Agent sharing, warehouse access and data permissions for that identity. | 
| The response has text but no rows | Read the response. It may be a clarification rather than a completed query result. | 
| The .NET SDK cannot be selected | The companion pins a .NET 8 SDK. Use its README's tested .NET 10 adaptation if you are working on .NET 10. | 

The published 0.4.0 client passed this offline fixture on .NET 8 and .NET 10. A separate

installed .NET 8 consumer also completed one live synthetic question in a nonproduction AWS

workspace. Its existing starter Agent generated `SELECT 1 AS probe_value` and returned one

complete row containing `1`.

The [current-source .NET 10 M2M suite](https://github.com/ivanvyd/LakeSpeak.NET/actions/runs/42409476224)

passed all nine live tests on 7 November 2026. That suite covers questions, follow-up,

re-execution, feedback and client cancellation. It is separate from the installed-package

check. Client cancellation does not establish that remote warehouse work stopped.

These checks do not establish business-answer accuracy or GCP compatibility. The [compatibility record](https://github.com/ivanvyd/LakeSpeak.NET/blob/89fc345147e62d74124f7990824c8bbd45f3e1cb/docs/compatibility.md)

keeps the dated checks and their limits.

The [official Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/reference/genie-commands)

already provides Genie terminal commands. Use the .NET client when the conversation belongs

inside your C# application. Databricks also provides [native benchmark evaluations](https://docs.databricks.com/aws/en/genie-agents/monitor).

LakeSpeak's separate Question Pack CLI supports versioned questions and reviewable reports.

In 0.4.0, `behavior.requireQueryResult: true` makes a pack reject missing or truncated results.

A complete zero-row result succeeds. The default is `false`; this setting does not judge

whether an answer is correct.

*AI drafted and edited this tutorial using the project source and verification results.*

## Top comments (0)

## Summary

**TLDR:** LakeSpeak gives .NET shops a clean path into Databricks Genie, and its offline-fixture-first approach is a quiet lesson in how SDK onboarding should work.

- LakeSpeak.NET is an independent open-source library that wraps the multi-step Databricks Genie conversation flow for C# apps.
- Asking Genie one question takes several API calls: start a conversation, poll until it finishes, then read the answer, SQL or rows.
- The demo runs against an in-memory HTTP fixture first, with no Databricks account, credentials or CLI required.
- The live path plugs into .NET dependency injection through Databricks CLI profile authentication.
- This fills a gap for enterprise .NET teams that want natural-language data queries without switching to Python.

## 摘要

**重點摘要：** LakeSpeak 讓 .NET 團隊能順利接上 Databricks Genie，而它「先離線跑通」的設計，正好示範了 SDK 上手體驗該怎麼做。

- LakeSpeak.NET 是一個獨立的開源函式庫，把 Databricks Genie 多步驟的對話流程包成 C# 可以直接呼叫的介面。
- 問 Genie 一個問題需要好幾次 API 呼叫：先開對話、等它處理完，再讀取答案、SQL 或資料列。
- 範例先用記憶體內的 HTTP fixture 執行，不需要 Databricks 帳號、憑證或 CLI。
- 正式環境則透過 Databricks CLI 設定檔驗證，並整合進 .NET 的依賴注入。
- 這補上了企業 .NET 團隊的缺口：想用自然語言查資料，又不必改用 Python。