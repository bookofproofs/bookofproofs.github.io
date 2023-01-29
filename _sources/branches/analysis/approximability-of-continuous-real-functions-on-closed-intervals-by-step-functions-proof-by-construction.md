layout: proof
categories: branches,analysis
nodeid: bookofproofs$6620
orderid: 50
parentid: bookofproofs$6619
title: 
description: PROOF BY CONSTRUCTION Proof of APPROXIMABILITY OF CONTINUOUS REAL FUNCTIONS ON CLOSED INTERVALS BY STEP FUNCTIONS &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$581
keywords: approximability,closed,continuous,functions,intervals,real,step,proof
contributors: bookofproofs

---


---

* Let `$[a,b]$` be a [closed real interval][bookofproofs$1153].
* Let `$\mathbb R$` be the [set of real numbers][bookofproofs$1105].
* Let `\(f:[a,b]\mapsto \mathbb R\)` a [continuous function][bookofproofs$219].
* It is to be shown that for every `\(\epsilon > 0\)` there exist some [step functions][bookofproofs$1751] `\(\phi:[a,b]\mapsto\mathbb R\)` and `\(\psi:[a,b]\mapsto\mathbb R\)` with `$(i)$` `$\phi(x) \le f(x)\le \psi(x)$` and `$(ii)$` `$|\phi(x)-\psi(x)|\le\epsilon$` for all `$x\in[a,b].$` This will be shown by construction.
   * Because all [continuous real functions on closed intervals are uniformly continuous][bookofproofs$6616], so is `$f$`.
   * This means that for every `$\epsilon > 0$` there is a `$\delta > 0$` such that `$|f(x)-f(y)| < \frac\epsilon2$` for all `$x,y\in D$` with `$|x-y| < \delta.$`
   * Because of the [existence of arbitrarily small positive rational numbers][bookofproofs$1846], we can choose a [natural number][bookofproofs$718] `\(n\)` big enough such that `$\frac 1n < \delta/(b-a)$`, or, equivalently `$\frac {b-a}n < \delta$`.
   * By setting `$$t_k:=a+k\frac{b-a}n,\quad k=0,1,\ldots, n,$$` we get an equidistant partition of the closed interval `$[a,b]$` with `$a=t_0 < t_1 < \ldots < t_n=b.$`
   * Set `$\phi(a):=\psi(a):=f(a)$`, and for `$k=1,\ldots,n$` and `$t_{k-1} < x\le t_k$` set `$$\phi(x):=f(t_k)-\frac\epsilon2,\quad \psi(x):=f(t_k)+\frac\epsilon2.$$`
   * By construction, it follows that `$|\phi(x)-\psi(x)|\le\epsilon$` for all `$x\in[a,b],$` thus `$(2)$` is proven.
   * For all `\(x\in ]t_{k-1},t_k]\)` we have by construction `$$-\frac \epsilon2 < f(x)-f(t_k) < \frac \epsilon2,$$` thus `$$\phi(x) = f(t_k)-\frac \epsilon2 < f(x) < f(t_k) + \frac \epsilon2=\psi(x),$$` therefore  `$\phi(x) \le f(x)\le \psi(x)$`  for all `$x\in[a,b],$` thus `$(1)$` is proven.
