layout: definition
categories: branches,logic
nodeid: bookofproofs$7879
orderid: 300
parentid: bookofproofs$7875
title: Proofs and Theorems in a Logical Calculus
description: PROOFS AND THEOREMS IN A LOGICAL CALCULUS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$7878
keywords: calculus,formal proof,logical,proofs,theorem,theorems
contributors: bookofproofs

---
With these prerequisites, we can introduce the concepts of a __formal proof__ and of a __theorem__ in a logical calculus.

---

Let `$(L,\mathcal A,\mathcal R)$` be [logical calculus][bookofproofs$7882] with `$n$` [axioms][bookofproofs$7876] `$\mathcal A:=\{a_1,\ldots, a_n\}$` and `$r$` [rules of inference][bookofproofs$7877] `$$\mathcal R:=\cases{f^{(1)}_1,\ldots,f^{(1)}_{m_{(1)}},\vdash f_1,\\ 
\vdots\\ 
f^{(r)}_1,\ldots,f^{(r)}_{m_{(r)}},\vdash f_r.}$$`
A **formal proof** is a chain of strings `$\phi_1, \phi_2,\ldots \phi_n\in L$` satisfying the following construction rules:

* `$\phi_i$` is an axiom for some `$i\in\{1,\ldots,n\}$`, or 
* there is a rule of inference such that  `$f^{(j)}_1,\ldots,f^{(j)}_{m_{(j)}},\vdash \phi_j$` for some  `$j\in\{1,\ldots,r\}.$`

The last string `$\phi_n$` is called a **theorem**.
