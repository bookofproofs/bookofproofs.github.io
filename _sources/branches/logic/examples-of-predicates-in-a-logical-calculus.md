layout: example
categories: branches,logic
nodeid: bookofproofs$7892
orderid: 50
parentid: bookofproofs$6223
title: Examples of Predicates in a Logical Calculus
description: EXAMPLES OF PREDICATES IN A LOGICAL CALCULUS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: calculus,examples,logical,predicates
contributors: bookofproofs

---


---

### Example 1

Let `$s$` be the [string][bookofproofs$708] [$x\in\mathbb N: x+2=5$", let `$U$` be the "domain of discourse][bookofproofs$6219] of [natural numbers][bookofproofs$718] `$\mathbb N:=\{0,1,2,\ldots,\}$` and let `$I(s)$` be the interpretation of `$s$` assigning it a meaning in `$U$`. Then the string `$s$` has the meaning:

> `$s$`: "an element `$x$` of the set of natural numbers `$\mathbb N$` such that `$x+2=5$`"

In this string, [$x\in N$" is a "unary predicate][bookofproofs$6223], since it takes only one argument `$x$` as input.

### Example 2

Take [real numbers][bookofproofs$1105] as the [domain of discourse][bookofproofs$6219], and consider the [`\(\epsilon-\delta\)` definition of continuous real functions][bookofproofs$219]:

> A real function `\(f:D\to\mathbb R\)` is continuous at the point `\(a\in D\)`, if for every `\(\epsilon > 0\)` there is a `\(\delta > 0\)` such that `\(|f(x)-f(a)| < \epsilon\)` for all `\(x\in D\)` with `\(|x-a| < \delta.\)`

This proposition can be codified using a string like this:

> "$\forall\epsilon\,(\epsilon > 0)\,\exists\delta\,(\delta > 0)\,\forall x\,(x\in D)\,(|x-a|<\delta\Longrightarrow|f(x)-f(a)|<\epsilon).$"

In this string, `\("x \in D"\)` is a unary predicate, because it takes one argument `\(x\)` to indicate that is contained in `\(D\)`. The comparison relation `\( " < " \)` is a binary predicate because it compares two arguments.
