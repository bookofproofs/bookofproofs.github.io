layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8422
orderid: 50
parentid: bookofproofs$8421
title: 
description: PROOF OF FACTORIAL POLYNOMIALS HAVE A UNIQUE REPRESENTATION ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$8404
keywords: factorial polynomials have a unique representation,proof
contributors: bookofproofs

---


---

* Assume, a given [factorial polynomial][bookofproofs$8418] `$\phi(x)$` of degree `$n$` has the two representations `$$\begin{align}\phi(x)&=b_{n+k}x^{\underline{n+k}}+b_{n+k-1}x^{\underline{n+k-1}}+\ldots+b_{n+1}x^{\underline{n+1}}+\nonumber \\
&\quad+b_nx^{\underline{n}}+b_{n-1}x^{\underline{n-1}}+\ldots+b_1x^{\underline{1}}+b_0\tag{1}\\
\phi(x)&=a_nx^{\underline{n}}+a_{n-1}x^{\underline{n-1}}+\ldots+a_1x^{\underline{1}}+a_0,\quad a_n\neq 0\tag{2}.\end{align}$$`
* This means that both equations `$(1)$` and `$(2)$` hold for all [complex numbers][bookofproofs$6788] `$x\in\mathbb C.$` 
* Subtracting `$(2)$` from `$(1)$` gives us `$$\begin{align}0&=b_{n+k}x^{\underline{n+k}}+b_{n+k-1}x^{\underline{n+k-1}}+\ldots+b_{n+1}x^{\underline{n+1}}+\nonumber \\
&\quad+(b_n-a_n)x^{\underline{n}}+(b_{n-1}-a_{n-1})x^{\underline{n-1}}+\ldots+(b_1-a_1)x^{\underline{1}}+(b_0-a_0)\tag{3}\end{align}$$`
for all `$x\in\mathbb C.$`
* Now, note that if for all `$x\in\mathbb C$` `$$\begin{align}0&=\alpha_mx^{\underline{m}}+\alpha_{m-1}x^{\underline{m-1}}+\ldots+\alpha_1x^{\underline{1}}+\alpha_0\tag{4}\end{align}$$` then `$$\begin{align}0&=\alpha_m=\alpha_{m-1}=\cdots=a_1=\alpha_0.\tag{5}\end{align}$$`
   * For if we let `$x=0,$` then `$\alpha_0=0.$` 
   * The [difference operator of falling factorial powers][bookofproofs$8416] of `$(4)$` gives us `$$\begin{align}0&=m\alpha_mx^{\underline{m-1}}+(m-1)\alpha_{m-1}x^{\underline{m-1}}+\ldots+2\alpha_2x^{\underline{2}}+\alpha_1\tag{6}\end{align}$$`
   * For `$x=0$` it follows `$\alpha_1=0.$`
   * Repeating this procedure, gives us `$(5)$`.
* From `$(3)$` and `$(5)$` it follows `$b_{n+k}=b_{n+k-1}=\cdots=b_{n+1}=0$` and `$b_r=a_r$` for `$r=0,1,\ldots,n.$`
