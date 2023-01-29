layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1118
orderid: 50
parentid: bookofproofs$1117
title: 
description:  Proof of SUM OF ARITHMETIC PROGRESSION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1112
keywords: arithmetic,progression,sum,proof
contributors: bookofproofs

---


---

Since `\(a,b\in F\)` are elements of a [field][bookofproofs$557] `\((F, +, \cdot)\)`, we can use the [commutative law][bookofproofs$1114] and replace `\(k\)` by `\(n-k\)`, obtaining

`\[S=\sum_{0\le k\le n} (a+bk)=\sum_{0\le n-k\le n} (a+b(n-k)).\]`

Since both sides of the equation are equal, the  [associative law][bookofproofs$1114] allows the addition of both representations of `\(S\)`, obtaining

`\[2\cdot S=\sum_{0\le k\le n} ((a+bk)+(a+bn-bk))=\sum_{0\le k\le n} (2a + bn).\]`

By the [distributive law][bookofproofs$1114] we obtain a trivial [sum][bookofproofs$216].
`\[2\cdot S=(2a + bn)\sum_{0\le k\le n} 1=(2a + bn)(n+1).\]`

Dividing by `\(2\)` we obtain

`\[S=\left(a + \frac{bn}2\right)(n+1).\]`
