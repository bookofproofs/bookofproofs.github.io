layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3525
orderid: 50
parentid: bookofproofs$8176
title: 
description:  Proof of COPRIMALITY AND CONGRUENCE CLASSES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: classes,congruence,coprimality,proof
contributors: bookofproofs

---


---

* By hypothesis, `$m$` is a [positive integer][bookofproofs$1075] and `$a(m)$` is a given [congruence class][bookofproofs$8154].
* Assume, we have two representatives `$a_1,a_2$`, i.e. `$a_1(m)\equiv a_2(m).$`
* By definition, this means `$m\mid (a_1-a_2).$`
* For any [divisor][bookofproofs$700] `$d\mid m$` we have by the [divisibility law no. 3][bookofproofs$508] that `$d\mid (a_1-a_2).$`
* By the [divisibility law no. 9][bookofproofs$508], this is equivalent to `$d\mid a_1$` and `$d\mid a_2.$`
* Therefore, `$d$` is a [common divisor][bookofproofs$1280] of `$m,$` `$a_1$` and `$a_2.$`
* Since the [greatest common divisor][bookofproofs$1280] is unique[^1], it follows `$\gcd(a_1,m)=\gcd(a_2,m).$`
* In particular, this is true if `$a_1\perp m$` and `$a_1\perp m$` are [co-prime][bookofproofs$8093], i.e. `$\gcd(a_1,m)=\gcd(a_2,m)=1.$`
* Therefore, any representative `$a\in\mathbb Z$` of a given congruence class `$a(m)\in\mathbb Z_m$` is either co-prime or not co-prime to `$m.$`


[^1]: Any maximum (the `$\gcd$` is a maximum, by definition) is unique, see [notes on special elements of posets][bookofproofs$7996].