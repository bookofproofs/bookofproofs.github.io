layout: definition
categories: branches,algebra
nodeid: bookofproofs$8657
orderid: 400
parentid: bookofproofs$343
title: Matrix and Vector Addition
description: MATRIX ADDITION, VECTOR ADDITON ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8684
keywords: matrix addition,matrix sum,matrix sums,matrix additions,vector addition,vector sum,vector sums,vector additions
contributors: bookofproofs

---


---

Let `\(A,B\in M_{m\times n}(F)\)` be two [matrices][bookofproofs$1048] over a given [field][bookofproofs$557] The **matrix addition** `$"+"$` is defined by

`$$
C:=A+B=\pmatrix{
\alpha_{11} & \alpha_{12} & \ldots & \alpha_{1n} \cr
\alpha_{21} & \alpha_{22} & \ldots & \alpha_{2n} \cr
\vdots & \vdots & \ddots & \vdots \cr
\alpha_{m1} & \alpha_{m2} & \ldots & \alpha_{mn} \cr
}+\pmatrix{
\beta_{11} & \beta_{12} & \ldots & \beta_{1n} \cr
\beta_{21} & \beta_{22} & \ldots & \beta_{2n} \cr
\vdots & \vdots & \ddots & \vdots \cr
\beta_{m1} & \beta_{m2} & \ldots & \beta_{mn} \cr
}=\pmatrix{
\alpha_{11}+\beta_{11} & \alpha_{12}+\beta_{12}  & \ldots & \alpha_{1n}+\beta_{1n} \cr
\alpha_{21}+\beta_{21} & \alpha_{22}+\beta_{22} & \ldots & \alpha_{2n}+\beta_{2n} \cr
\vdots & \vdots & \ddots & \vdots \cr
\alpha_{m1}+\beta_{m1} & \alpha_{m2}+\beta_{m2} & \ldots & \alpha_{mn}+\beta_{mn} \cr
}.$$`

The resulting matrix `$C\in M_{m\times n}(F)$` is called a **matrix sum** of the two matrices `\(A\)` and `\(B\)`.

Vector addition is a special case of matrix addition for matrices of the size `$M_{m\times 1}(F)$` for [column vectors][bookofproofs$7943] 

`$$
\pmatrix{
\alpha_{1} \cr
\alpha_{2} \cr
\vdots \cr
\alpha_{m} \cr
}+\pmatrix{
\beta_{1} \cr
\beta_{2} \cr
\vdots \cr
\beta_{m} \cr
}=\pmatrix{
\alpha_{1}+\beta_{1}\cr
\alpha_{2}+\beta_{2}\cr
\vdots \cr
\alpha_{m}+\beta_{m} \cr
}.$$`

or of the size `$M_{1\times n}(F)$` for [row vectors][bookofproofs$7943]. 

`$$ \pmatrix{\alpha_{1},&\alpha_{2},&\ldots, &\alpha_{n}} + \pmatrix{\beta_{1},&\beta_{2},&\ldots, &\beta_{n}}=\pmatrix{\alpha_{1}+\beta_{1},&\alpha_{2}+\beta_{2},&\ldots,& \alpha_{n}+\beta_{n}}.$$`
