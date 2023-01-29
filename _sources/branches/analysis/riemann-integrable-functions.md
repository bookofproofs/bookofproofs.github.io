layout: definition
categories: branches,analysis
nodeid: bookofproofs$1763
orderid: 100
parentid: bookofproofs$474
title: Riemann-Integrable Functions
description: RIEMANN-INTEGRABLE FUNCTIONS, RIEMANN INTEGRAL ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: integrable,riemann,riemann-integrable,riemann integrable,riemann integral,riemann integrals,riemann integrable functions,riemann integrable function,integrable function,non riemann integrable functions
contributors: bookofproofs

---
The following definition makes use of the fact that for any real functions `$h,f,g$` [bounded][bookofproofs$302] on an [interval][bookofproofs$1153] `$[a,b]$` it follows from `$h(x)\le f(x)\le g(x)$` for all `$x\in[a,b]$` that `$\int_a^b h(x)dx\le \int_a^b f(x)dx\le\int_a^b g(x)dx.$` In particular, if `$h,g$` are [step functions][bookofproofs$1751] then `$$\int_a^{b} h(x)dx\le\underbrace{\int_{a~*}^{b} f(x)dx}_{=:L}\le \int_a^b f(x)dx\le\underbrace{\int_a^{b~*} f(x)dx}_{=:U}\le\int_{a}^{b} g(x)dx.$$` If the two [lower and uppend bounds][bookofproofs$584] `$L$` and `$U$` are equal, then they must be also equal the integral in the middle.

---

Let `\([a,b]\)` be a [closed real interval][bookofproofs$1153]. A [bounded real function][bookofproofs$302] `\(f:[a,b]\mapsto\mathbb R\)` is called *Riemann-integrable*, if its [Riemann upper and Riemann lower integrals][bookofproofs$1761] are equal:

`$$\int_{a}^{b~*}f(x)dx=\int_{a~*}^{b}f(x)dx.$$`

In this case, we set 

`$$\int_{a}^{b}f(x)dx=\int_{a}^{b~*}f(x)dx.$$`

### Notes

* The expression `$\int_{a}^{b}f(x)dx$` is called the **Riemann integral** of the function `$f$` on the interval `$[a,b].$`
* We can use another variable instead of `$x$` without changing the meaning and the value of the Rieman integral, e.g.
`$$\int_{a}^{b}f(x)dx=\int_{a}^{b}f(t)dt=\int_{a}^{b}f(y)dy=\ldots$$`
