layout: proposition
categories: branches,number-theory
nodeid: bookofproofs$8161
orderid: 200
parentid: bookofproofs$8172
title: Cancellation of Congruences With Factor Co-Prime To Module, Field `$\mathbb Z_p$`
description: CANCELLATION OF CONGRUENCES WITH FACTOR CO-PRIME TO MODULE, FIELD Zp &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272,bookofproofs$8152,bookofproofs$8189
keywords: cancellation,congruences,factor,module,prime
contributors: bookofproofs

---
Unlike [addition, subtraction and multiplication of congruences][bookofproofs$8156], there is no general way to divide [congruences][bookofproofs$8155]. The reason for this is the following: We can have two [congruence classes][bookofproofs$8154] `$a(m),b(m)\in\mathbb Z_m$`, both unequal zero: `$a(m)\not\equiv 0(m),$` and `$b(m)\not\equiv 0(m),$` but their product is zero: `$a(m)\cdot b(m)\equiv 0(m).$` Take for example `$6(15)\cdot 5(15)\equiv 0(15).$` We say that `$(Z_m,\cdot,+)$` has [zero divisors][bookofproofs$821].
However, in some cases, we can simplify a given congruence `$ac(m)\equiv bc(m)$` by canceling out the factor `$c$`. The following proposition shows that this is only possible if `$c$` and the module `$m$` are [co-prime][bookofproofs$8093].
---

Let the `$a,b,c$` be [integers][bookofproofs$844], and `$m > 1$` be a [positive integer][bookofproofs$1075] and let `$c\perp m$` be [co-prime][bookofproofs$8093]. Then, from the equaility of the [congruences][bookofproofs$8154] `$$(ac)(m)\equiv (bc)(m)$$` it follows that `$$a(m)\equiv b(m).$$`

In particular, if `$m=p$` is a [prime number][bookofproofs$473], then `$\mathbb Z_p$` is a ([finite][bookofproofs$985]) [field][bookofproofs$557] and the congruence `$ax(p)\equiv b(p)$` is solvable, if `$a\perp p,$` and has the unique solution `$x(p)\equiv b\cdot a^{-1}(p).$`

### Notes

* see [calculation of inverses modulo a number][bookofproofs$8224] algorithm
