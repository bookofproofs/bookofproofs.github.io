layout: proof
categories: branches,analysis
nodeid: bookofproofs$934
orderid: 50
parentid: bookofproofs$1770
title: 
description: Proof of ADDITION AND SCALAR MULTIPLICATION OF RIEMANN UPPER AND LOWER INTEGRALS ★ master graduate maths ✔ visit BookOfProofs now!
references: bookofproofs$581
keywords: addition,riemann lower integral,riemann upper integral,scalar multiplication,proof
contributors: bookofproofs

---


---

* By hypothesis, `$[a,b]$` is a [closed interval][bookofproofs$1153] and `\(f,g:[a,b]\mapsto\mathbb R\)` are [bounded][bookofproofs$302] on `\([a,b]\)`. 
* Let `$\epsilon > 0$` be an arbitrarily small [real number][bookofproofs$1105], and let `$T[a,b]$` be the [set of all step functions][bookofproofs$6796] on `$[a,b].$` 
* Ad a)
   * By definition of the [Riemann upper integrals][bookofproofs$1761] there are [step functions][bookofproofs$1751] `$\phi,\psi\in T[a,b],$` such that `$\phi(x)\ge f(x), \psi(x)\ge g(x)$` for all `$x\in[a,b]$` and `$$\int_a^{b}\phi(x)dx\le \int_a^{b~*}f(x)dx+\frac{\epsilon}{2},\quad\quad\int_a^{b}\psi(x)dx\le \int_a^{b~*}g(x)dx+\frac{\epsilon}{2}.$$`
   * Thus,
`$$\int_a^{b}(\phi+\psi)(x)dx\le \int_a^{b~*}f(x)dx+\int_a^{b~*}g(x)dx+\epsilon.$$`
   * But, by construction, `$(\phi+\psi)(x)\ge (f+g)(x)$` for all `$x\in[a,b],$` it follows 
`$$\int_a^{b~*}(f+g)(x)dx\le \int_a^{b}(\phi+\psi)(x)dx\le \int_a^{b~*}f(x)dx+\int_a^{b~*}g(x)dx+\epsilon.$$`
   * Since `$\epsilon$` was arbitrary, it follows
`$$\int_a^{b~*}(f+g)(x)dx\le \int_a^{b~*}f(x)dx+\int_a^{b~*}g(x)dx.$$`
* Ad b)
   * By definition of the [Riemann upper and lower integrals][bookofproofs$1761], we have `$$\int_{a~*}^{b}f(x)dx=-\int_{a}^{b~*}(-f)(x)dx\quad\quad\int_{a~*}^{b}g(x)dx=-\int_{a}^{b~*}(-g)(x)dx.\label{E20175}\tag{*}$$`
   * Therefore, by a)
`$$\int_{a~*}^{b}(f+g)(x)dx\ge \int_{a~*}^{b}f(x)dx+\int_{a~*}^{b}g(x)dx.$$`
* Ad c)
   * Let `$\lambda \ge 0$`. 
   * In the casse `$\lambda = 0,$` the equation is trivial. 
   * So let `$\lambda > 0.$` We have to show that
`$$\lambda\int_a^{b~*}f(x)dx-\epsilon\le \int_a^{b~*}(\lambda f)(x)dx\le\lambda\int_a^{b~*}f(x)dx+\epsilon$$`
for all `$\epsilon > 0.$` 
   * By definition of the [Riemann upper and lower integrals][bookofproofs$1761], there is a step function `$\phi\in T[a,b]$` with `$\phi(x)\ge f(x)$` for all `$x\in[a,b]$` and `$$\int_{a}^{b}(\lambda \phi)(x)dx\le \lambda\int_{a}^{b~*}f(x)dx+\epsilon.$$`
   * Since `$\lambda\phi(x)\ge \lambda f(x)$` for all `$x\in[a,b],$` it follows
`$$\int_{a}^{b~*}(\lambda f)(x)dx\le \int_{a}^{b}(\lambda \phi)(x)dx\le \lambda\int_{a}^{b~*}f(x)dx+\epsilon.$$`
   * Analogously, we can show
`$$\int_{a}^{b~*}(\lambda f)(x)dx\ge \int_{a}^{b}(\lambda \phi)(x)dx\ge \lambda\int_{a}^{b~*}f(x)dx-\epsilon.$$`
   * Altogether, it follows
`$$\int_{a}^{b~*}(\lambda f)(x)dx=\lambda\int_{a}^{b~*}f(x)dx$$`
for all `$\lambda\ge 0.$`
* Ad d)
   * Analogously, by `$(\ref{E20175})$` and c) it follows
`$$\int_{a~*}^{b}(\lambda f)(x)dx=\lambda\int_{a~*}^{b}f(x)dx$$`
for all `$\lambda < 0.$`
* Ad e)
   * From `$(\ref{E20175})$` it follows
`$$\int_{a~*}^{b}(\lambda\cdot f)(x)dx=\lambda\cdot\int_{a}^{b~*}f(x)dx$$`
for all `$\lambda < 0.$`
