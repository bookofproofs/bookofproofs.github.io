layout: proposition
categories: branches,analysis
nodeid: bookofproofs$6801
orderid: 50
parentid: bookofproofs$1781
title: Riemann Sum Converging To the Riemann Integral
description: RIEMANN SUM CONVERGING TO THE RIEMANN INTEGRAL ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: riemann sum converges to riemann integral
contributors: bookofproofs

---


---

Let `$a < b$`, `$[a,b]$` be a [closed real interval][bookofproofs$1153] and let `$f:[a,b]\to\mathbb R$` be [Riemann-integrable][bookofproofs$1763].
If the [mesh][bookofproofs$1781] `\(\mu\)` of the partition  `\(a=x_0 < x_1 < \ldots < x_{n-1} < x_n=b\)`, with respect to which the [Riemann sum][bookofproofs$1781].
`\[\sum_{k=1}^n f(\xi_k)(x_k-x_{k-1})\]`
is defined, [converges][bookofproofs$141] to `$0$`, then the above Riemann sum of `$f$` converges against the [Riemann-integral][bookofproofs$1763] of `$f$`. 

More strictly, for every `$\epsilon > 0$` there is a `$\delta > 0$` such that for every partition `\(a=x_0 < x_1 < \ldots < x_{n-1} < x_n=b\)` with the mash `$\mu \le \delta$` and every choice of points `$\xi_i\in[x_{k-1},x_k]$` we have 

`$$\left|\int_a^bf(x)dx-\sum_{k=1}^nf(\xi_k)(x_k-x_{k-1})\right|\le \epsilon.$$`
