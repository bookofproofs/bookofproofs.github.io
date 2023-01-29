layout: proof
categories: branches,number-theory
nodeid: bookofproofs$1287
orderid: 50
parentid: bookofproofs$1280
title: Commutativity of the Greatest Common Divisor
description:  Proof of GREATEST COMMON DIVISOR &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: common,divisor,greatest,proof
contributors: bookofproofs

---


---

* Assume `\(a,b\)` are [integers][bookofproofs$844] and `\(D_{a,b}\)` is a [set][bookofproofs$550] defined by `$D_{a,b}:=\left\{d\in\mathbb Z : d\mid a\wedge d\mid b\right\}.$` 
* `$\mathbb N\cap D_{a,b}$` is not empty, since it contains e.g. the number `\(1.\)` 
* Moreover, `$\mathbb N\cap D_{a,b}$` is [finite][bookofproofs$985], since it is the [subset of the intersection][bookofproofs$6834] of the sets of [natural numbers][bookofproofs$718] `$\mathbb N$`, the set of divisors `$D_a$` of `$a$` and the set of divisors `$D_b$` of `$b$`, both intersections `$\mathbb N\cap D_a$` and `$\mathbb N\cap D_b$` have only a [finite number of divisors][bookofproofs$1278] and any [subset of a finite set is finite][bookofproofs$986].
* From the [existence and uniqueness of a maximum in subsets of natural numbers][bookofproofs$1436] it follows that `$\mathbb N\cap D_{a,b}$` contains a [maximum][bookofproofs$7995] `\(m_0\)`. 
* Thus, `$\gcd(a,b):=m_0$` exists and is unique.
* It is clear that `$\gcd(a,b)\mid a$` and `$\gcd(a,b)\mid b$`, since `$\gcd(a,b)\in D_{a,b}.$` 
* It remains to be shown that other common divisor `\(d\in D_{a,b}\)` [divides][bookofproofs$700] the greatest common divisor, i.e. we have `$d\mid \gcd(a,b)$` for all `$d\in D_{a,b}.$`
   * From `$d\mid a$` and `$d\mid b$` it follows that `$a\mid a\frac{b}{d}$` and `$b\mid b\frac{a}{d}.$`
   * This means that `$\frac{ab}d$` is a [common multiple][bookofproofs$1276] of `$a$` and `$b.$` 
   * Let `$m:=\frac{ab}{\gcd(a,b)}$`, i.e. `$ab=m\gcd(a,b).$` 
   * Therefore, since `$m\mid ab$` it follows even `$m\mid \frac{ab}d$` since `$\frac{ab}d$` is a [common multiple][bookofproofs$1276] of `$a$` and `$b.$`
   * This is equivalent to `$\frac{ab}{\gcd(a,b)}\mid \frac{ab}d$`, therefore the number `$\frac{\gcd(a,b)}{d}$` is an integer. 
   * This shows that `$d\mid\gcd(a,b).$`
