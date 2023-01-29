layout: theorem
categories: branches,analysis
nodeid: bookofproofs$6813
orderid: 700
parentid: bookofproofs$474
title: Integration by Substitution
description: INTEGRATION BY SUBSTITUTION ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: integration by substitution
contributors: bookofproofs

---


---

Let `$I$` be a [real interval][bookofproofs$1153], let `$f:I\to\mathbb R$` be a [continuous function][bookofproofs$1260], and let `$\phi:[a,b]\to\mathbb R$` be a [continouosly differentiable function][bookofproofs$6812] with an [image][bookofproofs$592] contained in `$I$`, formally `$\phi([a,b])\subset I$`. The term **integration by substitution** refers to the [Riemann integral][bookofproofs$1763] of the function `$f(\phi(t))\phi'(t)$` by the following formula:

`$$\int_a^bf(\phi(t))\phi'(t)dt=\int_{\phi(a)}^{\phi(b)}f(x)dx.$$`

### Mnemonic Notation

The above formula can be easily memorized by setting `$d\phi(t):=\phi'(x)dx$` and writing

`$$\int_a^bf(\phi(t))d\phi(t)=\int_{\phi(a)}^{\phi(b)}f(x)dx,$$`

where `$x$` is simply substituted by `$\phi(t).$` If `$t$` runs through the values from `$a$` to `$b$`, then `$x$` runs through the values from `$\phi(a)$` to `$\phi(b)$`.
