layout: proof
categories: branches,analysis
nodeid: bookofproofs$8353
orderid: 50
parentid: bookofproofs$8352
title: 
description: PROOF OF ROOT TEST ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$586
keywords: root test,proof
contributors: bookofproofs

---


---

* By hypothesis, `$\sum_{n=0}^\infty a_n$` is an [infinite series][bookofproofs$1109], and for a fixed[^1] [positive][bookofproofs$1107] number `$0 < q < 1$` there is an index `$N$` such that for all `$n\ge N$` the [n-th root][bookofproofs$46] of [absolute values][bookofproofs$583] is smaller than or equal `$q$`, i.e. `$\sqrt[n]{|a_n|}\le q$` for all `$n\ge N.$`
* This is equivalent to `$|a_n|\le q^n$` for all `$n\ge N.$` 
* Since the [geometric series][bookofproofs$1353]  `$\sum_{n=N}^\infty q_n$` is [convergent][bookofproofs$175], it follows from the [direct comparison test for absolutely convergent series][bookofproofs$1270] that `$\sum_{n=0}^\infty a_n$` is [absolutely convergent][bookofproofs$198].
* Now, assume there is an index `$N\in\mathbb N$` such that `$\sqrt[n]{|a_n|}\ge 1$` for all `$n\ge N,$` or at least `$\sqrt[n]{|a_n|}\ge 1$` for infinitely many `$n\in\mathbb N.$`
* This is equivalent to `$|a_n|\ge 1.$`
* Therefore, the sequence `$(a_n)_{n\in\mathbb N}$` cannot [converge][bookofproofs$175] to zero. 
* By [contraposition][bookofproofs$1330] to [convergent series implies convergent sequence][bookofproofs$1264], the series `$\sum_{n=0}^\infty a_n$` is [divergent][bookofproofs$217].
[^1]: Please note that you have to find a fixed number `$q$` that is `$< 1.$` In order to be able to apply the root test, it does not suffice to show that `$\sqrt[n]{|a_n|} < 1$` for all `$n > N,$` the inequality must be `$\sqrt[n]{|a_n|} < q < 1.$`
