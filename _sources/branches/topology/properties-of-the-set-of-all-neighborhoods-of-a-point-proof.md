layout: proof
categories: branches,topology
nodeid: bookofproofs$8617
orderid: 50
parentid: bookofproofs$8616
title: 
description: PROOF OF PROPERTIES OF THE SET OF ALL NEIGHBORHOODS OF A POINT &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$8613
keywords: properties of the set of all neighborhoods of a point,proof
contributors: bookofproofs

---


---

* By hypothesis, `$(X,\mathcal O)$` is a [topological space][bookofproofs$6189], `$A\in X,$` and `$\mathcal N(A)$` is the [set of all neighborhoods][bookofproofs$8563] of `$A.$` 

### Ad `$(1)$`

* `$X\in\mathcal N(A)$`.
* Therefore, `$\mathcal N(A)$` is not [empty][bookofproofs$550]).

### Ad `$(2)$`

* `$A\not\in\emptyset$`.
* Therefore, `$\emptyset$` is not an element of `$\mathcal N(A).$`

### Ad `$(3)$`

* Assume, `$U,W\in\mathcal N(A).$`
* By definition of [neighborhoods][bookofproofs$8563], `$A\in O_U\subset U$` and `$A\in O_W\subset W$` with `$O_U,O_W\in \mathcal O.$`
* Since `$X$` is a [topological space][bookofproofs$6189], `$\mathcal O$` contains the [intersection][bookofproofs$6828] `$O_U\cap O_W.$`
* On the other hand, `$A\in O_U\cap O_W\subset U\cap W.$`
* It follows that `$U\cap W$` is a neighborhood of `$A.$`
* Thus, `$U\cap W\in\mathcal N(A).$`

### Ad `$(4)$`

* Assume, `$U\in\mathcal N(A).$`
* Thus, `$A\in O\subset U$` for some `$O\in \mathcal O.$`
* But then `$A\in O\subset U\subset W$` for any [superset][bookofproofs$552] `$W$` of `$U$`. 
* It follows that `$W$` is a neighborhood of `$A.$`
* Thus `$W\in\mathcal N(A).$`
