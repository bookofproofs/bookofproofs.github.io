layout: proof
categories: branches,analysis
nodeid: bookofproofs$3566
orderid: 50
parentid: bookofproofs$6752
title: 
description: Proof of N-TH ROOTS OF UNITY ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: roots of unity,root of unity,unit root,unity roots,proof
contributors: bookofproofs

---


---

* By hypothesis, `$n\in\mathbb Z$` is a [positive integer][bookofproofs$1075] with `$n\ge 2,$` `$z\in\mathbb C$` is a [complex number][bookofproofs$216], and `$z^n=1.$`
* By [polar coordinates of complex numbers][bookofproofs$6750] we haver `$z=|z|.\exp(i\phi)$` for some [real numbers][bookofproofs$1105] `$r,\phi\in\mathbb R$` and `$0\le \phi < 2\pi,$` `$\pi$` being the [number pi][bookofproofs$6738].
* Since `$z^n=1$`, taking the [absolute value of complex numbers][bookofproofs$1247] gives us `$|z|^n=1.$` 
* Thus, `$r=1.$`
* Therefore, `$z^n=(\exp(i\phi))^n=\exp(in\phi)=1.$`
* By the [geralized Euler's identity][bookofproofs$6745], there is an integer `$k\in\mathbb Z$` such that `$2k\pi=n\phi.$` 
* Thus, `$\phi=\frac{2k}{n}\pi.$` 
* Because `$0\le \phi < 2\pi$`, we have `$0\le k < n.$` 
* Thus, if `$z\in\mathbb C$` solves `$z^n=1,$` then `$z=\zeta_k:=\exp\left(2\pi i\frac{k}{n}\right),$` `$k=0,1,\ldots,n-1.$` 
* Vice versa, if `$z=\zeta_k,$` then `$z^n=\exp\left(i\frac{2k\pi}{n}\right)=1.$`
* Finally, if `$m(n)\equiv k(n)$` are [congruent][bookofproofs$8153] `$k(n)\equiv m(n)$` modulo `$n,$` then `$m=k+ln$` for some `$l\in\mathbb Z.$` But then
`$$\exp\left(i\frac{2m\pi}{n}\right)=\exp\left(i\frac{2(k+ln\pi}{n}\right)=\exp\left(i\frac{2k\pi}{n}\right)\cdot \exp\left(i 2l\pi\right)=\zeta_k\cdot 1.$$`
