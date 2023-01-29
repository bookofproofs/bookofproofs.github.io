layout: proof
categories: branches,set-theory
nodeid: bookofproofs$6851
orderid: 50
parentid: bookofproofs$6849
title: 
description: PROOF OF EQUALITY OF SETS Proof of SET UNION IS ASSOCIATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: associative,set,union,proof
contributors: bookofproofs

---


---

* Suppose that `$A,B,C$` are [sets][bookofproofs$550].
* We will show that the [set union][bookofproofs$6827] is [associative][bookofproofs$668], i.e. `$(A\cup B)\cup C=A\cup (B\cup C).$`

### Part 1: `$(A\cup B)\cup C\subseteq A\cup (B\cup C).$`

* Let `$x\in (A\cup B)\cup  C.$`
* By the [definition of set union][bookofproofs$6828], we have `$x\in (A\cup B)\vee x\in C.$`
* Again, by the [definition of set union][bookofproofs$6828], we have `$(x\in A\vee x\in B)\vee x\in C.$`
* By the [associativity of disjunction][bookofproofs$6846], we get `$x\in A\vee (x\in B\vee x\in C).$`
* Again, by the definition of set union, `$x\in A\vee x\in B\cup C.$`
* Again, by the definition of set union, we get finally `$x\in A\cup (B\cup C).$`
* It follows that `$(A\cup B)\cup C\subseteq A\cup (B\cup C).$`

### Part 2: `$B\subseteq A$`

* Let `$x\in A\cup (B\cup C).$`
* By the [definition of set union][bookofproofs$6828], we have `$x\in A\vee x\in B\cup C.$`
* Again, by the [definition of set union][bookofproofs$6828], we have `$x\in A\vee (x\in B\vee x\in C).$`
* By the [associativity of disjunction][bookofproofs$6846], we get `$(x\in A\vee x\in B)\vee x\in C.$`
* Again, by the definition of set union, `$x\in A\cup B\vee x\in C.$`
* Again, by the definition of set union, we get finally `$x\in (A\cup B)\cup C.$`
* It follows that `$A\cup (B\cup C)\subseteq (A\cup B)\cup C.$`

### Conclusion

* It follows from the [equality of sets][bookofproofs$6841] that `$A\cup (B\cup C)=(A\cup B)\cup C.$`
