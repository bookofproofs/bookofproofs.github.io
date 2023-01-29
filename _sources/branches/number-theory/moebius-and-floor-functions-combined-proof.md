layout: proof
categories: branches,number-theory
nodeid: bookofproofs$8145
orderid: 50
parentid: bookofproofs$8144
title: 
description:  Proof of MöBIUS AND FLOOR FUNCTIONS COMBINED &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: combined,floor,functions,moebius,proof
contributors: bookofproofs

---


---

* Let `$x \ge 1$` be a [real number][bookofproofs$1105].
* Applying the proposition about the [sum of Möbius function over divisors][bookofproofs$8142] for `$n=1,2,\ldots,\lfloor x\rfloor$` and [adding up][bookofproofs$261] all results gives us
`$$1=\sum_{n=1}^{\lfloor x\rfloor}\sum_{d\mid n}\mu(d)=\sum_{d=1}^{\lfloor x\rfloor}\left\lfloor \frac xd\right\rfloor\mu(d).$$`
* In the last step we have used that there are exactly `$\left\lfloor \frac xd\right\rfloor$` [multiples of `$d$` less than `$x$`][bookofproofs$8107] and therefore the inner sum can be replaced[^1] by weighting the [Möbius function][bookofproofs$8116] `$\mu(d)$` by `$\left\lfloor \frac xd\right\rfloor.$`
