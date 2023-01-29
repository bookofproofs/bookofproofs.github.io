layout: definition
categories: branches,number-theory,sieve-methods
nodeid: bookofproofs$6402
orderid: 50
parentid: bookofproofs$366
title: Sieve of Eratosthenes
description: SIEVE OF ERATOSTHENES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$701
keywords: eratosthenes,sieve,sieve of eratosthenes
contributors: bookofproofs


---


---

It is well-known that there are [infinitely many prime numbers][bookofproofs$8099]. Due to "Eratosthenes of Cyrene":https://www.bookofproofs.org/history/eratosthenes-of-cyrene/, the following efficient method, called the **sieve of Eratosthenes**, can be used to find [prime numbers][bookofproofs$473]:

1. Start with the sequence of numbers `\(2,3,4,\ldots\)`.
1. The first number, which is not "sieved", is `\(2\)`. This is the first prime number.
1. Remove from the sequence all proper multiples of `\(2\)`, i.e. the numbers `\(2k\)` for `\(k=2,3,4,\ldots\)`.
1. Look for the next number, which is not "sieved"; this is `\(3\)`. This is the next prime number.
1. Remove from the sequence all proper multiples of `\(3\)`, i.e. the numbers `\(3k\)` for `\(k=2,3,4,\ldots\)`.
1. Repeat this procedure for any next number, which hes not yet been "sieved".
1. This procedure leads to the sequence of prime numbers, i.e. `\(2,3,5,7,11,\ldots\)`.

The following figure visualizes the sieve of Eratosthenes:


![sieveprimes](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/sieveprimes.png?raw=true)

