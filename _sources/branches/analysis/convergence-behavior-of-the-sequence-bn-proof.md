layout: proof
categories: branches,analysis
nodeid: bookofproofs$1352
orderid: 50
parentid: bookofproofs$1347
title: 
description:  Proof of CONVERGENCE BEHAVIOR OF THE SEQUENCE \B^N\ &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: convergence behavior of sequence of powers,proof
contributors: bookofproofs

---


---

There are four cases, how the [real number][bookofproofs$1105] `\(b\)` can influence the convergence of the [real sequence][bookofproofs$875] `\((b^n)_{n\in\mathbb N}\)`:

### Case `\((1)\)`: `\(|b| < 1\)` 

In this case, the sequence `\((b^n)_{n\in\mathbb N}\)` is [convergent][bookofproofs$141]. This follows immediately from the [corollary to the Archimedean Axiom about the existence of arbitrarilly small powers][bookofproofs$1350].
### Case `\((2)\)`. `\(b = 1\)` 

In this cases, it follows trivially that `\(\lim_{n\to\infty} b^n=1\)`.

### Case `\((3)\)`: `\(b = - 1\)`

Because the set `\((\mathbb R, + ,\cdot)\)` of [real numbers is a field][bookofproofs$1105], the set `\((\mathbb R\setminus\{0\},\cdot)\)` is an [Abelian group][bookofproofs$553]. Therefore, it follows from the [definition of the exponentiation for Abelian groups][bookofproofs$673] that

`\[b^n :=
\begin{cases}
1  & \text{ if } n=0 \\
b\cdot b^{n-1} & \text{ if } n > 0
\end{cases}\]`


It [can be proven][bookofproofs$522] that `\(-(-b)=b\)` for all `\(b\in\mathbb R\)`. Therefore, also `\(-(-1)=(-1)(-1)=(-1)^2=1\)`. It follows that the real sequence `\((-1)^n_{n\in\mathbb N}\)` is alternating between the values `\(1\)` and `\(-1\)`. It is simply the sequence `\((1,-1,1,-1,1,-1,\ldots)\)`. Since this sequence neither converges to the number `\(1\)`, nor it does converge to the number `\(-1\)`, it is [divergent, by definition][bookofproofs$1332].
### Case `\((4)\)`: `\(|b| > 1\)`

In this case, the sequence `\((b^n)_{n\in\mathbb N}\)` [tends to infinity][bookofproofs$1345]. This follows immediately from the [corollary to the Archimedean Axiom about the existence of powers exceeding positive real numbers][bookofproofs$1340].