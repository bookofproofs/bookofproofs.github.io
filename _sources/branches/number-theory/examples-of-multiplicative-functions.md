layout: example
categories: branches,number-theory
nodeid: bookofproofs$8140
orderid: 100
parentid: bookofproofs$505
title: Examples of Multiplicative Functions
description: EXAMPLES OF MULTIPLICATIVE FUNCTIONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: examples,functions,multiplicative
contributors: bookofproofs

---


---

* The [prime-counting function][bookofproofs$8114] `$\pi\mathbb N\to\mathbb N$` and the [von Mangoldt function][bookofproofs$702] `$\Lambda:\mathbb N\to\mathbb N$` are obviously not [multiplicative][bookofproofs$505]. For instance, `$\pi(1)=0\neq 1$` and `$\Lambda(1)=0\neq 1,$` which would otherwise be the case because of the [above corollary][bookofproofs$8138].
* The [number of divisors function][bookofproofs$8115] `$\tau\mathbb N\to\mathbb N$` is multiplicative. In particular, we have `$\tau(1)=1$` and, for instance `$\tau(24)=\tau(2^3)\cdot\tau(3^1)=4\cdot 2=8.$`
* The [Moebius function][bookofproofs$8116] `$\mu:\mathbb N\to\mathbb N$` is multiplicative, since if `$n,m$` are [co-prime][bookofproofs$8093] and [square-free][bookofproofs$8116], then their product is square-free. Therefore `$\mu(nm)=\mu(n)\mu(m).$` Moreover, we have `$\mu(1)=1$` by definition. 
* The [Euler function][bookofproofs$8117] `$\phi:\mathbb N\to\mathbb N$` is multiplicative. The argument for this proposition is the following: 
   * For any number `$n\ge 1$`, there are `$\phi(n)$` numbers co-prime to `$n$` among the numbers `$1,\ldots,n$`, also `$\phi(n)$` numbers co-prime to `$n$` among the numbers `$n+1,\ldots,2n$`, also `$\phi(n)$` numbers co-prime to `$n$` among the numbers `$2n+1,\ldots,3n,$` also `$\phi(n)$` numbers co-prime to `$n$` among the numbers `$3n+1,\ldots,4n,$` etc.
   * If we have `$m\ge 1$` and want count the numbers co-prime to `$nm$` among the numbers `$1,\ldots,nm$` then we shall start with counting the `$m\cdot \phi(n)$` numbers co-prime to `$n$` among the numbers `$1,\ldots,nm$` and then remove those numbers, which are multiples of `$m$`. 
   * This is equivalent to saying that `$\phi(n)\cdot \phi(m)$` is the count of the numbers `$1,\ldots,nm$` which are co-prime to both, `$n$` and `$m$`. This, by definitions, equals `$\phi(nm).$`
