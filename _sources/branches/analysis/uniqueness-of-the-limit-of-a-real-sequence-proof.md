layout: proof
categories: branches,analysis
nodeid: bookofproofs$8620
orderid: 50
parentid: bookofproofs$8619
title: 
description: PROOF OF UNIQUENESS OF THE LIMIT OF A REAL SEQUENCE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: uniqueness of the limit of a real sequence,proof
contributors: bookofproofs

---


---

* By hypothesis, a [real sequence][bookofproofs$875] `$(x_n)_{n\in N}$` is [convergent][bookofproofs$141].
* Assume, the sequence converges against two values `$x$` and `$y.$`
* By definition, this means that for every `$\epsilon > 0$` there is:
   * an index `$N_x\in\mathbb N$` with `$|x_n-x|<\frac\epsilon 2$` for all `$n\ge N_x,$` and
   * an index `$N_y\in\mathbb N$` with `$|x_n-y|<\frac\epsilon 2$` for all `$n\ge N_y.$`
* Now, from the [triangle inequality][bookofproofs$588], it follows `$$\begin{align}
|x-y|&=|x-x_n+x_n-y|\nonumber\\
&\le|x-x_n|+|x_n-y|\nonumber\\
&<\frac\epsilon 2+\frac\epsilon 2\nonumber\\
&=\epsilon\nonumber\end{align}$$`
for all `$n\ge\max(N_x,N_y).$` 
* This means that `$x-y=0,$` or `$x=y.$`
