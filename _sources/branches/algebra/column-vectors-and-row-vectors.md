layout: definition
categories: branches,algebra
nodeid: bookofproofs$7943
orderid: 2
parentid: bookofproofs$7942
title: Column Vectors and Row Vectors
description: COLUMN VECTORS AND ROW VECTORS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$7937
keywords: column vector,row vector,vectors,column vectors,row vectors
contributors: bookofproofs

---
Similar to the introduced matrices, in the following definition, we introduce the notion of a "vector" from a pure notational perspective as a special case of a matrix.

---

Let `$n\ge 1$` be a [natural number][bookofproofs$718] A **column vector** (or just **vector**) with `$n$` field elements is a [matrix][bookofproofs$1048] over a [field][bookofproofs$557] `$F$` with just one column and many rows, i.e. an element of `$M_{m\times 1}(F):$`

`$$v=\pmatrix{\alpha_1\\\vdots\\\alpha_m}$$`

Similarly, a **row vector** is [transposed][bookofproofs$1054] column vector

`$$v^T=\pmatrix{\alpha_1,&\ldots&,\alpha_m}$$`

A row vector is an element of `$M_{1\times m}(F)$`. 

### Notes

* Many sources introduce vectors differently, namely as elements of the [Cartesian product][bookofproofs$748] `$F^n$`, where `$F$` is a field. 
* We prefer to consider vectors as special cases of matrices with a single column. This will allow us to derive many properties of vectors as special cases of properties of matrices. In particular, we gained already the notion of the transposed vector `$v^T$` that cannot be derived from the Cartesian definition without additional explanation. 
* Nevertheless, we will sometimes follow the convention and write `$v\in F^n$` instead of `$v\in M_{m\times 1}(F)$`.
* Also by convention, we are going to denote vectors by small Latin or Greek letters, e.g. `$v$`, and we always mean a column vector by `$v$` and row vectors by `$v^T.$`
