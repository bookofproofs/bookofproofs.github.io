layout: proof
categories: branches,analysis
nodeid: bookofproofs$8355
orderid: 50
parentid: bookofproofs$8354
title: 
description: PROOF OF RAABE'S TEST ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$586
keywords: raabe's test,raabe test,raabe's test proof,raabe's test for convergence proof,proof
contributors: bookofproofs

---


---

* By hypothesis, `$\sum_{n=0}^\infty a_n$` is an [infinite series][bookofproofs$1109].
* Assume, for a fixed [positive][bookofproofs$1107] number `$\beta > 1$` there exists an index `$N$` such that `$a_n\neq 0$` and `$\left|\frac{a_{n+1}}{a_n}\right|\le 1-\frac{\beta}{n}$` for all `$n\ge N.$`
   * This is equivalent to `$n|a_{n+1}|\le n|a_{n}|-\beta|a_n|$` for all `$n\ge N.$` 
   * Thus, `$n|a_{n+1}|\le n|a_{n}|+|a_{n}|-\beta|a_n|-|a_n|$` and therefore `$(\beta-1)|a_n|\le (n-1)|a_n|-n|a_{n+1}|$` for all `$n\ge N.$` 
   * Since `$\beta > 1$` we get `$|a_n|<(n-1)|a_n|-n|a_{n+1}|$` and by [rules of calculations with inequalities][bookofproofs$594] `$0<|a_n|-|a_{n+1}|$` which is equivalent to `$|a_{n+1}| < |a_n|$`.
   * It follows that the sequence `$(|a_n|)_{n\in\mathbb N}$` is [monotonically decreasing][bookofproofs$1155].
   * On the other hand, the sequence is [bounded][bookofproofs$1136], since `$|a_n| > 0.$` 
   * Because [every bounded monontonic sequence is convergent][bookofproofs$197], `$(|a_n|)_{n\in\mathbb N}$` is a [convergent sequence][bookofproofs$141].
   * Set `$b_n:=(n-1)|a_n|-n|a_{n+1}|$` for all `$n\ge N.$` 
   * Then the [partial sums][bookofproofs$1109] `$\sum_{k=0}^Kb_k$` are, in fact, [telescoping series][bookofproofs$8375] and thus, the infinite series `$\sum_{k=0}^\infty b_k$` is [convergent][bookofproofs$175].
   * Since `$|a_n|\le\frac{b_n}{\beta-1}$`, the infinite series `$\sum_{n=0}^\infty a_n$` is [absolutely convergent][bookofproofs$198] by the [direct comparison test for absolutely convergent series][bookofproofs$1270].
* Now, assume there is an index `$N$` such that `$a_n\neq 0$` and `$\left|\frac{a_{n+1}}{a_n}\right|\ge 1-\frac{1}{n}$` for all `$n\ge N.$`
   * This is equivalent to `$n|a_{n+1}|\ge (n-1)|a_n|$` for all `$n\ge N.$`
   * This means that the sequence `$(n|a_{n+1}|)$` is a positive-valued, [monotonically increasing sequence][bookofproofs$1155], and therefore, its squence members exceed finally a [positive][bookofproofs$1107] bound `$\alpha > 0.$`
   * It follows that `$\frac{|a_{n+1}|}\alpha\ge \frac 1n.$` 
   * Since the [harmonic series][bookofproofs$237] diverges, it follows that the infinite series `$\frac{1}{\alpha}\sum_{n=0}^\infty a_n$` [diverges][bookofproofs$217], again by the [direct comparison test][bookofproofs$1270].
   * Therefore, except of the constant `$\frac{1}{\alpha}$`, the infinite series `$\sum_{n=0}^\infty a_n$` diverges.
