layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1122
orderid: 50
parentid: bookofproofs$1121
title: 
description:  Proof of THE GENERAL PERTURBATION METHOD &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1112
keywords: general,method,perturbation,proof
contributors: bookofproofs

---


---

Since the sets `\(\{1,2,\ldots,n\}\)` and `\(\{n+1\}\)`, respectively `\(\{0\}\)` and `\(\{1,2,\ldots,n+1\}\)` of [natural numbers][bookofproofs$718] and disjoint, by applying the [rule of combining different sets of indices][bookofproofs$1119] we get two (trivial) splits of the sum `\(S_n\)`:

`\[S_n + a_{n+1}=\sum_{0\le k\le n+1} a_k= a_0 + \sum_{1\le k\le n+1} a_k.\]`

By shifting the index of the right side of the equation twice ("perturbation" of the indices, which gives this method its name) we further get

`\[a_0 + \sum_{1\le k\le n+1} a_k=a_0 + \sum_{1\le k+1\le n+1} a_{k+1}=a_0 + \sum_{0\le k\le n} a_{k+1},\]`

which completes the proof.
