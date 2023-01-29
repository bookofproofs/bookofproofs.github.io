layout: lemma
categories: branches,analysis
nodeid: bookofproofs$8319
orderid: 300
parentid: bookofproofs$382
title: Sum of Roots Of Unity in Complete Residue Systems
description: SUM OF ROOTS OF UNITY IN COMPLETE RESIDUE SYSTEMS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8317
keywords: sum of roots of unity
contributors: bookofproofs

---
A basis for the DFT can be found in the following identity about `$n$`-th [roots of unity][bookofproofs$6752] `$\zeta_k$`, the sequence of which `$(\zeta_k)$` builds for all `$k\in\mathbb Z,$` an [$n$-periodical complex sequence][bookofproofs$8318].
---

For any [positive integer][bookofproofs$1075] `$n > 0,$` the sum of `$n$` consecutive `$n$`-th [roots of unity][bookofproofs$6752] equals `$0.$`

`$$\sum_{k=0}^{n-1}\zeta_k=\sum_{k=0}^{n-1}\exp\left(2\pi i\frac {k}n\right)=0.$$`

This result is only a special case for the [complete residue system][bookofproofs$8174] represented by the numbers `$k=\{0,1,\ldots,n-1\}.$` By introducing a factor `$(a-b)$` for arbitrary [integers][bookofproofs$844] `$a,b\in\mathbb Z,$` we have
`$$\sum_{k=0}^{n-1}\exp\left(2\pi i\frac {(a-b)k}n\right)=\begin{cases}n&\text{ if }a(n)\equiv b(n)\\0&\text{else.}\end{cases}$$`
