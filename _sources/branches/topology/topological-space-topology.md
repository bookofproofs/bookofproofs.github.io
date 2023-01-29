layout: definition
categories: branches,topology
nodeid: bookofproofs$6189
orderid: 50
parentid: bookofproofs$132
title: Topological Space, Topology
description: TOPOLOGICAL SPACE, TOPOLOGY ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$6907
keywords: topological,topological space,topology,topological spaces,topologies
contributors: bookofproofs

---


---

A **topological space** is an [ordered pair][bookofproofs$747] `$(X,\mathcal O)$` of a [set][bookofproofs$550] `$X$` together with a set of its [subsets][bookofproofs$552] [subset][bookofproofs$552] `$\mathcal {O}$` (called its **topology**), which obeys the following axioms:

1. The empty set `\(\emptyset\)` and the whole set `\(X\)` are elements of the topology (i.e. `\({\emptyset\in\mathcal {O}}\)` and `\({X\in\mathcal {O}}\)` ).
1. The [intersection][bookofproofs$6828] of [finitely many][bookofproofs$985] elements of the topology `$\mathcal O$` is an element of the topology, i.e. if `\(U_{1},\ldots ,U_{n}\in {\mathcal {O}}\)`, then also `\(U_{1}\cap \ldots \cap U_{n}\in {\mathcal {O}}\)`.
1. Every [union][bookofproofs$6827] of elements of the topology is again an element of it, i.e. with `\(U_{i}\in {\mathcal {O}}\)` for each `\(i\in I\)` (for an arbitrary [index set][bookofproofs$6198] `\(I\)`) we have also `\(\bigcup _{i\in I}U_{i}\in {\mathcal {O}}\)`.

### Notes

* A topological space is defined simply by a postulating that subsets of an arbitrary _carrier set_ `$X$` fulfill the above properties. 
* Because the axioms `$1$` to `$3$` do not uniquely define a topological space, it is possible to define many different topologies `$\mathcal O$` on a set `$X.$` 
* Even a set `$X=\{a,b\}$` with only two elements has different topologies (resulting in different topological spaces). How many? The reader might use this example as an exercise. (Hint: Consider all non-empty subsets of the power set `$\mathcal P(\{a,b\})$`).
