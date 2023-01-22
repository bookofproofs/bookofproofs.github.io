layout: example
categories: branches,algebra
nodeid: bookofproofs$7948
orderid: 2
parentid: bookofproofs$7945
title: Solution to a Degenerated Diagonal SLE
description: SOLUTION TO A DEGENERATED DIAGONAL SLE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$7937
keywords: degenerated,diagonal,sle,solution
contributors: bookofproofs

---


---

We extend our [previous example][bookofproofs$7947] by some zero lines: The [extended coefficient matrix][bookofproofs$7941] has now the form

`$$\left(\begin{array}{ccccccc|c}\alpha_{11}& 0&\ldots&0&0&\ldots&0&\beta_1\\
0& \alpha_{22}&\ldots&0&\vdots&\vdots&\vdots&\beta_2\\
\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\vdots&\vdots\\
0& 0 &\ldots&\alpha_{rr}&0&\ldots&0&\beta_r\\
\vdots& \vdots &\ldots&0&0&\ldots&0&\beta_{r+1}\\
\vdots& \vdots &\ldots&\vdots&\vdots&\ldots&\vdots&\vdots\\
0& \ldots &\ldots&0&0&\ldots&0&\beta_m\\
\end{array}\right)$$`

In this SLE, there exists an `$r\in \{1,\ldots,\min(m,n)\},$` for which `$\alpha_{jj}\neq 0$` for `$j=1,\ldots,r,$` and `$\alpha_{jj}=0$` for `$j=r+1,\ldots,m.$`

Like in the previous example, the solution of the SLE is given by `$$x_j:=\frac{\beta_j}{\alpha_{jj}}$$` for  `$j=1,\ldots,r.$` For the remaining `$x_j$` with `$j=r+1,\ldots,n$` we can choose arbitrary values, if `$\beta_j=0$` __for all__ `$j=r+1,\ldots m.$` Please note that the whole SLE has no (simultaneous) solution, if `$\beta_j\neq 0$` __for at least one__ of the "zero-lines" `$j=r+1,\ldots m.$`
