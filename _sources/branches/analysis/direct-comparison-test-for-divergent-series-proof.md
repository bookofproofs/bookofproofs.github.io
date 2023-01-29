layout: proof
categories: branches,analysis
nodeid: bookofproofs$1336
orderid: 50
parentid: bookofproofs$1335
title: 
description: Proof of DIRECT COMPARISON TEST FOR DIVERGENT SERIES ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: direct comparison test for divergent series,proof
contributors: bookofproofs

---


---

* By hypothesis `$\sum_{k=0}^\infty x_k$`  and `$\sum_{k=0}^\infty y_k$`  are [real infinite series][bookofproofs$1109] with `$x_k\ge y_k\ge 0$` for all `$k\in\mathbb N$` and with `$\sum_{k=0}^\infty y_k$` being [divergent][bookofproofs$217].
* Assume, `$\sum_{k=0}^\infty x_k$` is [convergent][bookofproofs$175].
   * Then, by the [direct comparison test for absolutely convergent series][bookofproofs$1270] it would follow that `$\sum_{k=0}^\infty y_k$` is [absolutely convergent][bookofproofs$198].
   * Then, because [absolute convergence implies convergence][bookofproofs$1268], `$\sum_{k=0}^\infty y_k$` would by convergent.
   * This is a [contradiction][bookofproofs$744] to hypothesis.
* It follows that the assumption is false. 
* Therefore, `$\sum_{k=0}^\infty x_k$` is not convergent, thus it is divergent.
