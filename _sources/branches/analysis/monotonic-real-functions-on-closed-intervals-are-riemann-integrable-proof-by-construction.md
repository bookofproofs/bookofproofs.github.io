layout: proof
categories: branches,analysis
nodeid: bookofproofs$6622
orderid: 50
parentid: bookofproofs$1767
title: 
description: PROOF BY CONSTRUCTION Proof of MONOTONIC REAL FUNCTIONS ON CLOSED INTERVALS ARE RIEMANN-INTEGRABLE &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$581
keywords: monotonic functions,integrable functions,proof
contributors: bookofproofs

---


---

* Let `\([a,b]\)` be a [closed real interval][bookofproofs$1153].
* Let `\(f:[a,b]\mapsto\mathbb R\)` be a [monotonic real function][bookofproofs$282].
* We will show by construction that `$f$` is [Riemann-integrable][bookofproofs$1763].
   * By setting `$$t_k:=a+k\frac{b-a}n,\quad k=0,1,\ldots, n,$$` we get an equidistant partition of the closed interval `$[a,b]$` with `$a=t_0 < t_1 < \ldots < t_n=b.$`
   * By setting `$$\begin{array}{rcl}\phi(x)&:=&f(t_{k-1}),\quad t_{k-1}\le x < t_k\\ \psi(x)&:=&f(t_{k}),\quad t_{k-1}\le x < t_k\\\phi(b)&:=&f(b)\\\psi(b)&:=&f(b)\end{array}$$` for `\(k=1,2,\ldots n\)` we achieve that `$\phi(x)\le f(x)\le \psi(x)$` for all `$x\in[a,b]$`.
   * Furthermore, we have by construction
`$$\begin{array}{rcl}\int_a^b\psi(x)dx-\int_a^b\phi(x)dx&=&\sum_{k=1}^n f(t_k)(t_k-t_{k-1})- \sum_{k=1}^n f(t_{k-1})(t_k-t_{k-1})\\&=&\frac{b-a}n\left(\sum_{k=1}^n f(t_{k})-\sum_{k=1}^n f(t_{k-1})\right)\\&=&\frac{b-a}n(f(t_n))-f(t_0)).\quad\quad ( * )\end{array}$$`
   * Because of the [existence of arbitrarily small positive rational numbers][bookofproofs$1846], `$( * )\le\epsilon,$` for sufficiently big [natural number][bookofproofs$718] `$n$`.
   * This means that   `$f$` is [Riemann-integrable][bookofproofs$1763].