layout: proof
categories: branches,set-theory
nodeid: bookofproofs$6865
orderid: 50
parentid: bookofproofs$6864
title: 
description:  Proof of COMPOSITION OF INJECTIVE FUNCTIONS IS INJECTIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: composition,functions,injective,proof
contributors: bookofproofs

---


---

* Assume, for some `$a_1,a_2\in A$`, we have `$(g\circ f)(a_1)=(g\circ f)(a_2)$`.
* By the definition of [composition][bookofproofs$1314], `$g(f(a_1))=g(f(a_2)).$`
* Since `$g:B\to C$` is [injective][bookofproofs$769], it follows `$f(a_1)=f(a_2).$`
* Since `$f:A\to B$` is injective, it follows that `$a_1=a_2$`.
* Altogether, we have concluded from `$(g\circ f)(a_1)=(g\circ f)(a_2)$` in `$C$` that `$a_1=a_2$` for any `$a_1,a_2$` in `$A$`.
* Thus, `$(g\circ f)$` is injective.
