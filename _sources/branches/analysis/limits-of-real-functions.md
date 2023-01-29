layout: definition
categories: branches,analysis
nodeid: bookofproofs$6683
orderid: 700
parentid: bookofproofs$126
title: Limits of Real Functions
description: LIMITS OF REAL FUNCTIONS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581,bookofproofs$6823
keywords: limit of real function,limits of real functions,limits
contributors: bookofproofs

---
In real analysis, it is mostly necessary to deal with the limits of functions instead of the limits sequences. Therefore we want to now generalize the concept of limits from sequences to functions.

---

Let `\(D\)` be a [subset][bookofproofs$552] of [real numbers][bookofproofs$1105] `\(\mathbb R\)`, `\(x\in D\)`, and let `\(f:D\to\mathbb R\)` be a [function][bookofproofs$592]. We define different notations:

> `$(1)$` *Limit of `$f$` at `$x$`*: For every [real sequence][bookofproofs$875] `$(\xi_n)_{n\in\mathbb N}$` with `$\xi_n\in D$` for all `$n\in\mathbb N$`, which is [convergent][bookofproofs$141] to `$x$` we have that `$\lim_{n\to\infty}f(\xi_n)=y$`. Then this can be notated as `$$\lim_{\xi\to x} f(\xi)= y.$$`
Equivalently, for every `$\epsilon > 0$` there is a `$\delta > 0$` such that for every `$\xi$` with `$\xi\in D$`  satisfying `$0 < |\xi-x| < \delta,$` it follows `$|f(\xi)-y| < \epsilon.$`


> `$(2)$` *Limit of `$f$` at `$x$` from above*: For every [real sequence][bookofproofs$875] `$(\xi_n)_{n\in\mathbb N}$` with `$\xi_n\in D$`, `$\xi_n > x$` for all `$n\in\mathbb N$`, which is [convergent][bookofproofs$141] to `$x$`, we have that `$\lim_{n\to\infty}f(\xi_n)=y$`. Then this can be notated as
`$$\lim_{\xi\searrow x} f(\xi)= y.$$`
Equivalently, for every `$\epsilon > 0$` there is a `$\delta > 0$` such that for every `$\xi$` with `$\xi\in D$`  satisfying `$0 < \xi-x < \delta,$` it follows `$|f(\xi)-y| < \epsilon.$`

> `$(3)$` *Limit of `$f$` at `$x$` from below*: For every [real sequence][bookofproofs$875] `$(\xi_n)_{n\in\mathbb N}$` with `$\xi_n\in D$`, `$\xi_n < x$`  for all `$n\in\mathbb N$`, which is [convergent][bookofproofs$141] to `$x$` we have that `$\lim_{n\to\infty}f(\xi_n)=y$`. Then this can be notated as
`$$\lim_{\xi\nearrow x} f(\xi)= y.$$`
Equivalently, for every `$\epsilon > 0$` there is a `$\delta > 0$` such that for every `$\xi$` with `$\xi\in D$`  satisfying `$0 < x-\xi < \delta,$` it follows `$|f(x)-y| < \epsilon.$`

> `$(4)$` *Limit of `$f$` at `$+\infty$`*: For every [real sequence][bookofproofs$875] `$(\xi_n)_{n\in\mathbb N}$` with `$\xi_n\in D$` for all `$n\in\mathbb N$`, which [tends to infinity][bookofproofs$1345], we have that `$\lim_{n\to\infty}f(\xi_n)=y$`. Then this can be notated as
`$$\lim_{\xi\to\infty} f(\xi)= y.$$`
Equivalently, for every `$\epsilon > 0$` there is an `$N\in\mathbb N$` such that for every `$\xi$` with `$\xi\in D$`  satisfying `$\xi > N$` it follows `$|f(\xi)-y| < \epsilon.$`

> `$(5)$` *Limit of `$f$` at `$-\infty$`*: For every [real sequence][bookofproofs$875] `$(\xi_n)_{n\in\mathbb N}$` with `$\xi_n\in D$` for all `$n\in\mathbb N$`, which [tends to minus infinity][bookofproofs$1345], we have that `$\lim_{n\to\infty}f(\xi_n)=y$`. Then this can be notated as
`$$\lim_{\xi\to-\infty} f(\xi)= y.$$`
Equivalently, for every `$\epsilon > 0$` there is an `$N\in\mathbb N$` such that for every `$\xi$` with `$\xi\in D$`  satisfying `$\xi < - N$` it follows `$|f(\xi)-y| < \epsilon.$`

