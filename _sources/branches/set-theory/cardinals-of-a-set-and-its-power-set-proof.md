layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8048
orderid: 50
parentid: bookofproofs$8047
title: 
description:  Proof of CARDINALS OF A SET AND ITS POWER SET &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$577,bookofproofs$1038
keywords: no surjective function of a set to its power set,proof
contributors: bookofproofs

---


---

* Let `$S$` be a [set][bookofproofs$550] and `$\mathcal P(S)$` its [power set][bookofproofs$6831].
* If `$S=\emptyset$` is empty then `$\mathcal P(S)=\{\{\emptyset\}\}.$` There is no [function][bookofproofs$592] `$f:S\to\mathcal P(S)$`, especially no [surjective][bookofproofs$770] function.
* Thus, assume `$S$` is not empty. 
* In this case we can define some [function][bookofproofs$592] `$f:S\to\mathcal P(S)$`, i.e. for every `$s\in S$` we have `$f(s)\in\mathcal P(S).$`
* Suppose, `$f$` is [surjective][bookofproofs$770].
* We construct the set `$X=\{s\in S\mid s\not\in f(s)\}$`. 
* Since `$f$` is surjective and `$\mathcal P(S)$` contains the empty set `$\emptyset$` as its element, there is by definition of surjectivity at least one `$s_1\in S$` with `$f(s_1)=\emptyset.$` Since `$s_1\not\in\emptyset$`, we have `$s_1\not\in f(s_1)$` and therefore `$X$` is not empty, because it contains at least `$s_1.$`
* Note that `$X$` is also a [subset][bookofproofs$552] of `$S$`, thus `$X\in\mathcal P(S).$`  Again, since `$f$` is surjective, there is at least one `$s_2\in S$` with `$f(s_2)=X.$`  
* Now, there are two cases:
   * `$s_2\in X$` - this case is not possible, since by definition of `$X$` we have `$s_2\not\in f(s_2)=X.$`
   * Therefore, we must have `$s_2\not\in f(s_2)=X.$` But either in this case it follows from the definition of `$X$` that `$s_2\in X.$`
* The assumption has to be wrong, i.e. `$f$` is not surjective.
