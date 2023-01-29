layout: proof
categories: branches,analysis
nodeid: bookofproofs$1355
orderid: 50
parentid: bookofproofs$1337
title: By Induction
description: Proof of RATIO TEST ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: ratio test,proof
contributors: bookofproofs

---


---

* By hypothesis,  `\(\sum_{n=0}^\infty a_n\)`  is an  [infinite series][bookofproofs$1109], and `\(a_n\neq 0\)` for all `\(n \ge N\)`, where `\(N\in\mathbb N\)` is some index (i.e. all but the first `\(N\)` sequence members `\(a_n\)` must be different from `\(0\)`), and there exists a fixed[^1] [positive][bookofproofs$1107] number `\(q\)` with `\(0 < q < 1\)` such that `\(\left|\frac{a_{n+1}}{a_n}\right|\le q\)` for all `\(n \ge N.\)`
* We observe that changing a [finite number][bookofproofs$985] of the sequence members does not change its convergence behavior. 
* Therefore, by changing the first `\(N\)` sequence members `\(a_n\)`, we can assume that `\(a_n\neq 0\)` for all `\(n \in\mathbb N\)` (i.e. all sequence members `\(a_n\)` are different from `\(0\)`), and there exists a real number `\(q\)` with `\(0 < q < 1\)` such that `\(\left|\frac{a_{n+1}}{a_n}\right|\le q\)` for all `\(n \in \mathbb N.\)`
* It follows from the [proving principle by induction][bookofproofs$657] that 
   * Base case: `$|a_1|\le |a_0| q^0=|a_0|\cdot 1,$` and that 
   * Induction step: given `\(|a_n|\le |a_0|q^{n-1},\)`, we have `$|a_{n+1}|\le |a_n|\cdot q\le  |a_0|q^{n}.$`
* Due to the [convergence of the infinite geometric series][bookofproofs$1353] `$ \sum_{n=0}^\infty |a_0|q^{n}=\frac{|a_0|}{1-q}$` is convergent.
* It follows from the [direct comparison test for absolutely convergent series][bookofproofs$1270]  that  `\(\sum_{n=0}^\infty a_n\)` is [absolutely convergent][bookofproofs$198].
* On the other hand, if `$q\ge 1$` then for some index `$N\in\mathbb N$` we have `$\left|\frac{a_{n+1}}{a_n}\right|\ge 1$` which is equivalent to `$|a_{n+1}|\ge |a_n|$` for all `$n\ge N.$` 
* Therefore, the [sequence][bookofproofs$875] `$(a_n)_{n\in\mathbb N}$` is [monotonically increasing][bookofproofs$1155] and therefore it cannot [converge][bookofproofs$141] to `$0.$`
* By [contraposition][bookofproofs$1330] to [convergent series implies convergent sequence][bookofproofs$1264], the series `$\sum_{n=0}^\infty a_n$` is [divergent][bookofproofs$217].
[^1]: Please note that you have to find a fixed number `$q$` that is `$< 1.$` In order to be able to apply the ratio test, it does not suffice to show that `$\left|\frac{a_{n+1}}{a_n}\right| < 1$` for all `$n > N,$` the inequality must be `$\left|\frac{a_{n+1}}{a_n}\right| < q < 1.$`
