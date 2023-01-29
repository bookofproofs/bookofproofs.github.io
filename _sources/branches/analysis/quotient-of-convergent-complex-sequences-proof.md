layout: proof
categories: branches,analysis
nodeid: bookofproofs$1723
orderid: 50
parentid: bookofproofs$1722
title: 
description:  Proof of QUOTIENT OF CONVERGENT COMPLEX SEQUENCES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: complex,convergent,quotient,sequences,proof
contributors: bookofproofs

---


---

We have to prove the proposition only for the special case of a constant complex sequence `\((a_n)_{n\in\mathbb N}\)` with `\(a_n=1\)` for all `\(n\in\mathbb N\)`, because the general case follows then immediately from the corresponding proposition about the [product of convergent complex sequences][bookofproofs$1715] and from the identity `\[\frac {a_n}{b_n}=a_n\cdot\frac 1{b_n}.\]`

By hypothesis, the limit of the [convergent complex sequences][bookofproofs$1700] `\((b_n)_{n\in\mathbb N}\)` does not equal the [complex zero][bookofproofs$1662] (`\(b\neq 0\)`). Thus, we can find some index `\(N(b)\)` such that 

`\[|b_n - b| < \frac{|b|}{2}\quad\quad\forall n \ge N(b).\]`

Therefore, it follows[^1] that `\(b_n\neq 0\)` for all `\(n \ge N(b)\)`, because `\(|b_n|\ge |b|/2\)` for all `\(n \ge N(b)\)`, or `\(1/|b_n|\le 2/|b|\)`. We will need this estimation a little bit later.

Now, it follows from the convergence of `\((b_n)_{n\in\mathbb N}\)`  that for a given `\(\epsilon  > 0\)`, there exists an index `\(N(\epsilon)\in\mathbb N\)` such that

`\[|b_n - b |< \frac{\epsilon|b|^2}{2}\quad\quad\forall n\ge N(\epsilon).\]` 

It follows for all `\(n\ge M(\epsilon,b):=\max(N(b),N(\epsilon))\)` that

`\[\left|\frac 1{b_n} - \frac 1b \right| = \left|\frac{ b - b_n}{b_n b}\right|=\frac{1}{|b_n||b|}\cdot |b_n - b| < \frac{2}{|b|^2}\cdot\frac{\epsilon|b|^2}{2}=\epsilon\quad\quad\forall n\ge M(\epsilon,b).\]` 

Thus, we have proven that :

`\[\lim_{n\rightarrow\infty,~n\ge M(\epsilon,b)} \frac{a_n}{b_n}=\frac{\lim_{n\rightarrow\infty,~n\ge M(\epsilon,b)} a_n}{\lim_{n\rightarrow\infty,~n\ge M(\epsilon,b)} b_n}.\]`

[^1]: This is just because each sequence member `\(b_n\)` is "closer" to `\(b\)` then it is to `\(0\)`, interpreting `\(|b|/2\)` as half the distance from `\(b\)` to `\(0\)`.
