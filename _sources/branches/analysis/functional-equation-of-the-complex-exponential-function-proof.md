layout: proof
categories: branches,analysis
nodeid: bookofproofs$1737
orderid: 50
parentid: bookofproofs$1735
title: 
description:  Proof of FUNCTIONAL EQUATION OF THE COMPLEX EXPONENTIAL FUNCTION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: complex,equation,exponential,function,functional,complex exponential function,proof
contributors: bookofproofs

---


---

Let `\(x,y\in\mathbb R\)` be [complex numbers][bookofproofs$1698]. By [definition of the complex exponential function][bookofproofs$312],

`\[\exp(x)=\sum_{n=0}^\infty\frac{x^n}{n!}\quad\text{ and }\quad\exp(y)=\sum_{n=0}^\infty\frac{y^n}{n!}\]`

are [absolutely convergent complex series][bookofproofs$1725] for all `\(x,y\in\mathbb C\)`. Therefore, their [Cauchy product][bookofproofs$1736].
`\[\sum_{n=0}^\infty c_n=\left(\sum_{n=0}^\infty\frac{x^n}{n{!}}\right)\cdot\left(\sum_{n=0}^\infty\frac{y^n}{n{!}}\right)\]`
is also an absolutely convergent complex series. Moreover, applying the [binomial theorem][bookofproofs$1397], we get
`\[c_n:=\sum_{k=0}^n\frac{x^{n-k}}{(n-k)! }\cdot\frac{y^k}{k! }=\frac1{n!}\sum_{k=0}^n\binom nk x^{n-k}y^k=\frac{(x+y)^n}{n! }.\]`
It follows
`\[\exp(x+y)=\sum_{n=0}^\infty\frac{(x+y)^n}{n! }=\left(\sum_{n=0}^\infty\frac{x^n}{n{ ! }}\right)\cdot\left(\sum_{n=0}^\infty\frac{y^n}{n{! }}\right)=\exp(x)\cdot \exp(y).\]`
