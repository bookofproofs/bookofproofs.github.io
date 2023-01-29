layout: proposition
categories: branches,analysis
nodeid: bookofproofs$6805
orderid: 600
parentid: bookofproofs$474
title: Integrals on Adjacent Intervals
description: INTEGRALS ON ADJACENT INTERVALS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: riemann integral on adjacent intervals,adjacent intervals
contributors: bookofproofs

---


---

Let `$a < b < c$`, let `$[a,c]$` be a [closed real interval][bookofproofs$1153]. The [function][bookofproofs$592] `$f:[a,c]\to\mathbb R$` is [Riemann-integrable][bookofproofs$1763], if and only if the [restrictions][bookofproofs$1170] `$f|_{[a,b]}$` and `$f|_{[b,c]}$` are Riemann-integrable. In this case, we have 

`$$\int_a^c f(x)dx=\int_a^b f(x)dx + \int_b^c f(x)dx.$$`

In particular, if we set `$$\int_a^a f(x)dx:=0$$` and `$$\int_a^b f(x)dx:=-\int_b^a f(x)dx,$$`

then the above formula hold for all relative positions of the points `$a,b,c$`, if `$f$` is Riemann-integrable in the interval `$[\min(a,b,c),\max(a,b,c)].$`
