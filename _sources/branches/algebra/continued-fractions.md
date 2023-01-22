layout: definition
categories: branches,algebra
nodeid: bookofproofs$8188
orderid: 1
parentid: bookofproofs$234
title: Continued Fractions
description: CONTINUED FRACTIONS ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8186,bookofproofs$8189
keywords: continued,continued fraction,finite continued fraction,fractions,infinite continued fraction,continued fractions
contributors: bookofproofs

---
In the following, we will introduce _continued fractions_, which will help us to find a representation of real numbers, which is independent of any basis and with the help of which we will be able to reveal the structure of a given real number.

---

A **continued fraction** is a [ratio][bookofproofs$6634] built from the  [positive integers][bookofproofs$1075] `$q_0, q_1,q_2,\ldots \in\mathbb Z$` of the following form:

`$$[q_0;q_1,q_2,\ldots]:=q_0+\cfrac{1}{q_1+\cfrac{1}{q_2+\cfrac{1}\ddots}}.$$`
 
### Notes

* If the [sequence][bookofproofs$875] `$(q_n)_{n\in\mathbb N}$` is infinite, then `$[q_0;q_1,q_2,\ldots]$` is called an **infinite continued fraction**.[^1]
* A the case of a finite sequence, `$[q_0;q_1,q_2,\ldots,q_n]$` is called a **finite continued fraction**.
* In a continued fraction (both finite or infinite), we sometimes consider the first `$k+1$` elements `$[q_0;q_1,q_2,\ldots,q_k]$` for a `$k\ge 0$` and call them the `$k$`-th **convergent** of the continued fraction. If this is a section of a finite continued fraction, then we require `$0\le k\le n.$`
* See [continued fraction][bookofproofs$8247] Python algorithm for practical calculation of the `$k$`-th section.

[^1]: This is only a formal definition, since the question, whether an infinite continued fraction is [convergent][bookofproofs$141], is not answered yet.
