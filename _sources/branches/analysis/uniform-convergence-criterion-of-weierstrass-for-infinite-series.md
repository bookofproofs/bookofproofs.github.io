layout: proposition
categories: branches,analysis
nodeid: bookofproofs$8397
orderid: 600
parentid: bookofproofs$8381
title: Uniform Convergence Criterion of Weierstrass for Infinite Series
description: UNIFORM CONVERGENCE CRITERION OF WEIERSTRASS FOR INFINITE SERIES ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: uniform convergence criterion of weierstrass,weierstraß,weierstrass criterion
contributors: bookofproofs


---
Note that for a domain `$D$`, the [infinite series][bookofproofs$1109] of functions `$f_n:D\to\mathbb F,$` i.e. the sum `$\sum_{n=0}^\infty f_n(x)$` is nothing else as the sequence `$(g_m(x))_{m\in\mathbb N}$` of its [partial sums][bookofproofs$1109] `$g_m(x):=\sum_{n=0}^m f_n(x).$` We can therefore apply the notion of [uniform convergence][bookofproofs$8381] also to the members of the sequence `$(g_m)_{m\in\mathbb N}.$` Clearly, by saying that `$(g_m(x))_{m\in\mathbb N}$` was [uniformly (or pointwise) convergent][bookofproofs$8381] to a limit function, we mean that this limit is the function `$f(x):=\sum_{n=0}^\infty f_n(x).$` Note that in this case, the terms of the infinite series `$f_n$` depend on two variables - the index `$n$` and the argument variable `$x,$` - while the limit function `$f$` only depends on the variable `$x.$`

The following proposition due to <a href="https://mathshistory.st-andrews.ac.uk/Biographies/Weierstrass/">Karl-Theodor Weierstrass</a> (1815 - 1897) creates a criterion for the uniform convergence in connection with an infinite series:

---

Let `$\mathbb F$` be a either the [field of real numbers][bookofproofs$1640] or the [field of complex numbers][bookofproofs$1690] and let `$D\subset \mathbb F.$` The [infinite series][bookofproofs$1109] of functions `$f_n:D\to\mathbb F$` `$$f(x):=\sum_{n=0}^\infty f_n(x)$$` converges [absolutely][bookofproofs$198] and [uniformly][bookofproofs$8382] to the function `$f:D\to\mathbb F,$` if the infinite series of [supremum norms][bookofproofs$8392] `$$A:=\sum_{n=0}^\infty ||f_n||_\infty$$` converges to a [finite][bookofproofs$985] limit `$A < \infty.$`
