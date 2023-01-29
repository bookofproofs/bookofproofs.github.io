layout: proof
categories: branches,set-theory
nodeid: bookofproofs$7999
orderid: 50
parentid: bookofproofs$7998
title: 
description:  Proof of WELL-ORDERED SETS ARE CHAINS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$979
keywords: are,chains,ordered,sets,well,proof
contributors: bookofproofs

---


---

* Suppose `$(V,\preceq )$` is [well-ordered][bookofproofs$7997].
* We have to prove that "`$\preceq$`" is a [total order][bookofproofs$6191], i.e. [reflexive, transitive][bookofproofs$572], [antisymmetric][bookofproofs$575], and [connex][bookofproofs$1308].
* Since "`$\preceq$`" is a [partial order][bookofproofs$576], and since any partial order is reflexive, transitive and antisymmetric, it only remains to be shown that "`$\preceq$`" is [connex][bookofproofs$1308].
* Since `$V$` is well-ordered, any of its non-empty, [finite][bookofproofs$985] subsets `$S$` has a [minimum][bookofproofs$7995].
* In particular, if `$S=\{x,y\}$` consists of exactly two arbitrary elements of `$V$`, it has a minimum, and therefore we have `$x\preceq y$` or `$y\preceq x$`.
* Since `$x,y$` are arbitrarily chosen from `$V$`, "`$\preceq$`" is connex, as required.
* Altogether, "`$\preceq$`" is a total order and `$V$` a [chain][bookofproofs$6191], by definition.
