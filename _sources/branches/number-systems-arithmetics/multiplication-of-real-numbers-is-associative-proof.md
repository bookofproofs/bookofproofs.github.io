layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1534
orderid: 100
parentid: bookofproofs$37
title: 
description:  Proof of MULTIPLICATION OF REAL NUMBERS IS ASSOCIATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: associative,multiplication,numbers,real,proof
contributors: bookofproofs

---


---

Let `\(x\)` and `\(y\)` be [real numbers, which by definition means ][bookofproofs$1105] that they are the equivalence classes `\[\begin{array}{rcl}x&:=&(x_n)_{n\in\mathbb N} + I,\\
y&:=&(y_n)_{n\in\mathbb N} + I.\\z&:=&(z_n)_{n\in\mathbb N} + I.\end{array}\]`
In the above definition, `\((x_n)_{n\in\mathbb N}\)`, `\((y_n)_{n\in\mathbb N}\)`, and `\((z_n)_{n\in\mathbb N}\)` denote elements of the set `\(M\)` of all rational Cauchy sequences, which represent the real numbers `\(x\)` and `\(y\)`, while `\(I\)` denotes the set of all rational sequences, which converge to `\(0\)`.

The associativity of the [multiplication of real numbers][bookofproofs$1532] `\((x\cdot y)\cdot z=x\cdot (y\cdot z)\)` for all `\(x,y,z\in\mathbb R\)` follows from the [associativity of multiplying rational Cauchy sequences][bookofproofs$1500]. For all rational Cauchy sequences `\((x_n)_{n\in\mathbb N}, (y_n)_{n\in\mathbb N}, (z_n)_{n\in\mathbb N}\in M\)` we have
`\[\begin{array}{rcll}
(x\cdot y)\cdot z&=&[((x_n)_{n\in\mathbb N}+ I)\cdot ((y_n)_{n\in\mathbb N}+ I)]\cdot ((z_n)_{n\in\mathbb N}+I)&\text{by definition of real numbers}\\
&=&[((x_n)_{n\in\mathbb N}\cdot (y_n)_{n\in\mathbb N})+ I]\cdot ((z_n)_{n\in\mathbb N}+I)&\text{by definition of multiplying real numbers}\\
&=&[((x_n)_{n\in\mathbb N}\cdot (y_n)_{n\in\mathbb N})\cdot (z_n)_{n\in\mathbb N}+I]&\text{by definition of multiplying real numbers}\\
&=&[(x_n)_{n\in\mathbb N}\cdot  ((y_n)_{n\in\mathbb N}\cdot  (z_n)_{n\in\mathbb N})+I]&\text{by associativity of multiplying rational Cauchy sequences}\\
&=&((x_n)_{n\in\mathbb N}+ I) \cdot  [(y_n)_{n\in\mathbb N})\cdot  (z_n)_{n\in\mathbb N}+I]&\text{by definition of multiplying real numbers}\\
&=&((x_n)_{n\in\mathbb N}+ I) \cdot  [((y_n)_{n\in\mathbb N})+ I) \cdot ((z_n)_{n\in\mathbb N}+I)]&\text{by definition of multiplying real numbers}\\
&=&x\cdot (y\cdot z)&\text{by definition of real numbers}\\
\end{array}\]`
