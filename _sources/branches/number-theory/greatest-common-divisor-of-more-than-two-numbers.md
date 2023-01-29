layout: proposition
categories: branches,number-theory
nodeid: bookofproofs$8122
orderid: 1200
parentid: bookofproofs$77
title: Greatest Common Divisor of More Than Two Numbers
description: GREATEST COMMON DIVISOR OF MORE THAN TWO NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: common,divisor,greatest,more,numbers,than,two
contributors: bookofproofs

---


---

Let `$n_1,n_1,\ldots,n_k\in\mathbb Z$` be [integers][bookofproofs$718]. The simultanous [greatest common divisor][bookofproofs$1280] of all these numbers can be calculated by the recursive formula

`$$\gcd(n_1,\ldots,n_k):=\gcd(\gcd(n_1,\ldots,n_{k-1}),n_k).$$`

This calculation is independent of the order, in which the recursive formula is used, following the [associativity][bookofproofs$668] and [commutativity][bookofproofs$672] of the `$\gcd$`. In particular, for any [integers][bookofproofs$844] `$a,b,c\in\mathbb Z$` we have
`$$\gcd(\gcd(a,b),c))=\gcd(a,\gcd(b,c))$$`
and
`$$\gcd(a,b)=\gcd(b,a).$$`
