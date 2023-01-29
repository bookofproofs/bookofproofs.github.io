layout: proof
categories: branches,analysis
nodeid: bookofproofs$8445
orderid: 50
parentid: bookofproofs$8444
title: 
description: PROOF OF TAYLOR'S FORMULA WITH REMAINDER TERM OF LAGRANGE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: taylor's formula with remainder term of lagrange,proof
contributors: bookofproofs

---


---

* By hypothesis, `$I\subset\mathbb R$` is an [interval][bookofproofs$1153] and `$f:I\to\mathbb R$` is a [$(n+1)$ times continuously differentiable function][bookofproofs$6205].
* Let `$a,x\in I.$` 
* By the [Taylor's formula][bookofproofs$8440], we have `$$f(x)=f(a)+\sum_{k=1}^n \frac{f^{\{k\}}(a)}{k!}(x-a)^k+R_{n+1}(x)$$` with the remainder term `$$R_{n+1}(x)=\frac 1{n!}\int_a^x (x-t)^nf^{\{n+1\}}(t)dt.$$`
* Since the `$(n+1)$`-th [derivative][bookofproofs$6204] is [continuous][bookofproofs$1260], the [mean value theorem for Riemann integrals][bookofproofs$1772] yields that there is a value `$\xi$` between `$a$` and `$x$` such that 
`$$\begin{align}R_{n+1}(x)&=\frac 1{n!}\int_a^x (x-t)^nf^{\{n+1\}}(t)dt\nonumber\\
&=f^{\{n+1\}}(\xi)\int_a^x \frac {(x-t)^n}{n!}dt\nonumber\\
&=-f^{\{n+1\}}(\xi)\frac{(x-t)^{n+1}}{(n+1) !}\;\Rule{1px}{4ex}{2ex}^{x}_{a}\nonumber\\
&=\frac{f^{\{n+1\}}(\xi)}{(n+1) !}(x-a)^{n+1}\nonumber\\
\end{align}$$`
