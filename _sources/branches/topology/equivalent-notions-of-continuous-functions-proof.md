layout: proof
categories: branches,topology
nodeid: bookofproofs$8585
orderid: 50
parentid: bookofproofs$8584
title: 
description: PROOF OF EQUIVALENT NOTIONS OF CONTINUOUS FUNCTIONS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$8336,bookofproofs$8560
keywords: equivalent notions of continuous functions,proof
contributors: bookofproofs

---


---

By hypothesis, `$(X,\mathcal O_X)$` and `$(Y,\mathcal O_Y)$` are [topological spaces][bookofproofs$6189] and `$f:X\to Y$` is a [function][bookofproofs$592].
### Ad `$(1)\Rightarrow(2)$`

* Assume, `$f$` is [continuous][bookofproofs$8583], i.e. the [inverse image][bookofproofs$592] `$f^{-1}[B]$` of every [open set][bookofproofs$853] `$B$` in `$Y$` is open in `$X.$`
* In particular, if `$B\subseteq Y$` and the [complement][bookofproofs$6829] `$B^C$` is open in `$Y,$` then `$f^{-1}[B^C]$` is open in `$X.$` 
* Therefore, if `$B$` is closed in `$Y,$` then `$f^{-1}[B]$` is closed in `$X.$`

### Ad `$(2)\Rightarrow(3)$`

* Assume, the [inverse image][bookofproofs$592] `$f^{-1}[B]$` of every [closed set][bookofproofs$853] `$B$` in `$Y$` is closed in `$X.$`
* Let `$B$` be a closed (but fixed)  [subset][bookofproofs$552] of `$Y.$`
* Since `$B$` is closed, it equals its [closure][bookofproofs$1202] `$B=B^-.$`
* Let `$A\subseteq X$` be any subset of `$X$` with `$f[A]=B.$` 
* Thus, `$f[A]=f[A]^-.$` 
* By assumption, `$f^{-1}[B]=f^{-1}[f[A]]$` is closed in `$X.$` 
* Therefore, `$A^-\subseteq f^{-1}[f[A]].$`
* Thus, `$f[A^-]\subseteq f[f^{-1}[f[A]]=f[A]=f[A]^ -.$` 
 
 
### Ad `$(3)\Rightarrow(4)$`

* Assume, the [image][bookofproofs$592] of the [closure][bookofproofs$1202] of a [subset][bookofproofs$552] `$A\subset X$` is contained in the closure of the image of this subset, formally `$f[A^-]\subseteq f[A]^-.$`
* Take `$A=X.$` Then `$X=X^-.$` 
* Let `$x\in X$` and let `$N_{f(x)}$` be a [neighborhood][bookofproofs$8563] `$N_{f(x)}$` of `$f(x)$` in `$Y.$` 
* Since `$N_{f(x)}$` is a neighborhood, it contains an [open set][bookofproofs$853] `$O\in O_Y$` with `$f(x)\in O\subseteq N_{f(x)}.$` 
* By `$(1)$`, the [inverse image][bookofproofs$592] `$f^{-1}[O]$` is open in `$X.$` 
* Set `$N_x:=f^{-1}[O].$`
* Then `$N_x$` is open in `$X$` with the [image][bookofproofs$592] `$f[N_x]=O.$`
* Since `$f(x)\in O$`, we have `$x\in N_x.$` 
* Altogether, we have found a neighborhood `$N_x$` of `$x$` such that `$f[N_x]\subseteq N_{f(x)}$` for any given `$x\in X$` and any neighborhood `$N_{f(x)}$` of `$f(x)$` in `$Y.$` 

### Ad `$(4)\Rightarrow(1)$`

* Assume, for each `$x\in X$` and each [neighborhood][bookofproofs$8563] `$N_{f(x)}$` of `$f(x)$` there exists a neighborhood `$N_x$` of `$x$` such that `$f[N_x]\subseteq N_{f(x)}.$`
* Let `$B\subseteq Y$` be open in `$Y.$` We have to show that `$f^{-1}[B]$` is open in `$X.$` 
* Take `$f(x)\in B.$`
* Since `$B$` is open, there is another open set `$O\subseteq Y$` contained in `$B$` that contains `$f(x).$` 
* In other words, `$B$` is a neighborhood of `$f(x)$` in `$Y.$`  
* By assumption, there exists a neighborhood `$N_x$` of `$x$` such that `$f[N_x]\subseteq B.$`
* Since `$N_x$` is neighborhood, it contains an open set `$Q\subseteq X$` containing `$x.$`
* Thus, `$Q\subseteq f^{-1}[f[Q]]\subseteq f^{-1}[B].$` 
* Thus, every point `$x$` in `$f^{-1}[B]$` contains an open set `$Q$` contained in `$f^{-1}[B],$` making `$f^{-1}[B]$` open in `$X.$`
