layout: proof
categories: branches,analysis
nodeid: bookofproofs$1125
orderid: 50
parentid: bookofproofs$1111
title: 
description:  Proof of \B\-ADIC FRACTIONS ARE REAL CAUCHY SEQUENCES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: adic,are,cauchy,fractions,real,sequences,proof
contributors: bookofproofs

---


---

It is sufficient to prove the proposition for a positive `\(b\)`-adic fraction. 

According to its [definition][bookofproofs$1110],  a `\(b\)`-adic fraction is a real series, which means that it is a sequence `\((s_m)_{m\in\mathbb N}\)` of partial of sums `\((s_m)_{m\in\mathbb N}\)` with 

`\[s_m=\sum_{k=-n}^m a_kb^{-k}.\]` 

and `\(0\le a_k < b\)`. We prove the proposition in two steps:

### `\((1)\)` The sequence `\((s_m)_{m\in\mathbb N}\)` is a real [Cauchy sequence][bookofproofs$1072].
Let `\(j\ge -n\)` and let without loss of generality `\(m \ge j\)`.  Then we have

`\[\begin{array}{rrl}
|s_m - s_j|&=&\sum_{k=-n}^m a_kb^{-k} - \sum_{k=-n}^j a_kb^{-k}\\
&=&\sum_{k=j+1}^m a_kb^{-k}\\
&\le & \sum_{k=j+1}^m (b-1)b^{-k}\\
&=&(b-1)b^{-j-1}\sum_{k=0}^{m-j-1} b^{-k}\quad\quad ( * )
\end{array}
\]`

In the sum `\( ( * ) \)`, we can apply the formula for the [sum of geometric progression][bookofproofs$1123], namely
 

`\[\sum_{k=0}^{m-j-1} b^{- k}=\sum_{k=0}^{m-j-1} \left(\frac 1b\right)^{k}=\frac{1-\left(\frac 1b\right)^{m-j}}{1- \frac 1b}=\frac{b-b^{j-m+1}}{b-1}.\]`

By replacing this result in `\( ( * ) \)`, we get

`\[\begin{array}{rrl}
|s_m - s_j|&=&(b - 1)b ^ { - j - 1}\cdot \frac{b - b^{j - m + 1}}{b - 1}\\
&=&b^{ - j } - b ^ { - m - 2}\\
&\le & b^{ - j} < \epsilon
\end{array}
\]`

for any arbitrarily small `\(\epsilon > 0\)`, if `\(j\)` gets sufficiently large. This proves that `\((s_n)_{n\in\mathbb N}\)` is a Cauchy sequence.


### `\((2)\)` The sequence `\((s_m)_{m\in\mathbb N}\)` converges to a real number.

This follows immediately from the [completeness principle][bookofproofs$1108] of real numbers, due to which each real Cauchy sequence has a real limit.
