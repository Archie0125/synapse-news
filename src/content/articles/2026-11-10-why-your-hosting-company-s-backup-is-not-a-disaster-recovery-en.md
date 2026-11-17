---
category: developer-tools
faqs:
- answer: A backup is a copy of your data. A disaster recovery plan defines who restores
    the site, from which copy, in what order and how long it takes, including when
    the hosting provider itself is unreachable.
  question: What's the difference between a backup and a disaster recovery plan?
- answer: Host backups usually live inside the same provider's infrastructure, so
    an account suspension, server compromise or data centre outage can take away the
    backup along with the site. That makes the host a single point of failure.
  question: Why aren't hosting company backups enough on their own?
- answer: Keep at least one recent, clean backup stored independently of the host,
    and make sure someone on the team has practiced restoring it. Knowing how long
    a restore takes before an emergency is part of the plan.
  question: What should site owners do to actually be recoverable?
featured: false
lang: en
publishedAt: '2026-11-10T05:58:14+00:00'
relatedSlugs: []
sources:
- name: Dev.to
  url: https://dev.to/harshit_verma_a3221b5f423/why-your-hosting-companys-backup-is-not-a-disaster-recovery-plan-5d8f
summary: Your host's backup is an undo button, not a disaster recovery plan, and it
  fails exactly when the host itself is the problem.
tags:
- cybersecurity
- industry
title: Why Your Hosting Company's Backup Is Not a Disaster Recovery Plan
trending: false
type: news
---

Almost every hosting plan advertises backups, and almost every site owner reads that line as "my site is safe." Sometimes that is true. Often it is only half true, and the missing half tends to show up on the worst day of the year.

This article is about the gap between having a backup and being able to recover. It is written for people who run one WordPress site, people who look after a dozen client sites, and anyone who has ever said "the host takes care of that." You will not need a technical background for most of it, though there are a few commands near the end for those who want them.

**A backup and a recovery plan are different things**

A backup is a copy of your data. A recovery plan is the answer to a longer question: if the site is gone at 2 a.m., who does what, with which copy, in what order, and how long does it take?

Host backups are usually built to answer a small, friendly version of that question. You installed a plugin that broke the layout, so you roll back to yesterday. You deleted a page by accident, so you fetch it from last night's snapshot. These are real problems and the built-in tools are often good at them.

Disaster recovery covers the unfriendly version. The server is compromised. The account is suspended over a billing mix-up. The data centre has an outage that lasts a day. A developer ran a destructive command on the wrong machine. In those cases the questions change. Is the backup still reachable? Can you log in to the thing that holds it? Is it recent enough? Is it clean? Does anyone on your team know how to restore it without guessing?

If your only answer to those questions is "I would open the host's control panel," then your recovery plan has a single point of failure, and the point of failure is the same company that is hosting the site.

**What host-provided backups usually are**

Hosting companies differ a lot, so it is unfair to describe them all with one brush. Still, a few traits show up again and again.

**They are snapshots taken by the platform.** The host runs a scheduled job that copies your files and database, usually once a day, and keeps a limited number of copies. You did not configure it, and you often cannot see how it runs.

**They are stored close to the site**. Many hosts keep the copies inside the same infrastructure that serves your site. That is cheap and fast to restore from. It also means a problem big enough to take the account offline can take the copies with it.

**They are tied to your account**. The backups exist because you are a customer. If the account is suspended, closed, or migrated, the backups follow the account's fate. Some hosts publish exactly what happens in that case. Others say little.

They are limited by plan. Retention, frequency, and manual backup slots commonly depend on which tier you bought. Hourly backups or longer history may be a paid extra.

**They are restored through the host's tools**. The restore button lives in a control panel you must be able to reach. Some hosts also offer file-level or database-level restores. Others restore the whole account.

**None of this is a scandal**. It is a sensible product for most customers most of the time. The trouble starts when a site owner treats it as a full safety net.

**Five failures that take the backup down with the site**

