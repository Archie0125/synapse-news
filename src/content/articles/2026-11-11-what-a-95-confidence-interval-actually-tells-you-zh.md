---
category: ai-ml
faqs:
- answer: 意思是：如果用同一套方法重複研究很多次，而且模型正確，大約 95% 的區間會包含真實參數。95% 描述的是方法，而不是某一個區間。
  question: 95% 信賴區間到底是什麼意思？
- answer: 在頻率學派統計中，參數是固定的，算出的區間不是包含它就是沒包含。95% 指的是蒐集資料前抽樣的隨機性，不是附在已算出區間上的機率。
  question: 為什麼「有 95% 把握真值落在這區間」是錯的？
- answer: Sander Greenland、Stephen Senn、Kenneth Rothman 等人 2016 年在《European Journal
    of Epidemiology》發表的常用指南中，把它列為檢定、P 值、信賴區間與檢定力的常見誤讀之一。
  question: 有誰記錄過這種常見誤讀？
featured: false
lang: zh
publishedAt: '2026-11-11T05:56:20+00:00'
relatedSlugs: []
sources:
- name: Dev.to
  url: https://dev.to/wanqiu_7ad7bc3efc7b7/what-a-95-confidence-interval-actually-tells-you-18ie
summary: 「有 95% 的把握真實值落在這個區間內」大概是統計學裡最常被複述的一句話，但它其實是錯的。這個 95% 描述的是估計方法本身的可靠度，而不是你手上算出來的那個區間。
tags:
- ai-ml
title: 95% 信賴區間到底在說什麼？
trending: false
type: news
---

A scientific paper reports that a mean difference is 1.4, with a 95% confidence interval of 0.6 to 2.2. In the news, and sometimes even in research talks, this is shortened to a more comforting sentence: we can be 95 percent sure the true value lies between 0.6 and 2.2. That sentence is easy to remember. For a frequentist confidence interval, it is also the wrong meaning.

The core idea is this: **a 95% confidence interval describes the long-run behavior of a method, not the probability that this particular interval covers the true value.** The number 95% belongs to the procedure. It does not attach itself, as a posterior probability, to the one interval you have just computed.

Here is what the procedure is supposed to do. You adopt a statistical model, collect a sample, and compute an interval from that sample by a fixed rule. Imagine, as a thought experiment, repeating the whole study many times, each time drawing a new sample from the same process and applying the same rule. If the model is right and the rule is a 95% confidence procedure, then in the long run about 95% of those intervals would contain the unknown parameter. The other 5% would miss it. In any one repetition, the parameter itself is not jumping around. It is treated as fixed but unknown. The interval is what changes. Once you have computed this week's interval, that specific pair of numbers either includes the parameter or it does not. There is no remaining 95% chance attached to the interval, because the randomness that the 95% referred to was in the sampling, not in the already-realized endpoints.

This distinction is one of the most common misreadings of frequentist intervals. In 2016, Sander Greenland, Stephen Senn, Kenneth Rothman and colleagues published a widely used guide to misinterpretations of tests, P values, confidence intervals, and power in the *European Journal of Epidemiology*. Among the points they stress is that a 95% interval should not be read as if it were a 95% probability statement about the parameter, and that values inside the interval are not thereby shown to be equally plausible, or "proven." The interval is a statement of compatibility with a model and a procedure, under assumptions that may themselves be wrong. If the model is badly misspecified, the long-run coverage can fail, and the label "95%" will not rescue it.

A clearly labeled illustration may help. Suppose some physical quantity has a fixed but unknown value. You measure it on a random sample and, by a standard method, obtain the interval 12.1 to 13.4. These numbers are made up for the example; they are not a result from a real study. The frequentist claim is not "there is a 95% probability that the true value sits between 12.1 and 13.4." It is: "This interval was produced by a method that, in repeated samples, covers the true value about 95% of the time." You cannot see, from the interval alone, whether this particular attempt was one of the successful ones.

The interval still tells you something useful, which is why it is worth reporting. It shows the precision of the estimate under the model: a narrow interval means that, if the assumptions hold, the estimate is tightly constrained; a wide interval means the data have not pinned the quantity down. It also shows which parameter values are more compatible with the data, in the limited sense used by the method. If a 95% interval for a difference excludes zero, that is closely related to a two-sided test at the 5% level rejecting "no difference," but the interval still carries extra information: it tells you about direction and about how large or small the compatible values can be. A result can be "statistically significant" and still have an interval wide enough to include effects too small to matter, or too large to be ignored. The label 95% itself is a convention, not a law of nature. A 90% interval is narrower and misses more often; a 99% interval is wider and misses less often, if the procedure is well calibrated.

A confidence interval is also not a range of individual observations, and it is not a prediction interval for the next data point. It is not an automatic judgment of practical importance. Two intervals that overlap can still be consistent with a statistically detectable difference, depending on how they were constructed and what is being compared; overlap is a rough visual check, not a substitute for the actual contrast. And a Bayesian credible interval, which can be given a direct probability reading under a prior, is a different object. It can be a reasonable way to express uncertainty, but it is not what a classical "95% CI" is promising unless the paper has actually taken that route.

A more careful way to read the sentence in the first paragraph is therefore more modest. The authors estimated a difference of 1.4 by a method that, under their model, would capture the true difference in about 95% of repetitions. The interval from 0.6 to 2.2 is the result of that method on this sample. It is a reason to treat values far outside that range as less compatible with the data, given the model. It is not a 95% bet that the truth lives between those two numbers. The work that remains is the usual work of reading a study: whether the model, the sample, and the measurement deserve the confidence the interval claims.

More research explainers: [https://www.crushsci.com](https://www.crushsci.com)

## Top comments (0)

## Summary

**TLDR:** '95% sure the true value is in this range' is the most repeated stats sentence, and it's wrong. The 95% describes the method, not your interval.

- A 95% confidence interval describes how a procedure behaves over many repeated studies, not the probability that one computed interval contains the true value.
- If the model is correct, about 95% of intervals built the same way would cover the fixed, unknown parameter.
- Once an interval is computed, it either contains the parameter or it does not; the randomness was in sampling, not in the final endpoints.
- A widely used 2016 guide by Greenland, Senn, Rothman and colleagues in the European Journal of Epidemiology lists this as a common misreading.
- The guarantee also depends on the statistical model being correct, which reported intervals rarely make clear.

## 摘要

**重點摘要：** 「有 95% 把握真值落在這區間」是最常被引用的統計說法，但它是錯的。95% 描述的是方法，不是你算出的那一個區間。

- 95% 信賴區間描述的是一套方法在大量重複研究下的表現，而不是某一個已算出的區間包含真值的機率。
- 如果模型正確，用同一方法算出的區間，長期約有 95% 會涵蓋那個固定但未知的參數。
- 區間一旦算出，不是有包含參數就是沒有；隨機性來自抽樣，不在已確定的端點上。
- Greenland、Senn、Rothman 等人 2016 年在《European Journal of Epidemiology》發表的常用指南，把這列為常見誤讀之一。
- 這個保證還建立在統計模型正確的前提上，而論文報告的區間很少交代這一點。