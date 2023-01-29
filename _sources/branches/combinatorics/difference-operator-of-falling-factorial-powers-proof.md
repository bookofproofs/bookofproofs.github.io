layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8417
orderid: 50
parentid: bookofproofs$8416
title: 
description: PROOF OF DIFFERENCE OPERATOR OF FALLING FACTORIAL POWERS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$8404
keywords: difference operator of falling factorial powers,proof
contributors: bookofproofs

---


---

* Let `$x\in \mathbb C$` is a [complex number][bookofproofs$6788] and let `$n\ge 0$` be [non-negative integer][bookofproofs$1075].
* Case `$n\ge 1$`:
   * Then, by definition of the [difference operator][bookofproofs$8408], we get for the [falling factorial power][bookofproofs$1618] `$$\begin{align}\Delta x^{\underline {n}}&=(x+1)^{\underline {n}}-x^{\underline {n}}\nonumber\\
&=(x+1)[x(x-1)\cdots(x-n+2)]-\nonumber\\
&\quad-[x(x-1)\cdots(x-n+2)(x-n+1)]\nonumber\\
&=[(x+1)-(x-n+1)]\cdot[x(x-1)\cdots(x-n+2)]\nonumber\\
&=nx^{\underline {n-1}}.\nonumber
\end{align}$$`
* Case `$n=0$`, `$x\neq 1$`:
   * By definition of the [difference operator][bookofproofs$8408] and the [falling factorial power][bookofproofs$1618] `$$\Delta x^{\underline {0}}=(x+1)^{\underline {0}}-x^{\underline {0}}=1-1=0=0\cdot x^{\underline {-1}}.$$`
* Case `$-n<0$`, `$x\not\in\{1,2,\ldots,n,n+1\}$`
   * By definition of the [difference operator][bookofproofs$8408] and the [falling factorial power][bookofproofs$1618].
`$$\begin{align}\Delta x^{\underline {-n}}&=\frac{1}{{x+1}^{\underline n}}-\frac{1}{x^\underline n}\nonumber\\
&=\frac{1}{(x+1)[x(x-1)\cdots(x-n-2)]}-\frac{1}{[x(x-1)\cdots(x-n-2)](x-n-1)}\nonumber\\
&=\frac{x-n-1}{(x+1)[x(x-1)\cdots(x-n-2)](x-n-1)}-\frac{x+1}{(x+1)[x(x-1)\cdots(x-n-2)](x-n-1)}\nonumber\\
&=-n\cdot \frac{1}{x^{\underline{n+1}}}\nonumber\\
&=-n\cdot x^{\underline{-n-1}}\nonumber
\end{align}$$`
* It follows that `$\Delta x^{\underline{n}}=nx^{\underline{n-1}}$` for all [integers][bookofproofs$844] `$n\in\mathbb Z.$`
