layout: definition
categories: branches,combinatorics
nodeid: bookofproofs$1399
orderid: 40000
parentid: bookofproofs$8407
title: Falling And Rising Factorial Powers
description: FALLING AND RISING FACTORIAL POWERS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1112
keywords: falling factorial power,rising factorial power,falling factorial powers,rising factorial powers,rising factorial
contributors: bookofproofs

---
A comparison of the [derivative of powers][bookofproofs$6755] `$\frac {d}{dx}x^n=nx^{n-1}$` known from calculus with the result of the [difference operator of powers][bookofproofs$8413] `$\Delta x^n=\sum_{k=1}^n \binom {n}{k} x^{n-k}$` shows that the latter does not have such a simple compact expression. It turns out that a function leading to a similar compact expression when using the difference operator is the so-called _falling factorial power_ `$x^{\underline n},$` and we will see soon that `$\Delta x^{\underline n}=nx^{\underline {n-1}}.$` We first define the falling factorial power and its counterpart - the _rasing factorial power_ and study some of their basic properties.

---

For a [real][bookofproofs$1105] or [complex number][bookofproofs$216] `\(x\)` and a [positive integer][bookofproofs$1075] `$n\ge 1$` we define the following operators:

> **falling factorial power** of `\(x\)` (also read "`\(x\)` to the `\(n\)` falling"):   
`\[x^{\underline{n}}:= x(x-1)(x-2) \cdots (x-n+1).\]`

> **rising factorial power** of `\(x\)` (also read "`\(x\)` to the `\(n\)` rising"):   
`\[x^{\overline{n}}:= x(x+1)(x+2) \cdots (x+n-1).\]`

Moreover, for `$x\not\in\{-1,-2,\ldots,-n\}$` we define `$$x^{\underline 0}:=1,\quad x^{\underline{-n}}:=\frac{1}{(x+n)^{\underline{n}}}=\frac{1}{(x+n)(x+n-1)\cdots(x+2)(x+1)},$$` and for `$x\not\in\{1,2,\ldots,n\}$` `$$x^{\overline 0}:=1,\quad x^{\overline{-n}}:=\frac{1}{(x-n)^{\overline{n}}}=\frac{1}{(x-n)(x-n+1)\cdots(x-2)(x-1)}.$$`
