layout: axiom
categories: branches,set-theory
nodeid: bookofproofs$716
orderid: 600
parentid: bookofproofs$1427
title: Axiom of Power Set
description: AXIOM OF POWER SET ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$983
keywords: axiom of power set,power set axiom,power set postulate,postulate of power set
contributors: bookofproofs

---
The axioms we have introduced so far do not ensure the existence of a [power set][bookofproofs$6831] for a set `$X$`, containing all the subsets of `$X$` as its elements. For instance, the [axiom of separation][bookofproofs$675] ensures the existence of _any_ subset of `$X$` separately, and we could use the [axiom of pairing][bookofproofs$667] to create a set containing _any two_ of such subsets as elements, but it is not possible to combine all subsets of a given set _at once_. For this reason, we need another axiom, the axiom of power set.

---

For each set `\(X\)` there exists a set containing all subsets of `$X$`, formally:

`$$\forall X~\exists~Y~\forall z~(z\in Y\Rightarrow z\subseteq X).$$`


![axiompowerset](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiompowerset.png?raw=true)

