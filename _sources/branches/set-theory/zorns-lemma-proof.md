layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8062
orderid: 50
parentid: bookofproofs$8061
title: 
description: Proof of ZORN'S LEMMA ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$979,bookofproofs$1038,bookofproofs$8055
keywords: zorn's lemma,zorn lemma,lemma zorn,proof
contributors: bookofproofs

---


---

* Let `$(V,\preceq )$` be a [poset][bookofproofs$576].
* Assume, the Zorn's lemma is false. 
   * This means that although every [chain][bookofproofs$6191] `$S\subseteq V$`  has an [upper bound][bookofproofs$7995], `$V$` has no [maximal][bookofproofs$7995] element.
   * Take `$S_0:=\{a_0\}$` as an example of a chain in `$V$` with `$a_0\in V.$`
      * By assumption, `$V$` contains at least one upper bound `$u$` of `$S_0$`, i.e. `$u\in V$` and `$a_0\preceq u.$`
      * By assumption, none of the existing upper bounds `$u$` can be maximal, i.e. there is at least one `$x\in V$` with `$x\succ u.$`
      * By the [axiom of choice][bookofproofs$8041], we can choose `$x$` from the set of all existing elements `$x\in V$` with `$x\succ u$` and set `$a_1:=x.$`
      * By construction, `$a_1\succ a_0$` and we can construct a new chain `$S_1:=\{a_0,a_1\}.$`
   * By analogy, we can construct a new chain `$S_3:=\{a_0,a_1,a_2\}$` with `$a_0\prec a_1\prec a_2.$`
   * This process can be repeated "endlessly", and holds even for an infinite chain `$S,$` while the [axiom of choice][bookofproofs$8041] ensures that we can extend `$S$` by those elements of `$X$` which are greater than any upper bound we have found for `$S$` in `$X.$`
   * But this [contradicts][bookofproofs$744] the assumption that _every_ chain `$S$` has an upper bound in `$X$` but still `$X$` has no maximal elements.
* Therefore, the assumption is false and `$X$` has at least one [maximal][bookofproofs$7995] element.
