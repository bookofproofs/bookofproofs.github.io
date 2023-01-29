layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$518
orderid: 50
parentid: bookofproofs$516
title: 
description: ELEMENTARY PROOF Proof of UNIQUE SOLVABILITY OF A+X=B ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: unique solvability of a plus x equals b,proof
contributors: bookofproofs

---


---

* We first show that `$x=b-a$` really _is_ the solution of the equation `$a+x=b.$`
   * Replacing `\(x\)` by `\((b-a)\)` in the equation leads to `$a+(b-a)=b.$`
   * By applying the [definition of subtracting real numbers][bookofproofs$1588] we get `$a+(b+(-a))=b.$`
   * The [commutativity of adding real numbers][bookofproofs$33] leads to `$a+((-a)+b)=b.$`
   *  The [associativity of adding real numbers][bookofproofs$31] leads to `$(a+(-a))+b=b.$`
   * The [uniqueness of negative numbers][bookofproofs$50] leads to `$0+b=b.$`
   * The [existence of zero][bookofproofs$34] leads to `$b=b.$`
   * Thus, `$x=b-a$` is the solution of the equation `$a+x=b$`.
* Now, we show, this solution is _the only_ solution of the equation. 
   * Take _any_ [real number][bookofproofs$1105] `\(y\)` with `$a+y=b.$` 
   * Adding `\((-a)\)` on both sides of the equation leads to `$(-a)+(a+y)=(-a)+b.$`
   * By [associativity of adding real numbers][bookofproofs$31] we get  
 `$((-a)+a)+y=(-a)+b.$`
   * By the [uniqueness of negative numbers][bookofproofs$50] it follows that `$0+y=(-a)+b.$`
   * By the [existence of zero][bookofproofs$34] we get `$y=(-a)+b.$`
   * The [commutativity of adding real numbers][bookofproofs$33] leads to `$y=b+(-a).$`
   * Applying the [definition of subtracting real numbers][bookofproofs$1588] we get `$y=b-a.$`
   * Thus, the solution `$(b-a)$` is the only solution of the equation `$a+x=b.$`
