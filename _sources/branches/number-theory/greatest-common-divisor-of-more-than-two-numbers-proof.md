layout: proof
categories: branches,number-theory
nodeid: bookofproofs$8123
orderid: 50
parentid: bookofproofs$8122
title: 
description:  Proof of GREATEST COMMON DIVISOR OF MORE THAN TWO NUMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: common,divisor,greatest,more,numbers,than,two,proof
contributors: bookofproofs

---


---

* Let `$a,b,c\in\mathbb Z$` be [integers][bookofproofs$844].
* The [commutativity][bookofproofs$672] of `$\gcd$` follows immediatly from the definition of the [greatest common divisor][bookofproofs$1280] because of the [associativity of conjunction][bookofproofs$1834]; i.e. since `$d\mid a\wedge d\mid b$` if and only if  `$d\mid b\wedge d\mid a,$` the sets `$D_{a,b}$` and `$D_{b,a}$` are equal and have the same [maximum][bookofproofs$7995].
* The [associativity][bookofproofs$668] of `$\gcd$` can be understood as follows:
   * If `$t$` is a [divisor][bookofproofs$700] of both, `$t\mid \gcd(a,b)$` and `$t\mid c,$` then `$t\mid \gcd(\gcd(a,b),c)).$` Moreover, `$t\mid a$` and `$t\mid b.$`
   * Therefore, `$t$` is also divisor of both, `$t\mid a$` and `$t\mid \gcd(b,c).$` Thus `$t$` divides `$t\mid \gcd(a,\gcd(b,c))$`
   * Since this reasoning holds for _any_ common divisor of `$t\mid a,$` `$t\mid b,$` and `$t\mid c,$` it follows `$\gcd(\gcd(a,b),c))=\gcd(a,\gcd(b,c)).$` 
* Since `$\gcd$` is both, commutative and associative, the notation `$\gcd(a,b,c)$` makes sense.
* By [induction][bookofproofs$657] over `$k,$` the formula `$\gcd(n_1,\ldots,n_k)=\gcd(\gcd(n_1,\ldots,n_{k-1}),n_k)$` follows.
