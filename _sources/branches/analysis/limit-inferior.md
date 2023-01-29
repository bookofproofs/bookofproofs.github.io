layout: definition
categories: branches,analysis
nodeid: bookofproofs$6674
orderid: 1700
parentid: bookofproofs$126
title: Limit Inferior
description: LIMIT INFERIOR ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: limit inferior,inferior
contributors: bookofproofs

---
> applicability: `$\mathbb {R}$`

---

Let `$(a_n)_{n\in\mathbb N}$` be a [real sequence][bookofproofs$875]. The **limit inferior** `$\varliminf a_n$` is the element of the [extended real numbers][bookofproofs$6668] `$\overline{\mathbb R}$` reached for `$n\to\infty$` by the [increasing sequence][bookofproofs$6672] `$(\inf D_n)_{n\in\mathbb N}$`, where `$\inf  D_n$` denotes the [infimum of extended real numbers][bookofproofs$6670] for the set `$D_n:=\{a_k:~k\ge n\},$` formally  

`$$\varliminf_{n\to\infty} a_n:=\lim_{n\to\infty}(\inf D_n).$$`

### Motivation

This definition is motivated by the following facts:
* The [sequence `$\inf D_n$` is monotonically increasing][bookofproofs$6672].
* This sequence is [bounded above][bookofproofs$1136] by definition.
* [Every bounded monotonic sequence is convergent][bookofproofs$197].
* Therefore, a limit `$\lim_{n\to\infty}(\inf D_n)$` must definitely exist, if the sequence `$(a_n)_{n\in\mathbb N}$` is [bounded][bookofproofs$1136]. 
* If the sequence is unbounded, it exists indefinitely by setting `$$\varliminf_{n\to\infty} a_n=-\infty.$$`
