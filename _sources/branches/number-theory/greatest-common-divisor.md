layout: proposition
categories: branches,number-theory
nodeid: bookofproofs$1280
orderid: 900
parentid: bookofproofs$77
title: Greatest Common Divisor
description: GREATEST COMMON DIVISOR &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: common,divisor,greatest
contributors: bookofproofs

---


---

Let `\(a,b\)` be [integers][bookofproofs$844] and let `\(D_{a,b}\)` be the [set][bookofproofs$550] of all **common divisors** of `\(a\)` and `\(b\)`:

`\[D_{a,b}:=\left\{d\in\mathbb Z : d\mid a\wedge d\mid b\right\}.\]`

`\(D_{a,b}\)` has a unique [maximum][bookofproofs$7995] `$\max(D_{a,b})$`, called the **greates common divisor** of `\(a\)` and `\(b\)`, denoted by 

`\[\gcd(a,b):=\max(D_{a,b}).\]`

We have `$\gcd(a,b)\mid a$` and `$\gcd(a,b)\mid b.$` Moreover, any divisor `$d$` [dividing][bookofproofs$700] both, `$d\mid a$` and `$d\mid b$` also divides their greatest common divisor `$d\mid \gcd(a,b).$` For this reason, since `$d\mid 0$` for all integers `$d\neq 0$`, we set `\(\gcd(0,0):=0\)`.

### Note

The [division with quotient][bookofproofs$818] can be used to efficiently calculate the `$\gcd$` of given two integers `$a,b.$` See a [Python implementation of the greatest common divisor algorithm][bookofproofs$503].