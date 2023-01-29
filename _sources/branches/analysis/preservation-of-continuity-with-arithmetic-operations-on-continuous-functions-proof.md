layout: proof
categories: branches,analysis
nodeid: bookofproofs$1262
orderid: 50
parentid: bookofproofs$1261
title: 
description:  Proof of PRESERVATION OF CONTINUITY WITH ARITHMETIC OPERATIONS ON CONTINUOUS FUNCTIONS &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$581
keywords: preservation of continuity for arithmetic operations,arithmetic operations for continuous functions,proof
contributors: bookofproofs

---


---

By hypothesis, `\(f,g:D\to\mathbb R\)` are functions, which are [continuous at the number][bookofproofs$219]  `\(a\in\mathbb R\)`, which means by definition that for any sequence `\((x_n)_{n\in\mathbb N}\)` of numbers `\(x_n\in D\)` convergent to `\(a\)`, i.e. with `\[\lim_{n\to \infty} x_n=a,\]` we have `\[\lim_{n\to\infty }f(x_n)=f(a)\text{ and }\lim_{n\to\infty }g(x_n)=g(a).\quad\quad( * )\]`

### `\((1)\)` We show that `\(f + g:D\to\mathbb R\)` is continuous at `\(a\)`. 

From the proposition about [sums of convergent real sequences][bookofproofs$1131], it follows that 
`\[\lim_{n\to\infty}(f + g)(x_n)=\lim_{n\to\infty}f(x_n) + \lim_{n\to\infty}g(x_n)\overset{( * )}{=}f(a) + f(b),
\]`
which means that `\(f + g:D\to\mathbb R\)` is continuous at `\(a\)`. 

### `\((2)\)` We show that `\(\lambda f:D \to \mathbb R\)` is continuous at `\(a\)` 

From the proposition about the [product of a real number with a convergent real sequence][bookofproofs$1140], it follows that 
`\[\lim_{n\to\infty}(\lambda f)(x_n)=\lambda \lim_{n\to\infty}f(x_n)\overset{( * )}{=}\lambda f(a),
\]`
which means that `\(\lambda f:D \to \mathbb R\)` is continuous at `\(a\)`. 


### `\((3)\)` We show that `\(f\cdot g:D \to \mathbb R\)` is continuous at `\(a\)` 

From the proposition about the [product convergent real sequences][bookofproofs$1135], it follows that 
`\[\lim_{n\to\infty}(f \cdot g)(x_n)=\lim_{n\to\infty}f(x_n) \cdot \lim_{n\to\infty}g(x_n)\overset{( * )}{=}f(a) \cdot f(b),
\]`
which means that `\(f\cdot g:D \to \mathbb R\)` is continuous at `\(a\)`. 

### `\((4)\)` We show that for `\(g(a)\neq 0\)` the function  `\(\frac fg:D' \to \mathbb R\)`  is continuous at `\(a\)`, where   `\(D':=\{x\in D:g(x)\neq 0\}\)`.

From the proposition about the [quotient of convergent real sequences][bookofproofs$1142], it follows that there is a some index `\(N\in\mathbb N\)` such that `\(g(x_n)\neq 0\)` for all `\(n \ge N\)` we have
`\[\lim_{n\to\infty,n \ge N}\left(\frac fg\right)(x_n)=\frac{\lim_{n\to\infty,n \ge N}f(x_n)}{\lim_{n\to\infty,n \ge N}b(x_n)} \overset{( * )}{=}\frac{f(a)}{f(b)},
\]`
which means that `\(\frac fg:D' \to \mathbb R\)` is continuous at `\(a\)`, with `\(D':=\{x\in D:g(x)\neq 0\}\)`.
