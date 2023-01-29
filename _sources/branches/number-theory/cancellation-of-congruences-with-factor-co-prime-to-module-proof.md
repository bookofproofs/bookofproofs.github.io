layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3513
orderid: 50
parentid: bookofproofs$8161
title: 
description: PROOF OF CANCELLATION OF CONGRUENCES WITH FACTOR CO-PRIME TO MODULE, FIELD $\MATHBB Z_P$ &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$1272,bookofproofs$8189
keywords: cancellation,congruences,factor,module,prime,proof
contributors: bookofproofs

---


---

* Let `$m > 1$` be a [positive integer][bookofproofs$1075] and `$a,b,c$` be [integers][bookofproofs$844].
* By hypothesis, we have `$m\mid (ac-bc)=c(a-b).$`
* Also by hypothesis, `$c$` and `$m$` are [co-prime][bookofproofs$8093], therefore from [divisors of a product of two factors, co-prime to one factor][bookofproofs$1293], it follows that `$m\mid (a-b).$`
* Therefore `$a(m)=b(m).$`
* It remains to be shown that if `$m=p$` is a [prime number][bookofproofs$473], then `$\mathbb Z_p$` is a [finite][bookofproofs$985] [field][bookofproofs$557].
   * We have seen that `$Z_p$` is a [commutative ring][bookofproofs$8156].
   * If for two elements `$a(p),b(p)$` we have `$a(p)\cdot b(p)\equiv 0(p),$` then we have `$p\mid ab.$` 
   * From the [Euclidean lemma][bookofproofs$1298], it follows that `$p\mid a$` or `$p\mid b.$` 
   * Therefore `$a(p)=0(p)$` or `$b(p)=0(p).$`
   * Thus, `$\mathbb Z_p$` is a commutative ring with `$0(p)$` as its only [zero divisor][bookofproofs$821], in other words it is a [integral domain][bookofproofs$821].
   * Since [finite integral domains are fields][bookofproofs$8222], `$\mathbb Z_p$` is [finite][bookofproofs$985] [field][bookofproofs$557].
* In particular, for every nonzeror `$a(p)\in\mathbb Z_p,$` there is an multiplicative [inverse][bookofproofs$670] element `$a^{-1}(p)\in\mathbb Z_p$` and the congruence `$(ax)(p)\equiv b(p)$` has the unique solution `$x(p)\equiv (b\cdot a^{-1})(p).$`
