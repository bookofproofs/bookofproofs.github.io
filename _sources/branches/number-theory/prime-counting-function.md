layout: definition
categories: branches,number-theory
nodeid: bookofproofs$8114
orderid: 50
parentid: bookofproofs$8113
title: Prime-Counting Function
description: PRIME-COUNTING FUNCTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: counting,function,prime,prime-counting function,prime counting function,who invented prime counting function,prime counting
contributors: bookofproofs

---
We have seen already that there are [infinitely many prime numbers][bookofproofs$8099]. In other words, if we count the primes `$p$` with `$p \le n$` for a given natural number `$n$` and let this number grow to infinity, the number of the primes we have to count will also grow to infinity. The question "how fast" this growth is one of the most key questions of number theory. The function which counts the number of primes in the described way an arithmetic function called the _prime-counting function_.

---

The *prime-counting function* is an [arithmetic function][bookofproofs$8112], which is in the number theory traditionally denoted by `$\pi:\mathbb N\to\mathbb N.$` It counts for an `$n > 0$`, `$\pi(n)$` how many [prime numbers][bookofproofs$473] `$p\in\mathbb P$` are there which are smaller or equal `$n$`, i.e. `$p\le n.$` In the [sum notation][bookofproofs$261], the function `$\pi$` can be written as `$$\pi(n):=\sum_{p\in\mathbb P,\; p\le n}1\quad\quad\forall n > 0.$$`

### Example.

The prime-counting function is a [step function][bookofproofs$6796], the beginning of which can be visualized using SageMath. If you click on the evaluate button, you will see the values of `$\pi(n)$` for `$n=1,\ldots,100.$` 


§§§1

---

§§§1
<div class='sage'>
plot(prime_pi(x), (x,1,100))
</div>
