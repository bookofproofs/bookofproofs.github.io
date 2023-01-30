layout: example
categories: branches,logic
nodeid: bookofproofs$7889
orderid: 50
parentid: bookofproofs$6220
title: Examples of Variables in a Logical Calculus
description: EXAMPLES OF VARIABLES IN A LOGICAL CALCULUS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: calculus,examples,logical,variables
contributors: bookofproofs

---


---

### Example 1

Let `$s$` be the [string][bookofproofs$708] "`$x+2=5$`", let `$U$` be the [domain of discourse][bookofproofs$6219] of 
[natural numbers][bookofproofs$718] `$0,1,2,\ldots$` and let `$I(s)$` be the [interpretation][bookofproofs$7874] of `$s$` 
assigning it a meaning of [adding natural numbers][bookofproofs$842] in `$U$`. 
Clearly, "`$x$`" is a substring of `$s$`. Also "`$2$`", "`$5$`" and "`$+$`" are substrings of ``$s$``, but the interpretation `$I$` means that only `$x$` is a 
[variable][bookofproofs$6220], since `$2,5$` are interpreted as constant natural numbers and "$+$" is interpreted as the addition sign. Then the variable `$x$` represents any of the (infinitely) many natural numbers `$0,1,2,\ldots$`. But only for one of these infinitely many possible meanings of `$x$` the string `$s$` will be valued as true: `$[[s]]_I=1$` only for `$x=3$`.

### Example 2

Take [real numbers][bookofproofs$1105] as the domain of discourse, and consider the [`\(\epsilon-\delta\)` definition of continuous real functions][bookofproofs$219]:

> "A real function `\(f:D\to\mathbb R\)` is continuous at the point `\(a\in D\)`, if for every `\(\epsilon > 0\)` there is a `\(\delta > 0\)` such that `\(|f(x)-f(a)| < \epsilon\)` for all `\(x\in D\)` with `\(|x-a| < \delta.\)`"

This proposition can be codified using a string like this:

> "$\forall\epsilon\,(\epsilon > 0)\,\exists\delta\,(\delta > 0)\,\forall x\,(x\in D)\,(|x-a|<\delta\Longrightarrow|f(x)-f(a)|<\epsilon).$"

In this string, the substrings `\("x"\)`, `\("\delta"\)`, `\("\epsilon"\)` and `\("a"\)` are variables, since they represent real numbers.
