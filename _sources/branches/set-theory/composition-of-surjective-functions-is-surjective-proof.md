layout: proof
categories: branches,set-theory
nodeid: bookofproofs$6863
orderid: 50
parentid: bookofproofs$123
title: 
description:  Proof of COMPOSITION OF SURJECTIVE FUNCTIONS IS SURJECTIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: composition,functions,surjective,proof
contributors: bookofproofs

---


---

* Let `$c\in C$`.
* Since `$g:B\to C$` is [surjective][bookofproofs$770], there is a `$b\in B$` with `$g(b)=c$`.
* Since `$f:A\to B$` is surjective, there is an `$a\in A$` with `$f(a)=b$`.
* Since `$(g\circ f)$` is a [composition][bookofproofs$1314], we have `$(g\circ f)(a)=g(f(a))=g(b)=c$`. 
* Therefore, there is an `$a\in A$` with `$(g\circ f)(a)=c$`.
* Thus, `$(g\circ f)$` is surjective.
