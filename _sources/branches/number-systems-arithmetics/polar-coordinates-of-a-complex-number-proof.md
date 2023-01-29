layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$3021
orderid: 50
parentid: bookofproofs$6750
title: 
description: Proof of POLAR COORDINATES OF A COMPLEX NUMBER ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: polar coordinates,polar coordinate,polar coordinate of complex number,polar coordinates of complex numbers,polar,polar coordinates uniquely represent the complex numbers,proof
contributors: bookofproofs

---


---

* By hypothesis, `$z\in\mathbb C$` can is a [complex number][bookofproofs$216].
* If `$z=0,$` we can write `$z=0\cdot\exp(i\phi)$` with an arbitrary `$\phi\in\mathbb R,$` with the [complex exponential function][bookofproofs$1747] `$\exp:\mathbb C\to\mathbb  C.$`
* Therefore, let `$z\neq 0.$`
* Since `$z\neq 0$`, it has a [positive][bookofproofs$1107] [absolute value][bookofproofs$1247] `$r:=|z| > 0.$` 
* Set `$\zeta:=z/r,$` then `$|\zeta|=1.$`
* We can write this complex number as `$\zeta=\xi+i\eta.$`
* Note that `$\xi^2+\eta^2=1.$`
* By setting `$cos(\phi):=\xi$` and `$\sin(\phi):=\eta$`, we can deduce from [Euler's formula][bookofproofs$1783] `$$\zeta=\exp(i\phi)=\cos(\phi)+i\sin(\phi).$$`
* It follows that `$$z=r\exp(i\phi).$$`
* It remains to be shown that this polar representation of the complex number `$z$` is unique.
* But this follows from the [general case of the Euler's identity][bookofproofs$6745] by which from the equality of `$\exp(i\phi)=\exp(i\psi)$` it follows that `$\exp(i(\psi-\psi)=1.$` 
* It follows, `$\exp(i\phi)$` is unique modulo `$k\cdot 2\pi$` for all [integers][bookofproofs$844] `$k\in\mathbb Z.$`
