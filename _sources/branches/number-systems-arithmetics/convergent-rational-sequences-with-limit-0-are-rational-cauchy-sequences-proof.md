layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1517
orderid: 50
parentid: bookofproofs$1516
title: 
description:  Proof of CONVERGENT RATIONAL SEQUENCES WITH LIMIT \0\ ARE RATIONAL CAUCHY SEQUENCES &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$696
keywords: are,cauchy,convergent,limit,rational,sequences,proof
contributors: bookofproofs

---


---

Let `\((M , + , \cdot)\)` be the [unit ring of all rational Cauchy sequences][bookofproofs$1101]. We want to show that the set `\(I:=\{(a_n)_{n\in\mathbb N}~|~a_n\in\mathbb Q,\lim a_n=0\}\)`, i.e. the set of all [rational sequences convergent][bookofproofs$1572] to `\(0\)` is a [subset][bookofproofs$552] of `\(M\)`, formally `\(I\subseteq R\)`. We will demonstrate that any rational sequence `\((a_n)_{n\in\mathbb N}\)` with `\(\lim a_n=0\)` is also a rational Cauchy sequence, formally `\[(a_n)_{n\in\mathbb N}\in I\Longrightarrow (a_n)_{n\in\mathbb N}\in M.\]`


Following the [definition of convergence][bookofproofs$148] in the [metric space][bookofproofs$1090] `\((\mathbb Q,|~|)\)`, for any arbitrarily small `\(\epsilon/2\)`, `\(\epsilon\in\mathbb Q\)`, there exists an `\(N(\epsilon/2)\in\mathbb N\)` such that for all `\(n , m > N(\epsilon/2)\)`,  we have `\[|a_n| < \frac \epsilon2\quad\text{and}\quad|a_m| < \frac \epsilon2.\]`
Thus, we can estimate (using the triangle inequality, see [third property of the metric][bookofproofs$1090]  `\(|\cdot|\)`),   
`\[|a_n-a_m|\le |a_n|+|a_m| < \frac\epsilon2 + \frac\epsilon2 = \epsilon.\]`
This demonstrates, that `\((a_n)_{n\in\mathbb N}\)` with `\(\lim a_n=0\)` is also a rational Cauchy sequence, or that `\(I\subseteq M\)`, as required.
