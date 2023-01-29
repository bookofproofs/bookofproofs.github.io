layout: definition
categories: branches,analysis
nodeid: bookofproofs$6673
orderid: 1500
parentid: bookofproofs$126
title: Limit Superior
description: LIMIT SUPERIOR ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: limit superior,superior
contributors: bookofproofs

---


---

Let `$(a_n)_{n\in\mathbb N}$` be a [real sequence][bookofproofs$875]. The **limit superior** `$\varlimsup a_n$` is the element of the [extended real numbers][bookofproofs$6668] `$\overline{\mathbb R}$` reached for `$n\to\infty$` by the [decreasing sequence][bookofproofs$6671] `$(\sup D_n)_{n\in\mathbb N}$`, where `$\sup D_n$` denotes the [supremum of extended real numbers][bookofproofs$6669] for the set `$D_n:=\{a_k:~k\ge n\},$` formally  

`$$\varlimsup_{n\to\infty} a_n:=\lim_{n\to\infty}(\sup D_n).$$`

### Motivation

This definition is motivated by the following facts:
* The [sequence `$\sup D_n$` is monotonically decreasing][bookofproofs$6671].
* This sequence is [bounded below][bookofproofs$1136] by definition.
* [Every bounded monotonic sequence is convergent][bookofproofs$197].
* Therefore, a limit `$\lim_{n\to\infty}(\sup D_n)$` must definitely exist, if the sequence `$(a_n)_{n\in\mathbb N}$` is [bounded][bookofproofs$1136]. 
* If the sequence is unbounded, it exists indefinitely by setting `$$\varlimsup_{n\to\infty} a_n=+\infty.$$`
