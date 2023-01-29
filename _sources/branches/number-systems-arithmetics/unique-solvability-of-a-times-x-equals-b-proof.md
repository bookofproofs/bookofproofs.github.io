layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$519
orderid: 50
parentid: bookofproofs$517
title: 
description: ELEMENTARY PROOF Proof of UNIQUE SOLVABILITY OF AX=B ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: unique solvability of a times x equals b,proof
contributors: bookofproofs

---


---

* By hypothesis, `$a\neq 0.$`
* First, we show that `$x=ba^{-1}$` really _is_ the solution of the equation `$ax=b.$`
   * Replacing `\(x\)` by `\(ba^{-1}\)` in the equation leads to `$a(ba^{-1})=b.$`
   * The [commutativity of multiplying real numbers][bookofproofs$38] leads to `$a(a^{-1}b)=b.$`
   * The [associativity of multiplying real numbers][bookofproofs$37] leads to `$(aa^{-1})b=b.$`
   * The [uniqueness of inverse real numbers][bookofproofs$51] leads to `$1\cdot b=b.$`
   * The [existence of one][bookofproofs$40] leads to `$b=b.$`
   * Thus, `$x=ba^{-1}$` is the solution of the equation `$ax=b.$`
* Now, we show this is _the only_ solution of the equation. 
   * Take _any_ [real number][bookofproofs$1105] `\(y\)` with `$ay=b.$` 
   * Multyplying both sides of the equation by `\(a^{-1}\)` leads to `$a^{-1}(ay)=a^{-1}b.$`
   * By [associativity of multiplying real numbers][bookofproofs$37] we get `$(a^{-1}a)y=a^{-1}b.$`
   * By the [uniqueness of inverse real numbers][bookofproofs$51] it follows that `$1\cdot y=a^{-1}b.$`
   * By the [existence of one][bookofproofs$40] we get `$y=a^{-1}b.$`
   * The [commutativity of multiplying real numbers][bookofproofs$38] leads to `$y=ba^{-1}.$`
   * Thus, the solution `$(ba^{-1})$` is the only solution of the equation `$ax=b.$`
