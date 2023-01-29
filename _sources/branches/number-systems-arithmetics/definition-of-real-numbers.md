layout: proposition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1105
orderid: 100
parentid: bookofproofs$167
title: Definition of Real Numbers
description: DEFINITION OF REAL NUMBERS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$696
keywords: real number,real numbers,real-valued
contributors: bookofproofs

---


---

Let `\((x_n)_{n\in\mathbb N}\)`, `\((y_n)_{n\in\mathbb N}\)` be [rational Cauchy sequences][bookofproofs$1485]. We call them equivalent, if their difference is [convergent][bookofproofs$1572] to `\(0\)`, formally

`\[(x_n)_{n\in\mathbb N}\sim(y_n)_{n\in\mathbb N}\quad\Longleftrightarrow\quad \lim_{n\to\infty } (y_n-x_n) =0\]`

The relation "`\(\sim\)`" defined above is an [equivalence relation][bookofproofs$574], i.e. for a given rational Cauchy sequence `\((x_n)_{n\in\mathbb N}\)` we can consider a whole set of rational Cauchy sequences `\((y_n)_{n\in\mathbb N}\)` equivalent to `\((x_n)_{n\in\mathbb N}\)`:

`\[x:=\{(y_n)_{n\in\mathbb N}\text{ is a rational Cauchy sequence},~ (y_n)_{n\in\mathbb N}\sim (x_n)_{n\in\mathbb N}\}\quad\quad ( * )\]`

The set[^1] `\(x\)` is called a **real number**, and the rational Cauchy sequence `\((x_n)_{n\in\mathbb N}\)` is called a *representation[^2] of the real number*. The set of all real numbers is denoted by `\(\mathbb R\)`.

For practical purposes, `\( ( * ) \)` it equivalent with the notation

`\[x:=(x_n)_{n\in\mathbb N} + I, \]`
where `\(I\)` is the set of all rational sequences convergent to `\(0\)`.


[^1]: Please note that real numbers are in fact sets.

[^2]: This has very important practical consequences, in particular it means that the same real number can be represented in many ways, especially in any numeral system (e.g. decimal or binary).
