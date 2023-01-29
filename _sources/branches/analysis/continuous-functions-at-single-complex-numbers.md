layout: definition
categories: branches,analysis
nodeid: bookofproofs$1742
orderid: 400
parentid: bookofproofs$130
title: Continuous Functions at Single Complex Numbers
description: CONTINUOUS FUNCTIONS AT SINGLE COMPLEX NUMBERS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: continuous complex functions,continuous complex function,continuous functions,continuous function,continuous
contributors: bookofproofs

---


---

Let `\(D\)` be a [subset][bookofproofs$552] of [complex numbers][bookofproofs$1105] `\(\mathbb C\)`, `\(a\in D\)`, and let `\(f:D\to\mathbb R\)` be a [function][bookofproofs$592]. As a special case of [continuous functions in metric spaces][bookofproofs$1205] we call `\(f\)` **continuous** at the complex number `\(a\in\mathbb C\)`, if and only if

`\[\lim_{x\to a} f(x)=f(a).\]`

This means that there for every [convergent complex sequence][bookofproofs$1700] `\((\xi_n)_{n\in\mathbb N}\)`, `\(\xi\in D\)` i.e. a sequence with  `\(\lim \xi_n=a\)`, we also have `\(\lim f(\xi_n)=f(a)\)`.

### Equivalent Definition

Continuous functions can also be defined using the [`\(\epsilon\)`-`\(\delta\)` definition of continuity][bookofproofs$1254] `\(f\)` is **continuous** at the point `\(a\)`, if and only if for every `\(\epsilon > 0\)` there is a `\(\delta > 0\)` such that
`\[|f(x)-f(a)| < \epsilon\]`
for all `\(x\in D\)` with 
`\[|x-a| < \delta.\]`

In the above definition, the general distance for metric spaces has been replaced by the [absolute value of complex numbers][bookofproofs$1247].