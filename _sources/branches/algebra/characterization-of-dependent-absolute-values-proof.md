layout: proof
categories: branches,algebra
nodeid: bookofproofs$8666
orderid: 50
parentid: bookofproofs$8665
title: 
description: PROOF OF CHARACTERIZATION OF DEPENDENT ABSOLUTE VALUES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6735
keywords: characterization of dependent absolute values,proof
contributors: bookofproofs

---


---

* By hypothesis, `$(F,+,\cdot)$` is a [field][bookofproofs$557] with two [absolute values][bookofproofs$8659] `$|\cdot|_1$` and `$|\cdot|_2$` defined on it. 
* Assume, `$|\cdot|_1$` and `$|\cdot|_2$` are [dependent][bookofproofs$8664] 
* Then for `$x\in F$` we have `$|x|_1 < 1\Longleftrightarrow |x|_2 < 1.$` 
* Let `$x_0\in F$` with `$|x_0|_1 > 1,$` then `$|x_0|_2 > 1.$`
* For an arbitrary `$x\in F$` with `$x\neq 0$`, we have for some [positive real number][bookofproofs$1107] `$\lambda > 0$` `$$|x|_1=|x_0|_1^\lambda.$$`
* For all real numbers `$\epsilon > 0$` we get the approximations `$$|x|_1^{\lambda-\epsilon} < |x_0|_1^\lambda< |x|_1^{\lambda+\epsilon},$$` implying `$$\left|\frac{x^{\lambda-\epsilon}}{x_0^\lambda}\right|_1 < 1 < \left|\frac{x^{\lambda+\epsilon}}{x_0^\lambda}\right|_1.$$` 
* Since `$|\cdot|_1$` and `$|\cdot|_2$` are [dependent][bookofproofs$8664], we get `$$\left|\frac{x^{\lambda-\epsilon}}{x_0^\lambda}\right|_2 < 1 < \left|\frac{x^{\lambda+\epsilon}}{x_0^\lambda}\right|_2,$$` implying `$$|x|_2^{\lambda-\epsilon} < |x_0|_2^\lambda< |x|_2^{\lambda+\epsilon}$$` for all `$\epsilon > 0,$` implying 
`$$|x|_2^{\lambda} = |x_0|_2^\lambda.$$`
* Obviously, `$\lambda$` exists and is a positive real number.
