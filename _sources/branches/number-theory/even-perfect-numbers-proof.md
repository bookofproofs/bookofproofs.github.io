layout: proof
categories: branches,number-theory
nodeid: bookofproofs$8135
orderid: 50
parentid: bookofproofs$8134
title: 
description:  Proof of EVEN PERFECT NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: even,numbers,perfect,proof
contributors: bookofproofs

---


---

### "`$\Rightarrow$`"

* Let `$n$` be an [even][bookofproofs$8130] [perfect number][bookofproofs$8131].
* Since `$n$` is even, it has the [factorization][bookofproofs$803] `$n=2^{k-1}u$` with some `$k > 1$`, where `$u > 0$` is [odd][bookofproofs$8130].
* We can [calculate its sum of divisors][bookofproofs$8128] `$F(n)$` and get
`$$2^ku=2n=F(n)=\frac{2^k-1}{2-1}F(u)=(2^k-1)F(u).$$`
* It follows for the [sum of divisors][bookofproofs$8127] `$F(u)$` that
`$$F(u)=\frac{2^ku}{2^k-1}=\frac{2^ku-u+u}{2^k-1}=\frac{(2^k-1)u+u}{2^k-1}=u+\frac u{2^k-1}.$$`
* Because `$\frac u{2^k-1}=F(u)-u$`, this fraction is a [whole number][bookofproofs$844].
* Therefore, since `$k > 1$`, the number `$2^k-1$` is a [divisor][bookofproofs$700] of `$u$`, and it is [even][bookofproofs$8130].
* The [sum of divisors][bookofproofs$8127] `$F(u)$` is therefore the sum of `$u$` and some [proper divisor(s)][bookofproofs$700].
* But `$u$` has no even divisors, since it is odd. Therefore `$u$` is a [prime number][bookofproofs$473] of the form `$2^k-1.$`
* Therefore, `$n=\frac{F(n)}2=2^{k-1}(2^k-1)$` where `$u=2^k-1$` is a prime number.

### "`$\Leftarrow$`"

* Let `$n=\frac{F(n)}2=2^{k-1}(2^k-1)$` where `$p=2^k-1$` is a prime number.
* We can [calculate its sum of divisors][bookofproofs$8128] `$F(n)$` and get
`$$\sum_{d\mid n}d=F(n)=\frac{2^k-1}{2-1}\frac{p^2-1}{p-1}=(2^k-1)(p+1)=(2^k-1)2^k=2n.$$`
* It follows by definition that `$n$` is a [perfect number][bookofproofs$8131].
if and only if `$p$` is a [prime number][bookofproofs$473] having the form `$p=2^k-1$` for an `$k > 1, k\in\mathbb N.$`