It helps to walk through specific situations, because the abstract warning ("don't keep all your eggs in one basket") rarely changes anyone's behaviour. Here are five that happen to real sites, described in general terms.

**The account gets suspended**

Accounts get suspended for several ordinary reasons: a card expires, a payment is disputed, resource usage trips an abuse rule, or a compromised site starts sending spam and the host shuts it down to protect its network. When that happens the site goes offline. The control panel may still let you in, or it may not. Your backups are held under the same account, so you are asking the suspended account to hand you the only copy of your business.

**The server is compromised**

If someone gets into your site, they often get into whatever the account can reach. Depending on the host, that can include the folder where on-account backups are kept. Even when the backups are stored somewhere the attacker cannot touch, you still face a second problem: the infection may have been sitting in the site for days or weeks. Yesterday's backup might contain it too. We will come back to this in the retention section.

**The host has an outage**

Large outages are rare, but they do happen, and a provider's backup system sits inside the provider. If the platform is down, the restore tool is down with it. You can wait, which is fine if you have a brochure site, and painful if you take orders.

**A human makes a mistake**

Developers and site owners delete the wrong folder, run an import against the production database, or overwrite a theme with an older copy. These errors are the most common cause of data loss on small sites, and host snapshots handle them well, as long as the mistake is noticed within the retention window.

**You change hosts, or the host changes you**

Agencies move clients between hosts. Hosts retire old plans, merge into other companies, or migrate customers to new infrastructure. During a move, the history of backups usually stays behind. If something goes wrong a week after the migration, the old host's snapshots may no longer be an option, and the new host has none yet.

**The retention problem nobody notices until it matters**

Retention means how far back your copies go. A host that keeps a month of daily copies sounds generous. For most accidents it is.

The problem is the slow bug. A plugin conflict that corrupts a handful of rows, an injected script that waits two months before doing anything visible, a spam payload hidden in a folder nobody opens, a WooCommerce setting that quietly changed tax rules. You notice weeks after it began. By then the oldest good copy may have rotated out.

There is no perfect retention policy, because storage costs money and nobody wants to keep everything forever. But a sensible approach uses tiers: recent copies every day, a smaller set of weekly copies going back a few months, and maybe one monthly copy that you keep much longer. Most host backup tools do not give you that shape. They keep a flat window of daily copies and drop the oldest.

If you cannot say how far back your oldest usable backup goes, find out today. It takes five minutes and it tells you how much slow-bug risk you are carrying.

**What a host's policy looks like when you read it closely**

Rather than guess, it is worth reading one host's published policy end to end. SiteGround is a good example because its documentation is detailed and recently updated.

At the time of writing, SiteGround's knowledge base page for its Site Tools backup service describes automatic daily copies for every site on its servers. It lists up to 30 daily copies on shared hosting and up to 7 on Cloud hosting. It also says some features, such as manual backups, hourly backups, and downloads, depend on your hosting plan or on a paid Premium Backup service. The page says the same service lets you restore a whole site or only parts of it, such as files, databases, or email.

That is a solid product. It also shows the shape described above: a fixed window of daily copies, features that vary by plan, and a restore path that runs through the host's own control panel. If you are on a shared plan with 30 days of history, the questions to ask are the ones from earlier. What if the account is closed? What if you need a copy from 45 days ago? What if you cannot log in? The article on [SiteGround backups](https://backupyoursite.com/blog/siteground-backup-alternative/) goes through those specific questions against SiteGround's own documentation, and it is a useful read if SiteGround is where your sites live. Check the vendor's current page before you rely on any number, because plans change.

The wider lesson is not about one company. Whatever host you use, open its backup documentation and write down four facts: how many copies, how often, where they are stored, and what happens to them if the account ends. If the documentation does not answer one of those, ask support and keep the reply.

**Shared hosts, managed hosts, and the "which one am I on" trap**

A confusing detail is that one hosting brand can run several different backup systems. A company may sell traditional cPanel hosting, managed WordPress hosting, a website builder, and an add-on backup product, and each can behave differently. The rules for one may not apply to another.

