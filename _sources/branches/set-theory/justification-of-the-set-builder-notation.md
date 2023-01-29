layout: corollary
categories: branches,set-theory
nodeid: bookofproofs$8017
orderid: 50
parentid: bookofproofs$675
title: Justification of the Set-Builder Notation
description: JUSTIFICATION OF THE SET-BUILDER NOTATION ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$983
keywords: builder,justification,notation,set,set builder notation
contributors: bookofproofs

---
Please recall the different [basic possibilities to describe sets][bookofproofs$587], in which the set-builder notation used the curly brackets, inside which we describe the definite properties of the set elements. The following corollary to the [axiom of separation][bookofproofs$675] allows justification of this notation.

---

Let `$p(z,X_1,\ldots,X_n)$` be an [atomic formula in predicate logic][bookofproofs$6226], in which the `$z$` is a [free variable][bookofproofs$6221] and in which `$x_1,\ldots,x_n, X$` are sets. Let `$Y$` be given, which fulfills the property of the [axiom of separation][bookofproofs$675], i.e. `$$\forall x_1,\ldots,x_n \forall X~\exists Y~\forall z~(z\in Y \Leftrightarrow z\in X\wedge p(z,x_1,\ldots,x_n)).$$`
Then `$Y$` is unique. Therefore, we can therefore use the formula to define the set `$Y,$`, justifying the [set-builder notation][bookofproofs$587] `$$Y:=\{z\in X\mid p(z,x_1,\ldots,x_n)\}.$$`
