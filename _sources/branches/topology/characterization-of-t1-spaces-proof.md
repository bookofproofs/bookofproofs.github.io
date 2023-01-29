layout: proof
categories: branches,topology
nodeid: bookofproofs$8623
orderid: 50
parentid: bookofproofs$8622
title: 
description: Proof of CHARACTERIZATION T1 SPACES ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$8613
keywords: singletons in t1 spaces,characterization of t1 spaces,proof
contributors: bookofproofs

---


---

By hypothesis, `$(X,\mathcal O)$` is a [topological space][bookofproofs$6189].
### "`$\Rightarrow$`"

* Assume, `$X$` is a [$T_1$ space][bookofproofs$6199].
* Let `$\{x\}\subseteq X$` be a [singleton][bookofproofs$8034] [subset][bookofproofs$552] of `$X.$` 
* Case 1: The [set difference][bookofproofs$6830] is [empty][bookofproofs$550], i.e. `$X\setminus \{x\}=\emptyset.$`
   * Then `$\{x\}=X$` and `$\{x\}$` is [closed][bookofproofs$853].
* Case 2: `$X\setminus \{x\}\neq \emptyset.$`
   * Then there is an `$y\in X\setminus \{x\}$` with `$y\neq x$` 
   * Since `$X$` is a `$T_1$` space, there is an open set `$U\in\mathcal O$` with `$x\not\in U$` and `$y\in U\subseteq X\setminus \{x\}.$`
   * Since this is the case for every such `$y$`, the set `$X\setminus\{x\}$` is [open][bookofproofs$853].
   * Thus, `$\{x\}$` is [closed][bookofproofs$853].
### "`$\Leftarrow$`"
     
* Assume, every [singleton][bookofproofs$8034] [subset][bookofproofs$552] of  `$X$` is [closed][bookofproofs$853].
* Let `$x,y\in X$` with `$x\neq y.$`
* Since `$\{x\}$` and `$\{y\}$` are closed, `$X\setminus\{x\}$` and `$X\setminus\{y\}$` are open.
* Moreover, `$X\setminus\{x\}$` is an open set not containing `$y$` and `$X\setminus\{y\}$` is an open set not containing `$x.$`
* Thus, `$X$` is a `$T_1$` space.
