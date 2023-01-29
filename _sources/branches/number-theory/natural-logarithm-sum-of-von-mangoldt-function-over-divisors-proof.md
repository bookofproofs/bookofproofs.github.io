layout: proof
categories: branches,number-theory
nodeid: bookofproofs$8119
orderid: 50
parentid: bookofproofs$8118
title: 
description:  Proof of NATURAL LOGARITHM SUM OF VON MANGOLDT FUNCTION OVER DIVISORS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: divisors,function,logarithm,mangoldt,natural,over,sum,von,von mangoldt function,proof
contributors: bookofproofs

---


---

* Let `$n\in\mathbb N,$` `$n > 0.$`
* If `$n=1$`, then the [sum][bookofproofs$261] `$( * )$` is empty and we have the correct equation `$0=0.$`
* If `$n > 1,$` consider the [canonical representation][bookofproofs$803] `$$n=\prod_{i=1}^\infty p_i^{e_i}=\prod_{p\mid n}p^e\quad ( * * )$$`
where the second product is built for all primes [dividing][bookofproofs$700] `$n$` and the exponent `$e$` depends on both, `$n$` and the particular [prime number][bookofproofs$473] `$p$` in the product.
* Taking the [natural logarithm][bookofproofs$1421] on both sides of `$( * * )$` we get
`$$\log(n)=\sum_{p\mid n}e\cdot \log(p)=\sum_{p\mid a}(\Lambda(p)+\Lambda(p^2)+\ldots+\Lambda(p^e))=\sum_{d\mid n}\Lambda(d).$$`
* This is the required [sum][bookofproofs$261] of the [von Mangoldt function][bookofproofs$702] over all [divisors][bookofproofs$700] of `$n.$`
