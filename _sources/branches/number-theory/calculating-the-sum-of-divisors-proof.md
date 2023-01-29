layout: proof
categories: branches,number-theory
nodeid: bookofproofs$8129
orderid: 50
parentid: bookofproofs$8128
title: 
description:  Proof of CALCULATING THE SUM OF DIVISORS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: calculating,divisors,sum,proof
contributors: bookofproofs

---


---

* Let `$n > 1$` and let `$n=\prod_{p\mid n}p^l$` be the [factorization][bookofproofs$803] of `$n.$`
* For each [prime number][bookofproofs$473] `$p$` which is a [divisor][bookofproofs$700] of `$n$` we have thet `$1=p^0,p^2,\ldots,p^l$` are all divisors of `$n.$`
* Therefore, in particular these divisors contribute to the sum of all divisors `$F(n)$` and, by the formula for the [sum of geometric progression][bookofproofs$6627], we have
`$$\sum_{m=0}^l p^m=\frac{p^{l+1}-1}{p-1}.$$`
* Now, not only one but any other prime number dividing `$n$` contributes this factor.
* By the [fundamental counting principle][bookofproofs$111] it follows that `$F(n)=\prod_{p\mid n}\frac{p^{l+1}-1}{p-1}.$`
