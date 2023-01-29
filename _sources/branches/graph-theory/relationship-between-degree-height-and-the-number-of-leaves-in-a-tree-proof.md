layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$8483
orderid: 50
parentid: bookofproofs$8481
title: By Induction
description: PROOF OF RELATIONSHIP BETWEEN TREE DEGREE, TREE HEIGHT AND THE NUMBER OF LEAVES IN A TREE ★ master graduate maths ✔ visit BookOfProofs now!
references: bookofproofs$1086
keywords: tree degree and the number of leaves,tree height and the number of leaves,degree height and leaves,proof
contributors: bookofproofs

---


---

* By hypothesis, `$T(V,E)$` is a [tree][bookofproofs$96] with `$|V|$` [vertices][bookofproofs$523] and a given [root][bookofproofs$8482] `$r$`.
* Let `$h$` be the [height][bookofproofs$8482] of `$T$` with respect to `$r$`, let `$d$` be the [degree][bookofproofs$8482] of `$T$` with respect to `$r$`, and let `$l$` denote the number of [leaves][bookofproofs$6366] in `$T$`.
* We prove the inequalities [by induction][bookofproofs$657] on the height `$h.$`
* Base case `$h=0$`:
   * If the height of the tree is `$0$` then `$|V|=1=l\le d^0\le 2\cdot d^0.$`
   * Moreover, `$0\le \log_d(l)$` ([logarithm to the base of the tree degree `$d$`][bookofproofs$6721]).
* Induction step `$h\to h+1$`
   * Assume, for all trees `$T^\prime$` with heights `$h^\prime\le h$` we have the inequalities
      * `$l^\prime\le d^{h^\prime}$`
      * `$|V|\le 2\cdot d^{h^\prime}$`
      * `$h^\prime\ge\log_d({l^\prime}).$`
   * Let `$T(V,E)$` be a tree of height `$h+1$`.
   * We prove `$l+1\le d^{h+1}$`:
      * Note that the [leaves][bookofproofs$6366] at the altitude `$h+1$` of a tree `$T$` have leaves of `$T^\prime$` as their predecessors.
      * Since `$T$` is of degree `$d,$` each leaf of `$T^\prime$` can have at most `$d$` new successors (leaves) in `$T.$`
      * It follows `$l+1\le d\cdot d^{h}=d^{h+1}.$`
   * We prove `$|V|\le 2\cdot d^{h+1}$`
      * We have just shown that at most `$d^{h+1}$` new vertices in `$T$` can be added at the altitude `$h+1$`.
      * The overall number of [vertices][bookofproofs$523] in `$T$` can be, therefore, estimated as `$|V|\le 2d^h+d^{h+1}\le d^{h+1}+d^{h+1}=2d^{h+1}.$`
   * We prove `$h+1\ge\log_d({l+1})$`:
      * Since `$l+1\le d^{h+1}$`, it follows `$\log_d(l+1)\le h+1$`
