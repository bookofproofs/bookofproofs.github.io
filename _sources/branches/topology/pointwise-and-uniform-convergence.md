layout: definition
categories: branches,topology
nodeid: bookofproofs$173
orderid: 50
parentid: bookofproofs$1205
title: Pointwise and Uniform Convergence
description: POINTWISE AND UNIFORM CONVERGENCE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$582
keywords: convergence,pointwise,uniform,pointwise and uniform convergence
contributors: bookofproofs

---


---

Let `\((X,d)\)` and `\((Y,d)\)` be [metric spaces][bookofproofs$617], let `\(f:X\to Y\)` be a [function][bookofproofs$592] and let `\(f_n:X\to Y\)`, `\(n\in\mathbb N\)` be a [sequence][bookofproofs$874] of functions. 

* The sequence `\((f_n)_{n\in\mathbb N}\)`  **converges pointwise** to `\(f\)`, if for each `\(x\in X\)` and each `\(\epsilon > 0\)` there exists an `\(N(x,\epsilon)\in\mathbb N\)`, such that
`\[d(f_n(x),f(x)) < \epsilon \text{ for all } n\ge N(x,\epsilon),\]`
i.e. if the sequence `\((f_n(x))_{n\in\mathbb N}\)` is [convergent][bookofproofs$148] to `\(f(x)\)` for each `\(x\in X\)`. 

* The sequence `\((f_n)_{n\in\mathbb N}\)`  **converges uniformly** to `\(f\)`, if for each `\(\epsilon > 0\)` there exists an `\(N(\epsilon)\in\mathbb N\)`, such that
`\[d(f_n(x),f(x)) < \epsilon \text{ for all } x\in X\text{ and all } n\ge N(\epsilon),\]`
i.e. if the sequence `\((f_n(x))_{n\in\mathbb N}\)` is [convergent][bookofproofs$148] to `\(f(x)\)` for each `\(x\in X\)` in such a way that the distance from `\(f_n(x)\)` to `\(f(x)\)` for sufficient big index `\(n\)` does not exceed the threshold value `\(\epsilon\)` for all `\(x\in X\)`. 

Please note that the difference between pointwise and uniform convergence is that in the first case the index `\(N\)` depends on both, `\(x\)` and `\(\epsilon\)`, while in the latter case it only depends on `\(\epsilon\)`.
