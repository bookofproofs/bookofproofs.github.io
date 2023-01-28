layout: definition
categories: branches,algebra
nodeid: bookofproofs$8151
orderid: 200
parentid: bookofproofs$211
title: Elementary Symmetric Functions
description: ELEMENTARY SYMMETRIC FUNCTIONS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$6735
keywords: elementary symmetric functions,elementary symmetric function
contributors: bookofproofs

---


---

Let `$a_1,\ldots,a_r\in R$` be elements of a [commutative ring][bookofproofs$880] and let `$x$` be a variable. We form the [polynomial][bookofproofs$487]
`$$\begin{array}{rcl}p(x)&:=&(x-a_1)\cdots (x-a_r)\\
&=&x^r+(-1)^1\Sigma_1x^{r-1}+(-1)^2\Sigma_2x^{r-2}+\ldots+(-1)^{r-1}\Sigma_{r-1}x+(-1)^{r}\Sigma_r
\end{array}$$`

The coefficients `$\Sigma_1,\ldots,\Sigma_r$` are called **elementary symmetric** [functions][bookofproofs$592] `$\Sigma_k:R^r\to R$`, which are defined as [sums][bookofproofs$261]
`$$\begin{array}{rcl}
\Sigma_1(a_1,\ldots,a_r)&:=&\sum_{1\le k\le r}a_k\\
\Sigma_2(a_1,\ldots,a_r)&:=&\sum_{1\le k < l\le r}a_ka_l\\
\Sigma_3(a_1,\ldots,a_r)&:=&\sum_{1\le k < l < m\le r}a_ka_la_m\\
\vdots&&\\
\Sigma_r(a_1,\ldots,a_r)&:=&a_1\cdots a_r\\
\end{array}$$`
