layout: proof
categories: branches,analysis
nodeid: bookofproofs$1354
orderid: 50
parentid: bookofproofs$1353
title: 
description:  Proof of INFINITE GEOMETRIC SERIES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: geometric,infinite,infinite geometric series,series,proof
contributors: bookofproofs

---


---

In order to calculate the sum of partial sums of the geometric series `\(\sum_{k=0}^\infty x^n\)`, we can use the formula of [geometric progression][bookofproofs$1123] and get

`\[\sum_{k=0}^n x^n=\frac{1-x^{n+1}}{1-x}.\]`

Because, by hypothesis, `\(x\)` is a [real number][bookofproofs$1105] with an [absolute value][bookofproofs$583] `\(|x| < 1\)`, it follows from the [convergence behavior][bookofproofs$1347] of the sequence `\((x_n)_{n\in\mathbb N}\)` that `\(\lim_{n\to\infty} x^n=0\)`. Thus, the [limit][bookofproofs$175] of the [real infinite series][bookofproofs$1109] is

`\[\sum_{k=0}^\infty x^n=\frac{1}{1-x}.\]`
