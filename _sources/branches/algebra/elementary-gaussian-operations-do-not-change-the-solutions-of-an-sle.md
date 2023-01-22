layout: lemma
categories: branches,algebra
nodeid: bookofproofs$7953
orderid: 1
parentid: bookofproofs$7951
title: Elementary Gaussian Operations Do Not Change the Solutions of an SLE
description: ELEMENTARY GAUSSIAN OPERATIONS DO NOT CHANGE THE SOLUTIONS OF AN SLE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$7937
keywords: change,elementary,gaussian,not,operations,sle,solutions
contributors: bookofproofs

---
The following lemma ensures that the elementary Gaussian operations indeed do not change the solutions of an SLE:

---

Let an [SLE][bookofproofs$1044] be given in the form of an [extended coefficient matrix][bookofproofs$7941] `$A|\gamma$` and let `$S$` be the [set][bookofproofs$550] of its solutions. Then `$S$` is an invariant of the [elementary Gaussian operations][bookofproofs$7952]

In other words, if we apply any finite series of these operations `$o_1,o_2,\ldots,o_k$` to `$A|\gamma$`, leading to the new SLEs

* SLE$_1:=A^{(1)}|\gamma^{(1)}:=o_1(A|\gamma)$ after the first opertion `$o_1,$`
* SLE$_2:=A^{(2)}|\gamma^{(2)}:=o_2(A^{(1)}|\gamma^{(1)})$ after the second opertion `$o_2,$`
* SLE$_3:=A^{(3)}|\gamma^{(3)}:=o_3(A^{2)}|\gamma^{(2)})$ after the third opertion `$o_3,$`
* ...
* SLE$_k:=A^{(k)}|\gamma^{(k)}:=o_k(A^{(k-1)}|\gamma^{(k-1)})$ after the `$k$`-th opertion `$o_k,$`

then the solutions `$S$` of SLE$_k$ (if any), will be exactly the same as the solutions as the original SLE.
