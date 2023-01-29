layout: proposition
categories: branches,analysis
nodeid: bookofproofs$6732
orderid: 100
parentid: bookofproofs$6731
title: Estimates for the Remainder Terms of the Infinite Series of Cosine and Sine
description: ESTIMATES FOR THE REMAINDER TERMS OF THE INFINITE SERIES OF COSINE AND SINE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: cosine,infinite,series,sine,sine infinite series,proof
contributors: bookofproofs

---


---

The [infinite series of cosine and sine][bookofproofs$6731] can be approximated by a [partial sum][bookofproofs$1109] of the first `$n+1$`:
`$$\begin{array}{rcl}\cos(x)&=&\sum_{k=0}^\infty (-1)^k\frac{x^{2k}}{(2k)!}=\sum_{k=0}^n(-1)^k\frac{x^{2k}}{(2k)!}1+r_{2n+2}(x),\\
\sin(x)&=&\sum_{k=0}^\infty (-1)^k\frac{x^{2k+1}}{(2k+1)!}=\sum_{k=0}^n(-1)^k\frac{x^{2k+1}}{(2k+1)!}+r_{2n+3}(x),\end{array}$$`

with some error remainder terms not greater than 

`$$\begin{array}{rcl}|r_{2n+2}(x)|\le\frac{|x|^{2n+2}}{(2n+2)!}&\text{ for }&|x|\le 2n+3,\\
|r_{2n+3}(x)|\le\frac{|x|^{2n+3}}{(2n+3)!}&\text{ for }&|x|\le 2n+4.\end{array}$$`
