layout: proposition
categories: branches,number-theory
nodeid: bookofproofs$1276
orderid: 800
parentid: bookofproofs$77
title: Least Common Multiple
description: LEAST COMMON MULTIPLE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: common,least,multiple
contributors: bookofproofs

---
It is a known result from [set theory][bookofproofs$27] that in contrast to the ordered set of integers `$(\mathbb Z,\le)$`, the ordered set of natural numbers `$(\mathbb N,\le)$` is [well-ordered][bookofproofs$7997]. This property of natural numbers ensures the existence of a [smallest element][bookofproofs$7995] in any non-empty subset of natural numbers. The existence is very useful in the study of divisibility, therefore, in the following, we will restrict our concept of divisibility to natural numbers only.

---

Let `\(a, b\in\mathbb Z\)` be [integers][bookofproofs$844] and let `\(M_{a,b}\)` be the [set][bookofproofs$550] of all **common multiples** of `\(a\)` and `\(b\)`:

`\[M_{a,b}:=\left\{m\in\mathbb Z : a\mid m\wedge b\mid m\right\}.\]`

`\(M_{a,b}\)` has a [minimum][bookofproofs$7995] `$\min(M_{a,b})$`, called the **least common multiple** of `\(a\)` and `\(b\)`, denoted by 

`\[\operatorname{lcm}(a,b):=\min(M_{a,b}).\]`

Moreover, `$\operatorname{lcm}(a,b)\mid m\in M_{a,b}$`, i.e. `\(\operatorname{lcm}(a,b)\)` is a [divisor][bookofproofs$700] of any other common multiple of `\(a\)` and `\(b\)`.
