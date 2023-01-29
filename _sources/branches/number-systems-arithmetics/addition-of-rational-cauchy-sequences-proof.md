layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1487
orderid: 50
parentid: bookofproofs$1486
title: 
description:  Proof of ADDITION OF RATIONAL CAUCHY SEQUENCES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: addition,rational cauchy sequences,cauchy,rational,sequences,addition of rational cauchy sequences,proof
contributors: bookofproofs

---


---

Let `\((x_n)_{n\in\mathbb N}\)` and `\((y_n)_{n\in\mathbb N}\)` be [rational Cauchy sequences][bookofproofs$1485]. By definition, it means that, for any arbitrarily small rational number `\(\epsilon > 0\)`, there exist two natural numbers `\(N_x(\epsilon/2)\)` and `\(N_y(\epsilon/2)\)` such that for all `\(n,m\in\mathbb N\)` with `\(n, m > \max(N_x(\epsilon/2),N_y(\epsilon/2))\)` we have
`\[|x_n  - x_m| < \frac\epsilon2 \quad\text{and}\quad |y_n  - y_m| < \frac\epsilon2. \]`

Note that, since `\(x_n\)` and `\(y_n\)` are rational numbers for all `\(n\in\mathbb N\)`, it follows from the definition of [addition of rational numbers][bookofproofs$1446] that `\((x_n - x_m)\)`, `\((y_n - y_m)\)`, `\((x_n + y_n)\)` are also rational numbers. Therefore, the sequence `\((x_n+y_n)_{n\in\mathbb N}\)` is a sequence of rational numbers. Using the [triangle inequality for the absolute value of rational numbers][bookofproofs$1090], we estimate 
`\[|(x_n + y_n) - (x_m + y_m)| \le |x_n  - x_m|+|y_n  - y_m|  < \frac\epsilon2 + \frac\epsilon2=\epsilon.~~~~~~~~~~~~( * )\]`
From `\( ( * ) \)` it follows that the rational sequence `\((x_n + y_n)_{n\in\mathbb N}\)` is a rational Cauchy sequence.
