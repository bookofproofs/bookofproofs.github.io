layout: theorem
categories: branches,analysis
nodeid: bookofproofs$8440
orderid: 50
parentid: bookofproofs$220
title: Taylor's Formula
description: TAYLOR'S FORMULA ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: taylor's formula
contributors: bookofproofs

---


---

Let `$I\subset\mathbb R$` be an [interval][bookofproofs$1153] and `$f:I\to\mathbb R$` be a [$(n+1)$ times continuously differentiable function][bookofproofs$6205]. For any values `$a,x\in I,$` the value `$f(x)$` can be written as

`$$f(x)=f(a)+\sum_{k=1}^n \frac{f^{\{k\}}(a)}{k!}(x-a)^k+R_{n+1}(x)$$`
where `$k!$` denotes the [factorial][bookofproofs$1005], `$f^{\{k\}}$` denots the `$k$`-th derivative of `$f$` and the remainder term `$R_{n+1}$` equals the [Riemann integral][bookofproofs$1763].
`$$R_{n+1}(x)=\frac 1{n!}\int_a^x (x-t)^nf^{\{n+1\}}(t)dt.$$`
