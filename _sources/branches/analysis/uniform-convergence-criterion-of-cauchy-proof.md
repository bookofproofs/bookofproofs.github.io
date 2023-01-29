layout: proof
categories: branches,analysis
nodeid: bookofproofs$8396
orderid: 50
parentid: bookofproofs$8395
title: 
description: PROOF OF UNIFORM CONVERGENCE CRITERION OF CAUCHY ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$586
keywords: uniform convergence criterion of cauchy,proof
contributors: bookofproofs

---


---

### "`$\Rightarrow$`"

* Assume, the [sequence of functions][bookofproofs$8382] `$f_n:D\to\mathbb F$` is [uniformly convergent][bookofproofs$8382] to a function `$f:D\to\mathbb F.$`
* The [real sequence][bookofproofs$875] of [supremum norms][bookofproofs$8392] `$(||f_n-f||_\infty)_{n\to\infty}$` is therefore [convergent][bookofproofs$175].
* By the lemma [convergent sequences are Cauchy sequences][bookofproofs$1394], the sequence `$(||(f_n-f)||_\infty)_{n\to\infty}$` is a [Cauchy sequence][bookofproofs$1704].
* By definition, this means for every `$\epsilon > 0$` there is an index `$N$` such that the [supremum norm][bookofproofs$8392] `$||(f_n-f)-(f_m-f)||_\infty=||f_n-f_m||_\infty < \epsilon$` for all `$n,m\ge N.$`

### "`$\Leftarrow$`"

* Assume, for every `$\epsilon > 0$` there is an index `$N$` such that the [supremum norm][bookofproofs$8392] `$||f_n-f_m||_\infty < \epsilon$` for all `$n,m\ge N.$`
* This means that `$|f_n(x)-f_m(x)|<\epsilon$` for all `$x\in D$` and all `$n,m\ge N.$` 
* By definition of [Cauchy sequences][bookofproofs$1704], this means that `$(f_n(x))_{n\in\mathbb N}$` is a Cauchy sequence for all `$x\in D.$` 
* By the [completeness principle][bookofproofs$1108], this means that there is a limit `$y:=\lim_{n\to\infty}f_n(x)$` for all `$x\in D.$`
* In other words, there is a function `$f:D\to\mathbb F$` to which the [sequence of functions][bookofproofs$8382] `$f_n:D\to\mathbb F$` is [uniformly convergent][bookofproofs$8382].
