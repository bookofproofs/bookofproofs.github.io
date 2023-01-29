layout: definition
categories: branches,set-theory
nodeid: bookofproofs$985
orderid: 200
parentid: bookofproofs$185
title: Finite Set, Infinite Set
description: FINITE SET, INFINITE SET ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$983
keywords: finite,infinite,finite set,infinite set,finite sets,infinite sets,finite subset,infinite subsets,finitely many,infinitely many
contributors: bookofproofs

---
[Cardinals][bookofproofs$980] allow us to distinguish between finite and infinite sets very easy. But to really understand how this is accomplished, we have to make a connection between two facts:

* Classic mathematics allows some _atomic objects_ which are not sets themselves, like numbers, points, etc. In modern mathematics, almost _all_ mathematical objects are sets. We will see later in [number systems][bookofproofs$195], how numbers, including natural numbers, can be defined from a purely set-theoretical perspective. For the time being, just please keep in mind that not only the _set of natural numbers_ `$\mathbb N$` is a set, but also _every natural number_ `$n\in\mathbb N$` is a set. 
* For this reason, each natural number `$n$` is a representative of its own cardinal equivalence class `$|n|.$`

Now, we are able to define exactly what it means for a set to be finite or to be infinite.

---

A [set][bookofproofs$550] `$X$` is called **finite**, if both, `$X$` and a [natural number][bookofproofs$718] `$n\in\mathbb N$` belong to the same [cardinal][bookofproofs$980], formally `$|X|=|n|$` (we could even write `$X\in |n|$` to express this[^1]). If such a natural number `$n$` does not exist, then the set `$X$` is called **infinite**.[^2] 

[^1]: Please note that the cardinal `$|n|$` is an equivalence class, by definition, and must not to be mixed up with the absolute value of `$|n|$`, with the same notation! This fact justifies the notation `$X\in |n|.$`

[^2]: Please note that the existence of infinite sets is ensured by the [axiom of infinity][bookofproofs$678] and therefore, there are also infinite cardinal numbers.
