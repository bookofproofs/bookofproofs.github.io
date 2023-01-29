layout: proof
categories: branches,analysis
nodeid: bookofproofs$1154
orderid: 50
parentid: bookofproofs$1152
title: By Induction
description:  Proof of EVERY BOUNDED REAL SEQUENCE HAS A CONVERGENT SUBSEQUENCE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: bolzano-weierstrass,bounded sequence,convergent subsequence,proof
contributors: bookofproofs

---


---

Since the real sequence `\((a_n)_{n\in\mathbb N}\)` is [bounded][bookofproofs$1136], there are real numbers `\(A,B\in\mathbb R\)` with

`\[A\le a_n \le B\quad\quad\forall n\in\mathbb N.\]`

We will prove the theorem in three steps:

#### Step `\(1\)` - We construct intervals `\([A_k,B_k]\)` fulfilling certain properties

We will prove [by induction][bookofproofs$657] that there exists a sequence `\((I_k)_{k\in\mathbb N}\)` of [closed real intervals][bookofproofs$1153] `\(I_k:=[A_k,B_k]\)` with the following properties:

1. `\([A_k,B_k]\)` contains infinitely many sequence members of the sequence `\((a_n)_{n\in\mathbb N}\)`, i.e. `\(a_n\in I_k\)` for infinitely many `\(n\in\mathbb N\)`.
1. `\([A_k,B_k]\subseteq [A_{k-1},B_{k-1}]\)`.
1. `\(B_k - A_k = 2^{-k}(B-A)\)`.

### Base case `\(k=0\)`

For `\([A_0,B_0]:=[A,B]\)` the properties are obviously fulfilled.

### Induction step `\(k\rightarrow k + 1\)`.

Let `\([A_k,B_k]\)` be an interval, for which the properties are fulfilled. Set `\(M:=(A_k + B_k)/2\)`. `\(M\)` is the "middle" of the interval  `\([A_k,B_k]\)`. Since `\([A_k,B_k]\)` contains infinitely many members of the sequence `\((a_n)_{n\in\mathbb N}\)`, at least one of the intervals `\([A_k,M]\)` and `\([M, B_k]\)` must also contain infinitely many members of this sequence. We set

`\[[A_{k+1},B_{k+1}]:=\cases{[A_k,M],\quad\text{ if }[A_k,M]\text{ contains infinitely many sequence members of }(a_n)_{n\in\mathbb N},\\
[M, B_k],\quad\text{ else.}
}\]`

By construction, `\([A_{k+1},B_{k+1}]\)` fulfills the properties mentioned above.

#### Step `\(2\)` - We construct a subsequence `\((a_{n_k})_{k\in\mathbb N}\)` with `\(a_{n_k}\in[A_k,B_k]\)` for all `\(k\in\mathbb N\)`

Now, again by induction, we define the members of the [subsequence][bookofproofs$6610] `\((a_{n_k})_{k\in\mathbb N}\)` with `\(a_{n_k}\in[A_k,B_k]\)` for all `\(k\in\mathbb N\)` as follows:


### Base case `\(k=0\)`

We set `\(a_{n_0}:=a_0\)`.

### Induction step `\(k\rightarrow k + 1\)`.

Let the sequence members `\(a_{n_0}, a_{n_1},\ldots,a_{n_k}\)` be already defined. Because the interval `\([A_{k+1},B_{k+1}]\)` contains infinitely many sequence members, there exists an `\(a_{n_{k+1}}\in[A_{k+1},B_{k+1}]\)` with `\(n_{k+1} > n_k\)`. Thus we can include `\(a_{n_{k+1}}\)` to the sequence `\(a_{n_0}, a_{n_1},\ldots,a_{n_k},a_{n_{k+1}}\)`.

#### Step `\(3\)` - We prove that the subsequence `\((a_{n_k})_{k\in\mathbb N}\)` is convergent.

Let `\(\epsilon > 0\)` be an arbitrarily small (but fixed) real number. Since the length of the `\(k\)`-th interval is `\(B_k - A_k=2^{-k}(B-A)\)`, there is an `\(N(\epsilon)\in\mathbb N\)`, for which the length the `\(N(\epsilon)\)`-th interval is 

`\[B_{N(\epsilon)} - A_{N(\epsilon)}=2^{-{N(\epsilon)}}(B-A) < \epsilon.\]`

By construction of the intervals, for all `\(k,j > N(\epsilon)\)` will have 
`\[\begin{array}{rcl}
a_{n_k}\in[A_{n_k},B_{n_k}]\subseteq [A_{N(\epsilon)},B_{N(\epsilon)}],\\
a_{n_j}\in[A_{n_j},B_{n_j}]\subseteq [A_{N(\epsilon)},B_{N(\epsilon)}].
\end{array}
\]`
Thus, for all `\(k,j > N(\epsilon)\)` we have
`\[|a_{n_k} - a_{n_j}| \le B_{N(\epsilon)} - A_{N(\epsilon)}=2^{-{N(\epsilon)}}(B-A) < \epsilon,\]`
which means that the subsequence `\((a_{n_k})_{k\in\mathbb N}\)` is a [Cauchy sequence][bookofproofs$1072]. By the [completeness principle][bookofproofs$1108], it is [convergent][bookofproofs$141] in `\(\mathbb R\)`.

Therefore, the limit of this convergent sequence is an [accumulation point][bookofproofs$174] of the sequence.
