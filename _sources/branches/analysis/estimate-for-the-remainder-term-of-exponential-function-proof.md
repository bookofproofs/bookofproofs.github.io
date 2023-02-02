layout: proof
categories: branches,analysis
nodeid: bookofproofs$1362
orderid: 50
parentid: bookofproofs$1361
title: 
description:  Proof of ESTIMATE FOR THE REMAINDER TERM OF EXPONENTIAL FUNCTION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: exponential series,exponential function,proof,proof
contributors: bookofproofs

---


---

Using the definition of the [exponential series][bookofproofs$281], the [triangle inequality][bookofproofs$618], the [distributivity law for real numbers][bookofproofs$520], the [properties of the absolute value for real numbers][bookofproofs$619], and the [rules for calculating with inequalities or real numbers][bookofproofs$594] we can estimate the remainder term of the exponential series as follows

`\[\begin{array}{rcll}
|r_{N + 1}(x)|&=& \sum_{n=N+1}^\infty\frac{x^n}{n! }&\text{definition of the exponential series}\\
&\le &\sum_{n=N+1}^\infty\frac{|x|^n}{n! }&\text{triangle inequality}\\
&=&\frac{|x|^{N+1}}{(N+1)!}\left(1 + \frac{|x|}{N+2} + \frac{|x|^2}{(N+2)(N+3)} + \ldots + \frac{|x|^k}{(N+2)\cdot\ldots\cdot(N+k+1)} + \ldots \right)&\text{properties of absolute value and distributivity law}\\
&\le&\frac{|x|^{N+1}}{(N+1)!}\left(1 + \frac{|x|}{N+2} + \left(\frac{|x|}{(N+2)}\right)^2 + \ldots + \left(\frac{|x|}{(N+2)}\right)^k + \ldots \right)&\text{rules for calculating with inequalities}\\
\end{array}\]`

If we require that `\(|x|\le\frac{N+2}{2}\)` then we have 
`\[\frac{|x|}{N+2}\le \frac{\frac{N+2}{2}}{N+2}=\frac 12.\]`

Therefore, for `\(|x|\le\frac{N+2}{2}\)` it follows with the formula for the [infinite geometric series][bookofproofs$1353].
`\[\begin{array}{rcl}
|r_{N + 1}(x)|&\le & \frac{|x|^{N+1}}{(N+1)!}\left(1 + \frac{1}{2} + \frac{1}{4} + \ldots + \frac{1}{2^k}  + \ldots \right)\\
&=&2\frac{|x|^{N+1}}{(N+1)!}.
\end{array}\]`
