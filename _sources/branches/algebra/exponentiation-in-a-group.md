layout: definition
categories: branches,algebra
nodeid: bookofproofs$401
orderid: 100
parentid: bookofproofs$838
title: Exponentiation in a Group
description: EXPONENTIATION IN A GROUP &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581,bookofproofs$7896
keywords: exponentiation,group
contributors: bookofproofs

---
The ensured existence of the inverse elements in a group allows us to extend the [exponentiation][bookofproofs$673] we have learned for monoids by explaining what it means to raise an element of a group to a negative power.

---

Let `\((G,\ast)\)` be a [group][bookofproofs$671], `\(x\in G\)`, and `\(n\)` an [integer][bookofproofs$844]. We define the *exponentiation to the `\(n\)`-th power* as the [binary operation][bookofproofs$6188] "`$\ast$`" applied `\(n\)` times to the element `\(x\)`. Like in [exponentiation in a monoid][bookofproofs$673], we set for all `$x\in G$`:

`\[x^n :=
\begin{cases}
e  & \text{ if } n=0 \\
x\ast x^{n-1} & \text{ if } n > 0.
\end{cases}\]`

In addition, we set for [negative][bookofproofs$1075] exponents
`$$x^{-n}:=(x^{-1})^n.$$`

In the above definition, `$e\in G$` denotes the [unique neutral element][bookofproofs$669] of `$G$` and `$x^{-1}$` denotes the [unique inverse element][bookofproofs$359] of `$x\in G.$`
