layout: proof
categories: branches,analysis
nodeid: bookofproofs$1740
orderid: 50
parentid: bookofproofs$1739
title: 
description:  Proof of \\EXP0=1\ COMPLEX CASE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: case,complex,equals,exp,proof
contributors: bookofproofs

---


---

According to the [estimate for the remainder term of the exponential complex function][bookofproofs$1732], we have
`\[\exp(x)=\sum_{n=0}^N\frac{x^n}{n! }+r_{N + 1}(x),\]`
`\[|r_{N + 1}(x)|\le 2\frac{|x|^{N+1}}{(N+1)!}\quad\text{for }|x|\le \frac {N+2}2.\]`
It follows for `\(N=0\)` that

`\[|\exp(x)-1|\le 2|x|\quad\text{for }|x|\le 1.\]`

For any [convergent complex sequence][bookofproofs$1700] `\((x_n)_{n\in\mathbb N}\)` with `\(\lim_{n\to\infty} x_n=0\)` it follows

`\[\lim_{n\to\infty}|\exp(x_n)-1|=0.\]`
Thus
`\[\lim_{n\to\infty}\exp(x_n)=1.\]`
