layout: proof
categories: branches,analysis
nodeid: bookofproofs$1376
orderid: 50
parentid: bookofproofs$1375
title: 
description: Proof of BASIC ARITHMETIC OPERATIONS INVOLVING DERIVATIVES, PRODUCT RULE, QUOTIENT RULE ★ master maths ✔ visit BookOfProofs!
references: bookofproofs$581
keywords: basic calculations with derivatives,proof
contributors: bookofproofs

---


---

Let `\(D\subseteq\mathbb R\)` (`\(D\)` is a [subset][bookofproofs$552] of [real numbers][bookofproofs$1105]). Let `\(x\in D,\lambda\in\mathbb R\)`. By hypothesis, `\(f,g:D\to\mathbb R\)` are [differentiable functions][bookofproofs$1370] at `\(x\)`. 

### `\((1)\)` Proof of `\((f+g)'(x)=f'(x)+g'(x)\)`

This rule follows immediately the [definition of derivatives][bookofproofs$1370] and the [calculation rule for the sum of convergent real sequences][bookofproofs$1133].
### `\((2)\)` Proof of `\((f-g)'(x)=f'(x)-g'(x)\)`

This rule follows immediately the [definition of derivatives][bookofproofs$1370] and the [calculation rule for the difference of convergent real sequences][bookofproofs$1131].
### `\((3)\)` Proof of `\((\lambda f)'(x)=\lambda f'(x)\)`

This rule follows immediately the [definition of derivatives][bookofproofs$1370] and the [calculation rule for the product of a real number with a convergent real sequence][bookofproofs$1140].
### `\((4)\)` Proof of the "Product Rule" `\((fg)'(x)=f'(x)g(x) + f(x)g'(x)\)`
 
Applying the [definition of derivatives][bookofproofs$1370] we get

`\[\begin{array}{rcl}
(fg)'(x)&=&\lim_{h\to 0}\frac{f(x+h)g(x+h)-f(x)g(x)}{h}\\
&=&\lim_{h\to 0}\frac{f(x+h)g(x+h)-f(x+h)g(x)+f(x+h)g(x)-f(x)g(x)}{h}\\
&=&\lim_{h\to 0}\frac{f(x+h)(g(x+h)-g(x))+(f(x+h)-f(x))g(x)}{h}\\
&=&\lim_{h\to 0}f(x+h)\frac{g(x+h)-g(x)}h+\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}g(x)\quad\quad( * )\\
&=&f'(x)g(x) + f(x)g'(x).
\end{array}\]`

In the step `\( ( * ) \)` we have used that `\(f\)` is [continuous, because it is differentiable][bookofproofs$1374] at `\(x\)`.

### `\((5)\)` Proof of the "Quotient Rule" `\(\left(\frac fg\right)'(x)=\frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}\)`

By hypothesis, we have `\(g(\xi)\neq 0\)` for all `\(\xi\in D\)`. We first consider the special case `\(f=1\)`.

`\[\begin{array}{rcl}
\left(\frac 1g\right)'(x)&=&\lim_{h\to 0}\frac 1h\left(\frac 1{g(x+h)}- \frac 1{g(x)}\right)\\
&=&\lim_{h\to 0}\frac {1}{g(x+h)g(x)}\left(\frac {g(x)-g(x+h)}h\right)\\
&=&\frac {-g'(x)}{g(x)^2}.
\end{array}\]`
Now, we can derive the general case by applying the Product Rule `\((4)\)` above:

`\[\begin{array}{rcl}
\left(\frac fg\right)'(x)&=&\left(f\cdot \frac 1g\right)'(x)\\
&=&f'(x)\frac 1{g(x)} + f(x)\frac{-g'(x)}{g(x)^2}\\
&=&\frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}.
\end{array}\]`
