layout: definition
categories: branches,analysis
nodeid: bookofproofs$6762
orderid: 50
parentid: bookofproofs$1370
title: One-sided Derivative, Right-Differentiability and Left-Differentiability
description: ONE-SIDED DERIVATIVE, RIGHT-DIFFERENTIABILITY AND LEFT-DIFFERENTIABILITY &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: derivative,differentiability,left,one,right,sided,one sided differentiability,one-sided derivative
contributors: bookofproofs

---


---

Let `\(D\subseteq\mathbb R\)` (`\(D\)` is a [subset][bookofproofs$552] of [real numbers][bookofproofs$1105]) and let `\(f:D\to\mathbb R\)` be a [function][bookofproofs$592]. The function `$f$` is called  *right-differentiable* at a point `$x\in D,$` if the [limit][bookofproofs$6683].
`\[f'_+(x):=\lim_{\substack{\xi\searrow x\\\xi\in D\setminus\{x\}}}\frac {f(\xi)-f(x)}{\xi-x}\]`
at `$x$` from above exists. In this case, `$f'_+(x)$` is called the *right-derivative* of `$f$` at `$x$`.

The function `$f$` is called *left-differentiable* at a point `$x\in D,$` if the [limit][bookofproofs$6683].
`\[f'_-(x):=\lim_{\substack{\xi\nearrow x\\\xi\in D\setminus\{x\}}}\frac {f(\xi)-f(x)}{\xi-x}\]`
at `$x$` from below exists. In this case, `$f'_-(x)$` is called the *left-derivative* of `$f$` at `$x$`.
