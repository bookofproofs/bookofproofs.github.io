layout: proof
categories: branches,analysis
nodeid: bookofproofs$1271
orderid: 50
parentid: bookofproofs$1270
title: 
description: Proof of DIRECT COMPARISON TEST FOR ABSOLUTELY CONVERGENT SERIES ★ master graduate maths ✔ visit BookOfProofs now!
references: bookofproofs$581
keywords: direct comparison test for absolutely convergent series,proof
contributors: bookofproofs

---


---

* Let `$\sum_{k=0}^\infty x_k$`  and `$\sum_{k=0}^\infty y_k$`  be [real infinite series][bookofproofs$1109].
* By hypothesis, let `$\sum_{k=0}^\infty y_k$` be [convergent][bookofproofs$175].
* By the [Cauchy criterion][bookofproofs$1148], for every `\(\epsilon  > 0\)` there is an index `\(N(\epsilon)\in\mathbb N\)` such that `\[\left| \sum_{k=m}^n y_k \right| < \epsilon\quad\quad \text{for all}\quad n\ge m\ge N(\epsilon).\]`
* Since, by hypothesis, `$|x_k|\le y_k$` for all `$k\in\mathbb N,$` we have `$$\left|\sum_{k=m}^n |x_k|\right| \le \left|\sum_{k=m}^n y_k\right| < \epsilon\quad\quad \text{for all}\quad n\ge m\ge N(\epsilon).$$`
* Applying the Cauchy criterion once again, we get that the `\(\sum_{k=0}^\infty |x_k|\)` is convergent.
* By definition, `\(\sum_{k=0}^\infty x_k\)` is [absolutely convergent][bookofproofs$198].