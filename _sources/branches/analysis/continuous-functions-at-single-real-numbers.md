layout: definition
categories: branches,analysis
nodeid: bookofproofs$219
orderid: 50
parentid: bookofproofs$200
title: Continuous Functions at Single Real Numbers
description: CONTINUOUS FUNCTIONS AT SINGLE REAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: continuous,functions,numbers,real,single
contributors: bookofproofs

---


---

Let `\(D\)` be a subset of [real numbers][bookofproofs$1105] `\(\mathbb R\)`, `\(a\in D\)`, and let `\(f:D\to\mathbb R\)` be a [function][bookofproofs$592] `\(f\)` is **continuous** at the real number `\(a\in\mathbb R\)`, if the [limit][bookofproofs$6683] `$\lim_{x\to a} f(x)=f(a)$` exists and is unique. This means that for every [real sequence][bookofproofs$875] `$(\xi_n)_{n\in\mathbb N}$` with `$\xi_n\in D$` for all `$n\in\mathbb N$`, which [convergent][bookofproofs$141] to `$a$` we have that `$\lim_{n\to\infty}f(\xi_n)=a$`. 

### Special Case in Metric Spaces

This definition is a special case of [continuous functions in metric spaces][bookofproofs$1205], because for any two real numbers `$x,y$`, the distance `$|x-y|$` makes [the real numbers a metric space][bookofproofs$618].
### Equivalent Definition

Continuous functions can also be defined using the [`\(\epsilon\)`-`\(\delta\)` definition of continuity][bookofproofs$1254], which is proven to be [equivalent to the definition of continuous functions in metric spaces][bookofproofs$1205]. According to the  `\(\epsilon\)`-`\(\delta\)` definition, `\(f\)` is **continuous** at the point `\(a\)`, if and only if for every `\(\epsilon > 0\)` there is a `\(\delta > 0\)` such that
`\[|f(x)-f(a)| < \epsilon\]`
for all `\(x\in D\)` with 
`\[|x-a| < \delta.\]`

In the above definition, the general distance for metric spaces between the points `$x$` and `$a$` or `$f(x)$` and `$f(a)$` has been replaced by the [absolute value][bookofproofs$583] of the differences `$|x-a|$` and `$|f(x)-f(a)|.$`
