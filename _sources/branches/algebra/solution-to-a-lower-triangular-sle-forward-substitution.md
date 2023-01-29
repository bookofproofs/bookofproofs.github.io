layout: definition
categories: branches,algebra
nodeid: bookofproofs$7950
orderid: 400
parentid: bookofproofs$7945
title: Solution to a Lower Triangular SLE - Forward Substitution
description: SOLUTION TO A LOWER TRIANGULAR SLE - FORWARD SUBSTITUTION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$7937
keywords: forward,forward substitution,lower,sle,solution,substitution,triangular
contributors: bookofproofs

---


---

### Introductory Example

A similar example, in which the [extended coefficient matrix][bookofproofs$7941] contains a [lower triangular matrix][bookofproofs$1053].
`$$\left(\begin{array}{lllllll|c}0& 0&\ldots&0&\ldots&\ldots&0&\beta_1\\
\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\vdots&\vdots\\
0& 0&\ldots&0&\ldots&\ldots&0&\beta_{r-1}\\
\alpha_{r1}& \alpha_{r2} &\ldots&\alpha_{rr}&0&\ldots&0&\beta_r\\
\alpha_{r+1,1}&\alpha_{r+1,2}&\ldots&\alpha_{r+1,r}&\alpha_{r+1,r+1}&\ldots&0&\beta_{r+1}\\
\vdots& \vdots &\ldots&\vdots&\vdots&\ddots&\vdots&\vdots\\
\alpha_{m1}& \ldots &\ldots&\alpha_{mr}&\alpha_{m,r+1}&\ldots&\alpha_{mn}&\beta_m\\
\end{array}\right)$$`

In this SLE, there exists an `$r\in \{1,\ldots,\min(m,n)\},$` for which `$\alpha_{jj}= 0$` for `$j=1,\ldots,r-1$` and `$\alpha_{jj}\neq 0$` for `$j=r,\ldots,m.$`

Similarly as the [previous example][bookofproofs$7048], if `$\beta_j\neq 0$` __for at least one__ of the "zero-lines" `$j=1,\ldots r-1,$` then the whole SLE has no (simultaneous) solution. Thus, assume `$\beta_j\neq 0$` __for all__ `$j=1,\ldots, r-1.$` In this case, the solution of the SLE can be found as follows:

### Definition **Forward Substitution**

# Choose arbitrary values for the unknowns `$x_{1},\ldots, x_{r-1}$`.
(Please note that if `$r > 1$`, the simultaneous solution has `$r-1$` degrees of freedom. Otherwise (if `$r=1$`), the solution is unique, as the following steps show:)
# Solve the `$r$`-th equation by setting
`$$x_r:=\frac 1{\alpha_{rr}}\left(\beta_r-\sum_{j=1}^{r-1} \alpha_{rj}x_j\right)$$`
For `$r=1,$` the equation has the form
`$$x_1:=\frac {\beta_1}{\alpha_{11}}$$`
1. Since  `$x_r$` is now known, we can subtitute it in the `$r+1$`-th equation and find a value for the unknown `$x_{r+1}.$`
1. We can repeat this process for all remaining unknowns, i.e. those with the indices `$r+2, r+3,\ldots, \min(m,n).$`

This solving approach is called forward substitution and can be written as the following formula:

`$$x_i:=\frac 1{\alpha_{ii}}\left(\beta_i-\sum_{j=1}^{\min(m,n)} \alpha_{ij}x_j\right),\quad\quad\text{for }i=1,2,\ldots,\min(m,n).$$`
