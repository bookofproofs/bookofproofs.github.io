layout: proposition
categories: branches,number-theory
nodeid: bookofproofs$8191
orderid: 500
parentid: bookofproofs$8195
title: A Necessary Condition for an Integer to be Prime
description: A NECESSARY CONDITION FOR AN INTEGER TO BE PRIME &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: condition,integer,necessary,prime
contributors: bookofproofs

---
The following proposition provides a basis for testing if an integer is a prime number. By [contraposition][bookofproofs$1330] to the corollary, if `$a^{p-1}(p)\not\equiv 1(p)$` for some integer `$a$` with `$p\not\mid a,$` then `$p$` is _not_ a [prime number][bookofproofs$473]. It, therefore, suffices to find _any_ number `$a$` with `$p\not\mid a$` to prove that `$p$` is not prime. On the other hand, to prove that `$p$` _is_ prime, we need to show that `$a^{p}(p)\equiv 1(p)$` for all integers `$a$` with `$1 < a < p.$` Therefore, this kind of prooving the primality of `$p$` is not efficient, if `$p$` is big. Later, we will learn about more efficient proofs of primality than this one.

---

For any [integer][bookofproofs$844] `$a\in\mathbb Z$` and any [prime number][bookofproofs$473] `$p$` the following [congruence][bookofproofs$8154] holds:

`$$a^p\equiv a(p).$$`

If `$p\not\mid a$` ($p$ does not [divide][bookofproofs$700] `$a$`) then `$$a^{p-1}(p)\equiv 1(p).$$`
