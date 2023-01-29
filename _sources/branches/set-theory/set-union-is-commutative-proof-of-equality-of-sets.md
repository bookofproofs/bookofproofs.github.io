layout: proof
categories: branches,set-theory
nodeid: bookofproofs$6843
orderid: 50
parentid: bookofproofs$6836
title: 
description: PROOF OF EQUALITY OF SETS Proof of SET UNION IS COMMUTATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: commutative,set,union,proof
contributors: bookofproofs

---


---

* Suppose that `$A$` and `$B$` are any [sets][bookofproofs$550].
* We want to show that the [set union][bookofproofs$6827] `$A\cup B$` is [commutative][bookofproofs$672], i.e. `$A\cap B=B\cup A.$`

### Part 1: `$A\cup B\subseteq B\cup A$`

* Let `$x\in A\cup B.$`
* By definition of [set union][bookofproofs$6827] , `$x\in A\vee x\in B.$`
* By [commutativity of disjunction][bookofproofs$1835], `$x\in B\vee x\in A.$`
* It follows `$x\in B\cup A.$`
* By [defintion of subsets][bookofproofs$552],  `$A\cup B\subseteq B\cup A.$`

### Part 2: `$B\cup A\subseteq A\cup B$`

* The proof is identical to Part 1 if we exchange the denotations of `$A$` and `$B.$`

### Conclusion

* It follows from the [equality of sets][bookofproofs$6841] that that `$A = B.$`
