layout: proposition
categories: branches,number-theory
nodeid: bookofproofs$8128
orderid: 100
parentid: bookofproofs$427
title: Calculating the Sum of Divisors
description: CALCULATING THE SUM OF DIVISORS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: calculating,divisors,sum
contributors: bookofproofs

---


---

Let `$n > 1$` and let `$n=\prod_{p\mid n}p^l$` be the [factorization][bookofproofs$803] of `$n.$` Then the [sum of divisors][bookofproofs$8127] of `$F(n)$` can be calculated using the formula `$$F(n)=\prod_{p\mid n}\frac{p^{l+1}-1}{p-1}.$$`

### Example

If `$n=28$` then `$n=2^2\cdot 7^1$` is its factorization. Therefore, `$$F(28)=\frac{2^{2+1}-1}{2-1}\cdot \frac{7^{1+1}-1}{7-1}=\frac{7}{1}\cdot \frac{48}{6}=7\cdot 8=56.$$`

Indeed, the [divisors][bookofproofs$700] of `$28$` are `$\{1,2,4,7,14,28\}$` and their sum is
`$$1+2+4+7+14+28=56.$$`
