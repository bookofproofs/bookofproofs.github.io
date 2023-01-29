layout: explanation
categories: branches,combinatorics
nodeid: bookofproofs$8303
orderid: 400
parentid: bookofproofs$264
title: Indicator Function and Complete Induction
description: INDICATOR FUNCTION AND COMPLETE INDUCTION ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8297
keywords: indicator function and complete induction
contributors: bookofproofs

---


---

The [indicator function][bookofproofs$8299] provides new insight into the [proving principle by complete induction][bookofproofs$657]. If `$p$` is a property which is valid for some [natural numbers][bookofproofs$718] `$m\in\mathbb N,$` then it defines a unique indicator function `$\chi(m)$` defined by `$$\chi(m):=\begin{cases}1&\text{if }p(m)\text{ is true}\\0&\text{else, i.e if }p(m)\text{ is false.}\end{cases}$$`
With this interpretation, the proving principle goes as follows:
* Base case: Prove that `$\chi(m)=1$` for some `$m.$`
* Induction step: Show that if `$n\ge m$` and `$\chi(m)=1$`, then `$\chi(n+1)=\chi(n).$`
* Conclusion: Conclude that `$\chi(n)=1$` for all `$n\ge m.$`

In other words, the proving principle uses the fact that the indicator function `$\chi$` is constant locally, i.e. for all the two natural numbers `$(n,n+1),$` if `$n\ge m$` and `$\chi(m)=\chi(n)=1.$` This allows the conclusion, that `$\chi$` is constant globally, i.e. for all consecutive pairs `$(n,n+1),$` `$(n+1,n+2),$` etc, we have `$\chi(m)=\chi(n)=\chi(n+1)=\chi(n+2)=\ldots.$` This, in turn, is equivalent to proving that the property `$p$` is true for all natural numbers `$n\ge m.$`
