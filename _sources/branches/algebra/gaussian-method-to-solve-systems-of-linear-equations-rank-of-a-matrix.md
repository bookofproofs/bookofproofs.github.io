layout: definition
categories: branches,algebra
nodeid: bookofproofs$7955
orderid: 200
parentid: bookofproofs$7951
title: Gaussian Method to Solve Systems of Linear Equations, Rank of a Matrix
description: GAUSSIAN METHOD TO SOLVE SYSTEMS OF LINEAR EQUATIONS, RANK OF A MATRIX &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$7937
keywords: equations,gaussian,gaussian method,linear,matrix,method,rank,solve,systems
contributors: bookofproofs

---


---

The **Gaussian method** is a method to solve a given [system of linear equations (SLE)][bookofproofs$1044] written in the form of an [extended coefficient matrix][bookofproofs$7941]:

`$$A|\beta:=\left(\begin{array}{ccc|c}\alpha_{11}& \ldots&\alpha_{1n}&\beta_1\\ 
\alpha_{21}& \ldots&\alpha_{2n}&\beta_2\\ 
\vdots&\vdots&\vdots&\vdots\\ 
\alpha_{m1}& \ldots&\alpha_{mn}&\beta_m\end{array}\right)\quad\quad ( * )$$`

with `$\beta_i,a_ij\in F$`, where `$F$` is a [field][bookofproofs$557] and not all `$\beta_i,a_{ij}$` are zero[^1].

The method consists of the following two steps:

1. Bring the system `$( * )$` to an [upper triangular][bookofproofs$7949] form 
`$$\left(\begin{array}{ccccccc|c}a_{11}& a_{12}&\ldots&a_{1r}&a_{1,r+1}&\ldots&a_{1n}&b_1\\ 
0& a_{22}&\ldots&a_{2r}&a_{2,r+1}&\ldots&a_{2n}&b_2\\ 
\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\vdots&\vdots\\ 
0& 0 &\ldots&a_{rr}&a_{r,r+1}&\ldots&a_{rn}&b_r\\ 
\vdots& \vdots &\ldots&0&0&\ldots&0&b_{r+1}\\ 
\vdots& \vdots &\ldots&\vdots&\vdots&\ldots&\vdots&\vdots\\ 
0& \ldots &\ldots&0&0&\ldots&0&b_m\\ 
\end{array}\right)\quad \quad ( * * )$$` 
using the [elementary Gaussian operations][bookofproofs$7952], where[^2] all the `$a_{ii}\neq 0$` for `$i=1,\ldots $` with some `$r\in\{1,\ldots,\min(m,n)\}.$` The number `$r$` is called the **rank** of the [coefficient matrix][bookofproofs$7941] `$A.$`
The first step might involve the following steps:
   1. Remove all columns consisting of only zero elements.
   2. Set `$k=1$`.
   3. Check, if in the remaining system, the element `$\alpha_{kk}$` is non-zero, if so proceed with the step 5.
   4. Let `$i$` be the row, in which in the first column the element `$\alpha_{ik}$` is not zero. Exchange the rows `$1$` and `$i,$` i.e. set `$a_{1k}:=\alpha_{ik}$` (applying Gaussian operation `$I.$`)[^3] 
   5. To set the numbers `$\alpha_{2k},\ldots,\alpha_{mk}$` to zero, add to the rows `$2,\ldots,m$` a suitable multiple of the `$k$`-th row (applying Gaussian operation `$III.$`)
   6. If the upper triangular form `$( * * )$` has been reached, end.
   7. Otherwise set `$k=k+1$` and go back to step 3. 
2. If in the system `$( * * )$` `$b_j\neq 0$` for at least one `$j > r,$` then the system `$( * )$` has no solutions[^4]. Otherwise, we can solve the system `$( * * )$` using the [backward substitution][bookofproofs$7949].

The Gaussian method makes use of the lemma that [the elementary Gaussian operations do not change the set of solutions][bookofproofs$7953] of the system `$( * ).$` Thus, the solution to `$( * * )$` found in the second step is also a solution to `$( * ).$`

[^1]: If so, we have the case [discussed in this example][bookofproofs$7946].
[^2]: In the system `$( * * )$` we have used the Latin notation `$a,b$` instead of the Greek notation `$\alpha, \gamma$` to indicate that these elements might be different from the original system `$( * )$` after having applied the elementary Gaussian operations.

[^3]: When implementing the algorithm for the computer, one should choose the row `$i$` with the maximal absolute value of `$\alpha_{i1}$` to make the algorithm numerically stable.

[^4]: As we have seen in [this example][bookofproofs$7948].