layout: proposition
categories: branches,number-theory
nodeid: bookofproofs$1302
orderid: 400
parentid: bookofproofs$232
title: Calculating the Number of Positive Divisors
description: CALCULATING THE NUMBER OF POSITIVE DIVISORS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: calculating,divisors,number,positive,positive divisors,distinct positive divisors,number of positive divisors
contributors: bookofproofs

---
As a next application of [arithmetic functions][bookofproofs$8112] we provide a general formula for the  [number of positive divisors][bookofproofs$8115] `\(\tau(n)\)`.

---

Let `\(n > 1 \)` be a [natural number][bookofproofs$718] with the [factorization][bookofproofs$803].
`\[n=\prod_{i=1}^\infty p_i^{e_i}.\]`

Then, the [number of positive divisors][bookofproofs$8115] `\(\tau(a)\)` can be calculated as 

`\[\tau(a)=\prod_{i=1}^\infty (e_i+1).\]` 

### Example:

`\(n=877800\)` has `\(192\)` positive divisors, since 

`$$n=877800=2^3\cdot 3^1\cdot 5^2\cdot 7^1\cdot 11^1\cdot 13^0\cdot 17^0\cdot 19^1\cdot\prod_{i=9}^\infty p_i^0$$`
and 
`\[\tau(877800)=4\cdot 2\cdot 3\cdot 2\cdot 2\cdot 1\cdot 1\cdot 2\cdot\prod_{i=9}^\infty 1=192.\]`
