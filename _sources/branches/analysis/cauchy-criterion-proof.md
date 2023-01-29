layout: proof
categories: branches,analysis
nodeid: bookofproofs$1149
orderid: 5000
parentid: bookofproofs$1148
title: 
description: Proof of CAUCHY CRITERION ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: cauchy convergence criterion,cauchy criterion,proof
contributors: bookofproofs

---


---

Let `\(s_j:=\sum_{k=0}^j x_k\)` be the `\(j\)`-th partial sum of the [infinite real series][bookofproofs$1109] `\(\sum_{k=0}^\infty x_k\)` and let `\((s_j)_{j\in\mathbb N}\)` be the real sequence of these partial sums. The proposed condition for the convergence states that for every `\(\epsilon  > 0\)` there is an index `\(N(\epsilon)\in\mathbb N\)` such that

`\[\left|\sum_{k=m}^n x_k\right| < \epsilon\quad\quad \text{for all}\quad n\ge m\ge N(\epsilon).\]`

Since

`\[s_n-s_{m-1}=\sum_{k=m}^n x_k,\]`

we get

`\[\left|s_n-s_{m-1}\right| < \epsilon\quad\quad \text{for all}\quad n\ge m\ge N(\epsilon).\]`

This means that the [real sequence][bookofproofs$875] `\((s_j)_{j\in\mathbb N}\)` is a  [real Cauchy sequence][bookofproofs$1704]. According to the [completeness principle][bookofproofs$1108] every real Cauchy sequence is convergent. If follows that `\(\sum_{k=0}^\infty x_k\)`  is a [convergent real series][bookofproofs$175].