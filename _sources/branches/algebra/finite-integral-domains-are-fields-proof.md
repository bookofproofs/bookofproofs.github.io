layout: proof
categories: branches,algebra
nodeid: bookofproofs$2880
orderid: 50
parentid: bookofproofs$8222
title: 
description: PROOF OF FINITE INTEGRAL DOMAINS ARE FIELDS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$677,bookofproofs$6735
keywords: are,domains,fields,finite,integral,proof
contributors: bookofproofs

---


---

* By hypothesis, `\((R, + ,\cdot)\)` is an [integral domain][bookofproofs$821], which is [finite][bookofproofs$985].
* Let `$R := \{0,a_1:=1,a_2, a_3, \ldots, a_n\}$` be the `$n+1 < \infty$` elements of `$R.$`
* We will show that every nonzero element of `$R$` is a [unit][bookofproofs$821], i.e. has a multiplicative [inverse][bookofproofs$670].
   * Let `$r \in R$` be given with `$r\neq 0.$`
   * We build the set `$R' = \{r \cdot 1, ra_2, ra_3, \ldots, ra_n\}.$`
   * Because `$R$` is closed under multiplication "`$\cdot$`", we have `$R'\subseteq R$`.
   * Since `$R$` is an integral domain, `$R'$` contains no [zero divisors][bookofproofs$821], i.e. for all elements of `$r'\in R'$`  we have `$r'\neq 0.$`
   * Moreover, all elements `$r'\in R'$`  are distinct, because from `$ra_i = ra_j$`  for some `$i \neq j,$`  it follows `$a_i = a_j$` from the cancelation law in integral domains.
   * In particular `$ra_i = 1$` for some `$i \in \{1, \ldots, n\},$` so `$r$` has an inverse.
* Altogether, it follows that every nonzero element `$r\in R$`  is a unit, thus `$R$`  is a [field][bookofproofs$557].