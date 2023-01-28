layout: definition
categories: branches,algebra
nodeid: bookofproofs$7949
orderid: 300
parentid: bookofproofs$7945
title: Solution to an Upper Triangular SLE - Backward Substitution
description: SOLUTION TO AN UPPER TRIANGULAR SLE - BACKWARD SUBSTITUTION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$7937
keywords: backward,backward substitution,sle,solution,substitution,triangular,upper
contributors: bookofproofs

---


---

### Introductory Example

In this example, the [extended coefficient matrix][bookofproofs$7941] contains an [upper triangular matrix][bookofproofs$1053]

`$$\left(\begin{array}{ccccccc|c}\alpha_{11}& \alpha_{12}&\ldots&\alpha_{1r}&\alpha_{1,r+1}&\ldots&\alpha_{1n}&\beta_1\\
0& \alpha_{22}&\ldots&\alpha_{2r}&\alpha_{2,r+1}&\ldots&\alpha_{2n}&\beta_2\\
\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\vdots&\vdots\\
0& 0 &\ldots&\alpha_{rr}&\alpha_{r,r+1}&\ldots&\alpha_{rn}&\beta_r\\
\vdots& \vdots &\ldots&0&0&\ldots&0&\beta_{r+1}\\
\vdots& \vdots &\ldots&\vdots&\vdots&\ldots&\vdots&\vdots\\
0& \ldots &\ldots&0&0&\ldots&0&\beta_m\\
\end{array}\right)$$`

In this SLE, there exists an `$r\in \{1,\ldots,\min(m,n)\},$` for which `$\alpha_{jj}\neq 0$` for `$j=1,\ldots,r,$` and `$\alpha_{jj}=0$` for `$j=r+1,\ldots,m.$`

We have seen already in the [previous example][bookofproofs$7948] that if `$\beta_j\neq 0$` __for at least one__ of the "zero-lines" `$j=r+1,\ldots m,$` then the whole SLE has no (simultaneous) solution. So let us assume `$\beta_j\neq 0$` __for all__ `$j=r+1,\ldots m.$` In this case, the solution of the SLE can be found as follows:

### Definition **Backward Substitution**

# Choose arbitrary values for the unknowns `$x_{r+1},\ldots, x_n$`.
(Please note that if `$r < n$`, the simultaneous solution has `$n-r$` degrees of freedom. Otherwise (if `$r=n$`), the solution is unique, as the following steps show:)
# Solve the `$r$`-th equation by setting
`$$x_r:=\frac 1{\alpha_{rr}}\left(\beta_r-\sum_{j=r+1}^n \alpha_{rj}x_j\right)$$`
For `$r=n$` the equation has the form
`$$x_n:=\frac {\beta_n}{\alpha_{nn}}$$`
1. Since  `$x_r$` is now known, we can subtitute it in the `$r-1$`-th equation and find a value for the unknown `$x_{r-1}.$`
1. We can repeat this process for all remaining unknowns, i.e. those with the indices `$r-2, r-3,\ldots, 1.$`

This solving approach is called backward substitution and can be written as the following formula:

`$$x_i:=\frac 1{\alpha_{ii}}\left(\beta_i-\sum_{j=i+1}^n \alpha_{ij}x_j\right),\quad\quad\text{for }i=r,r-1,\ldots,1.$$`
