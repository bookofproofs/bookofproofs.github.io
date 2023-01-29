layout: proposition
categories: branches,analysis
nodeid: bookofproofs$1264
orderid: 300
parentid: bookofproofs$196
title: Convergence of Series Implies Sequence of Terms Converges to Zero
description: CONVERGENCE OF SERIES IMPLIES ZERO SEQUENCE OF TERMS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: convergent series implies convergent sequence
contributors: bookofproofs

---
The following proposition shows that the convergence of terms in the sequence is a necessary condition for the series itself to converge.

---

A necessary, but not a sufficient[^1] condition for an infinite series `$\sum_{k=0}^\infty x_k$` for being  [convergent][bookofproofs$175] is that the sequence of the summands `\((x_n)_{n\in\mathbb N}\)` converges to zero, formally `$$\sum_{k=0}^\infty x_k\text{ convergent}\Longrightarrow\lim_{n\to\infty} x_n=0,$$`
`$$\lim_{n\to\infty} x_n= 0\not\Longrightarrow\sum_{k=0}^\infty x_k\text{ convergent}$$`

[^1]: Please note that by the rule of [contraposition][bookofproofs$1330], this statement can be used to prove that an infinite series does _not_ converge if the series of its summands does not converge to zero, i.e. 

`$$\lim_{n\to\infty} x_n\neq 0\Longrightarrow\sum_{k=0}^\infty x_k\text{ divergent}$$`
