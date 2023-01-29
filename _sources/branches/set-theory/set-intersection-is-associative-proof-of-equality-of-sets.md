layout: proof
categories: branches,set-theory
nodeid: bookofproofs$6850
orderid: 50
parentid: bookofproofs$6848
title: 
description: PROOF OF EQUALITY OF SETS Proof of SET INTERSECTION IS ASSOCIATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: associative,intersection,set,proof
contributors: bookofproofs

---


---

* Suppose that `$A,B,C$` are [sets][bookofproofs$550].
* We will show that the [set intersection][bookofproofs$6828] is [associative][bookofproofs$668], i.e. `$(A\cap B)\cap C=A\cap (B\cap C).$`

### Part 1: `$(A\cap B)\cap C\subseteq A\cap (B\cap C).$`

* Let `$x\in (A\cap B)\cap C.$`
* By the [definition of set intersection][bookofproofs$6828], we have `$x\in (A\cap B)\wedge x\in C.$`
* Again, by the [definition of set intersection][bookofproofs$6828], we have `$(x\in A\wedge x\in B)\wedge x\in C.$`
* By the [associativity of conjunction][bookofproofs$6844], we get `$x\in A\wedge (x\in B\wedge x\in C).$`
* Again, by the definition of set intersection, `$x\in A\wedge x\in B\cap C.$`
* Again, by the definition of set intersection, we get finally `$x\in A\cap (B\cap C).$`
* It follows that `$(A\cap B)\cap C\subseteq A\cap (B\cap C).$`

### Part 2: `$B\subseteq A$`

* Let `$x\in A\cap (B\cap C).$`
* By the [definition of set intersection][bookofproofs$6828], we have `$x\in A\wedge x\in B\cap C.$`
* Again, by the [definition of set intersection][bookofproofs$6828], we have `$x\in A\wedge (x\in B\wedge x\in C).$`
* By the [associativity of conjunction][bookofproofs$6844], we get `$(x\in A\wedge x\in B)\wedge x\in C.$`
* Again, by the definition of set intersection, `$x\in A\cap B\wedge x\in C.$`
* Again, by the definition of set intersection, we get finally `$x\in (A\cap B)\cap C.$`
* It follows that `$A\cap (B\cap C)\subseteq (A\cap B)\cap C.$`

### Conclusion

* It follows from the [equality of sets][bookofproofs$6841] that `$A\cap (B\cap C)=(A\cap B)\cap C.$`
