layout: proof
categories: branches,analysis
nodeid: bookofproofs$1744
orderid: 50
parentid: bookofproofs$1743
title: 
description:  Proof of CONTINUITY OF COMPLEX EXPONENTIAL FUNCTION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: complex,continuity,exponential,function,proof
contributors: bookofproofs

---


---

We have to show that the [complex exponential function][bookofproofs$312] `\(\exp:\mathbb C\to \mathbb C\)` is [continuous][bookofproofs$251] on whole `\(\mathbb C\)`, formally for any `\(a\in\mathbb C\)`, we have
`\[\lim_{x\to a}\exp(x)=\exp(a).\]`
Let `\((x_n)_{n\in\mathbb N}\)` be a [convergent complex series][bookofproofs$1700] with `\(\lim_{n\to\infty} x_n=a\)`. We have then `\(\lim(x_n-a)=0\)`. Together with the [result][bookofproofs$1739] `\(\exp(0)=1\)` it follows
`\[\lim_{n\to \infty}\exp(x_n-a)=1.\]`
Because of the [non-zero property of the complex exponential function][bookofproofs$1738] `\(\exp(x)\neq 0\)` for all `\(x\in\mathbb C\)`, and because of the [functional equation of the complex exponential function][bookofproofs$1735], we can conclude that
`\[1=\lim_{n\to \infty}\exp(x_n-a)=\frac{\lim_{n\to \infty}\exp(x_n)}{\lim_{n\to \infty}\exp(a)}=\lim_{n\to \infty}\frac{\exp(x_n)}{\exp(a)}.\]`
`\[\exp(a)=\lim_{n\to \infty}\exp(x_n).\]`
In the last step we have used the [formula for the quotient of convergent complex sequences][bookofproofs$1722].