layout: motivation
categories: branches,combinatorics
nodeid: bookofproofs$8415
orderid: 50
parentid: bookofproofs$1399
title: Formulae of Negative Factorial Powers Explained
description: FORMULAE OF NEGATIVE FACTORIAL POWERS EXPLAINED &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8404
keywords: negative factorial powers explained
contributors: bookofproofs

---


---

Now, we want to motivate, why we have provided the given formulae for negative [factorial powers][bookofproofs$1399].
The reason for setting `$$x^{\underline 0}:=1,\quad x^{\underline{-n}}:=\frac{1}{(x+n)^{\underline{n}}}$$` and `$$x^{\overline 0}:=1,\quad x^{\overline{-n}}:=\frac{1}{(x-n)^{\overline{n}}}$$` is similar to the reason given in elementary algebra that, for given [positive integers][bookofproofs$1075] `$n$` and `$m$` we have the formula `$x^nx^m=x^{n+m},$` and the only way to keep this formula hold also for negative exponents is to set `$x^0=1$` and `$x^{-n}=1/x^n.$`

### Case: Falling Factorial Powers

Note that by definition of [falling factorial powers][bookofproofs$1399] for positive `$n,m\ge 1$` we have `$$\begin{align}x^{\underline{n}}(x-n)^{\underline{m}}&=x(x-1)(x-2)\cdots(x-n+2)(x-n+1)\cdot \nonumber \\ &\quad\cdot (x-n)(x-n-1)(x-n-2)\ldots(x-n-m+2)(x-n-m+1) \nonumber\\
&=x^{\underline{n+m}}.\nonumber\end{align}$$`

If this formula has to hold also for `$n=0$`, then we have to require `$x^{\underline 0}=1,$` because then `$$x^{\underline 0}(x-0)^{\underline m}=x^{\underline {0+m}}=x^{\underline 0}\cdot x^{\underline m}=1\cdot x^{\underline m}.$$`

Therefore, for every [integer][bookofproofs$844] `$n\in Z$` we require `$$x^{\underline {-n}}(x-(-n))^{\underline {n}}=x^{\underline {-n+n}}=x^{\underline {0}}=1,$$` and thus `$$x^{\underline{-n}}:=\frac{1}{(x+n)^{\underline{n}}}.$$`

### Case: Raising Factorial Powers

Analogously, by definition of [raising factorial powers][bookofproofs$1399] for positive `$n,m\ge 1$` we have `$$\begin{align}x^{\overline{n}}(x-n)^{\overline{m}}&=x(x+1)(x+2)\cdots(x+n-2)(x+n-1)\cdot \nonumber \\ &\quad\cdot (x+n)(x+n+1)(x+n+2)\ldots(x+n+m-2)(x+n+m-1) \nonumber\\
&=x^{\overline{n+m}}.\nonumber\end{align}$$`

If this formula has to hold also for `$n=0$`, then we have to require `$x^{\overline 0}=1,$` because then `$$x^{\overline 0}(x+0)^{\overline m}=x^{\overline{0+m}}=x^{\overline 0}\cdot x^{\overline m}=1\cdot x^{\overline m}.$$`

Thus, for every [integer][bookofproofs$844] `$n\in Z$` we require `$$x^{\overline{-n}}(x+(-n))^{\overline {n}}=x^{\overline{-n+n}}=x^{\overline{0}}=1,$$` and thus `$$x^{\overline{-n}}:=\frac{1}{(x-n)^{\overline{n}}}.$$`
