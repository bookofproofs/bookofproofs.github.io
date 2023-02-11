layout: definition
categories: branches,set-theory
nodeid: bookofproofs$6190
orderid: 200
parentid: bookofproofs$189
title: Comparing the Elements of Posets and Chains
description: COMPARING THE ELEMENTS OF POSETS AND CHAINS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6907
keywords: chains,comparing,elements,incomparable,non-comparable,posets
contributors: @Brenner,bookofproofs

---
Therefore, the only difference between a [chain][bookofproofs$6191] `$(V,\preceq)$` and a [poset][bookofproofs$576] `$(V,\preceq)$` is that in a chain _all_ elements are comparable, while in a poset _some of them_ might be incomparable. This is the reason why the order "`$\preceq$`" is called "partial" in a poset, and "total" in a chain. Moreover, some subsets of a poset might be chains, but not vice versa. This leads us to the distinction between different cases when comparing the elements of a [poset][bookofproofs$576], which we want now to introduce:

---

Let `$(V,\preceq )$` be a [poset][bookofproofs$576] or a [chain][bookofproofs$6191]. The comparison of any two given elements `$a,b\in V$` can result in one of the following possibilities: 

* `$a$` is **equal to** `$b$`: `$b\preceq a$` and `$a\preceq b$` (in this case, we also write `$a=b$`),
* `$a$` is **smaller than or equal to** `$b$`: `$a\preceq b$`,
* `$a$` is **greater than or equal to** `$b$`: `$b\preceq a$` (in this case, we also write `$a\succeq b$`),
* `$a$` is **smaller than** `$b$`:  `$a\preceq b$` and `$a\neq b$` (in this case, we also write `$a\prec b$`),
* `$a$` is **greater than** `$b$`: `$b\succeq a$` and `$a\neq b$` (in this case we also write `$a\succ b$`),
* `$a$` and `$b$` are **incomparable** (*non-comparable*), if none of the above relations hold.
