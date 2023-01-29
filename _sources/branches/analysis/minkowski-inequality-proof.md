layout: proof
categories: branches,analysis
nodeid: bookofproofs$2921
orderid: 50
parentid: bookofproofs$6792
title: 
description: PROOF OF MINKOWSKI'S INEQUALITY ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: minkowski's inequality,proof
contributors: bookofproofs

---


---

* By hypothesis, let `$p\in[1,\infty)$` and `$x=(x_1,x_2,\ldots x_n)$` and `$y=(y_1,y_2,\ldots y_n)$` be two [vectors][bookofproofs$560] of a vector space `\(V\)` over the [field of real numbers][bookofproofs$1638] `$\mathbb R$` or the [field of complex numbers][bookofproofs$1690] `$\mathbb C$`. 
* If `$p=1$`, the inequality follows from the [triangle inequality][bookofproofs$588].
* Let `$p > 1$` and define `$q$` by `$\frac 1p+\frac 1q=1,$` i.e. `$q=\frac{p}{p-1}.$`
* Consider the vector `$z\in\mathbb C^n$` (or, in real case, `$z\in\mathbb R^n$`) with `$z_\nu:=|x_\nu+y_\nu|^{p-1}$` for `$\nu=1,\ldots,n.$` 
* Then we get `$z_\nu^q=|x_\nu+y_\nu|^{q(p-1)}=|x_\nu+y_\nu|^{p}$` for `$\nu=1,\ldots,n,$` and this yields for the [q-norm][bookofproofs$6789] of the vector `$z$` `$$\begin{array}{rcl}||z||_q&=&\left(\sum_{\nu=1}^n|z_\nu|^q\right)^{1/q}\\
&=&\left(\sum_{\nu=1}^n|x_\nu+y_\nu|^{p}\right)^{1/q}\\
&=&\left(\sum_{\nu=1}^n|x_\nu+y_\nu|^{p}\right)^{1/p\cdot p/q}\\
&=&||x+y||_p^{p/q}.\end{array}$$`
* We can now estimate:
   * `$\sum_{\nu=1}^n|x_\nu+y_\nu||z_\nu|\le \sum_{\nu=1}^n|x_\nu z_\nu|+\sum_{\nu=1}^n|y_\nu z_\nu|$` by the [triangle inequality][bookofproofs$588], and 
   * `$\le (||x||_p+||y||_p)||z||_q$` by the [Hölder's inequality][bookofproofs$6790].
* This yields by the definition of the vector `$z$`
`$$\begin{array}{rcl}||x+y||_p^p&=&\sum_{\nu=1}^n|x_\nu+y_\nu|^p\\
&=&\sum_{\nu=1}^n|x_\nu+y_\nu||x_\nu+y_\nu|^{p-1}\\
&=&\sum_{\nu=1}^n|x_\nu+y_\nu||z_\nu|\\
&\le&(||x||_p+||y||_p)||z||_q\\
&=&(||x||_p+||y||_p)||x+y||_p^{p/q}.\end{array}$$`
* Since `$p-\frac pq=1$`, we get (dividing both sides of the last inequality by `$||x+y||_p^{p/q}$`) `$$||x+y||_p\le ||x||_p+||y||_p.$$`
