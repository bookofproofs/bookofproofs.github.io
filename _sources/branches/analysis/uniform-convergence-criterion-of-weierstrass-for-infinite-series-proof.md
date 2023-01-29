layout: proof
categories: branches,analysis
nodeid: bookofproofs$8398
orderid: 50
parentid: bookofproofs$8397
title: 
description: PROOF OF UNIFORM CONVERGENCE CRITERION OF WEIERSTRASS FOR INFINITE SERIES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: uniform convergence criterion of weierstrass,weierstraß,weierstrass criterion,proof
contributors: bookofproofs


---


---

* By hypothesis, `$\mathbb F$` is either the [field of real numbers][bookofproofs$1640] or the [field of complex numbers][bookofproofs$1690] and `$D\subset \mathbb F.$` Moreover, the [infinite series][bookofproofs$1109] of [supremum norms][bookofproofs$8392] `$A:=\sum_{n=0}^\infty ||f_n||_\infty$` of functions `$f_n:D\to\mathbb F$` converges to a [finite][bookofproofs$985] limit `$A < \infty.$`
* By the definition of the [supremum norm][bookofproofs$8392] `$|f_n(x)|\le ||f_n||_\infty$` for all `$x\in D.$`
* Therefore, by the [direct comparison test for absolutely convergent complex series][bookofproofs$1727], the series `$\sum_{n=1}^\infty f_n(x)$` "converges absolutely":https://www.bookofproofs.org/branches/absolutely-convergent-complex-serie for all `$x\in D.$`
* By definition, this means that the sequence `$(\phi_n)_{n\in\mathbb N}$` of [partial sums][bookofproofs$1109] `$\phi_m(x):=\sum_{n=1}^m f_n(x)$` [converges uniformly][bookofproofs$8382] to a function `$f:D\to\mathbb F.$`
