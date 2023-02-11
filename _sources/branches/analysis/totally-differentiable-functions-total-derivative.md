layout: definition
categories: branches,analysis
nodeid: bookofproofs$6215
orderid: 400
parentid: bookofproofs$144
title: Totally Differentiable Functions, Total Derivative
description: TOTALLY DIFFERENTIABLE FUNCTIONS, TOTAL DERIVATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6907
keywords: derivative,differentiable,functions,total,totally,totally differentiable,total derivative
contributors: @Brenner,bookofproofs

---


---

Let `\(V\subseteq \mathbb R^n\)` and `\(W\subseteq \mathbb R^m\)` be [finitely dimensional vector spaces][bookofproofs$1206] over the field `\(\mathbb R\)`, let `\(G\subseteq V\)` be an [open set][bookofproofs$852] and let `\(\varphi \colon G\rightarrow W\)` be a [function][bookofproofs$592]. We call `\(\varphi \)` **differentiable** (or **totally differentiable**) at a point `\(x\in G\)`, if there exists a [linear function][bookofproofs$403] `\(A\colon V\rightarrow W\)` with the property

`\[\varphi (x+\xi)=\varphi (x)+A\xi+r(\xi)\,,\]`

where `\(r\)` is a function defined in a [neighborhood][bookofproofs$849] of `\(0\)` with values in `\(W\)`, i.e. `\(r:B\left(0,\delta \right)\rightarrow W\)` and fulfilling the property

`\[\lim_{\xi\to 0}\frac{r(\xi)}{\mid \mid \!\xi\!\mid \mid}=0\]`

for all `\(\xi\in V\)` with `\(x+\xi\in U\left(x,\delta \right)\subseteq G\)`.

The linear function `\(A\)`, if it exists, is called the *(total) derivative* of `\(\varphi \)` at the point `\(x\)` and is also denoted by 
`\[\left(D\varphi \right)_{x}.\]`
