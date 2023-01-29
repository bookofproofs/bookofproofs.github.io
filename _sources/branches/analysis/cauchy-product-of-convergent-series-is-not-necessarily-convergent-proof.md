layout: proof
categories: branches,analysis
nodeid: bookofproofs$1393
orderid: 50
parentid: bookofproofs$1392
title: 
description:  Proof of CAUCHY PRODUCT OF CONVERGENT SERIES IS NOT NECESSARILY CONVERGENT &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: cauchy,cauchy product,convergent,necessarily,not,product,series,cauchy product of series,cauchy product of two series,proof
contributors: bookofproofs

---


---

It is sufficient to find only one counter-example of two [convergent series][bookofproofs$198] `\(\sum_{n=0}^\infty a_n\)` and `\(\sum_{n=0}^\infty b_n\)`, the Cauchy product of which does not converge.

We construct such a counter-example. For a fixed `\(n\)` set

`\[a_n:=b_n:=\frac{(-1)^n}{\sqrt{n+1}}\quad\text{and}\quad c_n:=\sum_{k=0}^n a_{n-k}b_k.\]`

We will first show that the series   `\(\sum_{n=0}^\infty a_n\)` and `\(\sum_{n=0}^\infty b_n\)` are convergent. This follows from the [criterion for alternating infinite series][bookofproofs$1266], because the sequence `\[\left(\frac{1}{\sqrt{n+1}}\right)_{n\in\mathbb N}\]`
is a [monotonically decreasing real sequence][bookofproofs$1155], which converges to `\(0\)`.

The Cauchy product has the terms 
`\[c_n:=\sum_{k=0}^n a_{n-k}b_k=\sum_{k=0}^n \frac{(-1)^{n-k}}{\sqrt{n-k+1}}\cdot\frac{(-1)^n}{\sqrt{n+1}}=(-1)^n\sum_{k=0}^n\frac 1{\sqrt{(n-k+1)(k+1)}}.\]`
Now, for all `\(k=0,\ldots,n\)` we can estimate 
`\[(n-k+1)(k+1)=(n-k)k+(n-k)+(k+1)=(n-k)k+(n+1)\le n^2+(n+1) < n^2+2n+1=(n+1)^2,\]`
and
`\[\sqrt{(n-k+1)(k+1)} < (n+1).\]`
and thus, for all `\(k=0,\ldots,n\)`, we get the estimation
`\[\frac {1}{\sqrt{(n-k+1)(k+1)}}>\frac {1}{(n+1)}.\]`
With this estimation, we can therefore finally estimate  
`\[|c_n|=\left|\sum_{k=0}^n\frac {1}{\sqrt{(n-k+1)(k+1)}}\right| >  \left|\sum_{k=0}^n\frac {1}{(n+1)}\right|=(n+1)\cdot \frac {1}{(n+1)}=1.\]`
This demonstrates that the series `\(\sum_{n=0}^\infty c_n\)` cannot converge, since the [absolute value][bookofproofs$583] of every term is greater then `\(1\)`. (If the series converged, then it would violate the [necessary condition for convergent series][bookofproofs$1264] requiring all terms to converge to `\(0\)`.)
