layout: proof
categories: branches,number-theory
nodeid: bookofproofs$1334
orderid: 50
parentid: bookofproofs$1333
title: 
description:  Proof of DIVERGENCE OF HARMONIC SERIES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: divergence,harmonic,series,proof
contributors: bookofproofs

---


---

We want to show that the [harmonic series][bookofproofs$237] is [divergent][bookofproofs$217] with 

`\[\sum_{n=1}^\infty \frac 1n=\infty.\]`

Consider special partial sums

`\[\begin{array}{rcl}s_{2^{k+1}}&=&\sum_{n=1}^{2^{k+1}}\frac 1n\\
&=&1+\frac 12+\sum_{p=1}^k\left(\sum_{n=2^p+1}^{2^{p+1}}\frac 1n\right)\\
&=&1+\frac 12 \\
&& + \left(\frac 13+\frac 14\right) \\ 
&& +\left(\frac 15+\frac 16+\frac 17+\frac 18\right) \\
&&+ \left(\frac 17+\frac 18+\frac 19+\frac 1{10}+\frac 1{11}+\frac 1{12}+\frac 1{13}+\frac 1{14}+\frac 1{15}+\frac 1{16}\right) \\
&&\vdots\\
&&+\left(\sum_{n=2^k+1}^{2^{k+1}}\frac 1n\right).\end{array}\]`

Because the sums in all brackets are `\(\ge \frac 12\)`, it follows that 
`\[s_{2^{k+1}}\ge 1+\frac k2.\]`
Because the sequence of the partial sums `\((s_{2^{k + 1}})_{k\in\mathbb N}\)` is [unbounded][bookofproofs$217], the harmonic series is divergent.
