layout: proof
categories: branches,analysis
nodeid: bookofproofs$8377
orderid: 50
parentid: bookofproofs$457
title: 
description: PROOF OF GAMMA FUNCTION ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$586
keywords: gamma function,gamma functions,gamma,proof
contributors: bookofproofs

---


---

* Let `$x > 0$` be a [real number][bookofproofs$1105] and the [improper integral][bookofproofs$8343] `$\int_0^\infty \exp(-t)t^{x-1}dt$` be given.
* By [definition of improper integral][bookofproofs$8343], `$$\int_0^\infty \exp(-t)t^{x-1}dt=\underbrace{\int_{0}^1 \exp(-t)t^{x-1}dt}_{=:J_1}+\underbrace{\int_{1}^\infty \exp(-t)t^{x-1}dt}_{=:J_2}.$$`
* Because [$\exp(0)=1$][bookofproofs$1423], we get `$$\lim_{t\searrow 0}\frac{\exp(-t)t^{x-1}}{\frac{1}{t^{1-x}}}=\lim_{t\searrow 0}\frac{\exp(-t)t^0}{1}=1.$$`
* Using the [limit comparizon test][bookofproofs$8350], the [Riemann integral][bookofproofs$1763]  `$J_1$` is convergent if and only if this one does: `$$\int_{0}^1 \frac{1}{t^{1-x}}dt,$$` which is the case for any fixed `$x > 0.$` 
* On the other hand, for all `$x$` we have `$$\lim_{t\to\infty }\frac{\exp(-t)t^{x-1}}{\frac{1}{t^2}}=\lim_{t\to\infty}\frac{\exp(-t)t^{x+1}}{1}=0.$$`
* Using the limit comparizon test once again, the [improper integral][bookofproofs$8343] `$J_2$` is convergent since this one does: `$$\int_{1}^\infty \frac{1}{t^2}dt,$$` which is convergent for all `$x$` (in fact, this integral does not depend on `$x$` at all).
* Altogether, the improper integral of the sum `$J_1+J_2$` is convergent if and only if `$x > 0.$`
