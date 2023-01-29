layout: proof
categories: branches,analysis
nodeid: bookofproofs$1718
orderid: 50
parentid: bookofproofs$1715
title: 
description:  Proof of PRODUCT OF CONVEGENT COMPLEX SEQUENCES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: complex,convegent,product,sequences,proof
contributors: bookofproofs

---


---

Let the complex sequences `\((a_n)_{n\in\mathbb N}\)` and `\((b_n)_{n\in\mathbb N}\)` be  [convergent][bookofproofs$1700] with  `\(\lim_{n\rightarrow\infty} a_n=a\)` and `\(\lim_{n\rightarrow\infty} b_n=b\)`. It follows from the [corresponding proposition][bookofproofs$1716] that they are bounded by some [positive real number][bookofproofs$1107] `\(B > 0\)`. By making `\(B\)` sufficiently large, without any loss of generality, we can assume `\(|a_n|\le B\)` and `\(|b_n| \le B\)` for all `\(n\in\mathbb N\)`. Further, let `\(\epsilon > 0\)`. It follows that

1. there is an `\(N(\epsilon,B)\in\mathbb N\)` with `\(|a_n - a| < \frac{\epsilon}{2B}\)` for all `\(n > N(\epsilon,B)\)`, and that 
1. there is an `\(M(\epsilon,B)\in\mathbb N\)` with `\(|b_n - b| < \frac{\epsilon}{2B}\)` for all `\(n > M(\epsilon,B)\)`.

Therefore, for all `\(n > \max(N(\epsilon,B),M(\epsilon,B))\)` we get by virtue of the [triangle inequality][bookofproofs$1253].
`\[|a_nb_n - ab| = |a_n(b_n - b)+ (a_n-a)b| \le |a_n||b_n - b| + |a_n - a||b| < B\frac{\epsilon}{2B} + \frac{\epsilon}{2B}B=\epsilon.\]`

Since `\(\epsilon\)` can be arbitrarily small chosen, it follows that

`\[\lim_{n\rightarrow\infty} (a_n \cdot b_n)=\lim_{n\rightarrow\infty} a_n \cdot \lim_{n\rightarrow\infty} b_n.\]`
