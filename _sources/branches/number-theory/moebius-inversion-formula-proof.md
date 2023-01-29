layout: proof
categories: branches,number-theory
nodeid: bookofproofs$8150
orderid: 50
parentid: bookofproofs$8149
title: 
description:  Proof of MöBIUS INVERSION FORMULA &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: formula,inversion,moebius,mobius inversion formula proof,mobius inversion formula,inversion formula,mobius inversion,moebius inversion formula,proof
contributors: bookofproofs

---


---

* By assumptions, `$\alpha,\beta$` are [arithmetic functions][bookofproofs$232] with `$\beta(n)=\sum_{d\mid n}\alpha(d).$`
* For any [divisor][bookofproofs$700] `$d\mid n$` we have, therefore, `$$\beta\left(\frac nd\right)=\sum_{b\mid \frac nd}\alpha(b).$$`
* Multiplying both sides of the equation by the [Möbius function][bookofproofs$8116] of `$\mu(d)$` results in
`$$\mu(d)\beta\left(\frac nd\right)=\sum_{b\mid \frac nd}\mu(d)\alpha(b).$$`
* The [sum][bookofproofs$261] over all divisors `$d\mid n$` results in
`$$\sum_{d\mid n}\mu(d)\beta\left(\frac nd\right)=\sum_{d\mid n}\sum_{b\mid \frac nd}\mu(d)\alpha(b)=\sum_{b\mid n}\sum_{d\mid \frac nb}\mu(d)\alpha(b).$$`
* In the last step, we could exchange the indices `$d$` and `$b$` because as the index `$b$` runs through all divisors `$b\mid \frac nd$` so does `$d$` run through all [complementary divisors][bookofproofs$700] `$d\mid \frac nb.$`
* Now, the term `$\alpha(b)$` does not depend on the index `$d$` of the inner sum and we can use the [distributivity law][bookofproofs$520] to get
`$$\sum_{b\mid n}\sum_{d\mid \frac nb}\mu(d)\alpha(b)=\sum_{b\mid n}\alpha(b)\sum_{d\mid \frac nb}\mu(d).$$`
* The last sum can be significantly simplified using the [sum of Möbius function over divisors][bookofproofs$8142] and we get
`$$\sum_{b\mid n}\alpha(b)\sum_{d\mid \frac nb}\mu(d)=\sum_{b\mid n}\alpha(b)[b=n]=\alpha(n).$$`
* We have shown 
`$$\alpha(n)=\sum_{d\mid n}\mu(d)\beta\left(\frac nd\right).$$`
