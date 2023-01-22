layout: definition
categories: branches,algebra
nodeid: bookofproofs$6323
orderid: 1
parentid: bookofproofs$211
title: Polynomial Ring
description: POLYNOMIAL RING ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$6907
keywords: polynomial ring,polynomial rings
contributors: bookofproofs

---


---

The [set][bookofproofs$550] of all [polynomials][bookofproofs$487] 

`\[p=a_{0}+a_{1}x+a_{2}x^{2}+\cdots +a_{n}x^{n}\]`

over the [commutative ring][bookofproofs$880]  `\(R\)` (i.e. with `\(a_{i}\in R,\,i=0,\ldots ,n,\,n\in \mathbb {N} \)`), together with the component-wise addition and multiplication follow the usual rules of [exponentiation][bookofproofs$673] `\(X^{n}\cdot X^{m}:=X^{n+m}\)` is called **polynomial ring** and denoted by `\(R[X]\)`. Specifically, if `\(p,q\in R[X]\)` with

`\[p=a_{0}+a_{1}x+a_{2}x^{2}+\cdots +a_{m}x^{m},\]`

and

`\[q=b_{0}+b_{1}x+b_{2}x^{2}+\cdots +b_{n}x^{n},\]`

then the addition of the two polynomials in `\(R[X]\)` is defined as follows:

`\[p+q:=r_{0}+r_{1}x+r_{2}x^{2}+\cdots +r_{k}x^{k},\quad\quad k = \max(m, n),\,r_{i}:=a_{i}+b_{i}\]`

and

`\[p\cdot q:=s_{0}+s_{1}x+s_{2}x^{2}+\cdots +s_{l}x^{l},\quad\quad l = m + n,\,s_{i}=a_{0}b_{i}+a_{1}b_{i-1}+\cdots +a_{i-1}b_{1}+a_{i}b_{0}.\]`
