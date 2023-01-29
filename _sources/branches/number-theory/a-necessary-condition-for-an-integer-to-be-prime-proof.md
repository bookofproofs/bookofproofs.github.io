layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3536
orderid: 50
parentid: bookofproofs$8191
title: 
description:  Proof of A NECESSARY CONDITION FOR AN INTEGER TO BE PRIME &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272
keywords: condition,integer,necessary,prime,proof
contributors: bookofproofs

---


---

* According to the [explicit formula for the Euler function][bookofproofs$2790], we have `$\phi(p)=p-1$` for any [prime number][bookofproofs$473] `$p.$`
* Note that if `$p$` is not a [divisor][bookofproofs$700] of `$a$` then both are [co-prime][bookofproofs$8093].
* Therefore, `$a^{p-1}(p)\equiv 1(p)$` follows immediately from [Fermat's little theorem][bookofproofs$8190] for a prime module.
* [Multiplying][bookofproofs$8156] both sides gives us the [congruence][bookofproofs$8154] with `$a^p(p)\equiv a(p).$` 
* If `$p\mid a,$` then trivially `$a^p(p)\equiv 0(p)\equiv a(p).$` 
* Therefore, the congruence `$a^p(p)\equiv a(p)$` holds for all prime numbers `$p$` and all integers `$a,$` (i.e. no matter if `$p\mid a$` or `$p\not\mid a$`).
