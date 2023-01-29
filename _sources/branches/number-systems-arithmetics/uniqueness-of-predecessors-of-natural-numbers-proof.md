layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1543
orderid: 50
parentid: bookofproofs$1542
title: 
description:  Proof of UNIQUENESS OF PREDECESSORS OF NATURAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1538
keywords: natural,numbers,predecessors,uniqueness,proof
contributors: bookofproofs

---


---

Let `\(M\)` be a [subset][bookofproofs$552] of all [natural numbers][bookofproofs$718], which contains the number `\(0\)` and all `\(x\neq 0\)`, which have at least one predecessor `\(u\)`, i.e. for which the equation `\(x=u^+\)` holds.

We first show that `\(M\)` really contains not just the number `\(0\)`, but more elements. This is the case, since `\(0\in M\)` and, by Peano axioms **P1** and **P2** and construction of `\(M\)`, we have also `\(0^+\in M\)`.

Note that, again according to the Peano axiom **P2**, for each `\(x\in M\)` with `\(x\neq 0\)` there exists a natural number `\(x^+\)` with `\(x^+=(u^+)^+\)`, which is the unique [successor][bookofproofs$504] of every `\(x\in M\)`. By construction of `\(M\)`, we have `\(x^+\in M\)`. Since `\(0\in M\)`, we can apply the principle of induction **P5**, and conclude that `\(M\)` is not only a subset of natural numbers, but `\(M\)` contains all natural numbers `\(\mathbb N\)`, in particular, it contains `\(u\in M\)`. 

We have just shown that every `\(x\neq 0\)`, `\(x\in M\)` has at least one predecessor `\(u\in M\)`. By Peano axiom **P4** it follows, that there is only one such predecessor, thus `\(u\)` is unique.
