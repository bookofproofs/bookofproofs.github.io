layout: proof
categories: branches,analysis
nodeid: bookofproofs$2920
orderid: 50
parentid: bookofproofs$6790
title: 
description: PROOF OF HöLDER'S INEQUALITY ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: hölder's inequality,hoelder's inequality,proof
contributors: bookofproofs

---


---

* By hypothesis, `$p,q\in (1,\infty)$` with `$\frac 1p+\frac 1q=1$` and `$x=(x_1,x_2,\ldots x_n)$` and `$y=(y_1,y_2,\ldots y_n)$` are [vectors][bookofproofs$560] of a vector space `\(V\)` over the [field of real numbers][bookofproofs$1638] `\(\mathbb R\)` or the [field of complex numbers][bookofproofs$1690] `\(\mathbb C\)`. 
* Without loss of generality we can assume that the [p-norms][bookofproofs$6789] `$||x||_p|$` and `$||y||_q$` are both `$\neq 0$`, otherwise the inequality to be proven is trivial.
* For `$\nu=1,\ldots,n$` we set `$$\xi_\nu:=\left(\frac{|x_\nu|}{||x||_p}\right)^p,\quad\eta_\nu:=\left(\frac{|y_\nu|}{||y||_q}\right)^q.$$` 
* Note that by this definition and the definition of p-norms, `$\sum_{\nu=1}^n\xi_\nu=1$` and  `$\sum_{\nu=1}^n\eta_\nu=1$` and `$\xi_\nu,\eta_\nu\in(0,1)$` for `$\nu=1,\ldots,n.$`
* Therefore, we can apply the [lemma about an upper bound for the product of general powers][bookofproofs$6787] and get for `$\nu=1,\ldots,n$` the inequalities `$$\frac{|x_{\nu} y_{\nu}|}{||x||_p ||y||_q}=\xi_{\nu}^{1/p}\eta_{\nu}^{1/q}\le \frac{\xi_{\nu}}{p}+\frac{\eta_{\nu}}{q}.$$`
* Summing up both sides for `$\nu=1,\ldots,n$` yields `$$\frac{1}{||x||_p ||y||_q}\sum_{\nu=1}^n |x_{\nu} y_{\nu}|\le \frac 1p+\frac 1q=1.$$`
* It follows `$$\sum_{\nu=1}^n|x_\nu y_\nu|\le ||x||_p||x||_q.$$`
