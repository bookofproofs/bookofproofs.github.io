layout: proof
categories: branches,algebra
nodeid: bookofproofs$1047
orderid: 50
parentid: bookofproofs$1045
title: By Induction
description: PROOF BY INDUCTION PROOF OF FUNDAMENTAL LEMMA OF HOMOGENEOUS SYSTEMS OF LINEAR EQUATIONS &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$561
keywords: equations,fundamental,homogeneous,lemma,linear,systems,proof
contributors: bookofproofs

---


---

Let `\(\alpha_{ij}\in F\)` and `\(F\)` be an [field][bookofproofs$557], and let 
`\[\begin{array}{ccl}
\alpha_{11}X_1+\ldots+\alpha_{1n}X_n&=&0\\
\alpha_{21}X_1+\ldots+\alpha_{2n}X_n&=&0\\
\vdots&\vdots&\vdots\\
\alpha_{m1}X_1+\ldots+\alpha_{mn}X_n&=&0\\
\end{array}~~~~~~~~~~~~~~~~ ( * ) \]`
be a [homogeneous system of linear equations][bookofproofs$1044] with  `\(n\)` unknowns `\(X_1,\ldots,X_n\)` and (`\(1\le m < n\)`) equations. We have to show that the equation system `\( ( * ) \)` has a non-trivial solution.

First, we observe the following:

1. It is sufficient to assume `\(m=n-1\)` since if we have found a non-trivial solution for this case, it is also a solution of the more general case `\(m < n - 1\)` (after removing some more equations from the system).
1. We can assume `\(\alpha_{11}\neq 0\)`. If in `\( ( * )\)` all coefficients `\( \alpha_{ij} \)` were zero, then any elements of the field `\(F\)` replacing the unknowns `\(X_1,\ldots,X_n\)` would be a non-trivial solution. If `\(\alpha_{11}= 0\)` but some other `\(\alpha_{ij}\neq 0\)`, we can change the order of the equations by switching the `\(i\)`-th equation with the `\(1\)`-st equation and re-numbering the `\(j\)`-th unknown with the `\(1\)`-st unkonwn, so that   `\(\alpha_{11}\neq 0\)`. Note that these operations do not change the non-trivial solution, if it exists.
1. We can assume that besides `\(\alpha_{11}\)`, all other coefficients in the first column equal zero `\(\alpha_{21}=\alpha_{31}=\ldots=\alpha_{m1}=0\)`. In order to transform the equation system into this form, we have (for `\(i=2,\ldots,m\)`) to multiply the first equation with `\(\alpha_{i1}\)` and subtract the resulting product form the `\(\alpha_{11}\)` multiple of the `\(i\)`-th equation. Note that these operations do not change the non-trivial solution, if it exists, either.

After these preparations, it is possible to prove the lemma [by induction][bookofproofs$657] on the number of unknowns. 

### Base Case `\(n=2\)`. 

The equation system 

`\[\begin{array}{ccl}
\alpha_{11}X_1+\alpha_{12}X_2&=&0\\
\end{array}\]`
has the solution `\(X_1:=\beta_1=-\frac{\alpha_{12}}{\alpha_{11}} X_2\)`, `\(X_2:=\beta_2\in F\)`.

### Induction step `\(n > 2\)`. 

Let the fundamental lemma be proven for `\(m\ge 2\)` unknowns. We have to find a non-trivial solution of the equation system 
`\[\begin{array}{cllcl}
\alpha_{11}X_1&+&\alpha_{12}X_2+\ldots+\alpha_{1n}X_n&=&0\\
0&+&\alpha_{22}X_2+\ldots+\alpha_{2n}X_n&=&0\\
\vdots&&\vdots&\vdots&\vdots\\
0&+&\alpha_{m2}X_2+\ldots+\alpha_{mn}X_n&=&0\\
\end{array}~~~~~~~~~~~~~~~~~~~~~(1)\]`
According to the base case, there exist a non-trivial solution `\(b_2,\ldots,b_n\in F\)` of the equation system
`\[\begin{array}{lcl}
\alpha_{22}X_2+\ldots+\alpha_{2n}X_n&=&0\\
\vdots&\vdots&\vdots\\
\alpha_{m2}X_2+\ldots+\alpha_{mn}X_n&=&0\\
\end{array}~~~~~~~~~~~~~~~~~~~~~(2)\]`
Note that we have renumbered the unknowns of the smaller equation system  `\( (2) \)` from `\(X_1,\ldots,X_{n-1}\in F\)` to `\(X_2,\ldots,X_n\in F\)` in order to better embed them into the greater equation system `\( (1) \)`. Then the solution of the greater equation system is `\(X_1:=\beta_1=-\frac{\alpha_{12}}{\alpha_{11}} X_2 -\ldots -\frac{\alpha_{1n}}{\alpha_{11}} X_n\)`, `\(X_i:=\beta_i\in F\)`, `\(i=2,\ldots,n\)`.
