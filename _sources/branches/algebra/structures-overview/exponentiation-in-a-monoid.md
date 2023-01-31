layout: definition
categories: branches,algebra
nodeid: bookofproofs$673
orderid: 400
parentid: bookofproofs$120
title: Exponentiation in a Monoid
description: EXPONENTIATION IN A MONOID &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: exponentiation,monoid
contributors: bookofproofs

---
Because a monoid `$(X,\ast)$` ensures by definition the existence of a neutral element `$e\in X$` and the associativity of its binary operation `$"\ast",$` we can define a new kind of operation in it, called the _exponentiation_ of its elements.

---

Let `\((X,\ast)\)` be a [monoid][bookofproofs$659], `\(x\in X\)`, and `\(n\)` a [natural number][bookofproofs$718]. We define the *exponentiation to the `\(n\)`-th power* as the [binary operation][bookofproofs$6188] "`$\ast$`" applied `\(n\)` times to the element `\(x\)`. For `\(n=0\)`, we set `\(x^0:=e\)`. Formally:

`\[x^n :=
\begin{cases}
e  & \text{ if } n=0 \\
x\ast x^{n-1} & \text{ if } n > 0.
\end{cases}\]`

In the above definition, `$e\in X$` denotes the [unique neutral element][bookofproofs$669] of `$X.$`
