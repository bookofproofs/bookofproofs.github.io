layout: axiom
categories: branches,set-theory
nodeid: bookofproofs$1427
orderid: 50
parentid: bookofproofs$81
title: Zermelo-Fraenkel Axioms
description: ZERMELO-FRAENKEL AXIOMS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$983
keywords: fraenkel,zermelo,zermelo fraenkel axioms,zermelo-fraenkel axioms,zermelo fraenkel
contributors: bookofproofs

---
Usually, we denote sets by capital letters `$X,Y,\ldots$`, while writing small letters `$x,y,\ldots$` for their elements. In the Zermelo-Fraenkel set theory, sets can be themselves elements of other sets. Thus, there is no reason to introduce a different notation for sets and their elements and many sources in literature do without a distinctive notation. Nevertheless, we will keep sticking to this notation, just to make it clearer which sets are meant to be _the elements_ and which sets are meant to _contain these elements_. When you read small letters `$x,y,\ldots$` below, please keep in mind that they denote sets again.

---

A **set** is a mathematical object fulfilling the following axioms:

* [Axiom of Existence][bookofproofs$8015] - There is a universal set. Some sources mention the equivalent  [Axiom of Empty Set][bookofproofs$666] - There is an (improper) set, which does not contain any elements.
* [Axiom of Extensionality][bookofproofs$551] - If each element of the set `\(X\)` is also an element of the set `\(Y\)` and vice versa, then both are the same. In other words, a set is determined by its elements.
* [Schema of Separation Axioms][bookofproofs$675] - If `\(p(z)\)` is a definite property, then for all sets `\(X\)` there is a subset `\(Y\)` consisting of those elements `\(x\)`, for which `\(p(x)\)` is satisfied.
* [Axiom of Pairing][bookofproofs$667] - For any sets `\(X, Y\)` there exists a set containing a collection of the two sets as its elements, i.e. the set `\(\{X, Y\}.\)`
* [Axiom of Union][bookofproofs$674] - For each set `\(X\)` there is a set containing all elements of the elements of `$X$`.
* [Axiom of Power Set][bookofproofs$716] - For each set `\(X\)` there exists a set containing all subsets of `$X.$`
* [Axiom of Foundation][bookofproofs$717] - Every non-empty set `$X$` contains an element that is disjoint from `$X.$`
* [Axiom of Infinity][bookofproofs$678] - There exists a set `\(X\)` containing the empty set and also with every element `$z$` the element `$z\cup \{z\}.$`
* [Schema of Replacement Axioms][bookofproofs$715] - If we replace the elements of a set `\(X\)` with elements from another domain, then the resulting object is also a set.
* [Axiom of Choice][bookofproofs$8041] - For every set `$X$` of disjoint and nonempty sets there is a set `$Y$` containing exactly one element from each of these sets. 

We will now explain the contents of each axiom separately and discuss how they improve the consistency of the set theory in comparison to the naive set definition.
