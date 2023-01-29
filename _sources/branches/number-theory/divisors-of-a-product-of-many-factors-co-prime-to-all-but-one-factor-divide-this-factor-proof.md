layout: proof
categories: branches,number-theory
nodeid: bookofproofs$1301
orderid: 50
parentid: bookofproofs$1295
title: 
description:  Proof of DIVISORS OF A PRODUCT OF MANY FACTORS, CO-PRIME TO ALL BUT ONE FACTOR, DIVIDE THIS FACTOR &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$1272
keywords: all,but,divide,divisors,factor,factors,many,one,prime,product,this,proof
contributors: bookofproofs

---


---

* The case `$n=2$` was proven in the [proposition about divisors of a product of two factors co-prime to one factor][bookofproofs$1293].
* Let `\(n > 2\)`. If
`\[a\mid \prod_{\nu=1}^n a_\nu,\]`
then it follows from `\( a\perp a_\nu,\quad 1\le \nu < n,\)` in particular, that `\(a\)` and `\(a_1\)` are [co-prime][bookofproofs$1288], i.e. `\(\gcd(a,a_1)=1\)`. 
* Therefore, any common divisor other of `\(a\)` and `\(\prod_{\nu=1}^n a_\nu\)` other than `\(1\)` must be also a common divisor of `\(a\)` and `\(\prod_{\nu=2}^n a_\nu\)`, i.e. the product in which we left the first factor `\(a_1\)`. 
* Thus, it follows that 
`\[a\mid \prod_{\nu=2}^n a_\nu.\]`
* With the same argument, since `\(\gcd(a,a_2)=1\)`, we can remove `\(a_2\)` from the product and still conclude that
`\[a\mid \prod_{\nu=3}^n a_\nu.\]`
* The same reasoning and the same procedure can be repeated for all `\(\nu=1,\ldots,n\)`, until we get
`\[a\mid \prod_{\nu=n-1}^n a_\nu,\]`
and finally, after the removal of `\(a_{n-1},\)`
`\[a\mid a_n.\]`
