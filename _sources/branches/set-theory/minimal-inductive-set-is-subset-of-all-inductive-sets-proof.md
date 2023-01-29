layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8040
orderid: 50
parentid: bookofproofs$8039
title: 
description:  Proof of MINIMAL INDUCTIVE SET IS SUBSET OF ALL INDUCTIVE SETS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$983
keywords: all,inductive,minimal,set,sets,subset,proof
contributors: bookofproofs

---


---

By the [axiom of foundation][bookofproofs$717], we have to show that every element of the minimal inductive set `$\omega$` is also an element of any given [inductive set][bookofproofs$8037] `$X$`. From this, it will follow immediately that `$\omega\subseteq X.$` 

* Let `$X$` be an [inductive set][bookofproofs$8037].
* By the [definition of the minimal inductive set][bookofproofs$8038] `$\omega$`, the [empty set][bookofproofs$666] `$\emptyset$` is an element of `$\omega$` and thus, we have `$\emptyset\in \omega\Rightarrow \emptyset\in X.$`
* The same argument holds for all sets `$z\in \omega$`; thus  `$z\in \omega\Rightarrow z\in X.$`
* But if `$z$` is element of `$\omega$`, so is the [singleton][bookofproofs$8034] `$\{z\}$`; thus `$\{z\}\in \omega\Rightarrow \{z\}\in X.$`
* Finally, since `$z\in\omega$` and `$\{z\}\in \omega,$` then `$z\cup \{z\}\in \omega$`, and `$z\cup \{z\}\in X$`, by the same argument.
* Altogether, we have shown `$\omega\subseteq X$` for any given inductive set `$X.$`
