layout: definition
categories: branches,set-theory
nodeid: bookofproofs$8299
orderid: 50
parentid: bookofproofs$272
title: Indicator (Characteristic) Function, Carrier
description: INDICATOR CHARACTERISTIC FUNCTION, CARRIER ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8297
keywords: indicator function,characteristic function,indicator functions,characteristic functions,carrier,carriers
contributors: bookofproofs

---


---

Let `$S$` be a [set][bookofproofs$550]. An **indicator function** (or **characteristic function**) `$\chi$` on `$S$` is a [function][bookofproofs$592] `$\chi:S\to\{0,1\},$` i.e. a function mapping each element of `$S$` to exactly one of the two values `$1$` or `$0.$`

For a given characteristic function `$\chi$`, the [fiber][bookofproofs$592] of `$1$` under `$\chi$` is called its **carrier**.

### Notes

* Every non-empty set `$S$` can have _many_ different indicator functions, in particular the two `$\chi(x)=1,$` and `$\chi'(x)=0$` for all `$x\in S.$`
* The carrier of a given `$\chi$` defines a unique [subset][bookofproofs$552] `$C\subseteq S$` by `$C=\{x\in S\mid \chi(x)=1\}.$`
* Vice versa, for a given subset `$A\subseteq S,$` there is a unique characteristic function `$\chi_A$` such that its carrier equals `$A,$` i.e. this characteristic function is defined by `$$\chi_A(x):=\begin{cases}1&x\in S\wedge x\in A,\\0&x\in S\wedge x\not\in A.\\\end{cases}$$`

### Example

The carrier of the set of integers in the set of real numbers:



§§§1

---

§§§1
<div class='sage'>
def carrier(N):
   if N==floor(N):
      return 1
   else:
      return 0

points= [(i, carrier(i)) for i in range(-5,10)]
list_plot(points)
</div>
