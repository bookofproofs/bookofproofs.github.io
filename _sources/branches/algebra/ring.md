layout: definition
categories: branches,algebra
nodeid: bookofproofs$683
orderid: 100
parentid: bookofproofs$192
title: (Unit) Ring
description: RING ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$577,bookofproofs$6907
keywords: ring,ring with identity,unit ring,rings,rings with identity,unit rings
contributors: bookofproofs

---


---

A **ring** is an algebraic structure `\(R\)` with two [binary operations][bookofproofs$6188] `\( + \)` and `\(\cdot\)`, denoted by `\((R, + ,\cdot)\)`, for which the following holds:

1. `\((R, + )\)` is an [Abelian group][bookofproofs$553],
1. `\((R,\cdot)\)` is a [semigroup][bookofproofs$660] (i.e. the operation "`$\cdot$`" is associative),
1. The [distributivity law][bookofproofs$682] holds for all `\(x,y,z\in R\)`.

If `\((R,\cdot)\)` is a [monoid][bookofproofs$659] (i.e. if the semigroup contains a multiplicative identity `\(1\)`), then the ring is called a **unit ring** (or **ring with identity**).

"Unfolding" all definitions, a _ring_ fulfills the following axioms:

* Associativity of "`$+$`": `$x+(y+z)=(x+y)+z$` for all `$x,y,z\in R.$`
* Commutativity of "`$+$`": `$x+y=y+x$` for all `$x,y\in R.$`
* Neutral Element of "`$+$`": There is an element `$0\in R$` with `$0+x=x+0=x$` for all `$x\in R.$`
* Inverse elements of "`$+$`": For all `$x\in R$` there exists an `$-x\in G$` with `$x+(-x)=(-x)+x=0.$`
* Associativity of "`$\cdot$`": `$x\cdot(y\cdot z)=(x\cdot y)\cdot z$` for all `$x,y,z\in R.$`
* Neutral Element of "`$\cdot$`" (only when `$R$` is a unit ring!): There is an element `$1\in R$` with `$1\cdot x=x\cdot 1=x$` for all `$x\in R.$`
* Distributivity laws: `$(x+y)\cdot z=x\cdot z + y\cdot z$` and `$x\cdot (y+z)=x\cdot y + x\cdot z$` for all `$x,y,z\in R.$`
