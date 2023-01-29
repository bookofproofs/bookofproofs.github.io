layout: definition
categories: branches,set-theory
nodeid: bookofproofs$720
orderid: 300
parentid: bookofproofs$112
title: Transitive Set
description: TRANSITIVE SET &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$656
keywords: set,transitive,transitive set
contributors: bookofproofs

---
A fundamental concept in the theory of ordinal numbers is a _transitive set_, which we want now to introduce formally:

---

A **transitive** [set][bookofproofs$550] `\(Z\)` is one in which the following implication is always fulfilled:

`$$x\in y\wedge y\in Z\Longrightarrow x\in Z,$$` 

i.e. if `$x$` is element of `$y$` and `$y$` is element of `$Z$`, then `$x$` is also an element of `$Z.$` This is equivalent to the following: If `$y\in X$`, then `$y\subseteq X$` (i.e. every element `$y$` of `$Z$` is also its [subset][bookofproofs$552]).

Because of the [axiom of foundation][bookofproofs$717], by which no set can contain itself, we can even require that `$y$` is a [proper subset][bookofproofs$552] of `$Z,$` and the definition of a transitive set can then be written as follows:
`$$y\in Z\Longrightarrow y\subset Z.$$`
