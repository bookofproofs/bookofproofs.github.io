layout: proof
categories: branches,number-theory
nodeid: bookofproofs$8096
orderid: 50
parentid: bookofproofs$8095
title: By Induction
description:  Proof of NATURAL NUMBERS AND PRODUCTS OF PRIME NUMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272
keywords: natural,numbers,prime,products,proof
contributors: bookofproofs

---


---

We prove it by [induction][bookofproofs$657].
*Base case* `$n=2$`
* Since `$2$` is a [prime number][bookofproofs$473], it is a [product][bookofproofs$876] of prime numbers (consisting of only one factor).

*Induction step* `$n-1\to n$`
* Let `$n > 2$` and the proposition be proven for `$2,3,\ldots,n-1.$`
* If `$n$` is a prime number, then `$n$` is a product of prime numbers (consisting of only one factor).
* Otherwise `$n$` can be written as a product `$n=n_1n_2$` with `$1 < n_1 < n$` and `$1 < n_2 < n.$`
* By hypothesis, `$n_1$` and `$n_2$` are products of prime numbers.
* Thus, `$n$` is a product of prime numbers.
