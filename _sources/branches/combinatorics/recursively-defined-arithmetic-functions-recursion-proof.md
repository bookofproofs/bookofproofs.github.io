layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8680
orderid: 50
parentid: bookofproofs$8679
title: 
description: PROOF OF RECURSIVELY DEFINED ARITHMETIC FUNCTIONS, RECURSION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$977
keywords: recursively defined function,recursion,recursively defined,recursively defined functions,recursions,proof
contributors: bookofproofs

---


---

* By hypothesis, `$N\in\mathbb N$` is a given [natural number][bookofproofs$718].
* It is sufficient to show that the [arithmetic function][bookofproofs$8112] `$f:\mathbb N\to\mathbb C$` defined by specifying the value of `$f(m)$` for all `$m\le N$` and for all `$n > N$` with a given recursion formula `$f(n)=\mathcal R(f(m)\mid m < n)$` is well-defined (i.e. unique) for all [natural numbers][bookofproofs$718].
* Assume, `$f$` defined like this is not well-defined for some natural numbers.
   * Because of the [well-ordering principle][bookofproofs$698], there is the smallest natural number `$N_0\in\mathbb N$` for which `$f$` is not well-defined.
   * But then for `$m < N_0$` the values `$f(m)$` are well-defined and `$f(N_0)=\mathcal R(f(m)\mid m < N_0).$`
   * This is a [contradiction][bookofproofs$744].
* Therefore, `$f$` is well-defined for all [natural numbers][bookofproofs$718].