layout: proof
categories: branches,number-theory
nodeid: bookofproofs$510
orderid: 100
parentid: bookofproofs$8099
title: 
description: ANALYTIC PROOF ERDöS 1938 Proof of INFINITE SET OF PRIME NUMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: infinitely many prime numbers,infinite set of primes,there are infinitely many primes,proof
contributors: bookofproofs

---


---

* Assume, there are only [finitely many][bookofproofs$985] [prime numbers][bookofproofs$704] `\(p_1,p_2,p_3,\ldots,p_r\)` with `\(p_i\le n\)` for some [natural number][bookofproofs$718] `\(n\)`.  We observe that 
   * according to the [fundamental theorem of arithmetic][bookofproofs$800] any `\(m < n\)` can be written as a product of powers of the `\(p_i\)` and
   * any integer (`\(m\)` in particular!) can be written as the product of a square and a square-free integer[^1]. 
* Using these observations, for each such `\(m\)` we can write
`\[m=k^2\times p_1^{e_1}p_2^{e_2}p_3^{e_3}\cdots p_r^{e_r},\]`
where `\( e_i \in \left\{ 0,1 \right\} \)`, depending on whether a particular prime number is present or not in the square-free factor of `\(m\)`. 
* According to the [fundamental counting principle][bookofproofs$111], there are at most `\(2^r\)` possibilities of choosing such square-free factors. 
* On the other hand, from the [definition of square roots][bookofproofs$1161], it follows that  `\(k^2\le n\)` and `\(k\le \sqrt n\)`.
* It follows that integers smaller than `\(n\)` can be chosen in at most `\(2^r\times\sqrt n\)` ways, in other words
`\[n\le 2^r\times\sqrt n,\]`
resulting in 
`\[\sqrt n\le 2^r,\]`
and
`\[\frac 12\log_2 n\le r.\]`
* Since `\(n\)` is unbounded, so must the number `\(r\)` of primes smaller or equal `\(n\)` be. This completes the proof.


[^1]: This is clear enough if the integer is factorized into the product of its prime factors and the repeated ones are collected together. For example, `\(5096=2^3\cdot 7^2\cdot 13=(2\cdot 7)^2 \cdot (2\cdot 13)\)`.
