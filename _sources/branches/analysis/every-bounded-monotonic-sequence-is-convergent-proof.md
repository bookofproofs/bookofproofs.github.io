layout: proof
categories: branches,analysis
nodeid: bookofproofs$1157
orderid: 50
parentid: bookofproofs$197
title: 
description: Proof of EVERY BOUNDED MONOTONIC SEQUENCE IS CONVERGENT ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: bounded sequence,monotonic sequence,every bounded monotone sequence is convergent,every bounded monotonic sequence is convergent,monotonic and bounded sequence,monotonic and bounded sequences,bounded and monotone sequence,bounded and monotone sequences,every monotonic bounded sequence is convergent,proof
contributors: bookofproofs

---


---

* Assume, the [real sequence][bookofproofs$875]  `$\((a_n)_{n\in\mathbb N}\)` is [monotonic][bookofproofs$1155] and [bounded][bookofproofs$1136].
* According to the [theorem of Bolzano-Weierstrass][bookofproofs$1152], it has a [convergent][bookofproofs$141] [subsequence][bookofproofs$1151] `\((a_{n_k})_{k\in\mathbb N}\)` with`\[\lim_{n\rightarrow\infty} a_{n_k}=a.\]`
* According to the [definition of convergence][bookofproofs$141], this means that for every `\(\epsilon > 0\)` there is an index `\(K(\epsilon)\in\mathbb N\)` with `\[|a_{n_k} - a| < \epsilon\quad\quad\forall k \ge K(\epsilon).\]`
* Set `\(N(\epsilon):=n_{K(\epsilon)}\)`. For every `\(n > N(\epsilon)\)` there is a `\(k\ge K(\epsilon)\)` with 
`\[ n_k\le n < n_{k+1}\quad\quad( * ).\]`
* Since `\((a_n)_{n\in\mathbb N}\)` is [monotonically increasing][bookofproofs$1155] (or [monotonically decreasing][bookofproofs$1155]), it follows from `\( ( * ) \)` that `\[ a_{n_k}\le a_n \le a_{n_{k+1}}\quad\quad\text{or}\quad\quad a_{n_k}\ge a_n \ge a_{n_{k+1}}.\]`
* In either case we have for all `\(n > N(\epsilon)\)`:
`\[|a_n - a|\le\max(|a_{n_k} - a|,|a_{n_{k+1}} - a|) < \epsilon.\]` 
* This shows that `\((a_n)_{n\in\mathbb N}\)` is convergent.
