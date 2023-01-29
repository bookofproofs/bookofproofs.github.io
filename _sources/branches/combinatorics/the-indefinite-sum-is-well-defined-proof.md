layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8508
orderid: 50
parentid: bookofproofs$8507
title: 
description: PROOF OF ANTIDIFFERENCES ARE UNIQUE UP TO A PERIODIC CONSTANT ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$8404
keywords: indefinite sum is well-defined,periodic constant,antidifferences are unique up to a periodic constant,periodic constants,proof
contributors: bookofproofs

---


---

* Assume, for a [complex-valued][bookofproofs$216] [function][bookofproofs$592] `$f:\mathbb C\to\mathbb C$`, the [indefinite sum][bookofproofs$8506] has two different values `$G(x)=\sum f(x)$` and `$F(x)=\sum f(x)$`.
* By definition of the indefinite sum, `$\Delta F(x)=f(x)$` and `$\Delta G(x)=f(x)$`.
* The both [difference operators][bookofproofs$8408] are therefore equal `$\Delta F(x)=\Delta G(x)$`.
* It follows from the [basic calculations involving the difference operator][bookofproofs$8409] `$\Delta(F(x)-G(x))=0.$`
* If we set `$P(x)=F(x)-G(x)$`, then `$\Delta P(x)=0$`, or, by the definition of the [difference operator][bookofproofs$8408], `$P(x+1)=P(x)$`.
* Thus, `$F(x)=\sum f(x)+P(x)$`, `$G(x)=\sum f(x)-P(x)$`.
* In other words, any [antidifference][bookofproofs$8506] of `$f$` can be written as its [indefinite sum][bookofproofs$8506] plus/minus a periodic constant `$P(x).$`
