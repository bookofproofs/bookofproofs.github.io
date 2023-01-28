layout: definition
categories: branches,algebra
nodeid: bookofproofs$884
orderid: 300
parentid: bookofproofs$192
title: Subring
description: SUBRING ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$696,bookofproofs$6907
keywords: subring,subrings
contributors: bookofproofs

---


---

Let `\((R, + ,\cdot)\)` be a [ring][bookofproofs$683] A [subset][bookofproofs$552]  `\(S\subseteq R\)` is called a **subring**, if `\((S, + ,\cdot)\)` itself is a ring; or, equivalently[^1], if and only if for all `\(a,b\in S\)` the following conditions are fulfilled:

* (S1) `\(a-b\in S\)`.
* (S2) `\(a \cdot b\in S\)`.

equivalenty[^1]

* `\((S, + )\)` is a [subgroup][bookofproofs$554] of `\((R,+)\)` and 
* `\((S,\cdot)\)` is a [submonoid][bookofproofs$6210] of `\((R,\cdot)\)`.

[^1]: Please note that both definitions are indeed equivalent. For if `\((S, + ,\cdot)\)` is a ring, then (S1) and (S2) are trivially fulfilled. On the other side, if (S1) is fulfilled, then following the [subgroup definition][bookofproofs$554] `\((S, +)\)` is a commutative subgroup of the additive commutative group `\((R, + )\)`. Correspondingly, if (S2) is fulfilled, then `\(S\)` is closed under the multiplication, and therefore `\((S,\cdot)\)` is a [monoid][bookofproofs$659], since `\((R,\cdot)\)` is. The distributive law is then inherited by `\(S\)` from `\(R\)`. Since all defining conditions of a ring are fulfilled for `\(S\)`, `\((S, + ,\cdot)\)` is a ring.
