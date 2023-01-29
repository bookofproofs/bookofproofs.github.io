layout: proof
categories: branches,analysis
nodeid: bookofproofs$8384
orderid: 50
parentid: bookofproofs$8383
title: 
description: PROOF OF MINKOWSKI'S INEQUALITY FOR INTEGRAL P-NORMS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: minkowski's inequality for integral p-norm,proof
contributors: bookofproofs

---


---

* By hypothesis, `$[a,b]$` is a [closed real interval][bookofproofs$1153], `$p\ge 1$` is a [real numbers][bookofproofs$1105], and `$f,g:[a,b]\to\mathbb R$` are two [Riemann-integrable functions][bookofproofs$1763].
* Since `$f,g$` are Riemann-integrable, so are the functions `$f+g,$` `$f^p,$` and `$g^p.$`
* Let `$n\ge 1$` and `$h:=\frac{b-a}n.$` 
* The [Riemann sum converges to the Riemann integral][bookofproofs$6801], for suitably big `$n$` and the mash points `$\xi_k:=h*k+a,$` `$k=1,\ldots,n.$` 
* According to the [Minkowski's inequality][bookofproofs$6792] we get with the [p-norms][bookofproofs$6789] of the vectors `$\phi:=(f(\xi_1),f(\xi_2),\ldots,f(\xi_n))$`, `$\psi:=(g(\xi_1),g(\xi_2),\ldots,g(\xi_n))$`: `$$\begin{eqnarray}\left(\sum_{k=1}^n|f(\xi_k)+g(\xi_k)|^p\right)^{\frac 1p}\cdot h&\le &\left(\sum_{k=1}^n|f(\xi_k)|^p\right)^{\frac 1p} h+\left(\sum_{k=1}^n|g(\xi_k)|^p\right)^{\frac 1p} h\nonumber\\&=&||\phi||_p\cdot h+||\psi||_p\cdot h.\nonumber\end{eqnarray}$$`
* For `$n\to\infty$` we get with the [integral p-norms][bookofproofs$6804] the inequality `$$||f+g||_p\le ||f||_p+||g||_p.$$`
