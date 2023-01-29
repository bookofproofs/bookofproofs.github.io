layout: proposition
categories: branches,number-theory
nodeid: bookofproofs$8134
orderid: 300
parentid: bookofproofs$427
title: Even Perfect Numbers
description: EVEN PERFECT NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: even,numbers,perfect
contributors: bookofproofs

---


---

The number `$n:=\frac{p+1}2p=2^{k-1}(2^k-1)$` is an [even][bookofproofs$8130] [perfect number][bookofproofs$8131], if and only if `$p$` is a [prime number][bookofproofs$473] having the form `$p=2^k-1$` for an `$k > 1, k\in\mathbb N.$`

### Examples

We calculate some different cases:

#### `$k=2$`:

* `$p=2^2-1=3$`, `$n=2^1(2^2-1)=2\cdot 3=6\Longleftrightarrow 6$` is a perfect number.

#### `$k=3$`

* `$p=2^3-1=7$`, `$n=2^2(2^3-1)=4\cdot 7=28\Longleftrightarrow 28$` is a perfect number.

#### `$k=4$`

* `$p=2^4-1=15$` is not a prime number and `$n=2^3(2^4-1)=8\cdot 15=120$` is not(!) a perfect number.

#### `$k > 1$`, `$k$` composite

* In general, `$2^k-1$` never can be prime, if `$k$` is not prime. 
* Since if `$k$` is [composite][bookofproofs$8097], then `$k=bc$` for some `$b > 1$` and `$c > 1$`. 
* But then `$$2^k-1=2^{bc}-1=(2^b-1)(2^{b(c-1)}+2^{b(c-2)}+\ldots+2^{b}+1),$$` and both factors are `$ > 1.$`
* Therefore, the search for even perfect numbers should be restricted to prime numbers `$k$`.

#### `$k=5$`

* `$p=2^5-1=31$` `$n=2^4(2^5-1)=16\cdot 31=496\Longleftrightarrow 496$` is a perfect number.

#### Other cases and notes

Further perfect numbers can be found for the prime numbers `$k=7\Rightarrow n=8128$`, `$k=13\Rightarrow n=33550336,$` etc.

Although perfect numbers and the above elementary result have been known for at least 2500 years (see [Prop. 9.36 in Euclid's Elements][bookofproofs$2080]), still unsolved mathematical problems are:
* [Are there infinitely many even perfect numbers][bookofproofs$8132].
* [Existence of odd perfect numbers][bookofproofs$8133].