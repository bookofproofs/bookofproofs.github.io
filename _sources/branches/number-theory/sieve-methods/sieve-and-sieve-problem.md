layout: definition
categories: branches,number-theory,sieve-methods
nodeid: bookofproofs$8528
orderid: 200
parentid: bookofproofs$366
title: Sieve, Sieve Problem
description: SIEVE, SIEVE PROBLEM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8526,bookofproofs$8527
keywords: sieve, sieve problem
contributors: bookofproofs

---


---

A **sieve** is a [tuple][bookofproofs$747] `$(\mathcal A_N,\mathcal P_\rho,\mathcal R)$` consisting of
* `$\mathcal A_N:=\{a_1,\ldots,a_N\}\subset\mathbb N$`, i.e. a [subset][bookofproofs$552] of `$N$` (not necessarily consecutive) [natural numbers][bookofproofs$718],
* `$\mathcal P_\rho:=\{p_1,\ldots,p_\rho\}\subset\mathbb P$`, i.e. a subset of `$\rho$` (not necessarily consecutive) [prime numbers][bookofproofs$473].
* `$\mathcal R$` is a [union][bookofproofs$6827] of [congruence classes][bookofproofs$8154].
`$$\mathcal R:=\bigcup_{r=1}^\rho\bigcup_{j=1}^{k_r}R_{r}^{(j)},$$`
where for `$r=1,\ldots,\rho$`, some `$k_r$` congruence classes `$R_r^{(1)},\ldots,R_r^{(k_r)}$` are given modulo each prime number `$p_r$`.

Given a sieve, a **sieve problem** is the problem of estimating the [cardinality][bookofproofs$980] of all elements of `$\mathcal A$` that are _not_ [congruent][bookofproofs$8153] to any of the residue classes in `$\mathcal R$`, i.e. the number `$$S(N):=|\{n\in\mathbb N\mid a_n\not\in R\}|.$$`
