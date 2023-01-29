layout: proof
categories: branches,analysis
nodeid: bookofproofs$1139
orderid: 50
parentid: bookofproofs$1135
title: 
description: Proof of PRODUCT OF CONVERGENT REAL SEQUENCES ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: product of limits,product of convergent real sequences,proof
contributors: bookofproofs

---


---

Let the real sequences `\((a_n)_{n\in\mathbb N}\)` and `\((b_n)_{n\in\mathbb N}\)` be  [convergent][bookofproofs$141]  with  `\(\lim_{n\rightarrow\infty} a_n=a\)` and `\(\lim_{n\rightarrow\infty} b_n=b\)`. It follows from the [corresponding proposition][bookofproofs$1137] that they are bounded by some [positive real number][bookofproofs$1107] `\(B > 0\)`. By making `\(B\)` sufficiently large, and without any loss of generality, we can assume `\(|a_n|\le B\)` and `\(|b_n| \le B\)` for all `\(n\in\mathbb N\)`. Further, let `\(\epsilon > 0\)`. It follows that

1. there is an `\(N(\epsilon,B)\in\mathbb N\)` with `\(|a_n - a| < \frac{\epsilon}{2B}\)` for all `\(n > N(\epsilon,B)\)`, and that 
1. there is an `\(M(\epsilon,B)\in\mathbb N\)` with `\(|b_n - b| < \frac{\epsilon}{2B}\)` for all `\(n > M(\epsilon,B)\)`.

Therefore, for all `\(n > \max(N(\epsilon,B),M(\epsilon,B))\)` we get by virtue of the [triangle inequality][bookofproofs$618]:
`\[|a_nb_n - ab| = |a_n(b_n - b)+ (a_n-a)b| \le |a_n||b_n - b| + |a_n - a||b| < B\frac{\epsilon}{2B} + \frac{\epsilon}{2B}B=\epsilon.\]`

Since `\(\epsilon\)` can be arbitrarily small chosen, it follows that

`\[\lim_{n\rightarrow\infty} (a_n \cdot b_n)=\lim_{n\rightarrow\infty} a_n \cdot \lim_{n\rightarrow\infty} b_n.\]`
