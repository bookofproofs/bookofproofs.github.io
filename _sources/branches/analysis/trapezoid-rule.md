layout: lemma
categories: branches,analysis
nodeid: bookofproofs$8341
orderid: 1100
parentid: bookofproofs$474
title: Trapezoid Rule
description: TRAPEZOID RULE ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: trapezoid rule
contributors: bookofproofs

---
The idea of the following lemma, known as the _trapezoid rule_ is illustrated in the following figure.


![trapezoidrule](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/trapezoidrule.png?raw=true)


For a given, "sufficiently smooth" function `$f:[a,b]\to\mathbb R$` we want to calculate the area under the curve of this function, which equals the integral `$\int_{a}^b f(x)dx.$` If for whatever reasons, the exact calculation of the integral is too complicated, we can approximate this area by calculating the area of the _trapezoid_ in the points `$a$`, `$b$`, `$f(b)$` and `$f(a)$` instead, which is easily found using the formula `$$(b-a)\frac{f(a)+f(b)}{2}.$$`

When doing so, we will make an error `$R.$` We can expect that this error gets smaller and smaller if we replace the original trapezoid by the sum of areas of `$n\ge 2$` smaller trapezoids with equal bases built as follows: 
* We choose the number of trapezoids `$n\ge 2.$`
* We choose the length of the basis of all trapezoids to be `$h:=\frac{b-a}n,$` such that we have `$n+1$` points `$x_\nu:=a+\nu h.$` By this choice, we will have `$x_0=a$` and `$x_n=b.$`
* Since the area of a single `$\nu$`-th smaller trapezoid (for `$\nu=1,\ldots,n$`) is given by `$$h\frac{f(x_\nu)+f(x_{\nu-1})}{2},$$` the sum of all these `$n$` trapezoids is given by `$$h\left(\frac{f(a)}{2}+\sum_{\nu=1}^{n-1}f(x_\nu)+\frac{f(b)}{2}\right),$$` which is an approximation of the actual integral.

The following lemma specifies what exactly is meant by "sufficiently smooth" and how good we can expect this approximation to be.

---

Let the function `$f:\mathbb R\to\mathbb R$` be a [twice continuously differentiable][bookofproofs$6812]. Let `$n\ge 1$` be a [natural number][bookofproofs$718]. For the [closed real interval][bookofproofs$1153] `$[a,b]$`, the [Riemann integral][bookofproofs$1763] `$\int_a^b f(x)dx$` can be approximated using the function values of `$f$` via `$$\int_a^b f(x)dx=\left(\frac{f(a)}{2}+\sum_{\nu=1}^{n-1}f(a+\nu h)+\frac{f(b)}{2}\right)h+R,$$`
where `$h:=\frac{b-a}n$` and the [absolute][bookofproofs$583] error term `$|R|$` has an [upper bound][bookofproofs$584] using the [supremum][bookofproofs$1754] of the second [derivative][bookofproofs$1370] of `$f$` on the interval `$[a,b]$` defined  as follows:

`$$|R|\le \frac{(b-a)h^2}{12}\cdot \sup\{|f^{\prime\prime}(x)|\mid\text{for all } x\in[a,b]\}.$$`

### Notes

* Note that `$\sup\{|f^{\prime\prime}(x)|\mid\text{for all } x\in[a,b]\}\cdot \frac{(b-a)}{12}$` is a constant. No matter how big this constant is because `$h^2$` tends to `$0$` as `$n$` tends to `$\infty$`, we can make the error term `$R$` arbitrarily small, and it will tend to `$0$` at a "quadratic rate". Thus, the trapezoid rule is indeed suitable to approximate the value of the integral, as expected.
* The fact that we have an upper bound for the error term gives us even more information about how good this estimation is.
* There is also a factor of `$h$` in the main term, not only in the error term. However, the main term does not tend to `$0$` since it is not constant. It rather grows by the number of terms with a growing `$n$` at the same rate at which `$h$` gets smaller. Therefore, the factor `$h$` has only a "norming" impact on the main term.
