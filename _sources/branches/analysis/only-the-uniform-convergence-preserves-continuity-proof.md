layout: proof
categories: branches,analysis
nodeid: bookofproofs$8391
orderid: 50
parentid: bookofproofs$8390
title: 
description: PROOF OF ONLY THE UNIFORM CONVERGENCE PRESERVES CONTINUITY ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581,bookofproofs$586
keywords: uniform convergence preserves continuity,uniform convergence continuity,proof
contributors: bookofproofs

---


---

* By hypothesis, `$D\subset\mathbb R$` and let `$f_n:D\to\mathbb R$` are [continuous functions][bookofproofs$1260] on `$D.$` 
* Assume, the sequence `$(f_n)_{n\to\mathbb N}$` is [uniformly convergent][bookofproofs$8382] to a limit function `$f:D\to\mathbb R.$` 
   * By definition of uniformly convergent, there is an index `$N\in\mathbb N$` such that `$|f_N(x)-f(x)| < \frac {\epsilon}{3}$` for all `$x\in D.$` 
   * Since all `$f_n:D\to\mathbb R$` are [continuous][bookofproofs$1260] on `$D,$` so is `$f_N.$` 
   * By definition of continuous, there is a `$\delta > 0$` such that `$|f_N(x)-f_N(x^\prime)|<\frac {\epsilon}{3}$` for all `$x^\prime\in D$` with `$|x-x^\prime| < \delta.$`
   * By the [triangle inequality][bookofproofs$588], for all `$x^\prime\in D$` with `$|x-x^\prime| < \delta$`: `$$|f(x)-f(x^\prime)|\le |f(x)-f_N(x)|+|f_N(x)-f_N(x^\prime)|+|f_N(x^\prime)-f(x^\prime)| < \frac {\epsilon}{3}+\frac {\epsilon}{3}+\frac {\epsilon}{3}=\epsilon.$$`
   * It follows by definition of continous, that `$f:D\to\mathbb R$` is continous. 
* Now, assume the sequence `$(f_n)_{n\to\mathbb N}$` is only [pointwise convergent][bookofproofs$8382] to a limit function `$f:D\to\mathbb R.$`
   * As an example, consider `$f_n(x):=x^n$` on the [closed real interval][bookofproofs$1153] `$[0,1].$` 
   * Clearly, the functions `$x^n$` are [continuous][bookofproofs$1260] on `$[0,1].$` 
   * Moreover, for all `$x\in[0,1)$`, `$\lim_{n\to\infty} x^n=0,$` while for `$x=1$`, `$\lim_{n\to\infty} x^n=1.$`
   * The function `$f$` is therefore not continous at `$x=1\in[0,1].$`
   * Dispite the fact that for every `$x\in[0,1]$`, `$\lim_{n\to\infty} f_n=f,$` i.e. the continous functions `$f_n$` [converge only pointwise][bookofproofs$8382] to `$f.$`
