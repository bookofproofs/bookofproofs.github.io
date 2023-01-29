layout: proof
categories: branches,analysis
nodeid: bookofproofs$8351
orderid: 50
parentid: bookofproofs$8350
title: 
description: PROOF OF LIMIT COMPARIZON TEST ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$586
keywords: limit comparison test,proof
contributors: bookofproofs

---


---

* By hypothesis, `$\sum_{n=0}^\infty a_n$` and `$\sum_{n=0}^\infty b_n$` are [infinite series][bookofproofs$1109] with [positive][bookofproofs$1107] terms `$a_n > 0$` and `$b_n > 0$` for all `$n\in\mathbb N$`. Moreover the [sequence][bookofproofs$875] of ratios `$\left(\frac{a_n}{b_n}\right)_{n\in\mathbb N}$` [converges][bookofproofs$141] to a _positive_ limit `$\lim_{n\to\infty }\frac{a_n}{b_n}=c > 0.$`
* By the [definition of convergence][bookofproofs$141], there exists an index `$N$` such that for all `$n\ge N$` we have `$$0 < \alpha:=\frac c2 < \left(\frac{a_n}{b_n}\right) < \frac {3c}2=:\beta.$$`
* Thus, for all `$n\ge N$` we have `$0 < \alpha b_n < a_n < \beta b_n.$`
* It follows from the [direct comparison test for absolutely convergent series][bookofproofs$1270] that the sequences `$(a_n)_{n\in\mathbb N}$` and `$(b_n)_{n\in\mathbb N}$` are either both [absolutely convergent][bookofproofs$198] or both or both [divergent][bookofproofs$217].
* If the limit is zero ($c=0$), then there is some index `$N$` such that for all `$n\ge N$` we have `$0 < \left(\frac{a_n}{b_n}\right) \le 1,$` or `$0 < a_n <\le b_n.$` 
* The [direct comparison test for absolutely convergent series][bookofproofs$1270] shows that if `$(a_n)_{n\in\mathbb N}$` is absolutely convergent, if `$(b_n)_{n\in\mathbb N}$` is convergent. 
* If  `$(b_n)_{n\in\mathbb N}$` is divergent, no conclusion whatsoever on the convergence behavior of (a_n)_{n\in\mathbb N}$ can be made.
