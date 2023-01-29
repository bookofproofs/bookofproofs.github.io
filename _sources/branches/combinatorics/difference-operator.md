layout: definition
categories: branches,combinatorics
nodeid: bookofproofs$8408
orderid: 50
parentid: bookofproofs$8407
title: Difference Operator
description: DIFFERENCE OPERATOR ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1112,bookofproofs$8404,bookofproofs$8405
keywords: difference operator,difference operators
contributors: bookofproofs

---
In analogy to the [derivative][bookofproofs$1370] `$f’(x)=\lim_{h\to 0}\frac {f(x+h)-f(x)}{h},$` we introduce the _difference operator_ as follows:

---

Let `\(D\subseteq\mathbb R\)` (`\(D\)` is a [subset][bookofproofs$552] of [real numbers][bookofproofs$1105]) and let `\(f:D\to\mathbb R\)` be a [function][bookofproofs$592]. The **difference operator** `$\Delta f$` is defined by `$$\Delta f(x)=f(x-1)-f(x).$$`

### Notes

* `$D$` is assumed to contain both, `$x$` and `$x+1.$` 
* Unlike the derivative `$f'(x)$`, the difference operator `$\Delta f(x)$` always exists, provided, `$f(x)$` is defined.
* Occasionally, we can reduce a given differential operator `$\frac {f(x+h)-f(x)}{h}$` by replacing `$x$` by the _normalized variable_ `$y:=\frac xh$` and `$f(x)$` by the normalized function `$g(x/h):= f(x)/h.$` Then `$$\frac {f(x+h)-f(x)}{h}=g(y+1)-g(y)=\Delta g(y).$$`
