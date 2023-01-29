layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1097
orderid: 50
parentid: bookofproofs$1096
title: 
description: GEOMETRIC PROOF Proof of DISCOVERY OF IRRATIONAL NUMBERS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$1093
keywords: 5th,century,discovery,hippasus,irrational,metapontum,numbers,who discovered irrational numbers,hippasus irrational numbers,discovery of irrational numbers,proofs related to irrational numbers,proof
contributors: bookofproofs

---


---

* According to the [Pythagorean theorem][bookofproofs$968], given a square with the side `\(q\)` for some integer `\(q\in\mathbb N\)`, the length of the diagonal `\(p\)` is given by 
`\[p=\sqrt 2 q,~\quad\text{or}\quad\sqrt 2=\frac pq.\]`
* Assume that `\(\frac pq\)` is a [rational number][bookofproofs$1033] `\(\frac pq\in\mathbb Q\)` and that the positive integers `\(p\)` (numerator) and `\(q\)` (denominator) have no [common prime factors][bookofproofs$800] (otherwise cancel out these prime factors to get the reduced fraction). 
* Given these numbers, we can construct a smaller triangle (shaded) with the sides `\(2q-p\)`, `\(p-q\)`, `\(p-q\)`, like shown in the below picture.


![sqrt2_1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/sqrt2_1.jpg?raw=true)

* Since both triangles are [similar][bookofproofs$2782], we conclude that
`\[\sqrt 2=\frac pq=\frac {2q-p}{p-q}.\]`
* Since the numerator and the denominator of `\(\frac {2q-p}{p-q}\)` are smaller then the numerator and the denominator of `\(\frac pq\)`, the natural numbers `\(2q-p\)` and `\(p\)` as well as `\(p-q\)` and `\(q\)` have to have different [factorizations][bookofproofs$800]. 
* But this is a [conctradiction][bookofproofs$744] to how the fraction `\(\frac pq\)` was constructed (i.e. there were no more common prime factors we could cancel out from `\(p\)` and `\(q\)`). 
* On the other hand, only by such a cancellation, we would preserve the ratio of `\(\sqrt 2\)`. Therefore, our assumption that `\(p\)` is a whole number must be wrong. 
* Consequently, `\(\sqrt 2\)` must be irrational.
