layout: solution
categories: branches,set-theory
nodeid: bookofproofs$8308
orderid: 50
parentid: bookofproofs$8307
title: 
description: SOLUTION OF TO CONSTRUCT A PARTITION OF A GIVEN SET ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$8297
keywords: construct a partition,constructing partitions,partition sets,solution
contributors: bookofproofs

---


---

### Creating Partitions Using Fibers of Surjective Functions

* Let `$f:X\to Y$` be a given [surjective function][bookofproofs$770].
* By definition of surjective functions, every element `$y\in Y$` has an `$x\in X$` with `$f(x)=y.$`
* In general, there can be _many_ such elements `$x\in X,$` with `$f(x)=y,$` called the [fiber][bookofproofs$592] `$f^{-1}(y):=\{x\in X\mid f(x)=y,\;y\in Y\}.$`
* Since `$f$` is a function, for _any two_ `$y_1,y_2\in Y,$` the fibers `$f^{-1}(y_1)$` and `$f^{-1}(y_2)$` are [disjoint][bookofproofs$7985] in `$X.$`
* Therefore, the _all fibers_ `$f^{-1}(y),$` `$y\in Y$` arbitrary, are [mutually disjoint][bookofproofs$6227] in `$X.$`
* This means that the set of all fibers `$$\{f^{-1}(y)\mid y\in Y\}$$` is a [set partition][bookofproofs$8305] of `$X.$`

### Creating Partitions Using Equivalence Relations

* Let `$R\subseteq X\times X$` be a given [equivalence relation][bookofproofs$574].
* Then, for every element `$x\in X,$` we have an [equivalence class][bookofproofs$7990] `$[x]:=\{z\in X, zRx\}.$`
* Now, _any two_ equivalence classes `$[x]\neq [y]$` are [disjoint][bookofproofs$7985] in `$X,$` because otherwise, 
   * for an element `$z\in [x]\cap [y]$` we would have `$zRx$` and `$zRy.$` 
   * Because `$R$` is an equivalence relation, it is [transitive and symmetric][bookofproofs$572].
   * Therefore, from `$zRx$` and `$zRy$` it would follow that `$xRy$`, in [contradiction][bookofproofs$744] to `$[x]\neq [y].$`
* Therefore, _all equvalence classes_ `$[x]$`, `$x\in X$` are [mutually disjoint][bookofproofs$6227].
* This means that the [quotient set][bookofproofs$7991] of all equivalence classes `$$\{[x]\mid x\in X\}$$` is a [set partition][bookofproofs$8305] of `$X.$`

### Differences between the two possibilities

A partition built by a given equivalence relation can itself be reversely used to define this equivalence relation, i.e. if we are given partition, then its elements can be re-interpreted as equivalence classes of an equivalence relation. In other words, partitions and equivalence relations are mathematical concepts, which are very closely related to each other.

This one-to-one correspondence between partitions and equivalence relations cannot be observed for partitions built by means of fibers of a given surjective function. For a given partition, it is usually not possible to find an appropriate surjective function. The reason for this is simple. A given partition of a set `$X$` is independent of another set `$Y$`, which we need to define a function between `$X$` and `$Y.$`
