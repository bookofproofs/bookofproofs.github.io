layout: definition
categories: branches,set-theory
nodeid: bookofproofs$8306
orderid: 800
parentid: bookofproofs$65
title: Generalized Union of Sets
description: GENERALIZED UNION OF SETS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8297
keywords: union of sets
contributors: bookofproofs

---
The [set union][bookofproofs$6827] is defined for only two sets. Sometimes, it is convenient to have a more general definition involving an arbitrary number of sets.

---

Let `$X_i\text{ , }i\in I$` be a [family of sets][bookofproofs$6198] over the [index set][bookofproofs$6198] `$I$`. A **union of sets** of `$X_i\text{ , }i\in I$` is denoted and defined by `$$\bigcup_{i\in I}X_i:=\{x\in X\mid \exists i\in I\text{, }x\in X_i\}.$$`

### Notes

* The union of sets is a generalized case of the [set union][bookofproofs$6827] `$A\cup B,$` since if `$U$` is a [universal set][bookofproofs$7984] of `$A$` and `$B,$` then the index set consists only of two elements, e.g. `$I=\{1,2\},$` `$A=U_1$`, `$B=U_2$` and `$$A\cup B=\{x\in U\mid \exists i\in \{1,2\}\text{, }x\in U_i\}=\{x\in U\mid x\in A\vee x\in B\}.$$`
* The only thing which is required for the index set `$I$` of an index family is that it is [non-empty][bookofproofs$550]. It can be _any_ set, in particular, it does not have to consist of the commonly used positive integers. You can have any kind of indices, even indices which are uncountable[^1].

[^1]: The concept of countable/uncountable will be introduced, when we will be studying cardinal numbers.
