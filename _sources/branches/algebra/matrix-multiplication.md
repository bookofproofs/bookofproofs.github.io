layout: definition
categories: branches,algebra
nodeid: bookofproofs$1050
orderid: 700
parentid: bookofproofs$7942
title: Matrix Multiplication
description: MATRIX MULTIPLICATION ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1038
keywords: matrix product,matrix multiplication,product of matrices,multiplication of matrices,how to multiply two matrices
contributors: bookofproofs

---


---

Let `\(A\in M_{m\times n}(F)\)` and `\(B\in M_{n\times r}(F)\)` be two [matrices][bookofproofs$1048]. The **matrix multiplication** "`$\cdot$`" is defined by  

`\[
C:=AB=\pmatrix{
\alpha_{11} & \alpha_{12} & \ldots & \alpha_{1n} \cr
\alpha_{21} & \alpha_{22} & \ldots & \alpha_{2n} \cr
\vdots & \vdots & \ddots & \vdots \cr
\alpha_{m1} & \alpha_{m2} & \ldots & \alpha_{mn} \cr
}\cdot\pmatrix{
\beta_{11} & \beta_{12} & \ldots & \beta_{1r} \cr
\beta_{21} & \beta_{22} & \ldots & \beta_{2r} \cr
\vdots & \vdots & \ddots & \vdots \cr
\beta_{n1} & \beta_{n2} & \ldots & \beta_{nr} \cr
}=\pmatrix{
\sum_{k=1}^n\alpha_{1k}\beta_{k1} & \sum_{k=1}^n\alpha_{1k}\beta_{k2} & \ldots & \sum_{k=1}^n\alpha_{1k}\beta_{kr}  \cr
\sum_{k=1}^n\alpha_{2k}\beta_{k1} & \sum_{k=1}^n\alpha_{2k}\beta_{k2} & \ldots & \sum_{k=1}^n\alpha_{2k}\beta_{kr}  \cr
\vdots & \vdots & \ddots & \vdots \cr
\sum_{k=1}^n\alpha_{mk}\beta_{k1} & \sum_{k=1}^n\alpha_{mk}\beta_{k2} & \ldots & \sum_{k=1}^n\alpha_{mk}\beta_{kr}  \cr
}
\]`

The resulting matrix `$C\in M_{m\times r}(F)$` is called the **matrix product** of the two matrices `\(A\)` and `\(B\)`. 

### Notes 

* The matrix product of two matrices `\(A\)` and `\(B\)` is a matrix `\(C\)`, whose matrix elements in the `\(i\)`-th row and `\(j\)`-th column equal the [dot products][bookofproofs$1049] of the `\(i\)`-th row vector of `\(A\)` with the `\(j\)`-th column vector of `\(B\)`, `\(i=1,\ldots,m\)`, `\(j=1,\ldots,r\)`.
* A matrix product is only possible if the number of rows of the first matrix equals the number of columns of the second matrix. 
* In general, the matrix product is not commutative, i.e. `$AB\neq BA.$`