> `$(6)$` *Limit of `$f$` at `$x$` is `$\infty$`*: For every [real sequence][bookofproofs$875] `$(\xi_n)_{n\in\mathbb N}$` with `$\xi_n\in D$` for all `$n\in\mathbb N$`, which is [convergent][bookofproofs$141] to `$x$`, we have that the sequence `$(f(\xi_n))_{n\in\mathbb N}$` [tends to infinity][bookofproofs$1345]. Then this can be notated as
`$$\lim_{\xi\to x} f(\xi)= \infty.$$`
Equivalently, for every `$M\in\mathbb R$` there is an `$\delta > 0$` such that for every `$\xi$` with `$\xi\in D$`  satisfying `$0 < |\xi-x| < \delta$` it follows `$f(x) > M.$`

> `$(7)$` *Limit of `$f$` at `$x$` is `$-\infty$`*: For every [real sequence][bookofproofs$875] `$(\xi_n)_{n\in\mathbb N}$` with `$\xi_n\in D$` for all `$n\in\mathbb N$`, which is [convergent][bookofproofs$141] to `$x$`, we have that the sequence `$(f(\xi_n))_{n\in\mathbb N}$` [tends to minus infinity][bookofproofs$1345]. Then this can be notated as
`$$\lim_{\xi\to x} f(\xi)= -\infty.$$`
Equivalently, for every `$M\in\mathbb R$` there is an `$\delta > 0$` such that for every `$\xi$` with `$\xi\in D$`  satisfying `$0 < |\xi-x| < \delta$` it follows `$f(x) < M.$`

> `$(8)$` *Limit of `$f$`, as `$x$` approaches `$\infty$` is `$\infty$`*: For every [real sequence][bookofproofs$875] `$(\xi_n)_{n\in\mathbb N}$` with `$\xi_n\in D$` for all `$n\in\mathbb N$`, which [tends to infinity][bookofproofs$1345], we have that the sequence `$(f(\xi_n))_{n\in\mathbb N}$` also [tends to infinity][bookofproofs$1345]. Then this can be notated as
`$$\lim_{\xi\to \infty} f(\xi)= \infty.$$`
Equivalently, for every `$M\in\mathbb R$` there is an `$N\in\mathbb R$` such that for every `$\xi$` with `$\xi\in D$` satisfying `$\xi > N$` it follows `$f(x) > M.$`

> `$(9)$` *Limit of `$f$`, as `$x$` approaches `$\infty$` is `$-\infty$`*: For every [real sequence][bookofproofs$875] `$(\xi_n)_{n\in\mathbb N}$` with `$\xi_n\in D$` for all `$n\in\mathbb N$`, which [tends to infinity][bookofproofs$1345], we have that the sequence `$(f(\xi_n))_{n\in\mathbb N}$` [tends to minus infinity][bookofproofs$1345]. Then this can be notated as
`$$\lim_{\xi\to \infty} f(\xi)= -\infty.$$`
Equivalently, for every `$M\in\mathbb R$` there is an `$N\in\mathbb R$` such that for every `$\xi$` with `$\xi\in D$` satisfying `$\xi > N$` it follows `$f(x) < M.$`

> `$(10)$` *Limit of `$f$`, as `$x$` approaches `$-\infty$` is `$\infty$`*: For every [real sequence][bookofproofs$875] `$(\xi_n)_{n\in\mathbb N}$` with `$\xi_n\in D$` for all `$n\in\mathbb N$`, which [tends to minus infinity][bookofproofs$1345], we have that the sequence `$(f(\xi_n))_{n\in\mathbb N}$` [tends to infinity][bookofproofs$1345]. Then this can be notated as
`$$\lim_{\xi\to -\infty} f(\xi)= \infty.$$`
Equivalently, for every `$M\in\mathbb R$` there is an `$N\in\mathbb R$` such that for every `$\xi$` with `$\xi\in D$` satisfying `$\xi < N$` it follows `$f(x) > M.$`

> `$(11)$` *Limit of `$f$`, as `$x$` approaches `$-\infty$` is `$-\infty$`*: For every [real sequence][bookofproofs$875] `$(\xi_n)_{n\in\mathbb N}$` with `$\xi_n\in D$` for all `$n\in\mathbb N$`, which [tends to minus infinity][bookofproofs$1345], we have that the sequence `$(f(\xi_n))_{n\in\mathbb N}$` also [tends to minus infinity][bookofproofs$1345]. Then this can be notated as
`$$\lim_{\xi\to -\infty} f(\xi)= -\infty.$$`
Equivalently, for every `$M\in\mathbb R$` there is an `$N\in\mathbb R$` such that for every `$\xi$` with `$\xi\in D$` satisfying `$\xi < N$` it follows `$f(x) < M.$`
