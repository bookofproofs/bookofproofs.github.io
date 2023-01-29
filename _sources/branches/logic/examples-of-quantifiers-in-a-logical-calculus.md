layout: example
categories: branches,logic
nodeid: bookofproofs$7890
orderid: 50
parentid: bookofproofs$6221
title: Examples of Quantifiers in a Logical Calculus
description: EXAMPLES OF QUANTIFIERS IN A LOGICAL CALCULUS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: calculus,examples,logical,quantifiers,quantifiers examples
contributors: bookofproofs

---


---

### Example 1

Let `$s_1$` be the [string][bookofproofs$708] [$\forall x:x+2=5$", let `$s_2$` be the string "$\exists x:x+2=5$", let `$U$` be the "domain of discourse][bookofproofs$6219] of [natural numbers][bookofproofs$718] `$0,1,2,\ldots,$` and let `$I(s)$` be the interpretation of `$s$` assigning it a meaning of [adding natural numbers][bookofproofs$842] in `$U$`. Then the strings mean the following:

> `$s_1$`: "For all natural numbers `$x=0,1,2,\ldots$` the equation `$x+2=5$` holds." `$s_2$`: "There exists a natural number `$x$` such that the equation `$x+2=5$` holds."

Clearly, only `$s_2$` is true. Thus the valuation function gives us `$[[s_1]]_I=0$` and `$[[s_2]]_I=1.$`

### Example 2

For the same domain of discourse and the same interpretation as in example 1, let `$s$` be the string [$\exists x: x+2=y$." In this case, `$x$` is a "bound variable][bookofproofs$6221] and `$y$` is a [free variable][bookofproofs$6221]. The string means the following:

> `$s$`: "There exists a natural number `$x$` such that the equation `$x+2=y$` holds."

The [valuation function][bookofproofs$7874] `$[[s]]_I=undefined$`, since the free variable `$y$` prevents us from deciding if `$s$` is true or false. We won't be able to decide, unless we know, which natural number is assigned to the free variable `$y.$`

### Example 3

Take [real numbers][bookofproofs$1105] as the domain of discourse, and consider the [`\(\epsilon-\delta\)` definition of continuous real functions][bookofproofs$219]:

> A real function `\(f:D\to\mathbb R\)` is continuous at the point `\(a\in D\)`, if for every `\(\epsilon > 0\)` there is a `\(\delta > 0\)` such that `\(|f(x)-f(a)| < \epsilon\)` for all `\(x\in D\)` with `\(|x-a| < \delta.\)`

This proposition can be codified using a string like this:

> "$\forall\,(\epsilon > 0)\,\exists\,(\delta > 0)\,\forall\,(x\in D)\,(|x-a| < \delta\Longrightarrow|f(x)-f(a)| < \epsilon).$"

In this string, the substrings `$\epsilon$`, `$\delta$` and `$x$` are bound variables, since they occur together with the quantifiers `$\exists$` and `$\forall$`, whereas `$a$` is a free variable since it never occurs with a quantifier.
