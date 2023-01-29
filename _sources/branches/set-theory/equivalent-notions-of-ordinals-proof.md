layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8090
orderid: 50
parentid: bookofproofs$8089
title: 
description:  Proof of EQUIVALENT NOTIONS OF ORDINALS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$8055
keywords: equivalent,notions,ordinals,proof
contributors: bookofproofs

---


---

For a better readability, we will write in the following `$\in$` instead of `$\in_X$` but mean the [contained relation][bookofproofs$8066] `$\in_X$` defined on `$X.$`

#### `$(1) \Rightarrow (2)$`

* Let `$X$` be an [ordinal][bookofproofs$723].
* By definition, `$(X,\in)$` is [transitive][bookofproofs$720] and [strictly and totally][bookofproofs$7993] and [well-ordered][bookofproofs$7997] by `$\in_X.$`
* Let `$u \in v \in w\in X.$`
* Because `$X$` is transitive, `$u\in v\in X.$`
* Because `$X$` is transitive, `$u\in X.$`
* For the same reason, `$u\in w.$`
* Therefore, every element `$w\in X$` is itself a [transitive set][bookofproofs$720].

#### `$(2) \Rightarrow (1)$`

* Let `$X$` be a transitive set and all of its elements `$w\in X$` be also transitive sets.
* Since `$w$` is transitive, then from `$u \in v$` and `$v\in w$` it follows that `$u\in w.$`
* This means, by definition, that `$(X,\in)$` is a [strict total order][bookofproofs$7993], since `$\in$` is [connex][bookofproofs$1308].
* It remains to be shown that `$\in$` is a [well-order][bookofproofs$7997].
   * The [axiom of foundation][bookofproofs$717] postulates that `$X$` contains an element that is disjoint from `$X.$`
   * This means that there is an element `$z\in X$` and for no other element `$x\in X$` we have `$z\in x.$`
   * This means that the [contained relation][bookofproofs$8066] `$\in$` defined on a set `$X$` is [well-founded][bookofproofs$8058].
   * Therefore, `$X$` contains a [minimal][bookofproofs$7995] element with respect to the [contained relation][bookofproofs$8066] `$\in.$`
* Altogether, we have shown that `$(X,\in)$` is [transitive][bookofproofs$720], [strictly and totally][bookofproofs$7993] and [well-ordered][bookofproofs$7997] by `$\in.$`
* Therefore, `$X$` is an [ordinal number][bookofproofs$723].
#### `$(2) \Rightarrow (3)$`

*$"\Rightarrow"$*:

* Let `$w\in X.$`
* From `$(2)$` it follows that `$w\in X$` is itself a [transitive][bookofproofs$720] set. It remains to be shown that `$w\subset X$` (i.d. that `$w$` is a [proper subset][bookofproofs$552] of `$X.$`)
* If `$v\in W$` then `$v\in X,$` therefore `$w\subseteq X.$` 
* But `$w\neq X$` since otherwise `$X\in X,$` in [contradiction][bookofproofs$744] to the [axiom of foundation][bookofproofs$717].

*$"\Leftarrow"$*:

* Let `$w\subset X$` be itself a [transitive][bookofproofs$720] set.
* Since `$w$` is a [proper subset][bookofproofs$552] of `$X,$` the [set difference][bookofproofs$6830] `$X\setminus w$` is not empty.
* Since `$(2)$` and `$(1)$` are equivalent, `$\in$` is a [strict order][bookofproofs$7993] and a [well-order][bookofproofs$7997].
* Therefore, `$X\setminus w$` contains a [minimal][bookofproofs$7995] element `$z\in X\setminus w.$`
* Thus, `$z\in X$` and `$z\not\in w$` and there is no element `$x\in X\setminus w$` with `$x\in z.$` We will show that `$z=w,$` which means `$w\in X.$`
   * We have `$z\subseteq w.$`
      * If `$y\in z,$` then since `$y\in z\in X$` we have `$y\in X,$` because `$X$` is transitive. 
      * But `$z$` is minimal in `$X\setminus w$`, i.e. there is no other element `$x\in X\setminus w$` with `$x\in z.$`  
      * Since `$y\in z$` and `$y\in X$` and there is no other element `$x\in X\setminus w$` with `$x\in z,$` we have `$y\in w.$`
   * We have `$w\subseteq z.$`
      * Let `$y\in w.$` 
      * We have `$z\not\in y,$` otherwise we would have `$z\in w$` because `$w$` is transitive, in contradiction to the hypothesis `$z\not\in w.$`
      * Therefore, `$y\neq z$` and `$z\not\in y$` which means `$y\in z,$` since `$\in$` is a [strict total order][bookofproofs$7993]. 
* Altogether, we have shown, given the equivalence `$(1)\Leftrightarrow (2),$` that from `$w$` being transitive and `$w\subset X$` it follows that `$w\in X.$`

#### `$(3) \Rightarrow (2)$`

* Let `$w\in X$`  if and only if `$w\subset X$` and `$w$` is transitive for all elements `$w\in X.$`
* Therefore, all elements `$w\in X$` are transitive sets.
