layout: proof
categories: branches,analysis
nodeid: bookofproofs$1424
orderid: 50
parentid: bookofproofs$1423
title: 
description: Proof of EXP(0)=1 ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: exponential function of zero,exponential function zero,proof
contributors: bookofproofs

---


---

According to the [estimate for the remainder term of the exponential function][bookofproofs$1361], we have
`\[\exp(x)=\sum_{n=0}^N\frac{x^n}{n! }+r_{N + 1}(x),\]`
`\[|r_{N + 1}(x)|\le 2\frac{|x|^{N+1}}{(N+1)!}\quad\text{for }|x|\le \frac {N+2}2.\]`
It follows for `\(N=0\)` that

`\[|\exp(x)-1|\le 2|x|\quad\text{for }|x|\le 1.\]`

For any [convergent real sequence][bookofproofs$141] `\((x_n)_{n\in\mathbb N}\)` with `\(\lim_{n\to\infty} x_n=0\)` it follows

`\[\lim_{n\to\infty}|\exp(x_n)-1|=0.\]`
Thus
`\[\lim_{n\to\infty}\exp(x_n)=1.\]`
