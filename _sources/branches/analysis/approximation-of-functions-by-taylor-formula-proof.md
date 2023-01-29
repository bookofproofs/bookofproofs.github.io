layout: proof
categories: branches,analysis
nodeid: bookofproofs$8447
orderid: 50
parentid: bookofproofs$8446
title: 
description: PROOF OF APPROXIMATION OF FUNCTIONS BY TAYLOR'S FORMULA &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: taylor's formula as an approximation,approximation by taylor's formula,proof
contributors: bookofproofs

---


---

* By hypothesis, `$I\subset\mathbb R$` is an [interval][bookofproofs$1153] and `$f:I\to\mathbb R$` is a [$n$ times continuously differentiable function][bookofproofs$6205] .
* Let `$a\in I.$` 
* The [Taylor's formula with remainder term of lagrange][bookofproofs$8444] of the `$n$`-th order yields
`$$\begin{align}
f(x)-\sum_{k=0}^{n-1} \frac{f^{\{k\}}(a)}{k !}(x-a)^k&=\frac{f^{\{n\}}(\xi)}{n !}(x-a)^{n}\nonumber\\
&=\frac{f^{\{n\}}(a)}{n !}(x-a)^{n}+\frac{f^{\{n\}}(\xi)-f^{\{n\}}(a)}{n !}(x-a)^{n}\nonumber.\end{align}$$`
* Define a function `$r:I\to\mathbb R$` (note: the value of `$\xi$` depends on every `$x$`, since it lies between `$a$` an `$x$`): `$$r(x):=\frac{f^{\{n\}}(\xi)-f^{\{n\}}(a)}{n !}.$$`
* It follows from the hypothesis that the `$n$`-th [derivative][bookofproofs$6771] `$f^{\{n\}}$` is [continuous][bookofproofs$1260].
* Because of the [continuity of functions is preserved for arithmetic operations][bookofproofs$1261], and because `$\xi$` lies between `$a$` an `$x,$` we get for the [limit][bookofproofs$6683] `$$\lim_{x\to a} r(x)=\lim_{\xi\to a} \frac{f^{\{n\}}(\xi)-f^{\{n\}}(a)}{n !}=0.$$`
