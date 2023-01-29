layout: proof
categories: branches,analysis
nodeid: bookofproofs$1132
orderid: 50
parentid: bookofproofs$1131
title: 
description:  Proof of SUM OF CONVERGENT REAL SEQUENCES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: sum of convergent sequences,sum of limits,proof
contributors: bookofproofs

---


---

Let `\(\epsilon > 0\)`. Because the real sequences `\((a_n)_{n\in\mathbb N}\)` and `\((b_n)_{n\in\mathbb N}\)` are [convergent][bookofproofs$141] with `\(\lim_{n\rightarrow\infty} a_n=a\)` and `\(\lim_{n\rightarrow\infty} b_n=b\)`, it follows that

1. there is an `\(N(\epsilon)\in\mathbb N\)` with `\(|a_n - a| < \epsilon\)` for all `\(n > N(\epsilon)\)`, and that 
1. there is an `\(M(\epsilon)\in\mathbb N\)` with `\(|b_n - b| < \epsilon\)` for all `\(n > M(\epsilon)\)`.

Therefore, for all `\(n > \max(N(\epsilon),M(\epsilon))\)`, it follows from [triangle property of the absolute value][bookofproofs$618] that 
`\[|(a_n + b_n) - (a + b)| \le |a_n - a| + |b_n - b| < \epsilon + \epsilon=2\epsilon.\]`

Since `\(\epsilon\)` can be arbitrarily small chosen, it follows that

`\[\lim_{n\rightarrow\infty} (a_n + b_n)=\lim_{n\rightarrow\infty} a_n + \lim_{n\rightarrow\infty} b_n= a + b.\]`
