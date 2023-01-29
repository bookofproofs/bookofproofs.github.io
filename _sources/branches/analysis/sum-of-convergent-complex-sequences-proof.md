layout: proof
categories: branches,analysis
nodeid: bookofproofs$1712
orderid: 50
parentid: bookofproofs$1711
title: 
description:  Proof of SUM OF CONVERGENT COMPLEX SEQUENCES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: complex,convergent,sequences,sum,proof
contributors: bookofproofs

---


---

Let `\(\epsilon > 0\)`. By hypothesis, the complex sequences `\((a_n)_{n\in\mathbb N}\)` and `\((b_n)_{n\in\mathbb N}\)` are [convergent][bookofproofs$141] to the limits `\(\lim_{n\rightarrow\infty} a_n=a\)` and `\(\lim_{n\rightarrow\infty} b_n=b\)`. It follows that

1. there is an `\(N(\epsilon)\in\mathbb N\)` with `\(|a_n - a| < \epsilon\)` for all `\(n > N(\epsilon)\)`, and that 
1. there is an `\(M(\epsilon)\in\mathbb N\)` with `\(|b_n - b| < \epsilon\)` for all `\(n > M(\epsilon)\)`.

Therefore, for all `\(n > \max(N(\epsilon),M(\epsilon))\)`, it follows from [triangle property of the absolute value][bookofproofs$1253] that 
`\[|(a_n + b_n) - (a + b)| \le |a_n - a| + |b_n - b| < \epsilon + \epsilon=2\epsilon.\]`

Since `\(\epsilon\)` can be arbitrarily small chosen, it follows that

`\[\lim_{n\rightarrow\infty} (a_n + b_n)=\lim_{n\rightarrow\infty} a_n + \lim_{n\rightarrow\infty} b_n= a + b.\]`
