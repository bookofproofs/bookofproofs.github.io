layout: proof
categories: branches,analysis
nodeid: bookofproofs$1726
orderid: 50
parentid: bookofproofs$308
title: 
description:  Proof of A GENERAL CRITERION FOR THE CONVERGENCE OF INFINITE COMPLEX SERIES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: complex,convergence,criterion,general,infinite,series,proof
contributors: bookofproofs

---


---

Let `\(s_j:=\sum_{k=0}^j x_k\)` be the `\(j\)`-th partial sum of the [infinite complex series][bookofproofs$1724] `\(\sum_{k=0}^\infty x_k\)` and let `\((s_j)_{j\in\mathbb N}\)` be the [complex sequence][bookofproofs$1249] of these partial sums. The proposed condition for the convergence states that for every `\(\epsilon  > 0\)` there is an index `\(N(\epsilon)\in\mathbb N\)` such that

`\[\left|\sum_{k=m}^n x_k\right| < \epsilon\quad\quad \text{for all}\quad n\ge m\ge N(\epsilon).\]`

Since

`\[s_n-s_{m-1}=\sum_{k=m}^n x_k,\]`

we get

`\[\left|s_n-s_{m-1}\right| < \epsilon\quad\quad \text{for all}\quad n\ge m\ge N(\epsilon).\]`

This means that the [complex sequence][bookofproofs$1249] `\((s_j)_{j\in\mathbb N}\)` is a  [complex Cauchy sequence][bookofproofs$1250]. According to the [completeness principle for complex numbers][bookofproofs$1709], every complex Cauchy sequence is convergent. If follows that `\(\sum_{k=0}^\infty x_k\)`  is a [convergent complex series][bookofproofs$147].