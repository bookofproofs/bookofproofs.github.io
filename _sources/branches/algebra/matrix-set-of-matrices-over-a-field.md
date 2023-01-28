layout: definition
categories: branches,algebra
nodeid: bookofproofs$1048
orderid: 50
parentid: bookofproofs$7942
title: Matrix, Set of Matrices over a Field
description: MATRIX, SET OF MATRICES OVER A FIELD &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$979,bookofproofs$6907
keywords: field,matrices,matrix,over,set
contributors: bookofproofs

---
In the following definition, we introduce the notion of a "matrix" from a pure notational perspective, without in any way considering interesting mathematical properties of matrices, like dimensions and basis, which we will deal later in detail.

---

Let `\(F\)` be a [field][bookofproofs$557] and let `\(\alpha_{ij}\in F\)` be arbitrary field elements for `\(i=1,\ldots,m\)`, `\(j=1,\ldots,n\)`. Then the structure

`\[
A:=\pmatrix{
\alpha_{11} & \alpha_{12} & \ldots & \alpha_{1n} \cr
\alpha_{21} & \alpha_{22} & \ldots & \alpha_{2n} \cr
\vdots & \vdots & \ddots & \vdots \cr
\alpha_{m1} & \alpha_{m2} & \ldots & \alpha_{mn} \cr
}
\]`

is called a **matrix** over the field `\(F\)` with `\(m\)` rows and `\(n\)` columns. 

The set of all matrices over the field `\(F\)` with `\(m\)` rows and `\(n\)` columns is denoted by `\(M_{m\times n}(F)\)`.


### Generalization


If `\(I\)` and `\(J\)` are [index sets][bookofproofs$6198], then the matrix `\(I\times J\)` is a [function][bookofproofs$592] of the form

`\(I\times J\longrightarrow F,\,(i,j)\longmapsto a_{ij}\,.\)`

and can be visualized as 
`\[{\begin{pmatrix}a_{11}&a_{12}&\ldots &a_{1n}&\ldots\\a_{21}&a_{22}&\ldots &a_{2n}&\ldots\\\vdots &\vdots &\ddots &\vdots \\a_{m1}&a_{m2}&\ldots &a_{mn}&\ldots\\
\vdots&\vdots&\ldots &\vdots&\ddots\end{pmatrix}}\]`
