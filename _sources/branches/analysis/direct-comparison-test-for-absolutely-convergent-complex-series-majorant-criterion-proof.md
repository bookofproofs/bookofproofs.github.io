layout: proof
categories: branches,analysis
nodeid: bookofproofs$1728
orderid: 50
parentid: bookofproofs$1727
title: 
description: Proof of DIRECT COMPARISON TEST FOR ABSOLUTELY CONVERGENT COMPLEX SERIES MAJORANT CRITERION ★ master maths ✔ visit BookOfProofs!
references: bookofproofs$581
keywords: direct comparison test for absolutely convergent complex series,proof
contributors: bookofproofs

---


---

* By hypothesis, `$\sum_{k=0}^\infty x_k$` is a [complex series][bookofproofs$1724], `$\sum_{k=0}^\infty y_k$` is a [convergent real series][bookofproofs$175], and `$|x_k|\le y_k$` for all `$k\in\mathbb N.$`
* Since *\sum_{k=0}^\infty y_k* is a [convergent real series][bookofproofs$175], thus we can apply [Cauchy's general criterion for the convergence of infinite complex series][bookofproofs$308], and conclude that for every `\(\epsilon  > 0\)` there is an index `\(N(\epsilon)\in\mathbb N\)` such that `$$\left| \sum_{k=m}^n y_k \right| < \epsilon\quad\quad \text{for all}\quad n\ge m\ge N(\epsilon).$$`
* Because by hypothesis `\(|x_k|\le y_k\)` for all `\(k\)`, we get `$$\left|\sum_{k=m}^n |x_k|\right| \le \left|\sum_{k=m}^n y_k\right| < \epsilon\quad\quad \text{for all}\quad n\ge m\ge N(\epsilon).$$`
* Applying [Cauchy's general criterion for the convergence of infinite complex series][bookofproofs$308] once again, we get that the `\(\sum_{k=0}^\infty |x_k|\)` is convergent.
* Therefore `\(\sum_{k=0}^\infty x_k\)` is an [absolutely convergent complex series][bookofproofs$1725].