layout: proof
categories: branches,analysis
nodeid: bookofproofs$1733
orderid: 50
parentid: bookofproofs$1732
title: 
description: Proof of ESTIMATE FOR THE REMAINDER TERM OF COMPLEX EXPONENTIAL FUNCTION ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: complex,estimate,exponential,function,remainder,term,proof
contributors: bookofproofs

---


---

We can estimate the remainder term of the exponential series as follows

* By the definition of the [complex exponential series][bookofproofs$312], we have `$$|r_{N + 1}(z)|= \sum_{n=N+1}^\infty\frac{z^n}{n! }.$$`
* The [triangle inequality][bookofproofs$1253] gives us
`$$\ldots \le \sum_{n=N+1}^\infty\frac{|z|^n}{n! }.$$`  
* By the [distributivity law for real numbers][bookofproofs$520] and the [properties of the absolute value for real numbers][bookofproofs$619], `$$\ldots =\frac{|z|^{N+1}}{(N+1)!}\left(1 + \frac{|z|}{N+2} + \frac{|z|^2}{(N+2)(N+3)} + \ldots + \frac{|z|^k}{(N+2)\cdot\ldots\cdot(N+k+1)} + \ldots \right).$$` 
* Finally, by the [rules for calculating with inequalities or real numbers][bookofproofs$594] we get `$$\le\frac{|z|^{N+1}}{(N+1)!}\left(1 + \frac{|z|}{N+2} + \left(\frac{|z|}{(N+2)}\right)^2 + \ldots + \left(\frac{|z|}{(N+2)}\right)^k + \ldots \right).$$` 
* If we require that `\(|z|\le\frac{N+2}{2}\)` then we have 
`\[\frac{|z|}{N+2}\le \frac{\frac{N+2}{2}}{N+2}=\frac 12.\]`
* Therefore, for `\(|z|\le\frac{N+2}{2}\)` it follows with the formula for the [infinite geometric series][bookofproofs$1353].
`$$|r_{N + 1}(z)|\le  \frac{|z|^{N+1}}{(N+1)!}\left(1 + \frac{1}{2} + \frac{1}{4} + \ldots + \frac{1}{2^k}  + \ldots \right)=2\frac{|z|^{N+1}}{(N+1)!}.$$`
