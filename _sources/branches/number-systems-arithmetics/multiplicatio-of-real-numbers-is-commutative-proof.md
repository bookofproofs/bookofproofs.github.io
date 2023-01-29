layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1535
orderid: 50
parentid: bookofproofs$38
title: 
description:  Proof of MULTIPLICATION OF REAL NUMBERS IS COMMUTATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: commutative,multiplicatio,numbers,real,proof
contributors: bookofproofs

---


---

Let `\(x\)` and `\(y\)` be [real numbers, which by definition means ][bookofproofs$1105] that they are the equivalence classes `\[\begin{array}{rcl}x&:=&(x_n)_{n\in\mathbb N} + I,\\
y&:=&(y_n)_{n\in\mathbb N} + I.\end{array}\]`
In the above definition, `\((x_n)_{n\in\mathbb N}\)` and `\((y_n)_{n\in\mathbb N}\)` denote elements of the set `\(M\)` of all rational Cauchy sequences, which represent the real numbers `\(x\)` and `\(y\)`, while `\(I\)` denotes the set of all rational sequences, which converge to `\(0\)`.

The commutativity of the [multiplication of real numbers][bookofproofs$1532] `\(x\cdot y=y\cdot x\)` for all `\(x,y\in\mathbb R\)` follows from the [commutativity of multiplying rational Cauchy sequences][bookofproofs$1502]. For all rational Cauchy sequences `\((x_n)_{n\in\mathbb N}, (y_n)_{n\in\mathbb N}\in M\)` we have
`\[\begin{array}{rcll}
x\cdot y&=&((x_n)_{n\in\mathbb N}+ I)\cdot ((y_n)_{n\in\mathbb N}+ I)&\text{by definition of real numbers}\\
&=&[(x_n)_{n\in\mathbb N}\cdot  (y_n)_{n\in\mathbb N}]+ I&\text{by definition of multiplying real numbers}\\
&=&[(y_n)_{n\in\mathbb N}\cdot (x_n)_{n\in\mathbb N}]+ I&\text{by commutativity of multiplying rational Cauchy sequences}\\
&=&((y_n)_{n\in\mathbb N}+ I)\cdot ((x_n)_{n\in\mathbb N}+ I)&\text{by definition of multiplying real numbers}\\
&=&y\cdot x&\text{by definition of real numbers}\\
\end{array}\]`
