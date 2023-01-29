layout: proof
categories: branches,topology
nodeid: bookofproofs$8588
orderid: 50
parentid: bookofproofs$8587
title: 
description: PROOF OF BIJECTIVE  OPEN FUNCTIONS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8336,bookofproofs$8560
keywords: bijective open functions,bijective open function,bijective and open,proof
contributors: bookofproofs

---


---

By hypothesis, `$(X,\mathcal O_X)$` and `$(Y,\mathcal O_Y)$` are [topological spaces][bookofproofs$6189] and `$f:X\to Y$` is a [bijective function][bookofproofs$771].
### "`$\Rightarrow$`"

* Assume, `$f$` is an [open function][bookofproofs$8586].
* Then, the [image][bookofproofs$592] `$f[A]$` of each [open set][bookofproofs$853] `$A\subset X$` is open in `$Y.$`
* Since `$f$` is bijective, the [inverse image][bookofproofs$592] equals `$A$`, formally `$f^{-1}[f[A]]=A.$` 
* It follows that for every open set `$f[A]$` in `$Y$` the [inverse image][bookofproofs$592] `$f^{-1}[f[A]]$` is open `$X,$` since `$A$` is open in `$X.$`
* By definition, the [inverse function][bookofproofs$407] `$f^{-1}$` is [continuous][bookofproofs$8583].
### "`$\Leftarrow$`"

* Assume, the [inverse function][bookofproofs$407] `$f^{-1}$` is [continuous][bookofproofs$8583].
* Then for every open set `$B\in Y$` the inverse image `$f^{-1}[B]$` is open in `$X.$`
* Since `$B$` is bijective, `$A:=f^{-1}[B]$` is the only subset `$A\subseteq X$` for which `$f(A)=B.$`
* Thus, `$A$` is open in `$X.$`
* Therefore, for every open subset `$A\subseteq X$`, the image `$f[A]$` is open in `$Y.$`
* It follows, `$f$` is an [open function][bookofproofs$8586].