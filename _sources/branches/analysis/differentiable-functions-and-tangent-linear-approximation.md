layout: proposition
categories: branches,analysis
nodeid: bookofproofs$6763
orderid: 600
parentid: bookofproofs$347
title: Differentiable Functions and Tangent-Linear Approximation
description: DIFFERENTIABLE FUNCTIONS AND TANGENT-LINEAR APPROXIMATION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: approximation,differentiable,functions,linear,tangent
contributors: bookofproofs

---


---

Let `\(D\subseteq\mathbb R\)` (`\(D\)` is a [subset][bookofproofs$552] of [real numbers][bookofproofs$1105]) and let `$a\in D$` be a point such that there is at least one [real sequence][bookofproofs$875] `$(x_n)_{n\in\mathbb N}$` [convergent][bookofproofs$141] to `$a$`, i.e. `$\lim_{n\to\infty}x_n=a.$` 

A [function][bookofproofs$592] `$f:D\to\mathbb R$` is [differentiable][bookofproofs$1370] at `$a$` if and only if there is a constant `$c\in\mathbb R$`, such that `$$f(x)=f(a)+c(x-a)+\phi(x),\quad x\in D,$$` where `$\phi$` is a function for which `$$\lim_{\substack{x\to a\\x\neq a}}\frac{\phi(x)}{x-a}=0.\quad\quad ( * )$$`



### Note

In other words, the `$f$` is differentiable at `$a$` if and only if it is possible to draw in the [graph][bookofproofs$6679] of `$f$` a [linear function][bookofproofs$1377] with the equation 
`$$L(x)=f(a)+c(x-a).$$`

The graph of `$L$` is the **tangent** to the graph of `$f$` at the point `$a$`. 

Loosely speaking, by drawing the graph of `$L$` (which is straight line) instead of drawing the graph of `$f$` (which might be curved), in any neighborhood of `$a$` we are likely to make an error, which can be expressed by the function `$\phi$`. The condition `$( * )$` means that this error function is much smaller (tends faster to zero) as the difference `$x-a$` does, as `$x$` tends to the point `$a.$`
