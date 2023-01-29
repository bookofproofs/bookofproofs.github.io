layout: proof
categories: branches,number-theory
nodeid: bookofproofs$799
orderid: 50
parentid: bookofproofs$8098
title: 
description:  Proof of EXISTENCE OF PRIME DIVISORS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$696
keywords: divisors,existence,prime,proof
contributors: bookofproofs

---


---

* Trivially, every prime divides the integer `$0.$` Also, because with every divisor `\(d\mid n\)` it is also true that `\(d\mid -1\)`, it is sufficient to show the existence of prime divisors for [natural numbers][bookofproofs$718] `\(n > 1\)`, instead of [integers][bookofproofs$844] `\(n\neq\pm 1\)`. 
* Let `\(D(n):=\{d\in\mathbb N:b>1,~d\mid n\}\)` be the set of all divisors of `\(n\)`. 
* `\(D(n)\)` is not empty, since `\(n\in D(n)\)`. 
* Therefore, according to the [well-ordering principle][bookofproofs$698], `\(D(n)\)` must have a smallest element, which we denote by `\(p\)`. 
* By construction, `\(p > 1\)`.
* We will now show that `\(p\)` is a [prime number][bookofproofs$493].
   * For if it was [composite][bookofproofs$8097], then it would have a non-trivial divisor `\(q\mid p\)`, i.e. a divisor with `\(1 < q < p\)`.
   * Because `\(q\mid p\)` and `\(p\mid n\)`, it would follow from the [divisibility laws][bookofproofs$508] that `\(q\mid n\)` and so `\(q\in D(n)\)`. 
   * This is a [contradiction][bookofproofs$744] to the minimality of `\(p\)` in `\(D(n)\)`. 
   * Therefore, `\(p\)` must be prime.
