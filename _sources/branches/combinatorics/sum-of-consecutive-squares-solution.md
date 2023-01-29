layout: solution
categories: branches,combinatorics
nodeid: bookofproofs$8525
orderid: 50
parentid: bookofproofs$8524
title: 
description: SOLUTION OF SUM OF SQUARES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8404
keywords: sum of consecutive squares,solution,solution
contributors: bookofproofs

---


---

* Note that we can write `$x^2$` using the [falling factorial powers][bookofproofs$1399] as `$x^2=x(x-1)+x=x^{\underline{2}}+x^{\underline{1}}.$`
* Now, `$$\begin{align}1^2+2^2+3^2+\ldots+n^2&=\sum_{x=1}^n (x^{\underline{2}}+x^{\underline{1}})\nonumber\\
&=\left(\frac{x^{\underline 3}}{3}+\frac{x^{\underline 2}}{2}\right)\;\Rule{1px}{4ex}{2ex}^{n+1}_{1}\nonumber\\
&=\left(\frac{x(x-1)(x-2)}{3}+\frac{x(x-1)}{2}\right)\;\Rule{1px}{4ex}{2ex}^{n+1}_{1}\nonumber\\
&=\frac{(n+1)n(n-1)}{3}+\frac{(n+1)n}{2}\nonumber\\
&=\frac{n(n+1)(2n+1)}{6}.\nonumber
\end{align}$$`
