layout: proof
categories: branches,analysis
nodeid: bookofproofs$1717
orderid: 50
parentid: bookofproofs$1716
title: 
description:  Proof of CONVERGENT COMPLEX SEQUENCES ARE BOUNDED &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: are,bounded,complex,convergent,sequences,proof
contributors: bookofproofs

---


---

Let `\((a_n)_{n\in\mathbb N}\)` be a [convergent complex sequence][bookofproofs$1700] with `\(\lim_{n\rightarrow\infty} a_n=a\)`. It follows that there is an `\(N\in\mathbb N\)` such that 

`\[|a_n - a| < 1\quad\quad\forall n\ge N.\]` 
By virtue of the [triangle inequality][bookofproofs$1253], we get:

`\[|a_n| = |a_n - a + a|\le |a_n - a| + |a| < 1 + |a|\quad\quad\forall n\ge N.\]`

Set `\(B:=\max(|a_0|,|a_1|,\ldots,|a_{N-1}|,1 + |a|)\)`. With this [positive constant real number][bookofproofs$1107], we have

`\[|a_n| \le B\quad\quad\forall n\in\mathbb N.\]`

Therefore, `\((a_n)_{n\in\mathbb N}\)` is [bounded][bookofproofs$1714].