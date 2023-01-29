layout: section
categories: branches,analysis
nodeid: bookofproofs$8381
orderid: 1300
parentid: bookofproofs$200
title: Uniform Convergence of Functions
description: UNIFORM CONVERGENCE OF FUNCTIONS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: uniform convergence,uniform convergent
contributors: bookofproofs

---


---

The concept of [convergence][bookofproofs$141] of [real sequences][bookofproofs$875] can be carried over to the concept of _convergence of functions_. This is possible if we have infinitely many functions `$f_n:D\to\mathbb R,$` (i.e. for `$n=0,1,2,\ldots$`) which:
* all have the same domain `$D$`
* and at every point `$x\in D$` the [real sequence][bookofproofs$875] `$(f_n(x))_{n\in\mathbb N}$` converges to a [limit][bookofproofs$141] to a `$\lim_{n\to\infty} f_n(x)=f(x).$`

Such a _pointwise_ convergence to the function `$f$` (i.e. at the point `$x\in D$`) is not, in general, sufficient to be able to predict the properties of the limit function `$f,$` if we known the properties of the infinitely many given functions `$f_n.$` Concluding the properties of `$f$` based on the known properties of `$f_n$` becomes, however, possible, if the `$f_n$` converge "similarly quickly" and at "every  point" `$x\in D.$` This so called _uniform convergence_ is what this section of <strong><span style='color:orange'>Bookof</span><span style='color:lightblue'>Proofs</span></strong> will be about. It will contain a rigorous definition as well as the rules, which other properties exactly of `$f$` can be concluded based on those of `$f_n$` if uniform convergence is in place.
