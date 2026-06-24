---
title: "LastPass Hit by Supply-Chain Breach: Icarus Hackers Exploit Klue to Steal CRM Data"
summary: "LastPass confirmed on June 23 that hackers accessed customer data from its Salesforce environment after the Icarus threat group stole OAuth tokens from Klue, a third-party market intelligence platform. The breach exposed CRM records for an unknown number of enterprise customers but left password vaults intact."
category: "products"
publishedAt: 2026-06-24
lang: "en"
featured: false
trending: false
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/23/password-manager-maker-lastpass-says-hackers-stole-customer-support-case-data-during-klue-breach/"
  - name: "BleepingComputer"
    url: "https://www.bleepingcomputer.com/news/security/lastpass-confirms-data-breach-in-klue-supply-chain-attack/"
  - name: "Help Net Security"
    url: "https://www.helpnetsecurity.com/2026/06/24/lastpass-klue-data-breach-salesforce-environment/"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/lastpass-klue-supply-chain-breach-customer-data-stolen"
tags:
  - "LastPass"
  - "Klue"
  - "supply chain attack"
  - "Icarus"
  - "data breach"
  - "Salesforce"
  - "cybersecurity"
relatedSlugs:
  - "2026-05-25-github-nx-console-teampcp-supply-chain-attack-en"
  - "2026-04-14-rockstar-shinyhunters-breach-en"
---

LastPass, the password manager that has suffered several high-profile security incidents since its watershed 2022 breach, confirmed on June 23 that attackers accessed customer relationship management data stored in its Salesforce environment — the result of a supply chain compromise at Klue, a third-party market intelligence platform.

The breach, executed by a hacking and extortion group called Icarus, is the latest in a series of incidents in which enterprise software vendors become the vector for attacks on their customers. LastPass insists its core product — the encrypted password vault — was not touched.

## How the Attack Happened

On June 12, LastPass was notified that Klue, which its go-to-market teams use for competitive intelligence and customer research, had been compromised. The Icarus group had obtained access to Klue's infrastructure by exploiting compromised legacy credentials for an integration service account — a dormant technical user that still held live access tokens to customer environments.

From inside Klue's systems, the attackers harvested the OAuth tokens that Klue held on behalf of its customers, including LastPass, to access their Salesforce and Gong integrations. Using automated Python tooling, the attackers enumerated Salesforce objects and executed thousands of API queries, pulling CRM records at scale.

The attack did not require breaking encryption or bypassing multi-factor authentication. OAuth tokens, once stolen, behave as valid credentials until they are explicitly revoked. Klue's integration service account had not rotated credentials in an extended period, leaving the tokens exposed long after the service account was no longer actively managed.

## What Was Exposed

LastPass characterized the exposed data as "standard business contact information and related CRM data," including customer names, phone numbers, email addresses, physical addresses, support case data, and sales-related records. The company said it does not yet know precisely how many customer records were accessed.

Critically, LastPass says the breach did not affect its product infrastructure or the encrypted vaults that hold actual passwords. The Salesforce environment in question is a sales and customer success system, not a component of the password manager architecture. Users' master passwords and stored credentials were not compromised.

Other confirmed victims of the same Klue supply-chain attack include Recorded Future, Tanium, Jamf, Sprout Social, Gong, and Insurity — several of which are themselves security-adjacent companies, adding an ironic dimension to the breach.

## Icarus and the Ransom Threat

The Icarus group, which first appeared in late 2025, operates a leak site on which it publishes stolen data to extort affected companies. On June 22, data allegedly stolen in the Klue attack began appearing on the Icarus leak site, with demands directed at multiple affected companies.

LastPass confirmed it is working with law enforcement and has disabled employee access to Klue, rotated all exposed API and OAuth tokens, and engaged incident response specialists to assess the full scope of the compromise. The company did not confirm whether it had received a specific ransom demand or indicate whether it intends to pay one.

Security researchers who analyzed samples of the leaked data confirmed that the stolen records appear authentic — consistent with the types of enterprise CRM records that would flow through a market intelligence integration.

## The Supply-Chain Blind Spot

The Klue incident is the latest in a pattern that has security teams increasingly concerned: the attack surface for enterprise data no longer ends at the perimeter of the target company. Every third-party integration — every sales tool, HR platform, market intelligence feed, or analytics connector — is a potential entry point.

In LastPass's case, the company holds data that is, by definition, high-value: its customers are enterprises that trust it with credential management. Even CRM metadata about those customers — who they are, what support cases they've had, what their company phone numbers are — is commercially valuable to threat actors who can use it for spear-phishing, impersonation, or further supply chain attacks.

The 2022 LastPass breach, in which attackers eventually accessed encrypted customer vaults by targeting a developer's home computer, established a blueprint for multi-stage, laterally constructed attacks on high-value targets. The Klue incident follows a similar logic: reach LastPass not through its fortified core, but through a less-monitored peripheral integration.

## LastPass's Repeated Breach History

For LastPass, the Klue incident arrives at a particularly difficult moment for its reputation. The 2022 breach remained in headlines for more than a year as post-incident analysis revealed that the attackers had stolen encrypted vault data that remained at risk if customers had weak master passwords. A 2023 credential-stuffing incident followed.

The company was acquired by Francisco Partners in 2021 and has operated as an independent entity, investing heavily in security architecture rebuilds since 2022. This latest breach — while not as severe in terms of the data category exposed — reinforces a perception among security professionals that LastPass remains a disproportionately targeted organization.

"This isn't a failure of their vault architecture," one enterprise security consultant said. "But it's a reminder that the brand's exposure to headline risk from any security incident is higher than almost anyone else in the password manager market. When your core promise is security, the bar is different."

For enterprise IT teams, the immediate action item is straightforward: audit third-party integration platforms that hold OAuth tokens or API credentials connecting to sensitive internal systems, verify that integration service accounts are subject to the same rotation and monitoring policies as human user accounts, and confirm that access scopes granted to market intelligence and analytics tools are restricted to the minimum required.
