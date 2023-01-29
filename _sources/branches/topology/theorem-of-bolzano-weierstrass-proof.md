layout: proof
categories: branches,topology
nodeid: bookofproofs$6609
orderid: 50
parentid: bookofproofs$6608
title: 
description:  Proof of THEOREM OF BOLZANO-WEIERSTRASS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$582
keywords: theorem of bolzano-weierstrass,bolzano-weierstras,proof
contributors: bookofproofs

---


---

* Let `$X$` be a [metric space][bookofproofs$617].
* Let `\(A\subset X\)` be a [compact][bookofproofs$6575] [subset][bookofproofs$552].
* Let `$(x_n)_{n\in\mathbb N}$` be a [sequence][bookofproofs$874] of points `\(x_n\in A\)`. 
* We will [prove by contradiction][bookofproofs$744] that `$(x_n)_{n\in\mathbb N}$` contains a [subsequence][bookofproofs$1151] `$(x_{n_k})_{k\in\mathbb N}$`, which [converges][bookofproofs$148] against some point `\(a\in A\)`.
   * Assume, there is no such subsequence.
   * Then for every `$x\in A$` we can choose arbitrary small `\(\epsilon_x > 0\)` such that the [open ball][bookofproofs$849] `$B(x,\epsilon_x)$` contains only [finitely many][bookofproofs$985] sequence members. (Otherwise we could construct a subsequence convergent against `$x$`, since we can choose `\(\epsilon_x\)` arbitrarily small).
   * Note that `$(B(x,\epsilon_x))_{x\in A}$` is an [open cover][bookofproofs$150] of `$A$`, i.e. `$$ A\subset \bigcup_{x\in A} B(x,\epsilon_x).$$`
   * Since `$A$` is [compact][bookofproofs$6575], there are [finitely many][bookofproofs$985] points `\(x_1,\ldots,x_n\in A\)` forming with their open balls a finite open subcover of `$A$`, formally 
`$$ A\subset \bigcup_{k=1}^n B(x_k,\epsilon_{x_k}).$$`
   * But then, the sequence `$(x_n)_{n\in\mathbb N}$` would contain only finitely many points, which is a contradiction.
   * Therefore, the assumption that there is no [convergent][bookofproofs$148] [subsequence][bookofproofs$1151] `$(x_{n_k})_{k\in\mathbb N}$` of `$(x_n)_{n\in\mathbb N}$` is wrong.
