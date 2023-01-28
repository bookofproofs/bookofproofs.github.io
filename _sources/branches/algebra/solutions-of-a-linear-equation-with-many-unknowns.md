layout: corollary
categories: branches,algebra
nodeid: bookofproofs$7939
orderid: 50
parentid: bookofproofs$1043
title: Solutions of a Linear Equation with many Unknowns
description: SOLUTIONS OF A LINEAR EQUATION WITH MANY UNKNOWNS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$7937
keywords: equation,linear,many,solutions,unknowns
contributors: bookofproofs

---


---

Let `$n\ge 1$` and let `$\alpha_1x_1+\ldots+\alpha_nx_n=\gamma$` be a [linear equation][bookofproofs$1043] with the unknowns `$x_1,\ldots,x_n$` and the elements `$\alpha_1,\ldots,\alpha_n,\gamma$` of a [field][bookofproofs$557] `$F.$` There are the following cases for finding a solution to this equation:

### Case `$1$`: Not all coefficients `$\alpha_1,\ldots,\alpha_n$` are `$0$`.

We can re-index the coefficients and unknowns appropriately to let `$\alpha_1=0,\ldots,\alpha_{m-1}=0$` and `$\alpha_{m}\neq 0,\alpha_{m+1}\neq 0,\ldots,\alpha_n\neq 0.$` The (homogenous or inhomogenous) equation is then given by
`$$0 x_1 + 0 x_{m-1} + \alpha_m x_m + \alpha_{m+1} x_{m+1} + \ldots +\alpha_n x_n=\gamma.$$`
Then
`$$x_m:=\frac{\gamma-\alpha_{m+1}x_{m+1}-\ldots-\alpha_n x_n}{\alpha_m}\quad ( * )$$`
is a solution for any choice of the `$n-1$` unknowns `$x_1,\ldots,x_{m-1},x_{m+1}\ldots,x_n\in F.$` We say that the solution `$( * )$` has `$n-1$` **degrees of freedom**. If `$\gamma=0$` (the equation is homogenous), then we call the special choice `$x_1=0,\ldots,x_n=0$` the **trivial solution** of `$( * ).$`

### Case `$2$`: All coefficients `$\alpha_1,\ldots,\alpha_n$` are `$0$`, but `$\gamma\neq 0.$`

The inhomogenous equation is then given by
`$$0 x_1 +  \ldots +0x_n=\gamma.$$`
In this case, for any choice of the `$n$` unknowns `$x_1,\ldots,x_n\in F,$` the equation has no solution.

### Case `$3$`: All coefficients `$\alpha_1,\ldots,\alpha_n$` are `$0$`, and `$\gamma = 0.$`

The homogenous equation is then given by
`$$0 x_1 +  \ldots +0x_n=0$$`

Any choice of the `$n$` unknowns `$x_1,\ldots,x_n\in F,$` is a solution of the equation.
