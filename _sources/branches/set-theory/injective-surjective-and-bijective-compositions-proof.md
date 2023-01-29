layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8008
orderid: 50
parentid: bookofproofs$8006
title: 
description:  Proof of INJECTIVE, SURJECTIVE AND BIJECTIVE COMPOSITIONS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$979,bookofproofs$1038
keywords: bijective,compositions,injective,surjective,injective surjective,proof
contributors: bookofproofs

---


---

### Ad (1)

* Let `$x,y\in A$` with `$x\neq y$`.
* By hypothesis, the  [composition][bookofproofs$1314] `$g\circ f$` is [injective][bookofproofs$769].
* Thus, `$g(f(x))\neq g(f(y))$`.
* Since `$g$` is a [function][bookofproofs$592], `$g$` is [right-unique][bookofproofs$1308].
* Therefore, `$f(x)\neq f(y)$`, otherwise we would have `$g(f(x)) = g(f(y))$`, which is not the case.

### Ad (2)

* By hypothesis, the [composition][bookofproofs$1314] `$g\circ f$` is [surjective][bookofproofs$770].
* This means that there is an element `$x\in A$` with `$g(f(x))=z$` for every `$z\in C.$`
* Set `$y:=f(x)$`. Since `$y\in B$`, there is an element `$y\in B$` with `$g(y)=z$` for every `$z\in C.$`
* Therefore, `$g$` is surjective.

### Ad (3)

* By hypothesis, `$f$` is surjective and `$g\circ f$` is injective.
* Let `$x,y\in B$` with `$x\neq y$`.
* Since `$f$` is surjective, there are elements `$u,w\in A$` with `$f(u)=x$` and `$f(w)=y.$`
* Therefore, since `$x\neq y$`, we have `$f(u)\neq f(w).$`
* Since `$g\circ f$` is injective, we have `$g(f(u))\neq g(f(w)).$`
* Altogether, it follows `$g(x)\neq g(y).$`
* Thus, `$g$` is injective.

### Ad (4)

* By hypothesis, `$g\circ f$` is surjective and `$g$` is injective.
* Since `$g\circ f$` is surjective, there is an element `$x\in A$` with `$g(f(x))=y$` for every `$y\in B.$`
* Since `$g$` is injective, we have `$f(x)=y.$`
* In other words, there is an element `$x\in A$` with `$f(x)=y$` for every `$y\in B.$`
* Thus, `$f$` is surjective.
