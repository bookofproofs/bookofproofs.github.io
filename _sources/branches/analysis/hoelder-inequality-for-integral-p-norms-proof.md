layout: proof
categories: branches,analysis
nodeid: bookofproofs$8386
orderid: 50
parentid: bookofproofs$8385
title: 
description: PROOF OF HöLDER'S INEQUALITY FOR INTEGRAL P-NORMS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581,bookofproofs$586
keywords: hölder's inequality for integral p-norm,proof
contributors: bookofproofs

---


---

* By hypothesis, `$[a,b]$` is a [closed real interval][bookofproofs$1153], `$p,q > 1$` are [real numbers][bookofproofs$1105] with `$1/p+1/q=1,$` and `$f,g:[a,b]\to\mathbb R$` are two [Riemann-integrable functions][bookofproofs$1763].
* Since `$f,g$` are Riemann-integrable, so are the functions `$fg,$` `$f^p,$` and `$g^q.$`
* Let `$n\ge 1$` and `$h:=\frac{b-a}n.$` 
* The [Riemann sum converges to the Riemann integral][bookofproofs$6801], for suitably big `$n$` and the mash points `$\xi_k:=h*k+a,$` `$k=1,\ldots,n.$` 
* According to the [Hölder's inequality][bookofproofs$6790] we get with the [p-norms][bookofproofs$6789] of the vectors `$\phi:=(f(\xi_1),f(\xi_2),\ldots,f(\xi_n))$`, `$\psi:=(g(\xi_1),g(\xi_2),\ldots,g(\xi_n))$`: `$$\begin{eqnarray}\sum_{k=1}^n|f(\xi_k)g(\xi_k)|\cdot h&=&\sum_{k=1}^n|f(\xi_k)|h^{\frac 1p}\cdot |g(\xi_k)|h^{\frac 1q}\nonumber\\&\le& \left(\sum_{k=1}^n{|f(\xi_k)|^p}\right)^{\frac 1p}\cdot h^{\frac 1p}\cdot \left(\sum_{k=1}^n{|g(\xi_k)|^q}\right)^{\frac 1q}\cdot h^{\frac 1q}\nonumber\\&=&||\phi||_p||\psi||_q\cdot h.\nonumber\end{eqnarray}$$`
* For `$n\to\infty$` we get with the [integral p-norms][bookofproofs$6804] the inequality `$$\int_a^b |f(x)g(x)|dx\le ||f||_p||g||_q.$$`
