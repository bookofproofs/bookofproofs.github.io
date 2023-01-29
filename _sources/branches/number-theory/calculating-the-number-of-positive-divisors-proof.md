layout: proof
categories: branches,number-theory
nodeid: bookofproofs$1303
orderid: 50
parentid: bookofproofs$1302
title: 
description:  Proof of CALCULATING THE NUMBER OF POSITIVE DIVISORS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$701
keywords: calculating,divisors,number,positive,positive divisors,distinct positive divisors,number of positive divisors,proof
contributors: bookofproofs

---


---

* Let `\(n > 1 \)` be a [natural number][bookofproofs$718] with the [canonical representation][bookofproofs$803].
`\[n=\prod_{i=1}^\infty p_i^{e_i},\quad (e_i\ge 0 )\]`
i.e. all `\(p_i\)` are different and consecutive prime numbers with natural exponents `\(e_i\ge 0\)`. 
* Every other number
`\[d=\prod_{i=1}^\infty p_i^{\delta_i},\quad (\delta_i\ge 0 )\]`
is a [divisor][bookofproofs$1273] of `\(n\)` if and only if `$\delta_i\le e_i.$`
* Since there are `\(e_i+1\)` possibilities for each exponent `\(\delta_i\)` to be both, `\(\ge 0\)` and `\(\le e_i\)` and a specific choice of the exponent of one [prime number][bookofproofs$473] is independent from the specific choice of the exponent of another prime number to find another divisor of `\(n\)`, it follows from the [fundamental counting principle][bookofproofs$111] that the number of all distinct positive divisors must be `$\tau(n)=\prod_{i=1}^\infty (e_i+1).$`
* The postulated formula for the [number of of positive divisors][bookofproofs$8115] follows.
