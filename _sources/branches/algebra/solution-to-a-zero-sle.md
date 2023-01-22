layout: example
categories: branches,algebra
nodeid: bookofproofs$7946
orderid: 0
parentid: bookofproofs$7945
title: Solution to a Zero SLE
description: SOLUTION TO A ZERO SLE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$7937
keywords: sle,solution,zero
contributors: bookofproofs

---


---

Our first example is a rather degenerated SLE with an [extended coefficient matrix][bookofproofs$7941] consisting of a [zero matrix][bookofproofs$1052]:

`$$\left(\begin{array}{ccc|c}0& \ldots&0&\beta_1\\
0& \ldots&0&\beta_2\\
\vdots&\vdots&\vdots&\vdots\\
0& \ldots&0&\beta_m\end{array}\right)$$`

Each [linear equation][bookofproofs$1043] in such an SLE has the form

`$$0x_1+0x_2+\ldots+0x_n=\beta_j$$`

for `$j=1,\ldots,m$` and [we have seen in a corollary][bookofproofs$7939] that these equations have
* either no solutions at all if `$\beta_j\neq 0$`
* or infinitely many solutions with arbitrary choices for the unknowns `$x_1,\ldots,x_n,$` if `$\beta_j=0.$`

From this, we can conclude that the above SLE will have
* either no solutions at all, if `$\beta_j\neq 0$` for __at least one__ `$j$` with `$1\le j \le m,$`
* or infinitely many solutions with arbitrary choices for the unknowns `$x_1,\ldots,x_n,$` if `$\beta_j=0$` __for all__ `$j$` with `$1\le j \le m.$`
