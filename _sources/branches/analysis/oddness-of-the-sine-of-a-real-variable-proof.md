layout: proof
categories: branches,analysis
nodeid: bookofproofs$1793
orderid: 50
parentid: bookofproofs$1792
title: 
description: Proof of REAL SINE BEING ODD ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: sine is odd,odd function sine,oddness of sine,proof
contributors: bookofproofs

---


---

* By hypothesis, `$x\in\mathbb R$` is a [real number][bookofproofs$1105]. It follows:
* `$\sin(-x)=\frac 1{2i}(\exp(i(-x))-\exp(-i(-x)),$` [representing real sine by the complex exponential function][bookofproofs$1788],
* `$=\frac 1{2i}(\exp((-x)  i)-\exp((-1)(-x)i),$` by [commutativity of multiplying complex numbers][bookofproofs$1671],
* `$=\frac 1{2i}(\exp(-ix)-\exp(ix)),$` by [rules of multiplying positive and negative real numbers][bookofproofs$1598],
* `$=\frac 1{2i}(-\exp(ix)+\exp(-ix)),$` by [commutativity of adding complex numbers][bookofproofs$1660],
* `$=\frac 1{2i}((-1)(\exp(ix)-\exp(-ix))),$` by [distributivity law for complex numbers][bookofproofs$1678], 
* `$=- \frac 1{2i}(\exp(ix)-\exp(-ix))$`
* `$=-\sin(x),$` once again applying representing of real sine by the complex exponential function.
* Thus, the sine of a real variable is an [odd function][bookofproofs$416].