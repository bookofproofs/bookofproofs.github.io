layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3547
orderid: 50
parentid: bookofproofs$8208
title: 
description: PROOF OF GAUSSIAN LEMMA NUMBER THEORY &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: gaussian,lemma,number,theory,proof
contributors: bookofproofs

---


---

* By hypothesis, `$p > 2$` is an [odd][bookofproofs$8130] [prime number][bookofproofs$473] and `$n$` is an [integer][bookofproofs$844] not [divisible][bookofproofs$700] by `$p.$` 
* First of all, we observe that according to [creation of complete residue systems from others][bookofproofs$8175] the [congruence classes][bookofproofs$8154] `$ n,2n,3n,\dots ,{\frac  {p-1}{2}}n\mod p$` are all distinct and `$ > 0$` as well as `$ < p.$` 
* Therefore, indeed, there are `$\frac {p-1}2$` of them.
* Let `$m\ge 0$` be the number of residues `$ > \frac p2.$`
* If `$m > 0,$` let `$b_1,\ldots,b_m$` denote the residues `$ > \frac p2.$`
* Correspondingly, by setting `$l:=\frac {p-1}2-m,$` which is the number of residues `$ < \frac p2,$` we denote them by `$a_1,\ldots,a_l.$` 
* [Multiplying][bookofproofs$8157] all `$\frac{p-1}2$` residues with each other, we get the congruence[^1] `$$\prod_{s=1}^l a_s\prod_{t=1}^m b_t\equiv \prod_{h=1}^{\frac{p-1}2}hn\equiv \left(\frac{p-1}2\right)!\;\;n^{\frac{p-1}2}\mod p.$$`
* We now observe that the numbers `$p-b_t$` lie all between `$1$` and `$\frac {p-1}2$` and all these differences are distinct, since all `$b_t$` are distinct. 
* Moreover, each `$a_s$` is different from each `$p-b_t.$` We prove this result by [contradiction][bookofproofs$744]:
   * Assume `$a_s=p-b_t$` for some indices `$s,t.$`
   * Then there would be integers `$x,y$` with `$1\le x,y\le\frac{p-1}2$` and `$(xn)(p)\equiv (p-yn)(p).$`
   * From this, it would follow `$(xn)(p)\equiv (-yn)(p),$` or `$x(p)\equiv -y(p),$` by [congruence modulo a divisor][bookofproofs$8171].
   * But `$p\mid (x+y)$` contradicts `$0 < x+y < p.$`
* It follows that `$a_s$` and `$p-b_t$` are disjoint for all indices `$s,t$`. In other words, they form together the numbers `$1,\ldots,\frac{p-1}2$` (possibly re-ordered). 
* Therefore, we have 
`$$\left(\frac{p-1}2\right)!\equiv \prod_{s=1}^l a_s\prod_{t=1}^m (p-b_t)\equiv (-1)^m\prod_{s=1}^l a_s\prod_{t=1}^m b_t\equiv (-1)^m\left(\frac{p-1}2\right)!\;\;n^{\frac{p-1}2}\mod p.$$`
* By [congruence modulo a divisor][bookofproofs$8171], we get finally the congruence `$$1\equiv (-1)^m\cdot n^{\frac{p-1}2}\mod p.$$`
* The [Euler's criterion for quadratic residues][bookofproofs$8201] gives us `$\left(\frac np\right)\equiv(-1)^m\mod p.$`
* Therefore, `$\left(\frac np\right)=(-1)^m,$` for the [Legendre symbol][bookofproofs$8198] `$\left(\frac np\right),$` as required.

[^1]: In this congruence, `$\left(\frac{p-1}2\right)!$` denotes the the [factorial][bookofproofs$1005] of `$\left(\frac{p-1}2\right).$`
