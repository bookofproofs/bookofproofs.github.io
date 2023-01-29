layout: example
categories: branches,logic
nodeid: bookofproofs$7891
orderid: 50
parentid: bookofproofs$6222
title: Examples of Functions in a Logical Calculus
description: EXAMPLES OF FUNCTIONS IN A LOGICAL CALCULUS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: calculus,examples,functions,logical
contributors: bookofproofs

---


---

### Example 1

Let `$s$` be the [string][bookofproofs$708] [$\exists x:x+2=5$", let `$U$` be the "domain of discourse][bookofproofs$6219] of [natural numbers][bookofproofs$718] `$0,1,2,\ldots,$` and let `$I(s)$` be the interpretation of `$s$` assigning it a meaning of [adding natural numbers][bookofproofs$842] in `$U$`. Then the string `$s$` means the following:

> `$s$`: "There exists a natural number `$x$` such that the equation `$x+2=5$` holds."

In this string, `$2$` and `$5$` are [constants][bookofproofs$6222] and `$x+2=5$` defines a [binary function][bookofproofs$6222] since it takes two arguments - the  [variable][bookofproofs$6220] `$x$` and the constant `$2$` as input and maps these arguments to the constant `$5$` as output.

### Example 2.

Take [real numbers][bookofproofs$1105] as the [domain of discourse][bookofproofs$6219], and consider the [`\(\epsilon-\delta\)` definition of continuous real functions][bookofproofs$219]:

> A real function `\(f:D\to\mathbb R\)` is continuous at the point `\(a\in D\)`, if for every `\(\epsilon > 0\)` there is a `\(\delta > 0\)` such that `\(|f(x)-f(a)| < \epsilon\)` for all `\(x\in D\)` with `\(|x-a| < \delta.\)`

This proposition can be codified using a string like this:

> "$\forall\epsilon\,(\epsilon > 0)\,\exists\delta\,(\delta > 0)\,\forall x\,(x\in D)\,(|x-a|<\delta\Longrightarrow|f(x)-f(a)|<\epsilon).$"

In this string, the substring `\("0"\)` is a constant. The substrings `\("f"\)` and the absolute value `\("|\cdot|"\)` are unary functions, because they take one argument as input. The strings containing the subtraction sings `\(" x - a"\)` and `$f(x)-f(a)$` are binary functions, because they take two arguments and assign to them impolicitely a real value.
