layout: definition
categories: branches,logic
nodeid: bookofproofs$6226
orderid: 100
parentid: bookofproofs$186
title: Atomic Formulae in Predicate Logic
description: ATOMIC FORMULAE IN PREDICATE LOGIC &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$656
keywords: atomic,atomic formula in predicate logic,formulae,logic,predicate
contributors: 

---


---

Let `\(s_1,s_2,\ldots, s_n\)` be [terms in predicate logic][bookofproofs$6225] and let `\(P\)` be a [predicate with an arity][bookofproofs$6223] `\(n\ge 1\)`. Then `\(P(s_1,s_2,\ldots,s_n)\)` is called an **atomic formula in predicate logic**.

### Example

Take real numbers as the domain of discourse, and consider the [`\(\epsilon-\delta\)` definition of continuous real functions][bookofproofs$219]:

> A real function `\(f:D\to\mathbb R\)` is continuous at the point `\(a\in D\)`, if for every `\(\epsilon &gt; 0\)` there is a `\(\delta &gt; 0\)` such that `\(|f(x)-f(a)| &lt; \epsilon\)` for all `\(x\in D\)` with `\(|x-a| &lt; \delta.\)`

This proposition can be codified using a formula like this:

`\[\forall\epsilon\,(\epsilon &gt; 0)\,\exists\delta\,(\delta &gt; 0)\,\forall x\,(x\in D)\,(|x-a|&lt;\delta\Longrightarrow|f(x)-f(a)|&lt;\epsilon).\]`

In this formula, the strings `\("x\in D"\)`, `\("\epsilon &gt; 0"\)`, `\("\delta &gt; 0"\)` and `\("|x-a|&lt;\delta"\)` and `\("|f(x)-f(a)|&lt;\epsilon"\)` are atomic formulae, because they are unary and binary predicates of the terms `\("x"\)`,  `\("\epsilon"\)`, `\("\delta"\)`, `\("|x-a|"\)`, and `\("|f(x)-f(a)|"\)`.




### Other Examples of Atomic Formulae in Predicate Logic

* `\(P(0)\)`
* `\(P(1)\)`
* `\(P(x)\)`
* `\(P(y)\)`
* `\(P(f(x,x),x)\)`
* `\(P(1,f(0,1))\)`
* `\(P(x,f(x,y))\)`
* `\(P(f(x,x),f(0,1),x,y,0,1)\)`
*  ...
