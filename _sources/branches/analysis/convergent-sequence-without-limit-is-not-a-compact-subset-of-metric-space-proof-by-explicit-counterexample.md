layout: proof
categories: branches,analysis
nodeid: bookofproofs$6580
orderid: 50
parentid: bookofproofs$6579
title: 
description: PROOF BY EXPLICIT COUNTEREXAMPLE Proof of CONVERGENT SEQUENCE WITHOUT LIMIT IS NOT A COMPACT SUBSET OF METRIC SPACE &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$582
keywords: compact,convergent,limit,metric,not,sequence,space,subset,without,proof
contributors: bookofproofs

---


---

We will show that the following [subset][bookofproofs$552] is not [compact][bookofproofs$6575] in the [metric space of real numbers][bookofproofs$618] `\(\mathbb R\)`: `\[U:=\left\{\frac 1n:~n\in\mathbb N\setminus \{0\}\right\}\subset\mathbb R.\]`

* Set the [open real intervals][bookofproofs$1153] `\[U_1:=\left]\frac 12,2\right[\quad\text{ and }\quad U_n:=\left]\frac 1{n+1},\frac1{n-1}\right[\text{ for }n\ge 2.\]`
* Thus, `\((U_n)_{n\ge 1}\)` is an [open cover][bookofproofs$150] of `$U$`. 
* Moreover, every [open set][bookofproofs$852] `\(U_n\)` contains exactly one element of `\(U\)`, i.e. the point `\(\frac 1n\)`. 
* Thus, `\(U\)` cannot be covered by any [finite][bookofproofs$985] subcover `\(U_{n_1},U_{n_2},\ldots,U_{n_k}\)`. 
* Thus, `\(U\)` is not compact.
