layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$3474
orderid: 50
parentid: bookofproofs$8300
title: 
description: Proof of INDICATOR FUNCTION AND SET OPERATIONS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: indicator function vs. set operations, characteristic function on set operations,proof
contributors: bookofproofs

---


---

* By hypothesis, `$S$` is a [set][bookofproofs$550] with some [subsets][bookofproofs$552] `$A,B\subseteq S$` and the corresponding [indicator functions][bookofproofs$8299] `$\chi_A$` and `$\chi_B.$` 

### Set Union

* By definition, the [carrier][bookofproofs$8299] of `$\max(\chi_A,\chi_B)$` is the set `$\{x\mid x\in S,\max(\chi_A,\chi_B)=1\}.$`
* This set equals obviously the set `$\{x\mid x\in S,\chi_A(x)=1\vee \chi_B(x)=1\}.$`
* But it carrier is the [set union][bookofproofs$6827] `$A\cup B.$`
* Therefore, `$\chi_{A\cup B}=\max(\chi_A,\chi_B).$`

### Set Intersection

* By definition, the [carrier][bookofproofs$8299] of `$\min(\chi_A,\chi_B)$` is the set `$\{x\mid x\in S,\min(\chi_A,\chi_B)=1\}.$`
* This set equals obviously the set `$\{x\mid x\in S,\chi_A(x)=1\wedge \chi_B(x)=1\}.$`
* But it carrier is the [set intersection][bookofproofs$6828] `$A\cap B.$`
* Therefore, `$\chi_{A\cap B}=\min(\chi_A,\chi_B).$`

### Other

* The reader is invited to verify the other identities for [set complement][bookofproofs$6829] and [set difference][bookofproofs$6830] as an exercise.
