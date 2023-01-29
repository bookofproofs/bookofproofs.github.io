layout: proposition
categories: branches,number-theory
nodeid: bookofproofs$8124
orderid: 1300
parentid: bookofproofs$77
title: Least Common Multiple of More Than Two Numbers
description: LEAST COMMON MULTIPLE OF MORE THAN TWO NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: common,least,more,multiple,numbers,than,two
contributors: bookofproofs

---


---

Let `$n_1,n_1,\ldots,n_k\in\mathbb Z$` be [integers][bookofproofs$718]. The simultanous [least common multiple][bookofproofs$1276] of all these numbers can be calculated by the recursive formula

`$$\operatorname{lcm}(n_1,\ldots,n_k):=\operatorname{lcm}(\operatorname{lcm}(n_1,\ldots,n_{k-1}),n_k).$$`

This calculation is independent of the order, in which the recursive formula is used, following the [associativity][bookofproofs$668] and [commutativity][bookofproofs$672] of the `$\operatorname{lcm}$`. In particular, for any [integers][bookofproofs$844] `$a,b,c\in\mathbb Z$` we have
`$$\operatorname{lcm}(\operatorname{lcm}(a,b),c))=\operatorname{lcm}(a,\gcd(b,c))$$`
and
`$$\operatorname{lcm}(a,b)=\operatorname{lcm}(b,a).$$`
