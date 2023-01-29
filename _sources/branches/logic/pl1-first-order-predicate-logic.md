layout: part
categories: branches,logic
nodeid: bookofproofs$186
orderid: 400
parentid: bookofproofs$25
title: PL1 - First Order Predicate Logic
description: PL1 - FIRST ORDER PREDICATE LOGIC &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$656
keywords: first,first order,logic,order,pl1,predicate,predicate logic of first order
contributors: bookofproofs

---


---

A **predicate logic of first order** `\(\operatorname{PL1}\)` consists of all formulae, which obey a [syntax][bookofproofs$709] defined recursively by:

* Each [atomic formula][bookofproofs$6226] is a formula of `\(\operatorname{PL1}\)`.
* Let `\(\phi,~\psi\)` be formulae. Then we can combine them using[^1] [Boolean connectors][bookofproofs$1307] to produce more complex formulae:
   * [negation][bookofproofs$714] of `\(\phi\)`: 
`\((\neg \phi)\)` 
   * [conjunction][bookofproofs$712] of `\(\phi\)` and `\(\psi\)`: 
`\((\phi\wedge \psi)\)`,
   * [disjunction][bookofproofs$713] of `\(\phi\)` and `\(\psi\)`): 
`\((\phi\vee \psi)\)`, 
   * [conclusion][bookofproofs$1304] `\(\psi\)` follows from `\(\phi\)`: 
`\((\phi\Rightarrow \psi)\)`, and 
   * [equivalence][bookofproofs$1305] of `\(\phi\)` and `\(\psi\)`): 
`\((\phi\Leftrightarrow \psi)\)`.
* If `\(x\)` is a [variable][bookofproofs$6220] and `\(\phi\)` is a formula using this variable, then, using the [quantifiers][bookofproofs$6221] "`\(\exists\)`" and "`\(\forall\)`", the following expressions are also formulae:
   * `\(\exists x\,(\phi)\)`
   * `\(\forall x\,(\phi)\)`

The notion  **first order**" in the name of `\(\operatorname{PL1}\)` means that quantifiers can be applied to variables only[^2]. 

### Example

Take real numbers as the domain of discourse, and consider the [`\(\epsilon-\delta\)` definition of continuous real functions][bookofproofs$219]:

> A real function `\(f:D\to\mathbb R\)` is continuous at the point `\(a\in D\)`, if for every `\(\epsilon &gt; 0\)` there is a `\(\delta &gt; 0\)` such that `\(|f(x)-f(a)| &lt; \epsilon\)` for all `\(x\in D\)` with `\(|x-a| &lt; \delta.\)`

This proposition can be codified using a formula like this:

`\[\forall\epsilon\,(\epsilon &gt; 0)\,\exists\delta\,(\delta &gt; 0)\,\forall x\,(x\in D)\,(|x-a|&lt;\delta\Longrightarrow|f(x)-f(a)|&lt;\epsilon).\]`

In this formula, e.g. the strings `\("\epsilon &gt; 0"\)`, `\("\epsilon &gt; 0"\)`, or `\("|x-a|&lt;\delta\Longrightarrow|f(x)-f(a)|&lt;\epsilon"\)` are less complex formulae.





[^1]: Just like we can do with [Boolean variables in propositional logic][bookofproofs$1307]. Therefore, the first order predicate logic `\(\operatorname{PL1}\)` is an extension of a propositional logic, because Boolean variables are a simple special case of more complex formulae in `\(\operatorname{PL1}\)`.

[^2]: While `\(\operatorname{PL1}\)` only allows to apply quantifiers to variables, it is possible to apply them also to predicates and formulae in [higher order logics][bookofproofs$207].