layout: definition
categories: branches,analysis
nodeid: bookofproofs$8343
orderid: 50
parentid: bookofproofs$476
title: Improper Integral
description: IMPROPER INTEGRAL ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: improper integral,improper integrals,converge,converges,convergent
contributors: bookofproofs

---


---

The **improper integral** is defined as the limit of a [convergent sequence][bookofproofs$141] of [Riemann integrals][bookofproofs$1763] for the following three cases. We also say that the improper integral **converges** (or is **convergent**).

### Case 1: Unbounded Intervals

Let `$f:[a,\infty)$` be a [real-valued][bookofproofs$1105] [function][bookofproofs$592] such that 

* `$f$` is [Riemann-integrable][bookofproofs$1763] for all [closed intervals][bookofproofs$1153] `$[a,b]$` for `$a < b < \infty$` and
* the [limit][bookofproofs$6683]  `$\lim_{b\to\infty}\int_a^bf(x)dx$` exists.

Then we set the improper interval to this limit:

`$$\int_a^\infty f(x)dx:=\lim_{b\to\infty}\int_a^bf(x)dx$$` 

Analogously, if `$f:(\infty,b]$` is a real-valued function such that 

* `$f$` is Riemann-integrable for all closed intervals `$[a,b]$` for `$-\infty < a < b$` and
* the limit `$\lim_{a\to-\infty}\int_a^bf(x)dx$` exists,

then we set 

`$$\int_{-\infty}^b f(x)dx:=\lim_{a\to-\infty}\int_a^bf(x)dx.$$` 

### Case 2: The Riemann integral is undefined on one or even two integration endpoints

If `$f:[a,b)\to\mathbb R$` is a function such that 

* `$f$` is Riemann-integrable for all closed intervals `$[a,b-\epsilon]$` for all `$\epsilon > 0$` and
* the limit `$\lim_{\epsilon\searrow 0}\int_a^{b-\epsilon}f(x)dx$` exists,

then we set 

`$$\int_a^b f(x)dx:=\lim_{\epsilon\searrow 0}\int_a^{b-\epsilon}f(x)dx.$$` 

Analogously, if `$f:(a,b]\to\mathbb R$`

* is Riemann-integrable for all closed intervals `$[a+\epsilon,b]$` for all `$\epsilon > 0$` and
* the limit `$\lim_{\epsilon\searrow 0}\int_{a+\epsilon}^{b}f(x)dx$` exists,

then we set 

`$$\int_a^b f(x)dx:=\lim_{\epsilon\searrow 0}\int_{a+\epsilon}^bf(x)dx.$$` 

### Case 3: Mixed case, both endpoints of the improper integral are critical

Let `$f:(a,b)\to\mathbb R$` for `$a\in\mathbb R\cup \{-\infty\}$` and `$b\in\mathbb R\cup \{+\infty\}$` ($a,b$ being elements of the [extended real numbers][bookofproofs$6668]) is a function and let `$c\in(a,b)$` be given[^1]. If

* `$f$` is Riemann-integrable for all closed intervals `$[\alpha,\beta]\subset (a,b)$` and
* the limits `$\lim_{\alpha\searrow a}\int_\alpha^{c}f(x)dx$` and `$\lim_{\beta\nearrow b}\int_c^{\beta}f(x)dx$` both exist,

then we set 

`$$\int_a^b f(x)dx:=\lim_{\alpha\searrow a}\int_\alpha^{c}f(x)dx+\lim_{\beta\nearrow b}\int_c^{\beta}f(x)dx.$$`



[^1]: Note that this definition is independent of the specific choice of `$c\in(a,b).$` This is because by hypothesis, `$f$` is Riemann-integrable for all closed intervals `$[\alpha,\beta]\subset (a,b)$` and the [integrals can be summed to the same value on any adjacent intervals][bookofproofs$6805].