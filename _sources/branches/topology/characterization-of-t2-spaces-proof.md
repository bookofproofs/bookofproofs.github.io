layout: proof
categories: branches,topology
nodeid: bookofproofs$8625
orderid: 50
parentid: bookofproofs$8624
title: 
description: PROOF OF CHARACTERIZATION OF $T_2$ SPACES ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8613
keywords: characterization of t2 spaces,proof
contributors: bookofproofs


---


---

By hypothesis, `$(X,\mathcal O)$` is a [topological space][bookofproofs$6189].
### "`$\Rightarrow$`" 

* Assume, `$X$` is a [$T_2$ space][bookofproofs$6199].
* Let `$B$` be a [filter base]https://www.bookofproofs.org/branches/base-of-a-filter/.
* Further, assume that `$x,y$` are two distinct [limit points][bookofproofs$8573] of `$B.$`
   * Since `$X$` is a `$T_2$` space, there are disjoint [open sets][bookofproofs$853] `$O_x,O_y\in\mathcal O$` containing `$x$` and `$y$` respectively, i.e. `$x\in O_x$`, `$y\in O_y$` and `$O_x\cap O_y=\emptyset.$`
   * By the definition of a [limit point][bookofproofs$8573], `$O_x$` contains at least one point of `$B$` distinct from `$x$` and `$O_y$` contains at least one point of `$B$` distinct from `$y$`. 
   * But since `$B$` is a [filter base][bookofproofs$8595], _any_ two sets of `$B$` contain a set in `$B.$` 
   * Therefore, `$O_x\cap O_y$` contains a set in `$B.$`
   * But this is a [contradiction][bookofproofs$744] to `$O_x\cap O_y=\emptyset.$`

* It follows that `$x=y,$` i.e. `$B$` has only one unique limit point. 


### "`$\Leftarrow$`"

* Assume, `$B$` is a [filter base]https://www.bookofproofs.org/branches/base-of-a-filter/ `$B$` in `$X$` and has only one unique [limit point][bookofproofs$8573] `$x.$`
* Further assume that `$X$` is _not_ a `$T_2$` space.
   * By this assumption, there is a points `$y\in X$` distinct from `$x$` such that all open sets containing `$x$` and `$y$` respectively are not disjoint i.e. `$x\neq y$` but `$O_x\cap O_y\neq\emptyset$` for all `$O_x$` with `$x\in O_x$` and all `$O_y$` with `$y\in O_y.$`
   * Since `$B$` is a filter base, every [intersection][bookofproofs$6828] `$O_x\cap O_y$` contains a set in `$B.$`
   * But every such intersection has to contain a point `$y$` distinct from `$x.$`
   * This is a [contradiction][bookofproofs$744] to `$x\neq y.$`
* It follows that `$X$` is a `$T_2$` space.
