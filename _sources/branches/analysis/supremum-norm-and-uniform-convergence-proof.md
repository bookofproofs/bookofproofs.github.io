layout: proof
categories: branches,analysis
nodeid: bookofproofs$8394
orderid: 50
parentid: bookofproofs$8393
title: 
description: PROOF OF SUPREMUM NORM AND UNIFORM CONVERGENCE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581,bookofproofs$586
keywords: supremum norm and uniform convergence,proof
contributors: bookofproofs

---


---

In the following, `$D$` is a [set][bookofproofs$550] and `$\mathbb F$` denotes either the [field of real numbers][bookofproofs$1640] or the [field of complex numbers][bookofproofs$1690].
### "`$\Rightarrow$`"

* Assume, the sequence of functions `$f_n:D\to\mathbb F$` is [uniformly convergent][bookofproofs$8382] to a limit function `$f:D\to\mathbb F.$`
* This is equivalent to the statement: For any given `$\epsilon > 0$` there is an index `$N$` such that `$|f_n(x)-f(x)| <\epsilon$` for all `$n\ge N$` and all `$x\in D.$`
* By the definition of the [supremum norm][bookofproofs$8392], this is equivalent to the statement: For any given `$\epsilon > 0$` there is an index `$N$` such that `$||f_n-f||_\infty <\epsilon$` for all `$n\ge N$` and all `$x\in D.$`
* By the definition of [convergent sequence][bookofproofs$141], this means `$\lim_{n\to\infty}||f_n-f||_\infty=0.$`

### "`$\Leftarrow$`"

* Assume, `$\lim_{n\to\infty}||f_n-f||_\infty=0.$`
* Now, reverse the argumentation of the "`$\Rightarrow$`" block.
