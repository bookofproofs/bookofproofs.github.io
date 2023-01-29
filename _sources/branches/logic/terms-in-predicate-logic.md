layout: definition
categories: branches,logic
nodeid: bookofproofs$6225
orderid: 50
parentid: bookofproofs$186
title: Terms in Predicate Logic
description: TERMS IN PREDICATE LOGIC &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$656
keywords: logic,predicate,predicate logic terms,terms
contributors: 

---


---

Let `\(\Sigma = (V_\Sigma,F_\Sigma,P_\Sigma)\)` be a [signature of a predicate logic][bookofproofs$6224]. A set of **predicate logic terms** is defined recursively:

* Every [variable][bookofproofs$6220] `\(x\in V_\Sigma\)` is a term.
* Every [constant][bookofproofs$6222] (i.e. a function with arity `\(0\)`) `\(f\in F_\Sigma\)` is a term.
* If `\(s_1,s_2,\ldots, s_n\)` are terms `\(f\in F_\Sigma\)` is a [function with arity][bookofproofs$6222] `\(n\ge 1\)`, then `\(f(s_1,s_2,\ldots,s_n)\)` is a term.


### Example

Take real numbers as the domain of discourse, and consider the [`\(\epsilon-\delta\)` definition of continuous real functions][bookofproofs$219]:

> A real function `\(f:D\to\mathbb R\)` is continuous at the point `\(a\in D\)`, if for every `\(\epsilon &gt; 0\)` there is a `\(\delta &gt; 0\)` such that `\(|f(x)-f(a)| &lt; \epsilon\)` for all `\(x\in D\)` with `\(|x-a| &lt; \delta.\)`

This proposition can be codified using a formula like this:

`\[\forall\epsilon\,(\epsilon &gt; 0)\,\exists\delta\,(\delta &gt; 0)\,\forall x\,(x\in D)\,(|x-a|&lt;\delta\Longrightarrow|f(x)-f(a)|&lt;\epsilon).\]`

In this formula, the strings `\("x"\)`, `\("\delta"\)`, `\("\epsilon"\)` and `\("a"\)` are variables, thus they are terms. Also the constant `\("0"\)` as well as the functions `\("f(x)"\)`, `\("f(a)"\)`, `\("x-a"\)`, `\("f(x)-f(a)"\)` and `\("|x-a|"\)`, and `\("|f(x)-f(a)|"\)` are terms, because they are nullary, unary and binary functions.


are terms. 

### Other Examples of Terms in Predicate Logic

* `\(0\)`
* `\(1\)`
* `\(x\)`
* `\(y\)`
* `\(f(x,x)\)`
* `\(f(0,1)\)`
* `\(f(x,y)\)`
* `\(f(f(x,x),f(0,1))\)`
*  ...
