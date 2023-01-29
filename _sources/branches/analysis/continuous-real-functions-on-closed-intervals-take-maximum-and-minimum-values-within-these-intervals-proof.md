layout: proof
categories: branches,analysis
nodeid: bookofproofs$2956
orderid: 50
parentid: bookofproofs$6696
title: 
description: Proof of CONTINUOUS REAL FUNCTIONS ON CLOSED INTERVALS TAKE MAXIMUM AND MINIMUM VALUES WITHIN THESE INTERVALS ★ master maths ✔ visit BookOfProofs!
references: bookofproofs$581
keywords: continuous functions,closed intervals,maximum,minimum,proof
contributors: bookofproofs

---


---

* By hypothesis `$[a,b]$` is a [closed real interval][bookofproofs$1153] and `$f:[a,b]\to\mathbb R$` is [continuous][bookofproofs$1260].
* We take `$A$` as the [supremum][bookofproofs$6669] of the [image set][bookofproofs$592] `$\{(f(x)\mid x\in[a,b]\}.$` Please note that `$A$` is either a [real number][bookofproofs$1105] or `$A=\infty$` if the image set is [unbounded][bookofproofs$584].
* We have to show that `$A$` is a real number (which is equivalent to `$f(x)$` is bounded on `$[x,y]$`).
   * The definition of a supremum of the image set is equlivalent to there is a [convergent real sequence][bookofproofs$141] `$(x_n)_{n\in\mathbb N}$` with `$x_n\in[a,b]$` `$\lim_{n\to\infty} f(x_n)=A.$`
   * Since `$[a,b]$` is a [bounded subset of real numbers][bookofproofs$584], the [real sequence][bookofproofs$875] `$(x_n)_{n\in\mathbb N}$` with `$x_n\in[a,b]$` is a [bounded sequence][bookofproofs$1136].
   * Since  [every bounded real sequence has a convergent subsequence][bookofproofs$1152], so does `$(x_n)_{n\in\mathbb N}.$`
   * In other words, there is a [subsequence][bookofproofs$6610] `$(x_{n_k})_{k\in\mathbb N}$` of `$(x_n)_{n\in\mathbb N}$` such that  `$$\lim_{k\to\infty} x_{n_k}=\alpha$$` for some `$\alpha\in[a,b].$`  
   * Since `$f$` is continuous, we have `$$\lim_{k\to\infty} f(x_{n_k})=f(\alpha).$$`
   * Therefore, `$A=f(\alpha).$` In particular `$A$` is a real number and it is the [maximum][bookofproofs$6602] of the image set.

Note: The proof for the existence of a minimum can be formulated analogously, replacing `$f$` by `$-f$`, `$\sup$` by the infimum `$\inf,$` and `$\max$` by the minimum `$\min.$`
