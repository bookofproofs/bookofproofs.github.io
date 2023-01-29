layout: proof
categories: branches,analysis
nodeid: bookofproofs$8340
orderid: 50
parentid: bookofproofs$8339
title: 
description: PROOF OF RIEMANN INTEGRAL OF A PRODUCT OF CONTINUOUSLY DIFFERENTIABLE FUNCTIONS WITH SINE ★ master graduate maths ✔ visit BookOfProofs now!
references: bookofproofs$581
keywords: riemann integral of continuously differentiable functions,product of sine,proof
contributors: bookofproofs

---


---

* By hypothesis, `$[a,b]$` is a [closed real interval][bookofproofs$1153] and `$f:[a,b]\to\mathbb R$` is a [continuously differentiable function][bookofproofs$6812].
* We define for `$y\in\mathbb R,$` the [Riemann integral][bookofproofs$1763]  `$F(y):=\int_{a}^{b}f(x)\sin(yx)dx.$`
* Please note that the derivative of `$\frac {d}{dx}-\frac {\cos(yx)}{y}$` is `$sin(xy).$` 
* With this result, if `$y\neq 0,$` then the [partial integration][bookofproofs$8337] gives us `$$F(y)=\underbrace{-f(x)\frac{\cos(yx)}{y}\Rule{1px}{4ex}{2ex}^b_a}_{=:A}+\underbrace{\frac 1y\int_a^b f'(x)\cos(yx)dx}_{=:B}.\label{eq:E20241}\tag{1}$$`
* Because `$f$` and the [derivative][bookofproofs$1370] `$f'$` are [continuous][bookofproofs$1260] and because `$[a,b]$` is closed, [both continuous functions are bounded][bookofproofs$6697].
* By definition of [bounded functions][bookofproofs$302] there is a constant `$M\ge 0$` such that for all  `$$|f(x)|\le M,\quad |f'(x)|\le M,\quad\text{for all }x\in[a,b].$$`
* Since `$\cos(yx)\le 1$` for all `$x\in[a,b],$` the term `$A$` in `$(\ref{eq:E20241})$` can be approximated to `$|A|\le \frac{2M}{|y|}$` and the term `$B$` to `$|B|\le \frac{(b-a)M}{|y|},$` where `$|y|$` is the [absolute value][bookofproofs$583] of `$y.$`
* Since both upper bounds [tend to zero][bookofproofs$6683] as `$|y|$` [tends to infinity][bookofproofs$6683], we have `$\lim_{|y|\to\infty}F(y)=0.$`
