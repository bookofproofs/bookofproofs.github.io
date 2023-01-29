layout: proof
categories: branches,number-theory
nodeid: bookofproofs$8137
orderid: 50
parentid: bookofproofs$8136
title: 
description:  Proof of NUMBERS BEING THE PRODUCT OF THEIR DIVISORS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272
keywords: being,divisors,numbers,product,their,proof
contributors: bookofproofs

---


---

### "`$\Rightarrow$`"

* Let `$n$` be a [natural number][bookofproofs$718] equal the [product][bookofproofs$876] of all its [divisors][bookofproofs$700] `$n=\prod_{d\mid n}d.$`
* While the index `$d\mid n$` runs through all divisors of `$n$`, this holds also for the index `$\frac nd\mid n$` built from the [complementary divisor][bookofproofs$700].
* It follows `$$n^4=n^2\cdot n^2=\prod_{d\mid n}d\cdot \prod_{d\mid n}\frac nd=\prod_{d\mid n}\left(d\cdot \frac nd\right)=\prod_{d\mid n}n=n^{\tau(n)},$$` with `$\tau(n)$` being the [number of positive divisors][bookofproofs$8115] of `$n.$`
* Taking the [formula for calculating the number of positive divisors][bookofproofs$1302], the exponents in the [factorization][bookofproofs$803] `$n=p_1^{e_1}\cdots p_r^{e_r}$` obey the following restriction:
`$$(e_1+1)\cdots(e_r+1)=4.$$`
* This restriction can be only fulfilled, if `$r=1$` and `$e_i=3$` or if `$r=2$` and `$e_i=e_j=1$` for some `$i\ge 1$`, `$j\ge 1$`, with `$i\neq j.$`
* From this, it follows that `$n=p^3$` for some [prime number][bookofproofs$473] `$p$` (case `$r=1$`) or that `$n=p_ip_j$` for some prime numbers `$p_i\neq p_j$` (case `$r=2$`).

### "`$\Leftarrow$`"

* Let `$n=p^3$` for be some [prime number][bookofproofs$473] `$p.$`
   * It follows `$n=\prod_{d\mid p^2}d=1\cdot p\cdot p^2\cdot p^3=p^6=(p^3)^2=n^2.$`
* Let `$n=p_ip_j$` for some prime numbers `$p_i\neq p_j.$`
   * It follows `$n=\prod_{d\mid p_ip_j}d=1\cdot p_i\cdot p_j\cdot p_ip_j=p^6=(p_ip_j)^2=n^2.$`