GoDaddy is a common example. It sells several products, and the backup options and retention differ between them, and some involve paid add-ons. GoDaddy's help pages were blocking automated requests when I tried to read them while writing this, so I will not quote specifics. The point is to check which product your site actually runs on and read that product's page, not a general one. Agencies that inherited client accounts often discover they are on a plan nobody remembers buying. If you are weighing a [GoDaddy backup alternative](https://backupyoursite.com/blog/godaddy-backup-alternative/) for client sites, the first step is the same as for any host: confirm the plan, then confirm what the backup on that plan covers.

The same trap applies to any large host. Do not assume that because your friend's site gets 30 days, yours does too.

**Does the backup contain what you need to rebuild?**

Even a perfectly kept host snapshot can be incomplete in ways that matter. Run through this list for your own site.

**The database**. A WordPress site is files plus a MySQL or MariaDB database. Posts, pages, settings, orders, and user accounts live in the database. A backup that only copies files gives you a site with a theme and no content.

**Files outside the web root**. Some setups keep configuration, scheduled scripts, or private uploads outside the public folder. A "website backup" may skip them.

**The wp-config.php file**. It holds database credentials and security keys. A restore without it means rebuilding the connection by hand.

**Other databases and apps**. If your account also runs a staging site, a forum, or a small custom tool, find out whether they are in the backup.

**Email**. On many hosts mailboxes live on the same account. Some backup tools include them and some do not.

**DNS and domain settings**. These usually live somewhere else, which is a good thing, but make sure you know where, and that you can log in.

If one of those answers is "I'm not sure," that is the first thing to fix.

**The 3-2-1 idea, without the jargon**

Backup folks often repeat a rule: keep three copies of your data, on two kinds of storage, with one copy somewhere else. It is old, widely used, and it fits website backups well.

In plain terms it says this. Your live site is copy one. The host's snapshot is copy two. A third copy should sit with a different company, under a different login, in a different place. If you have only the first two, you are one account problem away from nothing.

The "different login" part is the one people forget. A copy stored in a second folder on the same hosting account is not independent. If that account is suspended or compromised, both folders go. A copy in a cloud storage bucket that only you control, with credentials that are not stored on the web server, is independent.

**Four ways to build an independent copy**

There is no single right answer. These are the common approaches, with honest trade-offs.

**A backup plugin that writes to remote storage**

WordPress backup plugins can run inside your site and send archives to Dropbox, Google Drive, Amazon S3 and similar places. They are easy to set up, and for many sites they are enough. The trade-offs are that the work happens inside WordPress, so it uses the same PHP and memory your visitors use, and that on large sites the job can time out. If WordPress is broken, the plugin may be broken too, although the archives already sitting in remote storage are still safe.

**A service that pulls the site from outside**

Some services connect to your server from the outside, usually over SSH or SFTP, read the files and dump the database, and store the result on their own storage. Nothing runs inside WordPress, so a broken site does not stop the backup from running. This approach needs SSH or SFTP access to the server, which not every host offers, especially on entry-level plans.

backupyoursite is one example of this model. Its features page describes the main service as agentless: it connects over SSH from the outside and streams the site and database to offsite storage, with a separate free WordPress plugin for hosts that do not allow SSH. Other tools use similar ideas, so compare them on what they store, how long they keep it, and how a restore works.

**A scripted copy you run yourself**

If you are comfortable with the command line, you can pull your own copy. Here is a simple pattern for a server where you have SSH and WP-CLI.

It is cheap and transparent. It is also entirely your responsibility: nobody tells you when it silently stops working, so add a check that emails you if no new file appeared in the last day.

**The host's own backup, kept as the quick-restore layer**

This is not an alternative so much as the layer you keep. For small mistakes, rolling back through the host's tool is still the fastest route. You are not choosing between the two. You are adding a second copy so the first one is no longer your only line.

**The restore is the part that proves everything**

A backup you have never restored is a belief, not a fact. Plenty of people discover during a real emergency that the archive is empty, that the database dump stops halfway, or that the restore needs a version of PHP the new server does not have.

A sensible backup process includes some form of verification. Good tools check that an archive can be read and that a database dump finishes properly. If you script your own, a basic check is to look for the closing line that mysqldump and WP-CLI write at the end of a complete dump, and to confirm that the file size is in the same range as yesterday's.

Beyond that, do a real restore drill at least twice a year, and also after any big change such as a host move. The drill does not need to be dramatic. Here is a version that takes under an hour.

Create a blank hosting space or a local environment, such as a free test subdomain or a local WordPress setup.

Take your independent backup, not the host's, and restore the files and database into it.

Edit the site URL settings so the copy does not redirect back to the live domain.

Log in, open the homepage, a post, a contact form, and the checkout or login page if you have one.

Write down how long it took and what went wrong.

The notes from step five are the real output. They become your runbook.

**Who needs to know where the backup is**

One underrated risk is that only one person knows the answers. If you run client sites, the backup location, the login, and the restore steps should be written somewhere your team can reach without you. Include the date of the last successful restore test.

For agencies there is also a business angle. Clients assume that "hosting" includes "someone is looking after backups." It is worth saying explicitly, in your service agreement or onboarding notes, who owns backups, where the copies are, and for how long they are kept. Surprises in this area become disputes.

**Why "I'll just check the control panel" fails under stress**

On a normal day, finding your backups takes a minute. On the day of an incident you are tired, the site is down, a client is calling, and the one login you need is on a password manager that is tied to an email address hosted on the same account. Plan for that version of yourself. Keep the backup location, the credentials, and the restore steps somewhere that does not depend on the site or the host being up, and make sure a second person can reach them.

**A short checklist you can finish in an afternoon**

Work through these in order for each site you care about.

1. Find the host's backup documentation and write down copies, frequency, storage location, and what happens at account closure.
2. Confirm which hosting product the site is actually on.
3. Check that the backup includes the database, wp-config.php, and any extra folders or databases.
4. Find your oldest usable restore point and decide whether that is far enough back.
5. Set up one copy that lives with a different provider and a different login.
6. Make sure the credentials for that copy are not stored only on the web server.
7. Turn on an alert for failed or missing backups.
8. Run one restore drill and keep notes.
9. Write down who can do all this if you are unavailable.

**The short version**

Host backups are useful, and for everyday mistakes they are often the quickest fix. They are not a disaster recovery plan, because they share a fate with the account and the platform that holds them. A recovery plan needs a copy somewhere else, a retention window that matches how slowly problems appear, and a restore that someone has actually tested. None of that is expensive or complicated. It does take one afternoon of attention before the bad day, which is far cheaper than finding out on the bad day.

## Top comments (0)

## Summary

**TLDR:** Your host's backup is an undo button, not a disaster recovery plan, and it fails exactly when the host itself is the problem.

- A backup is a copy of data. A recovery plan answers who restores what, from which copy, in what order, and how fast.
- Host backups handle friendly problems well, like a broken plugin or a deleted page.
- Real disasters include compromised servers, suspended accounts, multi-day data centre outages and destructive commands run on the wrong machine.
- If your only recovery path is the host's control panel, the company hosting the site is also your single point of failure.
- Fix: keep independent off-host copies, check that they're clean and recent, and make sure someone has actually practiced a restore.

## 摘要

**重點摘要：** 主機商的備份只是「復原鍵」，不是災難復原計畫，而且主機商本身出事的時候，它最派不上用場。

- 備份是資料的副本；復原計畫回答的是：誰、用哪份副本、按什麼順序、花多久把網站救回來。
- 主機商備份很擅長處理小問題，例如外掛搞壞版面、不小心刪了頁面。
- 真正的災難包括伺服器被入侵、帳號因帳務問題被停權、資料中心停擺一整天，或有人在錯的機器上下了毀滅性指令。
- 如果唯一的復原途徑是主機商的控制台，代管網站的公司本身就是你的單點故障。
- 解法：在主機商之外保留獨立副本，確認它乾淨又夠新，而且團隊裡真的有人演練過還原。