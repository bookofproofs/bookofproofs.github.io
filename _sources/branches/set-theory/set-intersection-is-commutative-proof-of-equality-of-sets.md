layout: proof
categories: branches,set-theory
nodeid: bookofproofs$6842
orderid: 50
parentid: bookofproofs$6840
title: 
description: PROOF OF EQUALITY OF SETS Proof of SET INTERSECTION IS COMMUTATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: commutative,intersection,set,proof
contributors: bookofproofs

---


---

* Suppose that `$A$` and `$B$` are any [sets][bookofproofs$550].
* We want to show that the [set intersection][bookofproofs$6828] `$A\cap B$` is [commutative][bookofproofs$672], i.e. `$A\cap B=B\cap A.$`

### Part 1: `$A\cap B\subseteq B\cap A$`

* Let `$x\in A\cap B.$`
* By definition of [set intersection][bookofproofs$6828], `$x\in A\wedge x\in B.$`
* By [commutativity of conjunction][bookofproofs$1834], `$x\in B\wedge x\in A.$`
* It follows `$x\in B\cap A.$`
* By [defintion of subsets][bookofproofs$552],  `$A\cap B\subseteq B\cap A.$`

### Part 2: `$B\cap A\subseteq A\cap B$`

* The proof is identical to Part 1 if we exchange the denotations of `$A$` and `$B.$`

### Conclusion

* It follows from the [equality of sets][bookofproofs$6841] that that `$A = B.$`
