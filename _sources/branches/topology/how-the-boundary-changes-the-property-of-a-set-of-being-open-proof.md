layout: proof
categories: branches,topology
nodeid: bookofproofs$1204
orderid: 50
parentid: bookofproofs$1203
title: 
description: Proof of HOW THE BOUNDARY CHANGES THE PROPERTY OF A SET OF BEING OPEN ★ master graduate maths ✔ visit BookOfProofs now!
references: bookofproofs$582
keywords: boundary closed,interior open,proof
contributors: bookofproofs

---


---

By hypothesis, `$(X,\mathcal O)$` is a [topological space][bookofproofs$6189] and `$B\subset X$` its subset. 

### Ad `$(1)$`

* Let `$x\in B \setminus \delta B$` be an element of the [interior][bookofproofs$1202].
* Since `$x$` is not a [boundary point][bookofproofs$1202], there is a [neighborhood][bookofproofs$8563] `$N_x$` that has no points in common with the [complement][bookofproofs$6829]  `$B^C$`.
* Moreover, we can choose `$N_x$` in a way that it has even no points in common with boundary `$\delta B.$` Otherwise, if there existed an `$y\in N_x \cap \delta B,$` then `$N_x$` would be a neighborhood of `$y$` and would have no points in common with the complement `$B^C.$` But _every_ neighborhood of a boundary point has points in common with the complement. 
* Thus, `$N_x$` has no boundary point in it.
* Altogether, we have shown that every neighborhood of `$x$` is contained in the interior. 
* It follows that the interior is [open][bookofproofs$853].
### Ad `$(2)$` 

* Let `$B^C$` be the complement of `$B.$`
* From the [definition of the boundary][bookofproofs$1202]  it follows that `$\delta B^C=\delta B$`. 
* From `$(1)$` we can deduce `$B^C\setminus \delta B^C)$` is open. 
* Therefore `$(B^C\setminus \delta B^C)^C$`  is closed. 
* But `$(B^C\setminus \delta B^C)^C=B\cup \delta B,$` which is the [closure][bookofproofs$1202].
* Therefore, the closure is closed.

### Ad `$(3)$`

* We have `$\delta B=(B\cup \delta B)\setminus(B\setminus \delta B).$` 
* It follows that `$X\setminus \delta B=(X\setminus(B\cup\delta B))\cup(B\setminus \delta B),$` which is, according to `\( (1)\)` and `\((2)\)`, a union of two open sets.
* By the third axiom of [topology][bookofproofs$6189], `$X\setminus \delta B=(\delta B)^C$` is open.
* Therefore, the complement `$((\delta B)^C)^C)=\delta B$` is closed, which is the boundary.
