layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3534
orderid: 50
parentid: bookofproofs$8185
title: 
description:  Proof of COMPLETE AND REDUCED RESIDUE SYSTEMS REVISED &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: complete,residuo,revised,system,proof
contributors: bookofproofs

---


---

By hypothesis, `$a > 0$` and `$b > 0$` are [co-prime][bookofproofs$8093]  [positive integers][bookofproofs$1075].
### Ad 1)

* Assume, `$x$` runs through all values of a [complete residue system modulo `$a$`][bookofproofs$8173] and `$y$` runs through all values of a [complete residue system modulo `$b$`][bookofproofs$8173].
* By assumption, there are `$ab$` numbers of the form `$ax+by.$`
* If for two different pairs `$(x_1,y_1),$` `$(x_2,y_y)$` we have `$(ax_1+by_1)(ab)\equiv (ax_2+by_2)(ab),$` then by [congruence modulo a divisor][bookofproofs$8171] we have `$$\begin{array}{rcl}
(ax_1+by_1)(b)&\equiv&(ax_2+by_2)(b)\\
(ax_1)(b)&\equiv&(ax_2)(b).\\
\end{array}$$`
* By [cancellation of congruences with general factor][bookofproofs$8162], it follows `$x_1(b)\equiv x_2(b).$`
* With a symmetrical argument, it follows `$y_1(a) \equiv y_2(b).$`
* This means that among the `$ab$` different numbers of the form `$ax+by,$` all are incongruent.
* In otherwords, `$ab$` runs through all values of the complete residue system modulo `$ab.$`

### Ad 2)

* Now, assume, `$x$` runs through all values of a [reduced residue system modulo `$a$`][bookofproofs$8174] and `$y$` runs through all values of a [complete residue system modulo `$b$`][bookofproofs$8174].
* If `$x$` and `$b$` are not co-prime, then the [greatest common divisor][bookofproofs$1280] `$\gcd(x,b) > 1.$`
* In this case,  by [divisibility laws][bookofproofs$508] `$\gcd(x,b)\mid (ax+by)$` and `$\gcd(x,b)\mid ab,$` therefore `$\gcd(x,b)\mid \gcd(ax+by,ab).$`  
* Altogether, from `$1 < \gcd(x,b)$` it follows `$\gcd(ax+by,ab) > 1.$`
* With a a symmetrical argument, it follows from  `$1 < \gcd(y,a)$` that `$\gcd(ax+by,ab) > 1.$`
* With 1), it remains to be shown that if `$1 = \gcd(x,b)$` and `$1 = \gcd(y,a),$` then `$\gcd(ax+by,ab) = 1.$`
   * Assume, a [prime number][bookofproofs$473] is a [divisor][bookofproofs$700] `$p\mid \gcd(ax+by,ab).$`
   * Then `$p$` would also divide `$ab$` and without loss of generality `$p\mid a.$`
   * Moreover, `$p$` would also divide `$ax+by,$` and therefore `$p\mid by.$`
   * Finally, because `$\gcd(a,b)$` it would follow `$p\mid y.$` 
   * But this is a contradiction to `$\gcd(y,a)=1.$`
* Therefore `$\gcd(ax+by,ab) = 1.$`
