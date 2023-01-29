layout: definition
categories: branches,analysis
nodeid: bookofproofs$6771
orderid: 200
parentid: bookofproofs$347
title: Higher-Order Derivatives
description: HIGHER-ORDER DERIVATIVES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: derivatives,higher,order
contributors: bookofproofs

---


---

Let `$D$` be a [subset][bookofproofs$552] of the [real numbers][bookofproofs$1105] `$\mathbb R$` and let `$f:D\to\mathbb R$` be a  [function][bookofproofs$592] which is [differentiable][bookofproofs$1370] on `$D.$` If its derivative `$f':D\to\mathbb R$` is itself differentiable at a point `$x\in D,$` then its derivative 
`$$\frac{d^2f(x)}{dx}:=f'\;'(x):=(f')'(x)$$` is called the *second-order derivative of `$f$` at `$x.$`*

In general, if `$f:D\;\cap\;]x-\epsilon,x + \epsilon[\to\mathbb R$` is `$(k-1)$` times differentiable in `$D\;\cap\;]x-\epsilon,x + \epsilon[$`, and if its `$(k-1)$`-th derivative is differentiable at `$x$`, then we call `$f^{(k)}$` its *$k$-th derivative* (or the *derivative of order `$k$`* at `$x.$`)[^1] 

There are several equivalent notations of this derivative:

`$$f^{(k)}(x):=\frac{d^kf(x)}{dx^k}:=\left(\frac d{dx}\right)^kf(x):=\frac d{dx}\left(\frac{d^{k-1}f(x)}{dx^{k-1}}\right).$$`

[^1]: The derivative of order `$0$` of `$f$` is the function `$f$` itself.
