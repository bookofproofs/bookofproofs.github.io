layout: section
categories: branches,algebra
nodeid: bookofproofs$7951
orderid: 500
parentid: bookofproofs$138
title: Solving General Systems Of Linear Equations - Gaussian Method
description: SOLVING GENERAL SYSTEMS OF LINEAR EQUATIONS - GAUSSIAN METHOD &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$7937
keywords: equations,gaussian,general,linear,method,solving,systems
contributors: bookofproofs


---


---

In the proceeding examples, in particular, the example of [backward substitution][bookofproofs$7949], we have seen that if an SLE is in an upper triangular form,

`$$\left(\begin{array}{ccccccc|c}\alpha_{11}& \alpha_{12}&\ldots&\alpha_{1r}&\alpha_{1,r+1}&\ldots&\alpha_{1n}&\beta_1\\
0& \alpha_{22}&\ldots&\alpha_{2r}&\alpha_{2,r+1}&\ldots&\alpha_{2n}&\beta_2\\
\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\vdots&\vdots\\
0& 0 &\ldots&\alpha_{rr}&\alpha_{r,r+1}&\ldots&\alpha_{rn}&\beta_r\\
\vdots& \vdots &\ldots&0&0&\ldots&0&\beta_{r+1}\\
\vdots& \vdots &\ldots&\vdots&\vdots&\ldots&\vdots&\vdots\\
0& \ldots &\ldots&0&0&\ldots&0&\beta_m\\
\end{array}\right)$$`

then we can easily decide whether there is no solution to the system or we can find an explicit solution to it. Therefore, if we could find some way to transform any given SLE into an upper triangular form, __without changing the set of its solutions__, then this would enable us to solve any given SLE, provided that it has a solution. Indeed, such a transformation exists and was found by the German mathematician <a href="https://mathshistory.st-andrews.ac.uk/Biographies/Gauss/">Carl Friedrich Gauss</a> (1777 - 1855). In the following, we define elementary Gaussian operations allowing us to transform any given SLE into an upper triangular form.
