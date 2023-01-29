layout: proof
categories: branches,analysis
nodeid: bookofproofs$6618
orderid: 100
parentid: bookofproofs$6616
title: 
description: PROOF BY CONTRADICTION Proof of CONTINUOUS REAL FUNCTIONS ON CLOSED INTERVALS ARE UNIFORMLY CONTINUOUS &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$581
keywords: are,closed,continuous,functions,intervals,real,uniformly,proof
contributors: bookofproofs

---


---

* Let `$[a,b]$` be a [closed real interval][bookofproofs$1153], `$\mathbb R$` be the [set of real numbers][bookofproofs$1105] and `\(f:[a,b]\mapsto \mathbb R\)` a [continuous function][bookofproofs$219].
* We will [prove by contradiction][bookofproofs$744] to that `\(f\)` is [uniformly continuous][bookofproofs$6611], i.e. for every `$\epsilon > 0$` there is a `$\delta > 0$` such that `$|f(x)-f(y)| < \epsilon$` for all `$x,y\in D$` with `$|x-y| < \delta.$`
   * Assume, `$f$` is not uniformly continuous. 
   * Then there is an `$\epsilon > 0$` such that for every [natural number][bookofproofs$718] `$n > 0$`  such that there as some points `$x_n, y_n\in [a,b]$` with `$$|x_n-y_n| < \frac 1n\quad\text{ and }\quad |f(x_n)-f(y_n)|\ge \epsilon.$$`
   * `$(x_n)_{n > 0}$` is [bounded real sequence][bookofproofs$1136].
   * Because [every bounded real sequence has a convergent subsequence][bookofproofs$1152], so has `$(x_n)_{n > 0}.$` 
   * Let this [subsequence][bookofproofs$6610] be `$(x_{n_k})_{k\in\mathbb N}$`, and let its [limit][bookofproofs$141] be `$\lim_{k\to\infty} x_{n_k}=p.$`
   * Since [convergence preserves upper and lower bounds][bookofproofs$1145], and since `$a \le x_{n_k} \le b$` for all `$k\in\mathbb N$`, we have that `$p\in[a,b].$` 
   * Since `$|x_{n_k}-y_{n_k}| < \frac 1{n_k}$` by construction, we have also that `$\lim_{k\to\infty} y_{n_k}=p.$`
   * From the [definition of continuity][bookofproofs$219] of `$f$` it follows `$$\lim_{k\to\infty}\left(f(x_{n_k})-f(y_{n_k})\right)=f(p)-f(p)=0.$$`
   * This is a contradiction to `$|f(x_{n_k})-f(y_{n_k})|\ge \epsilon$` for all `$k\in\mathbb N.$`
   * Thus the assumption, `$f$` was not uniformly continuous must be wrong.
   * Therefore `\(f\)` is [uniformly continuous][bookofproofs$6611].
