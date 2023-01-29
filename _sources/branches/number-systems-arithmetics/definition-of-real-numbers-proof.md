layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1106
orderid: 50
parentid: bookofproofs$1105
title: 
description:  Proof of DEFINITION OF REAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$696
keywords: real number,real numbers,real-valued,proof
contributors: bookofproofs

---


---

Let `\((x_n)_{n\in\mathbb N}\)`, `\((y_n)_{n\in\mathbb N}\)` be [rational Cauchy sequences][bookofproofs$1485]. We will prove that the relation defined by 

`\[(x_n)_{n\in\mathbb N}\sim(y_n)_{n\in\mathbb N}\quad\Longleftrightarrow\quad \lim_{n\to\infty } y_n-x_n =0\in\mathbb Q\]`

is an [equivalence relation][bookofproofs$574]. In other words, the real numbers as equivalence classes `\(x:=(x_n)_{n\in\mathbb N}+I:=\{(y_n)_{n\in\mathbb N},~ (y_n)_{n\in\mathbb N}\sim (x_n)_{n\in\mathbb N}\}\)` are well-defined.

### `\(( i )\)` Reflexivity

Clearly, `\(\lim_{n\to\infty } x_n-x_n =0\)`.

### `\(( ii )\)` Symmetry `\((x_n)_{n\in\mathbb N}\sim (y_n)_{n\in\mathbb N}\Leftrightarrow (y_n)_{n\in\mathbb N}\sim (x_n)_{n\in\mathbb N}\)`

Since `\(\lim_{n\to\infty } y_n-x_n =0\Leftrightarrow \lim_{n\to\infty } x_n-y_n =0\)`.

###  `\(( iii )\)` Transitivity

By hypothesis, the rational Cauchy sequences  `\((i_n)_{n\in\mathbb N}:=(y_n - x_n)_{n\in\mathbb N}\)` and `\((j_n)_{n\in\mathbb N}:=(z_n - y_n)_{n\in\mathbb N}\)`  are [convergent][bookofproofs$1572] to `\(0\)`. Because `\(z_n-x_n=j_n+i_n\)` and because `\(\lim_{n\to\infty} j_n+i_n=0\)`, it follows `\((x_n)_{n\in\mathbb N}\sim (z_n)_{n\in\mathbb N}\)`.
