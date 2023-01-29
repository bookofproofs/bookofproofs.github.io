layout: lemma
categories: branches,set-theory
nodeid: bookofproofs$1314
orderid: 600
parentid: bookofproofs$64
title: Composition of Functions
description: COMPOSITION OF FUNCTIONS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$979
keywords: composition,composition of functions,functions
contributors: bookofproofs

---
Let `\(A,B,C\)` be [sets][bookofproofs$550]. The following lemma shows that the [composition of relations][bookofproofs$1309] preserves the properties of a [function][bookofproofs$592].
---

Let `\(f:A\mapsto B\)` and `\(g:B\mapsto C\)` be [functions][bookofproofs$592]. The [composition][bookofproofs$1309] `$g\circ f\subseteq A\times C$` of the corresponding [relations][bookofproofs$571] `$f\subseteq A\times B$` and `$g\subseteq B\times C$` is also a [function][bookofproofs$592] defined by

`$$(g\circ f):A\to C,\;(g\circ f)(a):=g(f(a))$$`

and called the **composition of functions**.

### Examples


![composition](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/composition.png?raw=true)


If, for instance, `$A=\mathbb R\to \mathbb R, f(x)=x^2$` and `$g:\mathbb R\to \mathbb R, g(x)=x+2$`, then `$$(g\circ f)(x)=g(f(x))=g(x^2)=x^2+2,$$`
and 
`$$(f\circ g)(x)=f(g(x))=f(x+2)=x^2+2{x}+4.$$`
