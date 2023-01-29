layout: proof
categories: branches,analysis
nodeid: bookofproofs$6906
orderid: 50
parentid: bookofproofs$6905
title: 
description: Proof of SQUEEZING THEOREM FOR FUNCTIONS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$6823
keywords: functions,sandwich theorem,scrunch theorem,squeezing,squeezing theorem,theorem,proof
contributors: bookofproofs

---


---

* Let `$D\subseteq\mathbb R$` be a [subset][bookofproofs$552] of [real numbers][bookofproofs$1105].
* Let `$f,g,h:D\to\mathbb R$` be  [functions][bookofproofs$592] with `$g(x)\le f(x)\le h(x)$` for all `$x\in D$`. 
* Let `$g,h$` have a [limit][bookofproofs$6683] `$L$` at `$x=a\in D,$` i.e. `$\lim_{x\to a} g(x)=\lim_{x\to a}h(x)=L.$` 
* Let `$\epsilon > 0$` be given.
* By the [definition of limit][bookofproofs$6683], there is a `$\delta_1 > 0$` such that for all `$x\in D$` with `$0 < |x-a| < \delta_1,$` it follows `$|g(x)-L| < \epsilon.$`
* Similarly, there is a `$\delta_2 > 0$` such that for all `$x\in D$` with `$0 < |x-a| < \delta_2,$` it follows `$|h(x)-L| < \epsilon.$`
* Take the [minimum][bookofproofs$6603] `$\delta:=\min(\delta_1,\delta_2).$`
* For `$x\in D$` with `$0 < |x-a| < \delta,$` it follows  `$|g(x)-L| < \epsilon$` and `$|h(x)-L| < \epsilon.$`
* Thus, for those `$x,$` we have that `$-\epsilon < g(x)-L\le f(x)-L\le h(x)-L < \epsilon.$`
* For those `$x,$` it follows that `$|f(x)-L| < \epsilon.$`
* By the definition of limit, `$\lim_{x\to a} f(x)=L.$`
