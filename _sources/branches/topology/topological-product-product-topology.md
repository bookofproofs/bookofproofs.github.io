layout: definition
categories: branches,topology
nodeid: bookofproofs$8569
orderid: 400
parentid: bookofproofs$319
title: Topological Product, Product Topology
description: TOPOLOGICAL PRODUCT, PRODUCT TOPOLOGY ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8336,bookofproofs$8560
keywords: topological product,product topology,topological products,product topologies,open box,open boxes,product space,product spaces,tychonoff topology,tychonoff topologies
contributors: bookofproofs

---


---

Let `$(X,\mathcal O_X)$` and `$(Y,\mathcal O_Y)$` be two [topological spaces][bookofproofs$6189]. The **topological product** (or **product space**) `$(Z,\mathcal O_Z)$` of `$X$` and `$Y$` is defined as `$$ (Z,\mathcal O_Z):=(X\times Y,\mathcal O_Z\},$$` where `$X\times Y$` denotes the usual [Cartesian product][bookofproofs$748].
![producttopology1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/producttopology1.png?raw=true)


The **product topology** `$\mathcal O_Z$` of the topological product is defined as a set of subsets `$U\subseteq X\times Y$` such that for every `$(x,y)\in U\in\mathcal O_Z$` there exist [open sets][bookofproofs$853] `$A\in\mathcal O_X$` and `$B\in\mathcal O_Y$` such that `$x\in A,$` `$y\in B,$` and `$A\times B\subset U.$`


![producttopology](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/producttopology.png?raw=true)


### Notes

* The Cartesian product `$A\times B$` is also called an **open box**.
* The product topology is the [coarsest][bookofproofs$8559] topology on `$Z$` such that all of the coordinate projection are [continuous][bookofproofs$8583]. This topology is called the **Tychonoff topology**.
