layout: proof
categories: branches,analysis
nodeid: bookofproofs$1265
orderid: 50
parentid: bookofproofs$1264
title: 
description: Proof of CONVERGENCE OF SERIES IMPLIES ZERO SEQUENCE OF TERMS ★ master graduate maths ✔ visit BookOfProofs now!
references: bookofproofs$581
keywords: convergent series implies convergent sequence,proof
contributors: bookofproofs

---


---

* If the [infinite series][bookofproofs$1109] `\(\sum_{k=0}^\infty x_k\)` is [convergent][bookofproofs$175], then by  [Cauchy's criterion][bookofproofs$1148], for a given `\(\epsilon > 0\)`, we can find an index `\(N(\epsilon)\in\mathbb N\)` such that `\[\left|\sum_{k=m}^n x_k\right| < \epsilon\quad\quad \text{for all}\quad n\ge m\ge N(\epsilon).\]`
* In particular, for `\(m=n\)` we have `\[|x_n| < \epsilon\quad\quad \text{for all}\quad n\ge N(\epsilon).\]`
* Thus, it follows `\[\lim_{n\to\infty} x_n=0.\]`
* It remains to be shown that we cannot conclude from `\(\lim_{n\to\infty} x_n=0\)` that `\(\sum_{k=0}^\infty x_k\)` is convergent. It suffices to find at least one counter-example. This counter-example can be the harmonic series `\[\sum_{n=1}^\infty \frac 1n,\]` 
which is [divergent][bookofproofs$1333], but for which `\(\lim_{n\to\infty}\frac 1n=0\)`.
