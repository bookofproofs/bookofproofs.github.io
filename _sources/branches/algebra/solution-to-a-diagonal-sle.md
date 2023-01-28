layout: example
categories: branches,algebra
nodeid: bookofproofs$7947
orderid: 100
parentid: bookofproofs$7945
title: Solution to a Diagonal SLE
description: SOLUTION TO A DIAGONAL SLE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$7937
keywords: diagonal,sle,solution
contributors: bookofproofs

---


---

The next example is a more interesting SLE. While it is quite simple, it has [non-trivial][bookofproofs$1044] solutions. Its [extended coefficient matrix][bookofproofs$7941] contains a [diagonal matrix][bookofproofs$7944]

`$$\left(\begin{array}{cccc|c}\alpha_{11}& 0&\ldots&0&\beta_1\\
0& \alpha_{22}&\ldots&0&\beta_2\\
\vdots&\vdots&\ddots&\vdots\\
0& 0 &\ldots&\alpha_{mm}&\beta_m\end{array}\right)$$`

in which we assume all `$\alpha_jj\neq 0$` for `$j=1,\ldots,m.$` Please note that the coefficient matrix here is a [square matrix][bookofproofs$1056], since it has `$m$` columns and `$m$` rows. Each [linear equation][bookofproofs$1043] in such an SLE has the form

`$$\begin{array}{rcl}0x_1+\ldots+0x_{j-1}+\alpha_{jj}x_j+0x_{j+1}+\ldots+0x_n&=&\beta_j\\
\alpha_{jj}x_j&=&\beta_j\end{array}$$`
and therefore the SLE has the solution `$$x_j:=\frac{\beta_j}{\alpha_{jj}}$$`
for `$j=1,\ldots,m.$`

This example shows us that a diagonal SLE is not really a __system__ of linear equations since the simultaneous solutions to all equations are independent of each other. In other words, the system does not pose any constraints to the solution of every single equation which would depend on other equations.
