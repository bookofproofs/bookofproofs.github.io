layout: proof
categories: branches,algebra
nodeid: bookofproofs$2886
orderid: 0
parentid: bookofproofs$8268
title: 
description: Proof of ADDITIVE SUBGROUPS OF INTEGERS ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$677
keywords: additive subgroups,additive subgroup,integers,additive subgroups of integers,additive subgroup of integer,integer additive subgroup,proof
contributors: bookofproofs

---


---

* It has been shown in the [additive structure of integers][bookofproofs$1654] that `$(\mathbb Z,+)$` is a [group][bookofproofs$671]
* By the [criterion for subgroup][bookofproofs$811], if `$a=nk$` and `$b=nl$` then `$a-b=n(k-l)\in S_n,$` therefore, `$S_n$` is a [subgroup][bookofproofs$554] of  `$(\mathbb Z,+)$` for ever [natural number][bookofproofs$718] `$n\in\mathbb N.$` 
* It remains to be shown that _any_ subgroup of `$(\mathbb Z,+)$` has the required form.
   * Let `$S$` be any subgroup of `$(\mathbb Z,+).$`
   * If `$S=\{0\}$`, we have `$S=S_0$` and we are done. Therefore, assume `$S\neq \{0\}.$`
   * We have `$0\in S$` and, since `$(S,+)$` is closed under addition, we have `$-a\in S$` for all `$a\in S.$`
   * Let `$n\in S$` be the smallest[^1] [positive integer][bookofproofs$1075]
   * Since `$n\in S$`, we have `$nk\in S$` for all `$k\in\mathbb Z,$` therefore `$S_n\subset S.$`
   * On the other hand, any `$a\in S$` can be written as `$a=nk+r$` with `$k\in\mathbb Z$` and `$0\le r < k$`, by the [division with quotient and remainder][bookofproofs$818]
   * Since `$a-r=nk,$` and `$nk\in S_n,$` we have `$a-r\in S_n.$` 
   * But `$r=0,$` since `$r > 0$` would contradict the choice of `$n$` as the _smallest_ positive integer of `$S.$`
   * Therefore, `$a\in S_n,$` which shows `$S\subset S_n.$`
   * Altogether, we haver shown `$S=S_n$` by the [equality of sets][bookofproofs$6841]

[^1]: Such an integer exists due to the [well-ordering principle][bookofproofs$698]
