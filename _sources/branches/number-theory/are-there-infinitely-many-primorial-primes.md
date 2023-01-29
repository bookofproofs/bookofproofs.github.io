layout: problem
categories: branches,number-theory
nodeid: bookofproofs$511
orderid: 200
parentid: bookofproofs$179
title: Are there infinitely many primorial primes?
description: ARE THERE INFINITELY MANY PRIMORIAL PRIMES? &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: unsolved number-theoretic problems,solution
contributors: bookofproofs

---


---

We call the number `\(p_r\downarrow:=p_1p_2\cdots p_r\)` the **primorial** of the first `\(r\)` consecutive prime numbers smaller or equal `\(p_r\)`[^1]. 

The Euclidean proof for the infinite number of primes provides no indication of how to find the next prime number `\(P\)`. It only indicates that `\(p_r < P\le p_r\downarrow+1\)`. Thus, for some indices `\(r\)`, the number `\(p_r\downarrow+1\)` itself is a prime number, and for other indices it is composite. 

The following problems are unsolved:

1. Are there infinitely many primes `\(p\)`, for which `\(p\downarrow+1\)` is also prime?
1. Are there infinitely many primes `\(p\)`, for which `\(p\downarrow+1\)` is composite?
1. Are there infinitely many primes `\(p\)`, for which `\(p\downarrow-1\)` is also prime?
1. Are there infinitely many primes `\(p\)`, for which `\(p\downarrow-1\)` is composite?


We call the numbers `\(p\downarrow+1\)` and `\(p\downarrow-1\)` **primorial primes** if they are prime.

In 2002, Galdwell &amp; Gallot tested the primality of `\(p\downarrow+1\)` for primes `\(p\)` < 120000 and discovered that these numbers are prime only for the prime numbers `\(p=\)` 2, 3, 5, 7, 11, 31, 379, 1019, 1021, 2657, 3229, 4587, 11549, 13649, 18523, 23801, 24029, and 42209. The corresponding results for `\(p\downarrow-1\)` were `\(p=\)` 3, 5, 11, 13, 41, 89, 317, 337, 991, 1873, 2053, 2377, 4093, 4297, 4583, 6569, 13033, and 15877. Up to now, these results were confirmed for `\(p < \)` 637000 and `\(p < \)`  650000, respectively[^2]. 

[^1]: The name "primorial of `\(p\)`" for the product of all primes `\(\le p\)` was introduced 1987 by Dubner, probably in accordance with the name "factorial" `\(n!\)`, meaning the product of all natural numbers `\(\le n\)`.

[^2]: See Paolo Ribenboim, "The Little Book of Bigger Primes", Springer New York, 2004
