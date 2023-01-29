layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$6368
orderid: 50
parentid: bookofproofs$6367
title: 
description:  Proof of LOWER BOUND OF LEAVES IN A TREE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$566
keywords: bound,leaves,lower,tree,proof
contributors: bookofproofs

---


---

* By hypothesis, `\(T(V,E,\gamma)\)` is a [tree][bookofproofs$96] of [order][bookofproofs$6353] `\(|T|\ge 2\)`.
* According to [equivalent definitions of trees][bookofproofs$1242], for every pair of vertices `\(u,v\in V\)` there is exactly one [path][bookofproofs$1164] `\(P^k:=x_0x_1\ldots x_{k-1}x_k\)` in `\(T\)` with `\(x_0=u\)` and `\(x_k=v\)`.
* Choose `\(u,v\)` such that `\(P^k\)` will have a maximal length `\(k\)`.
* Since `\(P^k\)` is maximal, `\(\delta_T(u)\in P^k\)` with `\(\delta_G(u)=\{e\in E: u\in \gamma(e)\}\)`. 
* Therefore, the [degree][bookofproofs$362] `\(d_T(u)=|\delta_T(u)|=1\)`.
* Similarly for `\(v\in V\)`.
* Therefore, `\(T\)` has at least the two [leaves][bookofproofs$6366] `\(u\)` and `\(v\)`.
