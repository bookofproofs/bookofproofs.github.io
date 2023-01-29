layout: proof
categories: branches,analysis
nodeid: bookofproofs$6599
orderid: 50
parentid: bookofproofs$6598
title: 
description:  Proof of COMPACT SUBSET OF REAL NUMBERS CONTAINS ITS MAXIMUM AND ITS MINIMUM &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$582
keywords: compact,contains,its,maximum,minimum,numbers,real,subset,proof
contributors: bookofproofs

---


---

* Let `$A$` be a non-empty [compact][bookofproofs$6575] [subset][bookofproofs$552] of the [real numbers][bookofproofs$1105] `$\mathbb R$`.
* We have to show that `$\max(A)\in A$` and `$\min(A)\in A$`.
   * According to the [Heine-Borel theorem][bookofproofs$6596], `\(A\)` is [bounded][bookofproofs$6574] and [closed][bookofproofs$852].
   * Because `$A$` is a non-empty bounded subset of real numbers, it has an [upper bound][bookofproofs$584] and a [lower bound][bookofproofs$584].
   * Because [real numbers have the supremum and the infimum property][bookofproofs$1756], every non-empty subset, which has a upper and an lower bound, has also a [supremum][bookofproofs$1754] and an [infimum][bookofproofs$1755].
   * Thus, also `$A$` has a supremum and an infimum.
   * Therefore there exist [convergent][bookofproofs$141] [real sequences][bookofproofs$875] `$(x_k)_{k\in\mathbb N}$` and `$(y_k)_{k\in\mathbb N}$` with `\(x_k\in A\)` and `$y_k\in A$` for all `$k\in\mathbb N$` and `\(\lim x_k=\sup(A)\)`, `$\lim y_k=\inf(A)$`.
   * In any metric space, a closed set (like `$A$` is) [can be characterized by the limit of its sequences][bookofproofs$6585] as follows: if there is a [convergent sequence][bookofproofs$148] of points `$(x_k)_{k\in\mathbb N}$` contained in `$A$`, `$A$` will also contain its limit.
   * [Real numbers are a metric space][bookofproofs$618].
   * It follows that `$\sup(A)\in A$` and `$\inf(A)\in A$`.
   * By definition of [maximum][bookofproofs$6602] and [minimum][bookofproofs$6603], it follows that `$\max(A)\in A$` and `$\min(A)\in A$`.
