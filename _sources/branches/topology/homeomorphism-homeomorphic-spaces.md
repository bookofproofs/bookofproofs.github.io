layout: definition
categories: branches,topology
nodeid: bookofproofs$6197
orderid: 500
parentid: bookofproofs$129
title: Homeomorphism, Homeomorphic Spaces
description: HOMEOMORPHISM, HOMEOMORPHIC SPACES ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$6907
keywords: homeomorphic,homeomorphism,homeomorphisms,topologically equivalent
contributors: @Brenner,bookofproofs

---


---

Let `\(X\)` and `\(Y\)` be [topological spaces][bookofproofs$6189]. A [function][bookofproofs$592] `\(\varphi \colon X\longrightarrow Y\)`  is called an **homeomorphism**, if

* `\(\varphi\)` is [continuous][bookofproofs$6195] and 
* `\(\varphi\)` is [bijective][bookofproofs$771] and
* the [inverse][bookofproofs$407] `\(\varphi ^{-1}\)` is also continuous.

Two [sets][bookofproofs$550] `$X$` and `$Y$` are **homeomorphic** (or **topologically equivalent**), if there exists a homeomorphism `\(\varphi \colon X\longrightarrow Y\)` between them.

### Notes

* Homeomorphic sets are indistinguishable from a topological point of view since every open set of `$X$` corresponds to exactly one open set of `$Y$` and vice versa. 
* However, it is possible to have homeomorphic spaces `$X$` and `$Y$` with different [topologies][bookofproofs$6189].
* It is also possible that `$X$` and `$Y$` are homeomorphic, and have subsets `$A\subset X$` and `$B\subset Y$` that are also homeomorphic with each other, but there is no homomorphism of `$X$` and `$Y$` taking `$A$` onto `$B.$` For instance, take the subsets of real numbers `$A=\{0\}\cup[1,2]\cup\{3\}$` and `$B=[0,1]\cup \{2\}\cup \{3\}.$`
* Moreover, it is not automatically the case that if `$f$` is continuous and bijective, then `$f^{-1}$` is continuous. For instance, if `$X$` has discrete topology `$\mathcal O_X$` and `$Y$` has an indiscrete topology `$\mathcal O_Y,$` then the identity function `$id:X\to Y$` is continuous and bijective, but the inverse `$id^{-1}$` is not continuous.
