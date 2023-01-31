layout: explanation
categories: branches,algebra
nodeid: bookofproofs$1102
orderid: 300
parentid: bookofproofs$85
title: Operation Table
description: OPERATION TABLE ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$577
keywords: operation table,operation tables
contributors: bookofproofs

---


---

If the [set][bookofproofs$550] `$X$` in an [algebraic structure][bookofproofs$342] is [finite][bookofproofs$985], then it is possible to write down the **operation table**. This is a tabular schema in which all elements  `$x_1,\ldots,x_n\in X$` are the headers of columns and rows and in which the entry in the `$i$`-th row and the `$j$`-th column is the element `$x_{ij}\in X$` which fulfills the property `$x_ij=x_i\ast x_j$`.

`$$\begin{array}{c|ccccc}
\ast&x_1&\ldots&x_j&\ldots &x_n\\
\hline
x_1&x_1\ast x_1&\ldots&x_1\ast x_j&\ldots& x_1\ast x_n\\
\vdots&\vdots&&\vdots&&\vdots\\
x_i&x_i\ast x_1&\ldots&x_i\ast x_j&\ldots& x_i\ast x_n\\
\vdots&\vdots&&\vdots&&\vdots\\
x_n&x_n\ast x_1&\ldots&x_n\ast x_j&\ldots& x_n\ast x_n\\
\end{array}$$`

In some cases it is possible to recognize the properties of the binary operation "`$\ast$`" looking at the operation table:

* The operation table is symmetric, if "`$\ast$`" is [commutative][bookofproofs$672],
* The element `$x_i$` is [left-neutral][bookofproofs$661], if the `$i$`-th row corresponds to the column headers of the operation table.
* The element `$x_j$` is [right-neutral][bookofproofs$661], if the `$j$`-th column corresponds to the row headers of the operation table.
* If a neutral element exist and has been identified, whenever it occures as an entry in the operation table, the corresponding row and column headers are [inverse][bookofproofs$670] to each other.
