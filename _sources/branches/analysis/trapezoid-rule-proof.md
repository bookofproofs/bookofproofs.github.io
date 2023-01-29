layout: proof
categories: branches,analysis
nodeid: bookofproofs$8342
orderid: 50
parentid: bookofproofs$8341
title: 
description: TRAPEZOID RULE Proof ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: trapezoid rule,proof
contributors: bookofproofs

---


---

* By hypothesis, the function `$f$` is a [twice continuously differentiable function][bookofproofs$6812].
* First of all we will show that there is a mean value `$\xi\in[0,1]$` such that `$$\int_0^1f(x)dx=\frac{f(0)+f(1)}{2}-\frac{1}{12}f^{\prime\prime}(\xi).\label{eq:E20226}\tag{1}$$`
   * For let `$\phi(x):=\frac{1}{2}x(1-x).$`
   * Since we have the [derivatives][bookofproofs$1370] `$\phi^{\prime}(x):=\frac{1}{2}-x$` and `$\phi^{\prime\prime}(x):=-1,$` we have with [partial integration][bookofproofs$8337] `$$\int_0^1f(x)dx=-\int_0^1f(x)\phi^{\prime\prime}(x)dx=\underbrace{-f(x)\phi^{\prime}(x)\;\Rule{2px}{4ex}{2ex}^1_0}_{=:A}+\underbrace{\int_{0}^{1}\phi^{\prime}(x)f’(x)dx}_{=:B}.$$`
   * The term `$A$` evaluates to `$$A=-f(1)(\frac 12-1)+f(0)(\frac 12-0)=\frac 12f(1)+\frac 12f(0)=\frac 12(f(1)+f(0)).\label{eq:E20226a}\tag{2}$$`
   * The term `$B$` evaluates with yet another partial integration to `$$B=\underbrace{f'(x)\phi(x)\;\Rule{2px}{4ex}{2ex}^1_0}_{=0}-\int_0^1\phi(x)f^{\prime\prime}(x)dx=-\int_0^1\phi(x)f^{\prime\prime}(x)dx.$$`
   * Since `$\phi(x)\ge 0$` for all `$x\in[0,1],$` we can apply the [mean value theorem for Riemann integrals][bookofproofs$1772] and conclude that there exists a mean value `$\xi\in[0,1]$` such that `$$B=-f^{\prime\prime}(\xi)\cdot\int_0^1\phi(x)dx.$$`
   * Thus, there exists a mean value `$\xi\in[0,1]$` such that `$$B=-f^{\prime\prime}(\xi)\cdot\int_0^1\frac{1}{2}(x(1-x))dx=-f^{\prime\prime}(\xi)\frac 12\left(\int_0^1 xdx-\int_0^1 x^2dx\right)$$` `$$=-f^{\prime\prime}(\xi)\frac 12\left(\frac 12-\frac 13\right)=-f^{\prime\prime}(\xi)\frac 1{12}.\label{eq:E20226b}\tag{3}$$`
   * `$(\ref{eq:E20226})$` follows now immediately from `$(\ref{eq:E20226a})$` and `$(\ref{eq:E20226b}).$`
* Now, let `$n\ge 1$` be a [natural number][bookofproofs$718] and let `$h:=\frac{b-a}n.$`
* We define the values `$x_\nu:=a+h\nu$` for `$\nu=0,1,\ldots,n.$`
* By [integration by substitution][bookofproofs$6813] in `$(\ref{eq:E20226}),$` we get the result that there is a mean value `$\xi_\nu\in[x_{\nu-1},x_{\nu}]$` such that we can find the [Riemann integral][bookofproofs$1763] for `$\nu=1,\ldots,n$` `$$\int_{a+(\nu-1)h}^{a+\nu h} f(\eta)d\eta=h\cdot \frac{f(x_{\nu-1})+f(x_\nu)}{2}-\frac{h^3}{12}f^{\prime\prime}(\xi_\nu).\label{eq:E20226c}\tag{4}$$`
* Summing `$(\ref{eq:E20226c})$` over all values of `$\nu=1,\ldots,n$` gives us `$$\int_{a}^{b} f(x)dx=\left(\frac{f(a)}{2}+\sum_{\nu=1}^{n-1}f(x_\nu)+\frac{f(b)}{2}\right)h+R \label{eq:E20226d}\tag{5}$$` with an [absolute][bookofproofs$583] error term `$$|R|=\frac{h^3}{12}\sum_{\nu=1}^n f^{\prime\prime}(\xi_\nu).$$`
* Replacing the summands `$f^{\prime\prime}(\xi_\nu)$` by the [supremum][bookofproofs$1754] `$$K:=\sup\{|f^{\prime\prime}(x)|\mid\text{for all } x\in[a,b]\}$$` we get the approximation of the error term:
`$$|R|\le \frac{h^3}{12}\sum_{\nu=1}^n K=\frac{h^3}{12}nK=\frac{(b-a)^3}{n^3}\frac{1}{12}nK=\frac{(b-a)^3}{n^2}\frac{1}{12}K=\frac{(b-a)h^2}{12}K.$$`
