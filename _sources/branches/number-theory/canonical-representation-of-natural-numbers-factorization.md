layout: definition
categories: branches,number-theory
nodeid: bookofproofs$803
orderid: 300
parentid: bookofproofs$8104
title: Canonical Representation of Natural Numbers, Factorization
description: CANONICAL REPRESENTATION OF NATURAL NUMBERS, FACTORIZATION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$701
keywords: canonical,factorization,natural,numbers,representation,canonical factorization,canonical representation of a number,canonical representation,canonical number,canonical numbers,canonical representation of 156
contributors: bookofproofs

---
The [fundamental theorem of arithmetic][bookofproofs$8094] motivates the following definition:

---

Given consecutive [prime numbers][bookofproofs$473] `\(p_1=2, p_2=3, p_3=5, p_4=7, p_5=11,\ldots\)` we can write each [natural number][bookofproofs$718] `\(n \ge 1\)` as a [product][bookofproofs$876].
`\[n=\prod_{i=1}^\infty p_i^{e_i}.\]`
According to the above theorem, the product is unique for each `\(n > 1\)` and we call it the **canonical representation** of `\(n\)`. By setting the canonical representation of `\(1\)` to  
`\[1=\prod_{i=1}^\infty p_i^0,\]`
we can extend the definition to `\(n \ge 1\)`. Please note that for each `\(n \ge 1\)` its canonical representation is actually a finite product, since only finitely many exponents `\(e_i\)` are different from `\(0\)`.

Sometimes, it is more convenient to choose indexing of primes, which depends on the number `$n$` is such a way that `$p_1,\ldots,p_r$` are exactly those primes, which divide `$n.$` In this case the product `\[n=\prod_{i=1}^r p_i^{e_i}\]`
the **factorization** of `$n.$`
