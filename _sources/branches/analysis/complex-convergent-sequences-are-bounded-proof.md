layout: proof
categories: branches,analysis
nodeid: bookofproofs$6873
orderid: 50
parentid: bookofproofs$6872
title: 
description: Proof of COMPLEX CONVERGENT SEQUENCES ARE BOUNDED ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$6823
keywords: complex convergent sequences are bounded,complex convergent bounded sequences,proof
contributors: bookofproofs

---


---

* By hypothesis, `\((a_n)_{n\in\mathbb N}\)` is a [convergent complex sequence][bookofproofs$1700] with `\(\lim_{n\rightarrow\infty} a_n=a\)`. 
* Thus, there is an `\(N\in\mathbb N\)` such that `$|a_n - a| < 1\quad\quad\forall n\ge N.$`
* By virtue of the [triangle inequality][bookofproofs$1253], we get `$$|a_n| = |a_n - a + a|\le |a_n - a| + |a| < 1 + |a|$$` for all `$n\ge N.$`
* Set `\(B:=\max(|a_0|,|a_1|,\ldots,|a_{N-1}|,1 + |a|)\)`. 
* With this constant, we have `$|a_n| \le B$` for all `$n\in\mathbb N.$`
* Therefore, `\((a_n)_{n\in\mathbb N}\)` is [bounded][bookofproofs$1714].