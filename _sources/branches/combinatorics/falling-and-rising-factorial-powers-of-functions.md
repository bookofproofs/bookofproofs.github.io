layout: definition
categories: branches,combinatorics
nodeid: bookofproofs$8423
orderid: 700
parentid: bookofproofs$8407
title: Falling and Rising Factorial Powers of Functions
description: FALLING AND RISING FACTORIAL POWERS OF FUNCTIONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1112,bookofproofs$8404,bookofproofs$8405
keywords: falling and rising factorial powers of functions,rising factorial
contributors: bookofproofs

---
It is useful to define a generalization of the [falling and rising factorials][bookofproofs$1399] as follows:

---

Obviously, the [falling and rising factorials][bookofproofs$1399] `$x^\underline{n}$` and `$x^\overline{n}$` equal `$g^\underline{n}(x)$` and `$g^\overline{n}(x)$` for the complex identity function `$g(x):=x$` for all `$x\in\mathbb C.$` If `$f:D\to\mathbb C$` is a [function][bookofproofs$592] with a suitable domain[^1] `$D\subseteq\mathbb C$`, then the *falling `$f^\underline{n}$`* (and respectively) the *rising factorials `$f^\overline{n}$`* are defined as the [compositions][bookofproofs$1314] of `$$(g\circ f)(x)=f^\underline{n}(x),\quad f^\overline{n}(x).$$`

### Examples (for a positive `$n$`)

* `$f(x)=a+bx,$` `$$\begin{align}f^{\underline{n}}(x)&=(a+bx)(a+b(x-1))\cdots(a+b(x-n+1))\nonumber\\f^{\underline{-n}}(x)&=\frac 1{(a+b(x+1))(a+b(x+2))\cdots(a+b(x+n))}\nonumber\end{align}$$`
* `$f(x)=a^x,$` `$$\begin{align}f^{\underline{n}}(x)&=a^x\cdot a^{x-1}\cdots a^{x-n+1}=a^{x^{\underline n}}\nonumber\\f^{\underline{-n}}(x)&=\frac 1{a^{x+1}a^{x+2}\cdots a^{x+n}}=\frac 1{a^{(x+1)^{\underline n}}}\nonumber\end{align}$$`
* `$f(x)=\sin(x),$` `$$\begin{align}f^{\overline{n}}(x)&=\sin(x)\sin(x+1)\cdots\sin(x+n-1))\nonumber\\f^{\overline{-n}}(x)&=\frac 1{\sin(x-n)\sin(x-2)\cdots\sin(x-n)}\nonumber\end{align}$$`

[^1]: For a given `$x\in D,$` also `$x\pm i+1\in D$` for all integers `$i=0,\ldots,n$`
