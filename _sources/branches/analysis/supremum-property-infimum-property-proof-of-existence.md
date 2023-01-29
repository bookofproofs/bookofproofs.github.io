layout: proof
categories: branches,analysis
nodeid: bookofproofs$1757
orderid: 50
parentid: bookofproofs$1756
title: 
description:  OF EXISTENCE Proof of SUPREMUM PROPERTY, INFIMUM PROPERTY &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: infimum,infimum property,property,supremum,supremum property,proof
contributors: bookofproofs

---


---

Let `\(D\)` be [non-empty subset][bookofproofs$552] of [real numbers][bookofproofs$1105] with an [upper bound][bookofproofs$584], say `\(B_0\)`. We will to show that `\(D\)` has a [supremum][bookofproofs$1754] by constructing it (The existence of an infimum for a non-empty lower-bounded subset of real numbers can be proven in a similar way.)


We consider any `\(x_0\in D\)`. Then we have `\(x_0 < B_0\)`, or, equivalently, `\(B_0 - x_0 > 0\)`. This is because `\(B_0\)` is an upper bound, by assumption. We now [construct sequences of real numbers][bookofproofs$875].
* `\(x_0 \le x_1 \le x_2 \le \ldots\)`, `\(x_i\in D\)` and
* `\(B_0 \ge B_1 \ge B_2 \ge \ldots\)` of upper bounds of `\(D\)` 

with the following property:

 `\[B_n-x_n\le \frac{B_0-x_0}{2^n}\quad\quad\text{for all }n\in\mathbb N\quad\quad( * )\]`

in the following recursive way: 

1. Having constructed the first `\(n\)` sequence members `\(x_0 \le \ldots\le x_n\)` and `\(B_0 \ge \ldots\ge B_n\)`, we set `\(M:=\frac{B_n-x_n}{2}\)` as the middle of the [closed real interval][bookofproofs$1153] `\([x_n,B_n]\)`.
1. If `\(M\)` is an upper bound of `\(D\)`, then we set `\(x_{n+1}:=x_n\)` and `\(B_{n+1}:=M\)`.
1. Otherwise, there exists an `\(x_{n+1}\in D \cap (M,B_n]\)` and we set `\(B_{n+1}:=B_{n}\)`.
1. We repeat all these steps "infinitely many times".

In all steps, the required properties `\(x_n \le x_{n+1}\)`, `\(B_n \ge B_{n+1}\)`, and `\(( * )\)` are all preserved. Note that the sequence `\((B_n)_{n\in\mathbb N}\)` is [monotonically decreasing][bookofproofs$1155] with the lower bound `\(x_0\)`. Therefore, according to the [monotone convergence theorem][bookofproofs$197], it is [convergent][bookofproofs$141] to some limit `\(B\)`:

`\[\lim_{n\to\infty}B_n=B.\]`

Because [convergence preserves upper bounds for sequence members][bookofproofs$1145], and because for any `\(x\in D\)`, we have by construction `\(x\le B\)`, `\(B\)` proves to be an upper bound of `\(D\)`. It remains to be shown that there is no smaller upper bound of `\(D\)` than `\(B\)`. Take any `\(B'\)` with `\(B' < B\)`. We will show that `\(B'\)` is no more an upper bound of `\(D\)`. 

With a growing `\(n\)`, the number `\(2^{-n}\)` [becomes arbitrarily small][bookofproofs$1350]. Therefore, we can find an `\(n\)` such that for any `\(B' < B\)` we get `\[\frac{B_0-x_0}{2^n} < B - B'.\quad\quad ( * * )\]`

It follows that 

`\[\begin{array}{rcll}
x_n&\ge& B_n-\frac{B_0-x_0}{2^n}&\text{by virtue of }( * )\\
&\ge& B-\frac{B_0-x_0}{2^n}&\text{sequence }(B_n)_{n\in\mathbb N}\text{ is monotonically decreasing}\\
& > & B'&\text{by virtue of }( * * )
\end{array}\]`

Therefore, there is no smaller upper bound of `\(D\)` than `\(B\)`. Thus, `\(B\)` is a supremum.
