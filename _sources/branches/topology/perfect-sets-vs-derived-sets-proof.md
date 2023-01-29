layout: proof
categories: branches,topology
nodeid: bookofproofs$8576
orderid: 50
parentid: bookofproofs$8575
title: 
description: PROOF OF PERFECT SETS VS. DERIVED SETS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8336
keywords: perfect sets versus derived sets,proof
contributors: bookofproofs

---


---

By hypothesis, `$(X,\mathcal O)$` be a [topological space][bookofproofs$6189]. Let `$U$` be a [subset][bookofproofs$552] `$U\subseteq X.$` 

is   if and only if it equals its [derived set][bookofproofs$8574].
### "`$\Rightarrow$`"

* Assume, `$U$` is [perfect][bookofproofs$8574].
* By definition, `$U$` is [closed][bookofproofs$853] and [dense-in-itself][bookofproofs$8574].
* Since `$U$` is closed, the [complement][bookofproofs$6829] `$U^C$` is [open][bookofproofs$853] and contains no points of `$U$`, especially no limits of `$U$`.
* Therefore, `$U$` contains all of its [limits][bookofproofs$8573].
* By definition, `$U$` equals its [derived set][bookofproofs$8574].
### "`$\Leftarrow$`"

* Assume, `$U$` equals its [derived set][bookofproofs$8574].
* By definition, `$U$` contains all of its limits. 
* The complement `$U^C$` contains a [neighborhood][bookofproofs$8563] of each of its (limit) points. 
* Therefore, `$U^C$` is open.
* Thus, `$U$` is closed.
* Moreover, `$U$` contains no isolated points, because otherwise, they would be in `$U$` since it equals its derived set.
* Therefore, `$U$` is [dense-in-itself][bookofproofs$8574].
* Since `$U$` is closed and dense-in-itself, it is perfect.
