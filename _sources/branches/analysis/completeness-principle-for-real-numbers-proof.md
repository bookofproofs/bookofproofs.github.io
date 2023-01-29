layout: proof
categories: branches,analysis
nodeid: bookofproofs$1128
orderid: 50
parentid: bookofproofs$1108
title: 
description:  Proof of ALL CAUCHY SEQUENCES CONVERGE IN THE SET OF REAL NUMBERS COMPLETENESS PRINCIPLE &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$696
keywords: completeness,completeness principle,completeness principle of real numbers,proof
contributors: bookofproofs

---


---

By assumption, `\((x_n)_{n\in\mathbb N}\)` is a [real Cauchy sequence][bookofproofs$1704], i.e. a Cauchy sequence in the [metric space][bookofproofs$618] `\((\mathbb R,|~|)\)`. We have to show that it [converges against a limit][bookofproofs$141] `\(a\in\mathbb R\)`. 

By definition of real Cauchy sequences, for every `\(\epsilon\in\mathbb R\)`, `\(\epsilon > 0\)` there is a `\(N(\epsilon)\in\mathbb N\)` such that for all `\(m,n > N(\epsilon)\)` we have the estimation 

`\[|x_m - x_n| < \epsilon\quad\quad ( * )\]`

First, we observe that by the [definition of real numbers][bookofproofs$1105], each `\(n\)`-th sequence member `\(x_n\)` can be represented by the residue class 

`\[x_n=(c_{k}^{(n)})_{k\in\mathbb N} + I,\]`

i.e. of the class of all rational Cauchy sequences, the difference of which converges to `\(0\)`. Correspondingly, also the real number `\(\epsilon  > 0\)` can be represented as its residue class:

`\[\epsilon=(\epsilon_k)_{k\in\mathbb N} + I.\]`

Moreover, we can assume without loss of generality that `\(\epsilon\)` is an arbitrarily small (but fixed) rational number. In this case, we can set 

`\[\epsilon=(\epsilon)_{k\in\mathbb N} + I.\]`

In fact, the magnitude of `\(\epsilon\)` does not depend on the index `\(k\)`. 

Second, we observe that by the [definition of the order relation for real numbers][bookofproofs$1107] the estimation `\( ( * ) \)` means that

`\[|x_m - x_n| < \epsilon \Longleftrightarrow \exists q\in\mathbb Q, q > 0, N(q)\in\mathbb N: \epsilon - |c_{k}^{(m)}-c_{k}^{(n)}| > q\quad\quad\forall k\in\mathbb N, k > N(q).
\]`
In particular, for all pairs of natural numbers `\(n,m > N(\epsilon)\)` there exists an index `\(N(q)\)`, such that `\(|c_{k}^{(m)}-c_{k}^{(n)}| < \epsilon\)` for all `\(k > N(q)\)`. Because `\(N(q)\)` depends only on the pair `\(m,n\)` and this pair only depends on `\(\epsilon\)`, we can set `\(N(q):=N(n,m)=M(\epsilon)\)` and conclude that for all `\(k > M(\epsilon)\)`, we have `\(|c_{k}^{(m)}-c_{k}^{(n)}| < \epsilon\)`.

This means that the rational Cauchy sequence[^1] `\(( c_{k}^{(m)}-c_{k}^{(n)})_{k\in\mathbb N}\)` converges to `\(0\)`, or that `\(( c_{k}^{(m)}-c_{k}^{(n)})_{k\in\mathbb N}\in I\)`. But this means that both rational Cauchy sequences `\(( c_{k}^{(m)})_{k\in\mathbb N}\)` and `\((c_{k}^{(n)})_{k\in\mathbb N}\)` are the representatives of __the same__ residue class, or real number `\(a\in\mathbb R\)` with

`\[a=( c_{k}^{(m)})_{k\in\mathbb N} + I=(c_{k}^{(n)})_{k\in\mathbb N} + I.\]`

Therefore, we get together with the triangle inequality

`\[|c^{(m)}_k - a + a - c^{(n)}_k | \le  |c^{(m)}_k - a| + |a - c^{(n)}_k | < 2\cdot\epsilon,\quad\quad \forall k > M(\epsilon),\]`

or that 

`\[| x_n - a | < 2\cdot\epsilon,\quad\quad \forall n >\max(M(\epsilon),N(\epsilon)).\]`

Since `\(\epsilon\)` is arbitrarily small, it completes the proof that the real Cauchy sequence `\((x_n)_{n\in\mathbb N}\)` is convergent in `\(\mathbb R\)`.

[^1]: Please note that the difference of two Cauchy sequences is also a Cauchy sequence.
