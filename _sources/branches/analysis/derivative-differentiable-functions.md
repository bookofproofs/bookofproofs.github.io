layout: definition
categories: branches,analysis
nodeid: bookofproofs$1370
orderid: 100
parentid: bookofproofs$347
title: Derivative, Differentiable Functions
description: DERIVATIVE, DIFFERENTIABLE FUNCTIONS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: derivative,derivatives,differentiable,differentiable functions,differentiable function
contributors: bookofproofs

---


---

Let `\(D\subseteq\mathbb R\)` (`\(D\)` is a [subset][bookofproofs$552] of [real numbers][bookofproofs$1105]) and let `\(f:D\to\mathbb R\)` be a [function][bookofproofs$592]. Using the concept of the [difference quotient][bookofproofs$1369], 

`\[\Delta f(y,x)=\frac {f(y)-f(x)}{y-x},\quad y\neq x,\]`

for a fixed `\(x\in D\)` and all `\(\xi\in D\)` with `\(\xi\neq x\)`, we define a function `\(g:D\to\mathbb R\)` by 

`\[g(\xi):=\Delta f(\xi,x)=\frac {f(\xi)-f(x)}{\xi-x},\xi\neq x.\]`

If `\(g\)` is [continuous][bookofproofs$219] at `\(x\)`, its limit at `\(x\)` exists[^1] and is unique[^2]. This [limit][bookofproofs$6683] defines a new function 

`\[f'(x):=\lim_{\substack{\xi\to x\\\xi\in D\setminus\{x\}}} g(\xi)=\lim_{\substack{\xi\to x\\\xi\in D\setminus\{x\}}}\frac {f(\xi)-f(x)}{\xi-x}.\]`

called the *derivative of `\(f\)` at `\(x\)`*.

### Other Notions of Derivatives

1. By a change of variables, the derivative `\(f'(x)\)` can also be defined as `\[f'(x):=\lim_{h\to 0}\frac {f(x+h)-f(x)}{h}.\]` In this definition, only those sequences `\((h_n)_{n\in\mathbb N}\)` with  `\(\lim h_n=0\)` are allowed, for which `\(h_n\neq 0\)` and `\(x+h_n\in D\)`.
1. Instead of writing `\(f'(x)\)`, the derivative can also be written[^3] as `\(\frac {d f(x)}{dx}\)`.
1. `\(f\)` has a derivative at `\(x\)` `$\Longleftrightarrow f$` is *differentiable at `\(x\)`*. 
1. `\(f\)` has a derivative at every `\(x\in D\)` `\(\Longleftrightarrow f\)` is *differentiable on `$D$`*. 

[^1]: Please note that the continuity of `\(g\)` at `\(x\)` requires the existence of at least one sequence `\((x_n)_{n\in\mathbb N}\)`, `\(x_n\in D\)` with `\(\lim_{n\to\infty} x_n=x\)`.

[^2]: The uniqueness of the limit means that for every sequence `\((\xi_n)_{n\to\infty}\)`, `\(\xi_n\in D\setminus\{x\}\)` with `\(\lim_{n\to\infty} \xi_n=x\)` we have `\(g(\xi_n)=f'(x)\)`.

[^3]: The notation `\(\frac {d f(x)}{dx}\)` can, in comparison with the notation `\(f'(x)\)`, sometimes become cumbersome. For instance, if `\(x=0\)`, we can write `\(f'(0)\)`, but we cannot write `\(\frac {d f(0)}{d0}\)`. In this case it is necessary to write `\(\frac {d f}{dx}(0)\)` or `\({\frac {d f(x)}{dx}}|^{d0}_{x=0}\)`
