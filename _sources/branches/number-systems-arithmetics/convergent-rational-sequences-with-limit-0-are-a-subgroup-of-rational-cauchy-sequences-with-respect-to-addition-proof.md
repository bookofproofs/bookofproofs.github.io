layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1523
orderid: 50
parentid: bookofproofs$1522
title: 
description:  Proof of CONVERGENT RATIONAL SEQUENCES WITH LIMIT \0\ ARE A SUBGROUP OF RATIONAL CAUCHY SEQUENCES WITH RESPECT TO ADDITION &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$696
keywords: addition,are,cauchy,convergent,limit,rational,respect,sequences,subgroup,proof
contributors: bookofproofs

---


---

We want to show that the set `\(I:=\{(a_n)_{n\in\mathbb N}~|~a_n\in\mathbb Q,\lim a_n=0\}\)` of all [rational sequences convergent][bookofproofs$1572] to `\(0\)` is a [subgroup][bookofproofs$554] of the [commutative group of rational Cauchy sequences][bookofproofs$1518] `\((M, + )\)`, formally `\[(I, + )\subseteq (M, + ).\]`

We will do so by applying the first [subgroup criterion][bookofproofs$811]:

`\((1)\)` 
Note that `\(I\)` is not empty, since it contains the [rational sequence consinsting of rational zeros][bookofproofs$1498] `\((0)_{n\in\mathbb N}\)`, because `\(\lim 0=0\)`.

`\((2)\)` 
Moreover, we have already proven that `\(I\)` [is a subset of ][bookofproofs$1516] `\(M\)`, formally `\(I\subseteq M\)`. Therefore, for any rational sequences `\((a_n)_{n\in\mathbb N},(b_n)_{n\in\mathbb N}\)` being elements of `\(I\)` we can conclude [by definition of adding rational Cauchy sequences][bookofproofs$1486], that  
`\[(a_n)_{n\in\mathbb N} + [-(b_n)_{n\in\mathbb N}]=(a_n-b_n)_{n\in\mathbb N}\in M,\]`
which means that the rational sequence `\((a_n-b_n)_{n\in\mathbb N}\)` is en element of `\(M\)`, i.e. it is a rational Cauchy sequence.

`\((3)\)` 
It remains to be shown that `\((a_n-b_n)_{n\in\mathbb N}\)` is an element of `\(I\)`, or `\(\lim a_n-b_n=0\)`. By hypothesis, `\((a_n)_{n\in\mathbb N},(b_n)_{n\in\mathbb N}\in I\)`, which is equivalent to `\(\lim a_n=0\)` and `\(\lim b_n=0\)`. Following the [definition of convergence][bookofproofs$148] in the [metric space][bookofproofs$1090] `\((\mathbb Q,|~|)\)`, for an arbitrarily small `\(\epsilon/2\)`, `\(\epsilon\in\mathbb Q\)` there exist two indices `\(N_a(\epsilon/2), N_b(\epsilon/2), \in\mathbb N\)` such that for all `\(n > \max (N_a(\epsilon/2),N_b(\epsilon/2))\)`,  we have `\[|a_n| < \frac \epsilon2\quad\text{and}\quad|b_n| < \frac \epsilon2.\]`

Using the [triangle inequality of the metric][bookofproofs$1090]  `\(|\cdot|\)`), we can estimate  
`\[|a_n-b_n|\le |a_n|+|b_n| < \frac\epsilon2 + \frac\epsilon2 = \epsilon.\]`
This shows, that `\(\lim a_n-b_n=0\)`, or that `\((a_n-b_n)_{n\in\mathbb N}\in I\)`, or that `\((I, +)\)` is a subgroup of `\((M, + )\)`.
