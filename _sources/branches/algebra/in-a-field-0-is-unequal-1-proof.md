layout: proof
categories: branches,algebra
nodeid: bookofproofs$6859
orderid: 50
parentid: bookofproofs$6858
title: 
description: Proof of $0$ IS UNEQUAL $1$ ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$577
keywords: 0 unequal 1,1 unequal 0,1=0,0=1,0 equal 1,1 equal 0,proof
contributors: bookofproofs

---


---

* By hypothesis, `$(F,+,\cdot)$` is a [field][bookofproofs$557].
* Suppose, `$0=1$`.
   * Take `$x\in F$` with `$x\neq 0$`[^1].
   * Because `$0$` is the [neutral element of addition][bookofproofs$661] in `$F$`, `$1$` is its additive inverse, i.e. `$1-0=0.$`
   * From the [distributivity laws][bookofproofs$682] in `$F,$` we get `$x\cdot 0=x\cdot (1-0)=x\cdot 1-x\cdot 0.$`
   * Because `$1$` is the [neutral element][bookofproofs$661] of multiplication in `$F$`, it follows `$x\cdot 0=x-x\cdot 0,$` or `$x=x\cdot 0+x\cdot 0.$` 
   * From the distributivity laws, it follows `$x=x\cdot (0+0),$` and, since `$0$` is neutral with respect to the an addition, `$x=x\cdot 0.$`  
   * Altogether, it follows `$x=x-x,$` or `$x=0$`, in [contradiction][bookofproofs$744] to `$x\neq 0.$`
* The assumption `$0=1$` must be false, i.e. `$0\neq 1.$`

[^1]: Note that from the [definition of a field][bookofproofs$557] it follows that it is, in particular, a ring `$R$` which is not the [zero ring][bookofproofs$879] and that "every `$x\neq 0$` in `$F$` has an inverse element". Thus, such elements, for which `$x\neq 0$`, must exist in `$F$`.
