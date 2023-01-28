layout: definition
categories: branches,algebra
nodeid: bookofproofs$1044
orderid: 100
parentid: bookofproofs$138
title: Systems of Linear Equations with many Unknowns
description: SYSTEMS OF LINEAR EQUATIONS WITH MANY UNKNOWNS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$561,bookofproofs$7937
keywords: equations,homogeneous,inhomogeneous,linear,many,non-trivial,solution,systems,trivial,unknowns
contributors: bookofproofs

---


---

Let `\(F\)` be a [field][bookofproofs$557] A **system of linear equations** (SLE) with `\(n\)` **unknowns** `\(x_1,\ldots,x_n\)` and (`\(m\ge 1\)`) [linear equations][bookofproofs$1043] is given by 

`\[\begin{array}{ccl}
\alpha_{11}x_1+\ldots+\alpha_{1n}x_n&=&\beta_1\\\
\alpha_{21}x_1+\ldots+\alpha_{2n}x_n&=&\beta_2\\
\vdots&\vdots&\vdots\\
\alpha_{m1}x_1+\ldots+\alpha_{mn}x_n&=&\beta_m\\
\end{array}\quad\quad( * )\]`

with `\(\alpha_{ij}\in F\)`, `\(i=1,\ldots,n\)`, `\(j=1,\ldots,m\)` and some `\(\beta_1,\ldots,\beta_m\in F\)`.

The SLE `$( * )$` is called 
* **homogeneous** if `$\beta_1=0,\ldots,\beta_n=0,$`
* **inhomogeneous** if `$\beta_i\neq 0$` for at least one `$i\in\{1,\ldots,m\}.$`

The SLE  `$( * )$`  has a **solution**, if there exist numbers `\(a_1,\ldots,a_n\in F\)` such that for the replacement `\(x_1:=a_1,\ldots,x_n:=a_n\)` all linear equations in the SLE are simultaneously fulfilled.

The solution of a homogeneous SLE is called **trivial** if `\(a_i=0\)` for all `\(i=1,\ldots,n\)`, otherwise (if a solution with at least one `\(\beta_i\neq 0\)` exists), it is called *non-trivial*. 

### Indexing Convention 

In the double-index `\(ij\)` of the coefficients `\(\alpha_{ij}\)`, by convention, the first index `\(i\)` denotes the row, the second index `\(j\)` denotes the column of the system.
