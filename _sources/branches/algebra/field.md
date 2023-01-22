layout: definition
categories: branches,algebra
nodeid: bookofproofs$557
orderid: 0
parentid: bookofproofs$265
title: Field
description: FIELD ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$577,bookofproofs$6907
keywords: field,fields,field axioms
contributors: bookofproofs

---


---

A [commutative unit ring][bookofproofs$880] `$R$` (with the [multiplicative neutral element][bookofproofs$661] `$1$`) is called a **field**, if `$R$` is not the [zero ring][bookofproofs$879] and every element `\(x\in R\)` with `$x\neq 0$` ($0$ being the [additive neutral element][bookofproofs$661])  has a [multiplicative inverse][bookofproofs$670]

"Unfolding" all definitions, a _field_ fulfills the following axioms:

* `$(R,+)$` is a [commutative group][bookofproofs$553]:
   * [Associativity][bookofproofs$668] of `$"+"$`: `$x+(y+z)=(x+y)+z$` for all `$x,y,z\in F.$`
   * [Commutativity][bookofproofs$672] of `$"+"$`: `$x+y=y+x$` for all `$x,y\in F.$`
   * [Neutral Element][bookofproofs$661] of `$"+"$`: There is an element `$0\in F$` with `$0+x=x+0=x$` for all `$x\in F.$`
   * [Inverse elements][bookofproofs$670] of `$"+"$`: For all `$x\in F$` there exists an `$-x\in F$` with `$x+(-x)=(-x)+x=0.$`
* `$(R,\cdot)$` is a [commutative group][bookofproofs$553]:
   * [Associativity][bookofproofs$668] of `$"\cdot"$`: `$x\cdot(y\cdot z)=(x\cdot y)\cdot z$` for all `$x,y,z\in F.$`
   * [Commutativity][bookofproofs$672] of `$"\cdot"$`: `$x\cdot y=y\cdot x$` for all `$x,y\in F.$`
   * [Neutral Element][bookofproofs$661] of `$"\cdot"$`: There is an element `$1\in F$` with `$1\cdot x=x\cdot 1=x$` for all `$x\in F.$`
   * [Inverse elements][bookofproofs$670] of `$"\cdot"$`: For all `$x\in F$` with `$x\neq 0$` there exists an `$x^{-1}\in F$` with `$x\cdot x^{-1}=x^{-1}\cdot x=1.$`
* [Distributivity laws][bookofproofs$682]: `$(x+y)\cdot z=x\cdot z + y\cdot z$` and `$x\cdot (y+z)=x\cdot y + x\cdot z$` for all `$x,y,z\in F.$`

### Notes

* In some books, you will also encounter the axiom `$1\neq 0.$` This axiom will be proven later from the remaining axioms given above and the requirement that `$R$` must not be the [zero ring][bookofproofs$879].
