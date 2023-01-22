layout: definition
categories: branches,algebra
nodeid: bookofproofs$7941
orderid: 3
parentid: bookofproofs$138
title: Coefficient Matrix
description: COEFFICIENT MATRIX &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$641,bookofproofs$7937
keywords: coefficient,coefficient matrix,extended coefficient matrix,matrix
contributors: bookofproofs

---


---

Let `\(F\)` be a [field][bookofproofs$557] and let 

`\[\begin{array}{ccl}
\alpha_{11}x_1+\ldots+\alpha_{1n}x_n&=&\beta_1\\\
\alpha_{21}x_1+\ldots+\alpha_{2n}x_n&=&\beta_2\\
\vdots&\vdots&\vdots\\
\alpha_{m1}x_1+\ldots+\alpha_{mn}x_n&=&\beta_m\\
\end{array}\quad\quad( * )\]`

be an [SLE (system of linear equations) ][bookofproofs$1044]

The can write the coefficients `\(\alpha_{ij}\in F\)`, `\(i=1,\ldots,n\)`, `\(j=1,\ldots,m\)` as a [matrix][bookofproofs$1048] and call it the **coefficient matrix** `$A$` of the SLE `$( * ):$`

`$$A:=\pmatrix{\alpha_{11}& \ldots&\alpha_{1n}\\
\alpha_{21}& \ldots&\alpha_{2n}\\
\vdots&\vdots&\vdots\\
\alpha_{m1}& \ldots&\alpha_{mn}}$$`

We also introduce another term we will need later. The tabular schema 

`$$A|\beta:=
\left(\begin{array}{ccc|c}\alpha_{11}& \ldots&\alpha_{1n}&\beta_1\\
\alpha_{21}& \ldots&\alpha_{2n}&\beta_2\\
\vdots&\vdots&\vdots&\vdots\\
\alpha_{m1}& \ldots&\alpha_{mn}&\beta_m\end{array}\right)$$`

is called the **extended coefficient matrix** of the SLE `$( * ).$`
