layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1124
orderid: 50
parentid: bookofproofs$6627
title: 
description:  Proof of SUM OF GEOMETRIC PROGRESSION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1112
keywords: sum of geometric progression,proof
contributors: bookofproofs

---


---

* Let `\(n\in\mathbb N\)` be a [natural number][bookofproofs$718] and `\(a, x \in F\)` be any two elements of a given [field][bookofproofs$557] `\((F, +, \cdot)\)` with `\(x\neq 1\)`. 
* Set the [sum][bookofproofs$261] `\(S_n\)` geometric progression `\(a, ax, ax^2,\ldots ax^n\)` 
`\[S_n:=\sum_{0\le k\le n} ax^k\]`
* By applying the [general perturbation method][bookofproofs$1121] of the sum `\(S_n\)` in the first step and the [distributive law][bookofproofs$1114] in the second step, we get

`\[S_n+ ax^{n+1}=ax^0 + \sum_{0\le k\le n} ax^{k+1}= a + x\sum_{0\le k\le n} ax^k=a + xS_n.\]`

* By solving for `\(S_n\)` we obtain as required

`\[S_n=\frac{a-ax^{n+1}}{1-x},\quad\quad (x\neq 1).\]`
