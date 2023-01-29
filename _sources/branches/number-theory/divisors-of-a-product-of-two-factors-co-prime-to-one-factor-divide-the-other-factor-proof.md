layout: proof
categories: branches,number-theory
nodeid: bookofproofs$1294
orderid: 50
parentid: bookofproofs$1293
title: 
description:  Proof of DIVISORS OF A PRODUCT OF TWO FACTORS, CO-PRIME TO ONE FACTOR DIVIDE THE OTHER FACTOR &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$1272
keywords: divide,divisors,factor,factors,one,other,prime,product,two,proof
contributors: bookofproofs

---


---

* By hypothesis, we have `\(a\neq 0\)`, because `\(a\mid bc\)`, i.e. `\(a\)` [divides][bookofproofs$700] the product of the [integers][bookofproofs$844] `\(b\)` and `\(c\)`. Also by hypothesis, we have that `\(a\)` and `\(b\)` are [co-prime][bookofproofs$8093]. This means by definition that `\(\gcd(a,b)=1\)`. We have to prove that `\(a\mid c\)`.
* We inspect two cases:
   * Case `\((1)\)` `\(b=0\)`.
      * If `\(b=0\)`, then `\(a=\pm 1\)` because of  `\(\gcd(a,b)=1\)`. Therefore, `\(a\)` is a [trivial divisor][bookofproofs$700] of `\(c\)`. 
   * Case `\((2)\)` `\(b\neq 0\)`.
      * For the [least common multiple][bookofproofs$1276] of the natural numbers `\(|a|\)` and `\(|b|\)`[^1], it follows from the [relationship between the greatest common divisor and the least common multiple][bookofproofs$1281] that `$\operatorname{lcm}(|a|,|b|)=|a|\cdot |b|.$`
      * On the other hand, by hypothesis, we have that `\(bc\)` is a [multiple][bookofproofs$700] of `\(|a|\)` and, trivially, `\(bc\)` is a multiple of `\(|b|\)`. 
      * Thus, `\(bc\)` is a [common multiple][bookofproofs$1276] of `\(|a|\)` and `\(|b|\)`. 
      * Because the [least common multiple divides any common multiple][bookofproofs$1276], we have that `$\operatorname{lcm}(|a|,|b|)\mid bc\Rightarrow|a||b|\mid bc.$`
      * By the [definition of divisors][bookofproofs$700], this is equivalent to `$ab\mid bc,$` and from the [divisibility law no. 7][bookofproofs$508], it follows that `$a\mid  c.$` 

[^1]: Note that the [absolute values of integers][bookofproofs$1080] are [natural numbers][bookofproofs$718].