layout: definition
categories: branches,topology
nodeid: bookofproofs$148
orderid: 700
parentid: bookofproofs$69
title: Convergent Sequences and Limits
description: CONVERGENT SEQUENCES AND LIMITS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$582
keywords: convergent,sequences
contributors: bookofproofs

---


---

Let `\((X,d)\)` be a [metric space][bookofproofs$617]. The [sequence][bookofproofs$874]  `\((a_n)_{n\in\mathbb N}\)` with points `$a_n\in X$`  is called **convergent** to the point `\(a\in X\)`, if and only if for each [neighborhood][bookofproofs$849] `\(B(a,\epsilon)\)` there exists an `\(N\in\mathbb N\)` with `$a_n\in B(a,\epsilon)$` for all `$n\ge N$`. 

Alternative formulation: The sequence `\((a_n)_{n\in\mathbb N}\)` is **convergent** to `\(a\in X\)`, if and only if all but finitely many sequence members `$a_n$` lie in the [neighborhood][bookofproofs$849] `\(B(a,\epsilon)\)`, no matter how small `\(\epsilon > 0\)` is.


The point `\(a\in X\)` is called the **limit** of the sequence `\((a_n)\)` and is denoted by `$$\lim_{n\rightarrow\infty} a_n=a.$$`

Note that if `\((X,d)\)` is a [normed vector space][bookofproofs$847] `\((X,d)=(X,\|\|)\)` , this definition is equivalent to the following definition: For each `\(\epsilon > 0\)` there exists an `\(N\in\mathbb N\)` with `$\| a_n-a \| < \epsilon$` for all `$n\ge N.$`
