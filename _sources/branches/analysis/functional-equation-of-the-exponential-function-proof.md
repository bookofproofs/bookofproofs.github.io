layout: proof
categories: branches,analysis
nodeid: bookofproofs$1416
orderid: 50
parentid: bookofproofs$1415
title: 
description:  Proof of FUNCTIONAL EQUATION OF THE EXPONENTIAL FUNCTION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: functional equation of the exponential function,exp functional equation,functional equation of exp,exponential function,proof
contributors: bookofproofs

---


---

Let `\(x,y\in\mathbb R\)` be [real numbers][bookofproofs$1105]. By [definition of the exponential function][bookofproofs$281],

`\[\exp(x)=\sum_{n=0}^\infty\frac{x^n}{n!}\text{ and }\exp(y)=\sum_{n=0}^\infty\frac{y^n}{n!}\]`

are [absolutely convergent series][bookofproofs$198] for all `\(x,y\in\mathbb R\)`. Therefore, their [Cauchy product][bookofproofs$1390].
`\[\sum_{n=0}^\infty c_n=\left(\sum_{n=0}^\infty\frac{x^n}{n{!}}\right)\cdot\left(\sum_{n=0}^\infty\frac{y^n}{n{!}}\right)\]`
is also an absolutely convergent series. Moreover, applying the [binomial theorem][bookofproofs$1397], we get
`\[c_n:=\sum_{k=0}^n\frac{x^{n-k}}{(n-k)!}\cdot\frac{y^k}{k!}=\frac1{n!}\sum_{k=0}^n\binom nk x^{n-k}y^k=\frac{(x+y)^n}{n!}.\]`
It follows
`\[\exp(x+y)=\sum_{n=0}^\infty\frac{(x+y)^n}{n!}=\left(\sum_{n=0}^\infty\frac{x^n}{n{!}}\right)\cdot\left(\sum_{n=0}^\infty\frac{y^n}{n{!}}\right)=\exp(x)\cdot \exp(y).\]`
