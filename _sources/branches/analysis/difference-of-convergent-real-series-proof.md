layout: proof
categories: branches,analysis
nodeid: bookofproofs$6646
orderid: 50
parentid: bookofproofs$6645
title: 
description:  Proof of DIFFERENCE OF CONVERGENT REAL SERIES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: convergent,difference,real,series,proof
contributors: bookofproofs

---


---

* Let `$\sum_{k=0}^\infty a_k$` and `$\sum_{k=0}^\infty b_k$` be [convergent real series][bookofproofs$175].
* Let `$c_n:=\sum_{k=0}^n a_k$` and `$d_n:=\sum_{k=0}^n b_k$` be the corresponding [partial sums][bookofproofs$1109].
* The [real sequences][bookofproofs$875] of partial sums `$(c_n)_{n\in\mathbb N}$` and `$(d_n)_{n\in\mathbb N}$` are [convergent real sequences][bookofproofs$141] by hypothesis.
* From the [associativity][bookofproofs$31] and [commutativity][bookofproofs$33] laws for [adding][bookofproofs$1514] [real numbers][bookofproofs$1105] and from the [distributivity law for real numbers][bookofproofs$520] it follows `$$\sum_{k=0}^n (a_k-b_k)=\sum_{k=0}^n (a_k+(-b_k))=\sum_{k=0}^n a_k+\sum_{k=0}^n (-b_k)=\sum_{k=0}^n a_k+(-1)\sum_{k=0}^n b_k=\sum_{k=0}^n a_k-\sum_{k=0}^n b_k=c_n-d_n.$$`
* By the [law for the difference of convergent real sequences][bookofproofs$1133] it follows 
`$$\lim_{n\to\infty}(c_n-d_n)=\lim_{n\to\infty}c_n - \lim_{n\to\infty}d_n.$$`
* By construction, it follows 
`$$\sum_{k=0}^\infty(a_k-b_k)=\sum_{k=0}^\infty a_k - \sum_{k=0}^\infty b_k.$$`
* Therefore, the [real series][bookofproofs$1109] `$\sum_{k=0}^\infty (a_k-b_k)$` is a [convergent real series][bookofproofs$175].