layout: proof
categories: branches,analysis
nodeid: bookofproofs$1365
orderid: 50
parentid: bookofproofs$1364
title: 
description:  Proof of REARRANGEMENT OF ABSOLUTELY CONVERGENT SERIES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: absolutely,convergent,rearrangement,series,proof
contributors: bookofproofs

---


---

From the definition of [absolute convergence][bookofproofs$198] it follows that `\(\sum_{k=0}^\infty |x_k|\)` is [convergent][bookofproofs$175] to a limit, say `\(L\)`. We have to show that for every [permutation][bookofproofs$188] `\(\sigma:\mathbb N\to \mathbb N\)`, the [rearrangement][bookofproofs$1363] `\(\sum_{k=0}^\infty x_{\sigma(k)}\)` is  [convergent][bookofproofs$175] to `\(L\)`.

Assume `\(\epsilon > 0\)`. Because  `\(\sum_{k=0}^\infty |x_k|=L\)`, and applying the [triangle inequality][bookofproofs$588], there exists an index `\(N(\epsilon)\)` such that 

`\[\left|\sum_{k=0}^{N(\epsilon) - 1} x_{k}~- L\right|=\left|\sum_{k=N(\epsilon)}^{\infty} x_{k}\right|\le \sum_{k=N(\epsilon)}^{\infty} |x_{k}| < \frac\epsilon2.\quad\quad ( * )\]`

Consider the [subset][bookofproofs$552] of natural numbers given by

`\[\Sigma(M):=\{\sigma(0), \sigma(1), \sigma(2), \ldots, \sigma(M)\}.\]` 

Note that we can choose `\(M\)` big enough to satisfy 
`\[\{0, 1, 2, \ldots, N(\epsilon)-1 \}\subset \Sigma(M). \]`

This enforces the inequality  

`\[\left|\sum_{k=0}^{m} x_{\sigma(k)}~-~\sum_{k=0}^{N(\epsilon) - 1} x_{k}\right|\le \sum_{k=N(\epsilon)}^{\infty} x_{k}\le \sum_{k=N(\epsilon)}^{\infty} |x_{k}|,\quad\quad ( * * )\]`

since all sequence members `\(x_k\)`, `\(k=0,1,\ldots,N(\epsilon) - 1\)` cancel out, leaving only sequence members `\(x_k\)` left for `\(k \ge N(\epsilon)\)`. For all `\(m\ge M\)`, it follows from `\(( * ) \)` and `\(( * * ) \)`:

`\[\begin{array}{rcl}
\left|\sum_{k=0}^{m} x_{\sigma(k)}~-~L\right|&=&\left|\sum_{k=0}^{m} x_{\sigma(k)}~-~\sum_{k=0}^{N(\epsilon) - 1} x_{k}~+~\sum_{k=0}^{N(\epsilon) - 1} x_{k}~-~L\right|\\
&\le & \left|\sum_{k=0}^{m} x_{\sigma(k)}~-~\sum_{k=0}^{N(\epsilon) - 1} x_{k}\right|~+~\left|\sum_{k=0}^{N(\epsilon) - 1} x_{k}~-~L\right|\\
&\le& \sum_{k=N(\epsilon)}^{\infty} |x_{k}|~+~\frac\epsilon2\\
&\le& \frac\epsilon2~+~\frac\epsilon2=\epsilon.
\end{array}
\]`
