layout: proof
categories: branches,set-theory
nodeid: bookofproofs$987
orderid: 50
parentid: bookofproofs$986
title: 
description: Proof of SUBSETS OF FINITE SETS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$979
keywords: subsets of finite sets,subset of finite,finite subset,proof
contributors: bookofproofs

---


---

* If `\(S\subseteq X\)` and `\(S=X\)` then `\(S\)` is finite, since `\(X\)` is finite by hypothesis. 
* Let `\(S\subset X\)` and `\(S\neq X\)`. 
* Since `\(X\)` is [finite][bookofproofs$985] by hypothesis, there is an `\(n\in\mathbb N\)` with `\(|X|=|n|\)`. 
* Since `\(S\subset X\)`, `\(|S| < |X|\)`, by [characterization of finite sets][bookofproofs$8053] `$(3)$` and [comparison of cardinal numbers][bookofproofs$984].
* Let `\(K\)` be the set of all [natural numbers][bookofproofs$718], with `\(|S| \le k, k\in K\)`. Since `\(n\in K\)`, the set `\(K\)` is [non-empty][bookofproofs$550].
* Following the [well-ordering principle][bookofproofs$698], `\(K\)` has a minimal element `\(k_0\in K\)`, for which `\(|S| \le k_0\)`.
* Note, that `\(|S| \not < k_0\)`. Otherwise for some `\(j < k_0, j\in K\)` we would have `\(|S| \le j\)`, [contradicting][bookofproofs$744] the minimality of `\(k_0\)`. 
* Therefore `\(|S| = k_0=|k_0|\)`.
* Thus, `\(S\)` is finite.
