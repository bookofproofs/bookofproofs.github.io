layout: proof
categories: branches,analysis
nodeid: bookofproofs$6712
orderid: 50
parentid: bookofproofs$6709
title: 
description: Proof of LIMIT OF NTH ROOT ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: limit of the nth root of a positive constant,proof
contributors: bookofproofs

---


---

* Let `$(a_n)_{n\in\mathbb N}$` be a [real sequence][bookofproofs$875] defined by `$a_n=\sqrt[n]{a}$` for some [positive real number][bookofproofs$1107] `$a > 0$` and all `$n\in\mathbb N$`.
* By definition, the nth-root can be written as the [generalized power of `$x$`][bookofproofs$1626], i.e. as `$\sqrt[n]{a}=\exp_x\left(\frac 1n\right)$`, i.e. the  [exponential function to the general base `$x$`][bookofproofs$1603].
* Since the [exponential function of general base is continuous][bookofproofs$1610], we have `$$\lim_{n\to\infty} a_n=\lim_{n\to\infty}\sqrt[n]{a}=\lim_{n\to\infty}\exp_a\left(\frac 1n\right)=\exp_a\left(\lim_{n\to\infty}\frac 1n\right),\quad\quad( * )$$` which follows from the [exchangeability of the limit of function values with the function value of the limit of arguments for continuous functions][bookofproofs$6710].
* Since [it was proven][bookofproofs$6713] that `$\lim_{n\to\infty}\frac 1n=0,$`, we have that `$( * )$` equals `$\exp_a(0).$`
* By [definition][bookofproofs$1603], `$\exp_a(0)=\exp(0\cdot \log (a))=\exp(0).$`
* Since [it was proven][bookofproofs$1423] that `$\exp(0)=1$`, it follows that `$\lim_{n\to\infty}\sqrt[n]{a}=1.$`
