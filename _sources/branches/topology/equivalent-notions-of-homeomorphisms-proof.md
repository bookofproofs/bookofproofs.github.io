layout: proof
categories: branches,topology
nodeid: bookofproofs$8590
orderid: 50
parentid: bookofproofs$8589
title: 
description: PROOF OF EQUIVALENT NOTIONS OF HOMEOMORPHISMS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: equivalent notions homeomorphisms,proof
contributors: bookofproofs

---


---

By hypothesis, `$(X,\mathcal O_X)$` and `$(Y,\mathcal O_Y)$` are [topological spaces][bookofproofs$6189] and `$f:X\to Y$` is a [bijective function][bookofproofs$771].
### `$(1)\Rightarrow(2)$`

* Assume, `$f$` is a [homeomorphism][bookofproofs$6197], i.e. `$f$` and its [inverse function][bookofproofs$407] `$f^{-1}$`  are both [continuous][bookofproofs$8583].
* It suffices to show that `$f$` is an [open function][bookofproofs$8586].
* By [bijective open functions][bookofproofs$8587], `$f$` is open since `$f^{-1}$` is continuous. 

### `$(2)\Rightarrow(3)$`

* Assume, `$f$` is both, [continuous][bookofproofs$8583] and an [open function][bookofproofs$8586].
* Let `$A\subseteq X$` be a [subset][bookofproofs$552] of `$X.$`
* Case `$A$` is [closed][bookofproofs$853] in `$X.$`
   * Then `$A=A^-$` (equals its [closure][bookofproofs$1202] in `$X$`).
   * Since `$f$` is an [open function][bookofproofs$8586], the [image][bookofproofs$592] `$f[A^-]$` is closed in `$Y.$` 
   * Thus, `$f[A^-]=f[A^-]^-$` (equals its closure in `$Y$`). 
   * Therefore, `$f[A^-]=f[A]^-.$`
* Case `$A$` is [open][bookofproofs$853] in `$X.$`
   * Since `$f$` is [continuous][bookofproofs$8583], by [equivalent notions of continuous functions][bookofproofs$8584], `$f[A^-]\subseteq f[A]^-.$` 
   * Since `$f$` is an open function, `$f[A^-]$` is [closed][bookofproofs$853] in `$Y.$` 
   * Therefore, there is no `$y\in f[A]^-$` such that `$y\not\in f[A^-].$` 
   * In other words, `$f[A^-]\subseteq f[A]^-$` and `$f[A^-]\not\subset f[A]^-.$`
   * It follows, `$f[A^-]= f[A]^-.$`

### `$(3)\Rightarrow(1)$`

* Assume, for all [subsets][bookofproofs$552] `$A\subseteq X$`, the [image][bookofproofs$592] of the [closure][bookofproofs$1202] equals the closure of the image, formally `$f[A^-]=f[A]^-.$`
* Since `$f[A^-]\subseteq f[A]^-,$` the function `$f$` is [continuous][bookofproofs$8583] by [equivalent notions of continuous functions][bookofproofs$8584].
* On the other hand, since `$(2)$` is sufficient for the assumption `$(3),$` `$f$` must be an [open function][bookofproofs$8586].
* Since `$f$` is an open function and bijective, its [inverse function][bookofproofs$407] `$f^{-1}$` is [continuous][bookofproofs$8583], applying [bijective open functions][bookofproofs$8587].
