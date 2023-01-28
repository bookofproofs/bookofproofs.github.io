layout: proof
categories: branches,algebra
nodeid: bookofproofs$2888
orderid: 50
parentid: bookofproofs$8270
title: 
description: PROOF OF FINITE ORDER OF AN ELEMENT EQUALS ORDER OF GENERATED GROUP &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$677
keywords: finite order of an element equals group order,generated group,proof
contributors: bookofproofs

---


---

* By hypothesis, `$(G,\ast)$` is a [group][bookofproofs$671] and `$a\in G$` its element with a [finite][bookofproofs$985] [order][bookofproofs$807] `$\operatorname{ord}(a)=n < \infty.$` 
* By definition of [generating set of a group][bookofproofs$8265], we have  `$\langle a\rangle=\{a^k\mid k\in\mathbb Z\}.$`
* By [division with quotient and remainder][bookofproofs$818], we can write `$k=qn+r$` with `$0\ge r < n.$` 
* Because `$n$` is the order of the element `$a$`, we have `$a^{k}=a^{qn+r}=(a^n)^q\cdot a^r=e^q\cdot a^r=a^r$` with `$e\in G$` being the [neutral element][bookofproofs$661]
* Therefore, `$\langle a\rangle=\{a^0,a^1,a^2,\ldots a^{n-1}\}.$`
* Moreover, all of these elements are distinct.
   * Assume, they were not, e.g. `$a^i=a^j$` but `$0\le i < j\le n-1.$` 
   * Then, we would have `$a^{j-i}=e,$` in [contradiction][bookofproofs$744] to `$0 < j-i < n.$`
   * Therefore, `$n=\operatorname{ord}(a)$` equals the group order `$|\langle a\rangle|.$`
