layout: axiom
categories: branches,topology
nodeid: bookofproofs$8594
orderid: 800
parentid: bookofproofs$101
title: Filter
description: FILTER ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8336,bookofproofs$8560
keywords: filter,filters,set filtered by,filtered by,filtered set,filtered sets,sets filtered by
contributors: bookofproofs

---


---

Let `$X$` be a [set][bookofproofs$550]. A **filter** `$\mathcal F$` on `$X$` is a set of [subsets][bookofproofs$552] of `$X$` fulfilling the following axioms:

1. `$F$` contains with every set also all of its [supersets][bookofproofs$552], formally `$$O\in F\wedge O\subseteq S\Rightarrow S\in F.$$`
1. `$F$` contains for each pair of set elements also their [intersection][bookofproofs$6828], formally `$$O_1,O_2\in\mathcal F\Rightarrow O_1\cap O_2\in\mathcal F.$$`
1. `$F$` is not the [empty set][bookofproofs$550] and it does not contain the empty set `$$\mathcal F\neq\emptyset\wedge \emptyset\not\in\mathcal F.$$`

If `$X$` has a filter `$\mathcal F,$` then it is called **filtered by** `$\mathcal F.$`

### Notes

* A filter can be defined for any set, not only for topological spaces.
* Any [set of neighborhoods][bookofproofs$8563] of a point is a filter [according to its properties][bookofproofs$8616].