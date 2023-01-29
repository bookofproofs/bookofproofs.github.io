layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8011
orderid: 50
parentid: bookofproofs$6325
title: 
description:  Proof of THE INVERSE OF A COMPOSITION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1038
keywords: composition,inverse,proof
contributors: bookofproofs

---


---

* By hypothesis, `$f:A\mapsto B$` and `$g:B\mapsto C$` are [bijective functions][bookofproofs$771].
* It is clear that both functions are [invertible][bookofproofs$407]. Let `$f^{-1}$` and `$g^{-1}$` be their [inverse][bookofproofs$407] functions.
* We want to show that for all `$c\in C$` we have `$(g\circ f)^{-1}(c)=(f^{-1}\circ g^{-1})(c).$`
* If `$c\in C$`, then there is an `$a\in A$` with  `$(g\circ f)(a)=g(f(a))=c,$` since the composition is a function, and in particular it is surjective.
* Since `$g\circ f$` is bijective, it has an inverse `$(g\circ f)^{-1}$` and we have `$(g\circ f)^{-1}(c)=a.$` `$(*)$`
* On the other hand, we have `$(f^{-1}\circ g^{-1})(c)=f^{-1}(g^{-1}(c))$`.
* Since `$c=g(f(a))$` we have further `$(f^{-1}\circ g^{-1})(c)=f^{-1}(g^{-1}(g(f(a)))=f^{-1}(f(a))=a$`. `$(**)$`
* Comparing `$(*)$` with `$(**)$` we get `$(g\circ f)^{-1}(c)=(f^{-1}\circ g^{-1})(c)$` for all `$c\in C.$`
