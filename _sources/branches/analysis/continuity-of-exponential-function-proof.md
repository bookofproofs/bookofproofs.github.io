layout: proof
categories: branches,analysis
nodeid: bookofproofs$1425
orderid: 50
parentid: bookofproofs$1422
title: 
description:  Proof of CONTINUITY OF EXPONENTIAL FUNCTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: exponential series,exponential function,proof,continuity of exponential function,proof
contributors: bookofproofs


---


---

Let `\(a\in\mathbb R\)`. We have to show that the [exponential function][bookofproofs$281] `\(\exp:\mathbb R\to \mathbb R\)` is [continuous][bookofproofs$1260], formally
`\[\lim_{x\to a}\exp(x)=\exp(a).\]`
Let `\((x_n)_{n\in\mathbb N}\)` be any [convergent real series][bookofproofs$141] with `\(\lim_{n\to\infty} x_n=a\)`. We have then `\(\lim(x_n-a)=0\)`. Together with the [result][bookofproofs$1423] `\(\exp(0)=1\)` it follows
`\[\lim_{n\to \infty}\exp(x_n-a)=1.\]`
Because of the "non-zero property of the exponential function":[bookofproofs$141]7 `\(\exp(x)\neq 0\)` for all `\(x\in\mathbb R\)`, and because of the [functional equation of the exponential function][bookofproofs$141]5 we can conclude that
`\[1=\lim_{n\to \infty}\exp(x_n-a)=\frac{\lim_{n\to \infty}\exp(x_n)}{\lim_{n\to \infty}\exp(a)}=\lim_{n\to \infty}\frac{\exp(x_n)}{\exp(a)}.\]`
`\[\exp(a)=\lim_{n\to \infty}\exp(x_n).\]`
In the last step we have used the [formula for the quotient of convergent real sequences][bookofproofs$1142].